# 太阳系六大行星运行模型
# 化学与分子工程学院 尚游皓 1800011714

import math
import turtle

Mercury = turtle.Turtle()
Venus = turtle.Turtle()
Earth = turtle.Turtle()
Mars = turtle.Turtle()
Jupiter = turtle.Turtle()
Saturn = turtle.Turtle()
Sun = turtle.Turtle()

r = [39, 54, 75, 108, 190, 300]         # 代入半长轴数据
e = [0.206, 0.007, 0.017, 0.093, 0.048, 0.054]          # 代入偏心率数据
colors = ['gray', 'orange', 'blue', 'red', 'yellow', 'brown', 'white']
planets = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Sun]
size = [0.3, 0.57, 0.6, 0.4, 1.2, 1.0, 2.8]


def set_planets():
    """设置黑色背景，太阳和行星的形状、颜色、大小以及调整总体运行速度"""
    wn = turtle.Screen()
    wn.bgcolor('black')
    for i in range(7):
        planets[i].shape('circle')
        planets[i].color(colors[i])
        planets[i].delay = 0.01
        planets[i].speed(0)
        planets[i].shapesize(size[i], size[i], size[i])


def set_positions():
    """设置行星的初始位置"""
    for i in range(6):
        planets[i].pu()
        r_theta = r[i]/(1 + e[i] * math.cos(math.radians(53*i)))
        x = r_theta * math.cos(math.radians(53*i - 120*i))
        y = r_theta * math.sin(math.radians(53*i - 120*i))
        planets[i].goto(x, y)
        planets[i].pd()


def draw_step(t, r, e, theta, i):
    """使一颗初角度为120i的行星t转过角度theta"""
    r_theta = r/(1 + e*math.cos(math.radians(theta)))
    x = r_theta * math.cos(math.radians(theta - 120*i))
    y = r_theta * math.sin(math.radians(theta - 120*i))
    t.goto(x, y)


def main():
    set_planets()
    set_positions()
    theta = [0, 53, 53*2, 53*3, 53*4, 53*5]
    for p in range(2000):
        for i in range(6):                  # 六颗行星轮流前进,轨道长轴依次转过53i#
            k = (1 + e[i]*math.cos(math.radians(theta[i])))**2
            dtheta = 2/((r[i]/150)**1.5)*k
            theta[i] = theta[i] + dtheta
            draw_step(planets[i], r[i], e[i], theta[i], i)

    turtle.done()


if __name__ == '__main__':
    main()
