import sqlite3 as sq


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.counter = 0

        conn = sq.connect(database_name)
        self.cursor = conn.cursor()

    def __len__(self):
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.table_name} QUERY")
        length = self.cursor.fetchone()
        return length[0]

    def __getitem__(self, item):
        self.cursor.execute(
            f'SELECT * FROM {self.table_name} WHERE NAME = "{item}" LIMIT 1'
        )
        return self.cursor.fetchone()

    def __iter__(self):
        return self

    def __next__(self):
        if (
            self.counter
            < self.cursor.execute("SELECT COUNT(*) from presidents").fetchone()[0]
        ):
            self.counter += 1
            return self.cursor.execute(
                f"SELECT * from {self.table_name} LIMIT 1 OFFSET {self.counter-1}"
            ).fetchall()
        else:
            raise StopIteration

    def __contains__(self, item):
        data = self.cursor.execute(f"SELECT * FROM {self.table_name}").fetchall()
        for row in data:
            if row[0] == item:
                return True
        else:
            return False


if __name__ == "__main__":
    presidents = TableData("example.sqlite", "presidents")
    print(len(presidents))
    print(presidents["Yeltsin"])
    print("Yeltsin" in presidents)
