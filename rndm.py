def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first_num(a, b):
        return a
    return pair(first_num)

def cdr(pair):
    def last_num(a, b):
        return b
    return pair(last_num)



print(cdr(cons(3, 4)))