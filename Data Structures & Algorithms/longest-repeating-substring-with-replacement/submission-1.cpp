class Solution {
public:
    int characterReplacement(string s, int k) {
        int sz = s.size();
        int L = 0;
        //int R = 0;
        int longest = 0;
        vector<int>hash(26,0);
        int max_ct = 0;
        
        for(int R =0; R<sz; R++){
            int pos = s[R]-'A';
            hash[pos]++;
            //int max_hash = *max_element(hash.begin(),hash.end());
            max_ct = max(max_ct,hash[pos]);

            int length = R-L+1;
            if(length-max_ct>k){
                hash[s[L]-'A']--;
                L++;
            }
            longest = max(longest,R-L+1);
            // if(length-max_hash>=0 && length-max_hash<=k){
            //     longest = max(longest,length);
            //     //R++;
            // }
            // else{
            //     int rem = s[L]-'A';
            //     hash[rem]--;
            //     L++;
            // }
        }
        return longest;
    }
};
