# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # while the value of list1.val < list2.val , append to new list ?? we know they are both sorted... ! 


        new_list = ListNode()
        new_head = new_list
        # list1=[1,2,4]
        # list2=[1,3,5]
        while list1 and list2: 
            if list1.val < list2.val:
                print(f"list1.val : {list1.val}")
                new_list.next = list1
                new_list = new_list.next
                #print(f"list1.val < list2.val: {new_list.next.val}")
                list1 = list1.next
            elif list2.val < list1.val:
                print(f"list2.val : {list2.val}")
                new_list.next = list2
                new_list = new_list.next
                print(f"lst2.val < list1.val: {new_list.val}")
                list2 = list2.next
            elif list1.val == list2.val:
                print(f"final elif list1: {list1.val} and list 2: {list2.val}")
                new_list.next = list1
                new_list = new_list.next
                list1 = list1.next

        # cases that make a list not meet the while condition:
        # 1. list1 is None (reached end first)
        # 2. list2 is None (reached end first)
        # 3. list1 and list2 are None (both reached end at same time)

        if list1 is None and list2 is None:
            return new_head.next
        elif list2 is None:
            while list1:
                new_list.next = list1
                new_list = new_list.next
                list1 = list1.next
        elif list1 is None:
            while list2:
                new_list.next = list2
                new_list = new_list.next
                list2 = list2.next

        
        return new_head.next
        
                



