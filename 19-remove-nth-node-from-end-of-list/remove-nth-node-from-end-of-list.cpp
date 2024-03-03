/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* a= head;
        ListNode* b= head;
        for(int i=0;i<n;i++){
            b= b->next;
        }
        if(b == NULL){
            ListNode* z= head->next;
            delete(head);
            return z;
        }

        while(b && b->next){
            a = a->next;
            b = b->next;
        }

        ListNode* t = a->next;
        
        a->next = a->next->next;
        delete(t);

        return head;
    }
};