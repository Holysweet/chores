import random

kids = ["Nick",
        "Xandra",
        "Natasha",
        "Anastasia"]

chores = ["Vaatwasser Inruimen",
          "Vaatwasser Uitruimen",
          "Wc Beneden",
          "Wc Boven",
          "Bed Verschonen",
          "Stofzuigen Beneden",
          "Stofzuigen Boven",
          "Kamer Opruimen"]


random.shuffle(kids)
random.shuffle(chores)

for i in range(len(kids)):
    print(kids[i])
    print((chores[i*2:i*2+2]))



