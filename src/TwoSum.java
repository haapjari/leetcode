public class TwoSum {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }

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
