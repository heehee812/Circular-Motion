from vpython import *

size = 0.5          # 小球半徑
R = 5          # 圓周運動半徑
g = 9.8           # 重力加速度 9.8 m/s^2
v0 = 1*sqrt(g*R)          # 小球初速, 1 ~ 7 sqrt(g*R)
ratio = 0.1          # 箭頭長度與實際的比例
i = 0          # 小球回到出發點的次數
t = 0                
dt = 0.0001



#畫面設定

scene = canvas(title = "Vertical circle", width = 1200, height = 800, x = 0, y = 0, background = color.gray(0.9))
ring = ring(pos = vector(0, 0, -size), axis = vector(0, 0, 2*size), radius = R, color = color.gray(0.5))
ball = sphere(pos = vector(0, R, 0), radius = size, color = color.gray(0.5))
center = cylinder(pos = vector(0, 0, -size), axis = vector(0, 0, 2*size), radius = 0.1*size, color = color.gray(0.9))
ball.v = vector(-v0, 0, 0)
arrow_v = arrow(pos = ball.pos, axis = vector(0, 0, 0), radius = 0.2*size, shaftwidth = 0.4*size, color =vector(0.4,0.4,0.5))
arrow_an = arrow(pos = ball.pos, axis = vector(0, 0, 0), radius = 0.2*size, shaftwidth = 0.4*size, color = vector(0.8,0.4,0.1))
arrow_at = arrow(pos = ball.pos, axis = vector(0, 0, 0), radius = 0.2*size, shaftwidth = 0.4*size, color = vector(0.8,0.4,0.1))



#設定按鈕
def velocity():
    arrow_v.visible=not(arrow_v.visible)
    
    

velocity=button(text="Velocity component",bind=velocity)



def acceleration():
    arrow_an.visible=not(arrow_an.visible)
    arrow_at.visible=not(arrow_at.visible)

acceleration=button(text="Acceleration component",bind=acceleration)


#圖表
gd=graph(title="plot",width=1200,height=450,x=0,y=850,xtitle="t(s)",ytitle="green:v(m/s),orange:at(m/s^2),purple:an(m/s^2)")
vt_plot=gcurve(graph=gd,color=vector(0,0.25,0.2))
at_plot=gcurve(graph=gd,color=vector(0.8,0.4,0.1))
an_plot=gcurve(graph=gd,color=vector(0.4,0.4,0.5))



#計算運動量
def findan(v, pos):
    an = -v.mag2 / R * pos.norm()
    return an

def findat(pos):
    x = pos.x
    y = pos.y
    r = sqrt(x**2 + y**2)
    sintheta = abs(x)/r
    costheta = abs(y)/r
    absat = g*sintheta
    aty = -absat*sintheta



    if((x <= 0 and y <= 0) or (x >=0 and y>= 0)):
        atx = +absat*costheta
    elif((x <= 0 and y >= 0) or (x >= 0 and y <= 0)):
        atx = -absat*costheta
    at = vector(atx, aty, 0)
    return at


#開始運動
while True:
    rate(5000)
    xp = ball.pos.x
    an = findan(ball.v, ball.pos)
    at = findat(ball.pos)
    ball.v +=(an+at)*dt
    ball.pos += ball.v*dt
    xc = ball.pos.x


    #更新箭頭
    arrow_v.pos = ball.pos
    arrow_v.axis = ball.v * ratio
    arrow_an.pos = ball.pos
    arrow_an.axis = an* ratio
    arrow_at.pos = ball.pos
    arrow_at.axis = at* ratio 

    #更新圖表
    vt_plot.plot(t,ball.v.mag)
    at_plot.plot(t,at.mag)
    an_plot.plot(t,an.mag)

    #更新時間
    t += dt
    
    
    
    



