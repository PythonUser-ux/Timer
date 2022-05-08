import winsound
import time as tm
import datetime
import math

from sqlalchemy import true


def timer(seconds):
    a=tm.time()
    try:
        tm.sleep(seconds)
        date=str(datetime.datetime.now())
        print(date[:19])
        winsound.Beep(1500, 620)
    except:
        print("Interruption...")
        time=tm.time()
        if math.floor(time-a)>60:
            print("Min so far",round(math.floor(time-a)/60,1))
        else:
            print("Sec so far",math.floor(time-a))
        if seconds-math.floor(time-a)>60:
            print("Min left",round(((seconds-math.floor(time-a))/60),1))
        else:
            print("Sec left",seconds-math.floor(time-a))
        Restart=input("Continue? [Y]")
        if Restart.upper()=="Y":
            timer(seconds-math.floor(time-a))
        try:
            Restart=int(Restart)
            timer(seconds-math.floor(time-a)+Restart*60)
        except:
            pass

volume_test=true
if volume_test:
    winsound.Beep(1500, 620)
    tm.sleep(0.5)
    winsound.Beep(1500, 620)

while True:
    try:
        times=1
        seconds=int(input("Minutes? "))*60
        if seconds==-60:
            seconds=int(input("Seconds? "))
        if seconds==-120:
            times=int(input("Times? "))
            seconds=int(input("Minutes? "))*60
            if seconds==-60:
                seconds=int(input("Seconds? "))
        for _ in range(times):
            date=str(datetime.datetime.now())
            print(date[:19])
            timer(seconds)
    except:
        print("Error")