# import warnings
# import torch
# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# warnings.filterwarnings('ignore', category=UserWarning)
# warnings.filterwarnings('ignore', message="A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.0")

# class URLClassifier:
#     def __init__(self):
#         model_directory = "model"
#         self.tokenizer = AutoTokenizer.from_pretrained(model_directory)
#         self.model = AutoModelForSequenceClassification.from_pretrained(model_directory)

#     def classify_url(self, user_input):
#         inputs = self.tokenizer(user_input, return_tensors="pt")

#         # Ensure the input tensors are on the correct device (GPU if available)
#         inputs = {key: tensor.to(self.model.device) for key, tensor in inputs.items()}

#         # Perform inference
#         with torch.no_grad():
#             outputs = self.model(**inputs)

#         # Get predicted probabilities
#         probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

#         # Get predicted label (assuming a binary classification)
#         predicted_label = probs.argmax().item()
        
#         if predicted_label == 1:
#             return 'site is not secure'
#         elif predicted_label == 0:
#             return 'site is secure'
#         else:
#             return 'unknown classification'

# # Example usage
# if __name__ == '__main__':
#     model_directory = "model"  # replace with your actual model directory
#     classifier = URLClassifier()
#     user_input = "example input string"  # replace with your actual input string
#     result = classifier.classify_url(user_input)
#     print(result)
# pipeline.py

# import warnings
# import torch
# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# warnings.filterwarnings('ignore', category=UserWarning)
# warnings.filterwarnings('ignore', message="A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.0")

# class URLClassifier:
#     def __init__(self):
#         model_directory = "model"
#         self.tokenizer = AutoTokenizer.from_pretrained(model_directory)
#         self.model = AutoModelForSequenceClassification.from_pretrained(model_directory)

#     def classify_url(self, user_input):
#         inputs = self.tokenizer(user_input, return_tensors="pt")

#         # Ensure the input tensors are on the correct device (GPU if available)
#         inputs = {key: tensor.to(self.model.device) for key, tensor in inputs.items()}

#         # Perform inference
#         with torch.no_grad():
#             outputs = self.model(**inputs)

#         # Get predicted probabilities
#         probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

#         # Get predicted label (assuming a binary classification)
#         predicted_label = probs.argmax().item()

#         if predicted_label == 1:
#             return 'site is not secure'
#         elif predicted_label == 0:
#             return 'site is secure'
#         else:
#             return 'unknown classification'

#     def classify_text(self, text):
#         inputs = self.tokenizer(text, return_tensors="pt")

#         # Ensure the input tensors are on the correct device (GPU if available)
#         inputs = {key: tensor.to(self.model.device) for key, tensor in inputs.items()}

#         # Perform inference
#         with torch.no_grad():
#             outputs = self.model(**inputs)

#         # Get predicted probabilities
#         probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

#         # Get predicted label (assuming a binary classification)
#         predicted_label = probs.argmax().item()

#         if predicted_label == 1:
#             return 'spam'
#         elif predicted_label == 0:
#             return 'not spam'
#         else:
#             return 'unknown classification'

import warnings
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', message="A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.0")

class URLClassifier:
    def __init__(self):
        model_directory = "model"
        self.tokenizer = AutoTokenizer.from_pretrained(model_directory)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_directory)

        # Adjust tokenizer max_length if needed for longer texts
        if isinstance(self.tokenizer.model_max_length, dict) and 'bert' in self.tokenizer.model_max_length:
            self.tokenizer.model_max_length['bert'] = max(self.tokenizer.model_max_length['bert'], 512)
        else:
            self.tokenizer.model_max_length = 512

    def classify_url(self, user_input):
        # Tokenize the input
        inputs = self.tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=512)

        # Ensure the input tensors are on the correct device (GPU if available)
        inputs = {key: tensor.to(self.model.device) for key, tensor in inputs.items()}

        # Perform inference
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Get predicted probabilities
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

        # Get predicted label (assuming a binary classification)
        predicted_label = probs.argmax().item()
        
        if predicted_label == 1:
            return 'site is not secure'
        elif predicted_label == 0:
            return 'site is secure'
        else:
            return 'unknown classification'

    def classify_text(self, text):
        # Tokenize the input text
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

        # Ensure the input tensors are on the correct device (GPU if available)
        inputs = {key: tensor.to(self.model.device) for key, tensor in inputs.items()}

        # Perform inference
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Get predicted probabilities
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

        # Get predicted label (assuming a binary classification)
        predicted_label = probs.argmax().item()

        if predicted_label == 1:
            return 'spam'
        elif predicted_label == 0:
            return 'not spam'
        else:
            return 'unknown classification'

# Example usage
if __name__ == '__main__':
    model_directory = "model"  # replace with your actual model directory
    classifier = URLClassifier()
    user_input = "example input string"  # replace with your actual input string
    result = classifier.classify_url(user_input)
    print(result)
