"""
Legal Date Extractor Problem

Problem Statement:
Write a Python function that extracts dates from legal text documents. The function should:
1. Take a string of legal text as input
2. Find all dates written in either:
   - "Month Day, Year" format (e.g., "January 15, 2024")
   - "Day Month, Year" format (e.g., "15 January, 2024")
3. Return a list of all found dates

Requirements:
- Month names must be fully spelled out
- Day must be a number (1-31)
- Year must be a four-digit number
- The format must be either "Month Day, Year" or "Day Month, Year" with a comma after the day/month

Example Input:
legal_text = '''
The contract was signed on January 15, 2024, and will be effective until 31 December, 2024.
The previous agreement dated 1 March, 2023, has been terminated.
All payments must be made by February 28, 2024.
The parties met on 30 November, 2023, to discuss the terms.
'''

Expected Output:
['January 15, 2024', '31 December, 2024', '1 March, 2023', 'February 28, 2024', '30 November, 2023']
"""

import re

def extract_legal_dates(text):
    """
    Extract dates in both "Month Day, Year" and "Day Month, Year" formats from legal text.
    
    Args:
        text (str): The input legal text containing dates
        
    Returns:
        list: A list of all found dates in either format
    """
    # Define patterns for both date formats
    # Pattern 1: Month Day, Year
    # Pattern 2: Day Month, Year
    pattern = r'\b(?:[A-Z][a-z]+\s+\d{1,2}|\d{1,2}\s+[A-Z][a-z]+),\s+\d{4}\b'
    
    # Find all matches in the text
    dates = re.findall(pattern, text)
    
    return dates

# Example usage
if __name__ == "__main__":
    # Example legal text
    legal_text = '''
    The contract was signed on January 15, 2024, and will be effective until 31 December, 2024.
    The previous agreement dated 1 March, 2023, has been terminated.
    All payments must be made by February 28, 2024.
    The parties met on 30 November, 2023, to discuss the terms.
    '''
    
    # Extract dates
    found_dates = extract_legal_dates(legal_text)
    
    # Print results
    print("Found dates:")
    for date in found_dates:
        print(f"- {date}") 