function throttle(fn, delay) {
  let timer;

  return function (args) {
    if (!timer) {
      setTimeout(() => {
        fn(args);
      }, delay || 1000);
    }
  };
}

let throttleCtr = 0;

document.getElementById("btn").onclick = throttle(function () {
  console.log(++throttleCtr);
});
