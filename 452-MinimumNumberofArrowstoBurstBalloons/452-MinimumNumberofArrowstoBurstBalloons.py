        print(points)
        for start, end in points:
            if start > groupEnd:
                res += 1
                groupEnd = end
            else:
                groupEnd = min(groupEnd, end)
        return res
[
