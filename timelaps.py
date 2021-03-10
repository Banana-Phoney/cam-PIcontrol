import time
import gpiozero

morning = 6
night = 19

length = int(input("How long betwen photos? \nTime in seconds: "))

pic = gpiozero.LED(18)
pic.off()

while True:
    t = time.localtime()
    c_t = time.strftime("%H", t)
    k_t = int(c_t)

    if(k_t >= morning and k_t <= night):
        print("picture time!")
        pic.on()
        time.sleep(1)
        pic.off()
        time.sleep(tid_mellombilde)
    else:
        print("Sleeping!")
        time.sleep(5)
