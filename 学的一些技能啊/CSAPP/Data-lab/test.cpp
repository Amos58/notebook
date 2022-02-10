#include<iostream>
using namespace std;
int _xor(int x,int y){
     return ~(~(~x&y)&(~(x&(~y))));
}
int tmin(void) {
  return 1<<31;
}
int tmax(void) {
    int x=0;
  return UINT_MAX;
}
int main(){
    cout<<tmax()<<endl;
    return 0;
}