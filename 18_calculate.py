def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, raise error:

        >>> calculate('foo', 2, 3)
        Traceback (most recent call last):
          ...
        ValueError: Invalid Operation
    """

    # if we dont have a valid opertaion of add', 'subtract', 'multiply', or 'divide'
        # raise an error of valueError invalid operation 
    operations = ['add', 'subtract', 'multiply', 'divide']

    if operation not in operations:
        raise ValueError("Invalid Operation")
        
    
    # if we have add 
        # if makeInt is true
            # we return the msg int(a+b)
        # else 
            # we return the msg a+b
    if operation == "add":
        if make_int == True:
            return f"{message} {int(a+b)}"
        else:
            return f"{message} {a+b}" 

    # if we have subtract
        # if makeInt is true
            # we return the msg int(a-b)
        # else 
            # we return the msg a-b

    if operation == "subtract":
        if make_int == True:
            return f"{message} {int(a-b)}"
        else:
            return f"{message} {a-b}" 

    # if we have multiply
        # if makeInt is true
            # we return the msg int(a*b)
        # else 
            # we return the msg a*b
    if operation == "multiply":
        if make_int == True:
            return f"{message} {int(a*b)}"
        else:
            return f"{message} {a*b}"

    # if we have divide 
        # if makeInt is true
            # we return the msg int(a/b)
        # else 
            # we return the msg a/b
    if operation == "divide":
        if make_int == True:
            return f"{message} {int(a/b)}"
        else:
            return f"{message} {a/b}"
    