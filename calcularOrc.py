import sqlite3
from moveis.armario import calc_armario
from moveis.piso import calc_piso
from moveis.tampo import calc_tampo
from moveis.independente import calc_independente
from moveis.coluna import *

#from moveis.precoMaterial import obter_preco_material

def calc_orcamento():
    #conn = sqlite3.connect('orcamentos_cozinha.db')
    preco_total = 0
    tpmovel=input("Digite o tipo de móvel que quer adicionar: ")
    codigo_material=input("Digite o codigo do material que deseja usar: ")
    while (tpmovel != ("sair")):
        comprimento = float(input("Digite o comprimento do móvel em mm: "))
        profundidade = float(input("Digite a profundidade do móvel em mm: "))
        altura = float(input("Digite a altura do móvel em mm: "))
        dimensoes = [comprimento, profundidade, altura]
        if (tpmovel=="coluna"):
            codigo_material_orla=input("Digite a orla que deseja usar: ")
            portas=input("nº de portas: ")
            gavetas=input("nº de gavetas: ")
            gavetões=input("nº de gavetões: ")
            prateleiras=input("nº de prateleiras: ")
            preco_total+=calc_coluna(codigo_material ,dimensoes,gavetas,gavetões,portas,prateleiras,codigo_material_orla)
        if (tpmovel=="inferior"):
            codigo_material_orla=input("Digite a orla que deseja usar: ")
            portas=input("nº de portas: ")
            gavetas=input("nº de gavetas: ")
            gavetões=input("nº de gavetões: ")
            prateleiras=input("nº de prateleiras: ")
            preco_total+=calc_coluna(codigo_material ,dimensoes,gavetas,gavetões,portas,prateleiras,codigo_material_orla)
        if (tpmovel=="superior"):
            codigo_material_orla=input("Digite a orla que deseja usar: ")
            portas=input("nº de portas: ")
            gavetas=input("nº de gavetas: ")
            gavetões=input("nº de gavetões: ")
            prateleiras=input("nº de prateleiras: ")
            preco_total+=calc_coluna(codigo_material ,dimensoes,gavetas,gavetões,portas,prateleiras,codigo_material_orla)    
        if (tpmovel=="piso"):
            nome_material=input("Digite o nome do material do piso: ")
            area_piso = input("Digite a área do piso em m2: ")
            preco_total+=calc_piso(area_piso,nome_material)
        if(tpmovel=='tampo'):
            area_tampo = input("Digite a área do piso em m2: ")
            nome_material=input("Digite o nome do material do tampo: ")
            preco_total+=calc_tampo(nome_material,area_tampo)
        if(tpmovel=='remate' or tpmovel=='placa' or tpmovel=='painel'):
            nome_material=input("Digite o nome do material: ")
            preco_total+=calc_independente(nome_material,dimensoes)
        tpmovel=input("Digite o tipo de móvel que quer adicionar: ")

    return preco_total

# Exemplo de uso


#orcamento = calc_orcamento()
#print(f"O orçamento total da cozinha é: {orcamento:.2f}€")
