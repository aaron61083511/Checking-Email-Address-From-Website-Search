import re
import requests
import pandas as pd
import time

data = pd.read_csv('~Data.csv')
target = data['REQOR_FIRST_NAME'] + '+' + data['REQOR_LAST_NAME']

email_list = []
regex = r"([a-zA-Z0-9_.+-]+@rice.edu)"
counter = 0

for i in range(len(target)):
    if divmod(i, 10)[1] == 0:
        time.sleep(60)
        url = "https://search.rice.edu/?q=" + target[i]
        plain_text = requests.get(url).text
        email = re.findall(regex, plain_text)
        email_list.append(email)
        print(email)
    else:
        url = "https://search.rice.edu/?q=" + target[i]
        plain_text = requests.get(url).text
        email = re.findall(regex, plain_text)
        email_list.append(email)
        print(email)


print(email_list)
