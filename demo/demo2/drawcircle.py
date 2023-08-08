import math
import turtle


def draw_circle_with_turtle(x, y, r):
    # 提笔，开始绘画前先定位下笔位置
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))


draw_circle_with_turtle(0, 0, 50)
turtle.mainloop()
