from simplegmail import Gmail
from simplegmail.query import construct_query
import pandas as pd

class Mailer:

    def __init__(self):
        self.gmail = Gmail()
        self.messages = None

    def get_emails(self, query_params, datafile_path):
        # Get messages that are:
        # Newer than a month old, and are labeled as "PRESS PASS REQUESTS"
        self.messages = self.gmail.get_messages(query=construct_query(query_params))

        # Turns data into pd.DataFrame, then saves as CSV
        df = pd.DataFrame(columns=['To', 'From', 'Subject', 'Date', 'Body'])

        for message in self.messages:
            df.loc[len(df)] = [message.recipient, message.sender, message.subject, message.date, message.plain]

        # Saves a copy as a CSV
        df.to_csv(datafile_path)

        return df
    
    def add_label(self, message, label_name: str):
        # Package label name
        labels = self.gmail.list_labels()
        label = list(filter(lambda x: x.name == label_name, labels))[0]

        # Label message with new label
        message.add_label(label) 
