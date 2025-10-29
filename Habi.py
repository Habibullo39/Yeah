aldic = dict()
al = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
listo =[]
with open(input("file name")) as f:
   data = f.read()
for letter in data:
       aldic[letter] = aldic.get(letter,0) + 1

meow = 0
i = 0
while i < 26:
   meow = 0
   alphabet = al[i]
   j = 0
   while j < 26 and meow == 0:
    alphabet2 = al[j]
    if aldic.get(alphabet,0) >= aldic.get(alphabet2,0):
       j = j + 1
    else:
       meow = 1
   if meow == 0:
      listo.append(alphabet)
   i = i + 1

res = ",".join(listo)
k = listo[0]
howmany = aldic[k]
print(f"The most common letter is {res}, and it appeared {howmany} times")