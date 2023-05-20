def length_of_last_word(s):
    result = ''
    i = len(s)

    while (i >= 0):
        if s[i] == ' ':
            if not result:
                i -= 1
            else:
                break
        else:
            i -= 1

    return len(result)


length_of_last_word('Hello World')
