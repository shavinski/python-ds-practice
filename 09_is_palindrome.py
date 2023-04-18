def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_no_caps_no_space = phrase.lower().replace(" ", "", -1)[::-1]

    # print("palindrome==>", phrase_no_caps_no_space, "phrase==>", phrase)

    return phrase_no_caps_no_space == phrase.lower().replace(" ", "", -1)

    # return phrase.reverse() == phrase

print("should be True", is_palindrome('tacocat'))
print("should be True", is_palindrome('noon'))
print("should be False", is_palindrome('robert'))

print("should be True", is_palindrome('taco cat'))
print("should be True", is_palindrome('Noon'))
