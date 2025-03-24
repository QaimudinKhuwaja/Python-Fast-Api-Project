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

funny_jokes = [
    "Dost ne pocha: bhai sach bolun ya mazak? Mene kaha: mazak. Bola: tu bohot aqalmand hai!",
    "Ami ne kaha: doodh ubaal lo! Mene ubaal liya, ab roz phone kar ke poochti hain, kahan pohancha?",
    "Pakistan me gaari ke horn ki do aqsam hain: 'Peshgi ittila' aur 'Ab to gaya bhai'.",
    "Pehla Pakistani: Bhai waqt kya hua hai? Dosra: Mujhe kya pata, mera to WiFi connect nahi ho raha!",
    "Imtehan me sawal aya: Roshni kya hai? Mene likha: Loadshedding ke baad ka ek khwab!",
    "Pakistani aunty ke purse me paise kam aur bill zyada hote hain, jaise jaadui batwa!",
    "Dost: Bhai qarza diya tha yaad hai? Me: Haan, din raat duaon me yaad rakhta hoon!",
    "Ami kehti hain: Bahar se kuch na khana! Aur khud mehmanon ke liye gol gappay banwa rahi hoti hain!",
    "Agar Pakistan me koi sasta package chahiye to bas mobile network badalne ki dhamki de do!",
    "Pakistani signal todne ke baad dosray driver ko ghoortay aise hain jaise wahi ghalti par hai!",
    "Pakistan me har chaukidaar ke paas do cheezein zaroori hain: ek seeti aur dosra WhatsApp ka status!",
    "Pakistan me 'Free WiFi' ke peechay aisi daud lagti hai jaise free biryani mil rahi ho!",
    "Pakistan me barish ho jaye to log sarkon par aise khush hotay hain jaise naye note gir gaye hon!",
    "Ami: Beta pani bhar lo! Me: Ji Ami! (Aur phir dekhte hain balti khaali hai aur Ami khari hain!)",
    "Pakistan me 'Main raste me hoon' ka matlab hota hai ke abhi ghar se nikla bhi nahi!"
]


@app.get('/inspired_quotes' )
def get_inspired_quotes(api_key: str):
    """Returns a list of suggestions"""
    if api_key != '123':
        return{"error": "Invalid Api Key"}
    return{"quotes": random.choice(inspired_quotes)}


@app.get('/side_work')
def get_side_work(api_key:str):
    """Returns a list of sidework tasks"""
    if api_key != '123':
        return{"error": "Invalid Api Key"}
    return{"side_works": random.choice(side_work)}


@app.get('/funny_jokes')
def get_funny_jokes(api_key:str):
    """Returns a list of funny jokes"""
    if api_key != '123':
        return{"error": "Invalid Api Key"}
    return{"jokes": random.choice(funny_jokes)}
 