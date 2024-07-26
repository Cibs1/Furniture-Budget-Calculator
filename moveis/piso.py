import sqlite3
#from precoMaterial import obter_preco_material

def obter_preco_material(nome_material):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT preco_m2 FROM piso WHERE nome = ?
    ''', (nome_material,))
    preco = cursor.fetchone()
    conn.close()
    return preco[0] if preco else None

def calc_piso(dimensoes,nome_material):
    area_total=dimensoes[0]*dimensoes[1]
    custo_material = obter_preco_material(nome_material) * area_total
    mao_de_obra = area_total * 15  # exemplo de custo de mão de obra
    custo_total = custo_material + mao_de_obra
    return custo_total