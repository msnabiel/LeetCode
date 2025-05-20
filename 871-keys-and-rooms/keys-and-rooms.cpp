class Solution {
public:
    void DFS(int node, int parent, vector<bool>& visited,
             vector<vector<int>>& rooms) {
        visited[node] = true;
        for (int i = 0; i < rooms[node].size(); i++) {
            if (visited[rooms[node][i]] == false) {
                DFS(rooms[node][i], node, visited, rooms);
            }
        }
    }
    bool canVisitAllRooms(vector<vector<int>>& rooms) {

        vector<bool> visited(rooms.size(), false);

        DFS(0, -1, visited, rooms);

        for (bool el : visited)
            if (el == false)
                return false;

        return true;
    }
};