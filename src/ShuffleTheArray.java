/**
 * @author haapjari
 * @version 12e.4.2021
 * https://leetcode.com/problems/shuffle-the-array/
 */
public class ShuffleTheArray {

    /**
     * Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
     *
     * Return the array in the form [x1,y1,x2,y2,...,xn,yn].
     * @param args
     */

    /**
     * Input: nums = [2,5,1,3,4,7], n = 3
     * Output: [2,3,5,4,1,7]
     * Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
     */
    public static void main(String[] args) {
        int[] nums = {2, 5, 1, 3, 4, 7};
        int n = 3;

        shuffle(nums, n);
    }

    public static int[] shuffle(int[] nums, int n) {

        //  x1 x2  y1  y2  z1  z2
        // [2,  5,  1,  3,  4,  7]

        // target is to order the array
        // x1, y1, x2, y2, x3, y3 ...

        return nums;
    }
}
