import time
import board
import digitalio
import pwmio

def setDutyCycle(pin, dt=2 ** 15):
    pin.duty_cycle = dt
    return pin

#sets a pin as pwm
def setPinOut(pin, dt=0, ff=50):
    pwm = pwmio.PWMOut(pin, frequency=ff)
    setDutyCycle(pwm, dt)
    return pwm


bluegp = board.GP11; redgp = board.GP12; greengp = board.GP13
bluePin = redPin = greenPin = None

def confgp(blue=None, red=None, green=None):
    global bluegp; global redgp; global greengp;
    if blue is not None : bluegp = blue
    if red is not None : redgp = red
    if green is not None : greengp = green
    return((bluegp, redgp, greengp))

def basicSetup():
    global bluePin; global redPin; global greenPin;
    if bluePin is None :
        bluePin = setPinOut(bluegp)
        redPin = setPinOut(redgp)
        greenPin = setPinOut(greengp)

def blueOn(dt=2 ** 10) :
    global bluePin; basicSetup(); setDutyCycle(bluePin, dt)

def blueOff() :
    global bluePin; basicSetup(); setDutyCycle(bluePin, 0)

def greenOn(dt=2 ** 10) :
    global greenPin; basicSetup(); setDutyCycle(greenPin, dt)

def greenOff() :
    global greenPin; basicSetup(); setDutyCycle(greenPin, 0)

def redOn(dt=2 ** 10) :
    global redPin; basicSetup(); setDutyCycle(redPin, dt)

def redOff() :
    global redPin; basicSetup(); setDutyCycle(redPin, 0)

def allOn(dt = 2 ** 10) :
    blueOn(dt); greenOn(dt); redOn(dt)

def allOff(dt = 0) :
    blueOff(); greenOff(); redOff()

# pw.quickTest(20, 2 ** 15, 0.1, 02, 1)
def quickTest(loop_times = 2, dt = 2 ** 11, sleepon_time = 2, sleepoff_time = 1, no_print=0):
    global redPin; global greenPin; global bluePin;
    basicSetup()
    def onOff(color, pin):
        if no_print == 0 : print("PWM {} On ...".format(color))
        setDutyCycle(pin, dt)
        time.sleep(sleepon_time)
        if no_print == 0 : print("PWM {} Off ...".format(color))
        setDutyCycle(pin, 0)
        time.sleep(sleepoff_time)

    for ii in range(loop_times):
        onOff("Blue", bluePin)
        onOff("Green", greenPin)
        onOff("Red", redPin)
    print("----- Done ----")
