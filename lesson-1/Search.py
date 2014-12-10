

# A linear search algorithm
def findLinear(val, values):
    position = 0
    found = False
    while position < len(values) and not found:
        if values[position] == val:
            break;
        else:
            position = position + 1

    return position

# A binary search algortihm


def main():
    values = [1,2,3,4,5,6,7,8,9,10]
    val = 6
    pos = findLinear(val, values)
    print "Found: " + str(val) + " at index: " + str(pos)

if __name__ == "__main__":
    main()
