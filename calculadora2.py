def calculadora(opcao):
    num1 = int(input("\nDigite um numero: "))
    num2 = int(input("Digite outro numero: "))
    if(opcao == 1):
        return num1 + num2
    elif(opcao == 2):
        return num1 - num2
    elif(opcao == 3):
        return num1 * num2
    elif(opcao == 4):
        return num1 / num2 

while True:
    print("1: Soma\n" 
          + "2: Subtração\n"
          + "3: Multiplicação\n" 
          + "4: Divisão\n" 
          + "0: Sair\n")

    opcao = int(input("Selecione uma opção: "))
    if(opcao > 4 or opcao < 0):
        print("\nEssa opção não existe, tem novamente!\n")
        continue
    elif(opcao == 0):
        print("Saindo...")
        break
    else:
        print(f"\nResultado: {calculadora(opcao)}\n")
