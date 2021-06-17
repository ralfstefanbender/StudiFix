import NamedBusinessObject from './NamedBusinessObject';

/**
 * Represents an Learningprofile.
 */
export default class LearningProfileBO extends NamedBusinessObject  {

  /**
   * Constructs a new LearningProfileBO
   *
   */
  constructor(aPrevKnowledge, aExtroversion, aStudyState, aFrequency, aLearntyp, aSemester, aInterest, aDegreeCourse) {
    super();
    this.prev_knowledge = aPrevKnowledge;
    this.extroversion = aExtroversion;
    this.study_state = aStudyState;
    this.frequency = aFrequency;
    this.learntyp = aLearntyp;
    this.semester = aSemester;
    this.interest = aInterest;
    this.degree_course = aDegreeCourse;
  }

  /**
   * Sets the Prev Knowledge of the Learnprofile .
   *
   */
  setPrevKnowledge(aPrevKnowledge) {
    this.prev_knowledge = aPrevKnowledge;
  }

  /**
   * Gets the  Prev Knowledge of the Learnprofile.
   */
  getPrevKnowledge() {
    return this.prev_knowledge;
  }

  /**
   * Sets the extroversion of the Learnprofile .
   *
   */
  setExtroversion(aExtroversion) {
    this.extroversion = aExtroversion;
  }

  /**
   * Gets the  extroversion of the Learningprofile.
   */
  getExtroversion() {
    return this.extroversion;
  }

  /**
   * Sets the study state of thr learningprofile .
   *
   */
  setStudyState(aStudyState) {
    this.study_state= aStudyState;
  }

  /**
   * Gets the Study state of the learningprofile.
   */
  getStudyState() {
    return this.study_state;
  }



  /**
   * Sets the frequency of the leraningprofile .
   *
   */
  setFrequency(aFrequency) {
    this.frequency = aFrequency;
  }

  /**
   * Gets the frequency of the leraningprofile.
   */
  getFrequency() {
    return this.frequency;
  }


  /**
   * Sets the learntyp of the leraningprofile .
   *
   */
  setLearntyp(aLearntyp) {
    this.learntyp = aLearntyp;
  }

  /**
   * Gets the learntyp of the leraningprofile.
   */
  getLearntyp() {
    return this.learntyp;
  }

  /**
   * Sets the semester of the leraningprofile .
   *
   */
  setSemester(aSemester) {
    this.semester = aSemester;
  }

  /**
   * Gets the semesterof the leraningprofile.
   */
  getSemester() {
    return this.semester;
  }


  /**
   * Sets the interest of the leraningprofile .
   *
   */
  setInterest(aInterest) {
    this.interest = aInterest;
  }

  /**
   * Gets the interest of the leraningprofile.
   */
  getInterest() {
    return this.interest;
  }



  /**
   * Sets the degree course eof the leraningprofile .
   *
   */
  setDegreeCourse(aDegreeCourse) {
    this.degree_course = aDegreeCourse;
  }

  /**
   * Gets the Degree Course of the leraningprofile.
   */
  getDegreeCourse() {
    return this.degree_course;
  }
}