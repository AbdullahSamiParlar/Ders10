


f = open('form.txt', 'w', encoding='utf-8')
text = '...'
f.write(text)
f.close()

f = open('form.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()