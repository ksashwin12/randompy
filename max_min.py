def maxi(n):
    maxim=None
    for i in n:
        if maxim is None or i > maxim:
            maxim=i
    return maxim
def mini(n):
    minim=None
    for i in n:
        if minim is None or i < minim:
            minim=i
    return minim
def display(n):
    return f"The maximum is {maxi(n)} and the minimum is {mini(n)}"