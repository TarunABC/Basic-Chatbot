import json
from difflib import get_close_matches

def load_knowledge_base(file_path ):
    with open (file_path, 'r') as file:
        data = json.load(file)

    return data

def save_knowledge_base(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = 2)

def find_best_matches(user_question, questions):
    matches = get_close_matches(user_question, questions, n = 1, cutoff = 0.6)
    return matches[0] if matches else None

def get_answer_for_questions(question, knowledge_base):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]



def chatbot():

    knowledge_base = load_knowledge_base('/Users/tarunrockzz100/Desktop/Hackindia2025/Knowledge_base.json')
    
    while True:
        user_input = input("You : ")

        if user_input.lower() == "quit":
            break

        best_match = find_best_matches(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer = get_answer_for_questions(best_match, knowledge_base)
            print(f'bot: {answer}')
    
        else:
            print("Bot : I don/'t know the answers can you teach me ? ")
            new_answer = input("Enter the answer or skip : ")

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question" : user_input, "answer" : new_answer})
                save_knowledge_base('/Users/tarunrockzz100/Desktop/Hackindia2025/Knowledge_base.json', knowledge_base)
                print("Bot : Thank you")

if __name__ == '__main__':
    chatbot() 





    
