## Main test code starts here for pynotes file generation

# Add test cases
# define the new functions using a closure and different functions
test_for_doc_string_len1 = check_doc_string(check_doc_string)
test_for_doc_string_len2 = check_doc_string(dummy_func)
test_for_doc_string_len3 = check_doc_string(print)

# Test case 1
print(f'Doc string for function {check_doc_string.__name__} is: {check_doc_string.__doc__}')
print('Does it have comment words more than 50?')
print(test_for_doc_string_len1())

# Test case 2
print(f'Doc string for function {dummy_func.__name__} is: {dummy_func.__doc__}')
print('Does it have comment words more than 50?')
print(test_for_doc_string_len2())

# Test case 3
print(f'Doc string for function {print.__name__} is: {print.__doc__}')
print('Does it have comment words more than 50?')
print(test_for_doc_string_len3())

# Test case 4 -> Check for built-in functions: e.g., print, type, etc.
print(check_for_doc_string(print))
# Test case 5 -> Check for dummy function known to fail the test
print(check_for_doc_string(dummy_func))
# Test case 6 -> Check for valid function known to fail the test
print(check_for_doc_string(check_for_doc_string))
# Test case 7 -> Check it on the closure function itself
print(check_for_doc_string(check_doc_string))


# test case for Fibanocci sequence generation
fibanocci = fibanocci_seq()  # define the new function using the closure
# Test case 8 -> Check the values in the sequence
print(fibanocci())           # Run the function to generate the 1st number
print(fibanocci())           # Run the function to generate the 2nd number
print(fibanocci())           # Run the function to generate the 3rd number
print(fibanocci())           # Run the function to generate the 4th number
print(fibanocci())           # Run the function to generate the 5th number
print(fibanocci())           # Run the function to generate the 6th number
print(fibanocci())           # Run the function to generate the 7th number
print(fibanocci())           # Run the function to generate the 8th number

# Test the function counter closure function
add = counter(add)     # Create a new counter augmented addition
mul = counter(mul)     # Create a new counter augmented multiplication
div = counter(div)     # Create a new counter augmented division
print(add(1, 2))
print(add(4, 5))
print(mul(1, 2))
print(counters)
print(mul(4, 5))
print(div(1, 2))
print(div(4, 5))
print(div(4, 0))

# Test the function new counter closure function
add_new = counter_new(add)     # Create a new counter augmented addition
mul_new = counter_new(mul)     # Create a new counter augmented multiplication
div_new = counter_new(div)     # Create a new counter augmented division
print(add_new(1, 2))
print(add_new(4, 5))
print(mul_new(1, 2))
print(mul_new(4, 5))
print(div_new(1, 2))
print(div_new(4, 5))
print(div_new(4, 0))
print(counters_dict)

# Test the function new counter closure function
add_dict = dict()
mult_dict = dict()
div_dict = dict()
add_new = counter_new2(add, add_dict)     # Create a new counter augmented addition
mul_new = counter_new2(mul, mult_dict)     # Create a new counter augmented multiplication
div_new = counter_new2(div, div_dict)     # Create a new counter augmented division
print(add_new(1, 2))
print(add_new(4, 5))
print(mul_new(1, 2))
print(mul_new(4, 5))
print(div_new(1, 2))
print(div_new(4, 5))
print(div_new(4, 0))
print(add_dict)
print(mult_dict)
print(div_dict)
