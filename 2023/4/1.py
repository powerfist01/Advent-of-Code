

def get_scratchcards_input_From_file():

    with open('input', 'r+') as f:

        data = f.readlines()
        return data


if __name__ == '__main__':

    data = get_scratchcards_input_From_file()

    final_answer = 0

    for row in data:

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

        if(count_winning_numbers):
            final_answer += pow(2, count_winning_numbers-1)

    print(final_answer)