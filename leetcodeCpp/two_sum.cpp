#include <vector>
#include <iostream>
#include <map>
using namespace std ;

class Solution 
{
    public:
        vector <int> twoSum(vector <int>& nums, int target) {
        map <int,int> res_hash;
        vector <int> result;
        int i;
            for(i=0;i<nums.size();i++)
                {
                    if(res_hash.find(target-nums[i])!=res_hash.end())
                    {
                        
                        result.push_back(res_hash[target-nums[i]]);
                        result.push_back(i);
                        return result;
                    }
                    else
                        res_hash[nums[i]] = i;
                }       
}
};

int main()
{
    Solution sol ;
    vector <int> nums = {1, 2, 6, 9} ;
    int target = 10 ;

    vector <int> result = sol.twoSum(nums, target) ;
    cout << "the findings are: " << result[0] << " " << result[1] << endl; 
    return 0 ;

}

// https://medium.com/@navaneethrvce/two-sum-using-hashmap-in-c-458005428938
