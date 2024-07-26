import sqlite3

def obter_preco_material(codigo_material):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT preco_m2 FROM materiais WHERE codigo = ?
    ''', (codigo_material,))
    preco = cursor.fetchone()
    conn.close()
    return preco[0] if preco else None

def obter_preco_pedra(nome):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT preco_m2 FROM pedras WHERE nome = ?
    ''', (nome,))
    preco = cursor.fetchone()
    conn.close()
    return preco[0] if preco else None