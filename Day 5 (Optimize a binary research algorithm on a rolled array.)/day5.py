def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Left: {left}, Mid: {mid}, Right: {right}, Target: {target}")
        if nums[mid] == target:
            print(f"Found target at index {mid}")
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    print("Target not found")
    return -1

if __name__ == "__main__":
    print("Script avviato!")
    nums = [6, 7, 0, 1, 2, 4, 5]
    target = 4
    result = search_rotated_array(nums, target)
    print("Risultato:", result)
