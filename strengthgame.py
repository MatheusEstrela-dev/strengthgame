from random import choice

personagem = r'''
 O  
/|\
/ \
'''
palavra = 'CACHORRO'
lista = ['_'] * len(palavra)
letra = ''
k = ''
PA = None
cb = r'\ '.strip()
lista1 = [cb,'/',cb,'|','/','O']
a = "\033[35m-\033[m" * (len(palavra) + 2)
print('~*'*15)
print(f'\033[32m{"JOGO DA FORCA":^30}\033[m')
print('~*'*15)
print(personagem)
while not ''.join(lista) == palavra:
    usuario = str(input('SUGESTÃO:')).upper()
# VERIFICANDO SE A LETRA SE ENCONTRA NA PALAVRA.
    if usuario in palavra:
        for c,n in enumerate(palavra):
            if n == usuario:
                lista[c] = usuario
    else:
        PA = choice(lista1)
        parte = personagem.find(PA)
        for n,c in enumerate(personagem):
            if not n == parte:
                k += c
            else:
                k += ' '
                lista1.remove(c)
        personagem = k
        k = ' '
    if not usuario in letra:
        letra += ' ' + usuario
    else:
        print('!!!Letra já usada.!!!')
    print('\033[31mLetras já uasadas:\033[m',letra)
    print(f'+{a}+')
    print('|',''.join (lista),'|')
    print(f'+{a}+')

    print(personagem)

    if lista1 == []:
        print('\033[1;31mGAME OVER\033[m')
        break
if ''.join(lista) == palavra:
    print('\033[1;32mYOU WIN! Parabéns!\033[m')
