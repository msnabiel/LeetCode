/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int longestZigZag(TreeNode* root) {
        if(!root->right && !root->left)
            return 0;
        return solve(root, 0, false);
    }
    int solve(TreeNode* root, int length, bool shouldGoLeft) {
        if(!root)
            return length;

        int left = 0;
        int right = 0;
        int tmp = 0;

        if(shouldGoLeft && !root->left) {
            tmp = length;
            length = 0;
        } else if(!shouldGoLeft && !root->right) {
            tmp = length;
            length = 0;
        }

        right = solve(root->right, shouldGoLeft ? 1: length + 1, true);
        left = solve(root->left, shouldGoLeft ? length + 1 : 1, false);

        return std::max({left, right, tmp});
    }
};