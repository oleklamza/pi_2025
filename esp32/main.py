from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from time import sleep
import random

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 4, 20)
lcd.clear()

# blocks
blocks = (
    bytearray((0b11111,0b11111,0b11111,0b00000,0b00000,0b00000,0b00000,0b00000)),
    bytearray((0b00000,0b00000,0b00000,0b00000,0b00000,0b11111,0b11111,0b11111)),
    bytearray((0b11111,0b11111,0b11111,0b00000,0b00000,0b00000,0b11111,0b11111)),
    bytearray((0b10101,0b01010,0b10101,0b01010,0b10101,0b01010,0b10101,0b00000)),
    bytearray((0b00000,0b01010,0b10101,0b01010,0b10101,0b01010,0b00000,0b00000)),
    bytearray((0b00000,0b00100,0b01010,0b00100,0b01010,0b00100,0b00000,0b00000)),
    bytearray((0b00000,0b00000,0b01010,0b00100,0b01010,0b00000,0b00000,0b00000)),
    bytearray((0b00000,0b00000,0b00000,0b00100,0b00000,0b00000,0b00000,0b00000)),
)

# big font
font = (
    (255,0,255,255,1,255),  #0
    (1,255,32,32,255,32),   #1
    (0,2,255,255,1,1),      #2
    (0,2,255,1,1,255),      #3
    (255,32,255,0,0,255),   #4
    (255,2,0,1,1,255),      #5
    (255,2,0,255,1,255),    #6
    (0,0,255,32,32,255),    #7
    (255,2,255,255,1,255),  #8
    (255,2,255,1,1,255),    #9
)

# prepare display fonts
c = 0
for block in blocks:
    lcd.custom_char(c, block)
    c += 1


def putchar_big(code, pos_x, pos_y=0):
    for i in range(6):
        lcd.move_to(pos_x+i%3, pos_y+i//3)
        lcd.putchar(chr(font[code][i]))

def print_pi_big(x, pos_x=0, pos_y=0):
    #comma
    lcd.move_to(pos_x+3, pos_y+1)
    lcd.putchar(chr(1))
    # digits
    x = x*10000     # 4 decimal places
    for k in (10000, 1000, 100, 10, 1):
        d = int(x // k)
        x -= d * k
        putchar_big(d, pos_x)
        pos_x += 4
        if k==10000: pos_x+=1

# animation
px = 24
line = f"{chr(7)*20}{chr(6)}{chr(5)}{chr(4)}{chr(3)}{chr(255)}{chr(7)*20}"
def anim():
    global px
    lcd.move_to(0, 2)
    lcd.putstr(line[px:px+20])
    px -= 1
    if px <= 0:
        px = 24


# Monte Carlo
i = 0
err = 1
circle_points = 0
square_points = 0
while True:
    rx = random.random()
    ry = random.random()

    d = rx**2 + ry**2
 
    square_points += 1
    if d <= 1:
        circle_points += 1 
 
    pi = 4 * circle_points / square_points
    _err = abs(3.1415926535-pi)
    if _err < err:
        err = _err
        print_pi_big(pi)

    lcd.move_to(0, 3)
    lcd.putstr(f"{i:05d} {pi:.12f}")

    # if i%5 == 0:
    anim()

    i += 1



