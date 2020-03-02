from trello import TrelloClient
import requests
import re
import os
import timeit

start = timeit.default_timer()

client = TrelloClient(
    api_key='f0f3c926292bcce056db551471e95247',
    api_secret='3aa90a9a950fec265b7629381e4f9f5d9e432f8a79365ea93f2e027a6b5fb1e5',
    token='c6c08bb22bf251ecf4c978ac63a41e896b4c6cde75f48b4b8a36cfb2e83637f1'
)

board = client.list_boards()[13]
# print(board)
# for list in 
# print(board.open_lists())


list_id = board.open_lists()[0].id
my_list = board.get_list(list_id)

cards = my_list.list_cards()

print(cards)
attachments = []
for card in cards:
    # print(card.name)
    for i in range(1,4):
        attachment_name = card.get_attachments()[i].name
        if attachment_name:
            if "YYY" in attachment_name:
                url=attachment_name
                folder_name = card.name.replace(' ', '-')
                folder_name = re.sub('[^a-zA-Z0-9//-]+', '', folder_name)
                folder_name = folder_name.lower()
                path_folder = '/Users/rupkumar.saha/Desktop/Code/trello-images/' + folder_name
                if not os.path.exists(path_folder):
                    os.mkdir(path_folder) 
                print(url)
                r = requests.get(card.get_attachments()[i].url, allow_redirects=True)
                open(os.getcwd() + '/trello-images/'+ folder_name + '/group1.webp','wb').write(r.content)
                break
            
stop = timeit.default_timer()

print('Time: ', stop - start)  
