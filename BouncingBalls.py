def bouncingBall(h, bounce, window):
    if h>0 and ( 0 < bounce <1):
        if window < h:         
            counter = 1
            while h >0:
                h*= bounce
                if (h - window) > 0: 
                    counter += 2
                else:
                    return counter
    return -1
