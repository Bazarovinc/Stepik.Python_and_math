def front_x(words):
    x_first = []
    others = []
    for word in words:
        if len(word) != 0:
            if word[0] == 'x':
                x_first.append(word)
            else:
                others.append(word)
        else:
            others.append(word)
    return sorted(x_first) + sorted(others)


print(front_x(['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']))