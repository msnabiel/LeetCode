class Solution {
public:
    bool isPalindrome(string s) {
        string neww = "";

        // Filter the string to keep only alphanumeric characters and convert to lowercase
        for (char c : s) {
            if (isalnum(c)) {
                neww += tolower(c);
            }
        }

        // Check if the string is a palindrome
        string reversed = neww; 
        reverse(reversed.begin(), reversed.end());
        
        return neww == reversed;
    }
};