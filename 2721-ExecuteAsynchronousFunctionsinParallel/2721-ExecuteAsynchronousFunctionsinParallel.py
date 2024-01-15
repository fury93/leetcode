        }
        
        const res = new Array(functions.length).fill(null);

        let resolvedCount = 0;

        functions.forEach(async (el,idx) => {
            try {
                const subResult = await el();
                res[idx] = subResult;
                resolvedCount++;
                if(resolvedCount=== functions.length) {
                    resolve(res);
                }
            } catch(err) {
                reject(err);
            }
        });
    });
};
[() => new Promise(resolve => setTimeout(() => resolve(5), 200))]
[() => new Promise(resolve => setTimeout(() => resolve(1), 200)), () => new Promise((resolve, reject) => setTimeout(() => reject("Error"), 100))
]
