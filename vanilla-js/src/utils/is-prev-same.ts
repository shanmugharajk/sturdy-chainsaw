export const isPrevSame = (function () {
  let prev: any;

  function fn<T>(val: T) {
    const isSame = prev === val;
    prev = val;
    return isSame;
  }

  return fn;
})();
