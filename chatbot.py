# Install ChatterBot and ChatterBot Corpus
# pip install chatterbot chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
fitness_chatbot = ChatBot('FitnessBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(fitness_chatbot)

# Train the chatbot on the English language data
trainer.train('chatterbot.corpus.english')

# Define responses for fitness and wellness-related queries
fitness_responses = {
    'fitness_tips': 'Remember to incorporate both cardio and strength training exercises into your routine.',
    'healthy_diet': 'A balanced diet with plenty of fruits, vegetables, and lean proteins is crucial for overall health.',
    'mental_wellness': 'Taking breaks and practicing mindfulness can help improve mental well-being.',
    'goal_setting': 'Set realistic and achievable fitness goals to stay motivated.',
    'default': 'I m here to help with fitness and wellness questions. Ask me anything!'
}

# Function to get a response from the fitness chatbot
def get_fitness_response(user_input):
    response = fitness_chatbot.get_response(user_input)

    # Map specific queries to custom responses
    if 'fitness tips' in user_input:
        return fitness_responses['fitness_tips']
    elif 'healthy diet' in user_input:
        return fitness_responses['healthy_diet']
    elif 'mental wellness' in user_input:
        return fitness_responses['mental_wellness']
    elif 'goal setting' in user_input:
        return fitness_responses['goal_setting']
    else:
        return fitness_responses['default']

# Example usage
user_input = input("You: ")
while user_input.lower() != 'exit':
    bot_response = get_fitness_response(user_input)
    print(f"FitnessBot: {bot_response}")
    user_input = input("You: ")
