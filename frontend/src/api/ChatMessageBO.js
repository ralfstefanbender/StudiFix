import BusinessObject from './BusinessObject';

/**
 * Represents an chatinvitation.
 */
export default class ChatMessageBO extends ChatMessage  {

  /**
   * Constructs a new ChatMessageBO
   *
   */
  constructor(aChatId, aUserId, aText) {
    super();
    this.chat_id = aChatId;
    this.user_id = aUserId;
    this.text = aText;

  }

  /**
   * Sets the source owner of the chatmessage .
   *
   */
  setChatId(aChatId) {
    this.chat_id= aChatId;
  }

  /**
   * Gets the  source owner of the chatinvitation.
   */
  getChatId() {
    return this.chat_id;
  }

  /**
   * Sets the user of the chatmessage .
   *
   */
  setUserId(aUserId) {
    this.user_id = aUserId;
  }

  /**
   * Gets the user of the chatmessage.
   */
  getUserId() {
    return this.target_owner;
  }

  /**
   * Sets the text of the chatmessage .
   *
   */
  setText(aText) {
    this.text = aText;
  }

  /**
   * Gets the  text of the chat.
   */
  getText() {
    return this.text;
  }




  /**
   * Returns an Array of  chatmessageBO from a given JSON structure
   */
  static fromJSON(chatmessages) {
    let result = [];

    if (Array.isArray(chatmessages)) {
      chatmessages.forEach((a) => {
        Object.setPrototypeOf(a, ChatMessageBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = chatmessage;
      Object.setPrototypeOf(a, ChatMessageBO.prototype);
      result.push(a);
    }

    return result;
  }
}