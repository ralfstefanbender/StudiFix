import NamedBusinessObject from './NamedBusinessObject';

export default class StudyGroupBO extends NamedBusinessObject {


  /**
   * Constructs a new StudyGroupBO
   *
   */
  constructor(aChatId) {
    super();
    this.chat_id = aChatId;

  }



  /**
   * Sets the user id of the StudyGroupBO .
   *
   */
  setChatId(aChatId) {
    this.chat_id = aChatId;
  }

  /**
   * Gets the user id of the StudyGroupBO .
   */
  getChatId() {
    return this.chat_id;
  }





  /**
   * Returns an Array of  StudyGroupBO from a given JSON structure
   */

  static fromJSON(studygroups) {
    let result = [];

    if (Array.isArray(studygroups)) {
      studygroups.forEach((a) => {
        Object.setPrototypeOf(a, StudyGroupBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = studygroup;
      Object.setPrototypeOf(a, StudyGroupBO.prototype);
      result.push(a);
    }

    return result;
  }
}