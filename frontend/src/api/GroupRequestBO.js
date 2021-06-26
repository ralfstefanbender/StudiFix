import BusinessObject from './BusinessObject';

export default class GroupRequestBO extends BusinessObject {


  /**
   * Constructs a new GroupRequestBO
   *
   */
  constructor(aGroupId, aChatId, aGoogleId, aFirstName, aLastName, aEMail, aAdress) {
    super();
    this.chat_id = aChatId;
    this.group_id = aGroupId;
    this.google_id = aGoogleId;
    this.firstname = aFirstName;
    this.lastname = aLastName;
    this.email = aEMail;
    this.adress = aAdress;
  }

/**
 * Sets the user id of the GroupRequestBO .
 *
 */
setChatId(aChatId) {
this.chat_id = aChatId;
}

/**
 * Gets the user id of the GroupRequestBO .
 */
getChatId() {
return this.chat_id;
}

/** Sets the google_id of the user */
setGoogleId(aGoogleId){
this.google_id = aGoogleId;
}

/** Gets the google_id from the user */
getGoogleId(){
    return this.google_id;
}

/** Sets the firstname of the user */
setFirstName(aFirstName){
    this.firstname = aFirstName;
}

/** Gets the firstname of the user */
getFirstName(){
    return this.firstname;
}

/** Sets the lastname of the user */
setLastName(aLastName){
    this.lastname = aLastName;
}

/** Gets the lastname of the user */
getLastName(){
    return this.lastname;
}

/** Sets the email of the user */
setEMail(aEMail){
    this.email = aEMail;
}

/** Gets the email of the user */
getEMail(){
    return this.email;
}

/** Sets the adress of the user */
setAdress(aAdress){
    this.adress = aAdress;
}

/** Gets the adress of the user */
getAdress(){
    return this.adress;
}




  /**
   * Returns an Array of  GroupRequestBO from a given JSON structure
   */

  static fromJSON(studygroups) {
    let result = [];

    if (Array.isArray(studygroups)) {
      studygroups.forEach((a) => {
        Object.setPrototypeOf(a, GroupRequestBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = studygroups;
      Object.setPrototypeOf(a, GroupRequestBO.prototype);
      result.push(a);
    }

    return result;
  }
}