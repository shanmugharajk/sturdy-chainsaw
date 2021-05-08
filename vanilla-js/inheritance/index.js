// @ts-nocheck
function Employee(company, name) {
  this.name = name;
  this.company = company;
}

Employee.prototype.printDetails = function () {
  console.log(`Employee details - ${this.name}, ${this.company}`);
};

function SpaceXEmployee(name, spaceXId) {
  Employee.call(this, "SapceX", name);
  this.spaceXId = spaceXId;
}

SpaceXEmployee.prototype = Object.create(Employee.prototype);

const sherlock = new SpaceXEmployee("sherlock", 221);
sherlock.printDetails();
