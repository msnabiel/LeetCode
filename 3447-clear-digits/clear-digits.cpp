class Solution {
public:
    string clearDigits(string s) {
        int digit_ptr = 0;
        int char_ptr = 0;
        int n = s.size();

        while(digit_ptr < n){
            while(digit_ptr < n && !isdigit(s[digit_ptr])){
                digit_ptr++;
            }
            if(digit_ptr == n){
                break;
            }
            char_ptr = digit_ptr;
            while(char_ptr >= 0 && (s[char_ptr] < 'a' || s[char_ptr] > 'z')){
                char_ptr--;
            }
            s[digit_ptr] = '*';
            s[char_ptr] = '*';
            digit_ptr++;

        }
        string ans = "";
        for(auto it : s){
            if(it != '*'){
                ans += it;
            }
        }
        return ans;
    }
};