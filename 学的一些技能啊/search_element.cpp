#include<stdio.h>

void graph(char a,int n){
    int m;
    int sign=1;
    if(n%2){
        m=n/2+1;        
    }
    else{
        m=n/2;
    }
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
           if((i==0||i==m-1){
                printf("%c",a);

             }
            else{
                printf("%c",a);
                for(int k=0;k<n-2;k++){
                    printf(" ");
                };
                printf("%c",a);
                printf("\n");
            }
            if(j==n-1){
                printf("\n");
            }
    }
    }
}

int main(){
    graph('a',9);
    return 0;
}