from fastapi import FastAPI 
import random
import streamlit as st

app = FastAPI()

side_work =[
    "Cleaning up",
    "Washing dishes",
    "Packing supplies",
    "Loading trucks",
    "Mowing lawns",
    "Driving cars",
    "Babysitting",
    "Help with homework",
    "Taking care of pets",
    "Cooking meals",
    "Gardening",
    "Fixing computers",
    "Organizing files",
    "Typing",
    "Editing documents",
    "Researching",
    "Teaching",
    "Reading",
    "Writing",
    "Listening to music",
    "Playing games",
    "Practicing yoga",
    "Playing video games",
]

inspired_quotes = [
    "The most important thing in life is to enjoy every moment.",
    "The key to success is to focus on what you can control.",
    "If you're not willing to do what you believe in, you're not truly living.",
    "The key to happiness is to find a balance between work and play.",
    "To succeed, you must believe in yourself and your abilities.",
    "The most important thing in life is to have fun.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The only way to do great work is to love what you do.",
]


@app.get('/inspired_quotes' )
def get_inspired_quotes():
    """Returns a list of suggestions"""
    return{"quotes": random.choice(inspired_quotes)}


@app.get('/side_work')
def get_side_work(api_key:str):
    """Returns a list of sidework tasks"""
    if api_key != '123':
        return{"error": "Invalid Api Key"}
    return{"side_works": random.choice(side_work)}


 