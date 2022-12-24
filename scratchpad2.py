import runplan as rp
import led_play3 as lp3

led1 = lp3.LEDDef("led01.txt")
led1.load()
# print("LED HAS BEEN LOADED!")
# print()

routs = led1.objects['ROUT ']

print("THE LED1 ROUTS ARE")
# print(routs)
# print()

# str1 = "ABC + PQR * 2 + (ABC + 1000 + PQR * 3) << PQR"
str1 = "TT"
rpitem = rp.RunPlan([str1])
#rpitem.exps is an array, each array is an expression

# print([ii for ii in rpitem.exps])

#for now we just pass the evaluator the exps and the data structure to pluck it from separately
#evaluator takes exp and routs

def printCR(x1):
    for ii in x1.routs :
        try :
            kk1 = ii.kindish(ii)
            if kk1 == "CompoundRout" :
                # print("encountered compound root")
                printCR(ii)
                pass
            else :
                print(ii)
        except Exception as ex1:
            print(ii)

def unfold(item):
    final = []
    if type(item)==lp3.CompoundRout:
        # print(f"{item} is a compound root")
        # print(f"routs are {item.routs}")
        final.extend(unfold(item.routs))
    elif type(item)==lp3.Rout:
        final.append(item)
    elif type(item)==list:
        for thing in item:
            final.extend(unfold(thing))
    return final

#exp is an array of strings
exp = rpitem.exps[0]

# print(f"starting evaluator for {exp}")
final = rp.evaluator(exp, routs)
# print(final)
# print("===========THE FINAL IS=============")
thing = unfold(final)
print(thing)
print()

for t in range(17):
    print(f"-------- tick {t} ----------")
    print(final[t])