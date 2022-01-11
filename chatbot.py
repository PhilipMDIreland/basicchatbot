
# Just an example based on questions about house, uniform, and length of schools.

def chat_bot():
    house_position = -1
    uniform_position = -1
    length_position = -1
    schools_position = -1
    where_position = -1
    print("Welcome, New Boy")
    question = input("What is your question regarding Eton life?")
    question = question.lower()
    house_position = question.find("house") 
    uniform_position = question.find("uniform")
    length_position = question.find("length")
    schools_position = question.find("school")
    where_position = question.find("where")
    if house_position > -1:
        print("That is a great question, please do chat to your Housemater about that as he will know and can give more detail than I can.")
    elif uniform_position > -1:
        print("You need to wear your uniform to all but sports schools. The uniform consists of item one, item two, item three etc.")
    elif length_position > -1 and schools_position == -1:
        print("I think you are asking about the school day. It mostly starts at 0900 and finishes at 1800, but that is only schools.")
    elif length_position >-1 and schools_position >-1:
        print("The length of each school is 40 minutes.")
    elif where_position > -1:
        print("You can find the school map at www.etoncollege.com/map/")
    else:
        print("I am not too sure about that one, ask your Dame!")

chat_bot()
