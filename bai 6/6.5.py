class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

input_data = 'hello .py'

reverser = StringReverser(input_data)

output_data = reverser.reverse_words()
print(output_data)  
