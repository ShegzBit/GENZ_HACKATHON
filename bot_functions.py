#!/usr/bin/python3

import os
import openai
import json


openai.api_key = os.getenv("OPENAI_API_KEY")

def start_prompt():
    """Reads the start prompt from the start prompt json file"""
    with open("start_prompt.json", "r") as f:
        prompt = json.load(f)
    return prompt

def call_bot():
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = start_prompt()
            )
    return dict(completion.choices[0].message)

if __name__ == "__main__":
    print(call_bot().get("content"))
    exit(0)
