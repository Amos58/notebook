//#include"stdafx.h"
#include<process.h>
#include<stdio.h>
#include<windows.h>

int main(){
    float a=2.718f;
    unsigned char *b=(unsigned char*)&a;

    for(int i=0;i<4;i++){
        printf("0x%2x,",b[i]);
    }
    system("pause");
    return 0;
}
