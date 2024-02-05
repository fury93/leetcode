                even.append(i)
            else:
                odd.append(i)
        odd.sort()
        even.sort()
        res = 0
        for i in range(n):
            if arr[i] % 2 == 0:
                res = res*10 + even.pop()
            else:
                res = res*10 + odd.pop()
        return res
1
