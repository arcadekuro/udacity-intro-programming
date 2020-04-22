for x in range(16):
    if x % 3 == 0:
        print("Fizz")
        if x % 5 == 0:
            print("buzz")
    else:
        if x % 5 == 0:
            print("buzz")
        else:
            print(x)