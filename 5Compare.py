a = int( input("Input a number: "))


def difference(a):
    if a <= 17:
        return 17 - a
    else:
        return (a - 17)*2

print(difference(a))