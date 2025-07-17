CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário para digitar seu nome 
nome_usuario = input('Digite o seu nome: ')

# 2) Solicita ao usuário que digite o valor do seu salario  
# Converte o salario para float
salario_usuario = float(input('Digite o seu salario: '))

# 3) Solicita ao usuário para digitar o valor do bonus recebido 
# Converte o bonus para float
bonus_usuario = float(input('Digite o seu bonus: '))

# 4) Calcule o valor do bonus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprima a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f'Ola {nome_usuario}, seu bonus final foi de: {valor_do_bonus}')
