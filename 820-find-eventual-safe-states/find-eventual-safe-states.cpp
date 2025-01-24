class Solution {
private:
    bool safe(int node, vector<vector<int>>& graph, vector<int>& vis, vector<int>& isterminal) {
        if (vis[node] != 0) { 
            return isterminal[node] == 1;
        }

        vis[node] = -1; 
        for (auto it : graph[node]) {
            if (!safe(it, graph, vis, isterminal)) {
                return false; 
            }
        }

        vis[node] = 1;       
        isterminal[node] = 1;
        return true;
    }

public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int v = graph.size();
        vector<int> vis(v, 0);          
        vector<int> isterminal(v, 0);  
        for (int i = 0; i < v; i++) {
            if (!vis[i]) {
                safe(i, graph, vis, isterminal);
            }
        }
        vector<int> ans;
        for (int i = 0; i < v; i++) {
            if (isterminal[i] == 1) {
                ans.push_back(i);
            }
        }

        return ans;
    }
};