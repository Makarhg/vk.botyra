import vk_api, random
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN = "vk1.a.08fP6ghChGji0NGsKeQrUZqLsvDGHi-pvCoHxO0ODfCqpSAIeRuwkN1oOpz1B1ra2pgoWLBg5ZUtcArpA9t2-PXnsAqizUY-7QW3zDeezc7I7fAy41GfUXCjO7-skNsUmWj3OzFg8epOYKwVAG8tmEzXv_0uF5371XjEAeWw6a88deCz9KbqT2GS5iVN9gDb-K_0rNfgBJYEDPdLvoBbkw"

# Инициализация работы с vk
vk_session = vk_api.VkApi (token = TOKEN)

longpoll = VkLongPoll(vk_session)

# Метод get_api возвращает VkApiMethod(self)
# Позволяет обращаться к методам API как к обычным классам
vk = vk_session.get_api()

vars = ['камень','ножницы','бумага']

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        userText = str(event.text).lower()
        if event.from_user and userText in vars:
            botText = random.choice(vars)

            vk.messages.send(user_id = event.user_id,
                            message = botText,
                            random_id = random.randint(1,100000))
            
            out = None

            if botText == "ножницы":
              if userText == "ножницы":
                  out = "Ничья"
              elif userText == "бумага":
                  out = "Ты проиграл"
              else:
                  out = "Ты выиграл"
            elif botText == "бумага":
                if userText == "бумага":
                    out = "Ничья"
                elif userText == "камень":
                    out = "Ты проиграл"
                else:
                    out = "Ты выиграл"
            elif botText == "камень":
                if userText == "камень":
                    out = "Ничья"
                elif userText == "ножницы":
                    out = "Ты проиграл"
                else:
                    out = "Ты выиграл"
        
            vk.messages.send(user_id = event.user_id,
                            message = out,
                            random_id = random.randint(1,100000))
