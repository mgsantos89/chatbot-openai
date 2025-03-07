from chatbot import Chatbot

def main():
    bot = Chatbot()
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o chatbot.")
            break
        response = bot.ask(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
