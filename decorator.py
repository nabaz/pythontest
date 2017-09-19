from functools import wraps

def new_a(a_func):
    @wraps(a_func)
    def decorated(*args, **kwargs):
        if not can_run:
            return "not running"
        return a_func(*args, **kwargs)
    return decorated

@new_a
def func():
    return("function is running")



