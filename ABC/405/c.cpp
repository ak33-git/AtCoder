# include <iostream>

using namespace std;

int main(){
    int N;
    cin >> N;

    int a[N];
    for (int i = 0; i < N; i++){
        cin >> a[i];
    }
    
    int s_a[N-1];
    s_a[N-2] = a[N-1];
    for (int i = N-3; i >= 0; i--){
        s_a[i] = s_a[i+1] + a[i+1];
    }

    uint64_t s = 0;
    for (int i = 0; i < N-1; i++){
        s += a[i] * s_a[i];
    }
    
    cout << s << endl;

}