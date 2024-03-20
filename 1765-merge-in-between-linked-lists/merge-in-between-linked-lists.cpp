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

    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* head= list1;
        ListNode* cur= list1;
        for(int i=1;i<a;i++){
            cur = cur->next;
        }
        ListNode* x = cur;
        cur = cur->next;
        for(int i=a-1 ; i<b;i++){
            ListNode* t = cur;
            cur = cur->next;
            delete t;
        }
        x->next = list2;
        ListNode* last = list2;
        cout<<cur->val;
        while(last->next != NULL){ last = last->next;}
        last->next = cur;
        return head;


    }
};