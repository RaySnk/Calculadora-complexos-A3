import cmath  # Para funções matemáticas complexas (como phase/argumento)
import math   # Para funções matemáticas reais (como pi, cos, sin)

class ComplexOperations:
    """
    Implementa as operações de números complexos necessárias para a calculadora,
    especialmente aquelas não trivialmente tratadas pelos operadores nativos do Python.
    """

    @staticmethod
    def get_conjugate(z: complex) -> complex:
        """
        Calcula o conjugado do número complexo z. (a - bi)
        Regra 1: Conjugado
        """
        # O método .conjugate() é nativo do tipo complex do Python
        return z.conjugate()

    @staticmethod
    def get_root(z: complex, n: int) -> list[complex]:
        """
        Calcula as n raízes de um número complexo (Raiz n).
        Regra 1: Raiz
        
        Utiliza a fórmula de De Moivre para raízes:
        wk = r^(1/n) * [cos((theta + 2*pi*k)/n) + i * sin((theta + 2*pi*k)/n)], 
        onde k varia de 0 até n-1.
        """
        if n == 0:
            raise ValueError("O índice da raiz (n) não pode ser zero.")
        if n < 1:
            raise ValueError("A função de raiz deve receber n >= 1.")
            
        r = abs(z)  # Módulo (r)
        theta = cmath.phase(z)  # Argumento (theta)
        roots = []
        
        # Iteração para encontrar as n raízes
        for k in range(n):
            angle = (theta + 2 * math.pi * k) / n
            modulus_root = r ** (1/n)
            
            # Converte de volta para a forma retangular
            root_k = complex(
                modulus_root * math.cos(angle),
                modulus_root * math.sin(angle)
            )
            roots.append(root_k)
            
        return roots
    
# Exemplo de teste da classe
if __name__ == "__main__":
    z = complex(8, 0) # Exemplo: 8 + 0i
    n_roots = 3
    
    print(f"Conjugado de {z}: {ComplexOperations.get_conjugate(z)}")
    
    raizes = ComplexOperations.get_root(z, n_roots)
    print(f"\nAs {n_roots} raízes de {z}:")
    for i, root in enumerate(raizes):
        print(f"Raiz {i+1}: {root.real:.4f} + {root.imag:.4f}i")