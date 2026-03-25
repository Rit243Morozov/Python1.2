text = input()
matches = []
i = 0
n = len(text)
while i < n - 18:
    if (text[i+4] == '-' and text[i+7] == '-' and text[i+10] == ' ' and 
        text[i+13] == ':' and text[i+16] == ':'):
        year = text[i:i+4]
        month = text[i+5:i+7]
        day = text[i+8:i+10]
        hour = text[i+11:i+13]
        minute = text[i+14:i+16]
        second = text[i+17:i+19]
        if (year.isdigit() and month.isdigit() and day.isdigit() and 
            hour.isdigit() and minute.isdigit() and second.isdigit()):
            y = int(year)
            m = int(month)
            d = int(day)
            h = int(hour)
            mn = int(minute)
            s = int(second)
            if (2000 <= y <= 2099 and 1 <= m <= 12 and 1 <= d <= 31 and 
                0 <= h <= 23 and 0 <= mn <= 59 and 0 <= s <= 59):
                matches.append(text[i:i+19])
    i += 1
for match in matches:
    print(match)