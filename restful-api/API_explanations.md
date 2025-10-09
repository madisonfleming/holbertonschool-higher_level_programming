HTTP is a protocol that provides a standard for transferring data. The difference between HTTP and HTTPS is the security aspect that HTTPS provides. There is an extra layer of secure data being encrypted while the request is being processed. This means that sensitive data ie passwords are not readable to the public. 

**HTTP Error codes:**  
*100 informational response* – the request was received, continuing process.  
*200 successful* – the request was successfully received, understood, and accepted.  
*300 redirection* – further action needs to be taken in order to complete the request.  
*400 client error* – the request contains bad syntax or cannot be fulfilled   
*500 server error* – the server failed to fulfil an apparently valid request.  

**Common Error Codes:**
**200: Success.** The page requested by the user is successfully fetched and the webpage is displayed to the user.  
**301: Permanent Redirect.** The page requested by the user has been permanently redirected to a different url. The user will be automatically redirected to the new url.   
**302: Temporary Redirect.** The page requested by the user will be temporarily redirected to another webpage.  
**304: Not modified.** This error code is used for caching purposes. the response is so that the user can resume the same cache.   
**400: Bad request.** The user requests a page that the server is unable to understand. the user should not repeat the same request without changes.  
**401: Unauthorised Error.** The request requires the user to be authenticated.   
**403: Forbidden.** The server has understood the request but will not process the request.  
**404: Not found.** When the user requests a url and the server is unable to find it.  

**HTTP Requests/Methods:** 
Requests are the message sent by the user to request data from the server or perform an action. These methods allow users to interact with the database with each serving a specific role in the process.  
**GET**: used to read/retrieve data from a web server. GET returns an HTTP status code of 200 if successful   
**POST**: used to send data (file, data, etc) to the server. POST returns an HTTP status code of 201 if successful.  
**PUT**: used to modify data on the server. Replaces the entire content at the specified location or if there are no matches found, it will create one.  
**PATCH**: similar to PUT, but it will only replace the content you want to update.  
**DELETE**: used to delete data on the server at a specified location.  

**HTTP Response:**
After receiving an interpreting a request, the server responds with an HTTP response message. This includes:  
A Status line, Zero or more Header (General, Response, Entity), An empty line indicating the end of the header fields, Optionally a message-body ie

```python
Status-Line = HTTP-Version SP Status-Code SP Reason-Phrase CRLF
```

**response.json():** returns a JSON object of the result, if result was written in Json otherwise it will raise an error
**response.ok:** returns True if status_code is less than 200 otherwise False.  
**response.status_code:** returns a number that indicates the status ie 200. 
**response.headers:** returns a dictionary of response headers  
**response.content:** returns the content of the response in bytes (Binary Response Content). 
