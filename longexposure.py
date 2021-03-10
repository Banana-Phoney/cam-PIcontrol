import time
import gpiozero
import shutil
import os

lengde = int(input("How long should the picture be exposed? \nTime in seconds: "))

source_dir = ('/run/user/1000/gvfs/gphoto2:host=Canon_Inc._Canon_Digital_Camera/DCIM/104CANON')
target_dir = ('/home/pi/Desktop/ftp/bilder')

pic = gpiozero.LED(18)
pic.on()

focus = gpiozero.LED(17)
focus.on()

usbp = gpiozero.LED(4)
usbp.off()

time.sleep(5)

focus.off()
time.sleep(4)
focus.on()

print("Picture time!")
pic.off()
time.sleep(lengde)
pic.on()
print("Picture taken! Transfering to ftp folder.")
time.sleep(1)
usbp.on()
time.sleep(5)
usbp.off()
time.sleep(5)
print("Done!")

file_names = os.listdir(source_dir)

for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
