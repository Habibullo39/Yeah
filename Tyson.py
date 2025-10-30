import string
wodic = dict()
words = []
listo = []
with open(input("file name")) as f:
    data = f.read()

yeah = data.translate(str.maketrans("","",string.punctuation))
yeah = yeah.split()
for word in yeah:
    wodic[word] = wodic.get(word,0) + 1
    if word not in words:
        words.append(word)

for word in words:
    if listo == []:
        listo.append(word)
        continue
    num = listo[0]
    if wodic[word] > wodic[num]:
        listo = []
        listo.append(word)
    elif wodic[word] == wodic[num]:
        listo.append(word)

res = ", ".join(listo)
k = listo[0]
howmany = wodic[k]
if howmany == 1:
    print("all words appeared same times")
else:
    print(f"The most common word is {res}, and it appeared {howmany} times")