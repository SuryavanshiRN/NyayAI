from core import ask_constitution_bot

user_prompt=input("ENter Query :")
response = ask_constitution_bot(user_prompt)
print("FETCHING AND GENERATING :\n")
print(response)