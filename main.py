from googlevoice import Voice
from googlevoice.util import input

from GoogleVoiceclass import *

email = input("Enter gmail : ")
password = input("Enter password : ")
gv = GoogleVoice(email, password)

gv.login()

# Enter action

# Show view for action and x to go back

# Perform action and stay in the view until 'x'