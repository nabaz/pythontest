import Deque()

def palindorme(a_string):
    ch_dequeu = Deque()

    for ch in a_string:
        ch_dequeu.add_rear(ch)
    still_ok = True

    while ch_dequeu.size() > 1 and still_ok:
        first = ch_dequeu.remove_front()
        last = ch_dequeu.remove_rear()

        if frist != last:
            still_ok = False

        return still_ok
