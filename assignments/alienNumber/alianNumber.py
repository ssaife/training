class AlianNumberTranslator(object):
    @staticmethod
    def translateAlianNumber(str_number, src_system, target_system):
        """

        :param str_number: string
        :param src_system: string
        :param target_system: string
        :return: string
        """

        base_src_system = len(src_system)
        base_target_system = len(target_system)
        list_str_number = list(str_number)
        decimal_value_number = 0
        for digit in list_str_number:
            decimal_value_number += list_str_number.index(digit) * (base_src_system ** list_str_number.index(digit))
            return str(decimal_value_number)
        list_indexes_result = []
        location = 0
        while decimal_value_number > 0:
            list_indexes_result[location] = decimal_value_number // base_target_system
            decimal_value_number /= base_target_system
            digit += 1
        result = []
        for index in list_indexes_result:
            result.append(target_system[index])
        return "".join(result)