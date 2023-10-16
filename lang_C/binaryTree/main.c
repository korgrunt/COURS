#include <stdio.h>
#include <stdlib.h>




typedef struct Tree_ {
    struct Node_ * root;
    int nbElm;
} Tree;

typedef struct Node_ {
    
    int val;
    struct Node_ * left; // lower than val
    struct Node_ * right; // higher than val


} Node;

Tree * createTree(){
    Tree * tree = malloc(sizeof(Tree));
    tree->root = NULL;
    tree->nbElm = 0;
    return tree;
}


Node * createNode(int val){
    Node * node = malloc(sizeof(Node));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}

Node * insertNode(Node * parent, Node * node){
   
    if(parent == NULL){
        return node;
    }
    if(node->val < parent->val){
        Node * newNode = insertNode(parent->left, node);
        parent->left = newNode;
    } else if(node->val > parent->val){

        Node * newNode = insertNode(parent->right, node);
        parent->right = newNode;
    } 
    return parent;
}


Tree * removeNode(Tree * tree){

    return tree;
}


void suppressNode(Node * node){

    return;
}

void suppressTree(Tree * tree){

    return;
}


void printNodeAndChildren(Node * node, int lvl){
    if(node == NULL){
        return;
    }
    if(node->left != NULL){
        printNodeAndChildren(node->left, lvl+1);
    }

    if(node->right != NULL){
        printNodeAndChildren(node->right, lvl+1);
    }

    for(int i = 0; i < lvl; i++){
        printf("-");
    }
    printf("%d \n", node->val);
    
    return;
}

void printTree(Tree * tree){
    printf("Printing tree\n");
    if(tree->root == NULL){
        printf("Empty tree, nothing to print\n");
        return;
    }
    printNodeAndChildren(tree->root, 0);
    return;
}


int main(int argc, char * argv[]){
    
    Tree * tree = createTree();
    Node * node = createNode(42);
    Node * node1 = createNode(13);
    Node * node2 = createNode(23);
    Node * node3 = createNode(41);
    Node * node4 = createNode(10);
    Node * node5 = createNode(1);
    Node * node6 = createNode(100);
    Node * node7 = createNode(98);
    Node * node8 = createNode(77);

    
    printf("START **************************");
    
    Node * newRoot = insertNode(tree->root, node);
    tree->root = newRoot;
    
    newRoot = insertNode(tree->root, node1);
    tree->root = newRoot;


    newRoot = insertNode(tree->root, node2);
    tree->root = newRoot;

    newRoot = insertNode(tree->root, node3);
    tree->root = newRoot;

    newRoot = insertNode(tree->root, node4);
    tree->root = newRoot;

    newRoot = insertNode(tree->root, node5);
    tree->root = newRoot;

    newRoot = insertNode(tree->root, node6);
    tree->root = newRoot;

    newRoot = insertNode(tree->root, node7);
    tree->root = newRoot;

    newRoot = insertNode(tree->root, node8);
    tree->root = newRoot;



printTree(tree);


    printf("END **************************");

    return 0;

}
