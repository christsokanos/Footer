Exercise:

Imagine you’re creating a footer with pagination to browse through 
the several pages of a given website.

Let’s assume the usage of the following variables for the effect:
- current_page
- total_pages
- boundaries: how many pages we want to link in the beginning, or end 
(meaning, how many pages starting at page 1 and how many leading up to the last page, inclusive)
- around: how many pages we want to link before and after the current page, exclusive.
For pages with no direct link we should use one set of three points (...) per set of pages hidden.

Some examples:
1) current_page = 4; total_pages = 5; boundaries = 1; around = 0
Expected result: 1 ... 4 5
2) current_page = 4; total_pages = 10; boundaries = 2; around = 2
Expected result: 1 2 3 4 5 6 ... 9 10

The code should print the result and not only calculate it.

The solution should be developed “test-first”, and should have good unit test
coverage.



              *******INSTRUCTIONS*******

First thing to do after running the programm is  to give some basic values 
(total pages, current page, boundaries, around) to calculate and print your footer. 

Valid inputs must be positive numbers only! 

main.py file contains basic code for inputs and creates a new object. 

task.py file contains the class and it's methods.

test_task.py file contains unittest coverage.
