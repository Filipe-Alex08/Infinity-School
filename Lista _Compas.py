# Revisão Geral
"""
Você está desenvolvendo um programa para gerenciar uma lista de compras. O programa permite adicionar produtos à lista, visualizar a lista de produtos, atualizar as informações de um produto existente e remover produtos da lista. Além disso, o programa calcula o valor total de todos os produtos da lista.

O programa oferece as seguintes opções:

Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade e o valor unitário do produto. O programa calcula automaticamente o valor total do produto (quantidade * valor unitário) e atualiza o valor total de todos os produtos.

Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total de todos os produtos da lista.

Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. O programa solicita o nome do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.

Remover produto: O usuário pode remover um produto da lista informando o nome do produto que deseja remover. O programa atualiza automaticamente o valor total de todos os produtos.

Encerrar programa: Encerra a execução do programa.

O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as informações: "produto", "valor", "quantidade" e "total". A variável totalProdutos é utilizada para armazenar o valor total de todos os produtos da lista.

A cada operação realizada, o programa exibe mensagens indicando o resultado da operação.
"""


# Função para adicionar um novo produto à lista
def adicionar_produto(lista_produtos):
    nome_produto = input("Digite o nome do produto: ")
    valor_unitario = float(input("Digite o valor unitário do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    total_produto = valor_unitario * quantidade
    produto = {
        "produto": nome_produto,
        "valor": valor_unitario,
        "quantidade": quantidade,
        "total": total_produto
    }
    lista_produtos.append(produto)
    atualizar_total(lista_produtos)
    print(f"{nome_produto} foi adicionado à lista de compras.")

# Função para visualizar a lista de produtos
def visualizar_lista(lista_produtos):
    if not lista_produtos:
        print("A lista de compras está vazia.")
        return
    print("Lista de compras:")
    for produto in lista_produtos:
        print(f"Produto: {produto['produto']}, Valor Unitário: R${produto['valor']}, "
              f"Quantidade: {produto['quantidade']}, Total: R${produto['total']}")
    print(f"Valor total de todos os produtos: R${total_produtos:.2f}")

# Função para atualizar as informações de um produto
def atualizar_produto(lista_produtos):
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    for produto in lista_produtos:
        if produto["produto"] == nome_produto:
            valor_unitario = float(input("Digite o novo valor unitário do produto: "))
            quantidade = int(input("Digite a nova quantidade do produto: "))
            total_produto = valor_unitario * quantidade
            produto["valor"] = valor_unitario
            produto["quantidade"] = quantidade
            produto["total"] = total_produto
            atualizar_total(lista_produtos)
            print(f"As informações do produto {nome_produto} foram atualizadas.")
            return
    print(f"Produto {nome_produto} não encontrado na lista de compras.")

# Função para remover um produto da lista
def remover_produto(lista_produtos):
    nome_produto = input("Digite o nome do produto que deseja remover: ")
    for produto in lista_produtos:
        if produto["produto"] == nome_produto:
            lista_produtos.remove(produto)
            atualizar_total(lista_produtos)
            print(f"{nome_produto} foi removido da lista de compras.")
            return
    print(f"Produto {nome_produto} não encontrado na lista de compras.")

# Função para atualizar o valor total de todos os produtos da lista
def atualizar_total(lista_produtos):
    global total_produtos
    total_produtos = sum(produto["total"] for produto in lista_produtos)

# Função principal do programa
def main():
    lista_produtos = []
    global total_produtos
    total_produtos = 0.0
    while True:
        print("\nOpções disponíveis:")
        print("1. Adicionar produtos")
        print("2. Ver a lista de produtos")
        print("3. Atualizar produtos")
        print("4. Remover produto")
        print("5. Encerrar programa")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            adicionar_produto(lista_produtos)
        elif opcao == "2":
            visualizar_lista(lista_produtos)
        elif opcao == "3":
            atualizar_produto(lista_produtos)
        elif opcao == "4":
            remover_produto(lista_produtos)
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()