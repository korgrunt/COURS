#include <stdio.h>
#include <stdlib.h>

typedef struct Node_ {

    int val;
    struct Node_ * next;
    struct Node_ * prev;

} Node;

typedef struct List_ {

    struct Node_ * start;
    struct Node_ * end;
    struct int size;

} List;


Node* createNode(int val) {

    Node* elm = malloc(sizeof(Node));
    elm->val = val;
    elm->next = NULL;
    elm->prev = NULL;
    return elm;
}

List* createList() {

    List* list = malloc(sizeof(List));
    list->size = 0;
    list->start = NULL;
    list->end = NULL;
    return list;
}

List* insertElementAtEnd(List* list, int newVal){
    if(list->next == NULL && list->start == NULL){
        Node * newNode = createNode(newVal);
        newNode->next = newNode;
        newNode->prev = newNode;
        newNode->start = newNode;
        newNode->end = newNode;
        return list;
    }
   Node * lastNode = list->end;
   Node * firstNode = list->start;
   Node * newNode = createNode(newVal);

   firstNode->prev = newNode;
   lastNode->next = newNode;
   newNode->prev = list->end;
   newNode->next = list->start;
   list->end = newNode;
   list->size += 1;
   return list;
}


Node* insertElementAtStart(Node* firstNode, int newVal){
    if(list->next == NULL && list->start == NULL){
        Node * newNode = createNode(newVal);
        newNode->next = newNode;
        newNode->prev = newNode;
        newNode->start = newNode;
        newNode->end = newNode;
        return list;
    }
   Node * lastNode = list->end;
   Node * firstNode = list->start;
   Node * newNode = createNode(newVal);

   firstNode->prev = newNode;
   lastNode->next = newNode;
   newNode->prev = list->end;
   newNode->next = list->start;
   list->start = newNode;
   list->size += 1;
   return list;
}


void readListAtPositionN(List* list, int pos){
    if(list->start == NULL && list->end == NULL){
        printf("Cannot read from empty list");
        return;
    }
    Node * firstElement = list->start;
    int counter = 0;
    Node * tmp = list->start;
    while(tmp->next != NULL && counter < pos){
        tmp = tmp->next;
        counter++;
    }
    printf("Value we read at position %d, is %s \n", pos, tmp->val);
    return;

}

void destructNode(Node * node){
    node->next = NULL;
    node->prev = NULL;
    free(node);
    return;
}

void destructList(List * list){
    if(list->next == NULL && list->start == NULL){
        free(list);
        return;
    }
    Node * tmp = list->start;
    while(tmp->next != tmp->prev){
        Node * nextNode = tmp->next;
        destructNode(tmp);
        tmp = nextNode;
    }
    destructNode(tmp);
    return;
}

List* deleteElementFromList(List* list, int pos){
    if(list->start == NULL && list->end == NULL){
       printf("Cannot read from empty list");
       return;
    }
    Node * firstElement = list->start;
    int counter = 0;
    Node * tmp = list->start;
    while(tmp->next != NULL && counter < pos){
       tmp = tmp->next;
       counter++;
    }
    Node * sliceA = tmp->prev;
    Node * sliceB = tmp->next;
    sliceA->next = sliceB;
    sliceB->prev = sliceA;
    printf("Value we delete at position %d, is %s \n", pos, tmp->val);
    destructNode(tmp);
    return list;

}

int getSizeList(List* list){
    return list->size;
}

int main(int argc, char * argv[]){
    Node* list = NULL;
    list = createList();

    printf("My list just creaed, it's empty \n");
    list = insertElementAtEnd(list, 2);
    printf("My fisrt node is of val %d \n", list->val);

    list = insertElementAtStart(list, 99);

    printf("My fisrt node is of val %d \n", list->val);
    for(int i = 0; i < 10; i++){
        list = insertElementAtStart(list, i * i);
    }
    /*

    printf("My fisrt node is now of val %d \n", elm->val);
    readListAtPositionN(elm, 2);
    printf("\n\n Size of liste is currently %d \n", getSizeList(elm));

    readListAtPositionN(elm, 2);
    elm = deleteElementFromList(elm, 1);

    readListAtPositionN(elm, 2);
    printf("\n\n Size of liste is currently %d \n", getSizeList(elm));

    while(elm->next != NULL){
        elm = deleteElementFromList(elm, getSizeList(elm) - 1);
    }

    free(elm);

*/
    return 0;

}
