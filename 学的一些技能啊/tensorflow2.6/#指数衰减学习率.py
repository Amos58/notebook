#指数衰减学习率

import tensorflow as tf
epoch=40
lr_base=0.2
lr_decay=0.99
lr_step=1

for epoch in range(epoch):
    lr=lr_base*lr_decay**(epoch/lr_step)
    with tf.GradientTape() as Tape:
        loss=tf.square(w+1)
    grads=Tape.gradients(loss,w)
    w.assign_sub(lr*grads)