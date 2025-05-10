import re
from typing import List, Set

def legal_text(text:str, abbreviations: set) -> List[str]:

    #lower
    text = text.lower()

    #abbr
    for abbr in abbreviations:
        text = text.replace(abbr, f"__ABBR_{abbr}__ ")

    #special char
    text = re.sub(r'[^a-z0-9\s.,$]', '', text)

    #tokenization
    tokens = []
    for word in text.split():
        #case 1 : handle currency
        if word.startswith('$'):
            amount = word[1:].replace(',', '')
            tokens.extend(['$', amount])
            continue

        #case 2 : handle decimal numbers
        if re.match(r'^\d*\.\d+$', word):
            tokens.append(word)
            continue

        #case 3 : handle abbreviations
        if word.startswith('__abbr_'):
            abbr = word[7:-2]
            tokens.append(abbr)
            continue
        
        #case 4 : handle regular words
        sub_tokens = re.split(r'[.,](?!\d)', word)
        tokens.extend(t for t in sub_tokens if t)

    return tokens

def main():     
    # Test cases
    test_cases = [
        {
            "input": "The case cited in e.g., Smith v. Jones, 1.2 U.S.C. § 50, involved $100,000 in damages etc.",
            "abbreviations": {'e.g.', 'i.e.', 'cf.', 'etc.'}
        },
        {
            "input": "Section 1.2 of the contract, i.e., the payment terms, requires $50,000.00 etc.",
            "abbreviations": {'e.g.', 'i.e.', 'cf.', 'etc.'}
        },
        {
            "input": "The plaintiff's attorney (cf. Smith v. Jones) filed a motion for $1,000,000.00 in damages.",
            "abbreviations": {'e.g.', 'i.e.', 'cf.', 'etc.'}
        }
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print("Input:", test["input"])
        result = legal_text(test["input"], test["abbreviations"])
        print("Output:", result)    
    
if __name__ == "__main__":
    main()


