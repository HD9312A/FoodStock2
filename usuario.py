from abc import ABC, abstractmethod

class Usuario(ABC): # Classe abstrata para representar um usuário genérico
    def __init__(self, nome): # Construtor para inicializar o nome do usuário
        self.nome = nome # Atributo para armazenar o nome do usuário

    @abstractmethod # Método abstrato para mostrar as permissões do usuário, deve ser implementado pelas subclasses
    def mostrar_permissao(self): # Método abstrato para mostrar as permissões do usuário
        pass # Indica que o método é abstrato e deve ser implementado pelas subclasses

# Da linha 1 até a linha 9, o código contempla:
# 1. Classe abstrata, 
# 2. Herança, 
# 3. Polimorfismo, 
# 4. Encapsulamento (através do uso de atributos e métodos) e
# 5. Abstração (através do uso de métodos abstratos).


# A partir da linha 25 até a linha 35, o código contempla:
# 1. Herança (as subclasses herdam da classe abstrata Usuario - linha 3) - Classes filhas (cozinha - linha 25, estoquista - linha 29 e admin - linha 33) herdam da classe pai (Usuario linha 3),
# 2. Polimorfismo (cada subclasse implementa o método mostrar_permissao de maneira diferente), 
# 3. Encapsulamento (através do uso de atributos e métodos específicos para cada tipo de usuário) e
# 4. Abstração (as subclasses implementam o método abstrato mostrar_permissao de acordo com suas permissões específicas).

class cozinha (Usuario): # Subclasse que representa um usuário do tipo cozinha, herda de Usuario
    def mostrar_permissao(self): # Implementação do método abstrato para mostrar as permissões do usuário do tipo cozinha
        print("Cozinha: Acesso limitado ao estoque.") # Imprime a permissão específica para o usuário do tipo cozinha

class estoquista (Usuario): # Subclasse que representa um usuário do tipo estoquista, herda de Usuario
    def mostrar_permissao(self): # Implementação do método abstrato para mostrar as permissões do usuário do tipo estoquista
        print("Estoque: Controle operacional do estoque.")

class admin (Usuario): # Subclasse que representa um usuário do tipo admin, herda de Usuario
    def mostrar_permissao(self): # Implementação do método abstrato para mostrar as permissões do usuário do tipo admin
        print("Admin: Acesso total ao sistema. ") # Imprime a permissão específica para o usuário do tipo admin