from src.server.db.Mapper import Mapper
from src.server.bo.StudyGroup import StudyGroup


class StudyGroupMapper(Mapper):

    def __init__(self):
        super().__init__()

    def build_bo(self, tuples):

        result = []

        if len(tuples) == 1:
            for (id, name, creation_date, chat_id) in tuples:
                studygroup = StudyGroup()
                studygroup.set_id(id)
                studygroup.set_name(name)
                studygroup.set_creation_date(creation_date)
                studygroup.set_chat_id(chat_id)
                result = studygroup

        else:
            for (id, name, creation_date, chat_id,) in tuples:
                studygroup = StudyGroup()
                studygroup.set_id(id)
                studygroup.set_name(name)
                studygroup.set_creation_date(creation_date)
                studygroup.set_chat_id(chat_id)
                result.append(studygroup)

        return result

    def find_all(self):

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM studygroup"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, creation_date, chat_id FROM studygroup " \
                  "WHERE id LIKE '{}' ".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls keine Study_Group mit der angegebenen id gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_chat_id(self, chat_id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, creation_date, chat_id FROM studygroup " \
                  "WHERE chat_id LIKE '{}' ".format(chat_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls keine Study_Group mit der angegebenen id gefunden werden konnte,
                wird hier None als RÃ¼ckgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_group_name(self, name):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, creation_date, chat_id FROM studygroup " \
                  "WHERE name LIKE '{}' ".format(name)

        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, studygroup):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from studygroup")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                studygroup.set_id(1)
            else:
                studygroup.set_id(maxid[0] + 1)

        command = "INSERT INTO studygroup (id, name, creation_date, chat_id) VALUES " \
                  "('{}','{}','{}','{}')"\
                .format(studygroup.get_id(), studygroup.get_name(),
                        studygroup.get_creation_date(), studygroup.get_chat_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

        return studygroup

    def update(self, studygroup):

        cursor = self._cnx.cursor()
        command = "UPDATE studygroup SET name = ('{}'), creation_date = ('{}'), chat_id = ('{}')" \
                  "WHERE id = ('{}')" \
            .format(studygroup.get_name(), studygroup.get_creation_date(),
                    studygroup.get_chat_id(), studygroup.get_id())


        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, studygroup):

        cursor = self._cnx.cursor()
        command = "DELETE FROM studygroup WHERE id = ('{}')".format(studygroup.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if (__name__ == "__main__"):
    with StudyGroupMapper() as mapper:
        studygroup = StudyGroup()
        studygroup.set_name("Studifix1")
        studygroup.set_chat_id(1)

        mapper.insert(studygroup)
        mapper.find_by_group_name("Studifix1")
        print(mapper)
        # Nach mapper jegliche Methode dieser Klasse