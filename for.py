def long_add():
    l = 0
    print("Введите первое число:", end="")
    a = list(map(int, list(input())))
    a.reverse()
    print("Введите второе число:", end="")
    b = list(map(int, list(input())))
    b.reverse()
    c = []
    if len(a)<len(b):
        k = len(a)
        m = len(b)
    else:
        k = len(b)
        m = len(a)
    for i in range(k):
        t = a[i]+b[i]+l
        if(t>=10):
            l = 1
            t = t - 10
            c.append(t)

            continue
        else:
            l = 0

        c.append(t)

    for i in range(k, m):

        if len(a) < len(b):
            t = b[i]+l
            if t >= 10:
                l = 1
                t = t - 10
                c.append(t)
                continue
            else:
                l = 0
        else:
            t = a[i] + l
            if t >= 10:
                l = 1
                t = t - 10
                c.append(t)
                continue
            else:
                l = 0
            c.append(t)
    if l != 0:
        c.append(l)


    c.reverse()
    print(*c, sep='')