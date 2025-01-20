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
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val;  // Min-heap: prioritize smaller values
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Priority queue to store nodes, ordered by their value
        priority_queue<ListNode*, vector<ListNode*>, Compare> minHeap;

        // Push the head of each list into the priority queue
        for (ListNode* list : lists) {
            if (list) {
                minHeap.push(list);
            }
        }

        // Create a dummy node to simplify the result list construction
        ListNode* dummy = new ListNode(-1);
        ListNode* current = dummy;

        // Process the heap until it's empty
        while (!minHeap.empty()) {
            // Get the smallest node from the heap
            ListNode* node = minHeap.top();
            minHeap.pop();

            // Add it to the result list
            current->next = node;
            current = current->next;

            // If the node has a next node, push it into the heap
            if (node->next) {
                minHeap.push(node->next);
            }
        }

        // Return the merged list starting from the next node of dummy
        return dummy->next;
    }
};
