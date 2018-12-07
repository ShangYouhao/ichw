def judge(m, n, a, b, i):
    if i % m + a > m or i // m + b > n:
        return False

    for p in range(b):
        for r in states[i + p*m : i + p*m + a]:
            if r != 0:
                return False

    return True


def put(m, n, a, b, i=0):
    ans = []
    cantput = True
    if i >= m*n:
        return [[]]

    while states[i] != 0:
        i += 1
        if i == m*n:
            return [[]]

    for (a, b) in [(a, b), (b, a)]:
        if judge(m ,n, a, b, i):
            for p in range(b):
                states[i + p*m : i + p*m + a] = [1] * a
            parts = put(m, n, a, b, i)
            bricks = tuple([brick for q in range(b)
                                      for brick in range(i + q * m , i + q * m + a)])
            for part in parts:
                part.append(bricks)
            ans.extend(parts)
            for p in range(b):
                states[i + p*m : i + p*m + a] = [0] * a

    return ans


def tile(m, n, a, b):
    anss = list(set([tuple(ans) for ans in put(m, n, a, b)]))
    return anss


def draw(ans, m, n):
    import turtle
    s0 = int(300 / max(m, n))
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(10)
    for i in range(len(ans)):
        t.pu()
        site = ans[i][0]
        t.goto(s0 * (-m/2 + site%m),s0 * (n/2 - site//m))
        t.pd()
        j = 0
        while site in ans[i]:
            j += 1
            site += 1
            if j >= m:
                break
        lena = j * s0
        site -= 1
        j = 0
        while site in ans[i]:
            j += 1
            site += m
        lenb = j * s0
        for k in range(2):
            t.fd(lena)
            t.rt(90)
            t.fd(lenb)
            t.rt(90)
    turtle.done()


if __name__ == "__main__":
    mn = input("请输入墙的长和宽(用空格隔开)：").split()
    (m, n) = (int(mn[0]), int(mn[1]))
    ab = input("请输入瓷砖的长和宽(用空格隔开)：").split()
    (a, b) = (int(ab[0]), int(ab[1]))
    states = [0] * m * n
    anss = tile(m, n, a, b)
    if anss == []:
        print("不能铺满")
    else:
        print("共有", len(anss), "组解")
        area = input("""请输入需要查看的解(如：要查看从第35到第42组解，输入"35 42")""").split()
        if len(area) == 1:
            print("->", area[0], ":", anss[int(area[0]) - 1])
        else:
            while True:
                (start, end) = (int((area)[0]) - 1, int((area)[1]))
                if start >= end:
                    print("输入错误！")
                    area = input("""请输入需要查看的解(如：要查看从第35到第42个解，输入"35 42")""").split()
                elif end <= len(anss) and start >= 0:
                    for (i, ans) in enumerate(anss[start : end]):
                        print("->", i + start + 1, ":", ans)
                    break
                else:
                    print("序号超出范围！")
                    area = input("""请输入需要查看的解(如：要查看从第35到第42个解，输入"35 42")""").split()

        n_ans = int(input("请选择要画出的解的序号："))

        while True:
            if n_ans <= len(anss):
                draw(anss[n_ans - 1], m, n)
                break
            else:
                n_ans = int(input("请输入已有的序号："))

