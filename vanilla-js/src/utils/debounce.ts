export function debounce<T extends (...args: any[]) => any>(
  fn: T,
  wait = 1000
): (...args: Parameters<T>) => void {
  let timer: number;

  return function (...args: Parameters<T>) {
    if (timer) {
      clearTimeout(timer);
    }

    timer = window.setTimeout(() => {
      fn(args);
    }, wait || 1000);
  };
}
