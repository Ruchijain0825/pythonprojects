
import numpy as np
import tensorflow as tf


text = """
hello world
hello python
hello machine learning
hello world
hello python
"""


chars = sorted(set(text))

char_to_id = {
    char: i for i, char in enumerate(chars)
}

id_to_char = {
    i: char for i, char in enumerate(chars)
}

vocab_size = len(chars)

# 3. Convert text into numbers
data = np.array([
    char_to_id[c] for c in text
])


X = []
y = []

for i in range(len(data) - 3):

    X.append(data[i:i+3])

    y.append(data[i+3])

X = np.array(X)
y = np.array(y)


model = tf.keras.Sequential([

    tf.keras.layers.Embedding(
        vocab_size, 16
    ),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(
        32, activation="relu"
    ),

    tf.keras.layers.Dense(vocab_size)

])


model.compile(
    optimizer="adam",

    loss=tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True
    ),

    metrics=["accuracy"]
)


model.fit(
    X,
    y,
    epochs=100,
    verbose=0
)

print("Training completed!")

def generate_text(start, length=30):

    result = start

    for _ in range(length):

        last_three = result[-3:]

        input_data = np.array([[
            char_to_id[c] for c in last_three
        ]])

        prediction = model.predict(
            input_data,
            verbose=0
        )

        next_id = np.argmax(prediction[0])

        next_char = id_to_char[next_id]

        result += next_char

    return result



print(generate_text("hel", 30))

