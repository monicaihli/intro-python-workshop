#
#  Date:  Oct 13 2020
#  File:  case-1_A.py
#  Auth:  Monica Ihli monica@utk.edu


import requests # tell python you want to include functionality of this third party library


my_url = "http://volweb.utk.edu/~mihli1/demos/page1.html"
response_object = requests.get(url=my_url) # request what's at this address, just like if we were using a browser

print("PAGE CONTENT:")
print(response_object.content) # print the contents of the page that we fetched

print("\n\nREQUEST HEADERS\n\n")
print(response_object.headers) # show the headers that were sent with the http response