

criar = '''--sql
CREATE TABLE CARROS (
    id INTEGER NOT NULL AUTOINCREMENT,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    motor TEXT NOT NULL,
    cor TEXT NOT NULL,
    PRIMARY KEY (id)
)
'''

inserirCarro = '''
    INSERT INTO CARROS ( marca, modelo, motor, cor) VALUES
    ('Fiat', 'Uno', 'Motor 1.0', 'Branco')
    '''

inserirPessoa = '''
    INSERT INTO PESSOAS (cpf, nome) VALUES
    (42602156820, 'Ana')
'''

criarTabelaPessoas = '''
    CREATE TABLE PESSOAS (
    id INTEGER NOT NULL,
    cpf INTEGER NOT NULL,
    nome TEXT NOT NULL,
    UNIQUE (cpf),
    PRIMARY KEY (id)
)
'''

deletePessoas = '''
    DROP TABLE PESSOAS
'''

join = '''
    SELECT * FROM PESSOAS
    INNER JOIN CARROS USING(id)
'''
