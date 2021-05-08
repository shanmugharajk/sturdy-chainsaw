// @ts-nocheck
function Employee(company, name) {
  this.name = name;
  this.company = company;
}

Employee.prototype.printDetails = function () {
  console.log(`Employee details - ${this.name}, ${this.company}`);
};

function SpaceXEmployee(name, spaceXId) {
  // == calling employee with this 'this' and params ==
  Employee.call(this, "SapceX", name);
  this.spaceXId = spaceXId;
}

SpaceXEmployee.prototype = Object.create(Employee.prototype);

const sherlock = new SpaceXEmployee("sherlock", 221);
sherlock.printDetails();

// == binding for object literal ==
const obj = {
  printName() {
    console.log(this.name);
  },
};

obj.printName.call({ name: "sherlock" });
