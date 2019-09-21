lista_frutas = ['maça', 'banana', 'manga', 'abacaxi', 'melancia']
print(lista_frutas)

fiat = ['Cronos', 'Mobi', 'Argo', 'Uno']
volks = ['Up', 'Gol', 'Polo', 'Fox']
print(fiat == volks)
fiat = ['Cronos', 'Mobi', 'Argo', 'Uno']
volks = ['Up', 'Gol', 'Polo', 'Fox']
print(fiat == volks)
print(fiat is volks)
a = ['maca', 50,'True', 3.54]
print(a)
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
fiat = ['Cronos', 'Mobi', 'Argo', 'Uno']
volks = ['Up', 'Gol', 'Polo', 'Fox']
fiat = volks
print (fiat is volks)
a = ['maca', 50,'True', 3.54]

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
print(a[0])
print(a[2])
print(a[5])
print(a[-1])
print(a[-2])
print(a[-5])

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
b = a[2:5]
print(b)
print(a[1])
print(a[2:])

b = a[:5]
print(b)

fruta = ['banana', 'maça', 'uva', 'pera']
for c in fruta:
    print(c)
print(len(fruta))

for c in fruta:
    print(c)
    print('*****')
for c in fruta:
    print(c, end=" ")

    fruta = ['maça', 'banana', 'pera', 'abacate']
    print('banana' in fruta)
    print('abacaxi' in fruta)
    if 'banana' in fruta:
        print('Temos banana')
    else:
        print('Desculpe, banana está em falta')

fruta = ['maça', 'pera', 'abacate']
if 'banana' in fruta:
    print('Temos banana')
else:
    print('Desculpe, banana está em falta')

    if 'banana' not in fruta:
        print('Não temos banana')
        print(len(fruta))
        print(len(fruta[1]))
        fruta.append('limão')
        fruta[1] = 'laranja'
        fruta.insert(1, 'manga')
        fruta.remove('manga')  # remove pelo valor
        fruta.pop(0)  # remove pelo indice
        fruta.pop()  # pop sim referencia remove sempre o útimo elemento da lista
        del fruta[1]
        print(fruta)


frutas = ['maça', 'pera', 'abacaxi', 'abacate']
del frutas
print(frutas)

frutas = ['maça', 'pera', 'abacaxi', 'abacate']
print(frutas)
