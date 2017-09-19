def search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last ) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

def b_s(al, item): #not working currently
    if len(al) == 0:
        return False
    else:
        midpoint = len(al) // 2
        if al[midpoint] == item:
            return True
        else:
            if item < al[midpoint]:
                return b_s(al[:midpoint], item)
            else:
                return b_s(al[:midpoint+1], item)
