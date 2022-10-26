
from xml.sax.xmlreader import InputSource

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
menu = '''

    [1] Saque
    [2] Depositar
    [3] Extrato
    [4] FINALIZAR 

'''

while True:
    
    opcao = input(menu)

    if opcao == "2":
        valor = float(input("Informe o valor deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f} \n"
    
        else:
            print("Falha na operação, não é possivel realizar o deposito do valor solicitado.")

    elif opcao == "1":

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite


        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação, saldo insuficiente.")

        elif excedeu_limite:
            print("Não é possivel realizar saque, limite excedido.")

        elif excedeu_saques:
            print("Limite de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R${valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Falha na operação, o valor informado é invalido.")
        
    elif opcao == "3":
        print("\n============= EXTRATO ===============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "4":
        print("Agradecemos sua preferencia.")
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação.")
        

    



