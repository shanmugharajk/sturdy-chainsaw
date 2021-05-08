function debounce(fn, delay) {
  let timer;

  return function (args) {
    if (timer) {
      clearTimeout(timer);
    }

    timer = setTimeout(() => {
      fn(args);
    }, delay || 1000);
  };
}

let ctr = 0;

document.getElementById("btn").onclick = debounce(function () {
  console.log(++ctr);
}, 500);
