��������dp�=�[defaultdict(int)�for�_�in�range(len(nums))]
��������res�=�0
��������for�i�in�range(len(nums)):
������������for�j�in�range(i):
����������������
����������������#�We�are�looking�for�the�number�of�elements�before�j�in�the�arithmetic�
subsequence�that�has�nums[j]-nums[i]�as�difference.
����������������dif�=�nums[j]-nums[i]

����������������#�Simply�add�it�to�the�result.
����������������res�+=�dp[j][dif]

����������������#�Increase�the�number�of�elements�in�arithmetic�subsequence�at�i�with�this�dif.
with�```j```
class�Solution:
����def�numberOfArithmeticSlices(self,�nums:�List[int])�->�int:
��������#�use�defaultdict(int)�to�easily�get�the�difference�in�arithmetic�subsequences�ending�
