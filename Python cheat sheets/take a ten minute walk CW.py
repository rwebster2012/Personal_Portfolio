def is_valid_walk(walk):
    n = 0
    s = 0
    e = 0
    w = 0
    for i in walk:
        if i == 'n':
            n += 1
            s += (-1)
        elif i == 's':
            n += -1 
            s += 1
        elif i == 'e':
            e += 1 
            w += -1
        elif i == 'w':
            e += -1 
            w += 1
    if n == 0 and s == 0 and e == 0 and w == 0 and len(walk) == 10:
        return True
    else:
        return False
    
#print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))


#simpler solution from code wars

def isValidWalk2(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

print(isValidWalk2(['n','s','n','s','n','s','n','s','n','s']))

#another solution

def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10):
            return True
    return False