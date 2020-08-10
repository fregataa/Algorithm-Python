# cheapBurger = int(input())
# for i in range(2):
#     newBurger = int(input())
#     if newBurger < cheapBurger:
#         cheapBurger = newBurger 

# cheapDrink = int(input())
# newDrink = int(input())
# if newDrink < cheapDrink:
#     cheapDrink = newDrink

# print(cheapBurger + cheapDrink - 50)

menuList = [0]*5
# menuList = []

for i in range(5):
    menuList[i] = int(input())

print(min(menuList[0:3]) + min(menuList[3:5]) - 50)