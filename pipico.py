import board

GPIO = {}

GPIO["0"] = board.GP0 ;
GPIO["1"] = board.GP1 ;
GPIO["2"] = board.GP2 ;
GPIO["3"] = board.GP3 ;
GPIO["4"] = board.GP4 ;
GPIO["5"] = board.GP5 ;
GPIO["6"] = board.GP6 ;
GPIO["7"] = board.GP7 ;
GPIO["8"] = board.GP8 ;
GPIO["9"] = board.GP9 ;
GPIO["10"] = board.GP10 ;
GPIO["11"] = board.GP11 ;
GPIO["12"] = board.GP12 ;
GPIO["13"] = board.GP13 ;
GPIO["14"] = board.GP14 ;
GPIO["15"] = board.GP15 ;
GPIO["16"] = board.GP16 ;
GPIO["17"] = board.GP17 ;
GPIO["18"] = board.GP18 ;
GPIO["19"] = board.GP19 ;
GPIO["20"] = board.GP20 ;
GPIO["21"] = board.GP21 ;
GPIO["22"] = board.GP22 ;
GPIO["23"] = board.GP23 ;
GPIO["24"] = board.GP24 ;
GPIO["25"] = board.GP25 ;
GPIO["26"] = board.GP26 ;
GPIO["27"] = board.GP27 ;
GPIO["28"] = board.GP28 ;

def get_gpio(num1):
    return (GPIO["{}".format(num1)])

