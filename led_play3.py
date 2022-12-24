class Tick():
    def __init__(self, value1):
        self.value = int(value1)
        self.kind = "Tick"
    
    def __repr__(self):
        return(f"Tick({self.value})")

    def valueish(self,val1):
        try: 
            return val1.value
        except Exception:
            return val1

    def __add__(self, val1):

        val2 = self.valueish(val1)
        # print(f"adding {self} to {val1} (self's value is {self.value} val1's value is {val2})")

        if type(self) == Tick : return(Tick(self.value + val2))
        if type(self) == PreTick : return(PreTick(self.value + val2))
        if type(self) == PostTick : return(PostTick(self.value + val2))
        raise(Exception("Tick : unknown class type"))
    
    def __sub__(self, val1):
        # print(f"v1 sub={val1}  self={self}  type={type(val1)}")
        val2 = self.valueish(val1)

        #never do this in real life
        if val2 == Tick(0) : val2=0

        # print(f"v2 sub={val2}")
        if type(self) == Tick : return(Tick(self.value - val2))
        if type(self) == PreTick : return(PreTick(self.value - val2))
        if type(self) == PostTick : return(PostTick(self.value - val2))
    
    def __mul__(self, val1):
        val2 = self.valueish(val1)
        # print(f"multiplying {self} to {val1} (self's value is {self.value} val1's value is {val2})")

        if type(self) == Tick : return(Tick(self.value * val2))
        if type(self) == PreTick : return(PreTick(self.value * val2))
        if type(self) == PostTick : return(PostTick(self.value * val2))
    
    def __mod__(self, val1):
        val2 = self.valueish(val1)
        # print(f"mod v1 sub={val1.value}  val2={val2}  self={self}  type={type(val1)}")
        # if type(val1) == Tick or  type(val1) == PreTick or  type(val1) == PostTick :

        if type(self) == Tick : return(Tick(self.value % val2))
        if type(self) == PreTick : return(PreTick(self.value % val2))
        if type(self) == PostTick : return(PostTick(self.value % val2))
        raise(Exception("Tick : unkown class type"))

    def __cmp__(self, val1):
        if type(val1) == Tick or  type(val1) == PreTick or  type(val1) == PostTick :
            if self.value < val1.value  : return(-1)
            if self.value > val1.value  : return(1)
            return(0)
        else :
            if self.value < val1 : return(-1)
            if self.value > val1 : return(1)
            return(0)

    def __lt__(self, val1):
        if type(val1) == Tick or  type(val1) == PreTick or  type(val1) == PostTick :
            if self.value < val1.value  : return(True)
            return(False)
        else :
            if self.value < val1 : return(True)
            return(False)

    def __le__(self, val1):
        if type(val1) == Tick or  type(val1) == PreTick or  type(val1) == PostTick :
            if self.value <= val1.value  : return(True)
            return(False)
        else :
            if self.value <= val1 : return(True)
            return(False)

    def __ge__(self, val1):
        if type(val1) == Tick or  type(val1) == PreTick or  type(val1) == PostTick :
            if self.value >= val1.value  : return(True)
            return(False)
        else :
            if self.value >= val1 : return(True)
            return(False)

    def __gt__(self, val1):
        if type(val1) == Tick or  type(val1) == PreTick or  type(val1) == PostTick :
            if self.value > val1.value  : return(True)
            return(False)
        else :
            if self.value > val1 : return(True)
            return(False)

    def __eq__(self, val1):
        if type(val1) == Tick or  type(val1) == PreTick or  type(val1) == PostTick :
            if self.value == val1.value  : return(True)
            return(False)
        else :
            if self.value == val1 : return(True)
            return(False)

class PostTick(Tick):
    def __init__(self, val1):
        self.value = int(val1)
        self.kind = "PostTick"

class PreTick(Tick):
    def __init__(self, val1):
        self.value = int(val1)
        self.kind = "PreTick"

