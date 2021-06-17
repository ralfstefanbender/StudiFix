import LearningProfile from './LearningProfileBO';

export default class LearningProfileUserBO extends LearningProfile {


  /**
   * Constructs a new LearningProfileUserBO
   *
   */
  constructor(aUserId) {
    super();
    this.user_id = aUserId;

  }



  /**
   * Sets the user id of the Learnprofileuser .
   *
   */
  setUserId(aUserId) {
    this.user_id = aUserId;
  }

  /**
   * Gets the user id of the Learnprofileuser.
   */
  getUserId() {
    return this.user_id;
  }




  /**
   * Sets the group id of the Learnprofilegroup .
   *
   */
  setGroupId(aGroupId) {
    this.group_id = aGroupId;
  }

  /**
   * Gets the gorup id of the Learnprofile.
   */
  getGroupId() {
    return this.group_id;
  }


  
  /**
   * Returns an Array of  learningprofileUserBO from a given JSON structure
   */
 
  static fromJSON(learningprofileusers) {
    let result = [];

    if (Array.isArray(learningprofileusers)) {
      learningprofileusers.forEach((a) => {
        Object.setPrototypeOf(a, LearningProfileUserBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = learningprofileusers;
      Object.setPrototypeOf(a, LearningProfileUserBO.prototype);
      result.push(a);
    }

    return result;
  }
}