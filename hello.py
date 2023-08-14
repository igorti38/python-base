#!/bin/env python3


import os

current_language = os.getenv("LANG", "en_US")

msg = "Hello World"

if current_language == "pt_BR" :
    msg = "Ola, Mundo!"

elif current_language == "it_IT" :
   msg = "Ciao, Mondo!"    

print(msg)

