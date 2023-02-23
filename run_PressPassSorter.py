from emails import Mailer
import language_processing

import pandas as pd

'''
Sort email for Press Passes

Requirements
1. Mentions city they want to shoot in
2. They have some kind of portfolio / instagram
3. Wether or not they are press
'''

def check_criteria(df):
    # Initalize NLP
    nlp = NLP()
    df['contains_place'] = [nlp.contains_place(text) for text in df['Body']]
    df['contains_portfolio'] = [nlp.contains_portfolio(text) for text in df['Body']]

    df['is_formatted_correctly'] = df[columns].all(axis=1)
    correctly_formatted_rows = df.index[df['is_formatted_correctly']].tolist()

    return df, correctly_formatted_rows
    

if __name__ == '__main__':
    query_params = {
            "newer_than": (3, "month"),
            "labels":["PRESS PASS REQUESTS"]
        }
    datafile_path = './emails.csv'
    
    # Get all press pass email
    mail = Mailer()
    df = mail.get_emails(query_params, datafile_path = datafile_path)
        
    # In DataFrame, notes which emails meet criteria
    df, correct_ones = check_criteria(df)

    # Updates GMail label to "VERIFIED" if meeting critiera
    for idx in correct_ones:
        mail.add_label(mail.messages[idx], "VERIFIED")
    









