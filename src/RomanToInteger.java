public class RomanToInteger {

     /*
            Given a roman numeral, convert it to an integer.
            I can be placed before V (5) and (X) (10) to make 4 and 9.
            X can be placed before L (50) and (100) to make 40 and 90.
            C can be placed before D (500) and M (1000) to make 400 and 900.

     */

    public static void main(String[] args) {
        String s = "III";
        String s2 = "IV";

        System.out.println(romanToInt(s2));
    }

    public static int romanToInt(String s) {
        int[] map = new int[256];

        map['I'] = 1;
        map['V'] = 5;
        map['X'] = 10;
        map['L'] = 50;
        map['C'] = 100;
        map['D'] = 500;
        map['M'] = 1000;

        int ret = 0, pre = 1;

        for (int i = s.length()-1; i >= 0; --i) {

            int cur = map[s.charAt(i)];
            if (cur < pre) ret -= cur;

            else {
                pre = cur;
                ret += cur;
            }
        }

        return ret;
    }
}
