    function twoSum($nums, $target) {
        $seen = [];
        foreach($nums as $id=>$value) {
            $pairValue = $target - $value;
            if (array_key_exists($pairValue, $seen)) {
                return [$id, $seen[$pairValue]];
            }
            $seen[$value] = $id;
        }
        return [];
class Solution {
    }
}
[
