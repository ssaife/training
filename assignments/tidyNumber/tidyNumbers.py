import os


class TidyNumberGenerator:
    def __init__(self):
        pass

    @staticmethod
    def findTidyNum(str_number):
        # type: (str) -> str
        """
        Function to find closest
        tidy number smaller than the
        given number
        """
        assert isinstance(str_number, str)
        # validate
        try:
            int(str_number.lstrip('-+'))
        except ValueError as e:
            assert "Invalid Input"
            raise Exception("Invalid Input")
        # check if negative
        if str_number.startswith('-'):
            raise Exception("Negative Numbers Not Accepted")
        # check if have + sign
        if str_number.startswith('+'):
            str_number = str_number[1:]

        if int(str_number) < 0:
            raise Exception("Algorithm Requires non-negative")

        # convert the input string  into a list of chars into a list of integers
        list_int_number = map(int, list(str_number))
        for index in range(len(list_int_number) - 2, -1, -1):
            # check  tidy property
            if list_int_number[index] > list_int_number[index + 1]:
                # if  violates,
                # then decrease the value stored at that index by 1
                # and replace all the value right to its index by 9
                list_int_number[index] -= 1
                for index_digit in range(index + 1, len(list_int_number)):
                    list_int_number[index_digit] = 9
        # convert the result from a list of integers into a list of chars #comprehension
        list_chars_number = [str(index) for index in list_int_number]
        # convert the result from a list of chars into a string
        return "".join(list_chars_number).lstrip('0')


class FileTester:
    def __init__(self):
        pass

    @staticmethod
    def testFile(filename):
        # type: (str) -> None
        """
        Function to process a file
        by its name
        """
        # open read file
        if not os.path.isfile(filename):
            raise Exception("File Not Found")
        filein = open(filename, 'r')
        # open close file, same name of the input file but with additional prefix
        fileout = open(os.path.splitext(filename)[0] + 'Output.txt', 'w')
        # read the first line containing the number of test cases
        t = filein.readline()
        # represents the index of the current case
        index = 1
        # loop over the file lines - each contains a string value represents the number to be tested
        for number in filein:
            # validate
            try:
                int(number.lstrip('-+'))
            except ValueError as e:
                assert "Invalid Input"
                raise Exception("Case #" + str(index) + ": Invalid Input")
                index = index + 1
                continue
            # check if negative
            if number.startswith('-'):
                raise Exception("Case #" + str(index) + ": Negative Numbers Not Accepted")
                index = index + 1
                continue
            # check if have + sign
            if number.startswith('+'):
                number = number[1:]
            # write the result into the output file without leading zeros
            number_result = findTidyNum(number.strip())
            assert isinstance(number_result, str)
            fileout.write("Case #" + str(index) + ": " + number_result + "\n")
            index = index + 1
        # close opened files
        filein.close()
        fileout.close()
