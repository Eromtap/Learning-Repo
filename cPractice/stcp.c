/* my own implementation of strcp(). Just getting used to working with pointers */




#include <stdio.h>
#include <stdlib.h>

void stcp(char *x,int l, char y[]);

int main(){
    char name[100];

    stcp(name,sizeof(name), "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15");

    printf("%s\n",name);

    return 0;
}

void stcp(char *x,int l, char *y){
    int i=0;
    while(*y != '\0' && i<l){
        *x=*y;
        y++;
        x++;
        i++;
    }

}
