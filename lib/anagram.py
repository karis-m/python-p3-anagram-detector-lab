class Anagram:
    list = []
    def __init__(self, word):
        self.word = word
        self.list.append(word)
        
    
    def match(self):
        pass

    def __repr__(self) -> str:
        return f'{self.list}'

# your code goes here!