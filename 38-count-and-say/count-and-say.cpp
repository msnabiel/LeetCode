class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) {
            return "1";
        }

        string result = "1"; 

        for (int i = 2; i <= n; i++) {
            result = nextSequence(result); 
        }

        return result;
    }

    string nextSequence(const string& str) {
        stringstream ss;
        int count = 1;

        for (int i = 1; i <= str.size(); i++) {
            if (i == str.size() || str[i] != str[i - 1]) {
                ss << count << str[i - 1];
                count = 1;
            } else {
                count++;
            }
        }

        return ss.str();
    }
};
