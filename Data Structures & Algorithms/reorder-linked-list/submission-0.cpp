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
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        // traverse until slow is at n/2 node and fast at end
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse the second list
        ListNode* second = slow->next;
        ListNode* prev = slow->next = nullptr;
        while (second) {
            ListNode* tmp = second->next;
            second->next = prev;
            prev = second;
            second = tmp;
        }

        // merge the two lists
        ListNode* first = head;
        second = prev;
        while (second) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;
            first->next = second;
            second->next = tmp1;
            first = tmp1;
            second = tmp2;
        }

    }
};