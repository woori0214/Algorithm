#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, const char * argv[]) {
    int M, N;
    cin >> M >> N;
    
    int answer[10001]{0};
    int sum = 0;
    int answerCount = 0;
    
    for (int i=1; i<=M; i++){
        
        if(i*i >= M && i*i <= N){
            sum += i*i;
            answer[answerCount] = i*i;
            answerCount++;
        }
    }
    
    sort(answer, answer+answerCount);
    if (answer[0]==0){
        cout << -1;
    }
    else {
        cout << sum << "\n" << answer[0];
    }
    
}
