import matplotlib.pyplot as plt
from matplotlib import gridspec

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow import keras
from tensorflow.keras import layers

# Load training and validation sets
ds_train_ = image_dataset_from_directory(
    '../input/car-color/train_imgs',
    labels='inferred',
    label_mode='categorical',
    image_size=[256, 256],
    batch_size=64,
    shuffle=True,
)
ds_test_ = image_dataset_from_directory(
    '../input/car-color/test_imgs',
    labels='inferred',
    label_mode='categorical',
    image_size=[256, 256],
    batch_size=64,
    shuffle=False,
)

# Define the model
model = keras.Sequential([

    # First Convolutional Block
    layers.Conv2D(filters=16, kernel_size=3, activation="relu", padding='same',
                  # give the input dimensions in the first layer
                  # [height, width, color channels(RGB)]
                  input_shape=[256, 256, 3]),
    layers.BatchNormalization(),
    layers.MaxPool2D(),

    # Second Convolutional Block
    layers.Conv2D(filters=16, kernel_size=3, activation="relu", padding='same'),
    layers.BatchNormalization(),
    layers.MaxPool2D(),

    # Classifier Head
    layers.Flatten(),
    layers.Dense(units=4, activation="softmax"),
])
model.summary()

#train the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    ds_train_,
    #validation_data=ds_valid_,
    epochs=10,
)

plt.plot(history.history['accuracy'], label='accuracy')
#plt.plot(history.history['val_accuracy'], label = 'val_accuracy') # validation accuracy; no validation in this example
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

#test the model
scores = model.evaluate(ds_test_, verbose=0)
print('Accuracy on testing data: {}% \n Error on training data: {} \n'.format(scores[1], 1 - scores[1]))
print(model.predict(ds_test_))

#displaying an image with the detected label

from keras.preprocessing import image
im = image.load_img('/kaggle/input/car-color/test_imgs/Blue/2_00.jpg')
im = np.expand_dims(im, axis=0)
pred = model.predict(im, verbose=0)
print(pred)
classes = ["Black", "Blue", "Green", "No car"]
class_ID = np.argmax(pred)
title = 'predicted ' + classes[class_ID]

plt.imshow(tf.squeeze(im))
plt.axis('off')
plt.title(title)
plt.show()