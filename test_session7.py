#
# Python test code using pytest environment for auto-testing functions in session7 module
#

import session7
import pytest
import os
import inspect
import re

# Check for Readme's presence
def test_session7_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

# Check for contents in readme file
def test_session7_readme_500_words():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

# Test the number of # comments in the readme file
def test_session7_readme_file_for_more_than_10_hashes():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "More detailed \# comments needed"

# Test for use of capital letters in function names
def test_session7_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

# Test the docstring of built-in function print
def test_session7_check_doc_string1():
    assert session7.check_for_doc_string(print) == True, "Wrong - print function has good documentation"

# Test the docstring of dummy function
def test_session7_check_doc_string2():
    assert session7.check_for_doc_string(session7.dummy_func) == False, "Wrong - Dummy function has bad documentation"

# Test the docstring of docstring check function itself
def test_session7_check_doc_string3():
    assert session7.check_for_doc_string(session7.check_doc_string) == True, "Wrong - check_doc_string function has good documentation"

def test_session7_check_doc_string4():
    assert session7.check_for_doc_string(session7.check_for_doc_string) == False, "Wrong - check_for_doc_string function no documentation"

# test for initialization of the Fibanocci sequence generator
def test_session7_fibanocci1():
    fibanocci = session7.fibanocci_seq()  # define the new function using the closure
    value = fibanocci()
    assert value == 0, "Fibanocci sequence starting trouble -- check"

# test for second value in the Fibanocci sequence
def test_session7_fibanocci2():
    fibanocci = session7.fibanocci_seq()  # define the new function using the closure
    value = fibanocci()
    value = fibanocci()
    assert value == 1, "Fibanocci sequence 1st trouble -- check"

# test for third value in the Fibanocci sequence
def test_session7_fibanocci3():
    fibanocci = session7.fibanocci_seq()  # define the new function using the closure
    value = fibanocci()
    value = fibanocci()
    value = fibanocci()
    assert value == 1, "Fibanocci sequence 2nd trouble -- check"

# test for fourth value in the Fibanocci sequence
def test_session7_fibanocci4():
    fibanocci = session7.fibanocci_seq()  # define the new function using the closure
    value = fibanocci()
    value = fibanocci()
    value = fibanocci()
    value = fibanocci()
    assert value == 2, "Fibanocci sequence 3rd trouble -- check"

# test for sixth value in the Fibanocci sequence
def test_session7_fibanocci5():
    fibanocci = session7.fibanocci_seq()  # define the new function using the closure
    value = fibanocci()
    value = fibanocci()
    value = fibanocci()
    value = fibanocci()
    value = fibanocci()
    value = fibanocci()
    assert value == 5, "Fibanocci sequence 6th term is not correct -- check"

# test for Empty dictionary
def test_session7_add_count0():
    session7.counters = dict()
    add = session7.counter(session7.add)  # Create a new counter augmented addition
    mul = session7.counter(session7.mul)  # Create a new counter augmented multiplication
    div = session7.counter(session7.div)  # Create a new counter augmented division
    assert session7.counters == {}, "Something wrong- No calls -- dictionary should be empty"

# test for right addition values and correct count in the dictionary for the right function
def test_session7_add_count1():
    session7.counters = dict()
    add = session7.counter(session7.add)  # Create a new counter augmented addition
    assert add(1,2) == 3, "Adder output is wrong"
    assert add(4,-4) == 0, "Adder output is wrong"
    assert session7.counters["add"] == 2, "Counter values for add function are wrong"
    # Test for invalid inputs
    #with pytest.raises(TypeError, match=r".* add() missing 2 required positional arguments: 'a' and 'b' .*"):
    #    session7.add()
    #with pytest.raises(TypeError, match=r".* add() missing 1 required positional argument: 'b' .*"):
    #    session7.add(1)

