/**
 * @author haapjari
 * @version 24.2.2021
 * LeetCode Challenge: Two Sum (https://leetcode.com/problems/two-sum/)
 */
public class TwoSum {

    /**
     * @param args not used
     */
    public static void main(String[] args) {
        System.out.println("Hello World");
    }

    /**
     * Given array and target value, find two values from array that adds up to target
     * and return their indices.
     * @param nums Array, which will be tested.
     * @param target Target value which will be searched from Array.
     * @return Indices from original Array, which contains values that add up to target.
     */
    public int[] twoSum(int[] nums, int target) {

        for (int i = 0; i < nums.length; i++) {

            int sum = 0;
            int[] sumIndices = {0, 0};

            for (int j = 0; j < nums.length; j++) {

                if (i != j) {
                    int checkSum = nums[i] + nums[j];

                    if (checkSum == target) {

                        sumIndices[0] = i;
                        sumIndices[1] = j;

                        return sumIndices;
                    }
                }
            }

        }

        return null;
    }
}
