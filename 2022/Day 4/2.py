with open('input', 'r+') as f:
    
    total_pairs = 0

    for item in f.readlines():
        one, two, three, four = [int(i) for j in item.strip().split(',') for i in j.split('-') ]
        if(one in range(three, four+1) or two in range(three, four+1) or three in range(one, two+1) or four in range(one, two+1)):
            total_pairs += 1
    print(total_pairs)