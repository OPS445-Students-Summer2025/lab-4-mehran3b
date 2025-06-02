#!/usr/bin/env python3

def create_dictionary(keys, values):
    result = {}
    i = 0
    while i < len(keys):
        result[keys[i]] = values[i]
        i += 1
    return result

def shared_values(dict1, dict2):
    return set(dict1.values()) & set(dict2.values())

if __name__ == '__main__':
    list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
    list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']
    dict_york = {
        'Address': '70 The Pond Rd', 'City': 'Toronto',
        'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'
    }
    dict_newnham = {
        'Address': '1750 Finch Ave E', 'City': 'Toronto',
        'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'
    }
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
