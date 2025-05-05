import random
from tkinter import *
import time

impath = 'D:\\nichtGanzSoWichtiges\\MyPet\\'

#WINDOW PARAMS
window = Tk()
window.overrideredirect(True)
screen_height = window.winfo_screenheight()
lower_border = 40
width = 96
height = 64
x_position = 0
y_position = screen_height -height- lower_border
window.geometry(f"{width}x{height}+{x_position}+{y_position}")
window.wm_attributes("-transparentcolor", "white")
window.wm_attributes("-topmost", True)

#CHANCES FOR ANIMATION/BEHAVIOR
walk_right = [1]
walk_left = [2]
eat_event = [3,4,5]
idle_event = [6,7,8,9]
sleep_event = [10]

#ANIMATIONS
walk_pos = [PhotoImage(file=impath + 'walking_right.gif',format = 'gif -index %i' %i) for i in range(4)]
walk_neg = [PhotoImage(file=impath + 'walking_left.gif',format = 'gif -index %i' %i) for i in range(4)]
turn_forward_lr1 = [PhotoImage(file=impath + 'turn_forward_lr1.gif',format = 'gif -index %i' %i) for i in range(4)]
turn_forward_lr2 = [PhotoImage(file=impath + 'turn_forward_lr2.gif',format = 'gif -index %i' %i) for i in range(4)]
turn_backward_rl1 = [PhotoImage(file=impath + 'turn_backward_rl1.gif',format = 'gif -index %i' %i) for i in range(4)]
turn_backward_rl2 = [PhotoImage(file=impath + 'turn_backward_rl2.gif',format = 'gif -index %i' %i) for i in range(4)]
idle = [PhotoImage(file=impath + 'idle.gif',format = 'gif -index %i' %i) for i in range(4)]
sleep_up = [PhotoImage(file=impath + 'sleep_up.gif',format = 'gif -index %i' %i) for i in range(8)]
sleep = [PhotoImage(file=impath + 'sleep.gif',format = 'gif -index %i' %i) for i in range(8)]
sleep_down = [PhotoImage(file=impath + 'sleep_down.gif',format = 'gif -index %i' %i) for i in range(4)]
eat = [PhotoImage(file=impath + 'eat.gif',format = 'gif -index %i' %i) for i in range(4)]
eat_up = [PhotoImage(file=impath + 'eat_up.gif',format = 'gif -index %i' %i) for i in range(4)]
eat_down = [PhotoImage(file=impath + 'eat_down.gif',format = 'gif -index %i' %i) for i in range(4)]


def animate(frames,MinDurationInSec,MaxDurationInSec):
    ind = 0
    OneWholeAnimation = len(frames)
    randomDuration = random.randrange(MinDurationInSec * OneWholeAnimation,MaxDurationInSec * OneWholeAnimation, OneWholeAnimation)
    for i in range(randomDuration):
        if frames == walk_pos:
            if window.winfo_rootx() >= (window.winfo_screenwidth() - width):
                choose_behavior(3,1)
            window.geometry(f"{width}x{height}+{window.winfo_rootx() + 5}+{y_position}")
        if frames == walk_neg:
            if window.winfo_rootx() < 0:
                choose_behavior(1,3)
            window.geometry(f"{width}x{height}+{window.winfo_rootx() - 5}+{y_position}")
        frame = frames[ind]
        ind += 1
        if ind == OneWholeAnimation:
            ind = 0
        label.configure(image = frame)
        window.update()
        time.sleep(0.25)


def choose_behavior(event_number,prior_event):
    if event_number in walk_right:
        if prior_event in walk_left:
            animate(turn_forward_lr1, 1, 2)
            animate(turn_forward_lr2, 1, 2)
        animate(walk_pos,3,6)
    elif event_number in walk_left:
        if prior_event in walk_right or prior_event in idle_event:
            animate(turn_backward_rl1, 1, 2)
            animate(turn_backward_rl2, 1, 2)
        animate(walk_neg,3,6)
    elif event_number in eat_event:
        animate(eat_down,1,2)
        animate(eat,5,9)
        animate(eat_up, 1, 2)
    elif event_number in idle_event:
        if prior_event in walk_left:
            animate(turn_forward_lr1, 1, 2)
            animate(turn_forward_lr2, 1, 2)
        animate(idle,2,5)
    elif event_number in sleep_event:
        if prior_event in sleep_event:
            animate(idle, 2, 5)
        else:
            animate(sleep_down, 1, 2)
            animate(sleep,6,11)
            animate(sleep_up, 1, 2)
    prior_event = event_number
    randomNum = random.randrange(1, 11, 1)
    choose_behavior(randomNum,prior_event)

label = Label(window)
label.pack()
choose_behavior(7,10)
window.mainloop()

