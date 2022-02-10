---
title: Data-lab
date: 2022-02-10 20:16:18
tags:CSAPP
---

# Data-lab

## ReadMe

### Goal:

+ modify your copy of bits.c

### Function

这里只记录了做的过程中遇到难题的几个

#### 1.isTmax

​	题意：判断是否输入x是补码中最大的值。

```c
int isTmax(int x) {//假设x=0x0111
    int i=x+1;//i=1000
    x=x+i;
    /*
    这是当x=-1（1111）时，i=0（0000）；
    但是正确的情况下i=1000
    因此需要对i的值进行一个判断，题目不允许用If，需要设计新的算法
    */
    /*
    x=>0;
    if(i==0) x=x+i=0
    if(i!=0) x=x+i!=0
    */
    x=~x;
    i=!i;
    x=x+i;
    return !(x);
}
```

#### 2. alloddbits

题意：判断输入x的所有奇数位是否为1

```c
int allOddBits(int x) {
  int mask =0xAAAAAAAA;//构造mask
  x=x&mask;//非奇数位变0
  x=x+0x55555555;//x=-1
  return !(x+1);
}
```



#### 3.negate(**int** x)

题意：求-x

 考察补码的运算

#### 4.**int** isAsciiDigit(**int** x)

```c
int sign=1<<31;
  int upper=~(sign|0x39);
  int lower=~0x30;
  upper=(upper+x)>>31;
  lower=(lower+x+1)>>31;
  return !(upper|lower)
```

思路：x-0x30>=0&&x+(MAX_INT-0x39)>=0

#### 5. **int** isLessOrEqual(**int** x, **int** y)

```c
int isLessOrEqual(int x, int y) {
  int signX=(x>>31)&1;
   int signY=(y>>31)&1;
   int checksign=((y+(~x+1))>>31)&1;
   int xorbit=signX^signY;//数一
   int sign=signX;
   return ((!xorbit)&(!checksign))|(xorbit&sign);
}
```

#### 6.  **int** howManyBits(**int** x)

```c
//倍增法
  int b16,b8,b4,b2,b1,b0;
  int sign=x>>31;
  x=(sign&~x)|(~sign&x);
  b16=!!(x>>16)<<4;
  x=x>>b16;
  b8=!!(x>>8)<<3;
  x=x>>b8;
  b4=!!(x>>4)<<2;
  x=x>>b4;
  b2=!!(x>>2)<<1;
  x=x>>b2;
  b1=!!(x>>1)<<0;
  x=x>>b1;
  b0=x;
  return b0+b1+b2+b4+b8+b16+1;
```

#### 7. **unsigned** floatScale2(**unsigned** uf)

>#### IEEE浮点表示
>
>原理：使用x和y表示$ x\times 2^y$的数
>
>IEEE浮点标准用$V =(-1)^s \times M \times 2^E $​的形式表示一个数​。对0的符号位做特殊处理。对浮点数的位划分为符号位（1位）、尾数（n位）和阶码（k位）三个字段，分别对这些值进行编码。M的取值的范围是1~2-$ \epsilon $或者0~$1-\epsilon$。
>
>在float中，s=1,k=8,n=23；在double中，s=1,k=11,n=52。
>
>IEEE的浮点表示分为三种，非规格化、规格化以及无穷大和NaN
>
>+ 非规格化数的阶码为0，E=1-bias，这么做是可以实现从非规格化数到规格化数的平稳过渡
>  + 非规格化数的作用是表示0和表示接近0的数，对于接近0的数，越趋近于0时越稠密
>+ 规格化数的阶码大于0小于$2^k-1$
>+ 阶码全为一时分为两种情况，M$=$0时表示$\infin$，$M\not =0$时表示$NaN$



```c
int sign=uf&(1<<31);
  int exp=(uf&(0x7f800000))>>23;
  if(exp==0) return (uf<<1)|sign;
  if(exp==255) return uf;
  exp++;
  if(exp==255) return 0x7f800000|sign;
  return (uf&(~0x7f800000))|(exp<<23);
```

#### 8. **int** floatFloat2Int(**unsigned** uf)

```C
int floatFloat2Int(unsigned uf) {
   int sign=uf>>31;
  int exp=(0x7f800000)&uf;
  int M=(~0xff800000)&uf;
  exp=exp>>23;
  if(exp==0) return 0;
  M=(1<<23)|M;
  exp=exp-127;
  if(exp<0) return 0;
  if(exp>31) return 0x80000000;
  if(exp<23)
  M=M>>(23-exp);
  else{
  M=M<<(exp-23);
  }
  if(!sign) return M;
  else{
    M=(~M+1);
  }

  return M;
}
```

#### 9.floatPower2(int x)

```C
 int inf = 0xff<<23;
  int exp = x + 127;
  if(exp <= 0) return 0;
  if(exp >= 255) return inf;
  return exp << 23;
```

### SUM

![image-20220211003445804](C:\Users\Amos\AppData\Roaming\Typora\typora-user-images\image-20220211003445804.png)
