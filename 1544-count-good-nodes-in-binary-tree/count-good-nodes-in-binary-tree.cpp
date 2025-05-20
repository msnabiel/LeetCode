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
    int ans=0;
    void solve(TreeNode* root,int maxNodeSeen){
        if(!root) return;

        if(root->val>=maxNodeSeen){
            ans++;
            maxNodeSeen=root->val;
        }

        solve(root->left,maxNodeSeen);
        solve(root->right,maxNodeSeen);
    }
    int goodNodes(TreeNode* root) {
        if(!root) return 0;
        solve(root,root->val);
        return ans;
    }
};