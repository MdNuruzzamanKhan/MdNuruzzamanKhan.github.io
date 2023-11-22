//Reverse your name! (c)
/* Author: Md. Nuruzzaman Khan */

#include <stdio.h>
#include <string.h>

int main(){
    char name[100];
    printf("Enter your name:  ");
    fgets(name,sizeof(name),stdin);
    int l=strlen(name);
    for(int i=0,j=l-1; i<=j;i++,j--){
        char temp=name[i];
        name[i]=name[j];
        name[j]=temp;
    }
    printf("%s",name);
    return 0;
}

// OUTPUT:

// Enter your name:  nahK namazzuruN .dM