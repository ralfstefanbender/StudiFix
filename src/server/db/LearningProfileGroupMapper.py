from src.server.db.Mapper import Mapper
from src.server.bo.LearningprofileGroup import LearningProfileGroup


class LearningProfileGroupMapper(Mapper):

    def __init__(self):
        super().__init__()

    def build_bo(self, tuples):

        result = []

        if len(tuples) == 1:
            for (id, group_id, name, prev_knowledge, extroversion, study_state, frequency,
                 learntyp, semester, interest, degree_course, creation_date) in tuples:
                learning_profile = LearningProfileGroup()
                learning_profile.set_id(id)
                learning_profile.set_group_id(group_id)
                learning_profile.set_name(name)
                learning_profile.set_prev_knowledge(prev_knowledge)
                learning_profile.set_extroversion(extroversion)
                learning_profile.set_study_state(study_state)
                learning_profile.set_frequency(frequency)
                learning_profile.set_learntyp(learntyp)
                learning_profile.set_semester(semester)
                learning_profile.set_interest(interest)
                learning_profile.set_degree_course(degree_course)
                learning_profile.set_creation_date(creation_date)
                result = learning_profile

        else:
            for (id, group_id, name, prev_knowledge, extroversion, study_state, frequency,
                 learntyp, semester, interest, degree_course, creation_date) in tuples:
                learning_profile = LearningProfileGroup()
                learning_profile.set_id(id)
                learning_profile.set_group_id(group_id)
                learning_profile.set_name(name)
                learning_profile.set_prev_knowledge(prev_knowledge)
                learning_profile.set_extroversion(extroversion)
                learning_profile.set_study_state(study_state)
                learning_profile.set_frequency(frequency)
                learning_profile.set_learntyp(learntyp)
                learning_profile.set_semester(semester)
                learning_profile.set_interest(interest)
                learning_profile.set_degree_course(degree_course)
                learning_profile.set_creation_date(creation_date)
                result.append(learning_profile)

        return result

    def find_all(self):

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM learning_profile_group"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, group_id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile " \
                  "WHERE id LIKE '{}' ".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls kein LearningProfile Group mit der angegebenen id gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, group_id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile " \
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

    def insert(self, learning_profile):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from learning_profile_group")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                learning_profile.set_id(1)
            else:
                learning_profile.set_id(maxid[0] + 1)

        command = "INSERT INTO learning_profile (id, group_id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date) VALUES " \
                  "('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')" \
            .format(learning_profile.get_id(),
                    learning_profile.get_group_id(),
                    learning_profile.get_name(),
                    learning_profile.get_prev_knowledge(),
                    learning_profile.get_extroversion(),
                    learning_profile.get_study_state(),
                    learning_profile.get_frequency(),
                    learning_profile.get_learntyp(),
                    learning_profile.get_semester(),
                    learning_profile.get_interest(),
                    learning_profile.get_degree_course(),
                    learning_profile.get_creation_date())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

        return learning_profile

    def update(self, learning_profile):

        cursor = self._cnx.cursor()
        command = "UPDATE learning_profile_group SET name = ('{}'), group_id = ('{}'), prev_knowledge = ('{}'), extroversion = ('{}')," \
                  " study_state = ('{}'), frequency = ('{}'), learntyp = ('{}'), semester = ('{}')," \
                  " interest = ('{}'), degree_course = ('{}'), creation_date = ('{}') WHERE id = ('{}')" \
            .format(learning_profile.get_id(),
                    learning_profile.get_group_id(),
                    learning_profile.get_name(),
                    learning_profile.get_prev_knowledge(),
                    learning_profile.get_extroversion(),
                    learning_profile.get_study_state(),
                    learning_profile.get_frequency(),
                    learning_profile.get_learntyp(),
                    learning_profile.get_semester(),
                    learning_profile.get_interest(),
                    learning_profile.get_degree_course(),
                    learning_profile.get_creation_date())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, learning_profile):

        cursor = self._cnx.cursor()
        command = "DELETE FROM learning_profile_group WHERE id = ('{}')".format(learning_profile.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

if (__name__ == "__main__"):
    with LearningProfileGroupMapper() as mapper:
        learning_profile = LearningProfileGroup()
        learning_profile.set_name("Informatik")
        learning_profile.set_group_id(1)
        learning_profile.set_prev_knowledge("Garkeine")
        learning_profile.set_extroversion(2)
        learning_profile.set_study_state(3)
        learning_profile.set_frequency(4)
        learning_profile.set_learntyp(5)
        learning_profile.set_semester(6)
        learning_profile.set_degree_course("Wirtschaftsinformatik")

        mapper.insert(learning_profile)