import spacy

class NLP:

    def __init__(self, pipeline='en_core_web_sm'):
        self.nlp = spacy.load(pipeline)

    def contains_place(self, input_text):
        """
        Check if a place is mentioned in the input text.

        Parameters:
        input_text (str): The text to check for a place.

        Returns:
        bool: True if a place is mentioned, False otherwise.
        """
        doc = self.nlp(input_text)
        for ent in doc.ents:
            if ent.label_ == 'GPE':  # Check if the entity is a geographical location
                return True
        return False

    def contains_portfolio(self, input_text):
        """
        Check if a URL or Instagram handle is mentioned in the input text.

        Parameters:
        input_text (str): The text to check for a place.

        Returns:
        bool: True if a portfolio is mentioned, False otherwise.
        """
        doc = self.nlp(input_text)
        for ent in doc.ents:
            if ent.label_ in ['URL', 'PERSON']:  # Check if the entity is a portfolio or ig handle location
                return True
        return False