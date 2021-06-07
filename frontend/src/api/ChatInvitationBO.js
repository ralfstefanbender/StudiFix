import BusinessObject from './BusinessObject';

/**
 * Represents an chatinvitation.
 */
export default class ChatInvitationBO extends ChatInvitation  {

  /**
   * Constructs a new ChatInvitationBO
   *
   */
  constructor(aSourceUser, aTargetUser, aChatId, aIsAccepted) {
    super();
    this.source_owner = aSourceOwner;
    this.target_user = aTargetUser;
    this.chat_id = aChatId;
    this.is_accepted = aIsAccepted;
  }

  /**
   * Sets the source owner of the chatinvitation .
   *
   */
  setSourceOwner(aSourceOwner) {
    this.source_owner = aSourceOwner;
  }

  /**
   * Gets the  source owner of the chatinvitation.
   */
  getSourceOwner() {
    return this.source_owner;
  }

  /**
   * Sets the target owner of the chatinvitation .
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
   * Sets the chat id  of the chatinvitation .
   *
   */
  setChatId(aChatId) {
    this.chat_id = aChatId;
  }

  /**
   * Gets the  Chat id of the chatinvitation.
   */
  getChatId() {
    return this.chat_id;
  }



  /**
   * Sets the is acceptedof the chatinvitation .
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
  static fromJSON(chatinvitations) {
    let result = [];

    if (Array.isArray(chatinvitations)) {
      chatinvitations.forEach((a) => {
        Object.setPrototypeOf(a, ChatInvitationtBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = chatinvitation;
      Object.setPrototypeOf(a, ChatInvitationBO.prototype);
      result.push(a);
    }

    return result;
  }
}