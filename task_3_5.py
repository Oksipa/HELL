# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
import random

def get_jokes(n, repeat_words=False):
    '''Возвращает n шуток, сформированных из трех случайных слов'''

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = []
if not repeat_words:
    random.shuffle(nouns)
    random.shuffle(adverbs)
    random.shuffle(adjectives)
for num, (nouns, adverbs, adjectives) in enumerate(zip(nouns, adverbs, adjectives)):
    jokes.append(f'{nouns} {adverbs} {adjectives}')
    if num == n:
        break
else:
    for _ in range(n):
        jokes.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
return jokes
