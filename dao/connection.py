import sqlite3


class ConnectionFactory(object):

    def __init__(self):
        self.con = None
        self.cursor = None

    def iniciaConexao(self):
        self.con = sqlite3.connect('tarefas.db')
        self.cursor = self.con.cursor()

    def fechaConexao(self):
        self.cursor.close()
        self.con.close()