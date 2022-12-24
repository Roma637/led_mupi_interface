import re
from led_play3 import *

class RunPlan():
    def __init__(self, exps1):
        #exps1 is an array of expressions (strings)
        self.exps = [expression(h) for h in exps1]
        # self.seqs = [(evaluator(exp.ex)) for exp in self.exps]

    # def unfold(self,item):

    #     final = []

    #     if type(item)==CompoundRout:
    #         # print(f"{item} is a compound root")
    #         # print(f"routs are {item.routs}")
    #         final.extend(self.unfold(item.routs))
    #     elif type(item)==Rout:
    #         final.append(item)
    #     elif type(item)==list:
    #         for thing in item:
    #             final.extend(self.unfold(thing))

    #     return final

def helper(arr1, routs):

    # print(f"in helper, arr1 is {arr1}")
    # print(f"in helper, routs is {routs}")

    for plc in range(len(arr1)):
        item = arr1[plc]
        # print(f"ITEM IS {item}")
        if type(item)==list:
            helper(item, routs)
        elif type(item)==str and item.isalpha():
            for routine in routs:
                if routine.name==item:
                    arr1[plc] = routine
            else:
                pass
                # print(f"{item} not in routs :(")
        elif type(item)==str and item.isdigit():
            arr1[plc] = int(item)

    # print(f"after using helper, arr1 is now {arr1}")

def evaluator(exp, routs):
# exp is expression
# routs is the list of routines

    # print(exp)

    arr1 = exp[:]

    helper(arr1, routs)

    #OKAY SO ARR1 NOW HAS ROUTS IN IT!

    # print(arr1)
    # print()
    # print("----------FINISHED WITH HELPER----------")

    for place in range(len(arr1)):
        if type(arr1[place]) == list:
            # print(f"encountered list {arr1[place]}")
            arr1[place] = evaluator(arr1[place], routs)
            # print(f"the list is now {arr1[place]}")
            # print()
    
    accumulator = arr1.pop(0)
    # print(f"at the start, accumulator is {accumulator}")
    # print()
    
    for ii in range(len(arr1)//2):
        # print(f"{arr1[2*ii]}")
        # print(f"{arr1[2*ii + 1]}")

        other = arr1[1]
        # print(f"other is {other} and its type is {type(other)}")

        # to_carry_out = f"accumulator" + arr1[0] + f"{arr1[1]}"
        # print("going to carry out "+to_carry_out)
        # print()

        accumulator = eval(f"accumulator {arr1[0]} other")
        arr1.pop(0)
        arr1.pop(0)
        
        # print(f"accumulator is now {accumulator}")
        # print()

    # print(f"going to return {accumulator}")
    return accumulator

def expression(ex1):

    def parser(ex1):
        rx1 = re.split(r"(\W)", ex1)
        marr2 = [ii for ii in rx1 if re.search(r"\S", ii)]
        marr1 = []
        for ii in range(len(marr2)):
            if ii > 0 and marr2[ii] == marr2[ii - 1]:
                marr1[-1] += marr2[ii]
            else:
                marr1 += [marr2[ii]]

        # print(f"STEP 1 {marr1}")
        return marr1
    def parcompile(arr1) :
        #this turns parantheses into arrays
        narr1 = []
        ii2 = -1; iib1 = 0

        for ii in range(len(arr1)):
            val1 = arr1[ii] 
            if ii > (ii2 + iib1):
                if val1 == "(" :
                    (retv1, ii2) = parcompile(arr1[ii + 1:])
                    iib1 = ii + 1
                    narr1 += [retv1]
                elif val1 == ")" :
                    return((narr1, ii))
                else :
                    narr1 += [val1]
            # else:
                # print("skippint " + val1)
        
        # print(f"STEP 2 {narr1}")
        return((narr1, ii2))

    def mulmaker(arr1, ch1="*"):
        #this turns multiplication into arrays but you can pass other things

        narr1 = []
        ii = 0

        while ii<len(arr1):

            # print(f"in mulmaker, ii in {ii}")
            # print(narr1)

            if type(arr1[ii]) == list:
                narr1.append(mulmaker(arr1[ii]))
    #        elif arr1[ii] != ch1:
            elif arr1[ii] not in [ch1]:
                # print("No star  " , arr1[ii])
                narr1.append(arr1[ii])
            else:
                # print("Star  " , arr1[ii])
                narr1.pop()
                narr1.append(arr1[ii-1:ii+2])
                ii += 1
            
            ii += 1
    
        return narr1

    ex = mulmaker(mulmaker(parcompile(parser(ex1))[0]), "/")
    return ex

if __name__=="__main__":
    str1 = expression("ABC + PQR * 2 / CC + (ABC + 1000 + PQR * 3 / 30) << PQR")
    print(str1)

# def parsolve(arr1):
#     #every odd number should have an operand
#     arr1 = (int(ii) for ii in arr1 if ii.isint())

#NOTES
# evaluator function that takes in array and interprets it
# make executor understand [rout1, rout2]
# and then just do it !!