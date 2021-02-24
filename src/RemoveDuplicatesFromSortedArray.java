public class RemoveDuplicatesFromSortedArray {

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }

    public int removeDuplicates(int[] nums) {

        int n = nums.length;
        if(n == 0 || n == 1) return n;
        int i = 0;
        int j = 1;
        while(j < n) {
            if(nums[i] == nums[j]) j++;
            else nums[++i] = nums[j++];
        }
        return i+1;
    }
}