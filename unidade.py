from enum import Enum # Importação da classe Enum, que é utilizada para criar uma estrutura de enumeração, permitindo definir um conjunto de constantes nomeadas para representar as unidades de medida dos produtos de forma consistente e fácil de usar em todo o sistema.

class Unidade(Enum): # Classe de enumeração para representar as unidades de medida dos produtos, definindo constantes nomeadas para cada unidade de medida, facilitando a consistência e o uso das unidades de medida em todo o sistema.
    UNIDADE = "un" # Constante para representar a unidade de medida "unidade", utilizada para produtos que são contados em unidades, como latas, garrafas, etc.
    QUILO = "kg" # Constante para representar a unidade de medida "quilo", utilizada para produtos que são medidos em quilogramas.
    GRAMA = "g" # Constante para representar a unidade de medida "grama", utilizada para produtos que são medidos em gramas.
    MILIGRAMA = "mg" # Constante para representar a unidade de medida "miligrama", utilizada para produtos que são medidos em miligramas.
    LITRO = "l" # Constante para representar a unidade de medida "litro", utilizada para produtos que são medidos em litros.
    MILILITRO = "ml" # Constante para representar a unidade de medida "mililitro", utilizada para produtos que são medidos em mililitros.