//Algorithm
//
//        Define a function called findBound which takes three arguments: the array, the target to search for, and a boolean value isFirst which indicates if we are trying to find the first or the last occurrence of target.
//        We use 2 variables to keep track of the subarray that we are scanning. Let's call them begin and end. Initially, begin is set to 0 and end is set to the last index of the array.
//        We iterate until begin is greater than or equal to end.
//        At each step, we calculate the middle element mid = (begin + end) / 2. We use the value of the middle element to decide which half of the array we need to search.
//        nums[mid] == target
//        isFirst is true ~ This implies that we are trying to find the first occurrence of the element. If mid == begin or nums[mid - 1] != target, then we return mid as the first occurrence of the target. Otherwise, we update end = mid - 1
//        isFirst is false ~ This implies we are trying to find the last occurrence of the element. If mid == end or nums[mid + 1] != target, then we return mid as the last occurrence of the target. Otherwise, we update begin = mid + 1
//        nums[mid] > target ~ We update end = mid - 1 since we must discard the right side of the array as the middle element is greater than target.
//        nums[mid] < target ~ We update begin = mid + 1 since we must discard the left side of the array as the middle element is less than target.
//        We return a value of -1 at the end of our function which indicates that target was not found in the array.
//        In the main searchRange function, we first call findBound with isFirst set to true. If this value is -1, we can simply return [-1, -1]. Otherwise, we call findBound with isFirst set to false to get the last occurrence and then return the result.

class Solution {
    private int findBound(int[] nums, int target, boolean isFirst) {
        int begin = 0;
        int end = nums.length -1;


        while (begin <= end) {
            int mid = (begin + end) / 2;
            if (nums[mid] == target) {
                if (isFirst) {
                    if (mid == begin || nums[mid - 1] < target) {
                        return mid;
                    }
                    end = mid -1;
                } else {
                    if (mid == end || nums[mid + 1] > target) {
                        return mid;
                    }
                    begin = mid + 1;
                }
            } else if (nums[mid] > target) {
                end = mid - 1;
            } else {
                begin = mid + 1;
            }
        }
        return -1;
    }
    public int[] searchRange(int[] nums, int target) {
        int first = findBound(nums, target, true);
        if (first == -1)
            return new int[]{-1, -1};
        int last = findBound(nums, target, false);
        return new int[]{first, last};
    }
}