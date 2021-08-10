//simple_simulation
#include<stdio.h>
//3n+1
static int count=0;
void Callatz(int a){   
    if(a==1){
        return;
    }
    else{
        if(a%2){
            a=3*a+1;
            a=a/2;
            Callatz(a);
        }
        else{
            a=a/2;
            Callatz(a);
        }
    }
    count++; 
}

//挖掘机技术
void excavator(int n){ 
    int score[100010]={0};
    int temp,sc;
    int max_id,max;
    max_id=1;
    max=0;
    for(int i=1;i<=n;i++){
        scanf("%d%d",&temp,&sc);
        if(temp>100001||temp<1)
            return;
        else{
            score[temp]+=sc;
            if(score[temp]> max){
                max_id=temp;
                max=score[temp];
            }
        }
    }
    printf("%d %d",max_id,max);

}
int main(){
    int n;
    printf("请输入n");
    scanf("%d",&n);
    Callatz(n);
    printf("%d\n",count);
    excavator(6);
    return 0;
}