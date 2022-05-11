void solve(vector<int> &A,int start,int end,vector<int>& temp,set<vector<int> >& ans,int sum)
{
    if(sum<0) return;
    if(sum==0){
        ans.insert(temp);
        return;
    }
    if(start>end) return;
    solve(A,start+1,end,temp,ans,sum);
    temp.push_back(A[start]);
    solve(A,start,end,temp,ans,sum-A[start]);
    temp.pop_back();
}

vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    sort(A.begin(), A.end());
    int n=A.size(),i;
    vector<vector<int> > ret;
    if(n==0) return ret;
    set<vector<int> > ans;
    vector<int> temp;
    solve(A,0,n-1,temp,ans,B);
    for(auto it=ans.begin() ; it!=ans.end() ; it++)
        ret.push_back(*it);
    return ret;
}