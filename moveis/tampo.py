import sqlite3
#from precoMaterial import obter_preco_material

def obter_preco_pedra(nome):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT preco_m2 FROM pedras WHERE nome = ?
    ''', (nome,))
    preco = cursor.fetchone()
    conn.close()
    return preco[0] if preco else None

def calc_tampo(nome ,dimensoes):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    preco_m2 = float(obter_preco_pedra(nome))
    custo_total = preco_m2 * dimensoes[0] * dimensoes[1]
    cursor.close()
    return custo_total