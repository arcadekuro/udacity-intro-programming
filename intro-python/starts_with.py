def starts_with_v1(long, short):
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True

def starts_with_v2(long, short):
    length = len(short)
    beginning = long[0 : length]
    if beginning == short:
        return True
    else:
        return False

def starts_with_v3(long, short):
    return long[0:len(short)] == short


starts_with_v1("tin", "tinkerbell")
#starts_with_v2("tin", "tinkerbell")
#starts_with_v3("tin", "tinkerbell")