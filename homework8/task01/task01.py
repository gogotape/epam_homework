import re


class KeyValueStorage(dict):
    """A wrapper class for key value storage"""

    def __init__(self, file_path):
        super().__init__()

        self.file_path = file_path

        with open(self.file_path) as fi:
            for line in fi.readlines():

                key, value = line.split("=")

                if key in dir(
                    self
                ):  # if key clash existing built-in attributes take precedence
                    continue
                if re.match(
                    r"\d", key
                ):  # In case when key cannot be assigned to an attribute, ValueError is dropping
                    raise ValueError
                else:
                    try:
                        self[key] = int(value[:-1])
                        setattr(self, key, int(value[:-1]))
                    except ValueError:
                        self[key] = value[:-1]
                        setattr(self, key, value[:-1])
