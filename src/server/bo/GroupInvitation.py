from src.server.bo import BusinessObject as bo


class GroupInvitation(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._study_group_id = 0
        self._source_user = None
        self._target_user = None
        self._is_accepted = False

    def get_study_group_id(self):
        return self._study_group_id

    def set_study_group_id(self, value):
        self._study_group_id = value

    def get_source_user(self):
        return self._source_user

    def set_source_user(self, value):
        self._source_user = value

    def get_target_user(self):
        return self._target_user

    def set_target_user(self, value):
        self._target_user = value

    def get_is_accepted(self):
        return self._is_accepted

    def set_is_accepted(self, value):
        self._is_accepted = value

    def switch_accepted(self):
        if self._is_accepted is True:
            self._is_accepted = False
        else:
            self._is_accepted = True

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = GroupInvitation()
        obj.set_id(dictionary["id"])
        obj.set_creation_date(GroupInvitation.date_format(dictionary["creation_date"]))
        obj.set_study_group_id(dictionary["study_group_id"])
        obj.set_source_user(dictionary["source_user"])
        obj.set_target_user(dictionary["target_user"])
        obj.set_is_accepted(dictionary["is_accepted"])

        return obj
