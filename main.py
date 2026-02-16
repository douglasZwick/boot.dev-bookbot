import sys
import argparse
from stats import get_total_word_count, compute_char_counts, compute_word_counts, to_sorted_dict_list


def get_book_text(path):
  """
  Opens a given text file path and returns the text it contains.
  
  :param path: A local path to a text file.
  :type path: string
  :return: The text the file contains.
  :rtype: string
  """
  with open(path) as file:
    return file.read()


def main():
  DEFAULT_TOP = 30
  parser = argparse.ArgumentParser(description="count characters or words in a given text file")
  parser.add_argument("path",
                      help="local path to a text file to analyze")
  parser.add_argument("-w", "--count-words",
                      help="show word counts instead of letter counts",
                      action="store_true")
  parser.add_argument("-t", "--top",
                      help=f"display only the top this many items (default {DEFAULT_TOP})",
                      type=int)
  args = parser.parse_args()

  if args.top == None or args.top < 1:
    args.top = DEFAULT_TOP

  text = get_book_text(args.path)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {args.path}...")

  word_count = get_total_word_count(text)
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")

  key_name = "word" if args.count_words else "char"
  key_name_long = "Word" if args.count_words else "Character"
  compute_function = compute_word_counts if args.count_words else compute_char_counts

  counts = compute_function(text)
  dict_list = to_sorted_dict_list(counts, key_name)
  top_string = f"(Top {args.top}) " if args.count_words and len(dict_list) > args.top else ""
  print(f"--------- Individual {key_name_long} Counts {top_string}-------")
  shown = 0
  for dict in dict_list:
    item = dict[key_name]

    if not item.isalpha():
      continue

    num = dict["num"]
    print(f"{item}: {num}")
    shown += 1
    if args.count_words and shown >= args.top:
      break

  print("============= END ===============")


main()
