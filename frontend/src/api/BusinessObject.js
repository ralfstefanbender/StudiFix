import DateFnsUtils from "@date-io/date-fns";



export default class BusinessObject {

  /**
   * The null constructor.
   */

  constructor() {
    let today = new Date(),
    date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
    this.id = 0;
    this.creation_date=date;
  }

   getDate(){
        return this.creation_date;
    }

   setDate(aCreationDate){
        this.creation_date = aCreationDate;
    }
  /**
   * Sets the ID of this BusinessObject.
   *
   * @param {*} aId - the new ID of this BusinessObject
   */
  setID(aId) {
    this.id = aId;
  }

  /**
   * Returns the ID of this BusinessObject.
   */
  getID() {
    return this.id;
  }

  /**
   * Returns a string representation of this Object. This is useful for debugging purposes.
   */
  toString() {
    let result = '';
    for (var prop in this) {
      result += prop + ': ' + this[prop] + ' ';
    }
    return result;
  }
}