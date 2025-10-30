howmn = 0
meow = 0
try: 
    with open(input("filename")) as f:
     data = f.readlines()
except:
   print("file not found")
   exit()

for line in data:
  howmn = howmn + 1

bigin = howmn - 10
for line in data:
   meow = meow + 1
   if meow > bigin:
      print(line,end="")