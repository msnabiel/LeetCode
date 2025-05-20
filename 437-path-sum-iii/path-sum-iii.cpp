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
#include <unordered_map>

class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long, int> prefixSumCount;
        prefixSumCount[0] = 1; // Base case: a path that starts at the root
        return dfs(root, 0, targetSum, prefixSumCount);
    }

private:
    int dfs(TreeNode* node, long long currSum, int target, unordered_map<long long, int>& prefixSumCount) {
        if (!node) return 0;

        currSum += node->val;
        int numPathsToCurr = prefixSumCount[currSum - target];

        prefixSumCount[currSum]++;
        int count = numPathsToCurr
                    + dfs(node->left, currSum, target, prefixSumCount)
                    + dfs(node->right, currSum, target, prefixSumCount);
        prefixSumCount[currSum]--; // backtrack

        return count;
    }
};
