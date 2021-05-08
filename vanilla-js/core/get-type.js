function getType(val) {
  if (val === null) {
    return "null";
  }

  if (Object.prototype.toString.call(val) === "[object Array]") {
    return "array";
  }

  if (Object.prototype.toString.call(val) === "[object Object]") {
    return "object";
  }

  return typeof val;
}

function testGetType() {
  console.log(getType(null));
  console.log(getType(undefined));
  console.log(getType(true));
  console.log(getType([]));
  console.log(getType({}));
  console.log(getType(() => {}));
}
