import tensorflow as  tf
from sklearn import datasets
from sklearn.datasets import load_iris
from pandas import DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import time


#准备数据
#导入鸢尾花数据集
x_data=datasets.load_iris().data
y_data=datasets.load_iris().target
#x_data=DataFrame(x_data,columns=["花萼长度","花萼宽度","花瓣长度","花瓣宽度"])
pd.set_option('display.unicode.east_asian_width',True)#设置列对齐
#print(x_data)

#x_data["类别"]=y_data
#print(x_data)

#打乱数据
np.random.seed(116)
np.random.shuffle(x_data)
np.random.seed(116)
np.random.shuffle(y_data)
tf.random.set_seed(42)

#划分数据集
x_train=x_data[:-30]
y_train=y_data[:-30]
x_test=x_data[-30:]
y_test=y_data[-30:]

x_train=tf.cast(x_train,tf.float32)
x_test=tf.cast(x_test,tf.float32)

#配对
train_db=tf.data.Dataset.from_tensor_slices((x_train,y_train)).batch(32)
test_db=tf.data.Dataset.from_tensor_slices((x_test,y_test)).batch(32)

#可训练参数
w=tf.Variable(tf.random.truncated_normal([4,3],stddev=0.1,seed=1))
b=tf.Variable(tf.random.truncated_normal([3],stddev=0.1,seed=1))

lr=0.2
train_loss_results=[]
test_acc=[]
epoch=500
loss_all=0

v_w,v_b=0,0
beta=0.9
#循环迭代参数

now_time=time.time()
for epoch in range(epoch):
    for step,(x_train,y_train) in enumerate(train_db):
        with tf.GradientTape() as Tape:
            y=tf.matmul(x_train,w)+b
            y=tf.nn.softmax(y)
            y_=tf.one_hot(y_train,depth=3)
            loss=tf.reduce_mean(tf.square(y_-y))
            loss_all+=loss.numpy()

        #计算loss的梯度
        #rmsprop
        grads=Tape.gradient(loss, [w,b])

        v_w+=v_w*beta+(1-beta)*tf.square(grads[0])
        v_b+=v_b*beta+(1-beta)*tf.square(grads[1])

        w.assign_sub(lr*grads[0]/tf.sqrt(v_w))
        b.assign_sub(lr*grads[1]/tf.sqrt(v_b))


    #对每一个epoch 打印loss信息
    print("Epoch{},loss:{}".format(epoch,loss_all/4))
    train_loss_results.append(loss_all/4)
    loss_all=0

    #测试部分
    total_correct,total_number=0.0,0.0
    for x_test,y_test in test_db:
        y=tf.matmul(x_test,w)+b
        y=tf.nn.softmax(y)
        pred=tf.argmax(y,axis=1)
        pred=tf.cast(pred,dtype=y_test.dtype)
        correct=tf.cast(tf.equal(pred,y_test), dtype=tf.float32)
        correct=tf.reduce_sum(correct)
        total_correct+=int(correct)
        total_number+=x_test.shape[0]
    acc=total_correct/total_number
    test_acc.append(acc)
    print("test acc:",acc)
    print("```````````````````````````````````````")
total_time=time.time()-now_time
print("total_time:",total_time)
#绘制loss曲线
plt.title("Loss function Curve")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.plot(train_loss_results,label="$Loss$")
plt.legend()
plt.show()

#画出ACC曲线
plt.title("Acc Curve")
plt.xlabel("Epoch")
plt.ylabel("Acc")
plt.plot(test_acc,label="$Acc$")
plt.legend()
plt.show()


    

