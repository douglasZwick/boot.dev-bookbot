"""
stats.py

Functions for computing statistics about a text.
"""

def get_total_word_count(text):
  """
  Counts the number of words in the given text.
  
  :param text: The text to analyze.
  :type text: string
  :return: The number of words in the text.
  :rtype: int
  """
  words = text.split()
  return len(words)


def compute_word_counts(text):
  """
  Counts the occurrences of each word found in the given text and returns them in a dictionary.
  
  :param text: The text to analyze.
  :type text: string
  :return: A dictionary containing each unique word (lowercased) in the text, mapped to the number of occurrences of that word.
  :rtype: dictionary
  """
  word_counts = {}

  words = text.split()
  for word in words:
    lower_word = word.lower()
    if lower_word in word_counts:
      word_counts[lower_word] += 1
    else:
      word_counts[lower_word] = 1
    
  return word_counts


def compute_char_counts(text):
  """
  Counts the occurrences of each character found in the given text and returns them in a dictionary.
  
  :param text: The text to analyze.
  :type text: string
  :return: A dictionary containing each unique character in the text (with upper and lowercase letters combined), mapped to the number of occurrences of that character.
  :rtype: dictionary
  """
  char_counts = {}

  for char in text:
    lower_char = char.lower()
    if lower_char in char_counts:
      char_counts[lower_char] += 1
    else:
      char_counts[lower_char] = 1
  
  return char_counts


def to_sorted_dict_list(counts, key_name):
  """
  Generates a list of count dictionaries, sorted in descending order by the number of occurrences.
  
  :param char_counts: The count dictionary, as returned by compute_char_counts.
  :type char_counts: dictionary
  :param key_name: The name of the keys found in this dictionary (e.g. "char", "word", etc.)
  :type key_name: string
  :return: A list of dictionaries showing the number of occurrences of each character.
  :rtype: list
  """
  dict_list = []
  for key in counts:
    dict_list.append({ key_name: key, "num": counts[key], })
  dict_list.sort(reverse = True, key = lambda item: item["num"])
  return dict_list
