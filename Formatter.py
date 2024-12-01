class Formatter():
    def leetify(self, input_string):
        leet_dict = {
            'A': '4', 'E': '3', 'G': '6', 'I': '1', 'O': '0', 'S': '5', 'T': '7',
            'a': '4', 'e': '3', 'g': '6', 'i': '1', 'o': '0', 's': '5', 't': '7'
        }
        
        return ''.join(leet_dict.get(char, char) for char in input_string)