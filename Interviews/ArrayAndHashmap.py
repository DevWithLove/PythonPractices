

nums = [1,2,3,4]

def get_nums(arr): 
   result = []
   for i in range(len(arr)):
      total = 1
      for j in range(len(arr)):
         if i != j:
            total *= arr[j]

      result.append(total)
   return result

def get_nums2(arr):
    n = len(arr)
    result = [1] * n

    # 左边乘积
    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]

    # 右边乘积
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= arr[i]

    return result

print(get_nums2(nums))
