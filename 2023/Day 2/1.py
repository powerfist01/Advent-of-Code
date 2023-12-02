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

def calculate_sum_of_valid_games(processed_game_data: dict):
    
    MAX_CUBES_COUNT = {
        'red': 12,
        'blue': 14,
        'green': 13
    }

    sum_of_valid_games = 0

    for game_no, game_details in processed_game_data.items():
        
        is_valid_game = True
        for cube_color, cubes_count in game_details.items():

            if(cube_color not in MAX_CUBES_COUNT or cubes_count > MAX_CUBES_COUNT[cube_color]):
                is_valid_game = False

        sum_of_valid_games += game_no if is_valid_game else 0

    return sum_of_valid_games

if __name__ == '__main__':

    games = get_game_input_data()
    processed_game_data = get_processed_game_data(games)

    valid_games_sum = calculate_sum_of_valid_games(processed_game_data)
    print(valid_games_sum)