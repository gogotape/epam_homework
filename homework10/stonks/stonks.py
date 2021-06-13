import json
import time
from ast import literal_eval
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import RLock

import requests
from bs4 import BeautifulSoup

MAIN_URL = "https://markets.businessinsider.com"
SNP_500_URL = "https://markets.businessinsider.com/index/components/s&p_500?p="
all_urls_of_companies = list()
all_htmls_of_companies = list()
all_htmls_of_main_pages = list()
all_companies = dict()
lock = RLock()


def get_dollar_exchange_rate() -> float:
    rates = requests.get("https://www.cbr.ru/scripts/XML_daily.asp").text
    soup = BeautifulSoup(rates, "lxml")
    dollar_rate = float(soup.find(text="Доллар США").next.text.replace(",", "."))
    return dollar_rate


def get_html(url: str) -> str:
    resp = requests.get(url)
    return resp.text


def get_all_urls_of_main_pages() -> list:
    all_urls_of_pages = [SNP_500_URL + str(i) for i in range(1, 12)]
    return all_urls_of_pages


def add_html_to_all_htmls_of_main_pages(url):
    html = get_html(url)
    all_htmls_of_main_pages.append(html)


def add_html_to_all_htmls_of_companies(url):
    html = get_html(url)
    all_htmls_of_companies.append(html)


def add_urls_from_main_page_to_all_urls(url: str):
    global all_urls_of_companies
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")
    tds = soup.find("table", class_="table table__layout--fixed").find_all(
        "td", class_="table__td table__td--big"
    )
    urls = [MAIN_URL + td.find("a").get("href") for td in tds]
    all_urls_of_companies.extend(urls)


