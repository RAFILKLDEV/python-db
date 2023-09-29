criarTabelaPessoa = '''--sql
    CREATE TABLE PESSOA (
    id_pessoa INTEGER NOT NULL,
    nome TEXT NOT NULL,
    cpf INTEGER NOT NULL,
    PRIMARY KEY (id_pessoa)
    )
'''

criarTabelaLista = '''--sql
    CREATE TABLE LISTA (
    id_lista INTEGER NOT NULL,
    nome TEXT NOT NULL,
    id_anime INTEGER,
    id_pessoa INTEGER,
    FOREIGN KEY (id_anime) REFERENCES ANIME (id_anime),
    FOREIGN KEY (id_pessoa) REFERENCES PESSOA (id_pessoa),
    PRIMARY KEY (id_lista)
    )
'''

criarTabelaAnime = '''--sql
    CREATE TABLE ANIME (
    id_anime INTEGER NOT NULL,
    nome TEXT NOT NULL,
    lancamento INTEGER NOT NULL,
    id_estudio INTEGER,
    FOREIGN KEY (id_estudio) REFERENCES ESTUDIO (id_estudio),
    PRIMARY KEY (id_anime)
    )
'''

criarTabelaEstudio = '''--sql
    CREATE TABLE ESTUDIO (
    id_estudio INTEGER NOT NULL,
    nome TEXT NOT NULL,
    diretor TEXT NOT NULL,
    PRIMARY KEY (id_estudio)
    )
'''

addEstudio = '''--sql
    INSERT INTO ESTUDIO (nome, diretor) VALUES (
    "MADHOUSE", "Masao Maruyama"
    )

'''

addAnime = '''--sql
    INSERT INTO ANIME (nome, lancamento, id_estudio) VALUES (
    "Hunter x Hunter", 2011, 1
    )
'''

addPessoa = '''--sql
    INSERT INTO PESSOA (nome, cpf) VALUES (
    "RAFAEL ALMEIDA PENHA", 42602156809
    )
'''

addLista = '''--sql
    INSERT INTO LISTA (nome, id_anime, id_pessoa) VALUES (
    "ANIMES LEGAIS", 1, 1
    )
'''
