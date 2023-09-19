import psutil, math, time
#import Adafruit_CharLCD as LCD (only works on pi)
from datetime import datetime

#screen size 16x2
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p)
   return "%s %s" % (s, size_name[i])

def displayCpu():
    cputemp=69 #placeholder :)
    # temp sensor only works on linux, uncomment when deploying to pi
    # temps=psutil.sensors_temperatures()
    # cputemp=temps["core_thermal"].current
    
    return(f"CPU @ {psutil.cpu_freq().current/1000:.1f} GHz\n{psutil.cpu_percent()}% | {cputemp}°C")


def displayMemory():
    return(f"RAM Used: {psutil.virtual_memory().percent:.0f}%\nEmpty: {convert_size(psutil.virtual_memory().available)}")

def displayDisk():
    winpath="C:\\"
    pipath="/" #use this on linux?
    return(f"Disk: {psutil.disk_usage(winpath).percent:.0f}% full\n{convert_size(psutil.disk_usage(winpath).free)} free")

def screenLoop(delay):
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
    while(True):
        lcd.message(displayCpu())
        lcd.clear()
        time.sleep(delay)
        lcd.message(displayMemory())
        lcd.clear()
        time.sleep(delay)
        lcd.message(displayDisk())
        lcd.clear()
        time.sleep(delay)
print("16_characters___")
print(displayCpu())
print(displayMemory())
print(displayDisk())
