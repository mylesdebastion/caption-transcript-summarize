import sys
import re
import os
from datetime import datetime

def convert_file_to_transcript(input_file):
    # Generate output file name
    base_name = os.path.basename(input_file)
    name, ext = os.path.splitext(base_name)
    today = datetime.today().strftime('%y%m%d')
    output_file = f"{today}_{name}_transcript.txt"

    with open(input_file, 'r') as file, open(output_file, 'w') as transcript:
        content = file.read()

        # Check if the input file is a .vtt file
        if input_file.lower().endswith('.vtt'):
            # Remove timecodes and carriage returns
            content = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\n', '', content)

            # Remove webvtt header
            content = re.sub(r'WEBVTT\n\n', '', content)

        # Handle Zoom meeting .txt files
        elif input_file.lower().endswith('.txt'):
            # Remove speaker tags and timestamps
            content = re.sub(r'\[.*?\] \d{2}:\d{2}:\d{2}\n', '', content)

        # Replace newlines with spaces
        content = re.sub(r'\n', ' ', content)

        transcript.write(content)

    return output_file

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python caption-to-transcript.py <input_file>")
    else:
        output_file = convert_file_to_transcript(sys.argv[1])
        print(f"Transcript saved as: {output_file}")
