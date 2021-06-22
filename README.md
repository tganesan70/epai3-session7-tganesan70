# session7-tganesan70
#
# This assignment describes solutions to the following problems

#
# 1. Closure that takes a function to test the docstrings quality
#
  Goal: Write a closure that takes a function and then check whether the 
  function passed has a docstring with more than 50 characters. 50 is stored 
  as a free variable (+ 4 tests) 
  
  A closure function with name 'check_doc_string(fn)' was created with a local
  variable called comment_len with default value of 50. The inner function
  reads the fn.__doc__ variable and counts the number of words if it is not empty
  If the count is less than 50 or empty, it returns False else True
  
  A wrapper function was added which calls the closure to run it on any given
  function, including the closure function itself. This is tested on a dummy_function()
  which is designed to fail the test, built-in function which have more than 50 
  words comments and the closure function which has more than 50 word comments.

#
# 2. closure that gives the next Fibonacci number  
#
  Goal: Write a closure that gives you the next Fibonacci number (+ 2 tests) 
  
  A closure was created using two free variables, old1 and old2 which are initialized 
  to be zero by the outer function. The inner function accesses the old1 and old2 in the 
  nonlocal scope. Then the Fibanocci sequence is created by adding the past two values. 
  The past 2 values are stored in the old1 and old2 to maintain continuity across the
  function calls. 
  
  This is tested upto 5 to 6 terms to check for correctness.

#
# 3. closure that counts how many times a function was called
#
  Goal: We wrote a closure that counts how many times a function was called. 
  Write a new one that can keep a track of how many times add/mul/div functions 
  were called, and update a global dictionary variable with the counts (+ 6 tests)
  
  A closure was created with count as a free variable which can be accessed by
  returning the inner function which updates the count variable whenever the inner
  function is called by the outer function.
  
  Three function add, mul and div are defined with two arguments and they are called by 
  the inner function after incrementing their corresponding count values. 
  
  A global disctionary was created to store the counter for each of the arithmetic
  operations defined above.
  
#
# 4. pass in different dictionary variables to the closure that counts the function calls
#
  Goal: Modify above such that now we can pass in different dictionary variables 
  to update different dictionaries (+ 6 tests) 
  
  The above closure function was modified to take dictionary as an additional argument
  which save the values of the free variable for each of the arithmetic operations. 
  
  Three different dictionaries were created to be passed on each of the arithmetic
  functions and each counter is updated inside each of the dictionary functions.
  
  Since these dictionaries are accessible in global context, they can be read and
  printed at any level of the context
  
 # 5. Test cases added for the functions in session7 module
    1. 4 tests for docstring checking
        - built-in function : print
        - Dummy function : with less comments for ensuring fail for the test
        - docstring checking function itself
        - docstring wrapper function
        
    2. 5 tests for Fibanocci sequence generator
        - First value after intialization
        - Second value in the sequence
        - Third valie in the sequnece
        - Fourth value in the sequence
        - Sixth value in the sequence
        
    3. 6 tests for Closure to count the operations
        - Check for empty dictionary when no function was called
        - Check for add function counts
        - Check for mul function counts
        - Check for div function counts
        - Check for combination of mul and div
        - check for combinations of all, add mul and div
    4. 6 tests for closure, but with global dictionary passed as arguments
        - Similar to the above test cases
        
    5. 6 tests for closure but with individual disctionaty for each operation
        - Similar to the above test cases
        
    Total no. of test cases: 27
     
# End of file
