// ** Case 1
// * Input:
// * 5
//* 1
//* 2
//* 11
//* 1295
//* 1692
// * Output:
//* #1 10
//* #2 90
//* #3 110
//* #4 6475
//* #5 5076

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int T;
    cin >> T ;
    
    for (int test=1; test<T+1; test++){
        int N;
        int input; // test_input
        int sleep[10] = {0}; // 0~9 array
        int answer = 0 ;
        cin >> input;
        N = input;
        
        
        for (int i=0; ; i++){
            int temp = N;
            int sleep_cnt = 0; // 곱해줄 값
            
            while(N != 0){
                sleep[N%10] = 1;
                N /= 10;
            }
            
            for (int j=0; j<10; j++){
                if(sleep[j] == 1) sleep_cnt++;
            }
            if(sleep_cnt==10){
                answer = temp;
                break;
            }
            
            N = input * i;
        }
        printf("#%d %d\n",test, answer);
    }
    return 0;
}

