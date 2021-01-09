# import chatterbot library for the chat bot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# make a set of conversations(Chirag)
convo1 = ["Pardon",
          "Hello", "Hi, Its a pleasure to meet you!",
          "How can you help me?", " I can guide you on exploring places nearby and inside IIT Roorkee! :)"
          "All right!, tell me something about IIT Roorkee","Okay, What do you want to know?"]


convo2 = ["Which is the boys hostel for fresher?","Rajendra Bhawan",
          "Which is the girls hostel for fresher?", "Kasturba",
          "Which place is most favoured for photography?","Main Building",
          "Which Bhawan has the best canteen?","Cautley Bhawan",
          "Which is the best cafe?","Georgia",
          "From where you can get the view of whole IITR1", "",
          "Which is the best place for getting peace?", "",
          "Which is the best place to see snow fall?", "",
          "Which is the highest place nearby Roorkee?", "",
          "What adventurous sports to do in or nearby Roorkee?", "",
          "Is there any National Parks or Wildlife Sanctury inside or nearby Roorkee?", ""]

#historyofiitr
convo3 = ["When was it established?","It was officially established in 1847.",
          "When did it recieved IIT status?","It was given IIT status in 2001."
          "What were the initial names of IITR?","College of Civil Engineering,Thomason College of Civil Engineering,University of Roorkee"]

#transportation
convo4 = ["How do I get to Roorkee?","Well, the nearest airhead to Roorkee is Dehradun, around 70km away, but find Delhi a more convenient airport. Delhi is about 180km away",
          "How can I get a bus to roorkee?","Buses can be obtained either from I.S.B.T. Kashmere Gate, Delhi or from I.S.B.T. Anand Vihar Ghaziabad",
          "Which trains go to Roorkee?","Shatabdi and the JanShatabdi trains go all the way to Dehradun, passing through Roorkee"]

#undefined
convo5 = ["Which banks are inside the campus?","Punjab National Bank and State Bank of India",
          "How is the climate?","You'll see a continental, read extreme, climate. This means that it starts getting cold in about November.",
          "What are the best places to eat?","Royal Palace,Olive & Rustic House,Peppery Herbs,Pizza Hut & Domino’s"]

#places outside campus to visit in roorkee
convo6 = ["places for cinemas?","RR Cinemas and Neelam",
          "fresher's party?","Motel Divine",]


#Rishikesh
covo7 = ["How much distance from IITR?","51.1 km via NH334 and NH34",
             "What are the main features of tourism in Rishikesh","It has numerous yoga centres that attract tourists, ashrams, temple sections of Rama Jhula and Lakshman Jhula, the Ganga Arti performed at dusk at the Triveni Ghat is popular with visitors.",
             "Best places to visit in Rishikesh?", "Lakshman Jhula, Neelkanth Mahadev Temple, The Beatles Ashram, Swarg Ashram, Rajaji National Park, Parmarth Niketan, Kaudiyala, Shivpuri, Jumpin Heights, Narendra Nagar",
             "What total cost it may take to travel tto Rishikesh?", "around RS.6310 for two nights per person with makemytrip"
             "Nearest airport from Rishikesh?", "Jolly Grant Airport in Dehradun that is located at a distance of 35 km",
             "Do Rishikesh have a Railway Station?", "Rishikesh Railway Station (Station Code: RKSH) or Rishikesh Junction is a small railway station which connects through a branch line from Haridwar Railway Station."]







# define a function to train the bot with the training data(Siddharth)
chatbot = ChatBot("Name", read_only=True)

trainer = ListTrainer(chatbot)
trainer1 = ChatterBotCorpusTrainer(chatbot)

trainer.train(convo1)
trainer.train(convo2)
trainer.train(convo3)
trainer.train(convo4)
trainer.train(convo5)

# train additional attributes
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.emotion")




# define a function to get response from the bot (siddharth)

