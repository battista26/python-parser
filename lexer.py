import ply.lex as lex

tokens = (
    'LET',
    'DEF',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'RETURN',
    'DOGRU',
    'YANLIS',

    'TANIMLAYICI',
    'TAMSAYI',
    'ONDALIKLI',

    'TOPLA',
    'CIKAR',
    'CARP',
    'BOL',
    'MODUL',

    'ATAMA',
    'ESIT',
    'ESIT_DEGIL',
    'KUCUK',
    'BUYUK',
    'KUCUK_ESIT',
    'BUYUK_ESIT',

    'VE',
    'VEYA',
    'DEGIL',
    
    'SOL_PARANTEZ',
    'SAG_PARANTEZ',
    'SOL_SUSLU_PARANTEZ',
    'SAG_SUSLU_PARANTEZ',
    'SOL_KOSELI_PARANTEZ',
    'SAG_KOSELI_PARANTEZ',

    'NOKTALI_VIRGUL',
    'VIRGUL'
)

reserved = {
    'let': 'LET',
    'def': 'DEF',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'return': 'RETURN',
    'true': 'DOGRU',
    'false': 'YANLIS'
}


t_TOPLA = r'\+'
t_CIKAR = r'-'
t_CARP = r'\*'
t_BOL = r'/'
t_MODUL = r'%'
t_ATAMA = r'='
t_ESIT = r'=='
t_ESIT_DEGIL = r'!='
t_KUCUK = r'<'
t_BUYUK = r'>'
t_KUCUK_ESIT = r'<='
t_BUYUK_ESIT = r'>='
t_VE = r'&&'
t_VEYA = r'\|\|'
t_DEGIL = r'!'
t_SOL_PARANTEZ = r'\('
t_SAG_PARANTEZ = r'\)'
t_SOL_SUSLU_PARANTEZ = r'\{'
t_SAG_SUSLU_PARANTEZ = r'\}'
t_SOL_KOSELI_PARANTEZ = r'\['
t_SAG_KOSELI_PARANTEZ = r'\]'
t_NOKTALI_VIRGUL = r';'
t_VIRGUL = r','

# boşluk ve tab karakterlerini yoksay
t_ignore = ' \t\r'

# yorum satırlarını yoksay
def t_YORUM(t):
    r'\#.*'
    pass 

def t_ONDALIKLI(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_TAMSAYI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TANIMLAYICI(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'TANIMLAYICI')  # Check for reserved words
    # print(f"IDENTIFIER: {t.value} {t.lineno}")
    return t

# sıra numaraları takibi
def t_satirbasi(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Geçersiz karakter '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# dosyadan okuma
""" with open('test3.lang', 'r', encoding='utf-8') as f:
    lexer.input(f.read()) """

# tokenize
""" for tok in lexer:
   print(tok) """

if __name__ == "__main__":
    lexer.input("let x = 10 + 20 * (30 - 5);")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)