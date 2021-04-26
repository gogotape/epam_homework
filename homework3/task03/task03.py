# I decided to write a code that generates data filtering object from a list of keyword parameters:


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data if self.functions(item)
        ]  # found mistake in return


# example of usage:
positive_even = Filter(
    lambda a: a % 2 == 0 and a > 0 and isinstance(a, int)
)  # found mistake in lambda func
# positive_even.apply(range(100)) # should return only even numbers from 0 to 99


#   unsuccessful attempt to fix bugs in make_filter
def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(value):
            return key[value] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


#   so i wrote my own make_filter function
def my_own_make_filter(data, **kwargs):
    for dictionary in data:
        for key, value in kwargs.items():
            if key not in dictionary or value != dictionary[key]:
                continue
            else:
                return dictionary

    return None


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

# make_filter(name='polly', type='bird').apply(sample_data) #should return only second entry from the list
# print(make_filter(name='polly', type='bird').apply(sample_data))
# There are multiple bugs in this code. Find them all and write tests for faulty cases.


print(positive_even.apply(range(100)))
print(my_own_make_filter(sample_data, name="polly", type="bird"))
