// https://github.com/epoberezkin/fast-deep-equal

const isObject = (val: any) => typeof val === "object";

function isEqual(a: any, b: any) {
  // == for RegEx ==
  if (a.constructor === RegExp)
    return a.source === b.source && a.flags === b.flags;

  // == for Date ==
  // It has a valueOf method implemented in it.
  if (a.valueOf !== Object.prototype.valueOf)
    return a.valueOf() === b.valueOf();

  // == if it has a custom toString implementation use it ==
  // TODO: Figure out exact use case.
  if (a.toString !== Object.prototype.toString)
    return a.toString() === b.toString();
}

export function isDeepEqual(a: any, b: any) {
  // == check for reference equality ==
  if (a === b) return true;

  // == if any one is not object just check equality ==
  if (!isObject(a) || !isObject(b)) return isEqual(a, b);

  // == for object ==
  // == check the keys length if its a Object ==
  if (!Array.isArray(a)) {
    const keys = Object.keys(a);
    if (keys.length !== Object.keys(b).length) return false;
  }

  for (let key in a) {
    if (!isDeepEqual(a[key], b[key])) return false;
  }

  return true;
}
