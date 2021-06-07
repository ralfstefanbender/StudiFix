import BusinessObject from './BusinessObject';

export default class NamedBusinessObject extends BusinessObject {

    constructor(aName) {
        super();
        this.name = aName;
    }

    // setting a new Name for Named BOs
    setName(aName) {
        this.name = aName;
    }

    // getting the Named BOs Name
    getName() {
        return this.name;
    }
}