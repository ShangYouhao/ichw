"""tile.py: 有一面墙，规格为 长 m 宽 n 的长方形，现在要把规格为 长 a 宽 b 的长方形瓷砖铺满该墙面，输出选定总数的铺法，并将选定的铺法用turtle模块可视化。

__author__ = "shangyouhao"
__pkuid__ = "1800011714"
__email__ = "1800011714@pku.edu.cn"
"""


def judge(m, n, a, b, i):
    """判断在i位置能否放入长为a宽为b的瓷砖"""
    if i % m + a > m or i // m + b > n:
        return False

    for p in range(b):
        for r in states[i + p*m : i + p*m + a]:
            if r != 0:
                return False

    return True


def put(m, n, a, b, i=0):
    """能否从i位置开始将剩余部分铺满，若铺满则返回答案组成的列表，否则返回空列表"""
    ans = []
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


def put_square(m, n, a, i=0):
    """简化处理正方形的情况"""
    ans = []
    if i >= m*n:
        return [[]]

    while states[i] != 0:
        i += 1
        if i == m*n:
            return [[]]

    if judge(m ,n, a, a, i):
        for p in range(a):
            states[i + p*m : i + p*m + a] = [1] * a
        parts = put_square(m, n, a, i)
        bricks = tuple([brick for q in range(a)
                                    for brick in range(i + q * m , i + q * m + a)])
        for part in parts:
            part.append(bricks)
        ans.extend(parts)
        for p in range(a):
            states[i + p*m : i + p*m + a] = [0] * a

    return ans


def tile(m, n, a, b):
    """除重版本的铺砖函数"""
    if a == b:
        anss = list(set([tuple(ans) for ans in put_square(m, n, a)]))
    else:
        anss = list(set([tuple(ans) for ans in put(m, n, a, b)]))
    return anss


def draw(ans, m, n):
    """画出其中一组解"""
    import turtle
    s0 = int(600 / max(m, n))
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("blue")
    for i in range(n + 1):
        t.pu()
        t.goto(s0 * (-m/2), s0 * (n/2 - i))
        t.pd()
        t.fd(s0 * m)
    t.rt(90)
    for i in range(m + 1):
        t.pu()
        t.goto(s0 * (-m/2 + i), s0 * (n/2))
        t.pd()
        t.fd(s0 * n)
    t.lt(90)
    t.color("purple")
    for i in range(m):
        for j in range(n):
            t.pu()
            t.goto(s0 * (-m/2 +0.2 + i), s0 * (n/2 - 0.9 - j))
            t.write(str(i + j*m), "center")
    t.color("black")
    t.pensize(3)
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


def main(m, n, a, b):
    anss = tile(m, n, a, b)
    if anss == []:
        print("不能铺满")
    else:
        print("共有", len(anss), "组解")
        area = input("""请输入需要查看的解(如：要查看从第35到第42组解/第6组解，输入"35 42"/"6")""").split()
        while True:
            try:
                if len(area) == 1:
                    if int(area[0]) < 1 or int(area[0]) > len(anss):
                        print("序号超出范围！")
                        area = input("""请输入需要查看的解(如：要查看从第35到第42个解，输入"35 42")""").split()
                    else:
                        print("->", area[0], ":", anss[int(area[0]) - 1])
                        break

                else:
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

            except:
                print("输入错误")
                area = input("""请输入需要查看的解(如：要查看从第35到第42个解，输入"35 42")""").split()

        n_ans = int(input("请选择要画出的解的序号："))

        while True:
            if n_ans <= len(anss):
                draw(anss[n_ans - 1], m, n)
                break
            else:
                n_ans = int(input("请输入已有的序号："))


if __name__ == "__main__":
    mn = input("请输入墙的长和宽(用空格隔开)：").split()
    (m, n) = (int(mn[0]), int(mn[1]))
    ab = input("请输入瓷砖的长和宽(用空格隔开)：").split()
    (a, b) = (int(ab[0]), int(ab[1]))
    states = [0] * m * n
    main(m, n, a, b)

