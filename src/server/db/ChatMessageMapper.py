from src.server.db.Mapper import Mapper
from src.server.bo.ChatMessage import ChatMessage


class ChatMessageMapper(Mapper):

    def __init__(self):
        super().__init__()

    def build_bo(self, tuples):

        result = []

        if len(tuples) == 1:
            for (id, text, creation_date, chat_id, user_id) in tuples:
                chat_message = ChatMessage()
                chat_message.set_id(id)
                chat_message.set_text(text)
                chat_message.set_chat_id(chat_id)
                chat_message.set_user_id(user_id)
                result = chat_message

        else:
            for (id, text, creation_date, chat_id, user_id) in tuples:
                chat_message = ChatMessage()
                chat_message.set_id(id)
                chat_message.set_text(text)
                chat_message.set_chat_id(chat_id)
                chat_message.set_user_id(user_id)
                result.append(chat_message)

        return result

    def find_all(self):

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM chat_message"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, text, creation_date, chat_id, user_id FROM chat_message " \
                  "WHERE id LIKE '{}' ".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls keine ChatMessage mit der angegebenen id gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_by_chat_id(self, chat_id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, text, creation_date, chat_id, user_id FROM chat_message " \
                  "WHERE chat_id LIKE '{}' ".format(chat_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls keine ChatMessage mit der angegebenen id gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, chat_message):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from chat_message")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                chat_message.set_id(1)
            else:
                chat_message.set_id(maxid[0] + 1)

        command = "INSERT INTO chat_message (id, text, creation_date, chat_id, user_id) VALUES " \
                  "('{}','{}','{}','{}','{}')" \
            .format(chat_message.get_id(), chat_message.get_text(),
                    chat_message.get_creation_date(), chat_message.get_chat_id(), chat_message.get_user_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

        return chat_message

    def update(self, chat_message):

        cursor = self._cnx.cursor()
        command = "UPDATE chat_message SET text = ('{}'), creation_date = ('{}'), chat_id = ('{}')," \
                  " user_id = ('{}') " \
                  "WHERE id = ('{}')" \
            .format(chat_message.get_text(),
                    chat_message.get_creation_date(), chat_message.get_chat_id(), chat_message.get_user_id(),
                    chat_message.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, chat_message):

        cursor = self._cnx.cursor()
        try:
            command = "DELETE FROM chat_message WHERE id = ('{}')".format(chat_message.get_id())
            cursor.execute(command)

            self._cnx.commit()
            cursor.close()
        except:
            pass

if (__name__ == "__main__"):
    with ChatMessageMapper() as mapper:
        chat_message = ChatMessage()
        chat_message.set_text("")
        chat_message.set_chat_id(1)
        chat_message.set_user_id(1)

        mapper.insert(chat_message)
