import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


/*
* Input *
* 8
* 0 1 0 1 0 0 0 1
* 2
* 1 3
* 2 3
*
* Output *
* 1 0 0 0 1 1 0 1
*/
class Person{
    int gender;
    int number;
    Person(int gender, int number){
        this.gender = gender;
        this.number = number;
    }
}

class Solution{
    public void solutionRecursion(int start, int end, int cur, int switchArr[]){
        if (start<0 || end>=switchArr.length){ // 배열의 범위를 초과했을 때의 기저조건
            return;
        }
        if(switchArr[start]==switchArr[end]) { // 대칭 조건

            if (switchArr[start] == 1) switchArr[start] = switchArr[end] = 0;

            else switchArr[start] = switchArr[end] = 1;

            solutionRecursion(start - 1, end + 1, cur + 1, switchArr);
            // 대칭조건에 성립 시 다음 재귀로 넘어감
        }
    }
}

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine()); // 스위치 갯수 입력

        StringTokenizer st = new StringTokenizer(bf.readLine()); // 스위치 입력
        int switchArr[] = new int[N]; // 스위치리스트

        for(int i=0; i<N; i++){
            switchArr[i] = Integer.parseInt(st.nextToken());
        }

        int personNum = Integer.parseInt(bf.readLine()); // 사람 수 입력
        Person personArr[] = new Person[personNum]; // 사람들 Array


        for(int i=0; i<personNum; i++){
            st = new StringTokenizer(bf.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int number = Integer.parseInt(st.nextToken());
            personArr[i] = new Person(gender, number); // Person Class에 넣어줌
        }

        for(int i=0; i<personNum; i++) {
            if (personArr[i].gender == 1) {
                // 남자
                int switchMale = personArr[i].number;

                // 남자의 배수 구현
                for (int j = 0; j < N; j++) {
                    if ((j + 1) % switchMale == 0) {
                        if (switchArr[j] == 0) switchArr[j] = 1;
                        else switchArr[j] = 0;
                    }
                }
            } else {
                // 여자
                int switchFemale = personArr[i].number;

                // 여자의 대칭 구현
                for (int j = 0; j < N; j++) {
                    if (switchFemale == j + 1) {
                        Solution s = new Solution();
                        s.solutionRecursion(j - 1, j + 1, 0, switchArr);
                        if (switchArr[j] == 0) switchArr[j] = 1;
                        else switchArr[j] = 0;

                    }
                }
            }
        }
        for(int i=1; i<=N; i++){
            System.out.print(switchArr[i-1]+" ");
            if(i%20==0) System.out.println();
        }
    }
}

/*
* 참고 자료 *
* https://jooyoung0525.tistory.com/15
* 그림이 이해하기 편해서 참고해서 재귀를 풀었습니다.
*
* 느낀점 *
* (1) 재귀에서 기저조건을 잘 이용해야 재귀함수에서 빠져나올 수 있다는 것을 알았다. 처음에는 기저조건을 잘못이해해서
* 다른 방식으로 함수를 빠져나오게끔 구현을 했었는데 기저조건 코드를 작성하고나서 코드가 훨씬 간결해졌다.
*
* (2) 아직 java가 익숙하지 않아서 배열에 담는 것이 헷갈렸다.
* 특히 StringTokenizer를 계속 재선언했었는데 선언해준 변수명만 가져와서 쓰면 nextToken이 계속 이어진 다는 것을 알았다.
*
* (3) 클래스를 따로 만들어 construct들을 관리해주니 N의 갯수를 자동적으로 늘어날 수 있게 해서 편리했다.
* 훨씬 코드가 간결해졌다.
*
* */