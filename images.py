import requests
import json
import os
import urllib.request

user_query : str = input("Enter your query")
api_key = None #Enter your api key here
if api_key == None:
    print("API key not found! Please edit the api_key variable with your api key.")
    quit()
url = "https://bing-image-search1.p.rapidapi.com/images/search"
user = ""
querystring = {"q":user_query,"count": 30} #Change the count variable to the number of images you'd like to download
flag = False
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
    }

def download_images(img_path = "D:/TrainingImages/" ):
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_obj = json.loads(response.content)
    json_formatted = json.dumps(json_obj, indent=2)
    # print(json_formatted)
    k = 0
    for i in json_obj["value"]:
        k = k + 1
        new_path  = img_path + str(k)+".jpg"
        url_img = str(i["contentUrl"])
        try:
            urllib.request.urlretrieve(url_img, new_path)
        except Exception:
            print("Missed a picture!")


def dir_init(d_path = 'D:/', dir_name = 'TrainingImages'):
    global user, flag
    path = os.path.join(d_path, dir_name)
    try:
        os.mkdir(path)
    except OSError as error:
        if os.path.isdir(path):
            print("The directory already exists...")
            user = input("Do you want to proceed with the download? (y/n)")
            flag = True
        else:
            print("Sorry! Something went wrong")
    if not user=="n" :
        download_images(str(d_path+dir_name+"/"))

dir_init()
if flag and user == "y":
    print("done")
elif flag:
    flag = False
    user = input("Do you want to make a new directory?(y/n)")
    if user == "y":
        user_dir_change = input("Would you like to change the path?(y/n)")
        if user_dir_change == "y":
            new_path = input("Enter your new path")
            flag = True
        new_dir = input("Enter your new directory name")
        if flag:
            dir_init(d_path=str(new_path), dir_name= str(new_dir))
        else:
            dir_init(dir_name=str(new_dir))
    else:
        print("Exited")
