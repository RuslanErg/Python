# как-то получить от пользователя оценку
rate_as_str = input("оцените работу оператора от 1 до 5") # str (запишется строка)
rate=int(rate_as_str) # int (запишется число)

# проверить, что оценка от 1 до 5
if(rate<1):
    rate=1

if(rate>5):
    rate=5

print(rate)
# в зависимости от оценки, предложить дать обратную связь

feedback = ''
if rate == 1:
    feedback = input("расскажите,что нам улучшить: ")
elif rate == 2:
        feedback = input("расскажите,что вас смутило: ")
elif rate == 3:
     feedback = input("расскажите,что как нам стать лучше: ")
elif rate == 4:
     feedback = input("расскажите,почему не 5: ")
else:
    feedback = input("расскажите,за что похвалить оператора: ")
print(feedback)