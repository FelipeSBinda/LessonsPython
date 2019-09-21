carros = {
    "fabricante": "Fiat",
    "modelo": "Pálio",
    "ano": 2014
}
"""print(carros["fabricante"])
print(carros["modelo"])
print(carros["ano"])
x = carros["fabricante"]
print(x)
y = carros.get("modelo")
print(y)
carros["ano"] = 2013
print(carros["ano"])"""
for i in carros:
    print(f'{i.upper()} : {carros[i]}')
