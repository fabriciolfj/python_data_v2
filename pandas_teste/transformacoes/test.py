import pandas as pd

data = pd.DataFrame({
    "food": ["bacon", "pulled pork", "bacon", "pastrami", "corned beef", "Bacon", "pastrami", "honey ham", "nova lox"],
    "ounces" : [4, 3, 12, 6, 7.6, 8, 3, 5, 6]
})

meat_to_animal = {
    "pastrami": "cow",
    "bacon": "pig",
    "pulled pork": "pig",
    "corned beef": "cow",
    "honey ham": "pig",
    "nova lox": "salmon"
}


data["animal"] = data["food"].map(meat_to_animal)
print(data)