import random
with open('openrice.csv',encoding="utf-8") as f:
    foodlist = f.readlines()
foodlist =[x.strip() for x in foodlist]

#print(len(foodlist))

random_id = random.randint(0,len(foodlist))
print(foodlist[random_id])