2
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children: return -1
        money -= children
        cnt, restMoney = divmod(money, 7)
        if cnt == children and restMoney == 0:
            return children
        return min(cnt, children - 1)
        if cnt == children - 1 and restMoney == 3:
            return children - 2
