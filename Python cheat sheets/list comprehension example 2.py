#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

#The parameter of accum is a string which includes only letters from a..z and A..Z.


def accum(s):
    new_string = ''
    for i in range(len(s)):
        new_string = new_string + s[i].upper() + i * s[i] + '-'
    new_string = new_string[:-1]
    
    return new_string

print(accum("abcd"))

#better version from code wars pasted below

def accum2(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

print(accum2("abcd"))


# Third Version

def accum3(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))


"""
Created on Wed Mar 25 18:06:38 2020

@author: Deborah
"""

