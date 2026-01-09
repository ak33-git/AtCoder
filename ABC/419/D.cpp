#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    string S, T;
    cin >> S;
    cin >> T;
    vector<int> S_memo(N+2);
    for(int i = 0; i < N+2; i++){
        S_memo[i] = 0;
    }
    for(int i = 0; i < M; i++){
        int L, R;
        cin >> L >> R;
        S_memo[L] += 1;
        S_memo[R+1] += 1;
    }
    for(int i = 1; i < N+1; i++){
        S_memo[i] += S_memo[i-1];
    }
    string ans = "";
    for(int i = 1; i < N+1; i++){
        if(S_memo[i] % 2 == 0){
            ans += S[i-1];
        } else {
            ans += T[i-1];
        }
    }
    cout << ans << endl;
}