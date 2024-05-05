# Indentation in Python

"""
The use of indentation to define a block of code makes it very clear to read. In other programming languages indentation is purely 
for readability, but in Python, it is vital to the correct running of the program. The PEP8 standard is four spaces for indentation level. 
Python 3 will error if you mix spaces and tabs.

The maximum line length is 79 characters. This means that a line of code may have to be wrapped onto a continuation line. 
The continuation line indent cannot match the block indentation; otherwise, there will be an error. You can either add four further spaces 
to the continuation line indent or align with the opening delimiter on the preceding line.
"""

# This is easier to see than to explain so here are the official PEP8 suggestions.

# Correct:

# It is aligned with the opening delimiter, e.g. the opening parentheses.
foo = long_function_name(var_one, var_two,      # type: ignore
                         var_three, var_four)   # type: ignore

# Add four spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,               # type: ignore
    var_three, var_four)            # type: ignore


# No arguments are allowed on the first line where hanging indentation is used.

# Incorrect:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two, # type: ignore
    var_three, var_four)                   # type: ignore

# Further indentation required as indentation is not distinguishable.

def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

# No extra indentation.

foo = long_function_name(
    var_one, var_two, # type: ignore
    var_three, var_four) # type: ignore

# The closing brace/bracket/parenthesis on multiline constructs may be lined up 
# under the first non-whitespace character of the last line of list, as in:

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments( # type: ignore
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
