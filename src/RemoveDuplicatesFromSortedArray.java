/**
 * @author haapjari
 * @version 24.2.2021
 * LeetCode Challenge: Remove Duplicates from Array (https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
 */
public class RemoveDuplicatesFromSortedArray {

    /**
     * @param args not used
     */
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }

    /**
     * Given Array, method removes duplicate values.
     * @param nums Array with possible duplicate values.
     * @return Modified array without duplicate values.
     */
    public int removeDuplicates(int[] nums) {

        int n = nums.length;

        if (n == 0 || n == 1)
            return n;

        int i = 0;
        int j = 1;

        while (j < n) {
            if (nums[i] == nums[j])
                j++;
            else
                nums[++i] = nums[j++];
        }

        return i + 1;
    }
}