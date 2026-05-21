public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> s = new();
        foreach(var n in nums) {
            if (s.Contains(n)) return true;
            s.Add(n);
        }
        return false;
    }
}