def parser(filename):
    with open(filename) as file:
        data = [line.strip().split(' ') for line in file]

    for line in data:
        line[0] = int(line[0])
        line[2] = int(line[2])

    return data

def sorter(data):
    data2 = sorted(data, key=lambda x : x[0])
    return data2

def separator(data):
    red = [line for line in data if line[1]=='R']
    green = [line for line in data if line[1]=='G']
    blue = [line for line in data if line[1]=='B']

    return {"R" : red, "G" : green, "B" : blue}

def stepfn(start_int, end_int, start_time, end_time):

    #int stands for intensity
    def inner(time):
        print(f"step function for intensity {start_int}")
        return start_int

    return inner

def rampfn(start_int, end_int, start_time, end_time):

    #rise over run
    gradient = (end_int - start_int) / (end_time - start_time)

    def inner(time):
        ret = start_int + gradient * (time - start_time)
        print(f"ramp function currently doing {ret}")
        return ret

    return inner
