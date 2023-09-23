import torch, sentencepiece
from transformers import T5Tokenizer, T5ForConditionalGeneration



class grammar:
    def __init__(self,input_text):
        model_name = 'deep-learning-analytics/GrammarCorrector'
        self.torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name).to(self.torch_device)
        self.num_beams=10
        self.input_text = input_text
        self.num_return_sequences = 3

    def output(self):
        batch = self.tokenizer([self.input_text],truncation=True,padding='max_length',max_length=64, return_tensors="pt").to(self.torch_device)
        translated = self.model.generate(**batch,max_length=64,num_beams=self.num_beams, num_return_sequences=self.num_return_sequences, temperature=1.5)
        tgt_text = self.tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text