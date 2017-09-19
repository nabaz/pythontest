def binary_tree(r):
    return [r, [], []]
def insert_left(r, new_branch):
    t = r.pop(1)

    if len(t) > 1:
        r.insert(1, [new_branch, t, []])
    else:
        r.insert(1, [new_branch, [], []])
    return r

def insert_right(r, new_branch):
    t = r.pop(1)

    if len(t) > 1:
        r.insert(2, [new_branch, [], t])
    else:
        r.insert(2, [new_branch, [], []])
    return r

def get_root_val(r):
    return r[0]

def set_root_val(r, new_value):
    r[0] = new_value

def get_left_child(r):
    return r[1]


def get_right_child(r):
    return r[2]
