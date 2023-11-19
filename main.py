import PIL
from PIL import (
    ImageFont,
    ImageDraw,
    Image,           
)
import yaml
try:
    with open('db\locate.yaml','r',encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
except Exception as e:
    print(e)
                
from dataclasses import dataclass
from typing import Type

@dataclass(init=True)
class identity:
    '''indentity database'''
    YOUR_NAME:str
    YOUR_BIRTHDAY:str
    YOUR_IMAGE:str
    CARD:str
    ID_card_font_size:str
    Date_of_issue:str
'''change your info here'''
id_card=identity(YOUR_NAME='ditisrmel',
                 YOUR_BIRTHDAY='99-04-14',
                 YOUR_IMAGE='icon.png',
                 CARD='ID_BASE.png',
                 ID_card_font_size="108-05-10-北市",
                 Date_of_issue="F123456789")

def get():

    identity_card=Image.open(id_card.CARD) #(1200,712)
    your_icon=Image.open(id_card.YOUR_IMAGE)
    your_icon_=your_icon.resize((300,300))#(300,300)
    your_icon_.save('youricon.png')
    draw=ImageDraw.Draw(identity_card)

    font=ImageFont.truetype('edukai-4.0.ttf',size=60)
    font_second=ImageFont.truetype('edukai-4.0.ttf',size=30)
    font_third=ImageFont.truetype('edukai-4.0.ttf',size=60)

    draw.text((200,350),text=id_card.YOUR_NAME,fill='black',font=font)
    draw.text((307,501),text=id_card.YOUR_BIRTHDAY.split('-')[0],fill='black',font=font)
    draw.text((445,501),text=id_card.YOUR_BIRTHDAY.split('-')[1],fill='black',font=font)
    draw.text((575,501),text=id_card.YOUR_BIRTHDAY.split('-')[2],fill='black',font=font)

    draw.text((260,645),text=id_card.ID_card_font_size.split('-')[0],fill='black',font=font_second)
    draw.text((341,645),text=id_card.ID_card_font_size.split('-')[1],fill='black',font=font_second)
    draw.text((416,645),text=id_card.ID_card_font_size.split('-')[2],fill='black',font=font_second)
    draw.text((534,641),text=id_card.ID_card_font_size.split('-')[3],fill='black',font=font_second)

    draw.text((858,629),text=id_card.Date_of_issue,fill='black',font=font_third)

    identity_card.paste(your_icon_,(850,189))
    identity_card.show()    
    identity_card.save('new_id.png')

if __name__=="__main__":
    get()