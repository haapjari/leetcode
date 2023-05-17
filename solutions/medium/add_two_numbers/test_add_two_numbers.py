import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Two Empty Strings to hold the LinkedList (l1, l2 respectively) values.
        l1_str, l2_str = "", ""

        # Traverse through linked list.
        while l1:
            # Construct a string, append the nodes value to the beginning of the string.
            # "1" + "23" = "123".
            l1_str = str(l1.val) + l1_str
            l1 = l1.next

        while l2:
            l2_str = str(l2.val) + l2_str
            l2 = l2.next

        # Check if the strings are empty, in this case the value is not actually empty
        # but is 0, so this has to be 0.
        if not l1_str: l1_str = "0"
        if not l2_str: l2_str = "0"

        sum_of_values = int(l1_str) + int(l2_str)

        # Create an empty node for the head of resulting list.
        head = ListNode()
        current = head

        # Loop the characters in reverse order.
        for value in reversed(str(sum_of_values)):
            current.next = ListNode(int(value))
            current = current.next

        # Return the List from next to the Head, since Head is empty.
        return head.next


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
        self.assertEqual([8,9,9,9,0,0,0,1], result)


if __name__ == '__main__':
    unittest.main()
