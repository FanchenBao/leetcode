#include <iostream>
#include <queue>

using namespace std;


// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};


class NodeLvl {
public:
    Node* node;
    int lvl;
    
    NodeLvl(Node* _node, int _lvl): node(_node), lvl(_lvl) {}
};


/*
For the next four days, I will use C++ as a preparation for the debugging task
in the first round of Rosie's Amazon interview.
*/
class Solution1 {
public:
    /*
    89% ranking.
    This solution is a naive BFS, with a helper data structure NodeLvl to record
    both the node and level. Using level, we can identify which nodes belong to
    the same level and link them together. This solution is NOT O(1) extra
    space.
    */
    Node* connect(Node* root) {
        if (root != NULL) {
            queue<NodeLvl> nq;
            nq.push(NodeLvl(root, 0));
            Node* dummy = new Node();
            NodeLvl pre = NodeLvl(dummy, 0);
            while (!nq.empty()) {
                NodeLvl cur = nq.front();
                nq.pop();
                if (pre.lvl == cur.lvl) {
                    pre.node->next = cur.node;
                }
                if (cur.node->left != NULL) {
                    nq.push(NodeLvl(cur.node->left, cur.lvl + 1));
                }
                if (cur.node->right != NULL) {
                    nq.push(NodeLvl(cur.node->right, cur.lvl + 1));
                }
                pre = cur;
            }
            // clean up
            dummy->next = NULL;
            delete dummy;
        }
        return root;
    }
};


class Solution2 {
public:
    /*
    48% ranking.
    This is O(1) solution.
    For each root, connect the most right nodes of the left branch and the most
    left nodes of the right branch.
    */
    Node* connect(Node* root) {
        if (root == NULL) {return root;}
        Node* lb = root->left;
        Node* rb = root->right;
        while (lb != NULL) {
            lb->next = rb;
            lb = lb->right;
            rb = rb->left;
        }
        connect(root->left);
        connect(root->right);
        return root;
    }
};
 
 
int main() {
    cout<<"life is lonly\n";
    return 0;
}