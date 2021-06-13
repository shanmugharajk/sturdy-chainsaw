export function interval(wait: number) {
  const subscribe = (fn: () => void) => {
    const timer = setInterval(fn, wait);

    return () => {
      clearInterval(timer);
    };
  };

  return { subscribe };
}
