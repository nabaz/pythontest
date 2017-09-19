import pdb

def hi(name="nabaz"):
    def greet():
        return "greet() function"
    def welcome():
        return "welcome() function"

    if name == "nabaz":
        return greet
    else:
        return welcome

@hi
def a():
     return True

def add(v1, v2):
    result = v1 + v2
    return result
