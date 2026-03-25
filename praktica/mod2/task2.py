text = input()
emails = []
words = []
cur = ""
for ch in text:
    if ch == ' ':
        if cur:
            words.append(cur)
            cur = ""
    else:
        cur += ch
if cur:
    words.append(cur)
for w in words:
    if '@' in w:
        email = ""
        for ch in w:
            if ch.isalpha() or ch.isdigit() or ch in '@+_-#.':
                email += ch
        if email[-1] in ',.;:!?)':
            email = email[:-1]
        if email[0] in '("':
            email = email[1:]
        parts = email.split('@')
        if len(parts) == 2:
            local, domain = parts[0], parts[1]
            if local and domain and '.' in domain:
                if domain[0] != '.' and domain[-1] != '.':
                    emails.append(email)
for email in emails:
    print(email)