import openai,os,sys,time


user_input = print("pls insert")



def model_changename():
    print("Chose your model:davinci curie babbage ada ")
    model_input = input()
    if model_input == "davinci":
        print("save,pls reinsert")
        return  "text-davinci-003"
    #
    elif model_input == "curie":
    #     model().changename()
         print("save,pls reinsert")
         return "text-curie-001"
    elif model_input == "babbage":
    #     model().changename("text-babbage-001")
         print("save,pls reinsert")
         return "text-babbage-001"
    elif model_input == "ada":
         print("save,pls reinsert")
    #     model().changename()
         return "text-ada-001"
    elif model_input == "code-davinci":
    #     model().changename()
         print("save,pls reinsert")
         return "code - davinci - 002"

    else:
         return print("pls reinsert question OR Change model")

    #stanndname ="text-davinci-003"



# 开始循环
a = "text-davinci-003"
while user_input != "quit":
    # 请求输入

    user_input = input()



    if user_input =="change model":

        a = model_changename()

    elif user_input !="quit"or"change model":
        prompt = user_input
        openai.api_key = "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"

        start_time= time.time()
        completions = openai.Completion.create(
            engine =a,
            #text-davinci-003
            #text-curie-001
            #text - babbage - 001
            #text - ada - 001

            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop =None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        print (message)
        end_time = time.time()
        print("This Conversation Cost",end_time-start_time,"Seconds！")
        print("Model Name；",a)
        print ("pls reinsert")
    elif user_input == "quit":
        print("Goodbye!")

# 退出循环
print("Exiting loop")




