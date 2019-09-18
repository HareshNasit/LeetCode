def longest_consecutive(word):
    max_count = 0
    count = 1
    prev = word[0]
    curr = word[1]
    max_char = None

    for i in range(1, len(word)):
        if word[i] == prev:
            count += 1
            if count > max_count:
                max_char = word[i]
                max_count = count
        else:
            count = 1
        prev = word[i]
    return [max_char, max_count]

print(longest_consecutive("AABCAAADABBBEA"))
