// REF: https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
class Solution {
    public int maxSubArray(int[] nums) {
        int currentSubarray = nums[0];
        int maxSubarray = nums[0];

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            currentSubarray = Math.max(num, currentSubarray + num);
            maxSubarray = Math.max(maxSubarray, currentSubarray);
        }

        return maxSubarray;
    }
}