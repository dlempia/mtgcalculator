
def build_obj(fname): 
    obj = []
    cardnames = open(fname)
    
    for line in cardnames: 
        obj.append(line.strip("\n"))

    return obj



