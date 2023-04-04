// * *baekjoon1977 완전제곱근
// * Input :
// * 60
// * 100
// *
// * Output :
// * 245
// * 64
// *
// * Explain :
// * 완전탐색으로 풀었다. 문제를 제대로 읽지 않아서 for문 범위를 잘못 지정하는 바람에
// * 30분정도 헤멨었다.. 다음부턴 똑바로 문제를 읽어야 되겠다.
// * 다른 블로그 코드들을 보니까 answer의 배열을 오름차순 sort를 넣어서 정렬을 했는데
// * 나는 어차피 for문에서 작은 값부터 들어가기때문에 그렇게 해줄 필요가 없어서 그부분은 생략했다.


#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int M, N;
    cin >> M;
    cin >> N;
    
    int answer[10001]{0};
    int sum = 0;
    int count = 0;
    
    for (int i=0; i<=N; i++){
        
        if(i*i >= M && i*i <= N){
            sum += i*i;
            answer[count] = i*i;
            count++;
        }
    }
    
    if (count == 0){
        cout << -1;
    }
    else {
        cout << sum << "\n" << answer[0];
    }
    return 0;
    
}
