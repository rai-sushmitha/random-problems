#https://leetcode.com/problems/add-two-numbers/?envType=company&envId=google&favoriteSlug=google-thirty-days
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0

        temp1 = l1
        temp2 = l2

        head = None
        tail = None

        while(temp1 is not None or  temp2 is not None or rem > 0):

            val1 = temp1.val if temp1 is not None else 0
            val2 = temp2.val if temp2 is not None else 0

            val = val1 + val2 + rem

            rem = val//10
            newNode = ListNode( val%10)
            if(head == None):
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
            if temp1 is not None:
                temp1 = temp1.next
            if temp2 is not None:
                temp2 = temp2.next

        return head
