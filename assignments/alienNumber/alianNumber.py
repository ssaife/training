import os


class AlianNumberTranslator(object):
    @staticmethod
    def translateAlianNumber(str_number, src_system, target_system):
        """

        :param str_number: string
        :param src_system: string
        :param target_system: string
        :return: string
        """
        # validate inputs
        if not isinstance(str_number, str) \
                or not isinstance(src_system, str) \
                or not isinstance(target_system, str):
            raise Exception("Invalid Input(s)")
        # check duplicate in src and target systems
        if len(list(src_system.strip())) is not len(set(src_system.strip())):
            raise Exception("Duplicate i not accepted in src system")
        if len(list(target_system.strip())) is not len(set(target_system.strip())):
            raise Exception("Duplicate i not accepted in target system")
        base_src_system = len(src_system.strip())
        base_target_system = len(target_system.strip())
        list_str_number = list(str_number.strip())
        list_str_number.reverse()
        decimal_value_number = 0
        index_list_str_number = 0
        for digit in list_str_number:
            decimal_value_number += src_system.index(digit) * (base_src_system ** index_list_str_number)
            index_list_str_number = index_list_str_number + 1
        list_indexes_result = []
        while decimal_value_number > 0:
            list_indexes_result.append(decimal_value_number % base_target_system)
            decimal_value_number //= base_target_system
        str_result = []  # type: List[str]
        for index in list_indexes_result:
            str_result.append(target_system[index])
        str_result.reverse()
        return "".join(str_result).lstrip(target_system[0])


class FileTester:
    def __init__(self):
        pass

    @staticmethod
    def testFile(filename):
        """

        :param filename: string
        :return: None
        """
        # validate input
        if not isinstance(filename, str):
            raise Exception("Invalid Input: File name "
                            "should be in string format")
        # check existence
        if not os.path.isfile(filename):
            raise Exception("File Not Found")
        filein = open(filename, 'r')
        # open output file, same name of the input file but with additional prefix
        fileout = open(os.path.splitext(filename)[0] + 'Output.txt', 'w')
        try:
            number_test_cases = int(filein.readline().strip())
        except Exception:
            raise Exception("Number of test cases should be an integer")
        # represents the index of the current case
        index = 1
        # loop over the file lines - each contains a string value represents the number to be tested
        for input_case in filein:
            split_input_case = input_case.strip().split()
            # write the result into the output file without leading zeros
            str_result = AlianNumberTranslator.translateAlianNumber(split_input_case[0]
                                                                    , split_input_case[1]
                                                                    , split_input_case[2])
            assert isinstance(str_result, str)
            fileout.write("Case #" + str(index) + ": " + str_result + "\n")
            index = index + 1
            number_test_cases = number_test_cases - 1
            if number_test_cases is 0:
                break
        # close opened files
        filein.close()
        fileout.close()
