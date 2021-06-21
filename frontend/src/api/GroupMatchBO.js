import BusinessObject from './BusinessObject';

/**
 * Represents a groupinvitation.
 */
export default class GroupMatchBO extends BusinessObject  {

  /**
   * Constructs a new ChatInvitationBO
   *
   */
  constructor(aName, aSemester, aInterest, aScore) {
    super();
    this.name = aName;
    this.semester = aSemester;
    this.interest = aInterest;
    this.score = aScore;

  }

  /**
   * Sets the source owner of the groupinvitation .
   *
   */
  setName(aName) {
    this.name = aName;
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
  static fromJSON(match) {
    let result = [];

    if (Array.isArray(match)) {
      match.forEach((a) => {
        Object.setPrototypeOf(a, GroupMatchBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = match;
      Object.setPrototypeOf(a, GroupMatchBO.prototype);
      result.push(a);
    }

    return result;
  }
}