def proc(text1, text2):
    symbs = []
    for t in text2:
        if t not in symbs:
            symbs.append(t)
    for t in symbs:
        text1 = text1.replace(t, '')
    print(text1)
 
if __name__ == '__main__':
    text1 = 'как говорится все в этом прекрасном мире тлен'
    text2 = 'все тлен если не тлен'
    proc(text1, text2)
