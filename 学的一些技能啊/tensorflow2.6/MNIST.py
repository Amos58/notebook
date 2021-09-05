import tensorflow as tf 
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras import Model
import matplotlib.pyplot as plt

mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()

#可视化第一个数据
plt.imshow(x_train[0],cmap="gray")
plt.show()
print(x_train.shape)

#实现手写识别

#数据归一化
x_train,x_test=x_train/255.0,x_test/255.0

class MNISTModel(Model):
    def __init__(self):
        super(MNISTModel,self).__init__()
        self.flatten=Flatten()
        self.d1=Dense(128,activation="relu")
        self.d2=Dense(10,activation="softmax")
    
    def call(self,x):
        x=self.flatten(x)
        x=self.d1(x)
        y=self.d2(x)
        return y
    
model=MNISTModel()

#model.compile
model.compile(optimizer="adam",loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),metrics=["sparse_categorical_accuracy"])

#model.fit
model.fit(x_train,y_train,batch_size=32,epochs=5,validation_data=(x_test,y_test),validation_freq=1)

model.summary()
