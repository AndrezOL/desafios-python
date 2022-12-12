idade = int(input('Qual a sua idade? '))
peso = int(input('Quanto você pesa? '))
sono = input('Você dormiu pelo menos 6 horas nas últimas 24 horas? ')

if idade >= 16 and peso >= 50 and sono == 'sim' or 's':
    print('Você pode doar sangue')
else:
    print('Voce não pode doar sangue')