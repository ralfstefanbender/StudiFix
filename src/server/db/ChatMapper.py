from src.server.db.Mapper import Mapper
from src.server.bo.Chat import Chat


class ChatMapper(Mapper):

    def __init__(self):
        super().__init__()

    def build_bo(self, tuples):

        result = []

        if len(tuples) == 1:
            for (id, name, creation_date) in tuples:
                chat = Chat()
                chat.set_id(id)
                chat.set_name(name)
                chat.set_creation_date(creation_date)
                result = chat

        else:
            for (id, name, creation_date) in tuples:
                chat = Chat()
                chat.set_id(id)
                chat.set_name(name)
                chat.set_creation_date(creation_date)
                result.append(chat)

            return result

    def find_all(self):

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM chat"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, creation_date FROM chat " \
                  "WHERE id LIKE '{}' ".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls kein Chat mit der angegebenen id gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, creation_date FROM chat " \
                  "WHERE name LIKE '{}' ".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls kein Chat mit dem angegebenen Namen gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, chat):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from chat")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                chat.set_id(1)
            else:
                chat.set_id(maxid[0] + 1)

        command = "INSERT INTO chat (id, name, creation_date) VALUES " \
                  "('{}','{}','{}')".format(chat.get_id(), chat.get_name(), chat.get_creation_date())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

        return chat

    def update(self, chat):

        cursor = self._cnx.cursor()
        command = "UPDATE chat SET name = ('{}'), " \
                  "creation_date = ('{}') " \
                  "WHERE id = ('{}')" \
            .format(chat.get_name(), chat.get_creation_date(), chat.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, chat):
        cursor = self._cnx.cursor()

        command = "DELETE FROM chat WHERE id={}".format(chat.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if (__name__ == "__main__"):
    with ChatMapper() as mapper:
            chat = Chat()
            chat.set_name("Mathe Chat")
            chat.set_id(2)

            mapper.insert(chat)

            # Nach mapper jegliche Methode dieser Klasse