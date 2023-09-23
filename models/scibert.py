from summarizer import Summarizer
from transformers import *

class scimodel:
    def __init__(self,sci_text):
        model_name = "allenai/scibert_scivocab_uncased"
        custom_config = AutoConfig.from_pretrained(model_name)
        custom_config.output_hidden_states=True
        custom_tokenizer = AutoTokenizer.from_pretrained(model_name)
        custom_model = AutoModel.from_pretrained(model_name, config=custom_config)
        self.model = Summarizer(custom_model=custom_model, custom_tokenizer=custom_tokenizer)
        self.sci_text=sci_text
    def output(self):
        num_sent = 3
        summary = self.model(self.sci_text, num_sentences=num_sent)
        return summary