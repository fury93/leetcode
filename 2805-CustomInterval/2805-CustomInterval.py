
      dfs();

      return customId;
         }, delay + period * count);
         count++;
         intervalMap.set(customId, timerId);
      }
      function dfs() {
         const timerId = setTimeout(() => {
            fn();
            dfs();
   let intervalIdCounter = 0;
   const intervalMap = new Map();

   function setCustomInterval(fn, delay, period) {
      let count = 0;
      const customId = intervalIdCounter++;

const CustomInterval = (() => {
50
20
225
