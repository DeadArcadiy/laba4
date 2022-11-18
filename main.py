import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import math


def brezen(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    px = []
    py = []

    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el/2, 0

    px.append(x)
    py.append(y)

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        px.append(x)
        py.append(y)
    return px, py

def circle(x1,y1,x2,y2):
    px = []
    py = []
    r = math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))
    disp_x = x1
    disp_y = y1
    x = 0
    y = r
    delta = (1-2*r)
    error = 0
    while y >= 0:
        px.append(disp_x + x)
        py.append(disp_y + y)
        px.append(disp_x + x)
        py.append(disp_y - y)
        px.append(disp_x - x)
        py.append(disp_y + y)
        px.append(disp_x - x)
        py.append(disp_y - y)
        
        error = 2 * (delta + y) - 1
        if ((delta < 0) and (error <=0)):
            x+=1
            delta = delta + (2*x+1)
            continue
        if ((delta > 0) and (error > 0)):
            y -= 1
            delta = delta - (1 + 2 * y)
            continue
        x += 1
        delta = delta + (2 * (x - y))
        y -= 1
    return px,py

def submit(text):
    coor = list(map(int, text.split()))
    if (len(coor) == 4):
        point_x, point_y = brezen(coor[0], coor[1], coor[2], coor[3])
        ax1.plot(point_x, point_y, '*')
        x, y = circle(coor[0], coor[1], coor[2], coor[3])
        ax2.plot(x, y, '.')
        dx,dy = dda(coor[0], coor[1], coor[2], coor[3])
        ax3.plot(dx,dy,'.')
        sx,sy = step(coor[0], coor[1], coor[2], coor[3])
        ax4.plot(sx,sy,'+')
        plt.draw()

def dda(x1,y1,x2,y2):
    x =[]
    y =[]
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    if steps == 0:
        return [x1],[y1]
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)    
    for i in range(0, int(steps + 1)):
        x.append(round(x1))
        y.append(round(y1))
        x1 += Xinc
        y1 += Yinc
    return x,y

def step(x1,y1,x2,y2):
    x =[]
    y =[]
    dx = x2 - x1
    dy = y2 - y1
    xx = min(x1,x2)
    if dx == 0 and dy == 0:
        return [x1],[y1]
    if dy == 0:
        while xx <= max(x2,x1):
            y.append(y1)
            x.append(xx)
            xx +=1
        return x,y
    if dx == 0:
        yy = min(y1,y2)
        while yy <= max(y2,y1):
            y.append(yy)
            x.append(x1)
            yy += 1
        return x,y
    while xx <= max(x2,x1):
        y.append(round(y1 + dy * (xx - x1) / dx))
        x.append(xx)
        xx += 1
    return x, y

if __name__ == "__main__":
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    ax = fig.add_axes([0.1, 0, 0.8, 0.05])
    ax1.title.set_text("Brezenhem line")
    ax2.title.set_text('Brezenhem circle')
    ax3.title.set_text('DDA algoritm')
    ax4.title.set_text('Step algoritm')
    x = [10, 1]
    y = [1, 10]    
    point_x, point_y = brezen(x[0], x[1], y[0], y[1])
    ax1.plot(point_x, point_y, '*')
    cx, cy = circle(x[0], x[1], y[0], y[1])
    ax2.plot(cx, cy, '.')
    dx,dy = dda(x[0], x[1], y[0], y[1])
    ax3.plot(dx,dy,'.')
    sx,sy = step(x[0], x[1], y[0], y[1])
    ax4.plot(sx,sy,'+')
    
    text_box = TextBox(ax, "Input", initial="10 1 1 10")
    text_box.on_submit(submit)
    plt.show()
