# немного о строках

text = 'съешь еще этих мягких французских булок'
print(len(text))
print('еще' in text)
print(text.isdigit())
print(text.islower())
print(text.replace('еще', 'МНОГО'))
print('первая буква:')
print(text[0])
print(text[-1])  # последняя буква
print(text[:])  # print(text)
print(text[2:5])  # от второго до пятого "ешь"
print(text[0:len(text):2])  # взять с шагом 2
print(text[::2])  # взять с шагом 2 / другая запись
text = text[0:5] + " " + text[-5:-1] + text[-1]
print(text)
