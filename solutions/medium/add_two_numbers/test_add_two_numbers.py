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

        l3: ListNode
        temp_node = ListNode()
        curr_node = temp_node
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val

            if carry != 0:
                sum = sum + carry
                carry = 0

            if not 0 <= sum <= 9:
                carry = sum - 9
                # this is not correct and works on only cases, where
                # the sum is 10.
                # sum has to be the the last digit of the actual sum.
                # i think also there is tens case, which has to be handled
                sum = 0

            new = ListNode(sum)
            curr_node.next = new
            curr_node = new

            l1 = l1.next
            l2 = l2.next

        temp_node = temp_node.next

        return temp_node

        # This is the current Linked List
        # while temp_node:
        #     print(temp_node.val)
        #     temp_node = temp_node.next


class TestSolution(unittest.TestCase):
    def test_addTwoNumbers_case_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))

        s = Solution()
        result_list = s.addTwoNumbers(l1, l2)

        result = []
        while result_list:
            result.append(result_list.val)
            result_list = result_list.next

        # assert that the result is correct
        self.assertEqual(result, [7, 0, 8])

    def test_addTwoNumbers_case_2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)

        s = Solution()
        result_list = s.addTwoNumbers(l1, l2)

        result = []
        while result_list:
            result.append(result_list.val)
            result_list = result_list.next

        # assert that the result is correct
        self.assertEqual(result, [0])

    def test_addTwoNumbers_case_3(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

        s = Solution()
        result_list = s.addTwoNumbers(l1, l2)

        result = []
        while result_list:
            result.append(result_list.val)
            result_list = result_list.next

        # assert that the result is correct
        self.assertEqual(result, [8,9,9,9,0,0,0,1])


if __name__ == '__main__':
    unittest.main()
