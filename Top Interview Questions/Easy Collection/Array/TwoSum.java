class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = {0,0};

        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    result = new int[] {i,j};
                }
            }
        }

        return result;
    }

    public int[] twoSumHash(int[] nums, int target) {
        int[] result = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (map.get(complement) != null && map.get(complement) != i) {
                result[0] = i;
                result[1] = map.get(complement);
                break;
            }
            map.put(nums[i], i);
        }

        return result;
    }
}