class MergeSort:
    def sort_primitive_ascendent(self, nums):
        buffer = [0] * len(nums)
        self.merge_sort(nums, 0, len(nums) - 1, buffer)
        return nums

    def sort_primitive_descendent(self, nums):
        buffer = [0] * len(nums)
        self.merge_sort(nums, 0, len(nums) - 1, buffer)
        return nums[::-1]

    def sort_models_ascendent(self, array, attribute):
        buffer = [0] * len(array)
        self.merge_sort(array, 0, len(array) - 1, buffer, attribute)
        return array

    def sort_models_descendent(self, array, attribute):
        buffer = [0] * len(array)
        self.merge_sort(array, 0, len(array) - 1, buffer, attribute)
        return array[::-1]

    def merge_sort(self, nums, start, last, buffer, attribute=None):
        if start < last:
            mid = (start + last) // 2
            self.merge_sort(nums, start, mid, buffer, attribute)
            self.merge_sort(nums, mid + 1, last, buffer, attribute)
            self.merge_two_array(nums, start, mid, last, buffer, attribute)

    def merge_two_array(self, nums, start, mid, last, buffer, attribute=None):
        left = start
        right = mid + 1
        i = left

        while left <= mid and right <= last:
            if attribute:
                if not hasattr(nums[left], attribute) or not hasattr(nums[right], attribute):
                    raise AttributeError(f"Attribute {attribute} not found in one of the objects.")
                if getattr(nums[left], attribute) <= getattr(nums[right], attribute):
                    buffer[i] = nums[left]
                    left += 1
                else:
                    buffer[i] = nums[right]
                    right += 1
            else:
                if nums[left] <= nums[right]:
                    buffer[i] = nums[left]
                    left += 1
                else:
                    buffer[i] = nums[right]
                    right += 1
            i += 1

        while left <= mid:
            buffer[i] = nums[left]
            left += 1
            i += 1

        while right <= last:
            buffer[i] = nums[right]
            right += 1
            i += 1

        for j in range(start, last + 1):
            nums[j] = buffer[j]