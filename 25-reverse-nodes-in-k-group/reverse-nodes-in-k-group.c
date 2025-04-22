/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *
helper(struct ListNode **head, int k, struct ListNode **last)
{
    *last = *head;
    struct ListNode *prev = NULL;
    for (; k; k--)
    {
        struct ListNode *ff = (*head)->next;
        (*head)->next = prev;
        prev = *head;
        *head = ff;
    }
    return prev;
}

struct ListNode *
reverseKGroup(struct ListNode *head, int k)
{
    // Get the length of ListNode
    int i = 0;
    for (struct ListNode *n=head; n; i++) n = n->next;
    i /= k;

    struct ListNode res = { 0, NULL }, *last = &res;
    for (; i; i--) last->next = helper(&head, k, &last);

    // Link to remaining node
    last->next = head;
    return res.next;
}