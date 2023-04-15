"""
this function take in a non-keyworded arguments 
and iterate them.
"""
def myFun(*argv):
    for arg in argv:
        print(arg)

"""
when myFun is call it print out each argument in a separate line
"""
myFun('Hello,', 'Mr. man', 'you are', '24')
