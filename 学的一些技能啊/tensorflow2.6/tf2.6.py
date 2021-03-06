### 前向传播
import tensorflow as tf

w=tf.Variable(tf.constant(5,dtype=tf.float32))
lr=0.2
epoch=40

for epoch in range(epoch):
    with tf.GradientTape() as tape:# 梯度计算过程
        loss=tf.square(w+1)
    grads=tape.gradient(loss,w)

    w.assign_sub(lr*grads)
    print("After %s epoch,w is %f, loss is %f"%(epoch,w.numpy(),loss))
