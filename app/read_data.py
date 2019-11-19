data = []
with open('E:/work/python/usually/webapp/static/vedio', 'r', encoding='utf-8') as f:
    for i in f:
        if i[0] != 'h':
            text = i.replace('    ', '').split(' ')
            print(text[len(text) - 2:])
            data.append(text[len(text) - 2:])
        else:
            print(i)
            data.append(i)
print(data)

