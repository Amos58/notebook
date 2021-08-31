import tensorflow as tf 
import numpy as np
from sklearn import datasets

#导入数据
x_train = datasets.load_iris().data
y_train=datasets.load_iris().target

#打乱数据集
np.random.seed(42)
np.random.shuffle(x_train)
np.random.seed(42)
np.random.shuffle(y_train)
tf.random.set_seed(42)

#model Sequential
model=tf.keras.models.Sequential([
    tf.keras.layers.Dense(3,activation='softmax',kernel_regularizer=tf.keras.regularizers.l2())
])

#model compile
model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])

#model fit
model.fit(x_train, y_train,batch_size=32,epochs=500,validation_split=0.2,validation_freq=20)

#summary
model.summary()


