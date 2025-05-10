"""
Legal Text Analysis Problem

Problem Statement:
Write a Python function that analyzes legal text to find the most frequently occurring significant words.
The function should:
1. Take a string of legal text as input
2. Tokenize the text into words
3. Count word frequencies, excluding common stop words
4. Return the top 5 most frequent words

Requirements:
- Words should be converted to lowercase for consistent counting
- Punctuation should be removed from words
- Common English stop words should be excluded
- If there are ties in frequency for the top 5, include all words with that frequency
- The output should be a list of tuples containing (word, frequency)

Example Input:
legal_text = '''
The contract between Party A and Party B shall commence on January 1, 2024.
Party A agrees to provide services to Party B in accordance with the terms.
Party B shall make payments to Party A within 30 days of receiving the invoice.
The contract may be terminated by either party with 60 days written notice.
Any disputes arising from this contract shall be resolved through arbitration.
'''

Expected Output:
[('party', 4), ('contract', 3), ('days', 2), ('written', 1), ('notice', 1), 
('disputes', 1), ('arising', 1), ('resolved', 1), ('arbitration', 1)]
"""

from collections import Counter
import string

def analyze_legal_text(text):
    """
    Analyze legal text to find the most frequent significant words.
    
    Args:
        text (str): The input legal text
        
    Returns:
        list: A list of tuples containing (word, frequency) for the most frequent words
    """
    # Define common stop words
    stop_words = {'the', 'a', 'an', 'is', 'in', 'on', 'and', 'or', 'but', 'of', 
                 'for', 'with', 'to', 'by', 'shall', 'may', 'be', 'this', 'that',
                 'these', 'those', 'from', 'as', 'at', 'it', 'its', 'their', 'they'}
    
    # Convert text to lowercase and remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower().translate(translator)
    
    # Tokenize the text into words
    words = text.split()
    
    # Filter out stop words and count frequencies
    word_counts = Counter(word for word in words if word not in stop_words)
    
    # Get the top 5 most common words (including ties)
    most_common = word_counts.most_common()
    
    # Find the frequency of the 5th most common word (or last if less than 5)
    if len(most_common) >= 5:
        fifth_freq = most_common[4][1]
        # Include all words with frequency >= fifth_freq
        top_words = [(word, freq) for word, freq in most_common if freq >= fifth_freq]
    else:
        top_words = most_common
    
    return top_words

# Example usage
if __name__ == "__main__":
    # Example legal text
    legal_text = '''
    The contract between Party A and Party B shall commence on January 1, 2024.
    Party A agrees to provide services to Party B in accordance with the terms.
    Party B shall make payments to Party A within 30 days of receiving the invoice.
    The contract may be terminated by either party with 60 days written notice.
    Any disputes arising from this contract shall be resolved through arbitration.
    '''
    
    # Analyze the text
    frequent_words = analyze_legal_text(legal_text)
    
    # Print results
    print("Most frequent words in the legal text:")
    for word, frequency in frequent_words:
        print(f"- '{word}': {frequency} occurrences")
