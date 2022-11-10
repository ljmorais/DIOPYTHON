# nome = "Luiz"

# print(nome.upper())
# print(nome.lower())
# print(nome.title())

# texto = "Olá, mundo   "

# print(texto)

# print(texto.strip())
# print(texto.rstrip())

# menu = "Python"

# print("####"+ menu + "####")
# print(menu.center(14, "#"))
# print("-".join(menu))

# C = int(input()) 
# for i in range (C): 
#     if i <= 8000:
#       print("Inseto!")
#     else:
#       print("Mais de 8000!")
#     break

# class Veiculo:
#   def __init__(self, cor, placa, numero_rodas):
#     self.cor = cor
#     self.placa = placa
#     self.numero_rodas = numero_rodas
    
#   def ligar_motor(self):
#     print("Ligando o motor.")

# class Motocicleta(Veiculo):
#   pass

# class Carro(Veiculo):
#   pass

# class Caminhao(Veiculo):
#   def __init__(self, cor, placa, numero_rodas, carregado):
#     super().__init__(cor, placa, numero_rodas)
#     self.carregado = carregado

#   def esta_carregado(self):
#     print(f"{'Sim' if self.carregado else 'Não'} Estou carregado")


# moto = Motocicleta("preta", "ABC-1343", 2)

# moto.ligar_motor()

# carro = Carro("branco","CDE-4321", 4)

# carro.ligar_motor()

# caminhao = Caminhao("ROXO", "ZYX-1234", 8)

# caminhao.ligar_motor()

# class Animal:
#   def __init__(self, nro_patas):
#     self.nro_patas = nro_patas
  
#   def __str__(self):
#     return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# class Mamifero(Animal):
#   def __init__(self, cor_pelo, **kw):
#     self.cor_pelo = cor_pelo
#     super().__init__(**kw)

# class Ave(Animal):
#   def __init__(self, cor_bico, **kw):
#     self.cor_bico = cor_bico
#     super().__init__(**kw)

# class Gato(Mamifero):
#   pass

# class Ornitorrinco(Mamifero,Ave):
#   pass

# gato = Gato(nro_patas=4, cor_pelo="Branco")

# print(gato)

# ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo= "vermelho", cor_bico= "Laranja")

# print(ornitorrinco)

# class Pessoa:
#   def __init__(self, nome, ano_nascimento):
#     self._nome = nome
#     self.ano_nascimento = ano_nascimento
  
#   @property
#   def nome(self):
#     return self._nome
  
#   @property
#   def idade(self):
#     _ano_atual = 2022
#     return _ano_atual - self.ano_nascimento
  
# pessoa = Pessoa("Luiz", 1994)
# print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

class Estudante:
  escola = "DIO"

  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula = matricula

    def __str__(self):
      return f" {self.nome} - {self.matricula} - {self.escola}"

aluno_1 = Estudante("Luiz", 1)
aluno_2 = Estudante("Jonathan", 2)
print(aluno_1)