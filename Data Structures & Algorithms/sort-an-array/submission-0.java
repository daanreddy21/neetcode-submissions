class Solution {
    public int[] sortArray(int[] nums) {
        int n = nums.length;
        for (int i=0; i<n-1;i++){
            int minin = i;
            for(int j=i+1; j<n;j++){
                if(nums[j]<nums[minin]){
                    minin=j;
                }
            }
            int temp = nums[i];
            nums[i]=nums[minin];
            nums[minin]=temp;
        }
        return nums;

        
    }
}