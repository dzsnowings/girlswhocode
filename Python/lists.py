groceries = ["milk", "blueberries", "bagels", "ramen", "cabbages"]
names = ["Billy", "Bob", "Joe"]
fruits = [["Billy", "Bob", "Joe"],"apples", "bananas", "peaches", "pineapples", "plums"]
numbers = [1, 2, 3, 4, 5]

fruits[0][1]
#prints: Bob
numbers.append([6, 7])
#prints: [1, 2, 3, 4, 5, [6, 7]]
numbers.extend([6, 7])
#prints: [1, 2, 3, 4, 5, 6, 7]
t = (6, 7, 8, 9)
#prints: (6, 7, 8, 9)
names.index("Joe")
#prints: 2

def OnList(str milk, groceries[]):
    for i in groceries:
        if item == milk:
            print("True")
