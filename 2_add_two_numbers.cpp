#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* start = new ListNode();
        ListNode* curr = start;
        int carry =0;
        while(l1!=NULL || l2!=NULL || carry !=0){
            int x = l1 ? l1->val : 0;
            int y = l2 ? l2->val : 0;
            int sum = x + y + carry;
            carry = sum /10;
            curr->next = new ListNode((sum)%10);
            curr = curr->next;
            l1 = l1? l1->next:nullptr;
            l2 = l2? l2->next:nullptr;
        };
        return start->next;
    };
    pair<ListNode*, ListNode*> createListNodes(int* first, int* second, int first_size, int second_size){
        ListNode* dummy_head = new ListNode();
        ListNode* curr = dummy_head;
        for(int i=0; i<first_size; i++){
            curr->next = new ListNode(first[i]);
            cout << i << "th node is" << first[i];
            curr = curr->next;
        }
        ListNode* dummy_head2 = new ListNode();
        ListNode* curr2 = dummy_head2;
        for(int i=0; i<second_size; i++){
            curr2->next = new ListNode(second[i]);
            cout << i << "th node is" << second[i];
            curr2 = curr2->next;
        }
        return make_pair(dummy_head, dummy_head2);
    }
};

int main(){
    Solution* a = new Solution();
    std::vector<int> first = {1,0,2,4};
    std::vector<int> second = {1,0,2,4};
    pair<ListNode*, ListNode*> listnode_pair = a->createListNodes(&first[0], &second[0], first.size(), second.size());
    a->addTwoNumbers(listnode_pair.first, listnode_pair.second);

}