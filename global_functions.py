from django.core.serializers.python import Serializer

# check if two model object is same of different
def is_same(obj1, obj2, excluded_keys=[]):
    # make dictionary from objects
    d1, d2 = obj1.__dict__, obj2.__dict__
    # loop according to keys and values in first object
    for k, v in d1.items():
        # if passed special excluded keys, or those key always different , so we don't want make result different
        # _state, _django_cleanup_original_cache: belongs to django timestamp, creator_id: belongs to our models,
        # timestamp always will be different, but creator some time will be same and most time different
        if k in excluded_keys or k in ['_state', '_django_cleanup_original_cache', 'timestamp', 'creator_id']:
            # continue to check next key
            continue

        if v != d2[k]:
            # if found first value different to a key then don't check more and return false result
            return False
        else:
            # continue to check next key
            continue

    # after all keys checked and not found any different then return true
    return True


# for cleaning model to json data and change pk to id
class CleanSerializer(Serializer):
    def end_object( self, obj ):
        self._current['id'] = obj._get_pk_val()
        self.objects.append( self._current )
