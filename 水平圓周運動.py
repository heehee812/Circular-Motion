from vpython import *

Origin   = vector(0,0,0)
size = 1         # 小球半徑
v0 = 10             # 小球初速
R = 9                # 圓周運動半徑
t = 0               
dt = 1e-4        # 時間間隔
ratio=0.1
w = pi
Rv= R/10
m=1
r= R #polar coordinate r
x= 0 #polar coordinate
L=m*r**2*w
Rchanging = False
Rbreaking = False


#畫面設定
scene = canvas(title = "Horizontal circle",center=vector(0,0,15), width = 1200, height = 800, x = 0, y = 0, background = color.gray(0.9))
scene.ambient = color.gray(0.99) #環境光調節

ex = extrusion(pos=vector(0,-3/2*size,0), path=paths.circle(radius=0.65*R), shape=[shapes.rectangle(pos=[0,1], width=1.2*R,height=size)],color=color.gray(0.6))
thing = box(pos=vector(0,-1.2*R,0), length= 3*size,  height=3*size, width=3*size, color = color.gray(0.9), texture=textures.wood)
ball = sphere(pos=r*vector(cos(x), 0, -sin(x)), radius = size, color = color.gray(0.9),texture=textures.wood )
ball.v = (r*w) * cross(vector(cos(x),0,-sin(x)),vector(0,-1,0)) #設定v初值
ball.a = mag2(ball.v) / r * (-vector(cos(x),0,-sin(x))) #設定a初值

rope1 = cylinder(pos=Origin, axis = ball.pos,  radius = 0.1*size, color=vector(0.5,0.3,0.2), texture = textures.stucco)
rope2 = cylinder(pos=Origin, axis = thing.pos, radius = 0.1*size, color=vector(0.5,0.3,0.2), texture = textures.stucco)

gd = graph(title = "plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "orange: v(m/s), gray: a(m/s^2)")
v_plot = gcurve(graph = gd, color = color.orange)
a_plot = gcurve(graph = gd, color = color.gray(0.5))


#控制視圖
scene.camera.pos = vector(0, 4*R, 2*R)
scene.camera.axis = -vector(0, 4*R, 2*R)


def Rchange(Rchange_btn):
    global Rchanging
    Rchanging=not Rchanging
    global note

Rchange_btn=button(text='Rope change',bind=Rchange)

def Note(Note_btn):
    note=scene.append_to_caption('<h3 style="color:gray">依角動量守恆得知\n繩子等速變短，球體切線速度增大。\n又等速率圓周運動切線速度增大，半徑減短得知，向心加速度增大，繩張力增強。\n而當繩張力到達極限時，繩子斷裂，球體於切線方向等速飛出。')

Note_btn=button(text='Note',bind=Note)

def  Rbreak(Rbreak_btn):
    global Rbreaking
    Rbreaking=not Rbreaking

Rbreak_btn=button(text='Rope break',bind=Rbreak)


while (True):
    rate(1/dt)
    t+=dt
    if (Rchanging and  not Rbreaking):
        if r>size:
            r -= Rv * dt
            x += w * dt
            w = L/(m*r**2)
            rope1.axis = ball.pos-Origin
            thing.v = vector(0, -Rv, 0)
            thing.pos += thing.v*dt
            rope2.axis = thing.pos-Origin

            ball.v = (r*w) * cross(vector(cos(x),0,-sin(x)),vector(0,-1,0))
            ball.a = mag2(ball.v) / r * (-vector(cos(x),0,-sin(x)))
            ball.pos = r * vector(cos(x), 0, -sin(x))
           
        if r<=size :
            Rbreaking=True
        
    elif(Rbreaking):
        ball.pos += ball.v*dt
    else:
        axis = ball.pos - Origin #找出小球相對於轉軸的位置向量
        x += w * dt

        ball.v = (r*w) * cross(vector(cos(x),0,-sin(x)),vector(0,-1,0)) #v = r*w * 方向向量
        ball.a = mag2(ball.v) / r * (-vector(cos(x),0,-sin(x)))         #a = v^2/r   * 方向向量
        ball.pos = r * vector(cos(x), 0, -sin(x))
        rope1.axis = axis

    v_plot.plot(t, ball.v.mag)
    a_plot.plot(t, ball.a.mag)

        
