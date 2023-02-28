def print_lines(lines):
    total = 0
    numLines = int(lines[0])
    validAddition = False
    if numLines == 0 or numLines == -999:
        print("EMPTY")
        return "EMPTY"
    for i in range(1,int(lines[0])+1):
        if int(lines[i]) == -999 and validAddition:
            print(total)
            return total
        elif int(lines[i]) == -999 and not validAddition:
            print("EMPTY")
            return "EMPTY"
        elif int(lines[i]) >= 0:
            total += int(lines[i])
            validAddition = True
    if not validAddition:
        print("EMPTY")
        return "EMPTY"
    print(total)
    return total
##########################
if __name__=="__main__":
    filename = input()

    with open(filename) as data_file:
        lines:list[str] = data_file.readlines()

    print_lines(lines)
