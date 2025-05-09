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
    int pairSum(ListNode* head) {
        vector<int> values;
        
        // Step 1: Store all node values in an array
        while (head) {
            values.push_back(head->val);
            head = head->next;
        }
        
        int maxSum = 0;
        int n = values.size();
        
        // Step 2: Calculate twin sums and find the maximum
        for (int i = 0; i < n / 2; ++i) {
            int twinSum = values[i] + values[n - i - 1];
            maxSum = max(maxSum, twinSum);
        }
        
        return maxSum; // Step 3: Return the maximum twin sum
    }
};