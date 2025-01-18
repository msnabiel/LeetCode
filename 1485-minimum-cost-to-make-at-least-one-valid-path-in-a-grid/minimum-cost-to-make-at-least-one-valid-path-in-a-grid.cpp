class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        
        // Min-cost matrix initialized to INT_MAX
        vector<vector<int>> cost(n, vector<int>(m, INT_MAX));

        // Deque for BFS
        deque<pair<int, int>> dq;
        
        // Directions: Right (1), Left (2), Down (3), Up (4)
        vector<int> dx = {0, 0, 1, -1};
        vector<int> dy = {1, -1, 0, 0};

        // Start from (0,0)
        dq.push_front({0, 0});
        cost[0][0] = 0;

        // BFS
        while (!dq.empty()) {
            auto [i, j] = dq.front();
            dq.pop_front();

            for (int d = 0; d < 4; d++) {
                int ni = i + dx[d];
                int nj = j + dy[d];

                if (ni >= 0 && nj >= 0 && ni < n && nj < m) {
                    int newCost = cost[i][j] + (grid[i][j] != d + 1);

                    if (newCost < cost[ni][nj]) {
                        cost[ni][nj] = newCost;
                        
                        // If moving in the same direction, push to the front (0 cost)
                        if (grid[i][j] == d + 1) {
                            dq.push_front({ni, nj});
                        } else { // If changing direction, push to the back (cost 1)
                            dq.push_back({ni, nj});
                        }
                    }
                }
            }
        }
        
        return cost[n-1][m-1];
    }
};
