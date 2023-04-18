def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # TODO: try .get()
    result = {}
    for ltr in phrase:
        if ltr not in result:
            result[ltr] = 1
        else: 
            result[ltr] += 1
    
    return result




print("should be {'y': 2, 'a': 1}:",  multiple_letter_count('yay'))
print("should be {'Y': 1, 'a': 1, 'y': 1}:", multiple_letter_count('Yay'))