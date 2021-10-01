def isUnique(nums):
  seen = set()
  for n in nums:
    if n in seen:
      return False
    else:
      seen.add(n)
  return True

def noDataStructure(nums):
  for i in range(0,len(nums)-1):
    for j in range(i+1, len(nums)):
      if (nums[i] == nums[j]):
        return False
  return True

def main():
    isUnique([1,2,3,4,1])
    noDataStructure([1,2,3,4,1])

main()
