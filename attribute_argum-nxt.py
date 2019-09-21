"""carros = {
    "fabricante": "Fiat",
    "modelo": "Pálio",
    "ano": 2014
}
print(carros["fabricante"])
print(carros["modelo"])
print(carros["ano"])
x = carros["fabricante"]
print(x)
y = carros.get("modelo")
print(y)
carros["ano"] = 2013
print(carros["ano"])

for i in carros:
    print(f'{i.upper()} : {carros[i]}')


print()

carros["cor"] = "vermelho"
for a, b in carros.items():
    print(f'{a.upper()}:{b}')


print(len(carros))
carros.pop("modelo")

print()

for a, b in carros.items():
    print(f'{a.upper()}:{b}')

print()

carros.popitem()

for a, b in carros.items():
    print(f'{a.upper()}:{b}')

print()

del carros["fabricante"]

for a, b in carros.items():
    print(f'{a.upper()}:{b}')

print()

carros.clear()

for a, b in carros.items():
    print(f'{a.upper()}:{b}')

cars = carros.copy()

for a, b in cars.items():
    print(f'{a.upper()}:{b}')

print()

carros_br = dict(carros)
for a, b in carros_br.items():
    print(f'{a.upper()}:{b}')"""
fabrica_carros = {
    "carro1": {
        "fabricante": "Toyota",
        "modelo": "Prius",
        "ano": "2010"
    },
    "carro2": {
            "fabricante": "Peugeot",
            "modelo": "3006",
            "ano": "2010"
        },
    "carro3": {
            "fabricante": "Audi",
            "modelo": "A10",
            "ano": "2010"
        },
    "carro4": {
            "fabricante": "Dodge",
            "modelo": "Ram",
            "ano": "2009"
        }
    }
print(fabrica_carros["carro3"])

for c in fabrica_carros.items():
    for d in c:
        print(d)