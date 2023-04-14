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
 
## How to run summarize-transcript.py

Follow these steps to run the `summarize-transcript.py` script:

1. Make sure you have Python installed on your computer. You can check by running the following command in your terminal or command prompt:

```python --version```

If you don't have Python installed, you can download it from the official website: https://www.python.org/downloads/

2. Install the required libraries. Open your terminal or command prompt, navigate to the directory containing the `summarize-transcript.py` script, and run the following command:

```pip install openai```

3. Replace the placeholder `your_api_key` in the `summarize-transcript.py` script with your actual OpenAI API key. You can obtain an API key by signing up for an account on the OpenAI website: https://beta.openai.com/signup/

4. In the terminal or command prompt, navigate to the directory containing both the `summarize-transcript.py` script and the transcript file (generated using `caption-to-transcript.py` or any other transcript file you'd like to summarize). Run the following command:

```python summarize-transcript.py transcript_file.txt```

Replace `transcript_file.txt` with the name of your transcript file. The script will generate a summary and a bullet list of topics discussed and action items, then save the result in a text file in the same directory with a format like `YYMMDD_meeting_saved_closed_caption_transcript_summary.txt`.
