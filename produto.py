from datetime import datetime # Importação da biblioteca datetime para manipulação de datas, utilizada para lidar com a validade dos produtos.

class Produto: # Classe para representar um produto genérico, com atributos comuns a todos os produtos
    def __init__(self, nome, categoria, quantidade, unidade, quantidade_minima, data_validade): # Construtor para inicializar os atributos do produto
        self.nome = nome # Atributo para armazenar o nome do produto
        self.categoria = categoria # Atributo para armazenar a categoria do produto
        self.quantidade = quantidade # Atributo para armazenar a quantidade do produto
        self.unidade = unidade # Atributo para armazenar a unidade de medida do produto
        self.quantidade_minima = quantidade_minima # Atributo para armazenar a quantidade mínima do produto
        self.data_validade = data_validade # Atributo para armazenar a data de validade do produto

    def mostrar(self): # Método para mostrar as informações do produto, pode ser sobrescrito por subclasses para mostrar informações adicionais
        print(f"Produto: {self.nome}, Categoria: {self.categoria}, Quantidade: {self.quantidade}") # Imprime as informações do produto, método básico para mostrar as informações do produto

class ProdutoPerecivel(Produto): # Subclasse que representa um produto com validade, herda da classe Produto
    def __init__(self, nome, categoria, quantidade, unidade, quantidade_minima, data_validade): # Construtor para inicializar os atributos do produto com validade, chama o construtor da classe base para inicializar os atributos comuns e adiciona o atributo de validade
        super().__init__(nome, categoria, quantidade, unidade, quantidade_minima, data_validade) # Chama o construtor da classe base para inicializar os atributos comuns (nome, categoria e quantidade)
        self.validade = datetime.strptime(data_validade, "%Y-%m-%d") # Converte a string de validade para um objeto datetime, permitindo manipulação de datas

    def mostrar(self): # Sobrescrita do método mostrar para incluir a informação de validade, mostrando as informações do produto e a validade formatada
        print(f"Produto: {self.nome} |Categoria: {self.categoria} | Validade: {self.validade.strftime('%d/%m/%Y')}") # Imprime as informações do produto, incluindo a validade formatada, sobrescreve o método mostrar da classe base para mostrar informações adicionais específicas para produtos com validade.

class Bebida(ProdutoPerecivel): # Subclasse que representa um produto do tipo bebida, herda da classe Produto
    def __init__(self, nome, categoria, quantidade, unidade, quantidade_minima, data_validade, quantidade_unitaria): # Construtor para inicializar os atributos do produto do tipo bebida, chama o construtor da classe base para inicializar os atributos comuns e adiciona o atributo de quantidade unitária
        super().__init__(nome, categoria, quantidade, unidade, quantidade_minima, data_validade) # Chama o construtor da classe base para inicializar os atributos comuns (nome, categoria e quantidade)
        self.quantidade_unitaria = quantidade_unitaria # Atributo para armazenar a quantidade unitária da bebida (lata, garrafa pet, etc.)

# Da linha 1 até a linha 9, o código contempla:
# 1. Herança (a classe ProdutoPerecivel - linha 16, herda da classe Produto - linha 3),
# 2. Polimorfismo (o método mostrar é implementado de forma diferente na classe derivada),
# 3. Encapsulamento (através do uso de atributos e métodos específicos para cada tipo de produto) e
# 4. Abstração (a classe Produto define uma interface comum para todos os produtos).