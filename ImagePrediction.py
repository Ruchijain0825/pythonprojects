
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 1. Load dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()


class_names = [
    "Airplane", "Automobile", "Bird", "Cat", "Deer",
    "Dog", "Frog", "Horse", "Ship", "Truck"
]


X_train = X_train / 255.0
X_test = X_test / 255.0


model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(32, 32, 3)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])


model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


model.fit(
    X_train,
    y_train,
    epochs=10,
    validation_data=(X_test, y_test)
)


loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)


index = 10
image = X_test[index]

prediction = model.predict(
    np.expand_dims(image, axis=0),
    verbose=0
)

predicted_class = np.argmax(prediction[0])

print("Predicted:", class_names[predicted_class])
print("Actual:", class_names[int(y_test[index][0])])


plt.imshow(image)
plt.title(class_names[predicted_class])
plt.axis("off")
plt.show()