# test for right multiplication values and correct count in the dictionary for the right function,
# AND not in the unexecuted function
def test_session7_mul_count1():
    session7.counters = dict()
    mul = session7.counter(session7.mul)  # Create a new counter augmented multiplication
    assert mul(1,2) == 2, "Mult output is wrong"
    assert mul(4,-4) == -16, "Mult output is wrong"
    assert mul(4,0) == 0, "Mult output is wrong"
    assert (session7.counters["mul"] == 3) and ("add" not in session7.counters), "Counter values for mul function are wrong"
    # Test for invalid inputs
    #with pytest.raises(TypeError, match=r".* mul() missing 2 required positional arguments: 'a' and 'b' .*"):
    #    session7.mul()
    #with pytest.raises(TypeError, match=r".* mul() missing 1 required positional argument: 'b' .*"):
    #    session7.mul(1)

# Test for the division operation and division by zero error
def test_session7_div_count1():
    session7.counters = dict()
    div = session7.counter(session7.div)  # Create a new counter augmented division
    assert div(1,2) == 0.5, "division output is wrong"
    assert div(4,5) == 0.8, "division output is wrong"
    assert div(4,-4) == -1, "division output is wrong"
    assert div(2,0) == None, "division output is wrong"
    assert session7.counters["div"] == 4, "Counter values for div function are wrong"
    # Test for invalid inputs
    #with pytest.raises(TypeError, match=r".* div() missing 2 required positional arguments: 'a' and 'b' .*"):
    #    session7.div()
    #with pytest.raises(TypeError, match=r".* div() missing 1 required positional argument: 'b' .*"):
    #    session7.div(1)

# Test for the division and multiplication operations
def test_session7_mul_div_count1():
    session7.counters = dict()
    div = session7.counter(session7.div)  # Create a new counter augmented division
    mul = session7.counter(session7.mul)  # Create a new counter augmented division
    assert div(1,2) == 0.5, "division output is wrong"
    assert div(4,5) == 0.8, "division output is wrong"
    assert div(4,-4) == -1, "division output is wrong"
    assert div(2,0) == None, "division output is wrong"
    assert mul(4,-4) == -16, "Mult output is wrong"
    assert mul(4,0) == 0, "Mult output is wrong"
    assert (session7.counters["div"] == 4) and (session7.counters["mul"] == 2), "Counter values for div function are wrong"

# Test for the all three operations
def test_session7_add_mul_div_count1():
    session7.counters = dict()
    add = session7.counter(session7.add)  # Create a new counter augmented division
    div = session7.counter(session7.div)  # Create a new counter augmented division
    mul = session7.counter(session7.mul)  # Create a new counter augmented division
    assert add(1,2) == 3, "Adder output is wrong"
    assert div(1,2) == 0.5, "division output is wrong"
    assert div(4,5) == 0.8, "division output is wrong"
    assert div(4,-4) == -1, "division output is wrong"
    assert div(2,0) == None, "division output is wrong"
    assert mul(4,-4) == -16, "Mult output is wrong"
    assert mul(4,0) == 0, "Mult output is wrong"
    assert (session7.counters["div"] == 4) and (session7.counters["mul"] == 2) and (session7.counters["add"] == 1), "Counter values for div function are wrong"

# test for Empty dictionary in the new counter
def test_session7_add_new_count0():
    session7.counters_dict = dict()
    add = session7.counter_new(session7.add)  # Create a new counter augmented addition
    mul = session7.counter_new(session7.mul)  # Create a new counter augmented multiplication
    div = session7.counter_new(session7.div)  # Create a new counter augmented division
    assert session7.counters_dict == {}, "Something wrong- No calls -- dictionary should be empty"

# test for dictionary entry for add in the new counter dictionary
def test_session7_add_new_count1():
    session7.counters_dict = dict()  # Global dictionary to store counter values for each function
    add_new = session7.counter_new(session7.add)     # Create a new counter augmented addition
    assert add_new(1, 2) == 3, "Get your addition correct"
    assert add_new(4, 5) == 9, "Get your addition correct"
    assert session7.counters_dict["add"] == 2, "Wrong number of function counts"

