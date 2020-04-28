def is_substring(substring, string):
    """Function that returns true or false if the substring is 
    contained within the string.
    """
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False

# This one should return False
print(is_substring('bad', 'abracadabra'))
# This one should return True
print(is_substring('dab', 'abracadabra'))



def count_substring(string, target):
    """ Counts how many times the target letter or word appears
    in the string.
    """
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
        index += 1 
    return total

# Here's a call you can test it with. This should print 4:
print(count_substring('love, love, love, all you need is love', 'love'))

def count_substring2(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index += len(target)   # <- This is the key line
        else:
            index += 1
    return total


print(count_substring2("AAAA", "AA"))


def locate_first(string, sub): 
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            return index
        else:
            index += 1
    return -1


def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches