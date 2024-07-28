def sum_of_subset(numbers, target):
    def backtrack(index, current_sum, subset, result):
        if current_sum == target:
            result.append(subset[:])
        if current_sum > target or index >= len(numbers):
            return

        subset.append(numbers[index])
        backtrack(index + 1, current_sum + numbers[index], subset, result)
        subset.pop()
        backtrack(index + 1, current_sum, subset, result)        

    result = []
    backtrack(0, 0, [], result)
    return result

numbers = [2, 4, 7, 3, 9]
target = 9
subsets = sum_of_subset(numbers, target)
ans = []

if len(subsets) > 0:
    print("Subsets found:")
    for subset in subsets:
        if subset not in ans:
            ans.append(subset)
    for subset in ans[:len(ans) - 1]:
        print(subset)


 