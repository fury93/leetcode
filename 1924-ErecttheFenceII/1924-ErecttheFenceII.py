                if len(R) == 0: return (0, 0, 0)
                if len(R) == 1: return (R[0][0], R[0][1], 0)
                if len(R) == 2: 
                    (x0, y0), (x1, y1) = R
                    return ((x0+x1)/2, (y0+y1)/2, sqrt((x0-x1)**2+(y0-y1)**2)/2)
            x, y, r = fn(i+1, R)
            if (trees[i][0]-x)**2 + (trees[i][1]-y)**2 < r**2: return (x, y, r)
            return fn(i+1, R + [trees[i]])
            
        return fn(0, [])
[
