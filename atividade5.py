class Pessoa:
    def __init__(self,nome,email,sexo,idade,cpf):
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.idade = idade
        self.cpf = cpf

    def mostrar_dados(self):
        print("Nome: ", self.nome)
        print("Email: ", self.email)
        print("Sexo: ", self.sexo)
        print("Idade: ", self.idade)
        print("CPF: ", self.cpf)

pessoa1 = Pessoa(
    "Miguel"
    "paragamestops@gmail.com"
    "Masculino"
    "15 Anos"
    "087.212.491-64"
)

pessoa2 = Pessoa(
    "Ana"
    "Atividade5@gmail.com"
    "Feminino"
    "13 Anos"
    "000.763.821-33"
)

pessoa1.mostrar_dados()
pessoa2.mostrardados()