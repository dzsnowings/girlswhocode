from random import randint
randomNumber = randint(0, 9)

sides = ['coleslaw', 'buttered corn', 'mashed potatoes', 'salad', 'soup']
mainCourses = ['beef enchiladas', 'coconut shrimp', 'chicken fingers', 'spaghetti', 'meatloaf']
desserts = ['pie', 'cheesecake', 'ice cream', 'cookie', 'brownie']

print("Side: " + sides[randomNumber])
print("Main Course: " + mainCourses[randomNumber])
print("Dessert: " + desserts[randomNumber])
