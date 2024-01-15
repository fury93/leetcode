
    const newObj = {};
    let isEmpty = true

    for(const key in node) {
      const subRes = dfs(node[key]);
      if(subRes!== undefined) {
        newObj[key] = subRes;
        isEmpty = false
      }
    }

    if(isEmpty) return undefined;

    return newObj;
  }

  return dfs(obj);
}

[-5,-4,-3,-2,-1,0,1]
(x) => x > 0
{"a":1,"b":"2","c":3,"d":"4","e":5,"f":6,"g":{"a":1}}
