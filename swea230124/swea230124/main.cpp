//
//  main.cpp
//  swea230124
//
//  Created by WOORI JEON on 2023/02/08.
//
//**input : SWEA1230.
//**output
//
#include <iostream>
#define MAX_SIZE 10000

using namespace std;

typedef struct node {
    int value;
    struct node* next; //다음값 연결

}NODE;

NODE* head;
NODE* tail;
NODE nodeList[MAX_SIZE];

int nodeIndex = 0;

// voide로 하면 리턴이 되지 않음
// return할 변수의 타입으로 지정

NODE* initNode(int value) {
    // 내보내줄 노드
    NODE* returnNode = &nodeList[nodeIndex];
    nodeIndex++;

    returnNode->value = value;
    returnNode->next = NULL;

    return returnNode;
}

// node를 리스트 끝에 넣는 함수
void nodeAppend(NODE* node) {
    // tail==NULL이면 리스트가 비어있는 상태
    if (tail == NULL) {
        tail = node;
        head = node;
    }
    // tail!=NULL이면 리스트안에 노드가 있는 상태
    else {
        tail->next = node; // 현재 들어오는 노드를 끝에 연결
        tail = node; // 현재들어오는 노드가 끝임을 명시
    }
}

// node를 리스트 중간에 넣는 함수
void nodeInsert(NODE* prevNode, NODE* curNode) {
    curNode->next = prevNode->next;
    prevNode->next = curNode;
}

// node를 리스트에서 삭제하는 함수
void nodeDelete(NODE* prevNode, NODE* curNode) {
    if (curNode == head) {
        head = curNode->next;
    }
    else if (tail == curNode) {
        // tail == curNode
        prevNode->next = NULL;
        tail = prevNode;
    }
    // 중간에서 빠질때
    else {
        prevNode->next = prevNode->next->next;
        //prevNode->next->next == curNode->next
    }

}

void testCaseInit() {
    head = NULL;
    tail = NULL;
    nodeIndex = 0;

}

int main(int argc, const char* argv[]) {
    int test;
    for (test = 1; test <= 10; test++) {
        testCaseInit();

        int N_len;
        int M_len;
        cin >> N_len;


        for (int i = 0; i < N_len; i++) {
            int value;
            cin >> value;

            NODE* node = initNode(value);
            nodeAppend(node);
        }

        cin >> M_len;

        for (int i = 0; i < M_len; i++) {
            char func;
            cin >> func;

            if (func == 'I') {
                int x, y, s;
                cin >> x >> y;
                NODE* prevNode = head;

                if (x == 0) {
                    cin >> s;
                    NODE* node = initNode(s);
                    node->next = head;
                    head = node;
                    prevNode = head;

                    y--;
                }
                else {
                    while (x > 1) {
                        prevNode = prevNode->next;
                        x--;
                    }
                }

                for (int j = 0; j < y; j++) {
                    cin >> s;
                    NODE* node = initNode(s);
                    nodeInsert(prevNode, node);
                    prevNode = node;
                }
            }
            else if (func == 'D') {
                int x, y;
                cin >> x >> y;
                NODE* prevNode = head;

                while (x > 1){
                    prevNode = prevNode->next;
                    x--;
                }
                for (int j = 0; j < y; j++) {
                    if (x == 0) {
                        nodeDelete(prevNode, head);
                    }
                    else {
                        nodeDelete(prevNode, prevNode->next);
                    }
                }

            }
            else if (func == 'A') {
                int y, s;

                cin >> y;
                for (int j = 0; j < y; j++) {
                    cin >> s;
                    NODE* node = initNode(s);
                    nodeAppend(node);

                }

            }

        }
        //     순회 확인
        int count = 1;

        NODE* curNode = head;
        cout << "#" << test << " ";
        while (curNode != NULL && count <= 10) {
            count++;
            cout << curNode->value << " ";
            curNode = curNode->next;
        }
        cout << endl;

    }

}
