with open('input', 'r+') as f:
    
    priority_sum = 0

    group_arr = {}
    arr = f.readlines()
    for i in range(0, len(arr), 3):
        first = arr[i]
        for ch in first:
            if(ch in arr[i+1] and ch in arr[i+2]):
                ch_int = ord(ch)
                priority_sum += (ch_int - 96) if ch_int >= 97 else (ch_int - 38)
                break

    print(priority_sum)