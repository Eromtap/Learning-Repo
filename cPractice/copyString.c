/* using stcp.h */


#include <stdio.h>
#include <stdlib.h>
#include "stcp.h"

int main(){

    char name[100];

    stcp(name,sizeof(name),"hello, world");

    printf("%s\n",name);


    return 0;
}
