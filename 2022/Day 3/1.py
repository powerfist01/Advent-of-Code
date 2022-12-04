with open('input', 'r+') as f:
    
    priority_sum = 0

    for item in f.readlines():
        item = item.strip()
        first, second = item[0:int(len(item)/2)], item[int(len(item)/2):len(item)]
        
        for ch in second:
            if(ch in first):
                ch_int = ord(ch)
                priority_sum += (ch_int - 96) if ch_int >= 97 else (ch_int - 38)
                break
        
    print(priority_sum)