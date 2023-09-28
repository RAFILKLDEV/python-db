criarTabela = ''' CREATE TABLE CARROS (
    id INTEGER NOT NULL,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    motor TEXT NOT NULL,
    cor TEXT NOT NULL,
    PRIMARY KEY (id)
)
'''

inserirCarro = '''
    INSERT INTO CARROS (id, marca, modelo, motor, cor) VALUES
    (1, 'Ford', 'Fiesta', 'Motor v6', 'Amarelo')
    
    '''