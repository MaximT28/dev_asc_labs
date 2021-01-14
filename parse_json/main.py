from data_to_parse import *


class FindKey:
    def __init__(self):
        self.json = ""
        self.key = ""
        self.type = None
        self.err = "not found"

    def _is_expected_key(self, key, value):

        final_value = self.key == key  # check that the keys are the same
        if self.type is None:  # check the type of value if specified
            return final_value
        elif isinstance(self.type, type):  # check if its a type (list, dict...) and not ({},[]...)
            return final_value and isinstance(value, self.type)
        else:  # otherwise its a [] or {} or ...
            return final_value and isinstance(value, type(self.type))

    def _switch_type(self, my_object):
        if isinstance(my_object, dict):
            return self._parse_dict(my_object)
        elif isinstance(my_object, list):
            return self._parse_list(my_object)
        else:
            return False

    def _parse_dict(self, my_dict):
        for k, v in my_dict.items():
            # print(k)
            if self._is_expected_key(k, v):  # verify if current key is equal with given
                print(str(v)[:50])  # print first 50 chars
                return True
            else:
                if self._switch_type(v):  # check the type of value
                    return True
        return False

    def _parse_list(self, my_list):
        for item in my_list:
            # print(item)
            if self._switch_type(item):  # check the type of item
                return True
        return False

    def search(self, json, my_key, my_type=None):
        self.json = json
        self.key = my_key
        self.type = my_type
        return self._switch_type(self.json)  # check the type of json


def something():
    pass


if __name__ == "__main__":
    # print(isinstance([], type))
    test_key1 = FindKey().search(my_json, key1, [])
    test_key2 = FindKey().search(my_json, key2, [])
    print(f'Found key {key1}: {test_key1}')
    print(f'Found key {key2}: {test_key2}')
