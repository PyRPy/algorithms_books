// two_sum.cpp
// brutal force soluation
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i=0; i < nums.size(); ++i) {
            for (int j=i+1; j<nums.size(); ++j){
                int sum = nums[i] + nums[j];
                if (sum == target) {
                    return {i, j};
                }
            
            }
        }
        return {};
    }
};

int main() {
    Solution sol; 
    vector <int> nums = {1, 2, 6, 9};
    int target = 10;

    vector <int> result = sol.twoSum(nums, target);
    cout << "the findings are at: " << result[0] << " " << result[1] << endl; 
    cout << nums[result[0]] << " " << nums[result[1]] << endl; 
    cout << "the target is: " << target << endl;
    
    return 0; 
}