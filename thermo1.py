import time
import busio 
import board
import adafruit_amg88xx
def ondo():
    i2c = busio.I2C(board.SCL,board.SDA)
    sensor = adafruit_amg88xx.AMG88XX(i2c, addr=0x69)
    time.sleep(0.1)
    pix = sensor.pixels
    gati=0
    for i in pix:
        summ=0
        for j in range(8):
            summ+=i[j]
        gati+=summ/8  
    gati/=8
    print('{:.2f}'.format(gati))
    return gati
if __name__ == '__main__':
    ondo()
