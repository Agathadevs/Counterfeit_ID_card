import PIL
from PIL import (
                 ImageFont,
                 ImageDraw,
                 Image,
                )
from dataclasses import dataclass
from typing import Type

@dataclass(init=True)
class identity:

    YOUR_NAME:str
    YOUR_BIRTHDAY:str
    YOUR_IMAGE:str
    CARD:str

id_card=identity(YOUR_NAME='cheng',YOUR_BIRTHDAY='95-01-16',YOUR_IMAGE='icon.png',CARD='ID_BASE.png')

def get():

    identity_card=Image.open(id_card.CARD) #(1200,712)
    your_icon=Image.open(id_card.YOUR_IMAGE)
    your_icon_=your_icon.resize((300,300))#(300,300)
    your_icon_.save('youricon.png')
    draw=ImageDraw.Draw(identity_card)
    identity_card.paste(your_icon_,(850,189))
    identity_card.show()    

get()