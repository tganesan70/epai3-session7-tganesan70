#
# Python code for EPAi3-session-7 assignment on closure and free variables
#
# Ganesan Thiagarajan

def check_doc_string(
        fn: 'Function name that needs to be parsed') -> 'Returns whether the function has 50 words of descrition in its docstring or not':
    '''
    This function checks whether the function passed on to this has atleast 50 words of
    description.
    :param fn: Function name that is passed to this function
    :return: Returns a closure which allows the free variables can be accessed later
             The inner function Returns True if it has 50 or more words in its docstring description, else False
    Question: Will the docstring include the argument description function as well?  A BIG NO!
    '''

    '''
    Second set of comments not included in the docstring - add the long descriptions here
    '''
    comment_len = 50

    def inner_func(*args, **kwargs):
        '''
        Doc string for inner function
        :param args: Positional arguments for the function
        :param kwargs:Function arguments for the function
        :return: The function output
        '''
        if fn.__doc__ is None:
            return False
        else:
            fn_doc_string = fn.__doc__.split(sep=" ")
        print(f'No. of words in the docstring comment for {fn.__name__}() is : {len(fn_doc_string)}')
        if len(fn_doc_string) < comment_len:
            return False
        else:
            return True

    return inner_func


def dummy_func():
    '''
    This is a dummy function to check whether the check_doc_string() function fails correctly.
    :return: None
    '''
    pass


# Define a new function which calls the closure with free variable comment_len (default = 50) for any function
def check_for_doc_string(*args):
    '''
    Wrapper function for the closure returned by check_doc_string()
    :param args: function name
    :return: True if comment length > 50 else false
    '''
    return check_doc_string(*args)()


def fibanocci_seq():
    '''
    Generate the Fibanocci sequence 0,1,1,2,3,5,8,13,21
    :return: Returns the function closure so that free variables can be accessed
    '''
    old1 = 0     # Default state 1 variable
    old2 = 0     # Default state 2 variable
    counter = 0  # How many times this function is called -- extra variable for future use

    def next():
        '''
        Creates the Fibanocci sequence using the free and nonlocal variables old1 and old2
        :return: Next value in the Fibanocci sequence
        '''
        nonlocal old1, old2, counter
        counter += 1
        if old1 == 0 and old2 == 0:
            old2 = 1
        else:
            old1, old2 = old2, old1 + old2
        return old1

    return next


counters = dict()

# Function to count the number of times a function is called
def counter(func):
    '''
    Function to count the number of times a function "func" is called
    :param func: function name
    :return: The closure for accessing the free variable count
           : The inner function in turn returns the return value of the function called
    '''
    count = 0               # initialize the function call counter value

    def inner(*args, **kwargs):
        '''
        Doc string for inner function
        :param args: Positional arguments for the function
        :param kwargs:Function arguments for the function
        :return: The function output
        '''
        nonlocal count
        count +=  1
        counters[func.__name__] = count  # counters is global
        #print(f'Function {func.__name__} is called {count} times so far')
        return func(*args, **kwargs)
    return inner

def add(a, b):
    '''
    Add two numbers a and b
    :param a: addition argument 1
    :param b: addition argument 2
    :return: the sum a+b
    '''
    return a + b

def mul(a, b):
    '''
    Product of two numbers a and b
    :param a: multiplication argument 1
    :param b: multiplication argument 2
    :return: the product a*b
    '''
    return a*b

def div(a, b):
    '''
    Division of two numbers a and b
    :param a: Division argument 1
    :param b: Division  argument 2
    :return: the divsion a/b when b != 0 else returns None
    '''
    if b != 0:
        return a/b
    else:
        return None


counters_dict = dict()    # Global dictionary to store counter values for each function
def counter_new(func):
    '''
    Function to count the number of times a function "func" is called and the count is stored in a
    global dictionary called counters_dict
    :param func: function name
    :return: The closure for accessing the free variable count
           : The inner function in turn returns the return value of the function called
    '''
    count = 0  # initially fn has been run zero times

    def inner(*args, **kwargs):
        '''
        Doc string for inner function
        :param args: Positional arguments for the function
        :param kwargs:Function arguments for the function
        :return: The function output
        '''
        nonlocal count
        count += 1
        counters_dict[func.__name__] = count  # counters_dict is global
        return func(*args, **kwargs)

    return inner


def counter_new2(fun, func_dict):
    '''
    Function to count the number of times a function "func" is called and the count is stored in a
    dictionary func_dict passed as another argument
    :param func: function name
    :param func_dict: dictionary for storing the function counter value
    :return: The closure for accessing the free variable count
           : The inner function in turn returns the return value of the function called
    '''
    count = 0  # initially fn has been run zero times

    def inner(*args, **kwargs):
        '''
        Doc string for inner function
        :param args: Positional arguments for the function
        :param kwargs:Function arguments for the function
        :return: The function output
        '''
        nonlocal count
        count += 1
        func_dict[fun.__name__] = count  # counters is nonlocal
        return fun(*args, **kwargs)

    return inner

# End of file
