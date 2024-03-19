#Add error handling for db queries and API requests
from authorize import get_Service
#from db_services import db_connect
import base64
from emailClass import Email

CONST_GMAIL_API = get_Service()



def searchMessages(search):
    
    return(storeMessages((CONST_GMAIL_API.users().messages().list(userId='me', q = search).execute())))



def storeMessages(response):#This function encapsulates emails from searchMessages's response
                            # An array of Email objects is returned
   
    messageArray = []
    body = ""
    

    for mess in response["messages"]:#Error Checking for empty returns
        
        
        rsp = CONST_GMAIL_API.users().messages().get(userId='me', id = mess['id'],).execute()
        
        messData = rsp["payload"]
       
        if 'parts' in messData:

            for p in messData['parts']:

                if p["mimeType"] in ["text/plain"]:
                    body = base64.urlsafe_b64decode(p["body"]["data"]).decode("utf-8")
            header = messData['headers']
            #print(header)
            messageArray.append(Email(mess['id'], header, body))

    return messageArray    
        


                
                

        
    

