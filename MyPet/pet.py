import random
import os
import platform
from tkinter import *
import time

# Caminho adaptado para Linux (use ~/ ou caminho absoluto)
impath = os.path.expanduser('~/MyPet/')

#WINDOW PARAMS
window = Tk()
window.overrideredirect(True)
screen_height = window.winfo_screenheight()
lower_border = 40
width = 96
height = 64
x_position = 0
y_position = screen_height - height - lower_border
window.geometry(f"{width}x{height}+{x_position}+{y_position}")

# Transparência: no Linux, -transparentcolor não funciona.
# Alternativas: usar -alpha (translucidez) ou remover.
try:
    window.wm_attributes("-transparentcolor", "white")
except TclError:
    # Fallback Linux: janela levemente translúcida (opcional)
    try:
        window.wm_attributes("-alpha", 1.0)
    except TclError:
        pass

window.wm_attributes("-topmost", True)

#CHANCES FOR ANIMATION/BEHAVIOR
walk_right = [1]
walk_left = [2]
eat_event = [3, 4, 5]
idle_event = [6, 7, 8, 9]
sleep_event = [10]


def load_gif(name, frames):
    """Carrega um GIF animado dividido em frames."""
    path = os.path.join(impath, name)
    return [PhotoImage(file=path, format=f'gif -index {i}') for i in range(frames)]


#ANIMATIONS
walk_pos            = load_gif('walking_right.gif', 4)
walk_neg            = load_gif('walking_left.gif', 4)
turn_forward_lr1    = load_gif('turn_forward_lr1.gif', 4)
turn_forward_lr2    = load_gif('turn_forward_lr2.gif', 4)
turn_backward_rl1   = load_gif('turn_backward_rl1.gif', 4)
turn_backward_rl2   = load_gif('turn_backward_rl2.gif', 4)
idle                = load_gif('idle.gif', 4)
sleep_up            = load_gif('sleep_up.gif', 8)
sleep               = load_gif('sleep.gif', 8)
sleep_down          = load_gif('sleep_down.gif', 4)
eat                 = load_gif('eat.gif', 4)
eat_up              = load_gif('eat_up.gif', 4)
eat_down            = load_gif('eat_down.gif', 4)


def animate(frames, MinDurationInSec, MaxDurationInSec):
    ind = 0
    OneWholeAnimation = len(frames)
    randomDuration = random.randrange(
        MinDurationInSec * OneWholeAnimation,
        MaxDurationInSec * OneWholeAnimation,
        OneWholeAnimation
    )
    for i in range(randomDuration):
        if frames == walk_pos:
            if window.winfo_rootx() >= (window.winfo_screenwidth() - width):
                choose_behavior(3, 1)
            window.geometry(f"{width}x{height}+{window.winfo_rootx() + 5}+{y_position}")
        if frames == walk_neg:
            if window.winfo_rootx() < 0:
                choose_behavior(1, 3)
            window.geometry(f"{width}x{height}+{window.winfo_rootx() - 5}+{y_position}")
        frame = frames[ind]
        ind += 1
        if ind == OneWholeAnimation:
            ind = 0
        label.configure(image=frame)
        window.update()
        time.sleep(0.25)


def choose_behavior(event_number, prior_event):
    if event_number in walk_right:
        if prior_event in walk_left:
            animate(turn_forward_lr1, 1, 2)
            animate(turn_forward_lr2, 1, 2)
        animate(walk_pos, 3, 6)
    elif event_number in walk_left:
        if prior_event in walk_right or prior_event in idle_event:
            animate(turn_backward_rl1, 1, 2)
            animate(turn_backward_rl2, 1, 2)
        animate(walk_neg, 3, 6)
    elif event_number in eat_event:
        animate(eat_down, 1, 2)
        animate(eat, 5, 9)
        animate(eat_up, 1, 2)
    elif event_number in idle_event:
        if prior_event in walk_left:
            animate(turn_forward_lr1, 1, 2)
            animate(turn_forward_lr2, 1, 2)
        animate(idle, 2, 5)
    elif event_number in sleep_event:
        if prior_event in sleep_event:
            animate(idle, 2, 5)
        else:
            animate(sleep_down, 1, 2)
            animate(sleep, 6, 11)
            animate(sleep_up, 1, 2)
    prior_event = event_number
    randomNum = random.randrange(1, 11, 1)
    choose_behavior(randomNum, prior_event)


label = Label(window)
label.pack()
choose_behavior(7, 10)
window.mainloop()
