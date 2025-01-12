class Solution {
public:
    bool canBeValid(string s, string locked) {
    int n = s.length();

    // If the string length is odd, it cannot be valid.
    if (n % 2 != 0) return false;

    // Step 1: Left-to-right traversal to check if there are enough open parentheses.
    int balance = 0, flexible = 0; // Balance tracks '(' and ')' difference, flexible tracks unlocked positions.
    for (int i = 0; i < n; ++i) {
        if (locked[i] == '0') {
            flexible++; // Unlocked positions can be either '(' or ')'.
        } else if (s[i] == '(') {
            balance++; // Locked '(' increases the balance.
        } else {
            balance--; // Locked ')' decreases the balance.
        }

        // Flexible positions can compensate for negative balance.
        if (balance + flexible < 0) return false;
    }

    // Step 2: Right-to-left traversal to check if there are enough closing parentheses.
    balance = 0, flexible = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (locked[i] == '0') {
            flexible++; // Unlocked positions can be either '(' or ')'.
        } else if (s[i] == ')') {
            balance++; // Locked ')' increases the balance.
        } else {
            balance--; // Locked '(' decreases the balance.
        }

        // Flexible positions can compensate for negative balance.
        if (balance + flexible < 0) return false;
    }

    // If both passes succeed, the string can be valid.
    return true;
}
};