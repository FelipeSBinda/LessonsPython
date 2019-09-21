Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista_de_frutas = ['maçã','banana','manga','abacaxi','melancia']
>>> print(lista_de_frutas)
['maçã', 'banana', 'manga', 'abacaxi', 'melancia']
>>> fiat = ['cronos','mobi','argo','uno']
>>> volks = ['up','gol','polo','fox']
>>> fiat == volks
False
>>> a = [1,2,3,4]
>>> b = [1,2,3,4]
>>> a == b
True
>>> a is b
False
>>> fiat is volks
False
>>> jogador de lol = felipe
SyntaxError: invalid syntax
>>> jogador de lol = 'felipe'
SyntaxError: invalid syntax
>>> jogador de lol = ['felipe']
SyntaxError: invalid syntax
>>> jogadores_de_lol = ['felipe','zangetsu']
>>> jogando_a_vida_fora = ['ana']
>>> jogando_com_o_sistema = ['gabi']
>>> jogando_a_vida_fora == jogando_com_o_sistema
False
>>> jogadores_de_lol is jogando_a_vida_fora
False
>>> alunnos_ti = ['felipe','zangetsu']
>>> ogadores_de_lol = ['felipe','zangetsu']
>>> alunnos_ti is ogadores_de_lol
False
>>> #perceba que me faltam aulas de português
>>> a = ['maçã', 50, true, 3.54]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a = ['maçã', 50, true, 3.54]
NameError: name 'true' is not defined
>>> a = ['maçã', 50, True, 3.54]
>>> print(a)
['maçã', 50, True, 3.54]
>>> print(type(a[0]))
<class 'str'>
>>> print(type(a[1]))
<class 'int'>
>>> print(type(a[2]))
<class 'bool'>
>>> print(type(a[3]))
<class 'float'>
>>> z = ['café','leite']
>>> x = ['chocolate','chantily']
>>> z = x
>>> z is x
True
>>> z.append('açucar')
>>> z
['chocolate', 'chantily', 'açucar']
>>> x
['chocolate', 'chantily', 'açucar']
>>> x[-3]
'chocolate'
>>> x[-1]
'açucar'
>>> lA['vergonha na cara','emprego'.'faculdade','mais raiva','café']
SyntaxError: invalid syntax
>>> lA['vergonha na cara','emprego','faculdade','mais raiva','café']
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    lA['vergonha na cara','emprego','faculdade','mais raiva','café']
NameError: name 'lA' is not defined
>>> lA = ['vergonha na cara','emprego','faculdade','mais raiva','café']
>>> print(lA)
['vergonha na cara', 'emprego', 'faculdade', 'mais raiva', 'café']
>>> lA = [-5:-3]
SyntaxError: invalid syntax
>>> lA = [-4:-2]
SyntaxError: invalid syntax
>>> lA = [4:2]
SyntaxError: invalid syntax
>>> x = z[-1:-3]
>>> lAf = lA[-1:-4]
>>> lAf
[]
>>> a = [1,2,3,4,5,6,7]
>>> b = a[1:5]
>>> b
[2, 3, 4, 5]
>>> b = a[-1:-5]
>>> b
[]
>>> b = a[-5:-1]
>>> b
[3, 4, 5, 6]
>>> b = [:5]
SyntaxError: invalid syntax
>>> b = a[:5]
>>> b
[1, 2, 3, 4, 5]
>>> b = a[5:]
>>> b
[6, 7]
>>> cubos = ['3x3','4x4','5x5','megamix','pyraminx']
>>> for m in cubos:
	print(m)

	
3x3
4x4
5x5
megamix
pyraminx
>>> 
>>> 
>>> print(len(cubos))
5
>>>  #laço de repetição que executa os iotens da sua lista com quantidade equivalente
>>> for m in cubos:
	print('**************')
	print(m)
	print('**************')

	
**************
3x3
**************
**************
4x4
**************
**************
5x5
**************
**************
megamix
**************
**************
pyraminx
**************
>>> for m in cubos:
	print('**************')
	print(m)

	
**************
3x3
**************
4x4
**************
5x5
**************
megamix
**************
pyraminx
>>> for m in cubos:
	print(c, end='')

	
Traceback (most recent call last):
  File "<pyshell#78>", line 2, in <module>
    print(c, end='')
NameError: name 'c' is not defined
>>> for m in cubos:
	print(m, end='')

	
3x34x45x5megamixpyraminx
>>> for m in cubos:
	print(m, end='  ')

	
3x3  4x4  5x5  megamix  pyraminx  
>>> 
