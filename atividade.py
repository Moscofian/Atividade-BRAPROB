from time import sleep

menu = """Menu:
 1. Metros para milímetros
 2. Tempo em segundos
 3. Aumento salarial
 4. Desconto do produto
 5. Velocidade média
 6. Aluguel de carro
 7. Fumante
 8. Maior e menor número
 9. Aumento salarial if else
10. Valor viagem
11. Contagem regressiva
12. Divisão limitada
13. Depósito e juros
14. Dívida com juros
15. Divisão limitada 2
0. Sair
===> """

while True:
    opcao = input(menu)

    if opcao == '1':
        #Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
        valor = int(input("Insira um valor em metro para ser convertido para milímetros: "))

        print(f"O valor {valor}m em milímetros é de {valor * 1000}mm")
        input("Precione Enter para continuar...")

    elif opcao == '2':
        #Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
        dias = int(input("Escreva a quantidade de dias: "))
        horas = int(input("Escreva a quantidade de horas: "))
        minutos = int(input("Escreva a quantidade de minutos: "))
        segundos = int(input("Escreva a quantidade de segundos: "))

        print("O tempo total em segundos foi de {} segundos".format((dias * 86400) + (horas * 3600) + (minutos * 60) + segundos))
        input("Precione Enter para continuar...")

    elif opcao == '3':
        #Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
        salario = float(input("Insira o salário atual: "))
        porcentagem = int(input("Insira a porcentagem do aumento: "))

        print("Salário atual: %.2f \nAumento percentual: %d%% \nSalário final: %.2f" % (salario, porcentagem, salario + (salario * porcentagem / 100)))
        input("Precione Enter para continuar...")

    elif opcao == '4':
        #Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
        preco = float(input("Insira o preço do produto: "))
        desconto = int(input("Insira o percentual do desconto: "))

        print("Preço sem desconto: {} \nPercentual de desconto: {}% \nPreço com desconto: {}".format(preco, desconto,preco - (preco * desconto / 100)))
        input("Precione Enter para continuar...")

    elif opcao == '5':
        #Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
        distancia = int(input("Insira a distância em kilometros: "))
        velocidade = int(input("Insira a velocidade média em km/h esperada para a viagem: "))

        print(f"O tempo estimado para a viagem é de {distancia / velocidade} Horas")
        input("Precione Enter para continuar...")

    elif opcao == '6':
        #Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60,00 reais por dia e 0,15 centavos por km rodado.
        distancia = int(input("Insira a distancia percorrida em kilometros: "))
        tempo = int(input("Insira a quantidade de dias pelos quais o carro foi alugado: "))
        valorDist = distancia * 0.15
        valorTemp = tempo * 60
        SEPARADOR = ""

        print(SEPARADOR.center(30, "="))
        print(f"""Distância: {distancia}.R$0,15 = {valorDist}
        Dias: {tempo}.R$60,00 = {valorTemp}
        Total: R${valorDist + valorTemp} """)
        print(SEPARADOR.center(30, "="))
        input("Precione Enter para continuar...")

    elif opcao == '7':
        #Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
        cigarros = int(input("Insira a quantidade de cigarros fumados por dia: "))
        anos = int(input("Insira a quantidade de anos desde que começou a fumar: "))

        print("Você tem em média %.0f dias a menos de vida" % (((cigarros * 10) * (anos * 365)) / 1440))
        input("Precione Enter para continuar...")

    elif opcao == '8':
        #Escreva um programa que leia três números e que imprima o maior e o menor.
        numeros = []
        auxiliar = 0

        for i in range(3):
            auxiliar = int(input("Insira um valor: "))
            numeros.append(auxiliar)

        menor = min(numeros)
        maior = max(numeros)

        print(f"""Menor número: {menor}
        Maior número: {maior}""")
        input("Precione Enter para continuar...")

    elif opcao == '9':
        #Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
        salario = float(input("Insira o valor do salário: "))

        if salario > 1250:
            print("Aumento de 10%. \nResultado: {}".format(salario + (salario * 0.10)))
        else:
            print("Aumento de 15%. \nResultado: {}".format(salario + (salario * 0.15)))
        input("Precione Enter para continuar...")

    elif opcao == '10':
        #Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km, e R$0,45 para viagens mais longas.
        distancia = int(input("Digite a distância em kilometros: "))

        if distancia <= 200:
            print(f"Total: R${distancia * 0.5}")
        else:
            print(f"Total: R${distancia * 0.45}")
        input("Precione Enter para continuar...")

    elif opcao == '11':
        #Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.
        from time import sleep

        aux = int(10)

        print("Contagem:")
        for i in range(11):
            print(aux)
            aux -= 1
            sleep(1)

        print("Fogo!")
        input("Precione Enter para continuar...")

    elif opcao == '12':
        #Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        aux = 0

        while num1 >= num2:
            num1 -= num2
            aux += 1

        print(f"Quociente: {aux}")
        print(f"Resto: {num1}")
        input("Precione Enter para continuar...")

    elif opcao == '13':
        #Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
        deposito = int(input("Insira o depósito inicial: "))
        juros = int(input("Insira a taxa de juros: "))
        aux = 0
        i = 1

        print(f"{i}° mês: {deposito}")
        for i in range(23):
            i += 2
            aux += deposito * juros / 100
            deposito += deposito * juros / 100
            print("%d° mês: %.2f" % (i, deposito))
        print("Juros total: %.2f" % aux)
        input("Precione Enter para continuar...")

    elif opcao == '14':
        #Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
        divida = float(input("Insira o valor inicial da dívida: "))
        juros = int(input("Insira o juros mensal: "))
        tempo = int(input("Insira em quantos meses a dívida será paga: "))
        jurosTotal = float(0)

        for i in range(tempo):
            jurosTotal += divida * juros / 100
            divida += divida * juros / 100
        print("Valor a ser pago por mês durante %d meses: %.2f \nJuros total: %.2f" % (tempo, divida / tempo, jurosTotal))
        input("Precione Enter para continuar...")

    elif opcao == '15':
        #Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        aux = 0

        while num1 >= num2:
            num1 -= num2
            aux += 1

        print(f"Resto: {num1}")
        input("Precione Enter para continuar...")

    elif opcao == '0':
        break

    else:
        print("Opção inválida. Tente novamente.")
        input("Precione Enter para continuar...")