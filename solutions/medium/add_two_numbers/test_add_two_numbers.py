import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_str, l2_str = "", ""

        # Read the Values to Strings
        while l1 and l2:
            l1_str += str(l1.val)
            l2_str += str(l2.val)
            l1 = l1.next
            l2 = l2.next

        # Reverse Strings, Convert to Int, Add Together, Convert Result to String and Reverse
        l3 = str(int(l1_str[::-1]) + int(l2_str[::-1]))[::-1]

        # Create Head (Empty Node) and Current Variable
        # which points to the Empty Node.
        head = ListNode()
        curr = head

        # Loop through every character
        # Create node with desired attributes
        # Take the curr, mark the next field to point to the
        # new node, and curr pointer to the fresh node (head moves)
        for char in l3:
            node = ListNode(int(char))
            curr.next = node
            curr = curr.next

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
