# temp = ['abi','avi','richi']
# message = ''
# for i in temp:
#     temp_result = i+'\n'
#     message+=temp_result
#
# print(message)

import requests


url = 'https://www.thedrive.com/wp-content/uploads/images-by-url-td/content/2021/01/Genesis_GV80_Review-3.jpg?quality=85'
response = requests.get(url)
response.content

with open('car.jpg',"wb") as file:
    file.write(response.content)