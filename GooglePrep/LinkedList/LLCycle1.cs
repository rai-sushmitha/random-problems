https://leetcode.com/problems/linked-list-cycle/description/

public class Solution {
    public bool HasCycle(ListNode head) {
        if(head == null) {
            return false;
        }
        HashSet<ListNode> val = new HashSet<ListNode>();

        ListNode temp = head;
        while(temp.next != null)
        {
            if(val.Contains(temp.next)){
                return true;
            }
            val.Add(temp.next);
            temp = temp.next;
        }

        return false;
        
    }
}
