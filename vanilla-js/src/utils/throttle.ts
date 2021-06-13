import type { Parameters } from "./types";

export function throttle<T extends (...args: any[]) => any>(
  fn: T,
  wait = 1000
): (...args: Parameters<T>) => void {
  let timer: number | undefined;

  return function (...args: Parameters<T>) {
    if (!timer) {
      timer = window.setTimeout(function () {
        fn(args);
        timer = undefined;
      }, wait);
    }
  };
}
