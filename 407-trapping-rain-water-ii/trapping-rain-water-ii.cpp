class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        if (heightMap.empty() || heightMap[0].empty()) return 0;

        int m = heightMap.size();
        int n = heightMap[0].size();
        
        // Min-heap priority queue to store the cells by height
        priority_queue<Cell, vector<Cell>, greater<Cell>> minHeap;

        // To mark the visited cells
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        // Add all boundary cells to the min-heap and mark them as visited
        for (int i = 0; i < m; ++i) {
            minHeap.push(Cell(i, 0, heightMap[i][0]));
            visited[i][0] = true;
            minHeap.push(Cell(i, n-1, heightMap[i][n-1]));
            visited[i][n-1] = true;
        }
        for (int j = 0; j < n; ++j) {
            minHeap.push(Cell(0, j, heightMap[0][j]));
            visited[0][j] = true;
            minHeap.push(Cell(m-1, j, heightMap[m-1][j]));
            visited[m-1][j] = true;
        }

        int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int waterTrapped = 0;

        // Process the cells starting from the boundary (min-heap)
        while (!minHeap.empty()) {
            Cell current = minHeap.top();
            minHeap.pop();

            // Explore the 4 neighboring cells (up, down, left, right)
            for (auto& dir : directions) {
                int newRow = current.row + dir[0];
                int newCol = current.col + dir[1];

                // Check if the new cell is within bounds and not visited
                if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && !visited[newRow][newCol]) {
                    // Water can be trapped if the current boundary is higher than the neighbor
                    if (heightMap[newRow][newCol] < current.height) {
                        waterTrapped += current.height - heightMap[newRow][newCol];
                    }

                    // Push the neighbor into the heap with the max height between current and neighbor
                    minHeap.push(Cell(newRow, newCol, max(heightMap[newRow][newCol], current.height)));
                    visited[newRow][newCol] = true;
                }
            }
        }

        return waterTrapped;
    }
    
private:
    struct Cell {
        int row, col, height;
        Cell(int r, int c, int h) : row(r), col(c), height(h) {}
        
        bool operator>(const Cell& other) const {
            return height > other.height;
        }
    };
};
