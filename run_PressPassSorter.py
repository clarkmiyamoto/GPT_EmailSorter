from emails import Mailer
from language_processing import NLP

import pandas as pd
from tqdm import tqdm

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
    df['contains_place'] = [nlp.contains_place(text) for text in tqdm(df['Body'])]
    df['contains_portfolio'] = [nlp.contains_portfolio(text) for text in tqdm(df['Body'])]

    df['is_formatted_correctly'] = df[['contains_place', 'contains_portfolio']].all(axis=1)
    correctly_formatted_rows = df.index[df['is_formatted_correctly']].tolist()

    return df, correctly_formatted_rows
    

if __name__ == '__main__':
    query_params = {
            "newer_than": (3, "month"),
            "labels":["PRESS PASS REQUESTS"]
        }
    datafile_path = './emails.csv'
    verified_label = 'VERIFIED'

    
    # Get all press pass email
    print('Getting mail...')
    mail = Mailer()
    df = mail.get_emails(query_params, datafile_path = datafile_path).astype(str)
    print('Got mail!')

    # In DataFrame, notes which emails meet criteria
    print('Checking criteria...')
    df, correct_ones = check_criteria(df)
    print('Criterias all checked')

    # Updates GMail label to `verified_label` if meeting critiera
    print('Relabbeling Emails')
    for idx in tqdm(correct_ones):
        mail.add_label(mail.messages[idx], verified_label)
    print('Finished!')









