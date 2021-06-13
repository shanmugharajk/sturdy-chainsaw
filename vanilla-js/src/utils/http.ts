export const $http = {
  get: async function (url: string) {
    const result = await fetch(url);
    const json = await result.json();

    if (result.status !== 200) {
      throw json;
    }

    return json;
  },
};
