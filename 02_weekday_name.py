def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    WEEKDAY_NAMES = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }

    return WEEKDAY_NAMES.get(day_of_week)

print("should be Sunday", weekday_name(1))
print("should be Saturday", weekday_name(7))
print("should be Monday", weekday_name(2))
print("should be Friday", weekday_name(6))
print("should be None", weekday_name(9))
print("should be None", weekday_name(0))