import LearningProfile from './LearningProfile';

export default class LearningProfileBO extends LearningProfile  {

  /**
   * Constructs a new LearningProfilenBO
   *
   */
  constructor(aGroupId) {
    super();
    this.group_id = aGroupId;

  }



  /**
   * Sets the group id of the Learnprofilegroup .
   *
   */
  setGroupId(aGroupId) {
    this.group_id = aGroupId;
  }

  /**
   * Gets the gorup id of the Learnprofilegroup.
   */
  getGroupId() {
    return this.group_id;
  }







     /**
   * Returns an Array of  learningprofilegroupBO from a given JSON structure
   */

  static fromJSON(learningprofilegroups) {
    let result = [];

    if (Array.isArray(learningprofilegroups)) {
      learningprofilegroups.forEach((a) => {
        Object.setPrototypeOf(a, LearningProfileGroupBO.prototype);
        result.push(a);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = learningprofilegroup;
      Object.setPrototypeOf(a, LearningProfileGroupBO.prototype);
      result.push(a);
    }

    return result;
  }
}