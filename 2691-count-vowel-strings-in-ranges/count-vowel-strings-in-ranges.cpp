class Solution {
public:
    bool isVowel(char ch){
        if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'){
            return true;
        }
        return false;
    }
    int func(int l,int r, vector<string>& words){
        int cnt = 0;
        for(int i=l;i<=r;i++){
            if(isVowel(words[i][0]) && isVowel(words[i][words[i].size()-1])){
                cnt++;
            }
        }
        return cnt;
    }
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        int n = words.size();
        vector<int> prefix_sum(n+1,0);
        prefix_sum[0] = 0;
        int cnt = 0;
        for(int i=0;i<words.size();i++){
            if(isVowel(words[i][0]) && isVowel(words[i][words[i].size()-1])){
                prefix_sum[i+1] = ++cnt;
            }else{
                prefix_sum[i+1] = cnt;
            }
        }

        vector<int> ans;
        for(int i=0;i<queries.size();i++){
            int val = prefix_sum[queries[i][1]+1] - prefix_sum[queries[i][0]];
            ans.push_back(val);
        }

        return ans;
    }
};