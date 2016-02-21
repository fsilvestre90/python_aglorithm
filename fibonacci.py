def fibIterative(n):
    if (n <= 0): return 0
    elif (n == 1): return 1
    else:
        a = 0
        b = 1
        fi = 0
        for i in range(1, n):
            fi = a + b
            a = b
            b = fi
        return fi

def fibR(n):
    return fibRecursive(0, 1, 1, n)

def fibRecursive(a, b, fi, n):
    if (n == 0): return n
    if (n == 1): return n
    else:
        # print ("%s %s %s %s" % (a, b, fi, n))
        if fi is n: return a + b
        else:
            fi += 1
            return fibRecursive(b, a+b, fi, n)

for i in range(20000):
    print(fibR(i))
