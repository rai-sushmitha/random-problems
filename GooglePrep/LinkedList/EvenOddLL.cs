https://leetcode.com/problems/odd-even-linked-list/description/

public class Solution {
    public ListNode OddEvenList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }

        ListNode evenStart = null;
        ListNode evenEnd = null;
        ListNode oddStart = null;
        ListNode oddEnd = null;

        int i = 1;
        ListNode temp = head;
        while(temp != null){
            if(i%2 == 0){
                if(evenStart == null) evenStart = temp; 
                else evenEnd.next = temp;

                evenEnd = temp;
            } else {
                if(oddStart == null) oddStart = temp;
                else oddEnd.next = temp;

                oddEnd = temp;
            }

            temp = temp.next;
            i=i+1;
        }

        oddEnd.next = evenStart;
        evenEnd.next = null;
        return oddStart;
    }
}
