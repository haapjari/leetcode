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

        # create string of values per list
        # convert string to int per list
        # add
        # convert int to string
        # create new list
        # reverse -> create as many values as chars in string

        l1_str, l2_str = "", ""

        # This is the current Linked List
        while l1 and l2:
            l1_str += str(l1.val)
            l2_str += str(l2.val)
            l1 = l1.next
            l2 = l2.next

        print(l1_str)
        print(l2_str)

        return ListNode()


class TestSolution(unittest.TestCase):
    def test_addTwoNumbers_case_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))

        s = Solution()
        result_list = s.addTwoNumbers(l1, l2)

    #     result = []
    #     while result_list:
    #         result.append(result_list.val)
    #         result_list = result_list.next

    #     # assert that the result is correct
    #     self.assertEqual(result, [7, 0, 8])

    # def test_addTwoNumbers_case_2(self):
    #     l1 = ListNode(0)
    #     l2 = ListNode(0)

    #     s = Solution()
    #     result_list = s.addTwoNumbers(l1, l2)

    #     result = []
    #     while result_list:
    #         result.append(result_list.val)
    #         result_list = result_list.next

    #     # assert that the result is correct
    #     self.assertEqual(result, [0])

    # def test_addTwoNumbers_case_3(self):
    #     l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    #     l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    #     s = Solution()
    #     result_list = s.addTwoNumbers(l1, l2)

    #     result = []
    #     while result_list:
    #         result.append(result_list.val)
    #         result_list = result_list.next

    #     # assert that the result is correct
    #     self.assertEqual([8,9,9,9,0,0,0,1], result)


if __name__ == '__main__':
    unittest.main()
