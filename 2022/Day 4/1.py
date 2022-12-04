with open('input', 'r+') as f:
    
    total_pairs = 0

    for item in f.readlines():
        one, two, three, four = [int(i) for j in item.strip().split(',') for i in j.split('-') ]

        if((one >= three and two <=four) or (one <= three and two >= four)):
            total_pairs += 1
    print(total_pairs)