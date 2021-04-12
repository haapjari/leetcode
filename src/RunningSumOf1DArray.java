/**
 * @author haapjari
 * @version 7.4.2021
 */
public class RunningSumOf1DArray {

    public static void main(String[] args) {

        int[] nums = {1, 2, 3, 4};
        runningSum(nums);
    }

    /**
     * Given an array, we define sum of an array as runningSum[i] = sum[nums[0] ... nums[i]
     * Return the running sum of sums.
     *
     * Example 1:
     *
     * Input: nums = [1, 2, 3, 4]
     * Output: [1, 3, 6, 10]
     * Explanation: Running sum is obtained as follows [1, 1+2, 1+2+3, 1+2+3+4]
     *
     * @param nums
     * @return
     */
    public static int[] runningSum(int[] nums) {
        int[] result = new int[nums.length];

        // Initialize first element of result array with first element in nums.
        result[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            // Result at index `i` is sum of result at `i-1` and element at `i`.
            result[i] = result[i - 1] + nums[i]; // aina edellinen ja summataan nykyinen.
        }
        return result;
    }

}
