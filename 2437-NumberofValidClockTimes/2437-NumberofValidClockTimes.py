
        if time[3] == '?': res *= 6
        
        if time[4] == '?': res *= 10

        if time[:2] == '??':
            res *= 24
        elif time[0] == '?':
            res *= 3 if time[1] in '0123' else 2
        elif time[1] == '?':
            res *= 4 if time[0] == '2' else 10
        return res
        res = 1
"
