def commaCode(list):
    spamStr = ''
    for l in range(len(list)):
        if l < len(list) - 1:
            spamStr = spamStr + list[l] + ', '
        elif l == len(list) - 1:
            spamStr = spamStr + 'and ' + list[l]
    print(spamStr)

spam = ['apples', 'bananas', 'tofu', 'cats']
commaCode(spam)
