import openai

# create a new API key in OpenAI and paste it here
class Chatbot:
    def __int__(self):
        # create a new API key in OpenAI and paste it here
        openai.api_key ="your_key"

    def get_response(self, user_input):
        responds = openai.Completion.create(
            egine = "text-davinci-003",
            prompt = user_input,
            # tokens are words
            max_tokens=4000,
            # low temperature is more accurate answers but less diverse, more temperature is the opposite
            temperature=0.5
        )