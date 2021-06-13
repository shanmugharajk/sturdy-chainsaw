import { $http } from "./http";

export function poll<T>(url: string, wait = 2000, retry = 3) {
  let errCb: (err: Error) => void;
  let subscribed: boolean;

  let currentError: Error;
  let remaining = retry;

  async function fetch(cb: (data: T) => void) {
    try {
      const data = await $http.get(url);
      cb(data);
    } catch (error) {
      if (errCb) {
        errCb(error);
      }
      remaining = remaining - 1;
    } finally {
      if (remaining > 0) {
        setTimeout(async () => {
          fetch(cb);
        }, wait);
      }
    }
  }

  return {
    subscribe(cb: (data: T) => void) {
      try {
        if (!subscribed) {
          fetch(cb);
        }
        subscribed = true;
      } catch (error) {
        currentError = error;

        if (errCb) {
          errCb(currentError);
        }
      }

      return this;
    },

    catch(cb: (err: Error) => void) {
      if (!errCb) {
        errCb = cb;
      }

      if (currentError) {
        errCb(currentError);
      }

      return this;
    },
  };
}
