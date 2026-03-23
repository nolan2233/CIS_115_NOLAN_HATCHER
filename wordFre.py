#this program uses func and frequency to count each word as it appears in the sentence. 
def word_frequency(sentence):
    words = sentence.split()

    frequency= {}

    for word in words:
        word = word.lower()

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

sentence = input("Enter your sentence: ")
print(word_frequency(sentence))