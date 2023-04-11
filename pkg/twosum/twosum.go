package twosum

func TwoSum(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				var nums []int
				nums = append(nums, i)
				nums = append(nums, j)
				return nums
			}
		}
	}

	return []int{}
}
