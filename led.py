import RPi.GPIO as gpio
import time
import random
left=[5,9,11,10,20,21,6,22]
right=[21,22,10,9,5,6,11]

def hyouji(l,r,trig):
    if trig==True:
        for suji in l:
            gpio.output(suji,True)
    else:
        for suji in r:
            gpio.output(suji,True)
            
def reset():
    for f in left:
        gpio.output(f,False)    
def one(trig):
    l=[20,10,22]
    r=[9,5]
    hyouji(l,r,trig)
def two(trig):
    l=[21,20,6,9,11,22]
    r=[6,5,11,22,10]
    hyouji(l,r,trig)
def three(trig):
    l=[21,6,20,10,11,22]
    r=[6,20,11,9,10,5]
    hyouji(l,r,trig)
def four(trig):
    l=[5,6,10,20,22]
    r=[21,9,5,11]
    hyouji(l,r,trig)
def five(trig):
    l=[21,5,6,11,10,22]
    r=[21,11,10,20,6,9]
    hyouji(l,r,trig)
def six(trig):
    l=[5,21,9,11,10,6,22]
    r=[21,9,22,11,10,6]
    hyouji(l,r,trig)
def seven(trig):
    l=[5,21,10,20,22]
    r=[5,21,9,6]
    hyouji(l,r,trig)
def eight(trig):
    l=[5,21,9,11,10,20,6,22]
    r=[5,21,9,11,10,22,6]
    hyouji(l,r,trig)
def nine(trig):
    l=[5,21,11,10,20,6,22]
    r=[5,21,9,11,10,6]
    hyouji(l,r,trig)
def zero(trig):
    l=[5,21,9,11,20,10,22]
    r=[5,21,9,22,10,6]
    hyouji(l,r,trig)
def err(trig):
    gpio.output(4,trig)
    l=[11,6,5,21,9]
    r=[10,11,6,21,22]
    hyouji(l,r,trig)
    time.sleep(.01)
    reset()
def warota(j,trig):
    gpio.output(4,trig)
    if j==0: 
        zero(trig)
    elif j==1:
        one(trig)
    elif j==2:
        two(trig)
    elif j==3:
        three(trig)
    elif j==4:
        four(trig)
    elif j==5:
        five(trig)
    elif j==6:
        six(trig)
    elif j==7:
        seven(trig)
    elif j==8:
        eight(trig)
    elif j==9:
        nine(trig)
    time.sleep(.01)
    reset()

def ld(moji):
    gpio.setmode(gpio.BCM)
    gpio.setup(26,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(19,gpio.OUT)
    gpio.output(19,True)
    if moji=="0":
        gpio.output(13,True)
    else :
        gpio.output(13,False)
        
def ed(aa):
    gpio.setmode(gpio.BCM)
    gpio.setup(26,gpio.OUT)
    if aa=="0":
        gpio.output(26,False)
    else :
        gpio.output(26,True)
        
def seg(t):
#     while 1:
        gpio.setmode(gpio.BCM)
        gpio.setup(4,gpio.OUT)
        for b in left:
            gpio.setup(b,gpio.OUT)
        j=int(t*10%100)
        ju=int(j/10)
        ichi=j%10
        time_s=time_e=time.time()
        if int(t/10)!=3:
            while time_e-time_s<=3:
                trig =True
                err(trig)
                trig=False
                err(trig)
                time_e=time.time()
        else:
            while time_e-time_s<=3:
                trig =True
                warota(ju,trig)
                trig=False
                warota(ichi,trig)
                time_e=time.time()
            t=j=0
if __name__ == '__main__':
    seg()
  

