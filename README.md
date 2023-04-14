# caption-transcript-summarize
 Python scripts to help parse and summarize audio .vtt transcripts into summaries, topic lists and action items with via ChatGPT

---
### Project Functionality
Two separate Python scripts. The first script will convert the .vtt caption file into a plain text transcript, and the second script will parse the transcript into 2000-character chunks and generate a summary and action items using ChatGPT.

### Installation
Install dependencies
* pip install openai

### Usage
Use the following commands to convert the .vtt file and generate the summary:

* python vtt_to_transcript.py input.vtt output.txt
* python summarize_transcript.py output.txt

Remember to replace 'your_api_key' in the summarize_transcript.py script with your actual OpenAI API key. The output will be printed to the console. You can redirect the output to a file if you wish to save it.