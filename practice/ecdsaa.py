P = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 64 - 16 - 1  # Primo que define o campo finito
A = 0  # Coeficiente 'a' da curva
B = 7  # Coeficiente 'b' da curva
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240  # Coordenada x do ponto gerador
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337461467  # Coordenada y do ponto gerador
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # Ordem do grupo da curva
G = (Gx, Gy)  # Ponto gerador

def mod_inverse(k, p):
    """Calcula o inverso modular de k modulo p."""
    return pow(k, -1, p)

def point_add(P1, P2, p):
    """Soma dois pontos na curva elíptica."""
    if P1 is None:
        return P2
    if P2 is None:
        return P1

    x1, y1 = P1
    x2, y2 = P2

    if x1 == x2 and y1 != y2:
        return None

    if x1 == x2:
        # Duplicação de ponto
        m = (3 * x1**2 + A) * mod_inverse(2 * y1, p) % p
    else:
        # Soma de dois pontos diferentes
        m = (y2 - y1) * mod_inverse(x2 - x1, p) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

def scalar_mult(k, P, p):
    """Multiplica um escalar por um ponto na curva elíptica."""
    R = None
    Q = P

    while k:
        if k & 1:
            R = point_add(R, Q, p)
        Q = point_add(Q, Q, p)
        k >>= 1

    return R

# Chave privada
private_key = P

# Chave pública (multiplicação escalar da chave privada pelo ponto gerador)
public_key = scalar_mult(private_key, G, P)

# Mostrando os resultados
print("Chave privada (hex):", hex(private_key))
print("Chave pública (x):", public_key[0])
print("Chave pública (y):", public_key[1])
