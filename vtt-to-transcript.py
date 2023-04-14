import sys
import re

def convert_vtt_to_transcript(vtt_file, output_file):
    with open(vtt_file, 'r') as vtt, open(output_file, 'w') as transcript:
        content = vtt.read()

        # Remove timecodes and carriage returns
        content = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\n', '', content)

        # Remove webvtt header
        content = re.sub(r'WEBVTT\n\n', '', content)

        # Replace newlines with spaces
        content = re.sub(r'\n', ' ', content)

        transcript.write(content)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python vtt_to_transcript.py <input_vtt_file> <output_transcript_file>")
    else:
        convert_vtt_to_transcript(sys.argv[1], sys.argv[2])
