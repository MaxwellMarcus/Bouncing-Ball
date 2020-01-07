try:
    from tkiter import *
except ImportError:
    from Tkinter import *

root = Tk()

width = 500
height = 500

canvas = Canvas(root,width=width,height=height)
canvas.pack()
canvas.config(bg='black')


class Ball:
    def __init__(self):
        self.x = width/2
        self.y = 20

        self.vel_y = 0

        self.balls = []

        self.seconds = 0

        self.last_hit_time = ''

    def update(self):
        self.y += self.vel_y

        turning = False
        if self.vel_y < 0:
            turning = True

        self.vel_y +=.981

        if turning and self.vel_y >= 0:
            self.balls.append((width/2,self.y,self.seconds,int(height-self.y)))

        if self.y >= height-self.vel_y:
            self.y = height-1
            print(self.vel_y)
            self.vel_y = -self.vel_y/2
            self.last_hit_time = self.seconds
            print('hit')

        if len(str(self.last_hit_time)) > 0:
            print(self.vel_y)

        self.seconds += 1

        self.render()

    def render(self):
        for i in self.balls:
            if i[1] < height-10:
                canvas.create_oval(i[0]-5,i[1]-5,i[0]+5,i[1]+5,fill='white',outline='white')
                canvas.create_text(i[0]+25,i[1],text=str(i[2]),font=('TkTextFont',20),fill='white')
                canvas.create_text(i[0]-25,i[1],text=str(i[3]),font=('TkTextFont',20),fill='white')

        canvas.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,fill='green',outline='green')


        canvas.create_text(width-100,50,text='Seconds: '+str(self.seconds),font=('TkTextFont',15),fill='white')

        canvas.create_text(width/2-25,height-10,text=str(self.last_hit_time),font=('TkTextFont',20),fill='white')

ball = Ball()


while True:
    try:
        canvas.delete(ALL)

        canvas.create_line(0,height/2,width,height/2,fill='white',width=4)

        ball.update()

        root.update()


    except TclError:
        quit()
