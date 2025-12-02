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
    if isinstance(token, (complex, float, int)):
        return token
        
    token = token.strip().replace('i', 'j')
    try:
        return complex(token)
    except ValueError:
        return token

def tokenize(expressao):
    tokens = re.findall(r"raiz|conjugado|\*\*|[\+\-\*/\(\)]|[a-hj-z0-9\.]*i|[a-hj-z0-9\.]+|[a-hj-z]", expressao.replace(' ', ''))
    
    clean=[]
    i=0
    while i < len(tokens):
        t=tokens[i]
        
        if t == '-':
            is_unary=False
            
            if i==0:
                is_unary=True
            elif clean:
                last = clean[-1]
                if isinstance(last, str) and last in '(*+/-': 
                    is_unary=True
            
            if is_unary and i + 1 < len(tokens):
                next_t=tokens[i+1]
                n=parse_literal(next_t)
                if not isinstance(n, str): 
                    clean.append(complex(0) - n) 
                    i += 2 
                    continue
        
        clean.append(t)
        i += 1
        
    return clean

def parse_expression(tokens):
    if not tokens:
        return 0

    if len(tokens) == 1:
        return parse_literal(tokens[0])

    depth = 0
    min_prec = 5
    op_i = -1

    for i, t in enumerate(tokens):
        if t == '(':
            depth += 1
        elif t == ')':
            depth -= 1
        if depth == 0 and t in PRECEDENCIA:
            p = PRECEDENCIA[t]
            if p <= min_prec:
                min_prec = p
                op_i = i
    
    if op_i != -1:
        op = tokens[op_i]
        left = parse_expression(tokens[:op_i])
        right = parse_expression(tokens[op_i+1:])
        return [op, left, right]

    if tokens[0] == '(' and tokens[-1] == ')':
        return parse_expression(tokens[1:-1])

    if tokens[0] in ['raiz', 'conjugado'] and tokens[1] == '(' and tokens[-1] == ')':
        return [tokens[0], parse_expression(tokens[2:-1])]

    return 0

def format_lisp_output(arvore):
    if not isinstance(arvore, list):
        if isinstance(arvore, complex) or isinstance(arvore, float):
            return complex_operations.formatar(arvore).replace("(", "").replace(")", "")
        return str(arvore)
    op = arvore[0]
    args = ' '.join(format_lisp_output(a) for a in arvore[1:])
    return f"({op} {args})"

def encontrar_variaveis(expressao):
    return set(REGEX_VARIAVEL.findall(expressao.lower()))

def construir_arvore_lisp(expressao):
    tokens = tokenize(expressao)
    arvore = parse_expression(tokens)
    if arvore != 0:
        print("Árvore Sintática LISP:", format_lisp_output(arvore))
    return arvore

def executar_arvore(arvore, valores):
    if not isinstance(arvore, list):
        if isinstance(arvore, str) and arvore in valores:
            return valores[arvore]
        return arvore
    
    op_str = arvore[0]
    op_info = OPERADORES.get(op_str)
    if op_info is None:
        return f"Erro: Operador desconhecido '{op_str}'"
    f = op_info[1]
    aval = [executar_arvore(a, valores) for a in arvore[1:]]
    for a in aval:
        if isinstance(a, str) and a.startswith("Erro:"):
            return a
    if op_str == '/' and len(aval) > 1 and aval[1] == 0:
        return "Erro: Divisao por zero"
    try:
        if len(aval) == 2:
            return f(aval[0], aval[1])
        if len(aval) == 1:
            return f(aval[0])
        return f"Erro: Número incorreto de argumentos para '{op_str}'"
    except Exception as e:
        return f"Erro durante a execução: {e}"

def checar_erro(expressao):
    return expressao.count('(') == expressao.count(')')

def resolver_expressao(expressao):
    if not checar_erro(expressao):
        return "Erro: Expressão mal formada (parênteses desbalanceados)."
    vars = encontrar_variaveis(expressao)
    vals = {}
    if vars:
        print("\nVariáveis encontradas:", ", ".join(vars))
        for v in sorted(list(vars)):
            while True:
                try:
                    inp = input(f"Digite o valor para '{v}' (ex: 5+2i): ")
                    vals[v] = complex(inp.replace('i', 'j'))
                    break
                except:
                    print("Valor inválido.")
    arv = construir_arvore_lisp(expressao)
    if arv == 0:
        return "Erro: Expressão complexa ou sintaxe inválida."
    res = executar_arvore(arv, vals)
    if isinstance(res, (complex, float)):
        return complex_operations.formatar(res)
    return res

def checar_igualdade(e1, e2):
    print("\nVerificando se as expressões são iguais...")
    r1 = resolver_expressao(e1)
    if isinstance(r1, str) and r1.startswith("Erro:"):
        return f"Não é possível comparar (Expressão 1): {r1}"
    r2 = resolver_expressao(e2)
    if isinstance(r2, str) and r2.startswith("Erro:"):
        return f"Não é possível comparar (Expressão 2): {r2}"
    try:
        return complex(r1.replace('i', 'j')) == complex(r2.replace('i', 'j'))
    except:
        return "Não é possível comparar devido a erro interno."
