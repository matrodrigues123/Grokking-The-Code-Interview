def max_sub_array_of_size_k(k, arr):
    maxSum = 0
    windowSum, windowStart = 0.0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1

    return maxSum


def main():
    result = max_sub_array_of_size_k(2, [2,3,4,1,5])
    print('Averages of subarrays of size K: ' + str(result))

main()