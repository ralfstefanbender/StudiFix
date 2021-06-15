import NamedBusinessObject from './NamedBusinessObject';

/**
 * Represents an account object of a customer.
 */
export default class ChatBO extends NamedBusinessObject  {

  /**
   * Constructs a new ChatBO
   *
   */


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
      let a = chats;
      Object.setPrototypeOf(a, ChatBO.prototype);
      result.push(a);
    }

    return result;
  }
}
