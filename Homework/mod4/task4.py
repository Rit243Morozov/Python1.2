def build_palindrome(s):
    cnt = {}
    for ch in s:
        cnt[ch] = cnt.get(ch, 0) + 1
    
    odd_cnt = 0
    middle = ''
    for ch, val in cnt.items():
        if val % 2:
            odd_cnt += 1
            middle = ch
    
    if odd_cnt > 1:
        return None
    
    half = []
    for ch, val in cnt.items():
        half.append(ch * (val // 2))
    
    left = ''.join(half)
    right = left[::-1]
    
    if odd_cnt:
        return left + middle + right
    return left + right

text = input().strip()
res = build_palindrome(text)
if res:
    print(res)
else:
    print("Невозможно составить палиндром")