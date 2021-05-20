from src.server.db.Mapper import Mapper
from src.server.bo.StudyGroup import StudyGroup


class StudyGroupMapper(Mapper):

    def __init__(self):
        super().__init__()

    def build_bo(self, tuples):

        result = []

        if len(tuples) == 1:
            for (id, group_name, chat_id, learning_profile_id, creation_date) in tuples:
                studygroup = StudyGroup()
                studygroup.set_id(id)
                studygroup.set_group_name(group_name)
                studygroup.set_chat_id(chat_id)
                studygroup.set_learning_profile_id(learning_profile_id)
                studygroup.set_creation_date(creation_date)
                result = studygroup

        else:
            for (id, group_name, chat_id, learning_profile_id, creation_date) in tuples:
                studygroup = StudyGroup()
                studygroup.set_id(id)
                studygroup.set_group_name(group_name)
                studygroup.set_chat_id(chat_id)
                studygroup.set_learning_profile_id(learning_profile_id)
                studygroup.set_creation_date(creation_date)
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
        command = "SELECT id, group_name, chat_id, learning_profile_id, creation_date FROM studygroup " \
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

    def find_by_group_name(self, group_name):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, group_name, chat_id, learning_profile_id, creation_date FROM studygroup " \
                  "WHERE group_name LIKE '{}' ".format(group_name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_group_by_learning_profile_id(self, learning_profile_id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, group_name, chat_id, learning_profile_id, creation_date FROM studygroup " \
                  "WHERE learning_profile_id LIKE '{}' ".format(learning_profile_id)
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

        command = "INSERT INTO studygroup (id, group_name, chat_id, learning_profile_id, creation_date) VALUES " \
                  "('{}','{}','{}','{}','{}')"\
                .format(studygroup.get_id(), studygroup.get_group_name(),
                        studygroup.get_chat_id(), studygroup.get_learning_profile_id(), studygroup.get_creation_date())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

        return studygroup

    def update(self, studygroup):

        cursor = self._cnx.cursor()
        command = "UPDATE studygroup SET group_name = ('{}'), chat_id = ('{}'), learning_profile_id = ('{}')," \
                  " creation_date = ('{}') " \
                  "WHERE id = ('{}')" \
            .format(studygroup.get_group_name(),
                    studygroup.get_chat_id(), studygroup.get_creation_date(), studygroup.get_learning_profile_id(),
                    studygroup.get_id())
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
        studygroup.set_group_name("Studifix1")
        studygroup.set_chat_id(1)
        studygroup.set_learning_profile_id(1)

        mapper.insert(studygroup)
        mapper.find_by_group_name("Studifix1")
        print(mapper)
        # Nach mapper jegliche Methode dieser Klasse