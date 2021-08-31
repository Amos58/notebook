import tensorflow as tf
import numpy as np

#直接创建
a=tf.constant([1,2],dtype=tf.float64)

#numpy转化为tensor
a=np.arange(0,5)
b=tf.convert_to_tensor(a,dtype=tf.int64)
print("\n",a)
print("\n",b)

#创建指令张量
a=tf.zeros([1,2])
b=tf.ones([1,3])
c=tf.fill([2,2],9)#(shape,content)
d=tf.random.normal([2,2],mean=0.5,stddev=1)
e=tf.random.truncated_normal([2,2],mean=0.45,stddev=1)# 生成随机数在两倍标准差之内
f=tf.random.uniform([2,2],maxval=10,minval=0)

