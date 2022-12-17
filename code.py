import time
import board
import pwmio

import parser as p
import tabulate as t
import ticker as tk
import PWMLED as pled
import pipico as pp


while False:
    pled.quickTest()

while False:
    led.duty_cycle = 0xf000

while False:
    for change in seq:
        led.duty_cycle = change[2]
        time.sleep(change[0])
h = p.separator(p.sorter(p.parser('test.txt')))
all = t.all_colours(h)
print(all)

tickHash1 = {}

def led(int1, color1, tick1):
    hash1 = {"R" : pled.redOn, "G" : pled.greenOn, "B" : pled.blueOn, "scala" : lambda x : int(x * 2 ** 16 / 256), "waitfn" : lambda : time.sleep(0.7)}
    newint1 = int(int1 * 2 ** 16 / 256)
    hash1.get(color1, lambda x : print(f"Unknown color {color1}"))(newint1)
    if not (tick1 in tickHash1.keys()) : hash1["waitfn"]()
    tickHash1[tick1] = 1


tk.executor(all, led)


