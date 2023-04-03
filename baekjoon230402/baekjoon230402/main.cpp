// * * case 1
// * input :
// * 1 2 3 4 5 6 7 8
// * output :
// * ascending
// *
// * * case 2
// * input :
// * 8 7 6 5 4 3 2 1
// * output :
// * descending
// *
// * * case 3
// * input :
// * 8 1 7 2 6 3 5 4
// * output :
// * mixed
// *

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    
    int music[8];
    int asc = 0;
    int dsc = 0;
    
    for (int i = 0; i<8; i++){
        cin >> music[i];
        
        if (music[i] == i+1) asc+=1;
        
        else if (music[i]== 8-i) dsc+=1;
        
    }
    
    if (asc == 8){
        cout << "ascending";
    }
    else if (dsc == 8){
        cout << "descending";
    }
    else cout << "mixed";
    
}
