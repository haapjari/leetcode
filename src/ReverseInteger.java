/**
 * @author haapjari
 * @version 24.2.2021
 * LeetCode Challenge: Reverse Integer (https://leetcode.com/problems/reverse-integer/)
 */
public class ReverseInteger {

    /**
     * @param args not used
     */
    public static void main(String[] args) {
        System.out.println("Hello World");
    }

    /**
     * Given parameter as a signed 32-bit integer, return the integer with digits reversed.
     * If the value goes outside of the integer range [-2**31, 2**31 - 1] then return 0.
     * @param x Signed 32-bit Integer Value to be reversed.
     * @return Reversed value of 32-bit Integer, or if out of range - 0.
     * Source: https://leetcode.com/problems/reverse-integer/solution/
     */
    public static int reverse(int x) {

        int rev = 0;

        while (x != 0) {

            int pop = x % 10;
            x /= 10;

            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7))
                return 0;

            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8))
                return 0;

            rev = rev * 10 + pop;
        }
        return rev;
    }
}
