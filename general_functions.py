def compare_if_is_same(obj1, obj2, excluded_keys):
    d1, d2 = obj1.__dict__, obj2.__dict__
    for k, v in d1.items():
        # print('check key: ' + k)
        if k in excluded_keys or k in ['_state', '_django_cleanup_original_cache']:
            # _state make difference so automatically exclude it
            # print(k + ' is in excluded keys')
            continue

        if v != d2[k]:
            # print('value in not equal in second object')
            return False
        else:
            # print('it is same')
            continue

    # print('all keys checked, so both object is same')
    return True
