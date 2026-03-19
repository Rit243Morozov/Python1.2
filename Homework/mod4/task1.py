def analyze_numbers():
    nums = [int(x) for x in input().split()]
    uniq = set(nums)
    if len(uniq) == 1:
        print("Все числа равны")
    elif len(uniq) == len(nums):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

analyze_numbers()