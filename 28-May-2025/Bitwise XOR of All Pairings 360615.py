# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size();
        int m=nums2.size();
        int first_xor=accumulate(nums1.begin(),nums1.end(),0,bit_xor());
        int second_xor=accumulate(nums2.begin(),nums2.end(),0,bit_xor());
        if(n%2 && m%2){
            return first_xor^second_xor;
        }else if(n%2){
            return second_xor;
        }else if(m%2){
            return first_xor;
        }else{
            return 0;
        }
    }
};