def breakify(strings):
    return "<br>".join(strings)


def remove_substring(string, substring):
    # create a new list variable
    output = []
    index = 0
    while index < len(string): # loops for as long as index is less than the length of the string.
        # if the slicing result string is the same lenght of the target, skip over it/
        if string[index: index + len(substring)] == substring: 
            index += len(substring)
        else:
            #Otherwise, append the current character to ouput list and advance the index by 1
             output.append(string[index])
             index += 1
   
print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
# print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
# print(remove_substring('I am NOT learning to code.', 'NOT '))


def remove_substring2(string, substring):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)

def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(replacement)
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)