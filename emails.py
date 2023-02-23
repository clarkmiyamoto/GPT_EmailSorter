from simplegmail import Gmail
from simplegmail.query import construct_query
import pandas as pd

class Mailer:

    def __init__(self):
        self.gmail = Gmail()
        self.messages = None

    def get_emails(self, query_params: dict, datafile_path: str = ''):
        '''
        Args:
        - query_params (dict): Parameters to filter emails.
        - datafile_path (str): Where should these emails save (saves as a CSV).
            Default option:
            datafile_path = '': Defaults to NOT saving a copy.
            
        Returns:
        - df (pd.DataFrame): Messages given in a DataFrame structure.
        '''
        # Get messages according to `query_params`
        self.messages = self.gmail.get_messages(query=construct_query(query_params))

        # Turns data into pd.DataFrame, then saves as CSV
        df = pd.DataFrame(columns=['To', 'From', 'Subject', 'Date', 'Body'])

        for message in self.messages:
            df.loc[len(df)] = [message.recipient, message.sender, message.subject, message.date, message.plain]

        # Saves a copy as a CSV
        if (datafile_path != ''):
            df.to_csv(datafile_path)

        return df
    
    def add_label(self, message: 'Message', label_name: str):
        '''
        Adds a pre-existing label to a message.
        
        Args:
        - message (Message): simplegmail Message object. The email to be labeled.
        - label_name (str): Name of label.
        '''
        # Package label name
        labels = self.gmail.list_labels()
        label = list(filter(lambda x: x.name == label_name, labels))[0]

        # Label message with new label
        message.add_label(label) 
