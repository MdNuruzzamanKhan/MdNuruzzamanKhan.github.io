//Is it a prime number? (c)
/* Author: Md. Nuruzzaman Khan */

#include<stdio.h>

int main() {
    int n,r,i,ind=0;
    printf ("Enter a number:");
    scanf ("%d",&n);
    if(n<=0)
    printf(" %d\nplease, enter a positive integer.",n);
    else if(n==1)
    printf(" 1\nThe number is 1.");
    else{
        for(i=2;i<=n/2;i++){
            r=n%i;//reminder
            if(r==0){
                ind=1;
                break;
            }
        }
    if(ind==1)
    printf (" %d\nIt is not a prime number.",n);
    else
    printf (" %d\nIt is a prime number.",n);
    }
    return 0;
}

// OUTPUT:

// Enter a number: 1
// The number is 1.

// Enter a number: 13
// It is a prime number.

// Enter a number: 27
// It is not a prime number.