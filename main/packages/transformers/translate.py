"""
    pip install transformers
    pip install sentencepiece
    pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/torch_stable.html
    pip install sacremoses
"""

from transformers import MarianMTModel, MarianTokenizer

# Load pre-trained model and tokenizer 
model_name = 'Helsinki-NLP/opus-mt-en-ro'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Text to translate
text = "Hello, how are you?"

# Tokenize the input text
inputs = tokenizer(text, return_tensors="pt")

# Perform translation
translated = model.generate(**inputs)

# Decode translated text
translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

# Output result
print(text)
print(translated_text)

"""
    Hello, how are you?
    Bună, ce mai faci?
"""