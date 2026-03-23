phrases = input().split(';')
lengths = []
for phrase in phrases:
    word_count = 0
    in_word = False
    for ch in phrase:
        if ch != ' ':
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False
    lengths.append(word_count)
print(phrases)
print(lengths)