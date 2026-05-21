public class Solution {
    public bool IsAnagram(string s, string t) {
        var ss = String.Concat(s.OrderBy(c => c));
        var tt = String.Concat(t.OrderBy(c => c));
        return ss == tt;
    }
}
