import cmath
import math

def soma(z1: complex, z2: complex) -> complex:
    return z1 + z2

def subtracao(z1: complex, z2: complex) -> complex:
    return z1 - z2

def multiplicacao(z1: complex, z2: complex) -> complex:
    return z1 * z2

def divisao(z1: complex, z2: complex) -> complex:
    if z2 == 0:
        raise ZeroDivisionError("Divisão por zero não permitida.")
    return z1 / z2

def potencia(z: complex, n: complex) -> complex:
    return z ** n

def conjugado(z: complex) -> complex:
    return z.conjugate()

def raiz(z: complex, n: complex) -> complex or list[complex]:
    if n.imag != 0 or n.real < 1 or n.real != int(n.real):
        return z ** (1/n)
    
    n_int = int(n.real)
    
    if n_int == 0:
        raise ValueError("O índice da raiz não pode ser zero.")
        
    r = abs(z)
    theta = cmath.phase(z)
    
    angle = theta / n_int
    modulus_root = r ** (1/n_int)
    
    return complex(
        modulus_root * math.cos(angle),
        modulus_root * math.sin(angle)
    )

def formatar(z: complex or float) -> str:
    z = complex(z)
    real_part = z.real
    imag_part = z.imag
    
    real_part = round(real_part, 8)
    imag_part = round(imag_part, 8)
    
    if imag_part == 0:
        return f"({real_part})"
    if real_part == 0:
        return f"({imag_part}i)"
    
    op = '+' if imag_part > 0 else ''
    return f"({real_part}{op}{imag_part}i)"
