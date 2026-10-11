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
private:
    ListNode* merge(ListNode* a, ListNode* b) {
        ListNode ans(0);
        ListNode* cur = &ans;

        while (a && b) {
            if (a->val <= b->val) {
                cur->next = a;
                a = a->next;
            } else {
                cur->next = b;
                b = b->next;
            }
            cur = cur->next;
        }
        if (a) {
            cur->next = a;
        } else {
            cur->next = b;
        }
        return ans.next;
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) {
            return {};
        }

        for (int gap = 1; gap < lists.size(); gap *= 2) {
            for (int i = 0; i + gap < lists.size(); i += gap * 2) {
                lists[i] = merge(lists[i], lists[i + gap]);
            }
        }

        return lists[0];
    }
};
