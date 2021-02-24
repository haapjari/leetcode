import java.util.Map;
import java.util.HashMap;

/**
 * @author haapjari
 * @version 24.2.2021
 * LeetCode Challenge: Roman to Integer (https://leetcode.com/problems/roman-to-integer/)
 */
public class RomanToInteger {

    /**
     * @param args not used
     */
    public static void main(String[] args) {
        String s = "III";
        String s2 = "IV";

        System.out.println(romanToInt(s2));
    }

    /**
     * Given string, convert string from Roman Numbers to Decimal Numbers.
     * @param s Parameter string to be converted to Decimal Numbers.
     * @return Input string converted as Decimal.
     * Source: https://leetcode.com/problems/roman-to-integer/discuss/589035/My-Java-Solution
     */
    public static int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>();

        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);

        char [] str = s.toCharArray();

        int decimal = 0;
        int roman = 0;

        for ( int i = str.length - 1; i >= 0; i--) {

            if ( map.get(str[i]) < roman ) {
                decimal -= map.get(str[i]);
            } else {
                decimal += map.get(str[i]);
            }
            roman = map.get(str[i]);
        }
        return decimal;
    }
}
