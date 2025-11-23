import cmath  # Para funções complexas como phase (argumento)
import math   # Para funções reais como pi e cos/sin

# --- Funções Aritméticas Básicas (Chamadas pelo expression_handler) ---

def soma(z1: complex, z2: complex) -> complex:
    """Implementa z1 + z2."""
    return z1 + z2

def subtracao(z1: complex, z2: complex) -> complex:
    """Implementa z1 - z2."""
    return z1 - z2

def multiplicacao(z1: complex, z2: complex) -> complex:
    """Implementa z1 * z2."""
    return z1 * z2

def divisao(z1: complex, z2: complex) -> complex:
    """Implementa z1 / z2 (Regra 1)."""
    if z2 == 0:
        # Detecta e rejeita a divisão por zero (Regra 5)
        raise ZeroDivisionError("Divisão por zero não permitida.")
    return z1 / z2

def potencia(z: complex, n: complex) -> complex:
    """Implementa z ** n (Regra 1)."""
    return z ** n

def conjugado(z: complex) -> complex:
    """
    Calcula o conjugado de z. (a - bi) (Regra 1)
    """
    return z.conjugate()

def raiz(z: complex, n: complex) -> complex or list[complex]:
    """
    Calcula as raízes n-ésimas de z (Regra 1).
    Retorna a primeira raiz (k=0) como resultado da expressão.
    """
    # Se o índice da raiz (n) não for um número real positivo (>= 1), trata como potência
    if n.imag != 0 or n.real < 1 or n.real != int(n.real):
        return z ** (1/n)
    
    n_int = int(n.real)
    
    if n_int == 0:
        raise ValueError("O índice da raiz não pode ser zero.")
        
    r = abs(z)  # Módulo (r)
    theta = cmath.phase(z)  # Argumento (theta)
    
    # Cálculo apenas da primeira raiz (k=0) para a execução da expressão:
    angle = theta / n_int
    modulus_root = r ** (1/n_int)
    
    return complex(
        modulus_root * math.cos(angle),
        modulus_root * math.sin(angle)
    )

# --- Função de Formatação (Chamada pelo expression_handler e main) ---

def formatar(z: complex or float) -> str:
    """
    Formata o número complexo (Regra 0).
    Garante que 'j' (interno) seja exibido como 'i' (externo) no formato (a+bi).
    """
    z = complex(z)
    real_part = z.real
    imag_part = z.imag
    
    # Arredondamento para evitar problemas de precisão
    real_part = round(real_part, 8)
    imag_part = round(imag_part, 8)
    
    if imag_part == 0:
        return f"({real_part})"
    if real_part == 0:
        return f"({imag_part}i)"
    
    op = '+' if imag_part > 0 else ''
    
    return f"({real_part}{op}{imag_part}i)"