import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

#------------------------------------------------------------------------
input_text = """
用户：你好，你是？
ChatGPT：你好，我是 ChatGPT，是一个由 OpenAI 训练的大型语言模型, 旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。
"""

one_turn = """

用户：{user_input}
ChatGPT："""

print(input_text)

while True:


    user_input = input("用户：")
    input_text = input_text + one_turn.format(user_input=user_input)
    
    print("ChatGPT：",end = '', flush=True)
   
    ans = "" 
    for res in openai.Completion.create(
      model="text-davinci-003",
      prompt=input_text,
      temperature=0.7,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.5,
      stop=["用户："],
      stream=True,
    ) :
        print(res["choices"][0]["text"],end = '', flush=True)
        ans = ans+res["choices"][0]["text"]
 
    print('\n')
    input_text = input_text + ans
    