def get_company_data_from_company_page(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    try:
        name = soup.find("span", class_="price-section__label").text.strip()
        short_name = (
            soup.find("title")
            .text.strip()
            .split("|")[1]
            .replace(" Stock Price Today ", "")
            .replace(".", "")[1:]
        )

        company_code = soup.find("title").text.split()[0]
        current_price = float(
            soup.find("div", class_="snapshot__data-item")
            .text.strip()
            .split()[0]
            .replace(",", "")
        )

        out = soup.find_all(class_="snapshot__data-item")
        price_of_company = float(out[2].text.strip().split()[0].replace(",", ""))
        high_week_52 = float(out[7].text.strip().split()[0].replace(",", ""))
        low_week_52 = float(out[6].text.strip().split()[0].replace(",", ""))
        pe = float(out[8].text.strip().split()[0].replace(",", ""))

    except:
        print("There are some problems with parsing!")
        name = short_name = company_code = ""
        current_price = high_week_52 = low_week_52 = pe = price_of_company = 0

    data = (
        str(name)
        + "***"
        + str(
            {
                "name": name,
                "short_name": short_name,
                "code": company_code,
                "price_of_company": price_of_company,
                "current_price": current_price,
                "high_week_52": high_week_52,
                "low_week_52": low_week_52,
                "pe": pe,
            }
        )
    )

    return data


def write_company_growth_info_to_txt(html: str):
    soup = BeautifulSoup(html, "lxml")

    company_names = soup.find_all("td", class_="table__td table__td--big")

    holder = soup.find_all("td", class_="table__td")
    company_growths = [
        holder[i].text.strip().split()[-1] for i in range(7, len(holder), 8)
    ]

    with open("temporary_files/companies_growth.txt", "a", encoding="utf-8") as fi:
        for name, growth in zip(company_names, company_growths):
            try:
                fi.write(str(name.text.strip().upper()) + "***" + str(growth + "\n"))
            except:
                print(
                    f"Some problems with getting growth for company {name.text.strip()}, skipped"
                )


def write_to_txt_main_company_info(html: str):
    data = get_company_data_from_company_page(html)
    with lock:
        with open("temporary_files/stocks_info.txt", "a", encoding="utf-8") as fi:
            fi.write(str(data) + "\n")
            #   print(data.split("***")[0], "successfully processed")


def create_dict_with_all_companies_data(file: str):
    global all_companies
    with open(file) as fi:
        for line in fi.readlines():
            try:
                company_name, company_data = line.strip().split("***")
                all_companies[company_name] = literal_eval(company_data)
                all_companies[company_name][
                    "potential_profit"
                ] = calculate_potential_profit(company_name)
            except:
                print(
                    f"There is some problem with {company_name} while making dict with all companies data!"
                )


def calculate_potential_profit(company_name: str) -> float:
    global all_companies
    potential_profit = round(
        (
            float(all_companies[company_name]["high_week_52"])
            / float(all_companies[company_name]["low_week_52"])
            - 1
        )
        * 100,
        2,
    )
    return potential_profit


def create_dict_with_growths_of_companies() -> dict:
    with open("temporary_files/companies_growth.txt", encoding="utf-8") as fi:
        growth_dict = {
            line.split("***")[0]: float(line.split("***")[-1][:-2])
            for line in fi.readlines()
        }
        return growth_dict


def add_property_of_growth_to_company(growth_dict: dict):
    global all_companies
    for key, value in all_companies.items():
        if value["short_name"] in growth_dict:
            all_companies[key]["growth_of_company"] = growth_dict[value["short_name"]]
        else:
            all_companies[key]["growth_of_company"] = 0


def find_top_10_companies_by_key(data: dict, key: str, reverse=True) -> list:
    result = sorted(data.values(), key=lambda x: float((x[key])), reverse=reverse)[:10]
    return result


def main():
    start = time.time()

    #   clearing of temporary files
    open("temporary_files/companies_growth.txt", "w", encoding="utf-8").close()
    open("temporary_files/stocks_info.txt", "w", encoding="utf-8").close()

    dollar_rate = get_dollar_exchange_rate()
    print("Dollar rate:", dollar_rate)

    all_urls_of_main_pages = get_all_urls_of_main_pages()
    print(f"Got {len(all_urls_of_main_pages)} urls of main pages")

    with ThreadPoolExecutor() as pool:
        pool.map(add_html_to_all_htmls_of_main_pages, all_urls_of_main_pages)
    print(f"Saved {len(all_urls_of_main_pages)} htmls of main pages")

    print("Starting process of getting all urls for companies...")
    with ThreadPoolExecutor() as pool:
        pool.map(add_urls_from_main_page_to_all_urls, all_urls_of_main_pages)
    print(f"Successfully got {len(all_urls_of_companies)} urls for companies")

    print("Getting all htmls for companies...")
    with ThreadPoolExecutor() as pool:
        pool.map(add_html_to_all_htmls_of_companies, all_urls_of_companies)
    print(f"Successfully got {len(all_urls_of_companies)} htmls for companies")

    print("Processing all htmls...")
    with ProcessPoolExecutor() as pool:
        pool.map(write_to_txt_main_company_info, all_htmls_of_companies)

    print("Processing all htmls of main pages for saving growth info...")
    with ProcessPoolExecutor() as pool:
        pool.map(write_company_growth_info_to_txt, all_htmls_of_main_pages)

    create_dict_with_all_companies_data("temporary_files/stocks_info.txt")
    add_property_of_growth_to_company(create_dict_with_growths_of_companies())

    with open("output/top_10_current_price.json", "w") as fi:
        json.dump(
            find_top_10_companies_by_key(all_companies, "current_price"), fi, indent=3
        )

    with open("output/lower_10_pe.json", "w") as fi:
        json.dump(
            find_top_10_companies_by_key(all_companies, "pe", reverse=False),
            fi,
            indent=3,
        )

    with open("output/top_10_growth.json", "w") as fi:
        json.dump(
            find_top_10_companies_by_key(all_companies, "growth_of_company"),
            fi,
            indent=3,
        )

    with open("output/top_10_potential_profit.json", "w") as fi:
        json.dump(
            find_top_10_companies_by_key(all_companies, "potential_profit"),
            fi,
            indent=3,
        )

    print("---Json's successfully saved in /output---")
    print("Program time:", round(time.time() - start), "seconds")


if __name__ == "__main__":
    main()
