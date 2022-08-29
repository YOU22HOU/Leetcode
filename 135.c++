// 一群孩子站成一排，每一个孩子有自己的评分。
// 现在需要给这些孩子发糖果，规则是如果一个孩子的评分比
// 自己身旁的一个孩子要高，那么这个孩子就必须得到比身旁孩子更多的糖果
// 所有孩子至少要有一个糖果。
// 求解最少需要多少个糖果。

class Solution {
public:
    int candy(vector<int>& ratings) {
        int size = ratings.size();
        if(size < 2){
            return size
        }
        vector<int> num(size, 1);
        for(int i = 1; i < size; i++){
            if(ratings[i]>ratings[i-1]){
                num[i] = num[i-1]+1;
            }
        }
    }
};