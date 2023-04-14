import openai
import sys
import textwrap

# Replace 'your_api_key' with your OpenAI API key
openai.api_key = 'your_api_key'

def generate_summary(transcript_file):
    with open(transcript_file, 'r') as file:
        content = file.read()

    summary = ''
    for chunk in textwrap.wrap(content, 2000):
        prompt = (
            f"Create a meeting summary followed by a bullet list of topic descriptions "
            f"and suggested action items from the following text:\n{chunk}"
        )
        response = openai.Completion.create(engine='text-davinci-002', prompt=prompt, max_tokens=150, n=1, stop=None, temperature=0.7)
        summary += response.choices[0].text.strip()

    return summary

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python summarize_transcript.py <transcript_file>")
    else:
        summary = generate_summary(sys.argv[1])
        print(summary)
