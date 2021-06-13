export function delayed<T>(data: T, delay = 1000) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(data);
    }, delay);
  });
}

export async function sleep(wait = 2000) {
  return new Promise((resolve) =>
    setTimeout(() => resolve([true, wait]), wait),
  );
}
