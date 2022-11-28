/* stcp (my string copy) made as header file */



void stcp(char *x,int l, char *y){
    int i=0;
    while(*y != '\0' && i<l){
        *x=*y;
        y++;
        x++;
        i++;
    }

}
