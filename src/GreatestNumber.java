import java.util.ArrayList;
import java.util.List;

/**
 * @author haapjari
 * @version
 * https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
 */
public class GreatestNumber {

    /**
     * Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
     *
     * For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them.
     * Notice that multiple kids can have the greatest number of candies.
     */

    /**
     * Input: candies = [2,3,5,1,3], extraCandies = 3
     * Output: [true,true,true,false,true]
     * Explanation:
     * Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids.
     * Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.
     * Kid 3 has 5 candies and this is already the greatest number of candies among the kids.
     * Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies.
     * Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.
     */

    /**
     * Input: candies = [4,2,1,1,2], extraCandies = 1
     * Output: [true,false,false,false,false]
     * Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.
     */

    public static void main(String[] args) {
        System.out.println("Hello World");

        int[] candies = {4, 2, 1, 1, 2};
        int extraCandies = 1;
        kidsWithCandies(candies, extraCandies);
    }

    public static List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List list = new ArrayList();

        // 1: Find the kid / kid's who has the greatest number of candies.

        int candyKing = 0;
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] >= candyKing) {
                candyKing = candies[i];
            }
        }

        // 2: Then compare is there any other kid that could be the candy king.
        // If YES, then save the boolean to list.
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= candyKing) {
                list.add(true);
            } else {
                list.add(false);
            }
        }

        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }

        return list;
    }
}
