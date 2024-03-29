from src.server.bo import BusinessObject as bo


# Group Invitation Klasse
class GroupInvitation(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._is_accepted = False
        self._study_group_id = 0
        self._target_user = 0
        self._source_user = 0

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

    # Erstellung von Group Invitation mit Dictionary
    @staticmethod
    def from_dict(dictionary=dict()):
        obj = GroupInvitation()
        obj.set_id(dictionary["id"])
        obj.set_creation_date(dictionary["creation_date"])
        obj.set_source_user(dictionary["source_owner"])
        obj.set_target_user(dictionary["target_owner"])
        obj.set_study_group_id(dictionary["study_group_id"])
        obj.set_is_accepted(dictionary["is_accepted"])
        return obj
