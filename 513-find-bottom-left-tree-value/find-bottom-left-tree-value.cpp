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
    
    int findBottomLeftValue(TreeNode* root) {
        if(!root) return 0;
        queue<TreeNode*> visit;
        visit.push(root);
        int node=0;
        while(!visit.empty()){
            TreeNode* t = visit.front();
            visit.pop();
            node = t->val;
            
            
            
            if( t -> right != NULL ) visit.push(t->right); 
            if( t -> left != NULL ) visit.push(t->left);
            
            
            

        }
        return node;
    }
};