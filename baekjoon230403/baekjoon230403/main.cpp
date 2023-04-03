// * baekjoon 8958 "OX퀴즈"
// * input :
// *
// * 5
// * OOXXOXXOOO
// * OOXXOOXXOO
// * OXOXOXOXOXOXOX
// * OOOOOOOOOO
// * OOOOXOOOOXOOOOX
// * output
// *
// * 10
// * 9
// * 7
// * 55
// * 30

#include <iostream>
using namespace::std;
int main(int argc, const char * argv[]) {
    int N;
    string quiz;
    cin >> N;
    
    for (int i=0; i<N; i++){
        
        int answer = 0;
        int count = 0;
        cin >> quiz;
        
        for (int j=0; j< quiz.length(); j++){
            if (quiz[j] == 'O'){
                count++;
                answer+=count;
            }
            else{
                count = 0;
            }
        }
        cout << answer << endl;
    }
}