# test for dictionary entry for mul in the new counter dictionary
def test_session7_mul_new_count1():
    session7.counters_dict = dict()  # Global dictionary to store counter values for each function
    mul_new = session7.counter_new(session7.mul)     # Create a new counter augmented multiplication
    assert mul_new(1, 2) == 2, "Get your multiplication correct"
    assert mul_new(4, 5) == 20, "Get your multiplication correct"
    assert session7.counters_dict["mul"] == 2, "Wrong number of function counts"

# test for dictionary entry for div in the new counter dictionary
def test_session7_div_new_count1():
    session7.counters_dict = dict()  # Global dictionary to store counter values for each function
    div_new = session7.counter_new(session7.div)     # Create a new counter augmented division
    assert div_new(1, 2) == 0.5, "Get your division correct"
    assert div_new(4, 5) == 0.8, "Get your division correct"
    assert div_new(4, 0) == None, "You can't divide by zero"
    assert session7.counters_dict["div"] == 3, "Wrong number of function counts"

# test for dictionary entry for div in the new counter dictionary
def test_session7_mul_div_new_count1():
    session7.counters_dict = dict()  # Global dictionary to store counter values for each function
    mul_new = session7.counter_new(session7.mul)     # Create a new counter augmented multiplication
    div_new = session7.counter_new(session7.div)     # Create a new counter augmented division
    assert mul_new(1, 2) == 2, "Get your multiplication correct"
    assert mul_new(4, 5) == 20, "Get your multiplication correct"
    assert div_new(1, 2) == 0.5, "Get your division correct"
    assert div_new(4, 5) == 0.8, "Get your division correct"
    assert div_new(4, 0) == None, "You can't divide by zero"
    assert (session7.counters_dict["div"] == 3) and (session7.counters_dict["mul"] == 2), "Wrong number of function counts"

# test for separate dictionary entry for add in the new counter2 dictionary
def test_session7_add_new_dict_count1():
    add_dict = dict()
    add_new = session7.counter_new2(session7.add, add_dict)     # Create a new counter augmented addition
    assert add_new(1, 2) == 3, "Nursery kid will beat you in math"
    assert add_new(4, 5) == 9, "Nursery kid will beat you in math"
    assert add_dict["add"] == 2, "Wrong count for add operation"

# test for separate dictionary entry for mul and div in the new counter2 dictionary
def test_session7_mul_new_dict_count1():
    mult_dict = dict()
    div_dict = dict()
    mul_new = session7.counter_new2(session7.mul, mult_dict)     # Create a new counter augmented multiplication
    assert mul_new(1, 2) == 2, "Primary school kid will beat you in math"
    assert mul_new(4, 5) == 20, "Primary school kid will beat you in math"
    div_new = session7.counter_new2(session7.div, div_dict)     # Create a new counter augmented division
    assert div_new(1, 2) == 0.5, "Middle school kid will beat you in math"
    assert div_new(4, 5) == 0.8, "Middle school kid will beat you in math"
    assert div_new(4, 0) == None, "Middle school kid will beat you in math"
    assert (mult_dict["mul"] == 2) and (div_dict["div"] == 3) , "Wrong count for mul operation"

# test for division operation including division by zero case
def test_session7_div_new_dict_count1():
    div_dict = dict()
    div_new = session7.counter_new2(session7.div, div_dict)     # Create a new counter augmented division
    assert div_new(1, 2) == 0.5, "Middle school kid will beat you in math"
    assert div_new(4, 5) == 0.8, "Middle school kid will beat you in math"
    assert div_new(4, 0) == None, "Middle school kid will beat you in math"
    assert div_dict["div"] == 3, "Wrong count for div operation"

# End of file
