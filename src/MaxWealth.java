/**
 * @author haapjari
 * @version 13.4.2021
 */
public class MaxWealth {

    /**
     * Input: accounts = [[1,2,3],[3,2,1]]
     * Output: 6
     * Explanation:
     * 1st customer has wealth = 1 + 2 + 3 = 6
     * 2nd customer has wealth = 3 + 2 + 1 = 6
     * Both customers are considered the richest with a wealth of 6 each, so return 6.
     */

    /**
     * Input: accounts = [[1,5],[7,3],[3,5]]
     * Output: 10
     * Explanation:
     * 1st customer has wealth = 6
     * 2nd customer has wealth = 10
     * 3rd customer has wealth = 8
     * The 2nd customer is the richest with a wealth of 10.
     */

    public static void main(String[] args) {
        System.out.println("Hello World");
        int[][] accounts = {{1, 2, 3}, {3, 2, 1}};
        maximumWealth(accounts);
    }

    public static int maximumWealth(int[][] accounts) {

        // first calculate sum of all values inside arrays, that are element of the first array
        // then compare the sums
        // return biggest sum

        int temp = 0;
        int biggestSum = 0;

        for (int i = 0; i < accounts.length; i++) {
            for (int j = 0; j < accounts[i].length; j++) {

                for (int z = 0; z < accounts[i].length; z++) {
                    temp += accounts[i][z];
                }

                if (temp > biggestSum) {
                    biggestSum = temp;
                    temp = 0;
                } else {
                    temp = 0;
                }
            }
        }

        return biggestSum;
    }
}
