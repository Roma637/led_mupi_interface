
def R_on(value):
    print(f"red is now at {value}")

def B_on(value):
    print(f"blue is now at {value}")

def G_on(value):
    print(f"green is now at {value}")

def executor(all, cbfunc):

    #all is a dictionary of dictionaries

    duration = 0

    for set_of_ticks in all.values():
        if duration < set_of_ticks['end']:
            duration = set_of_ticks['end']
        #now duration holds the max time

    print(f"duration is {duration}")

    current_functions = {clr:None for clr in all.keys()}

    for tick in range(duration+1):

        print(f"Tick - {tick} - ")

        for col in all.keys():

            print(f"    for colour {col}", end=" - ")

            #if a change is due
            if tick in all[col].keys():
                current_functions[col] = all[col][tick]
                print(f" Setting fn for {col}  fn {current_functions[col]}  " , end="  ")

            # hash1[col](hash1["scala"](current_functions[col](tick)))
            cbfunc(current_functions[col](tick), col, tick)
