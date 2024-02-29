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
    bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int level=0;
        while(!q.empty()){
            int size = q.size();
            vector<int> node;
            for(int i=0;i<size;i++){
                TreeNode* t = q.front();
                q.pop();
                if( (level %2 == 0 && t->val % 2 == 0 )||
                (level %2 != 0 && t->val % 2 != 0 ) ) return false;
                node.push_back(t->val);
                if(t->left!= NULL) q.push(t->left);
                if(t->right!= NULL) q.push(t->right);
            }
            if(level%2 == 0) {
                for(int i=0;i <node.size()-1; i++){
                    if(node[i] >= node[i+1]){
                        return false;
                    }
                }
            }
            if(level%2 != 0){
                for(int i=0;i <node.size()-1; i++){
                    if(node[i] <= node[i+1]){
                        return false;
                    }
                }
            }
            level++;
            
        }
        return true;

    }
};