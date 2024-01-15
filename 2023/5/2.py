import re


def get_input_from_file():

    with open('input', 'r+') as f:

        data = f.read()
        return data

def get_mapped_data_by_value(mapped_data, key):

    for i in range(0, len(mapped_data), 3):

        dest = int(mapped_data[i])
        source = int(mapped_data[i+1])
        length = int(mapped_data[i+2])

        if(key >= source and key < source + length):
            return dest + (key - source)

    return key

def get_minimum_location(input_data):

    input_data = re.sub(r'\n+', ' ', input_data)

    regex = r'(seeds: [0-9 ]+)(seed-to-soil map: [0-9 ]+)(soil-to-fertilizer map: [0-9 ]+)(fertilizer-to-water map: [0-9 ]+)(water-to-light map: [0-9 ]+)(light-to-temperature map: [0-9 ]+)(temperature-to-humidity map: [0-9 ]+)(humidity-to-location map: [0-9 ]+)'

    matches = re.findall(regex, input_data)

    seeds = list(filter(lambda x: x != '', matches[0][0].split(' ')[1:]))

    seed_to_soil_map = list(filter(lambda x: x != '', matches[0][1].split(':')[1:][0].split(' ')))

    soil_to_fertilizer_map = list(filter(lambda x: x != '', matches[0][2].split(':')[1:][0].split(' ')))

    fertilizer_to_water_map = list(filter(lambda x: x != '', matches[0][3].split(':')[1:][0].split(' ')))

    water_to_light_map = list(filter(lambda x: x != '', matches[0][4].split(':')[1:][0].split(' ')))

    light_to_temperature_map = list(filter(lambda x: x != '', matches[0][5].split(':')[1:][0].split(' ')))

    temperature_to_humidity_map = list(filter(lambda x: x != '', matches[0][6].split(':')[1:][0].split(' ')))

    humidity_to_location_map = list(filter(lambda x: x != '', matches[0][7].split(':')[1:][0].split(' ')))

    MIN_LOCATION = None

    CACHE = {}
    for i in range(0, len(seeds), 2):

        seed_pos = int(seeds[i])
        seed_range = int(seeds[i+1])
        
        for item in range(seed_pos, seed_pos+seed_range):

            seed = int(item)
            print(seed)

            if(seed in CACHE):
                continue

            soil = get_mapped_data_by_value(seed_to_soil_map, seed)

            fertilizer = get_mapped_data_by_value(soil_to_fertilizer_map, soil)

            water = get_mapped_data_by_value(fertilizer_to_water_map, fertilizer)

            light = get_mapped_data_by_value(water_to_light_map, water)

            temperature = get_mapped_data_by_value(light_to_temperature_map, light)

            humidity = get_mapped_data_by_value(temperature_to_humidity_map, temperature)

            location = get_mapped_data_by_value(humidity_to_location_map, humidity)

            if(not MIN_LOCATION or location < MIN_LOCATION):
                MIN_LOCATION = location 

            CACHE[seed] = location

    return MIN_LOCATION

if __name__ == '__main__':

    input_data = get_input_from_file()

    MIN_LOCATION = get_minimum_location(input_data)

    print(MIN_LOCATION)