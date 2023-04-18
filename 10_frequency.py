def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """

    return lst.count(search_term)


print("should be 3", frequency([1, 4, 3, 4, 4], 4))
print("should be 0", frequency([1, 4, 3], 7))