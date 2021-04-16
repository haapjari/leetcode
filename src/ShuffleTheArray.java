import java.util.ArrayList;

/**
 * @author haapjari
 * @version 12.4.2021
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

    /**
     * Input: nums = [1,2,3,4,4,3,2,1], n = 4
     * Output: [1,4,2,3,3,2,4,1]
     */
    public static void main(String[] args) {
        int[] nums = {2, 5, 1, 3, 4, 7};
        int n = 3;

        shuffle(nums, n);
    }

    public static int[] shuffle(int[] nums, int n) {

        //  x1 x2  y1  y2  z1  z2
        // [2,  5,  1,  3,  4,  7]
        // n = 3
        // target is to order the array
        // x1, y1, x2, y2, x3, y3 ...

        //   x1  x2  x3  x4  y1  y2  y3   y4
        // [  1,  2,  3,  4,  4,  3,  2,  1]
        // n = 4
        // target is to order the array
        // x1, y1, x2, y2, x3, y3 ...
        // 1, 4, 2, 3, 3, 2, 4,  1

        // first split the array from n

        int[] firstHalf = new int[n];
        int[] secondHalf = new int[n];
        int[] returnArray = new int[n * 2];

        // firstHalf (the x's)

        for (int i = 0; i < firstHalf.length; i++) {
            firstHalf[i] = nums[i];
        }

        // thinking the secondHalf wrong way, maybe should start from n ?
        int secondHalfCounter = 0;
        for (int i = n; i < nums.length; i++) {
            secondHalf[secondHalfCounter] = nums[i];
            secondHalfCounter++;
        }

        // lets create the return array, by putting the values into arraylist, converting that to array and returning that
        ArrayList<Integer> returnListAsArrayList = new ArrayList<>();

        // adding first array
        int pairCounter = 0; // x's
        int oddCounter = 1; // y's
        for (int i = 0; i < nums.length / 2; i++) {

            // making sure that array wont nullpoint
            if (i + 1 < nums.length) {
                returnListAsArrayList.add(firstHalf[i]);
                returnListAsArrayList.add(secondHalf[i]);
            }
        }

        for (int i = 0; i < returnListAsArrayList.size(); i++) {
            returnArray[i] = returnListAsArrayList.get(i);
        }

        // print returnArray
        for (int i = 0; i < returnArray.length; i++) {
            System.out.println(returnArray[i]);
        }

        return returnArray;
    }
}
