from dao import connection


class TarefasDao(object):

    def __init__(self):
        self.connect = connection.ConnectionFactory()

    def cadastrar(self, tarefa):

        self.connect.iniciaConexao()

        try:
            sql = "INSERT INTO tarefas(titulo,descricao,data,empresa) VALUES" \
                       "(' "+tarefa.titulo+" ',' "+tarefa.descricao+" ',' "+tarefa.data+" ',' "+tarefa.empresa+" '); "

            self.connect.cursor.execute(sql)
            self.connect.con.commit()
            self.connect.fechaConexao()
            return
        except RuntimeError:
            return

    def retornaTodos(self):

        try:

            self.connect.iniciaConexao()
            sql = "SELECT * FROM tarefas"
            self.connect.cursor.execute(sql)
            lista = list()

            for registro in self.connect.cursor.fetchall():
                tarefa = {}

                tarefa['id'] = registro[0]
                tarefa['titulo'] = registro[1]
                tarefa['descricao'] = registro[2]
                tarefa['data'] = registro[3]
                tarefa['empresa'] = registro[4]

                lista.append(tarefa)
            return lista
        except RuntimeError:
            return

    def deletar(self,id):

        try:
            self.connect.iniciaConexao()
            self.connect.cursor.execute("DELETE FROM tarefas WHERE id = %s" % id)
            self.connect.con.commit()
            self.connect.fechaConexao()
            return
        except RuntimeError:
            return