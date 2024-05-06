# Taking Parameters and Returning Results

"""
Functions can take parameters and return results. This is a powerful feature of functions that allows you 
to write code that is more flexible and reusable. Parameters are the values that you pass into a function when
you call it, and results are the values that the function returns when it finishes running. You can use parameters
to customize the behaviour of a function, and you can use results to pass information. This allows you to write
functions that can be used in many different situations.


The purpose behind using functions is to have reusable code. The function that we created in the first functions 
example was called print_message, which then prints out Hello World. That’s all well and good, but what if we wanted 
to say hello to a user instead of saying Hello World. The problem is that our function doesn’t allow for that level 
of flexibility. One way around this would be to create a function for every name, but that would get very unwieldy, 
and the codebase would end up being massive! Instead, we can use parameters. Parameters allow us to provide a function 
with input data that we want it to use.
"""

def add(a, b):
    sum = a + b
    return sum

# in JavaScript
"""
function add(a,b) {
    let sum = a + b;
    return sum;
}
"""

"""
A function's parameters are the special variables used by a function to handle this input, whereas the arguments are the 
values provided for the parameters when we run the function. For example, on line 1, we create a function that has a parameter 
named name, and then on line 5 we run that function and pass in the value of the variable username as the argument for that parameter.
"""

def print_message(name):
    print(f"Hello {name}")

username = input("What's your name? ")
print_message(username)


"""
We can also use optional parameters. Optional parameters will allow us to provide values to a function with some value in case they 
are not provided when the function is invoked. To do so, we use the assignment operator to set a value to the parameter when we are 
defining our function. In the example below, we have given the name parameter a default value of World.

We don’t provide an argument when we invoke the function as we do on line 5, the function will just print out Hello World. Notice 
that we initially stored the value in a variable called username, but inside the function, we’ve called in a name. This is because 
we’re passing a new variable to the function called name, with the value of username. The name variable cannot be accessed outside 
of the function. Therefore if we were to try to print name outside of the function, it wouldn’t work. This is known as variable scope.

Rather than printing the result in the function, we have returned it. This is how a computer program expects to see the result of a 
function. However, to see the output as a human, we then need to wrap the function calls in print() , so the result is printed to the terminal.
"""

def print_message(name="World"):
    return f"Hello {name}"

username = input("What's your name? ")
print(print_message())
print(print_message(username))

