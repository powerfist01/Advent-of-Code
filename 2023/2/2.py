import re

def get_game_input_data():
    
    with open('input', 'r+') as f:
        
        lines = f.readlines()
        return lines

def get_processed_game_data(games: list):
    
    processed_game_data = {}

    for game in games:
        game = game.strip()

        game_data = game.split(':')

        game_meta = game_data[0].strip()
        game_no = int(game_meta.split(' ')[1])

        game_rounds = game_data[1].strip()

        game_regex = r'(\d+ [a-z]+)'

        for _, match in enumerate(re.finditer(game_regex, game_rounds)):
            
            if(game_no not in processed_game_data):
                processed_game_data[game_no] = {}

            cubes_count = int(match.group(0).split(' ')[0])
            cubes_color = match.group(0).split(' ')[1]

            if(cubes_color not in processed_game_data[game_no]):
                processed_game_data[game_no][cubes_color] = cubes_count
            else:
                processed_game_data[game_no][cubes_color] = max(processed_game_data[game_no][cubes_color], cubes_count)

    return processed_game_data

def calculate_sum_of_minimun_cubes_required(processed_game_data: dict):
    

    sum_of_minimun_cubes = 0

    for _, game_details in processed_game_data.items():
        
        power = 1
        for _, cubes_count in game_details.items():

            power = cubes_count * power
        
        sum_of_minimun_cubes += power

    return sum_of_minimun_cubes

if __name__ == '__main__':

    games = get_game_input_data()
    processed_game_data = get_processed_game_data(games)

    sum_of_power = calculate_sum_of_minimun_cubes_required(processed_game_data)
    print(sum_of_power)