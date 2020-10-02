import re

def find(str):
    set_list = []
    str = str.lower()
    p = re.compile('[a-z][a-z]')
    for i in range(len(str)-1):
        c = str[i] + str[i+1]
        if not p.match(c):
            continue
        set_list.append(c)
    return set_list
    
def solution(str1, str2):
    set1 = find(str1)
    set2 = find(str2)
    if not (set1 or set2):
        return 65536
    orer, ander = len(set1+set2), 0
    for s in set1:
        if s in set2:
            ander += 1
            set2.remove(s)
    orer -= ander
    return int(ander/orer*65536)

