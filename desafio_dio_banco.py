# Eder Souza
print("****Olá, bem vindo ao bank bank****")
menu = """
|*****Digite a Operação Desejada: *****|\n 
          |****[1]-> Depósito |     
          |****[2]-> Saque    |
          |****[3]-> Extrato  |
          |****[4]-> Sair     |\n
|**************************************|
  """
deposito = 0.0
extrato = ""
saldo = 0.0
limite_para_saque = 500
LIMITE_SAQUES = 3

while True: 
    print(menu)
    operacao = input("=>")
   
    if operacao == "1":
      deposito =  float(input("Digite o valor que deseja depositar:  "))
      if deposito > 0:
         saldo += deposito
         extrato += f"Depósito: R$ {deposito:.2f}\n"
         print(f"########## Sucesso ############")
         print(f"Valor depositado: R$ {deposito:.2f}")
      else:
         print("Valor digitado é inválido")

    elif operacao == "2":
      if LIMITE_SAQUES < 1:
         print(f"########## Operação não realizada ############")
         print("##### Quantidade de saques diários excedida. #######")
         continue
      saque =  float(input("Digite o valor que deseja Sacar:  "))
      if saque > limite_para_saque:
         print(f"########## Operação não realizada ############")
         print("##### Valor acima do permitido para um saque. #######")
      elif saque > saldo:
         print(f"########## Operação não realizada ############")
         print(f"##### Valor desejado é acima de saldo em conta => Saldo em conta: R${saldo:.2f} ######")
      elif saldo == 0:
          print(f"########## Operação não realizada ############")
          print(f"##### Saldo insulficiente para realizar saques => Saldo em conta: R${saldo:.2f} ######")      
      else: 
         saldo -= saque
         extrato += f"Saque: R${saque:.2f}\n"
         print("######## Sucesso ##########")
         print(f"Valor do saque: R${saque:.2f}")
         print("Retire seu Dinheiro ")
         LIMITE_SAQUES -= 1

    elif operacao == "3":
      if extrato == "":
         print(f"##### Até o momento, nenhuma operação foi realizada, Saldo na conta: R${saldo:.2f} ######")               
      else:
        print("\n*****************Extrato*****************\n")
        print(f"Saldo na conta: R${saldo:.2f}, Quantidade de saques Disponivel: {LIMITE_SAQUES} \n")
        print(f"Operação/valor")
        print(extrato)
        print("*********************************************\n")
    elif operacao == "4":
      deposito =  print("Até Logo!\n")
      break 
    else: 
       print("Opção inválida, por favor digite uma opação do menu \n") 
    