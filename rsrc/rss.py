from bs4 import BeautifulSoup
from bs4.element import Comment
import pandas as pd
import numpy as np
import requests

final_data = pd.DataFrame()
for i in range(10):

    url = "https://itunes.apple.com/us/rss/customerreviews/page={}/id=284882215/sortBy=mostrecent/xml".format(i+1)

    xml_data = requests.get(url).content

    soup = BeautifulSoup(xml_data, "xml")

    # Find all text in the data
    texts = str(soup.findAll(text=True)).replace('\\n','')

    #Find the tag/child
    child = soup.find("entry")

    Title = []
    content_type = []
    updated = []
    rating = []
    user_name = []

    while True:
        try:
            updated.append(" ".join(child.find('updated')))
        except:
            updated.append(" ")

        try:
            Title.append(" ".join(child.find('title')))
        except:
            Title.append(" ")

        try:
            content_type.append(" ".join(child.find('content')))
        except:
            content_type.append(" ")

        try:
            rating.append(" ".join(child.find('im:rating')))
        except:
            rating.append(" ")

        try:
            user_name.append(" ".join(child.find('name')))
        except:
            user_name.append(" ")

        try:
            # Next sibling of child, here: entry
            child = child.find_next_sibling('entry')
        except:
            break

    data = []
    data = pd.DataFrame({"updated":updated,
                                    "Title":Title,
                                    "content_type":content_type,
                                    "rating":rating,
                                    "user_name":user_name})
    final_data = final_data.append(data, ignore_index = True)
