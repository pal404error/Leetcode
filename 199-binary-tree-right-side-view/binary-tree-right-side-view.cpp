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
    void ans(TreeNode* root, vector<int>& a , int lvl){
        if(!root) return ;
        if(lvl == a.size()) a.push_back(root->val);

        ans( root->right, a, lvl+1);
        ans( root->left , a, lvl+1);
    }
    vector<int> rightSideView(TreeNode* root) {
        int level=0;
        vector<int> a;
        ans(root, a, 0);
        return a;
    }
};