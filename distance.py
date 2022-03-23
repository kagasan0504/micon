import time
import RPi.GPIO as GPIO
import thermo1
import led

def main(time_in=0,time_out=0):
    wewe=taion=taionn=0
    while 1:
      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(17,GPIO.OUT)
      GPIO.setup(27,GPIO.IN)
      GPIO.output(17,GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(17,True)
      time.sleep(0.00001)
      GPIO.output(17,False)
      while GPIO.input(27) == 0:
        sig_off = time.time()
      while GPIO.input(27) == 1:
        sig_on = time.time()
      try:
        timepass = sig_on - sig_off
        distance = timepass * 331.5 / 0.02
        if distance < 6.0:
          time_out = time.time()
        else :
          time_in = time.time()
        if (time_out - time_in) > 0.5:
          if wewe<5:
            print('OK! : {:.1f}cm'.format(distance))
            wewe+=1
            taion+=thermo1.ondo()
            taionn=taion/5
          else :
            break
        else :
          print('.   : {:.1f}cm'.format(distance))
          wewe=taion=taionn=0
      except:
        print('err : distance is too close.')
      GPIO.cleanup()
    print('{:.3f}'.format(taionn))
    led.seg(taionn)
    return taionn
if __name__ == '__main__':
    main()
