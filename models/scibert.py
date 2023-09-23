from summarizer import Summarizer
from transformers import *

def load_model():
    # Load model, model config and tokenizer via Transformers
    model_name = "allenai/scibert_scivocab_uncased"
    custom_config = AutoConfig.from_pretrained(model_name)
    custom_config.output_hidden_states=True
    custom_tokenizer = AutoTokenizer.from_pretrained(model_name)
    custom_model = AutoModel.from_pretrained(model_name, config=custom_config)
    model = Summarizer(custom_model=custom_model, custom_tokenizer=custom_tokenizer)
    return model

model = load_model()
num_sent = 3

sci_txt=''''''

summary = model(sci_txt_1, num_sentences=num_sent)