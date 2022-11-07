import textwrap

def menu():
    menu="""\n
    ===================== MENU =============
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova conta
    [lc]\t Listar contas
    [nu]\t Novo Usuario
    [q]\t Sair
     -->  """

    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n === DEPOSITO REALIZADO COM SUCESSO ===")
    
    else:
        print("\n === Operação falhou, o valor informado está incorreto. ===")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeros_saques, limites_saques):
    excedeu_saldo = valor > saldo
    excedeu_limites = valor > limite
    excedeu_saques = numeros_saques >= limites_saques

    if excedeu_saldo:
        print(" === Falha na operação, saldo insuficiente. ===")

    elif excedeu_limites:
        print("=== Não é possivel realizar saque, limite excedido. ===")

    elif excedeu_saques:
        print("=== Limite de saques excedido. ===")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"saque: R${valor:.2f}\n"
        numero_saques += 1
        print("\n === Saque realizado com sucesso! === ")
        
    else:
        print("Falha na operação, o valor informado é invalido.")

    return saldo, extrato
        
def exibir_extrato(saldo, /, *, extrato):
    print("\N ===== EXIBIR EXTRATO =====")
    print(" Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\n saldo: \t \t R$ {saldo:.2f}")
    print("=================================")

def criar_usuarios(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ==== Já existe usuario com esse CPF! =====")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe o endereço da sua casa: ")

    usuarios.append({"nome":nome , "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print(" ===== Usuario cadastrado com sucesso =====")

def filtrar_usuario( cpf, usuarios):
    usuarios_filtatrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    
    return usuarios_filtatrados[0] if usuarios_filtatrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ===== Conta Criada com sucesso! ===")
        return { "agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print ("\n ======= Usuario não encontrado, Fluxo de criação de conta encerrado ======")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print('=' * 100)
        print(textwrap.dedent(linha))


def main():

LIMITE_SAQUES = 3
agencia = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

while True:
    opção = menu()

    if opção == "d":
        valor = float(input("Informe o valor do deposito: "))

        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opção == 's':
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato
            limite=limite,
            limite_saques=LIMITE_SAQUES, 
        )
    
    elif opção == "e":
        exibir_extrato(saldo, extrato=extrato)
    
    elif opção == "nu":
        criar_usuarios(usuarios)
    
    elif opção == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(agencia, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opção == "lc":
        listar_contas(contas)

    elif opção == "q":
        break

main()        

