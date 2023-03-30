from typing import Final
import re


def get_data_from_file(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.replace('\n', '') for line in f.readlines()]


def change_numbers(edi_lst, start_number):
    for i, line in enumerate(edi_lst):
        if re.match(r'<LineNumber type="PurchaseOrder">.*', line):
            number_str = re.findall(r'\d+', line)[0]  # extract the number as a string
            if int(number_str) >= start_number:
                number = int(number_str) + 1 # compute the new number using the start_number parameter
                new_line = line.replace(number_str, str(number))  # replace the old number with the new number
                edi_lst[i] = new_line  # replace the old line with the new line
    return edi_lst


def save_data_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write('\n'.join(data))


def main() -> None:
    FILENAME_1: Final[str] = 'test3'
    FILENAME_2: Final[str] = 'edi3'
    get_data = get_data_from_file(FILENAME_1)

    x = change_numbers(get_data, 11)

    save_data_to_file(FILENAME_2, x)


if __name__ == '__main__':
    main()
