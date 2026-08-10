class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>store;
        for(int n:nums){
            store[n]++;
        }
        int s = nums.size();
        vector<vector<int>> buckets(s+1);
        for(auto& [n,count]:store){
            buckets[count].push_back(n);

        }

        vector<int>result;
        for(int i=s; i>=0 &&result.size()<k;--i){
            for(int num:buckets[i]){
                result.push_back(num);
            }
        }
        return result;
    }
};
