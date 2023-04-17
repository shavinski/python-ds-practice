def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> nums = [1, 2, 3]
        >>> last_element(nums)
        3
        >>> last_element([]) is None
        True

    Make sure original list has not been mutated:

        >>> nums == [1, 2, 3]
        True
    """
    if len(lst) == 0:
        return None
    return lst[-1]

nums = [1, 2, 3]
print("should be 3", last_element(nums))
print("should be true", nums == [1, 2, 3])
print("should be None", last_element([]))