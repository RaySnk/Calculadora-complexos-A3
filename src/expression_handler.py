import complex_operations
import cmath
import re

OPERADORES = {
    '+': (1, complex_operations.soma),
    '-': (1, complex_operations.subtracao),
    '*': (2, complex_operations.multiplicacao),
    '/': (2, complex_operations.divisao),
    '**': (3, complex_operations.potencia),
    'raiz': (4, complex_operations.raiz),
    'conjugado': (4, complex_operations.conjugado)
}
PRECEDENCIA = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
REGEX_VARIAVEL = re.compile(r'\b[a-hj-z]\b(?![a-z0-9_])') 

def parse_literal(token):
    token = token.strip().replace('i', 'j')
    try:
        return complex(token)
    except ValueError:
        return token

def tokenize(expressao):
    tokens = re.findall(r"[\+\-\*/\(\)\*\*]|[a-hj-z0-9\.\+\-]+i|[a-hj-z0-9\.\+\-]+|[a-hj-z]", expressao.replace(' ', ''))
    
    clean_tokens = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token == '-':
            if i == 0 or tokens[i-1] in '(*+/-':
                if i + 1 < len(tokens):
                    try:
                        num = parse_literal(tokens[i+1])
                        if not isinstance(num, str):
                            clean_tokens.append(complex(0) - num)
                            i += 1
                        else:
                            clean_tokens.append(token)
                    except ValueError:
                        clean_tokens.append(token)
                else:
                    clean_tokens.append(token)
            else:
                clean_tokens.append(token)
        elif token == '+' and (i == 0 or tokens[i-1] in '(*+/-'):
             i += 1
             continue
        else:
            clean_tokens.append(token)
        i += 1
    return clean_tokens

def parse_expression(tokens):
    if not tokens:
        return 0

    if len(tokens) == 1:
        return parse_literal(tokens[0])

    depth = 0
    min_prec = 5
    op_index = -1

    for i, token in enumerate(tokens):
        if token == '(': depth += 1
        elif token == ')': depth -= 1
        
        if depth == 0 and token in PRECEDENCIA:
            prec = PRECEDENCIA[token]
            if prec <= min_prec:
                min_prec = prec
                op_index = i
    
    if op_index != -1:
        op = tokens[op_index]
        left = parse_expression(tokens[:op_index])
        right = parse_expression(tokens[op_index+1:])
        return [op, left, right]

    if tokens[0] == '(' and tokens[-1] == ')':
        return parse_expression(tokens[1:-1])

    if tokens[0] in ['raiz', 'conjugado']:
        if tokens[1] == '(' and tokens[-1] == ')':
            return [tokens[0], parse_expression(tokens[2:-1])]
        
    return 0

def format_lisp_output(arvore):
    if not isinstance(arvore, list):
        if isinstance(arvore, complex) or isinstance(arvore, float):
            return complex_operations.formatar(arvore).replace("(", "").replace(")", "")
        return str(arvore)
    
    op = arvore[0]
    args = ' '.join(format_lisp_output(arg) for arg in arvore[1:])
    return f"({op} {args})"

def encontrar_variaveis(expressao):
    variaveis = set(REGEX_VARIAVEL.findall(expressao.lower()))
    return variaveis

def construir_arvore_lisp(expressao):
    tokens = tokenize(expressao)
    arvore = parse_expression(tokens)
    
    if arvore != 0:
        arvore_lisp_str = format_lisp_output(arvore)
        print(f"Árvore Sintática LISP: {arvore_lisp_str}") # Regra 6
    
    return arvore

def executar_arvore(arvore, valores_variaveis):
    if not isinstance(arvore, list):
        if isinstance(arvore, str):
            if arvore in valores_variaveis:
                return valores_variaveis[arvore] # Regra 7
        return arvore
    
    operador_str = arvore[0]
    op_info = OPERADORES.get(operador_str)

    if op_info is None:
        return f"Erro: Operador desconhecido '{operador_str}'"
    
    funcao = op_info[1]
    
    operandos_avaliados = [executar_arvore(operando, valores_variaveis) for operando in arvore[1:]] # Regra 4

    for op in operandos_avaliados:
        if isinstance(op, str) and op.startswith("Erro:"):
            return op

    if operador_str == '/' and len(operandos_avaliados) > 1 and operandos_avaliados[1] == 0:
        return "Erro: Divisao por zero" # Regra 5

    try:
        if len(operandos_avaliados) == 2:
            return funcao(operandos_avaliados[0], operandos_avaliados[1])
        elif len(operandos_avaliados) == 1:
            return funcao(operandos_avaliados[0])
        else:
            return f"Erro: Número incorreto de argumentos para o operador '{operador_str}'"
            
    except Exception as e:
        return f"Erro durante a execução: {e}"

def checar_erro(expressao):
    if expressao.count('(') != expressao.count(')'):
        return False
    return True

def resolver_expressao(expressao):
    if not checar_erro(expressao):
        return "Erro: Expressão mal formada (parênteses desbalanceados)." # Regra 5

    variaveis = encontrar_variaveis(expressao)
    valores_variaveis = {}
    
    if variaveis:
        print(f"\nVariáveis encontradas: {', '.join(variaveis)}. Favor fornecer valores.")
        for var in sorted(list(variaveis)):
            while True:
                try:
                    valor_str = input(f"Digite o valor (complexo ou real) para '{var}' (ex: 5+2i): ")
                    valores_variaveis[var] = complex(valor_str.replace('i', 'j')) 
                    break
                except ValueError:
                    print("Valor inválido. Use o formato 'a+bi' ou apenas um número.") # Regra 7

    arvore = construir_arvore_lisp(expressao) 

    if arvore == 0:
        return "Erro: Expressão complexa ou sintaxe inválida para o parser." # Regra 5

    resultado = executar_arvore(arvore, valores_variaveis)
    
    if isinstance(resultado, complex) or isinstance(resultado, float):
        return complex_operations.formatar(resultado) # Regra 0
    else:
        return resultado

def checar_igualdade(expressao1, expressao2):
    print("\nVerificando se as expressões são iguais...")
    
    res1_formatado = resolver_expressao(expressao1)
    
    if res1_formatado.startswith("Erro:"):
        return f"Não é possível comparar (Expressão 1): {res1_formatado}"

    res2_formatado = resolver_expressao(expressao2)
    
    if res2_formatado.startswith("Erro:"):
        return f"Não é possível comparar (Expressão 2): {res2_formatado}"
        
    try:
        res1_valor = complex(res1_formatado.replace('i', 'j'))
        res2_valor = complex(res2_formatado.replace('i', 'j'))
        
        return res1_valor == res2_valor # Regra 3

    except Exception:
        return f"Não é possível comparar devido a erro interno."