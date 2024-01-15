

def get_scratchcards_input_From_file():

    with open('input', 'r+') as f:

        data = f.readlines()
        return data


if __name__ == '__main__':

    data = get_scratchcards_input_From_file()

    final_answer = 0

    TOTAL_DICT = {}
    for idx, row in enumerate(data):
        
        if(idx+1 in TOTAL_DICT):
            TOTAL_DICT[idx+1] += 1
        else:
            TOTAL_DICT[idx+1] = 1

        row = row.strip()
        
        row = row.split(':')

        row = row[1].replace('  ', ' ').strip()

        lists = row.split(' | ')

        winning_numbers = set()

        for item in lists[0].split(' '):
            winning_numbers.add(item)

        count_winning_numbers = 0
        for item in lists[1].split(' '):
            if(item in winning_numbers):
                count_winning_numbers += 1

        for j in range(TOTAL_DICT[idx+1]):
            for i in range(idx+2, idx+count_winning_numbers+2):
                if(i in TOTAL_DICT):
                    TOTAL_DICT[i] += 1
                else:
                    TOTAL_DICT[i] = 1

    SUM = 0

    for key, val in TOTAL_DICT.items():

        SUM += val

    print(SUM)