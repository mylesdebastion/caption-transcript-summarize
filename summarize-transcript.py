import openai
import sys
import textwrap
import os
from datetime import datetime

# Replace 'your_api_key' with your OpenAI API key
openai.api_key = 'your_api_key'

def generate_summary_chunks(transcript_file):
    with open(transcript_file, 'r') as file:
        content = file.read()

    summary = ''
    for chunk in textwrap.wrap(content, 2000):
        prompt = f"Create a meeting summary from the following text:\n{chunk}"
        response = openai.Completion.create(engine='text-davinci-002', prompt=prompt, max_tokens=150, n=1, stop=None, temperature=0.7)
        summary += response.choices[0].text.strip()

    return summary

def generate_bullet_list(summary):
    prompt = (
        f"Create a bullet list of topic descriptions and suggested action items from the following summary:\n{summary}"
    )
    response = openai.Completion.create(engine='text-davinci-002', prompt=prompt, max_tokens=150, n=1, stop=None, temperature=0.7)
    bullet_list = response.choices[0].text.strip()

    return bullet_list

def save_summary(summary, bullet_list, transcript_file):
    base_name = os.path.basename(transcript_file)
    name, ext = os.path.splitext(base_name)
    today = datetime.today().strftime('%y%m%d')
    summary_file = f"{today}_{name}_summary{ext}"

    with open(summary_file, 'w') as file:
        file.write(summary)
        file.write("\n\n")
        file.write(bullet_list)

    return summary_file

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python summarize_transcript.py <transcript_file>")
    else:
        summary_chunks = generate_summary_chunks(sys.argv[1])
        bullet_list = generate_bullet_list(summary_chunks)
        summary_file = save_summary(summary_chunks, bullet_list, sys.argv[1])
        print(f"Summary saved as: {summary_file}")
