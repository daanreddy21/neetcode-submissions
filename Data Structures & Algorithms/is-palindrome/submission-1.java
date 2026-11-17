class Solution {
    public boolean isPalindrome(String s) {
        String s2 = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int left = 0;
        int right = s2.length() - 1;
        while (left < right) {
            if (s2.charAt(left) != s2.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
