def is_paranthesis_balanced(s):
    l={')':'(',']':'[','}':'{','>':'<' }
    a = []
    if len(s)==0:
        return True
    for i in s:
        if i in l and len(a)>0 and l[i]==a[-1]:
            a.pop()
        else:
            a.append(i)
    if len(a)>0:
        return False
    else:
        return True