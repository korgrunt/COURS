#include <stdio.h>
#include <stdlib.h>

typedef struct Node_ {

    int val;
    struct node * next;

} Node;


Node* createNode(int valFirstElm) {

    Node* elm = malloc(sizeof(Node));
    elm->val = valFirstElm;
    elm->next = NULL;
    return elm;
}

Node* createChainedList(int valFirstElm) {

    Node* list;
    list = createNode(valFirstElm);
    return list;
}
Node* insertElementAtEnd(Node* list, int newVal){
    Node* tmp = list;
    while(tmp->next != NULL){
        tmp = tmp->next;
    }
    tmp->next = createNode(newVal);
    return list;
}


Node* insertElementAtStart(Node* list, int newVal){

    Node* elm = createNode(newVal);
    elm->next = list;
    return elm;
}


void readListAtPositionN(Node* list, int pos){
    printf("READ LIST NOW ________\n");
    int counter = 0;
    if(pos == 0){
        printf("Position %d, has a node of %d", counter, list->val);
    } else if (pos > 0){
        Node* tmp = list;
        int counter = 0;
        while(tmp->next != NULL){
            if(counter == pos){

                printf("\n\n THE Position asked  %d, has a node of %d\n\n", counter, tmp->val);
            }
            printf("Position %d, has a node of %d\n", counter, tmp->val);
            tmp = tmp->next;
            counter++; 
        }
        printf("Position %d, has a node of %d\n", counter, tmp->val);
        counter++; 

    }
    return;
}

void destructNode(Node * node){
    free(node);
    return;
}

Node* deleteElementFromList(Node* list, int pos){

    if(pos == 0 && list->next != NULL){
        return list->next;
    } 
    Node* tmp = list;
    Node* tmpPrev = list;
    int counter = 0;
    while(counter <= pos){
        printf("\nWe are at counter %d \n", counter);
        printf("We are at pos %d \n", pos);
        if(tmp->next != NULL && counter == pos-1){
            Node * slice = tmp->next; // slice should be delete
            if(slice->next != NULL){
                tmp->next = slice->next;
                destructNode(slice);
                return list;
            }
        } else if (tmp->next == NULL &&counter == pos){
            printf("HERE WE delete the last");
            destructNode(tmp);
            tmpPrev->next = NULL;
            return list;
        }
        if(tmp->next != NULL){
            tmpPrev = tmp;
            tmp = tmp->next;

        } else {
            printf("Cannot delete node outside the list.");   
            return list;
        }
        counter++;
    }
    return list;



}

int getSizeList(Node* list){

    Node* tmp = list;
    int counter = 0;
    while(tmp->next != NULL){
        tmp = tmp->next;
        counter++;
    }
    return counter + 1;
}

int main(int argc, char * argv[]){

    Node* elm = createChainedList(1);
    //    -1__1__2__
    printf("My fisrt node is of val %d \n", elm->val);
    elm = insertElementAtEnd(elm, 2);  


    printf("My fisrt node is of val %d \n", elm->val);
    for(int i = 0; i < 1000; i++){
        elm = insertElementAtStart(elm, i * i);
    }

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


    return 0;

}
