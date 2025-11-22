#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        # Replace multiple punctuation marks with single ones
        # Then split on sentence-ending punctuation
        value = self.value
        
        # Replace multiple periods/exclamations/questions with single period
        value = re.sub(r'[.!?]+', '.', value)
        
        # Split on the period to get sentences
        sentences = value.split('.')
        
        # Filter out empty strings and strip whitespace
        sentences = [s.strip() for s in sentences if s.strip()]
        
        return len(sentences)
