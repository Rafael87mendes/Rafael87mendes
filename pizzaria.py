dadostam = []
dadossab= []
print('-=-' * 30)
print(f'{"LANCHONETE DO THEO":^40}')
print('-=-' * 30)
nome = str(input('Olá, qual é o seu nome?\n ')).strip().upper()
print()
print(f'Olá, {nome} tudo bem!')
print()
print('-=-' *30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-=-' *30)
valor = ('[1] Pizza Grande', 45,
'[2] Pizza Média', 35,
'[3] Pizza Pequena', 25)
for pos in range(0,len(valor)):
    if pos % 2 == 0:
        print(f'{valor[pos]:.<30}',end='')
    else:
        print(f'{valor[pos]:.>7.2f}')
tamanho = int(input('Digite o número da sua opção?\n'))
while True:
    if tamanho > 3 or tamanho <=0:
        print('Valor invalido. Tente novamente.....')
        tamanho = int(input('Digite o número da sua opção?\n'))
    elif tamanho <= 4 or tamanho > 0:
            break
    else:
        print('')
if tamanho == 1:
    dadostam.append('Pizza grande')
elif tamanho == 2:
    dadostam.append('Pizza Média')
elif tamanho == 3:
    dadostam.append('Pizza Pequena')
print('Qual será o sabor?')
print('''[1] Calabresa
[2] Mussarela
[3] Portuguesa
[4] Frango C/Catupyri''')
sabor = int(input('Digite o número da opção do sabor?\n '))
while True:
    if sabor > 4 or sabor <=0:
        print('Valor invalido. Tente novamente.....')
        sabor = int(input('Digite o número da sua opção?\n'))
    elif sabor <= 4 or sabor > 0:
            break
    else:
        print('')
if sabor == 1:
    dadossab.append('Calabresa')
elif sabor == 2:
    dadossab.append('Mussarela')
elif sabor == 3:
    dadossab.append('Portuguesa')
elif sabor == 4:
    dadossab.append('Frango C/Catupyri')
endereço = str(input('Qual é o seu endereço?\n ')).strip().upper()
print('')
if tamanho == 1:
    print('Valor da pizza deu R$48 com a entrega')
elif tamanho == 2:
    print('Valor da pizza deu R$38 com a entrega')
elif tamanho == 3:
    print('Valor da pizza deu R$28 com a entrega')
print('')
pagamento = int(input('Qual será a forma de pagamento? \n[1]Dinheiro \n[2]Cartão? \nDigite o número da opção:\n'))
if pagamento == 1:
    print('Vai precisar de troco?')
    r = str(input('Digite [S/N]:\n ')).strip().upper()[0]
    if r in 'Ss':
        troco = int(input('Troco pra quanto?\n '))
    else:
        print('ok')
tel = str(input('Pode me passar um telefone para contato:\n'))
ref = input('Pode me passsar um ponto de refência por favor?\n').strip().upper()
print('Verique se seu pedido está correto')
print(f'{nome}, {dadostam}, {dadossab}, {endereço}, {tel}, {ref}')
print('')
print(f'Obrigado {nome}, dentro de 30 minutos a sua pizza estará chegando até a sua residência.\nTenha uma boa noite!.')



