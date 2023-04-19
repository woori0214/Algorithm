// * baekjoon2747 "피보나치의 수"

// 1. DP 방식

//#include <iostream>
//using namespace std;
//
//int main(int argc, const char * argv[]) {
//    int n;
//    cin >> n;
//    int array[n];
//    array[0] = 0;
//    array[1] = 1;
//
//    for (int i=2; i<n+1; i++){
//        array [i] = array[i-2]+array[i-1];
//    }
//
//    cout<<array[n];
//}

//2. Recur 방식
//
#include <iostream>
using namespace std;


int arr[100]{0}; // 0으로 다 초기화

int fibo(int n){

    if (n <= 1) return n; // n이 1이하면 0과 1이기때문에 그대로 출력이 가능

    if (arr[n] > 0) return arr[n]; // 메모이제이션

    arr[n] = fibo(n-1) + fibo(n-2); // 재귀를 통해 fibo를 연속적으로 들어가서 값을 계산
        return arr[n];
}

int main(){

    int n;
    cin >> n;

    arr[0] = 0;
    arr[1] = 1;

    cout << fibo(n);
}
