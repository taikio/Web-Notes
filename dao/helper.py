from dao import connection


class DaoHelper(object):

    def __init__(self):
        self.connect = connection.ConnectionFactory()

    def criarTabelas(self):
        self.connect.iniciaConexao()

        sqlTarefas = """ CREATE TABLE IF NOT EXISTS tarefas
              (id integer primary key autoincrement,
              titulo varchar(100),
              descricao varchar(200),
              data varchar(10),
              empresa varchar(50))"""

        self.connect.cursor.execute(sqlTarefas)

        self.connect.fechaConexao()