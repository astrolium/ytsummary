#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os
import re
import nltk
from youtube_transcript_api import YouTubeTranscriptApi
import openai
from googleapiclient.discovery import build


# In[16]:


api_key = 'AIzaSyDJUvWBGjN2VhaQtojtOXRQO-yWBcnLyqQ'  # Replace 'YOUR_API_KEY' with your own API key
youtube = build('youtube', 'v3', developerKey = api_key)


# In[17]:


def get_video_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ""
    for segment in transcript:
        text += ' ' + segment['text']
    return text


# In[18]:


def generate_summary(text):
    openai.api_key = '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'  # Replace with your OpenAI API key
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=100,
        temperature=0.3,
        top_p=0.95,
        n=1,
        stop=None
    )
    summary = response.choices[0].text.strip()
    return summary


# In[19]:


# Main function
def main():
    # Get YouTube video URL from user
    video_url = input("Enter the YouTube video URL: ")

    # Extract video ID from the URL
    video_id = video_url.split('v=')[1]

    # Return the transcript
    transcript = get_video_transcript(video_id)
    
    # Summarize in ChatGPT
    generate_summary(transcript)


# In[12]:


main()