class Intensity():
    def __init__(self, value1):
        self.value = int(value1)
    def __repr__(self):
        return(f"Intensity({self.value})")

    def valueish(self,val1):
        try:
            return val1.value
        except Exception:
            return val1
    
    def __add__(self, val1):
        val2 = self.valueish(val1)
        return(Intensity(self.value + val2))
    
    def __sub__(self, val1):
        val2 = self.valueish(val1)
        return(Intensity(self.value - val2))
    
    def __mul__(self, val1):
        val2 = self.valueish(val1)
        return(Intensity(self.value * val2))
    
    def __floordiv__(self, val1):
        val2 = self.valueish(val1)
        return(Intensity(self.value // val2))
        return(self.value * val1) 
        #this runs if val1 is not any tick of intensity
        #did this cause the error?

class Rout():
    def __init__(self, name, data, pretick=0,posttick=0,repeat=3, begin:int=0):
        self.name = name; 
        self.data = data; #array of arrays that have tick,col,intensity
        self.kind = "Rout"
        self.pretick,self.posttick,self.repeat = PreTick(pretick),PostTick(posttick),repeat
        self.begin = begin
    
    def __repr__(self):
        return("Rout(" + f"name=\"{self.name}\", data={self.data}, pretick={self.pretick}, posttick={self.posttick}, repeat={self.repeat}, begin={self.begin}" + ")")
    
    def __getitem__(self, val1):
        # print(f"getitem for {self.name} is happening for {val1}")
        return self.getvalues(Tick(val1))

    def getvalues(self, tick1):
        # print(f"getvalues calculation for {self.name} is happening for {tick1}")
        width1 = self.spanv()
        # print(f"HHH - ( {self.pretick} + {width1} * {self.repeat} + {self.posttick} + {self.begin} )")
        if self.begin <= tick1 <= ( self.pretick + width1 * self.repeat + self.posttick + self.begin ) :
            tick2 =  (tick1 -  self.pretick) - self.begin 
            # print(f"tick2={tick2}  tick1={tick1} self.pretick={self.pretick}  self.begin={self.begin} ")
            if tick2 < 1 : return(None)
            # if tick2 > ( self.pretick + width1 * self.repeat + self.begin ) : return None
            # ToDo ; implement mod
            tick3_2 = (tick2 - self.minv()) % self.spanv()
            tick3 = ( tick3_2 + self.pretick + self.minv() ) + self.begin
            vv1 = [ii for ii in self.data if ii[0] <= tick3]
            vv2 = [ii for ii in self.data if ii[0] > tick3]
            # print(f"vv1={vv1}   vv2={vv2}   tick3={tick3}   ")
            hh1 = {} ; hh2 = {}
            for ii in vv1 : hh1[ii[1]] = ii
            for ii in vv2 : 
                if ii[1] not in hh2.keys() : hh2[ii[1]] = ii
            hh3 = {}
            for ii in hh1.keys():
                # print(f"GGG hh1={hh1}   hh2={hh2}  tick3={tick3} spanv={self.spanv()}  tick2={tick2}   hh[ii][0]={hh1[ii][0]}   ii={ii} self.maxv={self.maxv()}  self.minv={self.minv()}")
                if len(hh1[ii]) < 4 :
                    hh3[ii] = hh1[ii][2]
                else :
                    if hh1[ii][3].startswith("Ramp") :
                        if ii in hh2.keys():
                            hh3[ii] = hh1[ii][2] + ((hh2[ii][2] - hh1[ii][2] ) * (tick3 - hh1[ii][0]) // (hh2[ii][0] - hh1[ii][0] ))
                        else:
                            print(f"Warn : Ramp seems to be last item for Rout {self.name}. Taking final val as 255")
                            hh3[ii] = hh1[ii][2] + ((Intensity(255) - hh1[ii][2] )  * (tick3 - hh1[ii][0]) // (self.spanv() - hh1[ii][1] + 1 ) )
                    else:
                        hh3[ii] = hh1[ii][2]
            return(hh3)
        return(None)

    def maxv(self):
        v1 = 0
        for dd1 in self.data :
            if dd1[0] > v1 : v1 = dd1[0]
        return(v1)

    def minv(self):
        v1 = 99999
        for dd1 in self.data :
            if dd1[0] < v1 : v1 = dd1[0]
        return(v1)

    def spanv(self):
        return(self.maxv() - self.minv() + 1)

    def clone(self):
        aa1 = Rout(self.name, self.data[:], self.pretick.value, self.posttick.value, self.repeat)
        return(aa1)

    def __mul__(self, val1):
        if self.kindish(val1)=="Rout":
            #not yet decided
            pass 
        else:
            aa1  = self.clone()
            aa1.repeat = aa1.repeat * self.valueish(val1)
            return(aa1)

    def __pow__(self, num1):
        if self.kindish(num1)=="Rout":
            #not yet decided
            pass 
        else:
            aa1  = self.clone()
            for entry in aa1.data:
                entry[2] *= num1
            return(aa1)

    def __lshift__(self, num1): #<<
        if self.kindish(num1)=="Rout":
            aa1 = num1.clone()
            aa1.begin =  (self.pretick + self.posttick + (self.spanv() * self.repeat)) + ( self.begin + aa1.begin )
            return(CompoundRout([self, aa1], "append"))

        else: #assumes that it's an integer
            aa1 = self.clone()
            aa1.pretick += num1
            return aa1

    def __rshift__(self, num1): #>>
        if self.kindish(num1)=="Rout":
            #not yet decided
            pass
        else: #assumes that it's an integer
            aa1 = self.clone()
            aa1.posttick += num1
            return aa1

    def __add__(self, num1):
        aa1 = self.clone()
        if self.kindish(num1) == "PreTick" :
            aa1.pretick = self.pretick + num1
        elif self.kindish(num1) == "PostTick" :
            aa1.posttick = self.posttick + num1
        elif self.kindish(num1) == "Tick" :
            aa1.pretick = self.pretick + num1
        elif self.kindish(num1) == "Rout":
            aa1 = num1.clone()
            return(CompoundRout([self,aa1], "merge"))
        else :
            aa1.begin = self.begin + num1
        return(aa1)

    def __sub__(self, num1):
        aa1 = self.clone()
        if self.kindish(num1)=="Rout":
            #print(f"subtracting {num1} from {self}")
            aa1 = -num1.clone()
            #print(f"aa1.data is now {aa1.data}")
            return(CompoundRout([self,aa1], "merge"))
        else:
            aa1.begin = self.begin - num1
            return aa1

    def __neg__(self):
        for entry in self.data:
            entry[2] = entry[2]* -1

    def valueish(self,val1):
        try: 
            return val1.value
        except Exception:
            return val1

    def kindish(self,val1):
        try: 
            return val1.kind
        except Exception:
            return "Unknown"

class CompoundRout():
    def __init__(self, routs, oper): 
        #routs is an array of 2 routs
        #kind is either append or merge
        #the purpose of this class is to distribute
        self.routs = routs
        # print("----new compound root object created----")
        # print(f"routs are {routs}")
        # print("----------------------------------------")
        self.kind = "CompoundRout"
        self.oper = oper

    def __getitem__(self, tk):
        final = {}
        for item in self.routs:

            # print(f"item is {item}")
            to_add = item[tk]
            # print(f"to_add is {to_add}")
            if to_add==None:
                pass
            else:
                for chan in to_add.keys():
                    if chan in final.keys():
                        final[chan] += to_add[chan]
                    else:
                        final[chan] = to_add[chan]
        return final
                
    def __mul__(self, val1):

        if rout.kindish(val1)=="Rout":
            #not yet decided
            pass 
        else:
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1  = rout.clone()
                aa1.repeat = aa1.repeat * rout.valueish(val1)
                bb1.routs[index] = aa1
            return bb1
        

    def __pow__(self, num1):
        if rout.kindish(num1)=="Rout":
            #not yet decided
            pass 
        else:
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1  = rout.clone()
                for entry in aa1.data:
                    entry[2] *= num1
                bb1.routs[index] = aa1
            return bb1

    def __lshift__(self, num1): #<<
        if self.kindish(num1)=="Rout":
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                # print(f"rout is {rout}")
                aa1 = num1.clone()
                # print(f"ABCDDD={rout.begin}      {aa1.begin}")
                tmp1 = (rout.begin + aa1.begin)
                # print(f"tmp1={tmp1} = {rout.begin} +++++ {aa1.begin}")
                aa1.begin =  (rout.pretick + rout.posttick + (rout.spanv() * rout.repeat)) + (rout.begin + aa1.begin)
                bb1.routs[index] = CompoundRout([rout, aa1], "append")
            return bb1
        else: #assumes that it's an integer
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1 = rout.clone()
                aa1.pretick += num1
                bb1.routs[index] = aa1
            return bb1

    def __rshift__(self, num1): #>>
        if self.kindish(num1)=="Rout":
            #not yet decided
            pass
        else: #assumes that it's an integer
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1 = rout.clone()
                aa1.posttick += num1
                bb1.routs[index] = aa1
            return bb1

    def __add__(self, num1):
        if self.kindish(num1) == "PreTick" :
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1 = rout.clone()
                aa1.pretick = rout.pretick + num1
                bb1.routs[index] = aa1
            return bb1
        elif self.kindish(num1) == "PostTick" :
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1 = rout.clone()
                aa1.posttick = rout.posttick + num1
                bb1.routs[index] = aa1
            return bb1
        elif self.kindish(num1) == "Tick" :
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1 = rout.clone()
                aa1.pretick = rout.pretick + num1
                bb1.routs[index] = aa1
            return bb1
        elif self.kindish(num1) == "Rout":
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1 = num1.clone()
                bb1.routs[index] = CompoundRout([rout,aa1], "merge")
            return bb1
        elif self.kindish(num1) == "CompoundRout":
            aa1 = self.routs
            bb1 = num1.routs
            to_ret = CompoundRout(self.routs + num1.routs, "merge")
            return to_ret
        else :
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1 = rout.clone()
                aa1.begin = num1 + rout.begin
                bb1.routs[index] = aa1
            return bb1

    def __sub__(self, num1):
        if self.kindish(num1)=="Rout":

            bb1 = self.clone()

            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1 = -num1.clone()
                #print(f"aa1.data is now {aa1.data}")
                bb1.routs[index] = CompoundRout([rout,aa1], "merge")

            return bb1

        else:
            bb1 = self.clone()
            for index in range(len(bb1.routs)):
                rout = bb1.routs[index]
                aa1 = rout.clone()
                aa1.begin = rout.begin - num1
                bb1.routs[index] = aa1
            return bb1

    def __neg__(self):
        for index in range(len(self.routs)):
            rout = self.routs[index]
            for entry in rout.data:
                entry[2] = entry[2]* -1

    def valueish(self,val1):
        try: 
            return val1.value
        except Exception:
            return val1

    def kindish(self,val1):
        try: 
            return val1.kind
        except Exception:
            return "Unknown"

    def clone(self):
        aa1 = CompoundRout(self.routs, self.kind)
        return aa1

class Chann():
    def __init__(self, name1, data1):
        self.name = name1; self.data = data1; self.kind = "Chann"
    def __repr__(self):
        return("Chann( " + f"name=\"{self.name}\", data={self.data}" + " )")

class Runplan():
    def __init__(self, name1, data1):
        self.name = name1; self.data = data1; self.kind = "Runplan"
    def __repr__(self):
        return("Runplan(" + f"name=\"{self.name}\", data={self.data}" + ")")

class LEDDef():
    def __init__(self, file1):
        self.file = file1
        with open(self.file) as ff1:
            self.data = ff1.readlines()
        self.pattPairs = [["CHANN ",None], ["ROUT ", "ROUTEND"], ["RUNSEQ", "RUNSEQEND"]]
        self.parseData = []
        self.objects = {}
    def validate(self):
        errc1 = 0
        for rs1 in self.objects["RUNSEQ"]  :
            for rt1, *rt2 in rs1.data :
                ff1 = list(filter(lambda rr1 : rr1.name == rt1, self.objects["ROUT "]))
                if len(ff1) == 0 : 
                    print(f"Error : Could not find a ROUT with name {rt1} for RUNSEQ {rs1.name}")
                    errc1 += 1
                if len(ff1) > 1 : 
                    print(f"Error : Found more than one ROUT with name {rt1} for RUNSEQ {rs1.name}")
                    errc1 += 1
        for rt1 in self.objects["ROUT "] :
            for tk1, ch1, int1, *rtt in rt1.data :
                ff1 = list(filter(lambda cc1: cc1.name == ch1 , self.objects["CHANN "]))
                if len(ff1) == 0 : 
                    print(f"Error : Could not find a CHANN with name {ch1} for ROUT {rt1.name}")
                    errc1 += 1
                if len(ff1) > 1 : 
                    print(f"Error : Found more than one CHANN with name {ch1} for ROUT {rt1.name}")
                    errc1 += 1

        if errc1 > 0 :
            raise(Exception(f"Errors have been detected parsing the file '{self.file}'"))
    def factory(self, nm1, dd1):
        def aghelp(a1, a2, indx1):
            try:
                t1 = a1[indx1]
                return(t1)
            except IndexError :
                t1 = a2[indx1]
                return(t1)
        if nm1 == "CHANN " : 
            a1, *a2 = dd1[0].split(" ")
            if len(a2) != 2 : raise(Exception(f"{nm1} line format error - {dd1[0]}"))
            return(Chann(a2[0], {"PIN" : a2[1]} ))
        if nm1 == "ROUT " : 
            (hd1, *body1, footer1) = dd1
            aa1, *aa2 = hd1.split(" ")
            aa2x = ["XX", 0,0,3]
            if len(aa2) == 0  : raise(Exception(f"{nm1} line format error - {dd1}"))
            return(Rout(aa2[0], [[Tick(a1), a2, Intensity(a3)] + a4 for a1,a2,a3,*a4 in [bb1.split(" ") for bb1 in body1]], aghelp(aa2,aa2x,1), aghelp(aa2,aa2x,2), aghelp(aa2,aa2x,3) ))
        if nm1 == "RUNSEQ" : 
            (hd1, *body1, footer1) = dd1
            aa1, *aa2 = hd1.split(" ")
            if len(aa2) != 1 : raise(Exception(f"{nm1} line format error - {dd1}"))
            return(Runplan(aa2[0], [[a1] + [int(aa3) for aa3 in a4] for a1,*a4 in [bb1.split(" ") for bb1 in body1] ]))
        print(f"Dunno - {nm1} -- {dd1}")
    def populate(self):
        for ii in range(len(self.pattPairs)):
            nm1 = self.pattPairs[ii][0]
            for dd1 in self.parseData[ii]:
                self.objects.setdefault(nm1, []).append( self.factory(nm1, dd1) )

    def parse(self):
        class Dummy():
            pass
        hhc2 = Dummy()
        hhc2.flg1 = 99; hhc2.ta1 = [[] for ii in range(len(self.pattPairs))]
        def helper(dd1, hhc1):
            if hhc1.flg1 == 99 :
                for ii in range(len(self.pattPairs)):
                    if dd1.startswith(self.pattPairs[ii][0]):
                        hhc1.ta1[ii] += [[dd1]]
                        if self.pattPairs[ii][1] is not None:
                            hhc1.flg1 = ii
            else:
               hhc1.ta1[hhc1.flg1][-1].append(dd1)
               if dd1.startswith(self.pattPairs[hhc1.flg1][1]):
                   hhc1.flg1 = 99
        for dd2 in self.data : helper(dd2.strip(), hhc2) 
        self.parseData = hhc2.ta1
    def load(self):
        self.parse()
        self.populate()
        #self.validate()

def squarewave(width, hightime, color, name="squarewave"):
    return(Rout(name, [[Tick(1), color, Intensity(255)], [Tick(hightime), color, Intensity(0)],[Tick(width), color, Intensity(0)]],repeat=100))
def trianglewave(width, hightime, color, name="trianglewave"):
    return(Rout(name, [[Tick(1), color, Intensity(1), "Ramp"], [Tick(hightime), color, Intensity(255),"Ramp"],[Tick(width), color, Intensity(0)]],repeat=100))
def sawtooth(width, color,  name="sawtooth"):
    return(Rout(name, [[Tick(1), color, Intensity(1), "Ramp"], [Tick(width), color, Intensity(255)]],repeat=100))
def negsawtooth(width, color,  name="sawtooth"):
    return(Rout(name, [[Tick(1), color, Intensity(255), "Ramp"], [Tick(width), color, Intensity(0)]],repeat=100))

# def evaluator1(arr1):

#     for index in range(len(arr1)):
#         item = arr1[index]
#         if type(item)==list:
#             arr1[index] = evaluator1(item)
#     else:

#         accum = arr1.pop(0)

#         for ii in range(len(arr1)//2):
            
#             accum = eval(f"{accum}" + arr1[0] + f"{arr1[1]}")
#             arr1.pop(0)
#             arr1.pop(0)
        
#         return accum

# it = [1,'+',2,'+',[3,'+',4],'+',100]
# print(evaluator1(it))

if __name__ == "__main__" :
    import led_play3 as lpp
    led1 = lpp.LEDDef("led01.txt")
    led1.load()
    # print(led1.data)
    # print(led1.parseData)
    # print(led1.objects)
    # print(led1.objects["ROUT "][0])
    # print(led1.objects["ROUT "][1].getvalues(lpp.Tick(7)))
    
    # for item in led1.objects["ROUT "]:
    #     print(item.name)
    
    # ABC = led1.objects["ROUT "][0]
    # PQR = led1.objects["ROUT "][1]

    # print(ABC)
    # print('-----------------------')
    # print(PQR)
    # print('-----------------------')
    # f = ABC << PQR
    # print(f)
    # for ii in range(1, 50):
    #     # print(f"ii={ii}  retV={pqr.getvalues(Tick(ii))}")
    #     print(f"ii={ii}  retV={pqr[ii]}")