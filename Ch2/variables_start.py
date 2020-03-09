# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)


# # re-declaring the variable works
f="abc"
print(f)


# # ERROR: variables of different types cannot be combined
# print("this is a string" + 123)   # this fails
print("this is a string" + str(123))

# Global vs. local variables in functions
def someFunction():
    f="def"
    print(f) # variables are scoped locally to the function by default

someFunction()
print(f)

# using global variable
def someFunction2():
    global f # override default local scope
    f="def"
    print(f) 

someFunction2()
print(f)

del(f)
print(f) # throws "name 'f' is not defined" error
