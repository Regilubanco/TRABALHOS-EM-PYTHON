# calculadora_v2.py

# Variável para armazenar a saída
saida = ''

# Função para adição
def adicao(a, b):
    return a + b

# Função para subtração
def subracao(a, b):
    return a - b

# Função para multiplicação
def multiplicacao(a, b):
    return a * b

# Função para divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adição':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtração':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicação':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisão':
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"
    
    return resultado

# Laço while para continuar a calculadora
while saida.lower() != 'n':
    # Solicita os números e a operação ao usuário
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação desejada (+, -, *, / ou o nome da operação): ')

    # Chama a função calculadora e armazena o resultado
    resultado = calculadora(num1, num2, operacao)

    # Exibe o resultado
    print(f'Resultado da operação: {resultado}')

    # Pergunta ao usuário se deseja continuar
    saida = input('Deseja continuar? (S/N): ')
