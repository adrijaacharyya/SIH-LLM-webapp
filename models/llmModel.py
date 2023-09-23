from transformers import BartForConditionalGeneration, BartTokenizer
import torch 


class BartModel:
    def __init__(self, input_text):
        # Load the pre-trained BART model and tokenizer
        model_name = "facebook/bart-large-cnn"
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)
        self.input_text = input_text
# Tokenize the input text
    def output(self):
        inputs = self.tokenizer(self.input_text, return_tensors="pt", max_length=1024, truncation=True)
        # Generate the summary
        with torch.no_grad():
            summary_ids = self.model.generate(
                inputs["input_ids"],
                num_beams=4,  # Adjust as needed for the desired summary length and quality
                length_penalty=2.0,  # Adjust as needed for the desired summary length and quality
                min_length=200,  # Minimum length of the summary
                max_length=1000,  # Maximum length of the summary
                early_stopping=True,
            )

        # Decode the generated summary
        generated_summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Print the generated summary
        return generated_summary