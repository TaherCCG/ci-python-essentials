# Functions
"""
Functions allow us to write a chunk of code that we can invoke whenever we choose. We can also introduce the use of code comments
to explain to a developer how individual sections of code work.

We’ve used plenty of different functions at this point, like print(), input(), range(), and len(). These are all functions that 
Python provides for us, so we don’t have to write all of the logic to perform these tasks ourselves. Not only does this mean that 
we can reuse the same pieces of code, but it also helps to improve the readability of the code. For example, print() would be quite 
difficult to implement if we had to write out the logic every time that we wanted to print something out to the console. It would 
be much more beneficial if we could just write the code once and then use it again and again. Not only that, but the word print is 
much easier to read and understand than the code would be if we were to write out all of that code ourselves. 
Let’s take a look at how we can create some functions.
"""

# Function definition
def greet():
    print("Hello, World!")

# Function call
greet()

"""
The editor highlights the code with color to show the purpose of each section.
    
    def: This is the keyword that we use to tell Python that we are creating a function definition. It is in blue in the editor.

print_message: This is the name that we’ve decided to give our function. Be sure to give your functions meaningful names so that when 
    other people try to use your code, they’ll able to make sense of what the function does without having to read the code in the function. 
    This is highlighted in purple in the editor as it is a function name.
(): The parentheses denote the parameters that a function takes. In this example, we don’t have any parameters yet, but we’ll start adding 
some in soon.
After all of this, we have the code inside of our function. The code inside the function is the actual logic that we wish to perform. 
It is indented by four spaces to show that this code is in the function. In this instance, we just print out Hello World which the editor 
highlights in green (#036a07) to show it is a string. As you can see we are calling the print() function from within our print_message function.
This is highlighted in blue (#0000ff) in the editor as it is a function name. Functions can call functions. Lastly, on line 4 we invoke that 
function which works in the same way that we used print(), only this time we don’t have arguments to pass as the function doesn’t take any 
parameters. It is not indented to show it is not in the function. Remove the code from line 4 and rerun the code to see what happens. Nothing, 
right? That’s because just defining the function doesn’t do anything. We need to invoke or call it.
"""


# Function definition
def greet():
    print("Hello, World!")

# Function call
greet()

"""
There is another type of function in Python known as Lambda. A lambda function is a small anonymous function. 
It can take any number of arguments but only has one expression. As you can see the function has no name (hence anonymous) 
so we have assigned it to the variable add.
"""

add = lambda a, b : a + b
print(add(5, 12))

