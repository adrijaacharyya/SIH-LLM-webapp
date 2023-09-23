from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class t5model:
    def __init__(self,paper_text):
        self.tokenizer = AutoTokenizer.from_pretrained("t5-small")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
        self.paper_text = paper_text
    def output(self):
        # Tokenize the input paper
        input_ids = self.tokenizer.encode("summarize: " + self.paper_text, return_tensors="pt", max_length=1024, truncation=True)

        # Generate the summary
        summary_ids = self.model.generate(input_ids, max_length=2000, min_length=500, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode and print the generated summary
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    
