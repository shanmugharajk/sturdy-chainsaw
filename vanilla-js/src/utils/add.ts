type Add = {
  (num: number): Add;
  value: number;
};

export function add(num: number) {
  let res = 0;

  let _add: Add = Object.assign((num: number) => {
    if (typeof num === "undefined") {
      throw new Error("Please enter number.");
    }
    res = res + num;
    _add.value = res;
    return _add;
  });

  return _add(num);
}
