import time
import board
import pwmio
from parser import sorter

led = pwmio.PWMOut(board.LED)

#(seq, not_imp, not_imp_2) = sorter('test.txt')
#print(seq)

while False:
    led.duty_cycle = 0xf000

while False:
    for change in seq:
        led.duty_cycle = change[2]
        time.sleep(change[0])
