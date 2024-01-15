
def get_the_proble_input_from_file():

    with open('input', 'r+') as f:

        data = f.readlines()
        return data

def check_for_valid_number(number, row_idx, col_idx, input):

    if(not number): return 0

    start_row = row_idx - 1 if row_idx-1 >= 0 else 0
    end_row = row_idx + 1 if row_idx+1 < len(input) else len(input) - 1

    start_col = col_idx - len(number) - 1 if col_idx - len(number) - 1 > 0 else 0
    end_col = col_idx

    for row in range(start_row, end_row+1):

        for col in range(start_col, end_col+1):
            
            if(input[row][col] != '.' and not input[row][col].isdigit()):
                # print('yaassss', row, col)
                return int(number)

    return 0

def process_input_for_answer(input):

    total_sum = 0

    for row_idx, row in enumerate(input):

        row_str = row.strip()
    
        number = ''
        for col_idx, ch in enumerate(row_str):
            
            if(ch.isdigit()):
                number += ch
            else:
                number = check_for_valid_number(number, row_idx, col_idx, input)
                total_sum += number

                number = ''
        
        number = check_for_valid_number(number, row_idx, col_idx, input)
        total_sum += number

    return total_sum

if __name__ == '__main__':

    data = get_the_proble_input_from_file()

    total_sum = process_input_for_answer(data)
    print(total_sum)
