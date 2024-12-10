def chatbot():
    responses = {
        "ciao": "Ciao! Come posso aiutarti?",
        "come stai?": "Sto bene, grazie! E tu?",
        "qual è il tuo nome?": "Sono un chatbot!",
        "addio": "Addio! Spero di rivederti presto."
    }

    print("Chatbot attivo! Digita 'esci' per terminare.")
    while True:
        user_input = input("Tu: ").lower()
        if user_input == "esci":
            print("Chatbot: Ciao!")
            break
        response = responses.get(user_input, "Non so come rispondere a questa domanda.")
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
