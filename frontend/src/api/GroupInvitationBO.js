import BusinessObject from './BusinessObject';

/**
 * Represents an groupinvitation.
 */
export default class GroupInvitationBO extends BusinessObject  {

  /**
   * Constructs a new ChatInvitationBO
   *
   */
  constructor(aIsAccepted, aStudyGroupId, aSourceOwner, aTargetUser) {
    super();
    this.is_accepted = aIsAccepted;
    this.study_group_id = aStudyGroupId;
    this.target_user = aTargetUser;
    this.source_owner = aSourceOwner;

  }

  /**
   * Sets the source owner of the groupinvitation .
   *
   */
  setSourceOwner(aSourceOwner) {
    this.source_owner = aSourceOwner;
  }

  /**
   * Gets the  source owner of the groupinvitation.
   */
  getSourceOwner() {
    return this.source_owner;
  }

  /**
   * Sets the target owner of the groupinvitation .
   *
   */
  setTargetOwner(aTargetOwner) {
    this.target_owner = aTargetOwner;
  }

  /**
   * Gets the  target owner of the chatinvitation.
   */
  getTargetOwner() {
    return this.target_owner;
  }

  /**
   * Sets the chat id  of the groupinvitation .
   *
   */
  setStudyGroupId(aStudyGroupId) {
    this.study_group_id = aStudyGroupId;
  }

  /**
   * Gets the  Chat id of the groupinvitation.
   */
  getStudyGroupId() {
    return this.study_group_id;
  }



  /**
   * Sets the is acceptedof the groupinvitation .
   *
   */
  setIsAccepted(aIsAccepted) {
    this.is_accepted = aIsAccepted;
  }

  /**
   * Gets the is accepted of the chatinvitation.
   */
  getIsAccepted() {
    return this.is_accepted;
  }


  /**
   * Returns an Array of  chatinvitationBO from a given JSON structure
   */
  static fromJSON(groupinvitations) {
    let result = [];

    if (Array.isArray(groupinvitations)) {
      groupinvitations.forEach((a) => {
        Object.setPrototypeOf(a, GroupInvitationBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = groupinvitations;
      Object.setPrototypeOf(a, GroupInvitationBO.prototype);
      result.push(a);
    }

    return result;
  }
}