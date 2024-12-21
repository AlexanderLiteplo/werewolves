from typing import List, Dict
from dataclasses import dataclass
import openai
from constants import LLMModel
import os
@dataclass
class Message:
    role: str
    content: str

class LLM:
    def __init__(self, model: LLMModel = LLMModel.GPT4_MINI):
        self.model = model
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def chat_completion(self, messages: List[Dict[str, str]]) -> str:
        """
        Send a chat completion request to the OpenAI API
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            
        Returns:
            The assistant's response text
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model.value,
                messages=messages,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in chat completion: {e}")
            return "I apologize, but I encountered an error processing your request."
