/**
 * @author haapjari
 * @version 26.2.2021
 */
public class LongestCommonPrefix {

    public static void main(String[] args) {

        String[] arr = {"flower","flow","flight"};
        System.out.println("Hello World");
        longestCommonPrefix(arr);
    }

    /**
     * Method takes array of string as parameter and returns longest common prefix among elements.
     * If not similar prefixes around - return empty String.
     * @param strs Array of strings, which elements which will be tested.
     */
    public static String longestCommonPrefix(String[] strs) {

        if (strs.length == 0) return "";
        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++)  {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }
        return prefix;
    }
}