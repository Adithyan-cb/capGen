import base64
import os
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

class Hashtag(BaseModel):
    tag: str = Field(description="The hashtag including the # symbol")
    popularity: str = Field(description="Popularity level: low, medium, high, or trending")

class CaptionResult(BaseModel):
    text: str = Field(description="The caption text")
    hashtags: List[Hashtag] = Field(description="List of hashtags specific to this caption")

class GenerationResponse(BaseModel):
    captions: List[CaptionResult] = Field(description="List of engaging Instagram captions with their hashtags")

def analyze_image_and_generate_captions(image_file, vibe, count):
    """
    Analyzes the image using Gemini 1.5 Flash 
    and generates captions and hashtags in a structured format.
    """
    
    # Initialize the Gemini Flash model
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )
    
    # Load system prompt from file
    prompt_path = os.path.join(os.path.dirname(__file__), 'sysPrompt.md')
    try:
        with open(prompt_path, 'r') as f:
            system_prompt_template = f.read()
    except FileNotFoundError:
        # Fallback if file is missing
        system_prompt_template = "You are an expert Instagram content strategist."

    # Bind structured output
    structured_llm = model.with_structured_output(GenerationResponse)
    
    # Encode image to base64
    image_data = base64.b64encode(image_file.read()).decode("utf-8")
    
    # Inject count into the prompt template
    system_prompt = system_prompt_template.replace("{{count}}", str(count))
    
    human_content = [
        {
            "type": "text",
            "text": f"Vibe: {vibe}\nRequested number of captions: {count}\n\nPlease generate exactly {count} captions and relevant hashtags for each."
        },
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}
        }
    ]
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_content)
    ]
    
    try:
        response = structured_llm.invoke(messages)
        if response is None:
            print("Error generating captions: response is None")
            return {
                "captions": ["Error generating captions. Please try again."],
                "caption_details": [],
                "hashtags": []
            }
        return {
            "captions": [cap.text for cap in response.captions],
            "caption_details": [cap.dict() for cap in response.captions],
            "hashtags": [h.dict() for cap in response.captions for h in cap.hashtags]
        }
    except Exception as e:
        print(f"Error generating captions: {e}")
        return {
            "captions": ["Error generating captions. Please try again."],
            "caption_details": [],
            "hashtags": []
        }
