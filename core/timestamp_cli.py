from datetime import datetime
import pyperclip
from utils.time_utils import get_formatted_timestamp

def main():
  timestamp = get_formatted_timestamp(datetime.now())
  pyperclip.copy(timestamp)
  print(timestamp)

if __name__ == '__main__':
  main()