import csv, requests, json

with open('data.txt', 'w') as outfile:
    for i in range(1,732):
        string = "https://superheroapi.com/api.php/access_token/" + str(i)
        response = requests.get(string)
        jsondata = response.json()
        json.dump(jsondata, outfile, indent=4)
        print(i)