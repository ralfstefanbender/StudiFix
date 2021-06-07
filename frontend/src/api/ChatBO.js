import NamedBusinessObject from './NamedBusinessObject';

/**
 * Represents an account object of a customer.
 */
export default class ChatBO extends Chat  {

  /**
   * Constructs a new ChatBO
   *
   */
  constructor() {
    super();
  }


  /**
   * Returns an Array of  chatBO from a given JSON structure
   */
  static fromJSON(chats) {
    let result = [];

    if (Array.isArray(chats)) {
      chats.forEach((a) => {
        Object.setPrototypeOf(a, ChatBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = chat;
      Object.setPrototypeOf(a, ChatBO.prototype);
      result.push(a);
    }

    return result;
  }
