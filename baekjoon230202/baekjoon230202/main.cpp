// ** Case 1
// * Input :
//15
//push 1
//push 2
//front
//back
//size
//empty
//pop
//pop
//pop
//size
//empty
//pop
//push 3
//empty
//front
//
// * Output :
//1
//2
//2
//0
//1
//2
//-1
//0
//1
//-1
//0
//3
#include <iostream>
#include <queue>
using namespace std;

int N, x;
string str;

int main(int argc, const char * argv[]) {
    cin.tie(NULL);
    cin.sync_with_stdio(false);
    
    queue<int> queue;
    
    cin >> N;
    
    for (int i=0; i<N; i++){
        cin >> str;
        
        if(str == "push"){
            cin >> x;
            queue.push(x);
        }
        
        else if(str == "pop"){
            if (!queue.empty()){
                cout << queue.front() << '\n';
                queue.pop();
            }
            else cout << -1 << '\n';
        }
        
        else if(str == "size"){
            cout << queue.size() << '\n';
        }
        
        else if(str == "empty"){
            cout << queue.empty() << '\n';
        }
        
        else if(str == "front"){
            if(!queue.empty()) cout << queue.front() << '\n';
            else cout << -1 << '\n';
        }
        
        else if(str == "back"){
            if(!queue.empty()) cout << queue.back() << '\n';
            else cout << -1 << '\n';
        }
    }
}
