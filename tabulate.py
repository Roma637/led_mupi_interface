from parser import rampfn, stepfn

def table(colour, complete):

    work_with = complete[colour]

    pass_to_fn = []

    final_table = {}

    #extracts start time, end time, start intensity, end intensity
    for entry in range(len(work_with)-1):
        print(f"entry is now {entry}")
        temp = [work_with[entry][0], work_with[entry+1][0], work_with[entry][2], work_with[entry+1][2]]
        pass_to_fn.append(temp)
        if len(work_with[entry])>3 and work_with[entry][3]=='Ramp': #if theres an additional string that says 'ramp'
            final_table[work_with[entry][0]] = rampfn(*temp)
        else:
            final_table[work_with[entry][0]] = stepfn(*temp)

    #print(pass_to_fn)
    #print(final_table)

    return final_table
