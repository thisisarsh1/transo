import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense

# Sample parallel corpus (replace this with a larger dataset)
english_sentences = ["Hello.", "How are you?", "What is your name?"]
marathi_sentences = ["नमस्कार.", "तुमचं कसं आहे?", "तुमचं नाव काय आहे?"]

# Tokenize sentences
english_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
english_tokenizer.fit_on_texts(english_sentences)
english_seq = english_tokenizer.texts_to_sequences(english_sentences)
english_max_len = max(len(seq) for seq in english_seq)

marathi_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
marathi_tokenizer.fit_on_texts(marathi_sentences)
marathi_seq = marathi_tokenizer.texts_to_sequences(marathi_sentences)
marathi_seq = tf.keras.preprocessing.sequence.pad_sequences(marathi_seq, maxlen=4, padding='post')  # Adjust sequence length
marathi_max_len = 4

# Pad sequences
english_seq = tf.keras.preprocessing.sequence.pad_sequences(english_seq, maxlen=english_max_len, padding='post')

# Define the model
embedding_dim = 256
units = 512

encoder_inputs = Input(shape=(english_max_len,))
encoder_embedding = tf.keras.layers.Embedding(len(english_tokenizer.word_index) + 1, embedding_dim)(encoder_inputs)
encoder_lstm = LSTM(units, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding)
encoder_states = [state_h, state_c]

decoder_inputs = Input(shape=(4,))  # Adjust the input shape
decoder_embedding = tf.keras.layers.Embedding(len(marathi_tokenizer.word_index) + 1, embedding_dim)(decoder_inputs)
decoder_lstm = LSTM(units, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=encoder_states)
decoder_dense = Dense(len(marathi_tokenizer.word_index) + 1, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model (replace this with a larger dataset and more epochs)
model.fit([english_seq, marathi_seq[:, :-1]], np.expand_dims(marathi_seq[:, 1:], -1), epochs=50, batch_size=1)

# Example translation
def translate(input_sentence):
    input_sequence = english_tokenizer.texts_to_sequences([input_sentence])
    input_sequence = tf.keras.preprocessing.sequence.pad_sequences(input_sequence, maxlen=english_max_len, padding='post')
    prediction = model.predict([input_sequence, np.zeros((1, 4))])
    predicted_sequence = np.argmax(prediction, axis=-1)
    translated_sentence = ' '.join([marathi_tokenizer.index_word[idx] for idx in predicted_sequence[0] if idx > 0])
    return translated_sentence

# Test the translation
test_sentence = "Hello, how are you?"
translation = translate(test_sentence)
print(f"Input: {test_sentence}")
print(f"Translation: {translation}")
