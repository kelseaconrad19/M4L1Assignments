"""
Task 1: Custom Module with Aliases
    - Problem Statement: Create a custom module named text_utils.py with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.
    - Expected Outcome: Your main script should be able to use the functions from text_utils.py via an alias, demonstrating an understanding of custom module creation and aliasing.
"""
from text_utils import reverse_string as rev
from text_utils import capitalize_string as cap

my_string = "this is an interesting string."
reversed_string = rev(my_string)
print(reversed_string)
capitalized_string = cap(my_string)
print(capitalized_string)

