/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* current = head;  // Pointer to traverse the list

    while (current != NULL && current->next != NULL) {
        if (current->val == current->next->val) {
            // Remove duplicate by skipping the next node
            struct ListNode* temp = current->next;
            current->next = current->next->next;
            free(temp);
        } else {
            // Move to the next unique node
            current = current->next;
        }
    }
    return head; // Return modified list
}