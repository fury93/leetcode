        shiftRes = 0
        for direction, amount in shift:
            if direction == 0:
                shiftRes -= amount
            else:
                shiftRes += amount
        shiftRes = shiftRes % len(s)

        if shiftRes < 0:
            shiftRes = abs(shiftRes)
            return s[shiftRes:] + s[:shiftRes]
        else:
            return s[-shiftRes:] + s[:-shiftRes]

