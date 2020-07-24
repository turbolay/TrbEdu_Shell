# Basic wrapper for requests
# Wrappers like this force error handling and return homogenization
# If a function of the base module is not wrapped, it's still accessible, in that case through self.pyRequests

import requests as pyRequests

class RequestsWrapper():
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Usefull to make non-wrapped functions available from other class
    pyRequests = pyRequests

    def exec(self,requestType,url,params=()):
        if(requestType == "GET"):
            try:
                results = pyRequests.get(url)
                return (results.status_code,results.text)
            except:
                return (-1,"ERROR DURING API CALL")
                
        return(-2,"REQUEST TYPE NOT KNOWS")