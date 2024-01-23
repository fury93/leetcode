        if sm < k: return 0
        ribbons.sort(reverse=True)
        l, r = 1, max(ribbons)

        def isEnough(cutSize, k):
            for size in ribbons:
                if size < cutSize or k == 0: break
                k -= size // cutSize
            return k <= 0
                
        while l < r:
            m = (l + r + 1) // 2
            if isEnough(m, k):
                l = m
            else:
                r = m - 1
        
        return l
