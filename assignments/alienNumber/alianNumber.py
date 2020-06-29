import os


class AlianNumberTranslator(object):
    def __init__(self, str_number, str_src_system, str_target_system):
        self._str_number = str_number.strip()
        self._str_src_system = str_src_system.strip()
        self._str_target_system = str_target_system.strip()
        self._list_str_number = self._extract_reversed_list()

    def translate(self):

        self._validate_inputs()
        self._check_duplicate_in_src_and_target_systems()
        base_src_system, base_target_system = self._calculate_src_and_target_bases()
        decimal_value_number = self._convert_to_decimal(base_src_system)
        list_indexes_result = self._convert_from_decimal_to_list_of_indexes_of_target_system(base_target_system,
                                                                                             decimal_value_number)
        str_result_without_leading_zeros = self._convert_from_list_of_indexes_to_string_result(list_indexes_result)
        return str_result_without_leading_zeros

    def _convert_from_list_of_indexes_to_string_result(self, list_indexes_result):
        str_result = []
        for index in list_indexes_result:
            str_result.append(self._str_target_system[index])
        str_result.reverse()
        str_result_without_leading_zeros = "".join(str_result).lstrip(self._str_target_system[0])
        return str_result_without_leading_zeros

    def _convert_from_decimal_to_list_of_indexes_of_target_system(self, base_target_system, decimal_value_number):
        list_indexes_result = []
        while decimal_value_number > 0:
            list_indexes_result.append(decimal_value_number % base_target_system)
            decimal_value_number //= base_target_system
        return list_indexes_result

    def _convert_to_decimal(self, base_src_system):
        decimal_value_number = 0
        running_index = 0
        for digit in self._list_str_number:
            decimal_value_number += self._str_src_system.index(digit) * (base_src_system ** running_index)
            running_index = running_index + 1
        return decimal_value_number

    def _extract_reversed_list(self):
        list_str_number = list(self._str_number)
        list_str_number.reverse()
        return list_str_number

    def _calculate_src_and_target_bases(self):
        base_src_system = len(self._str_src_system)
        base_target_system = len(self._str_target_system)
        return base_src_system, base_target_system

    def _check_duplicate_in_src_and_target_systems(self):
        if len(list(self._str_src_system.strip())) is not len(set(self._str_src_system.strip())):
            raise Exception("Duplicate is not accepted in src system")
        if len(list(self._str_target_system.strip())) is not len(set(self._str_target_system.strip())):
            raise Exception("Duplicate is not accepted in target system")

    def _validate_inputs(self):
        # validate inputs
        if not isinstance(self._str_number, str) \
                or not isinstance(self._str_src_system, str) \
                or not isinstance(self._str_target_system, str):
            raise Exception("Invalid Input(s)")


class FileTester:
    def __init__(self, file_name):
        self._file_name = file_name
        pass

    def test_File(self):
        self._validate_input()
        self._check_file_existence()
        filein, fileout = self._open_input_and_output_files()
        number_test_cases = self._read_number_of_test_cases(filein)
        self._convert_cases_in_input_file(filein, fileout, number_test_cases)
        # close opened files
        self._close_input_and_output_files(filein, fileout)

    def _open_input_and_output_files(self):
        filein = open(self._file_name, 'r')
        fileout = open(os.path.splitext(self._file_name)[0] + 'Output.txt', 'w')
        return filein, fileout

    def _check_file_existence(self):
        if not os.path.isfile(self._file_name):
            raise Exception("File Not Found")

    def _validate_input(self):
        if not isinstance(self._file_name, str):
            raise Exception("Invalid Input: File name "
                            "should be in string format")

    def _close_input_and_output_files(self, filein, fileout):
        filein.close()
        fileout.close()

    def _convert_cases_in_input_file(self, filein, fileout, number_test_cases):
        running_index = 1
        for input_case in filein:
            split_input_case = input_case.strip().split()
            str_result = AlianNumberTranslator(split_input_case[0], split_input_case[1], split_input_case[2]).translate()
            assert isinstance(str_result, str)
            fileout.write("Case #" + str(running_index) + ": " + str_result + "\n")
            running_index = running_index + 1
            number_test_cases = number_test_cases - 1
            if number_test_cases is 0:
                break

    def _read_number_of_test_cases(self, filein):
        try:
            number_test_cases = int(filein.readline().strip())
        except Exception:
            raise Exception("Number of test cases should be an integer")
        return number_test_cases
