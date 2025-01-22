
class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int m = isWater.size();
        int n = isWater[0].size();
        
        vector<vector<int>> height(m, vector<int>(n, -1));
        
        queue<pair<int, int>> q;
        
        // Add all water cells to the queue, and set their height to 0
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (isWater[i][j] == 1) {
                    height[i][j] = 0;  // Water cells have height 0
                    q.push({i, j});     // Add to BFS queue
                }
            }
        }
        
        // Directions for moving north, south, east, and west
        vector<int> directions = {-1, 0, 1, 0, -1, 0};  // {north, east, south, west}
        
        // Perform BFS
        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();
            
            // Check all 4 possible directions
            for (int i = 0; i < 4; ++i) {
                int nx = x + directions[i];
                int ny = y + directions[i + 1];
                
                // Check if the new position is within bounds and hasn't been visited yet
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && height[nx][ny] == -1) {
                    height[nx][ny] = height[x][y] + 1;
                    q.push({nx, ny});  
                }
            }
        }
        
        return height;
    }
};