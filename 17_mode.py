def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # most variable set to 0
    # loop through list
        # use count method on each el of list 
            # return value of count on cur num is greater than most 
            # then reassign most to current num
    # then return most 

    most = 0
    for num in nums:
        if nums.count(num) > most: 
            most = num
    
    return most 
