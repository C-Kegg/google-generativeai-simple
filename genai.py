import subprocess

subprocess.run(["pip", "install", "google"])
subprocess.run(["pip", "install", "google-generativeai"])

import google.generativeai as genai

class Chat:
   def __init__(self, assistant_name, user_name, api_key, custom_commands: str = ""):
       self.assistant_name = assistant_name
       self.user_name = user_name
       genai.configure(api_key=api_key)

       # Set up the model
       self.generation_config = {
           "temperature": 0.9,
           "top_p": 1,
           "top_k": 1,
           "max_output_tokens": 2048,
       }

       self.safety_settings = [
           {
               "category": "HARM_CATEGORY_HARASSMENT",
               "threshold": "BLOCK_MEDIUM_AND_ABOVE"
           },
           {
               "category": "HARM_CATEGORY_HATE_SPEECH",
               "threshold": "BLOCK_MEDIUM_AND_ABOVE"
           },
           {
               "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
               "threshold": "BLOCK_MEDIUM_AND_ABOVE"
           },
           {
               "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
               "threshold": "BLOCK_MEDIUM_AND_ABOVE"
           },
       ]

       self.model = genai.GenerativeModel(model_name="gemini-pro",
                                          generation_config=self.generation_config,
                                          safety_settings=self.safety_settings)

       self.convo = self.model.start_chat(history=[])
       self.run(f"Adopt the name {assistant_name}. I am {user_name}.\nIf the following line has no text, ignore this line's content. Follow the custom instructions on the next line:\n{custom_commands}")

   def run(self, input):
       self.convo.send_message(input)
       response = self.convo.last.text
       return response

def run(self, input: str, prompt="default", defaults: dict = {}) -> str:
    """Run a basic request to the Google Generative AI model.
    Params: 
        input: str = Required. Your query/request for the model
        prompt: str = This is used to rapidly train the model
    Returns:
        t: str = The model's response
    """
    if defaults == {}:
        generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }

        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        ]

        model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    if input == "Terminate(\"program\")":
        print("Terminating program.")
        exit()
    if prompt == "default":
        prompt = """Answer the following query to the best of your ability""" # This essentially trains the model
    else:
        prompt += "\ninput: " + input + "\noutput:"""""""
    prompt_parts: list = [prompt]
    response = model.generate_content(prompt_parts)
    t = response.text
        
    return t
