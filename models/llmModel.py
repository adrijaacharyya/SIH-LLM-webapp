from transformers import BartForConditionalGeneration, BartTokenizer
import torch 


class BartModel:
    def __init__(self, input_text):
        # Load the pre-trained BART model and tokenizer
        model_name = "facebook/bart-large-cnn"
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)
        self.input_text = input_text

# # Define your input text
# input_text = """
# Friction in bilateral relations won’t affect investment flows: FinMin official

# According to government data, bilateral trade between India and Canada has grown significantly in recent years, reaching $8.16 billion in 2022-23. (Mint)

# NEW DELHI : The diplomatic row over the killing of a Sikh leader in British Columbia will not affect the flow of Canadian investments into India, a senior finance ministry official said on Tuesday.

# “Firstly, Western nations have invested in markets they have found promising irrespective of political or diplomatic differences. One example is China. Secondly, Canada’s pension fund and other investments into India are small and are not critical to the Indian economy," said the official, who spoke on condition of anonymity.

# Experts also endorsed the government’s view, while some highlighted the absence of a trade deal between the two nations as a factor that could pose unpredictability for businesses. “The India-Canada relationship is based on mutual benefits, complementarity in trade and deep people-to-people connect; hence, it will not be impacted by the current diplomatic impasse," said Ajay Srivastava, founder of the Global Trade Research Initiative (GTRI), a think tank and consulting firm.

# “Both India and Canada trade in complementary products and do not compete on similar products. Hence, the trade relationship will continue to grow and not be affected by day-to-day events," he added.

# Srivastava pointed out that two major investment sources from Canada—pension funds and remittances from people of Indian origin—will continue to flow, as the funds typically invest for the long term based on the intrinsic economic strength of the country, and Indians abroad will continue to send money back home.

# According to government data, bilateral trade between India and Canada has grown significantly in recent years, reaching $8.16 billion in 2022-23. India’s exports ($4.1 billion) to Canada include pharmaceuticals, gems and jewellery, textiles, and machinery, while Canada’s exports to India at $4.06 billion include pulses, timber, pulp and paper, and mining products.

# Canadian pension funds have invested over $45 billion in India, making it the world’s fourth-largest recipient of Canadian foreign direct investment (FDI) by the end of 2022. The top sectors for Canadian pension fund investment in India include infrastructure, renewable energy, technology and financial services.

# According to the Canadian Bureau for International Education (CBIE), Indian students contributed $4.9 billion to the Canadian economy in 2021. Indian students are the largest international student group in Canada, accounting for 20% of all international students in 2021. A finance ministry spokesperson did not immediately respond to an email seeking comments.

# A second government official, who also spoke on condition of anonymity, noted that cross-border investments are unlikely to be significantly affected, as investments are driven by commercial considerations.

# Canadian investors are unlikely to pause their activity in the country, said a fund manager, also on condition of anonymity. “The funds have more at stake in the Indian market, given there aren’t many investment destinations for deployment of capital of that size," the person said.

# Funds backed by the Canadian government, such as Ontario Teachers’ Pension Plan (OTPP), Caisse de dépôt et placement du Québec (CDPQ) and Canada Pension Plan Investment Board (CPPIB) are the most active investors in the country.

# A CPPIB spokesperson declined to comment. Spokespersons of OTPP and CDPQ didn’t respond to emails seeking comments.

# Negotiations between India and Canada for a free trade agreement, which resumed after a decade, recently came to a halt due to political differences. The absence of trade agreements can bring unpredictability.

# In general, existing investments get impacted by various factors, which include whether both countries have investment agreements, terms and conditions of double taxation treaties, and if the countries allow FDI, said Arpita Mukherjee, professor at the Indian Council for Research on International Economic Relations (ICRIER).

# “The contours or the quality of the agreements between countries give the level of protection for investors. If you analyse business deals and investments, each deal/investment is different depending on their terms and conditions," Mukherjee said.

# “While investments are dependent on commercial decisions, we have a predictable situation or stability with trade agreements," she added.

# Some economists think Canada’s withdrawal from the FTA could have broader implications. The withdrawal is serious given that all major economies are eying the Indian market, said Biswajit Dhar, a professor at the Centre for Economic Studies and Planning, Jawaharlal Nehru University. “And he is under tremendous political pressure at home. I think this could have a broad impact. As far as (foreign) investors are concerned, they have their own logic. But if the home government is not very friendly, then normally, there is an impact on investment," Dhar added.

# Ravi Dutta Mishra and Gireesh Chandra Prasad in Delhi contributed to this story.

# """
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
    

input_text = '''Canadian Prime Minister Justin Trudeau has said that the shared evidence that Indian government agents were potentially involved in the murder of a Sikh separatist leader in British Columbia with New Delhi weeks ago.

Trudeau added, "We are there to work constructively with India. We hope that they engage with us so that we can get to the bottom of this very serious matter".

Earlier this week, the Canadian Prime Minister said they had credible intelligence linking Indian government agents to the murder in June of Khalistani separatist Hardeep Singh Nijjar.

Trudeau said the intelligence included communications of Indian officials present in Canada, adding that some of the information was provided by an unidentified ally in the Five Eyes alliance.

Five Eyes is an intelligence-sharing network that includes the US, the UK, Canada, Australia and New Zealand.

However, Trudeau has not provided any details about what Canada's spy agencies have collected.

Meanwhile, US Secretary of State Antony Blinken said the United States wanted to see "accountability" over the killing.'''

br = BartModel(input_text)
print(br.output())