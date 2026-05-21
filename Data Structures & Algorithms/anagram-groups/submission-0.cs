public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string,List<string>> d = new();
        foreach(var s in strs) {
            var k = String.Concat(s.OrderBy(c => c));
            if (d.TryGetValue(k, out var value)) {
                value.Add(s);
            }
            else {
                d[k] = [s];
            }
        }
        return d.Values.ToList();
    }
}
