      return new Promise((resolve, reject) => {
        // Introduce the delay
        setTimeout(() => {
          el()
            .then(res => {
              resolve(res);
            })
            .catch(err => {
              reject(err);
            });
        }, ms);
      });
    }

    // Add the new function with the delay to the results
  functions.forEach(el => {
    const newFuncWithPromise = () => {
  const newFunctions = [];

function delayAll(functions, ms) {
[() => new Promise((resolve) => setTimeout(resolve, 30))]
50
[() => new Promise((resolve) => setTimeout(resolve, 50)),() => new Promise((resolve) => setTimeout(resolve, 80))]
