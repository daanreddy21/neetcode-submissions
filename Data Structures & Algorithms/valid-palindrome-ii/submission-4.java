
class Solution {
    public boolean validPalindrome(String s) {
        String s2 = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int left = 0;
        int right = s2.length() - 1;
        while (left < right) {
            if (s2.charAt(left) != s2.charAt(right)) {
                return check(s2, left + 1, right) ||
                       check(s2, left, right - 1);
            }
            left++;
            right--;
        }
        return true;
    }
    public boolean check(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
