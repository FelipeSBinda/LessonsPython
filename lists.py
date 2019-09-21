print('Hello World')
doces = ['biscoito','cookie','bolinho','amanteigados','bombinhas','tortinhas']
print('cookie' in doces)
print('bolinho' in doces)
print('nozes' in doces)
if 'biscoito' in doces:
    print('Temos biscoito')
if 'waffles' in doces:
    print('Temos waffles')
else:
    print('Não temos waffles')
if 'bombom' not in doces:
    print('Não temos bombons')
print(len(doces))
print(len(doces[3]))
doces.append('waffles')
print(doces)
doces[0] = 'biscoitos'
print(doces)
print(doces[3])
doces.insert(1, 'bombons')
print(doces)
doces.remove('waffles')
print(doces)
doces.append('waffles')
print(doces)
print(len(doces))
doces.pop(0)
print(doces)
doces.insert(0,'biscoito')
print(doces)
del doces[0]
print(doces)
doces.insert(0,'biscoitos')
print(doces)

