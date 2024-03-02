


class Email:
    subject = ""
    sender = ""
    receiver = ""
    message = ""
    id = 0
    header = []
    
    def __init__(self, id, header, message):
        self.id = id
        self.header = header
        self.message = message

        for entry in header:
            if entry['name'] == "From":
                self.sender = entry['value']
            if entry['name'] == "To":
                self.receiver = entry['value']
            if entry['name'] == "Subject":
                self.subject = entry['value']
        print( "From: "+ self.sender)








