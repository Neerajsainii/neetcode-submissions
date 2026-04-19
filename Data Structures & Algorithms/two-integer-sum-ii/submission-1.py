class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers) - 1
        while(first<second):
            # print("f,s",first,second)
            if target > (numbers[first] + numbers[second]):
                first += 1
            elif target < (numbers[first] + numbers[second]):
                second -= 1
            else:
                return [first+1,second+1]
        return []