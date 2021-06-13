export function timer(wait: number) {
  const subscribe = (fn: () => void) => {
    const timer = setTimeout(fn, wait);

    return () => {
      clearTimeout(timer);
    };
  };

  return { subscribe };
}
