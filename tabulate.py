from parser import rampfn, stepfn

def table(colour, complete):

    work_with = complete[colour]

    final_table = {}

    #extracts start intensity, end intensity, start time, end time,
    for entry in range(len(work_with)-1):
        #print(f"entry is now {entry}")
        temp = work_with[entry][2], work_with[entry+1][2], work_with[entry][0], work_with[entry+1][0]

        if len(work_with[entry])>3 and work_with[entry][3]=='Ramp': #if theres an additional string that says 'ramp'
            final_table[work_with[entry][0]] = rampfn(*temp)
        else:
            final_table[work_with[entry][0]] = stepfn(*temp)

    final_table['start'] = work_with[0][0]
    final_table['end'] = work_with[-1][0]

    #print(pass_to_fn)
    #print(final_table)

    return final_table

def all_colours(complete):

    #this will keep them in RGB order
    #this is assuming that colours for all 3 have been specifiedd
    all = {ii:table(ii, complete) for ii in ['R', 'G', 'B']}

    return all
