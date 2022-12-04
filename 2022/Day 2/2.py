with open('input', 'r+') as f:

    winning_arr = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]
    
    total_points = 0

    for item in f.readlines():
        first, second = item.strip().split(' ')
        total_points += winning_arr[ord(first)-65][ord(second)-88]

    print(total_points)