"""Base Agent class with core functionality"""
from typing import Dict, List, Any, Optional
from datetime import datetime
import json


class BaseAgent:
    """Base class for all agents with common functionality"""
    
    def __init__(self, name: str, description: str = ""):
        """
        Initialize the base agent.
        
        Args:
            name: Name of the agent
            description: Description of what the agent does
        """
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.conversation_history: List[Dict[str, Any]] = []
        
    def add_to_history(self, role: str, content: str, metadata: Optional[Dict] = None):
        """
        Add a message to the conversation history.
        
        Args:
            role: Role of the message sender (user, agent, system)
            content: Content of the message
            metadata: Optional metadata about the message
        """
        entry = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
        }
        if metadata:
            entry["metadata"] = metadata
        self.conversation_history.append(entry)
        
    def get_history(self) -> List[Dict[str, Any]]:
        """Get the full conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
        
    def process(self, message: str) -> str:
        """
        Process a message and return a response.
        Must be implemented by subclasses.
        
        Args:
            message: Input message to process
            
        Returns:
            Response from the agent
        """
        raise NotImplementedError("process method must be implemented by subclasses")
    
    def get_capabilities(self) -> List[str]:
        """
        Return a list of capabilities the agent has.
        Must be implemented by subclasses.
        
        Returns:
            List of capability descriptions
        """
        raise NotImplementedError("get_capabilities method must be implemented by subclasses")
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
