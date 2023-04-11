import tkinter as tk
from vector2 import *
import monitor
import time
import random

window2 = tk.Toplevel()
window2.title("MIGUEL")


class miguel():
    def __init__(self):
        # create a window
        monitor.init_monitors()
        # placeholder image
        self.walking_positive = [tk.PhotoImage(file='walk222.gif',format = 'gif -index %i' %(i)) for i in range(4)]
        self.walking_negative = [tk.PhotoImage(file='walk111.gif',format = 'gif -index %i' %(i)) for i in range(4)]
        
        
        self.frame_index = 0
        self.img = self.walking_negative[self.frame_index]
        # timestamp to check whether to advance frame
        self.timestamp = time.time()

        # set focushighlight to black when the window does not have focus


        # make window frameless
        window2.overrideredirect(True)

        

        # make window draw over all others
        window2.attributes('-topmost', 1)
        # turn black into transparency
        window2.wm_attributes('-transparentcolor', '#00ff00')

        # create a label as a container for our image
        self.label = tk.Label(window2, bd=0, bg='#00ff00')

        # create a window of size 128x128 pixels, at coordinates 0,0
        self.pos = Vector2(-110, monitor.max_pos_y-200)
        self.target= Vector2(0,0)
        self.maxlimit= Vector2(monitor.max_pos_x-65,monitor.max_pos_y-155)
        self.minlimit= Vector2(monitor.min_pos_x,monitor.min_pos_y)

        window2.geometry('61x152+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        window2.after(0, self.start)

    def start(self):
        # move right by one pixel
        
        if ((self.pos.x)<100):
            self.pos.x += 1


            

            # advance frame if 50ms have passed
            if time.time() > self.timestamp + 0.05:
                self.timestamp = time.time()
                # advance the frame by one, wrap back to 0 at the end
                self.frame_index = (self.frame_index + 1) % 4
                self.img = self.walking_negative[self.frame_index]

            # create the window
            window2.geometry('61x152+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
            # add the image to our label
            self.label.configure(image=self.img)
            # give window to geometry manager (so it will appear)
            self.label.pack()

            # call update after 10ms
            window2.after(10, self.start)
        else:
            window2.after(10, self.update)

    
    def inside(self):
        if(self.pos.y>self.maxlimit.y):
            self.target.y = random.randrange(-1,1,1)
        elif(self.pos.y<self.minlimit.y):
            self.target.y = random.randrange(0,2,1)
        
        return self.target.y
        



    def update(self):
        check = random.randrange(0,2,1)
        self.target.x = random.randrange(self.minlimit.x,self.maxlimit.x+1,1)
        self.target.y = random.randrange(-1,2,1)
        if check == 0:
            window2.after(10,self.foward)
            
            #idle to sleep
        else:
            window2.after(10,self.backward)
            #sleep

    def foward(self):
        # move right by one pixel
        #if((self.pos.x<self.target.x)and(self.pos.y<self.maxlimit.y)and(self.pos.y>self.minlimit.y)):
        if(self.pos.x<self.target.x):
            self.pos.x += 1
            self.pos.y += self.inside()

            

        

        # advance frame if 50ms have passed
            if time.time() > self.timestamp + 0.05:
                self.timestamp = time.time()
                # advance the frame by one, wrap back to 0 at the end
                self.frame_index = (self.frame_index + 1) % 4
                self.img = self.walking_negative[self.frame_index]

            # create the window
            window2.geometry('61x152+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
            # add the image to our label
            self.label.configure(image=self.img)
            # give window to geometry manager (so it will appear)
            self.label.pack()

            window2.after(10, self.foward)
        # call update after 10ms
        else:
            # self.img = self.walking_negative[1]
            # time.sleep(0.5)
            window2.after(10, self.update)

    def backward(self):
        # move right by one pixel
        
        #((self.pos.x>self.maxlimit.x-self.target.x)and(self.pos.y<self.maxlimit.y)and(self.pos.y>self.minlimit.y))
        
        if(self.pos.x>self.target.x):
            self.pos.x -= 1
            self.pos.y += self.inside()


        

        # advance frame if 50ms have passed
            if time.time() > self.timestamp + 0.05:
                self.timestamp = time.time()
                # advance the frame by one, wrap back to 0 at the end
                self.frame_index = (self.frame_index + 1) % 4
                self.img = self.walking_positive[self.frame_index]

            # create the window
            window2.geometry('61x152+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
            # add the image to our label
            self.label.configure(image=self.img)
            # give window to geometry manager (so it will appear)
            self.label.pack()

            window2.after(10, self.backward)
        # call update after 10ms
        else:
            # self.img = self.walking_positive[1]
            # time.sleep(0.5)
            window2.after(10, self.update)


