            
            # If the two bitsets overlap, skip to the next result
            if new_chars & res_chars:
                continue
            
            # Add the current word to the result
            # and recurse to the next position
            res_chars += new_chars
            res_len += new_len
            best = max(best, self.backtracking(opt_arr, i + 1, res_chars, res_len))
            
            # Backtrack the result before continuing
            res_chars -= new_chars
            res_len -= new_len
        return best
