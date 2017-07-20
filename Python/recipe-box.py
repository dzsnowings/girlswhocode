LemonIngredients = {"extra-large whole eggs:":"3", "extra-large separated eggs:":"3", "sugar:":"1 cup and 2 tbs", "grated lemon zest:":"2 tsp", "Kosher salt:":"1/8 tsp", "heavy cream:":"1 cup", "good bottled lemon curd:":"1/2 cup", "Sweetened Whipped Cream:":"1 cup", "sliced lemon:":"1"}
lemonCreamIngredients = {"cold heavy cream:":"1 cup", "sugar:":"1 tbs", "pure vanilla extract:":"1/2 tsp"}
LemonInstructions = ["whisk together the 3 whole eggs, 3 egg yolks, 1 cup sugar, the lemon zest, lemon juice, and a pinch of salt",
"Cook mixture for 10-12 minutes over pan of simmering water while constantly stirring until thick like pudding",
"Cool for 15 minutes, then cover with plastic wrap and refrigerate for 1-2 hours",
"Place half the egg whites and a pinch of salt in the bowl of an electric mixer with the whisk attachment",
"Beat on high speed, then add the reamining 2 tablespoons of sugar and beat till whites are stiff",
"Fold the beaten whites into the cold lemon mixture",
"Beat the cream on high speed with the electric mixer until stiff peaks are formed ",
"Fold in the lemon curd and pour into a 7-inch diameter, 3-inch deep souffle dish.",
"Decorate with the Sweetened Whipped Cream (recipe below)and lemon slices cut into quarters. Chill and serve cold"]
LemonCreamInstructions = ["Place the cream, sugar, and vanilla in the electric mixer fitted with whisk attachment",
"Whip on medium and then high until the cream forms still peaks",
"Spoon the whipped cream into a pastry bag fitted with a large star tip"]
ChocolateIngredients = {"whipping cream:":"1 3/4 cups", "semi-sweet chocolate chips:":"12 oz", "espresso or strong coffee:":"3 oz", "butter:":"4 tbs", "flavorless, granulated gelatin:":"1 tsp"}
ChocolateInstructions = ["Chill 1 1/2 cups whipping cream in refrigerator. Chill metal mixing bowl and mixer beaters in freezer.",
"In top of a double boiler, combine chocolate chips, coffee, and butter",
"Melt over barely simmering water, stirring constantly. Remove from heat while a couple of chunks are still visible.",
"Cool, stirring occasionally to just above body temperature.",
"Pour remaining 1/4 cup whipping cream into a metal measuring cup and sprinkle in the gelatin. Allow gelatin to 'bloom' for 10 minutes.",
"Carefully heat by swirling the measuring cup over a low gas flame or candle. Do not boil or gelatin will be damaged.",
"Stir mixture into the cooled chocolate and set aside.",
"In the chilled mixing bowl, beat cream to medium peaks.",
"Stir 1/4 of the whipped cream into the chocolate mixture to lighten it.",
"Fold in the remaining whipped cream in two doses.",
"Spoon into bowls or martini glasses and chill for at least 1 hour. Garnish with fruit and serve."]

print('What kind of mousse would you like to make? ')
user_input = input()
if user_input == "lemon":
    print("Ingredients:")
    for value,key in LemonIngredients.items():
        print(value,key)

    print ("\nInstructions:")
    for i in LemonInstructions:
        print(LemonInstructions.index(i) +1, end=' ')
        print(" ",i)

    print("\nSweetened Whipped Cream recipe:")
    for value,key in lemonCreamIngredients.items():
        print(value,key)

    print ("\nSweetened Whipped Cream Instructions:")
    for i in LemonCreamInstructions:
        print(LemonCreamInstructions.index(i) +1, end=' ')
        print(" ",i)

if user_input == "chocolate":
    print("Ingredients:")
    for value,key in ChocolateIngredients.items():
        print(value,key)

    print ("\nInstructions:")
    for i in ChocolateInstructions:
        print(ChocolateInstructions.index(i) +1, end=' ')
        print(" ",i)
