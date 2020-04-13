# https://www.codewars.com/kata/56f411dc9821795fd90011d9/python
class UnexpectedTypeException(BaseException):
    pass

def expected_type(return_types):
    """Check if decorated function returns object of return_types or raise UnexpectedTypeException.
    
    Example:
    
    @expected_type((str))
    def return_something(input):
        # do stuff here with the input...
        return something
    
    >>> return_something('The quick brown fox jumps over the lazy dog.')
    'The quick brown fox jumps over the lazy dog.'

    >>> return_something('The quick brown fox jumps over the lazy dog.')
    'Maybe you'll output another string...'
    
    >>> return_something(None)
    UnexpectedTypeException: Was expecting instance of: str
    
    """
    def decorator_repeat(func):
        def wrapper_func(*args, **kwargs):  
                value = func(*args, **kwargs)
                if isinstance(value, return_types):
                    pass
                else:
                    raise UnexpectedTypeException    
                return value               
        return wrapper_func
    return decorator_repeat