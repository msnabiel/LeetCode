class Solution {
public:
    string clearDigits(string s) {
        stack<char> stk;
        for(char i : s){
            if(!isdigit(i)){
                stk.push(i);
            }
            else{
                if(!stk.empty() && (stk.top() >= 'a' && stk.top() <= 'z')){
                    stk.pop();
                }
                else if(!stk.empty() || (stk.top() <= 'a' && stk.top() >= 'z')){
                    stk.push(i);
                }
            }
        }
        string rev = "";
        while(!stk.empty()){
            rev+=stk.top();
            stk.pop();
        }
        reverse(rev.begin(),rev.end());
        return rev;
    }
};