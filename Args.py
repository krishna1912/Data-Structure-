def add(*args):
    sum=0
    stuff = list(args)
    stuff[0]=0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))
