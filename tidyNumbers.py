import os


def tidynum(num):
    # type: (str) -> str
    """
    Function to find closest
    tidy number smaller than the
    given number
    """
    # convert the input string  into a list of chars into a list of integers
    num = map(int, list(num))
    for i in range(len(num) - 2, -1, -1):
        # check  tidy property
        if num[i] > num[i + 1]:
            # if  violates,
            # then decrease the value stored at that index by 1
            # and replace all the value right to its index by 9
            num[i] -= 1
            for j in range(i + 1, len(num)):
                num[j] = 9
    # convert the result from a list of integers into a list of chars
    num = [str(i) for i in num]
    # convert the result from a list of chars into a string
    return "".join(num)


def testfile(filename):
    # type: (str) -> none
    """
    Function to process a file
    by its name
    """
    # open read file
    filein = open(filename, 'r')
    # open close file, same name of the input file but with additional prefix
    fileout = open(os.path.splitext(filename)[0] + 'Output.txt', 'w')
    # read the first line containing the number of test cases
    t = filein.readline()
    # represents the index of the current case
    i = 1
    # loop over the file lines - each contains a string value represents the number to be tested
    for n in filein:
        # write the result into the output file
        fileout.write("Case #" + str(i) + ": " + tidynum(n.strip()).lstrip('0') + "\n")
        i = i + 1
    # close opened files
    filein.close()
    fileout.close()


# driver code - pass test files by its name
testfile('B-small-practice.in')
testfile('B-large-practice.in')
