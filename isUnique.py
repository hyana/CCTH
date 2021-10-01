def isUnique(nums):
  seen = set()
  for n in nums:
    if n in seen:
      return False
    else:
      seen.add(n)
  return True

def main():
    isUnique([1,2,3,4,1])

main()
