def somma(a,b):
    return a + b

def sottrazione(a,b):
    return a - b

def moltiplicazione(a,b):
    return a * b

def divisione(a,b):
    if b == 0:
        raise ValueError("Non si possono effettuare divizioni per 0.")
    else:
        return a / b