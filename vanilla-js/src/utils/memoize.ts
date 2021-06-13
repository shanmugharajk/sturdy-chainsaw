import { isDeepEqual } from "./is-deep-equal";
import type { Parameters, ReturnType } from "./types";

export function memoize<T extends (...args: any[]) => any>(
  func: T,
): (...funcArgs: Parameters<T>) => ReturnType<T> {
  let prevArgs: Parameters<T>;
  let prevResult: ReturnType<T>;

  return (...args: Parameters<T>): ReturnType<T> => {
    if (isDeepEqual(args, prevArgs ?? [])) {
      return prevResult;
    }

    prevResult = func(...args);
    prevArgs = args;

    return prevResult;
  };
}
