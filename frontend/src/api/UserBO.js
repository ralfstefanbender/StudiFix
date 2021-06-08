import BusinessObject from './BusinessObject';

/**
 * Represents a user
 */
export default class UserBO extends BusinessObject {
    /**
   * Constructs a new User
   */
    constructor(aGoogleId, aFirstName, aLastName, aEMail, aAdress) {
        super();
        this.google_id = aGoogleId;
        this.firstname = aFirstName;
        this.lastname = aLastName;
        this.email = aEMail;
        this.adress = aAdress;
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
}



  /**
   * Returns an Array of  learningprofileUserBO from a given JSON structure
   */

  static fromJSON(users) {
    let result = [];

    if (Array.isArray(users)) {
      users.forEach((a) => {
        Object.setPrototypeOf(a, UserBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = user;
      Object.setPrototypeOf(a, UserBO.prototype);
      result.push(a);
    }

    return result;
  }
}