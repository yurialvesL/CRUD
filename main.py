from multiprocessing import context
import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao= pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor


    )
    try:
        yield conexao
    finally:
        print('conxao fechada')
        conexao.close()

#with conecta() as conexao:  MANEIRA 1 DE INSERIR EM TABELAa
    #with conexao.cursor() as cursor:
        #sql = 'INSERT INTO clientes (nome,sobrenome, idade, peso) VALUES '\
            #'(%s,%s,%s,%s)'
        #cursor.execute(sql,('Yuri','Alves','22','80'))
        #conexao.commit()


#with conecta() as conexao: 
    #with conexao.cursor() as cursor:
        #sql = 'INSERT INTO clientes (nome,sobrenome, idade, peso) VALUES '\
            #'(%s,%s,%s,%s)'

        #dados = [
            #('MURIEL','FIGUEREDO','30','85'),
            #('CAMILLA','ALVES','25','70'),
            #('JOSE','FIGUEREDO','19','85'),

        #]
        #cursor.executemany(sql,dados)
        #conexao.commit()

#with conecta() as conexao: MANEIRA 1 DE EXCLUIR EM TABELA
    #with conexao.cursor() as cursor:
        #sql = 'DELETE FROM clientes WHERE id = %s '
        #cursor.execute(sql,(6,))
        #conexao.commit()

#with conecta() as conexao:  MANEIRA 2 DE EXCLUIR EM TABELA
   # with conexao.cursor() as cursor:
        #sql = 'DELETE FROM clientes WHERE id IN(%s,%s,%s) '
        #cursor.execute(sql,(7,8,9))
        #conexao.commit()

#with conecta() as conexao: MANEIRA 4 DE EXCLUIR EM TABELA
   #with conexao.cursor() as cursor:
        #sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s '
        #cursor.execute(sql,(11,13))
        #conexao.commit()


with conecta() as conexao: #UPDATE 
   with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s '
        cursor.execute(sql,('JOANA',5))
        conexao.commit()



with conecta() as conexao: #seleciona os dados
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes  ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)




