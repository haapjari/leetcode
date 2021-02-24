/**
 * @author haapjari
 * @version 24.2.2021
 * LeetCode Challenge: PalindromeNumber (https://leetcode.com/problems/palindrome-number/)
 */
public class PalindromeNumber {

    /**
     * @param args not used
     */
    public static void main(String[] args) {
        System.out.println("Hello World");
    }

    /**
     * Given Integer tests if that value is an palindrome.
     * @param x Integer to be tested.
     * @return Boolean value if input is palindrome or not.
     */
    public boolean isPalindrome(int x) {

        String inputAsString = Integer.toString(x);
        String inputAsReverse = "";

        for (int i = inputAsString.length() - 1; i >= 0; i-- ) {
            inputAsReverse = inputAsReverse + inputAsString.charAt(i);
        }

        if (inputAsString.equals(inputAsReverse)) {
            return true;
        } else {
            return false;
        }

    }
}
