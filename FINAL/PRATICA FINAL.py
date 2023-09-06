class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)
    
    def _inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None or no.direita is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.esquerda)            
        else:
            if no.direita is None or no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.direita)  


    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def mostrar_raiz(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            print('Raiz:', self.raiz.valor, end=' ')   

    def altura_da_arvore(self):
        if self.raiz is None:
            return 0
        else:
            return self.altura_arvore(self.raiz) - 1

    def altura_arvore(self, no):
        if no == None:
            return 0
        else:
            return max(self.altura_arvore(no.esquerda), self.altura_arvore(no.direita)) + 1

    def mostrar_nos_internos(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_nos_internos_recursivo(self.raiz)

    def mostrar_nos_internos_recursivo(self, no):
        if no is not None:
            if no.esquerda is not None and no.direita is not None:
                print(no.valor, end=' ')
            self.mostrar_nos_internos_recursivo(no.esquerda)
            self.mostrar_nos_internos_recursivo(no.direita)

    def mostrar_as_folhas(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_as_folhas_recursivo(self.raiz)

    def mostrar_as_folhas_recursivo(self, no):
        if no is not None:
            if no.esquerda is None and no.direita is None:
                print(no.valor, end=' ')
            self.mostrar_as_folhas_recursivo(no.esquerda)
            self.mostrar_as_folhas_recursivo(no.direita)
            
    def procurar(self, v):
        if self.raiz is None:
            return False
        else:
            return self._procurar(self.raiz, v)
    
    def _procurar(self, no, v):
        if no is None:
            return False
        if no.valor == v:
            return True
        if self._procurar(no.esquerda, v):
            return True
        if self._procurar(no.direita, v):
            return True

def main():
    a = ArvoreBinaria()
    while True:
        print('\n-----------------------------------------------------------------')
        print(' Menu de opções:')
        print('1. Inserir um valor na árvore.')
        print('2. Mostrar a raiz da árvore.')
        print('3. Mostrar a altura da árvore.')
        print('4. Mostrar os nós internos da árvore.')
        print('5. Mostrar as folhas da árvore.')
        print('6. Verificar se um valor está na árvore.')
        print('7. Sair.')
        print('')
        opcao = input('Opção: ')
        if opcao == '1':
            qtd_valores = int(input('Quantos valores deseja inserir: '))
            for j in range(qtd_valores):
                num = int(input('Digite os valores: ')) 
                a.inserir_em_nivel(num)
        elif opcao == '2':
            a.mostrar_raiz()
        elif opcao == '3':
            print('Altura:', a.altura_da_arvore())
        elif opcao == '4':
            a.mostrar_nos_internos()
        elif opcao == '5':
            a.mostrar_as_folhas()
        elif opcao == '6':
            x = int(input('Informe o número para verificar presença na árvore: '))
            if a.procurar(x):
                print('Número presente na árvore')
            else:
                print('Número não está presente na árvore!')
        elif opcao == '7':
            break
        else:
            print('Opção inválida!')
main()
