'''
Due to limited context window ,
It's not possible to get web-based infos 
TODO : Implement a langchain based Google search API 
 
'''
import requests
import re 
def extract_url(prompt):
        return re.findall(r'(https?://\S+)', prompt)
def get_site_data(url):
    dom_bucket=[]
    for items in url:
        page = requests.get(items)
        dom_bucket.append(page.text)
    return dom_bucket
