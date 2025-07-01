#include <stdio.h>
#include <string.h>
 int main(){
    char str[100];
    int i=0, state=0;
    printf("string hann: ");
    scanf("%s",str);
    while(str[i] != '\0'){
        char x=str[i];
        switch(state){
            case 0:
            if(x=='a'){
                state=1;
            }
            else{
                state=3;
            }
            break;
            case 1:
            if(x=='b'){
                state=2;
            }
            else{
                state=3;
            }
            break;
            case 2:
            if(x=='a' ||x=='b' ){
                state=2;
        }
        
        }
        i++;
        
        

    }
    if (state==2){
        printf("accept vyo: %s ",str);

    }else 
    {
        printf("rejected: %s",str);
    }
return 0;
    
 }

