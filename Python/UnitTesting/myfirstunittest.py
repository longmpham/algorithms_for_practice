import unittest
import cap

class TestCap(unittest.TestCase): # boiler plate, call the unittest.TestCase
    
    def test_one_word(self): # create a function to run a test in the class
        text = "python" # actual 
        result = cap.cap_text(text) # actual
        self.assertEqual(result, "Python") # actual, expected
        
    def multiple_words(self):
        text = "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Monty Python")
        
        
if __name__ == "__main__":
    unittest.main() # call unittest.main() to run the unit tests
    