from typing import List

def read_file(filename='input.txt') -> str:
    with open(filename) as f:
        content = f.readlines()
    return content

def clean_raw_input(content: str) -> List[List[int]]:
    spreadsheet = []
    for column in content:
        row = column.replace('\n', '').split('\t')
        row = list(map(int, row))
        spreadsheet.append(row)
    return spreadsheet

def find_divisible_value(row: List[int]) -> int:
    for x in row:
        for y in row:
            if x != y:
                if x % y == 0:
                    return x // y
                elif y % x == 0:
                    return y // x
    raise Exception()

def calculate_checksum(spreadsheet: List[List[int]]) -> int:
    total = 0
    for row in spreadsheet:
        total += find_divisible_value(row)
    return total

spreadsheet = clean_raw_input(read_file())
answer = calculate_checksum(spreadsheet)
print(answer)

