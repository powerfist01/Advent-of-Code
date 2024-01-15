import re

def get_input_from_file():

    with open('input', 'r+') as f:

        data = f.readlines()
        return data
    
def ways_to_reach(total_time, distance):
    ''''''
    for i in range(1, total_time):
        
        if(i*(total_time-i) > distance):
            
            return total_time - 2*i + 1

def process_data(data):
    
    time_line = re.sub(r' +', ' ', data[0].replace('Time:', '').strip())
    time_line = time_line.replace(' ', '')

    dist_line = re.sub(r' +', ' ', data[1].replace('Distance:', '').strip())
    dist_line = dist_line.replace(' ', '')

    MAX_WAYS = ways_to_reach(int(time_line), int(dist_line))
    
    return MAX_WAYS

if __name__ == '__main__':

    data = get_input_from_file()
    max = process_data(data)

    print(max)