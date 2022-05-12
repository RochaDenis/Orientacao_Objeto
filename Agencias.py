from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 100000:
            print('Caixa abaixo do nivel recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O valor de caixa está ok. Caixa Atual: {}'.format(self.caixa))

    def empresta_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
           self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não é possível. Dinheiro não disponivel em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append(nome, cpf, patrimonio)


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor

class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 100000
            super().adicionar_cliente(nome, cpf, patrimonio)

        else:
            print('O cliente não tem patrimonio minimo necessario para entrar na agência Premium')


if __name__ == '__main__':
   agencia1 = Agencia(22223333, 2000000000, 4568)

   agencia_virtual = AgenciaVirtual('www.denis.com.br', 1239849, 1909873)
   agencia_virtual.verificar_caixa()
   print(agencia_virtual.site)

   agencia_comum = AgenciaComum(22222255555, 25555550000000)
   agencia_comum.verificar_caixa()

   agencia_premium = AgenciaPremium(222999999, 9989983776)
   agencia_premium.verificar_caixa()









