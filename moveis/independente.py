import sqlite3

def obter_preco_material(codigo_material):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT preço FROM materiais WHERE codigo = ?
    ''', (codigo_material,))
    preco = cursor.fetchone()[0]
    conn.close()
    return preco[0] if preco else None

def calc_independente(material,dimensoes):
    preco_material=obter_preco_material(material)
    area_total=dimensoes[0]*dimensoes[1]*dimensoes[2]
    custo_material = area_total * preco_material
    mao_de_obra = area_total * 10  # exemplo de custo de mão de obra
    custo_total = custo_material + mao_de_obra