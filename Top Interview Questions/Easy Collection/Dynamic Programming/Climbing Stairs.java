public class Solution {
    public int climbStairs(int n) {
        int[] array = new int[46];
        array[0] = 0;
        array[1] = 1;
        array[2] = 2;

        if (n < 3)
            return array[n];

        int i = 3;
        while (i <= n) {
            array[i] = array[i - 1] + array[i - 2];
            i++;
        }

        return array[n];
    }

    public int climbStairs2(int n) {
        int[] memo = new int[n + 1];
        return climb_Stairs(0, n, memo);
    }
    public int climb_Stairs(int i, int n, int[] memo) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        if (memo[i] > 0) {
            return memo[i];
        }
        memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo);
        return memo[i];
    }
}
