ncom = str(input('Digite aqui o seu nome completo: ')).upper().strip()
nome = ncom.split()
print('Muito prazer em te conheer!!! ')
print('  ')
print('  ')
print('Seu primeiro nome é {}'.format(nome[0]))
print('  ')
print('  ')
print('Seu último nome é {}'.format(nome[len(nome)-1]))
