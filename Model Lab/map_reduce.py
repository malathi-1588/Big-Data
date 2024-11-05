
sentences = ["This is a sentence", "This is another sentence", "This is the third sentence"]

def map_function(sentence):
    words = sentence.split()
    mapped_values = []
    for word in words:
        mapped_values.append((word,1))
    return mapped_values

def shuffle_function(mapped_values):
    shuffled_values = {}
    for mapped_value in mapped_values:
        key = mapped_value[0]
        value = mapped_value[1]
        if key in shuffled_values:
            shuffled_values[key].append(value)
        else:
            shuffled_values[key] = [value]
    return shuffled_values

def reduce_function(key,values):
    reduced_key = key
    reduced_value = sum(values)
    return reduced_key,reduced_value

if __name__=="__main__":
    # Sample input data: list of sentences
    # Step 1: Apply map function to each sentences
    mapped_value = []
    for sentence in sentences:
        mapped_value.extend(map_function(sentence))

    # Step 2: Shuffle grouped values by key(word in this case)
    grouped_values = shuffle_function(mapped_value)
    # Step 3: Apply reduce function to each grouped values
    reduced_values = {}
    for key,values in grouped_values.items():
        reduced_key,reduced_value = reduce_function(key,values)
        reduced_values[reduced_key] = reduced_value

    print("Word Frequency: ", reduced_values)
