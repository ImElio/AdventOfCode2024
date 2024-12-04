def count_combinations(nums, target):
    nums.sort()
    memo = {}
    def dfs(index, total):
        key = (index, total)
        if key in memo:
            return memo[key]
        if total == target:
            return 1
        if total > target or index == len(nums):
            return 0
        count = dfs(index + 1, total + nums[index]) + dfs(index + 1, total)
        memo[key] = count
        return count
    return dfs(0, 0)

# Esempio di utilizzo:
if __name__ == "__main__":
    nums = [2, 3, 5]
    target = 8
    result = count_combinations(nums, target)
    print("Numero di combinazioni:", result)
