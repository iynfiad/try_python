import random
import time

start_time = time.time()

question = input('Ask Question : ')

random_num = random.randint(1, 6)

if random_num == 1:
    answer = 'It is certain'
elif random_num == 2:
    answer = 'It is decidedly so'
elif random_num == 3:
    answer = 'What?'
elif random_num == 4:
    answer = 'Reply hazy try again'
elif random_num == 5:
    answer = 'Ask again later'
elif random_num == 6:
    answer = 'Concentrate and ask again'
else:
    answer = 'Error'

print('magic 8 ball : ' + answer)

print (time.time() - start_time, "seconds")