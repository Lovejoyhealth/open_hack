"""Company Agent with business-specific capabilities"""
from typing import Dict, List, Any, Optional
from datetime import datetime
import re
from .base_agent import BaseAgent


class CompanyAgent(BaseAgent):
    """Agent designed to help with company and business tasks"""
    
    def __init__(self, company_name: str = "Your Company"):
        """
        Initialize the company agent.
        
        Args:
            company_name: Name of the company the agent is serving
        """
        super().__init__(
            name=f"{company_name} Agent",
            description=f"AI assistant for {company_name} helping with various business tasks"
        )
        self.company_name = company_name
        self.tasks: List[Dict[str, Any]] = []
        self.meetings: List[Dict[str, Any]] = []
        
    def get_capabilities(self) -> List[str]:
        """Return the list of capabilities"""
        return [
            "Task management (create, list, complete tasks)",
            "Meeting scheduling and management",
            "Information lookup and Q&A",
            "Business communication assistance",
            "Report generation",
            "Calendar management"
        ]
    
    def process(self, message: str) -> str:
        """
        Process a user message and return an appropriate response.
        
        Args:
            message: User's input message
            
        Returns:
            Agent's response
        """
        self.add_to_history("user", message)
        
        message_lower = message.lower()
        
        # Task management
        if "create task" in message_lower or "add task" in message_lower:
            response = self._create_task(message)
        elif "list task" in message_lower or "show task" in message_lower:
            response = self._list_tasks()
        elif "complete task" in message_lower or "finish task" in message_lower:
            response = self._complete_task(message)
            
        # Meeting management
        elif "schedule meeting" in message_lower or "create meeting" in message_lower:
            response = self._schedule_meeting(message)
        elif "list meeting" in message_lower or "show meeting" in message_lower:
            response = self._list_meetings()
            
        # General help
        elif "help" in message_lower or "what can you do" in message_lower:
            response = self._get_help()
        elif "hello" in message_lower or "hi" in message_lower:
            response = f"Hello! I'm the {self.company_name} agent. How can I assist you today?"
            
        else:
            response = self._handle_general_query(message)
        
        self.add_to_history("agent", response)
        return response
    
    def _create_task(self, message: str) -> str:
        """Create a new task from the message"""
        # Extract task description (simple extraction after "task")
        task_match = re.search(r'task[:\s]+(.+)', message, re.IGNORECASE)
        if task_match:
            task_description = task_match.group(1).strip()
        else:
            task_description = message
            
        task = {
            "id": len(self.tasks) + 1,
            "description": task_description,
            "created_at": datetime.now().isoformat(),
            "completed": False
        }
        self.tasks.append(task)
        return f"Task created successfully! Task #{task['id']}: {task_description}"
    
    def _list_tasks(self) -> str:
        """List all tasks"""
        if not self.tasks:
            return "No tasks found. Create a task to get started!"
        
        active_tasks = [t for t in self.tasks if not t["completed"]]
        completed_tasks = [t for t in self.tasks if t["completed"]]
        
        response = "📋 **Active Tasks:**\n"
        if active_tasks:
            for task in active_tasks:
                response += f"  #{task['id']}: {task['description']}\n"
        else:
            response += "  No active tasks\n"
            
        if completed_tasks:
            response += "\n✅ **Completed Tasks:**\n"
            for task in completed_tasks:
                response += f"  #{task['id']}: {task['description']}\n"
                
        return response
    
    def _complete_task(self, message: str) -> str:
        """Mark a task as completed"""
        # Extract task ID
        task_id_match = re.search(r'#?(\d+)', message)
        if not task_id_match:
            return "Please specify a task ID to complete (e.g., 'complete task #1')"
        
        task_id = int(task_id_match.group(1))
        
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat()
                return f"✅ Task #{task_id} marked as completed!"
        
        return f"Task #{task_id} not found."
    
    def _schedule_meeting(self, message: str) -> str:
        """Schedule a new meeting"""
        # Extract meeting details from message
        meeting_match = re.search(r'meeting[:\s]+(.+)', message, re.IGNORECASE)
        if meeting_match:
            meeting_title = meeting_match.group(1).strip()
        else:
            meeting_title = message
            
        meeting = {
            "id": len(self.meetings) + 1,
            "title": meeting_title,
            "scheduled_at": datetime.now().isoformat(),
            "created_at": datetime.now().isoformat()
        }
        self.meetings.append(meeting)
        return f"Meeting scheduled! Meeting #{meeting['id']}: {meeting_title}"
    
    def _list_meetings(self) -> str:
        """List all meetings"""
        if not self.meetings:
            return "No meetings scheduled."
        
        response = "📅 **Scheduled Meetings:**\n"
        for meeting in self.meetings:
            response += f"  #{meeting['id']}: {meeting['title']}\n"
        return response
    
    def _get_help(self) -> str:
        """Return help information"""
        capabilities = self.get_capabilities()
        response = f"I'm the {self.company_name} Agent. Here's what I can help you with:\n\n"
        for i, capability in enumerate(capabilities, 1):
            response += f"{i}. {capability}\n"
        response += "\nTry commands like:\n"
        response += "  - 'Create task: Review Q4 reports'\n"
        response += "  - 'List tasks'\n"
        response += "  - 'Complete task #1'\n"
        response += "  - 'Schedule meeting: Team sync tomorrow'\n"
        response += "  - 'List meetings'\n"
        return response
    
    def _handle_general_query(self, message: str) -> str:
        """Handle general queries"""
        return (
            f"I understand you're asking about: '{message}'\n\n"
            f"As the {self.company_name} agent, I can help you with tasks, meetings, "
            f"and other business activities. Type 'help' to see what I can do!"
        )
    
    def generate_report(self) -> str:
        """Generate a summary report of agent activity"""
        report = f"📊 **{self.company_name} Agent Report**\n"
        report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        report += f"**Tasks:**\n"
        report += f"  Total: {len(self.tasks)}\n"
        active = sum(1 for t in self.tasks if not t["completed"])
        completed = len(self.tasks) - active
        report += f"  Active: {active}\n"
        report += f"  Completed: {completed}\n\n"
        
        report += f"**Meetings:**\n"
        report += f"  Total: {len(self.meetings)}\n\n"
        
        report += f"**Conversation History:**\n"
        report += f"  Messages: {len(self.conversation_history)}\n"
        
        return report
