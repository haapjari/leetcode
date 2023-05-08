import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
            You are given two non-empty linked lists representing two non-negative
            integers. Digits are stored in reverse order, and each of their nodes contains
            single digit. Add the two numbers and return the sum as linked list.

            If the sum is more than 10, result will overflow
        """

        # Traverse through Linked List
        curr = l1
        while curr:
            print(curr.val)
            curr = curr.next

        pass


class TestSolution(unittest.TestCase):
    def test_addTwoNumbers(self):
        # create example lists

        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))

        # calculate sum of two lists
        s = Solution()
        result_list = s.addTwoNumbers(l1, l2)

        # convert result list to Python list
        # result = []
        # while result_list:
        #     result.append(result_list.val)
        #     result_list = result_list.next

        # # assert that the result is correct
        # self.assertEqual(result, [7, 0, 8])


if __name__ == '__main__':
    unittest.main()
