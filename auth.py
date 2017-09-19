from functools import  wraps

def logit(func):
    @wraps(func)
    def with_logging(*arg, **kwargs):
        print(func.__name__ + " was called")
        return func(*arg, **kwargs)
    return with_logging

@logit
def add_fun(x):
    return x + x

