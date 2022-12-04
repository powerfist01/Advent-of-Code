with open('input', 'r+') as f:

    sum_calories = []
    elf_calories = 0
    max_calories = 0
    for item in f.readlines():
        calorie = int(item.strip()) if item.strip() else 0
        if(calorie):
            elf_calories += calorie
        else:
            sum_calories.append(elf_calories)
            max_calories = max(max_calories, elf_calories)
            elf_calories = 0

    sum_calories.append(elf_calories)      
    max_calories = elf_calories if elf_calories > max_calories else max_calories

    print(sum(list(reversed(sorted(sum_calories)))[:3]))