import time as t
import pyautogui as pag
pag.FAILSAFE = False

X, Y = 1365, 767*1.5

def speed(X,Y,depth=0,*args,**kargs):
    factor = kargs['factor'] if kargs else 1/2
    Xn,Yn=int(X*factor),int(Y*factor)
    x,y = pag.position()
    if depth < 8 and x < Xn and y < Yn:
        return speed(Xn,Yn,depth=depth+1,*args,**kargs)
##    print(X,Y,x,y,depth)
    return x,y,depth

def toggle_taskview():
            pag.keyDown('winleft')
            pag.keyDown('tab')
            pag.keyUp('tab')
            pag.keyUp('winleft')
            
def run():
    while True:
        x,y,_speed = speed(X,Y,factor=0.6)
        _wait = 1/3**_speed if x+y<800 and x<500 and y<400 else 0.5
        t.sleep(_wait)
        if x<15 and y<15:
            toggle_taskview()
            x1,y1 = pag.position()
            while x1<15 and y1<15:
                x1,y1 = pag.position()
                t.sleep(0.5)
##            print('---------hit---------')
                
if __name__=='__main__':
    print('program started')
    run()
