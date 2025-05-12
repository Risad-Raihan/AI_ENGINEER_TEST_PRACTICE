def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
if __name__ == "__main__":
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(search(nums1, target1))  # Output: 4

    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(search(nums2, target2))  # Output: -1 