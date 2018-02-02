# -*- coding: utf-8 -*-


def compare_lists(list_1, list_2, info, file_pointer):
    """

    :param list_1: keys
    :param list_2: keys
    :param info:
    :param file_pointer:
    :return: True if keys are same False if not
    """
    difference1 = set(list_1) - set(list_2)
    difference2 = set(list_2) - set(list_1)
    if difference1:
        file_pointer.write('{difference} {meta} (Missing in Python end point)\n'.format(
            difference=difference1, meta=info))
    if difference2:
        file_pointer.write('{difference} {meta} (Missing in PHP end point)\n'.format(
            difference=difference2, meta=info))
    return True if difference1 or difference2 else False


def check_and_compare_lists(list1, list2, key, file_pointer):
    """

    :param list1:
    :param list2:
    :param key: key which is having the list in boht apis
    :param file_pointer: file in which we save output
    :return: Similarity check
    """
    try:
        if len(list1) == 0 and len(list2) == 0:
            return
    except Exception as exception:
        file_pointer.write('An expception occurred {e}\n'.format(e=exception))
        return
    if key == 'outlets':
        id1 = []
        id2 = []
        for l1, l2 in zip(list1, list2):
            id1.append(l1['id'])
            id2.append(l2['id'])
        id1.sort()
        id2.sort()
    monitoring_list1 = all(isinstance(x, (int, bool, str, float)) for x in list1)
    monitoring_list2 = all(isinstance(x, (int, bool, str, float)) for x in list2)
    monitoring_dict_list1 = all(isinstance(x, (dict)) for x in list1)
    monitoring_dict_list2 = all(isinstance(x, (dict)) for x in list2)
    do_not_sort = False
    if monitoring_dict_list1 and monitoring_dict_list2:
        if key != 'merchant_attributes':
            try:
                keys = None
                try:
                    keys = 'id' if 'id' in list1[0] else 'offer_id'
                except:
                    pass
                if key == 'outlets':
                    keys = 'id'
                if key == 'attributes':
                    keys = 'key'
                if key == 'offers':
                    keys = 'product_id'
                if key == 'products':
                    keys = 'sort_order' if 'sort_order' in list1[0] else 'id'
                if key == 'home_sections':
                    keys = 'identifier'
                if key == 'tiles':
                    keys = 'tile_id' if 'tile_id' in list1[0] else 'identifier'
                if key == 'hotels': # only for home call
                    file_pointer.write('** Going to skip sorting for {key} ** '
                                       'as no available sorting option is present\n'.format(key=key))
                    do_not_sort = True
                if not do_not_sort and keys:
                    file_pointer.write(
                        '-- {key} is going to be sorted on the basic of {keys} --\n'.format(
                            key=key, keys=keys))
                    from operator import itemgetter
                    list1 = sorted(list1, key=itemgetter(keys))
                    list2 = sorted(list2, key=itemgetter(keys))
            except:
                file_pointer.write('** Going to skip sorting for {key} ** '
                                   'as no available sorting option is present\n'.format(key=key))
                return False

    if not monitoring_list1 and not monitoring_list2 and len(list1) == len(list2):
        for val1, val2 in zip(list1, list2):
            if type(val1) == type(val2):
                if isinstance(val1, (list, set)):
                    check_and_compare_lists(val1, val2, file_pointer)
                elif isinstance(val1, (dict)):
                    correct_result = compare_data(val1, val2, file_pointer)
                    if not correct_result:
                        pass
            else:
                file_pointer.write('Type of {val1} in PHP does not match with {val2} in python\n'.format(
                    val1=val1, val2=val2))
    elif len(list1) != len(list2):
        file_pointer.write(
            'Length of {key} do not match so can not be checked length of both lists are {php_length} in PHP'
            ' and {python_length} in python\n'.format(
            key=key, php_length=len(list1), python_length=len(list2)))
    else:
        compare_lists(list1, list2, 'element not present in comparision of list for attribute:' + key, file_pointer)


def compare_data(dict1, dict2, file_pointer):
    """

    :param dict1: Dictionary 1
    :param dict2: Dictionary 2
    :param file_pointer: File to save logs in
    :return: Similarity status
    """
    correct_status = True
    compare_lists(dict1.keys(), dict2.keys(), 'difference in keys of document', file_pointer)

    for key,value in dict1.items():
        if key == 'cmd':
            continue
        try:
            if type(value) != type(dict2[key]):
                file_pointer.write('Value types do not match for attribute: {key},'
                                   ' clash is between {type1} in PHP and {type2} in Python)\n'.format(
                    key=key, type1=type(value), type2=type(dict2[key])))
        except Exception as exception:
            file_pointer.write('An expception occured {e}\n'.format(e=exception))
        if isinstance(value, (int, str, float, bool)):
            try:
                if value != dict2[key]:
                    correct_status = False
                    file_pointer.write('Value do not match for attribute: {key},'
                                       ' clash is between {value1} in PHP and {value2} in Python\n'.format(
                        key=key, value1=value, value2=dict2[key]))
            except Exception as exception:
                file_pointer.write('An expception occurred {e}\n'.format(e=exception))
        elif isinstance(value, (list, set)):
            try:
                check_and_compare_lists(value, dict2[key], key, file_pointer)
            except Exception as exception:
                file_pointer.write('An expception occurred {e}\n'.format(e=exception))
        elif isinstance(value, dict):
            correct_result = compare_data(value, dict2[key], file_pointer)
            if not correct_result:
                pass
    return correct_status


def compare_data_dictionaries(dict1, dict2, file_pointer):
    """
    This function is required because other function is being called recursively.
    :param dict1: passing to other function
    :param dict2: passing to other function
    :param file_pointer: passing to other function
    :return: Comparision of the dictionaries
    """
    return compare_data(dict1=dict1, dict2=dict2, file_pointer=file_pointer)

