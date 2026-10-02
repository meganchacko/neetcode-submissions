
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # [0,1,2,3]
        previous = None
        current = head
        while current:
            next_node = current.next   # save before we overwrite
            #print(f"next_node is : {next_node.val}")
            current.next = previous    # reverse the pointer
            if current.next != None:
                print(f"current.next is : {current.next.val}")
            previous = current         # move previous forward
            #print(f"previous is : {previous.val}")
            current = next_node        # move current forward
            #print(f"current is : {current.val}")

        return previous


            