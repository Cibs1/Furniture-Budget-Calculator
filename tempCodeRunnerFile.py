import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('orcamentos_cozinha.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS materiais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    nome TEXT NOT NULL,
    medida TEXT NOT NULL,
    preço FLOAT NOT NULL
)
''')

# Inserindo dados na tabela de materiais
materiais = [
    (1,'PL0015', 'Aglomerado crú 16mm', 'M2', 4.70)
    (2,'PL0300', 'Aglomerado crú 19mm', 'M2', 5.99)
    (3,'PL0397', 'Aglomerado Egger H1346 ST32 19mm', 'M2', 22.03)
    (4,'PL0003', 'Aglomerado folheado carvalho 16mm', 'M2', 13.54)
    (5,'PL0004', 'Aglomerado folheado carvalho 19mm', 'M2', 14.00)
    (6,'PL0376', 'Aglomerado folheado pinho A/B SuperPan 19mm', 'M2', 7.80)
    (7,'PL0336', 'Aglomerado laminado 16mm gramagem 100', 'M2', 5.60)
    (8,'PL0016', 'Aglomerado laminado branco 08mm', 'M2', 4.37)
    (9,'PL0018', 'Aglomerado laminado branco 16mm', 'M2', 4.17)
    (10,'PL0289', 'Aglomerado laminado branco superpan 10mm', 'M2', 4.80)
    (11,'PL0169', 'Aglomerado laminado branco superpan 16mm', 'M2', 7.10)
    (12,'PL0254', 'Aglomerado laminado branco superpan 19mm', 'M2', 6.02)
    (13,'PL0386', 'Aglomerado laminado carvalho superpan 10mm', 'M2', 5.92)
    (14,'PL0279', 'Aglomerado laminado carvalho superpan 16mm', 'M2', 7.10)
    (15,'PL0286', 'Aglomerado laminado nero U129/Smart 19mm', 'M2', 12.88)
    (16,'PL0039', 'Aglomerado laminado vermelho 19mm', 'M2', 6.93)
    (17,'PL0243', 'Contraplacado bétula carvalho 15mm', 'M2', 36.00)
    (18,'PL0163', 'Contraplacado bétula carvalho 18mm A/B', 'M2', 40.00)
    (19,'PL0053', 'Contraplacado bétula mogno 15mm A/C', 'M2', 28.00)
    (20,'PL0046', 'Contraplacado choupo 15/16mm', 'M2', 19.50)
    (21,'PL0047', 'Contraplacado choupo 18mm', 'M2', 22.00)
    (22,'PL0060', 'Decoratex carvalho 03mm', 'M2', 6.50)
    (23,'PL0194', 'Folha de carvalho composto', 'M2', 8.46)
    (24,'PL0388', 'Folha de carvalho rustico', 'M2', 3.75)
    (25,'PL0151', 'Folha de cerejeira', 'M2', 5.00)
    (26,'PL0238', 'Folha de nogueira', 'M2', 8.33)
    (27,'PL0394', 'Folha Eucalipto Painel B', 'M2', 1.10)
    (28,'PL0395', 'Folha Pinho Painel FC (A)', 'M2', 2.50)
    (29,'PL0316', 'Folhinha Afizélia Pachyloba', 'M2', 5.95)
    (30,'PL0359', 'Folhinha de Carvalho', 'M2', 4.28)
    (31,'PL0239', 'HPL egger F509 ST2 08mm', 'M2', 10.62)
    (32,'PL0217', 'Fórmica OberBois gougés ashen oak T310 sat 1.3mm', 'M2', 75.36)
    (33,'PL0314', 'Fórmica OberFlex Crezo Americano r-m sati M1', 'M2', 68.40)
    (34,'PL0216', 'Fórmica OberFlex roble T326 salvia sat 1mm', 'M2', 59.99)
    (35,'PL0069', 'MDF 03mm', 'M2', 2.40)
    (36,'PL0070', 'MDF 05mm', 'M2', 3.42)
    (37,'PL0077', 'MDF hidrofugo 16mm', 'M2', 10.00)
    (38,'PL0079', 'MDF hidrofugo 19mm', 'M2', 11.25)
    (39,'PL0321', 'Orla ABS H1346 ST32 0.8X23mm', 'MLineares', 0.46)
    (40,'PL0323', 'Orla ABS U999 ST12 0.8/23mm', 'MLineares', 0.46)
    (41,'PL0320', 'Orla ABS U999 ST38 0.8/23mm', 'MLineares', 0.46)
    (42,'PL0090', 'Orla folha madeira carvalho 0.5x25mm com fleece', 'MLineares', 0.35)
    (43,'PL0092', 'Orla folha madeira carvalho 2x23mm', 'MLineares', 0.75)
    (44,'PL0091', 'Orla folha madeira carvalho composto 0.5x23mm com fleece', 'MLineares', 0.35)
    (45,'PL0094', 'Orla folha madeira faia 2x23mm', 'MLineares', 0.35)
    (46,'PL0242', 'Orla folha madeira faia vaporizada 23mm com fleece', 'MLineares', 0.30)
    (47,'PL0096', 'Orla folha madeira mogno 0.5x23mm', 'MLineares', 0.30)
    (48,'PL0105', 'Orla PVC branco SF 1x22mm', 'MLineares', 0.28)
    (49,'PL0119', 'Orla PVC carvalho 1x23mm', 'MLineares', 0.30)
    (50,'PL0100', 'Orla PVC cinza escuro 1x35mm', 'MLineares', 0.30)
    (51,'PL0273', 'Orla PVC cinza liso 1x23mm top face', 'MLineares', 0.30)
    (52,'PL0361', 'Orla PVC Linho Cancun Ptextil 23mm', 'MLineares', 0.30)
    (53,'PL0113', 'Orla PVC mogno 0.4x23mm', 'MLineares', 0.35)
    (54,'PL0315', 'Piso flutuante Finsa Original AC5 Columbia', 'M2', 9.01)
    (55,'PL0202', 'Piso pav eco rob prov 101 RWT', 'M2', 6.25)
    (56,'PL0083', 'Platex 3.2mm', 'M2', 1.66)
    (57,'PL0225', 'Rodapé contraplacado carvalho 2.5', 'MLineares', 3.50)
    (58,'PL0248', 'Rodapé madeira bol carvalho env. 15', 'MLineares', 3.90)
    (59,'PL0084', 'Termolaminado AR Plus cinza 18mm', 'M2', 24.00)
    (60,'PL0396', 'Aglomerado folheado carv. listado 16mm', 'M2', 20.40)
    (61,'PL0402', 'Aglomerado folheado carv. listado 19mm', 'M2', 21.00)
    (62,'PL0398', 'Contraplacado betula cru BB/BB 18mm', 'M2', 25.30)
    (63,'PL0399', 'Contraplacado mogn 18mm', 'M2', 36.50)
    (64,'PL0400', 'Aglomerado laminado cinsa soft 8mm', 'M2', 5.70)
    (65,'PL0401', 'Aglomerado laminado cinsa soft 16mm', 'M2', 6.75)
    (66,'PL0403', 'Aglomerado Egger W980 ST2 19mm', 'M2', 12.70)
    (67,'PL0404', 'Aglomerado Egger W980 ST2 16mm', 'M2', 8.56)
    (68,'PL0405', 'Aglomerado Egger F425 ST10 16mm', 'M2', 8.56)
    (69,'PL0406', 'Pavimento flut. Carv Ame Top G04 cru acustico', 'M2', 56.70)
    (70,'PL0407', 'HPL Egger W980 ST2 0.8mm', 'M2', 10.65)
    (71,'PL0408', 'HPL Egger F274 ST9 0.8mm', 'M2', 16.00)
    (72,'PL0409', 'Aglomerado Egger U113 ST9 16mm', 'M2', 8.56)
]


cursor.executemany('''
INSERT INTO materiais (id,codigo,nome,medida,preço) 
VALUES (?,?,?,?,?) 
''',materiais  ) 