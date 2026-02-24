def vsota_kvadratov_stevk(n):
    stotica = n // 100
    desetica = (n // 10) % 10
    enica = n % 10
    return stotica ** 2 + desetica ** 2 + enica ** 2 

def obrat(n):
    stotica = n // 100
    desetica = (n // 10) % 10
    enica = n % 10
    return enica * 100 + desetica * 10 + stotica 

def dodaj_kontrolno_stevko(sklic):
    n = sklic
    vsota = 0
    utez = 2
    for _ in range(12):
        stevka = n % 10
        vsota += stevka * utez
        n //= 10
        utez += 1
    ostanek = vsota % 11
    k = 11 - ostanek
    kontrolna = 0 if k == 10 else k
    return sklic * 10 + kontrolna

def je_prestopno(leto):
    if leto % 400 == 0:
        return True
    if leto % 100 == 0:
        return False
    if leto % 4 == 0:
        return True
    else:
        return False 
    
def stevilo_dni(mesec, leto):
    if mesec in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mesec in [4, 6, 9, 11]:
        return 30
    elif mesec == 2:
        return 29 if je_prestopno(leto) else 28
    
def je_veljaven_datum(dan, mesec, leto):
    if not (1 <= mesec <= 12) or leto < 1:
        return False
    return 1 <= dan <= stevilo_dni(mesec, leto)

def disjunkcija(a, b):
    return a or b

def negacija(a):
    return not a

def implikacija(a, b):
    return not a or b 

def evikvalenca(a, b):
    return a == b

def xor(a, b):
    if a == b:
        return False
    else:
        return True
    
def nand(a, b):
    return not (a and b)

def negacija_nand(a):
    return nand(a, a)

def disjunkcija(a, b):
    return nand(nand(a, a), nand(b, b))

def konjunkcija(a, b):
    pogoj = nand(a, b)
    return nand(pogoj, pogoj)

def enostavno_obrestovanje(polog, mesecna_obrestna_mera, st_mesecev):
    a = polog
    m = mesecna_obrestna_mera
    n = st_mesecev
    return a * (1 + m * n)

def obrestno_obrestovanje(polog, mesecna_obrestna_mera, st_mesecev):
    a = polog
    m = mesecna_obrestna_mera
    n = st_mesecev
    return a * ((1 + m) ** n)

def pretvori_v_letno_obrestno_mero(mesecna_obrestna_mera):
    m = mesecna_obrestna_mera
    faktor_leta = (1 + m) ** 12
    letna_stopnja = (faktor_leta - 1) * 100
    return round(letna_stopnja)