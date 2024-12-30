class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        int n = arr.size();
        bool flag = false;
        for(int i =0; i<n;++i){
            for(int j = 0; j<n;++j ){
                if(i==j){
                    continue;
                }
                else {
                    if(0 <= i){
                        if(j < n){
                            if(arr[i] == 2 * arr[j]){
                                flag = true;
                                break;
                            }
                        }
                    }
                }
            }
        }
        return flag;
    }
};