import runplan as rp
import led_play3 as lp3

led1 = lp3.LEDDef("led01.txt")
led1.load()
print("LED HAS BEEN LOADED!")
print()

routs = led1.objects['ROUT ']

print("THE LED1 ROUTS ARE")
print(routs)
print()


str1 = "ABC + PQR * 2 + (ABC + 1000 + PQR * 3) << PQR"
rpitem = rp.RunPlan([str1])
#rpitem.exps is an array, each array is an expression

print([ii for ii in rpitem.exps])

#for now we just pass the evaluator the exps and the data structure to pluck it from separately
#evaluator takes exp and routs

#exp is an array of strings
for exp in rpitem.exps:
    print(f"starting evaluator for {exp}")
    print(rp.evaluator(exp, routs))