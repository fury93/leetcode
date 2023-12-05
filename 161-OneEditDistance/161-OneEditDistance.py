"
        # mode 1 - insert,  2-remove, 3 - change
        if l1 < l2: mode = 1
        elif l1 > l2: mode = 2
        else: mode = 3

        i, j, isEdited = 0, 0, False

        while i < l1 or j < l2:
            ss = s[i] if i < l1 else None
            tt = t[j] if j < l2 else None
            if ss != tt:
                if isEdited: return False
                isEdited = True
                if mode == 1:
                    j += 1
                    continue
                elif mode == 2:
                    i += 1
                    continue
            i += 1
            j += 1
        
        return isEdited
