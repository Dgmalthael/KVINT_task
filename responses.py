#state mashine
from transitions import Machine
#auto answers and states for state machine
automatic_answers = ['What is the size of your pizza?Small or Large?', 'What is the payment method?', 'Do you want a',
                     'Thank you for your order!']
errror_messages = ["I don't understand you", "What do you mean?", "Sorry, Can you write again?"]

class Matter(object):
    pass


lump = Matter()
#adding changes of states
transitions = [
    {'trigger': 'pizza_size', 'source': automatic_answers, 'dest': automatic_answers[1]},
    {'trigger': 'payment_method', 'source': automatic_answers, 'dest': automatic_answers[2]},
    {'trigger': 'thank', 'source': automatic_answers, 'dest': automatic_answers[3]},
    {'trigger': 'turn_back', 'source': automatic_answers, 'dest': automatic_answers[0]},

]
machine = Machine(model=lump, states=automatic_answers, transitions=transitions, initial=automatic_answers[0])
# answer choice
size = ['small', 'large']
payment = ['cash', 'card']
y_n = ['yes', 'no']



