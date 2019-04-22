# Soru 1 - listedeki en büyük 2. sayıyı sıralama yapmadan bulun
# Question 1 - Find the second greatest number in the list
data = [635, 321, 365, 169, 653, 265, 518, 396, 784, 253, 506, 705, 152, 267, 796, 392, 504, 587, 378, 181]
dataSet = set(data)
dataSet.remove(max(dataSet))
print(max(dataSet))


# Soru 2 - words listesinde kaç farklı kelime vardır
# Question 2 - How many different words are there in the words
words = ['aba','ada','aca','aba','aba', 'aca', 'ada', 'aaa','aab','aca']

wordsSet = set(words)
print(len(wordsSet))

# Soru 3 - her bir kelimeden kaçar tane vardır
# Question 3 - How many occurrences of each word in the words

####################################
# 1. Çözüm: Try-except (1st Solution with try-except)
wordCounts = {}
for word in words:
    try:
        count = wordCounts[word]
    except KeyError:
        count = 0
    wordCounts[word] = count + 1

print("1. Çözüm:", wordCounts)
####################################
# 2. Çözüm: get metodu (2nd Solution using get method of dictionary)
wordCounts = {}
for word in words:
    count = wordCounts.get(word)
    if count:
        wordCounts[word] = count + 1
    else:
        wordCounts[word] = 1

print("2. Çözüm:", wordCounts)

####################################
# 3. Çözüm: get metodu default değer ile
# (3rd Solution using get method of dictionary with default value)
wordCounts = {}
for word in words:
    count = wordCounts.get(word, 0)
    wordCounts[word] = count + 1

print("3. Çözüm:", wordCounts)

####################################
# 4. Çözüm: comprehension ile
# (4th solution using dictionary comprehension)
wordCounts = {word: words.count(word) for word in words}
print("4. Çözüm:", wordCounts)