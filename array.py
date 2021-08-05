from typing import List


class Solution:
    @staticmethod
    def single_number(nums: List[int]) -> int:
        my_dict = {}
        for number in nums:
            is_inside = my_dict.get(number)
            if is_inside is None:
                my_dict[number] = 1
            else:
                my_dict[number] += 1

        for number, qty in my_dict.items():
            if qty == 1:
                return number

    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        """
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        Do not return anything, modify nums in-place instead.
        """
        for step in range(1, k+1):
            number = nums.pop()
            nums.insert(0, number)

        print(nums)

    @staticmethod
    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        """Given two integer arrays nums1 and nums2, return an array of their intersection.
        Each element in the result must appear as many times as it shows in both arrays and
        you may return the result in any order.
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]

        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [4,9]
        Explanation: [9,4] is also accepted.
        """
        nums1.sort()
        nums2.sort()
        result = []
        if len(nums1)>len(nums2):
            short_list = nums2[:]
            long_list = nums1[:]
        else:
            short_list = nums1[:]
            long_list = nums2[:]
        for number in short_list:
            if number in long_list:
                result.append(number)
                long_list.remove(number)
        return result

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for num_index, num in enumerate(nums):
            second_number = target - num
            first_index = num_index

            if second_number in nums and second_number != num:
                second_index = nums.index(second_number)
                break
            else:
                second_number_indexes = [index for index, number in enumerate(nums) if number == second_number]
                if len(second_number_indexes) > 1:
                    second_index = second_number_indexes[-1]
                    break
                else:
                    continue

        result = [first_index, second_index]
        return result

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        pass

print(Solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
