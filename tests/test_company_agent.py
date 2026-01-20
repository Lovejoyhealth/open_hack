"""Tests for the Company Agent"""
import unittest
from datetime import datetime
from agent import BaseAgent, CompanyAgent


class TestBaseAgent(unittest.TestCase):
    """Test cases for BaseAgent"""
    
    def setUp(self):
        """Set up test agent"""
        self.agent = BaseAgent(name="Test Agent", description="Test description")
    
    def test_initialization(self):
        """Test agent initialization"""
        self.assertEqual(self.agent.name, "Test Agent")
        self.assertEqual(self.agent.description, "Test description")
        self.assertIsInstance(self.agent.created_at, datetime)
        self.assertEqual(len(self.agent.conversation_history), 0)
    
    def test_add_to_history(self):
        """Test adding messages to history"""
        self.agent.add_to_history("user", "Hello")
        self.assertEqual(len(self.agent.conversation_history), 1)
        self.assertEqual(self.agent.conversation_history[0]["role"], "user")
        self.assertEqual(self.agent.conversation_history[0]["content"], "Hello")
    
    def test_clear_history(self):
        """Test clearing conversation history"""
        self.agent.add_to_history("user", "Test message")
        self.agent.clear_history()
        self.assertEqual(len(self.agent.conversation_history), 0)
    
    def test_get_history(self):
        """Test getting conversation history"""
        self.agent.add_to_history("user", "Message 1")
        self.agent.add_to_history("agent", "Response 1")
        history = self.agent.get_history()
        self.assertEqual(len(history), 2)


class TestCompanyAgent(unittest.TestCase):
    """Test cases for CompanyAgent"""
    
    def setUp(self):
        """Set up test company agent"""
        self.agent = CompanyAgent(company_name="Test Company")
    
    def test_initialization(self):
        """Test company agent initialization"""
        self.assertEqual(self.agent.company_name, "Test Company")
        self.assertIn("Test Company Agent", self.agent.name)
        self.assertEqual(len(self.agent.tasks), 0)
        self.assertEqual(len(self.agent.meetings), 0)
    
    def test_get_capabilities(self):
        """Test getting agent capabilities"""
        capabilities = self.agent.get_capabilities()
        self.assertIsInstance(capabilities, list)
        self.assertGreater(len(capabilities), 0)
    
    def test_greeting(self):
        """Test greeting response"""
        response = self.agent.process("Hello")
        self.assertIn("Hello", response)
        self.assertIn("Test Company", response)
    
    def test_help_command(self):
        """Test help command"""
        response = self.agent.process("help")
        self.assertIn("help you with", response.lower())
    
    def test_create_task(self):
        """Test creating a task"""
        response = self.agent.process("Create task: Test task description")
        self.assertEqual(len(self.agent.tasks), 1)
        self.assertIn("created successfully", response)
        self.assertEqual(self.agent.tasks[0]["description"], "Test task description")
        self.assertFalse(self.agent.tasks[0]["completed"])
    
    def test_list_tasks(self):
        """Test listing tasks"""
        self.agent.process("Create task: Task 1")
        self.agent.process("Create task: Task 2")
        response = self.agent.process("List tasks")
        self.assertIn("Task 1", response)
        self.assertIn("Task 2", response)
    
    def test_complete_task(self):
        """Test completing a task"""
        self.agent.process("Create task: Task to complete")
        response = self.agent.process("Complete task #1")
        self.assertTrue(self.agent.tasks[0]["completed"])
        self.assertIn("completed", response.lower())
    
    def test_schedule_meeting(self):
        """Test scheduling a meeting"""
        response = self.agent.process("Schedule meeting: Team standup")
        self.assertEqual(len(self.agent.meetings), 1)
        self.assertIn("scheduled", response.lower())
    
    def test_list_meetings(self):
        """Test listing meetings"""
        self.agent.process("Schedule meeting: Meeting 1")
        self.agent.process("Schedule meeting: Meeting 2")
        response = self.agent.process("List meetings")
        self.assertIn("Meeting 1", response)
        self.assertIn("Meeting 2", response)
    
    def test_generate_report(self):
        """Test generating a report"""
        self.agent.process("Create task: Task 1")
        self.agent.process("Schedule meeting: Meeting 1")
        report = self.agent.generate_report()
        self.assertIn("Report", report)
        self.assertIn("Tasks", report)
        self.assertIn("Meetings", report)
    
    def test_conversation_history(self):
        """Test conversation history tracking"""
        self.agent.process("Hello")
        self.agent.process("Create task: Test")
        history = self.agent.get_history()
        self.assertEqual(len(history), 4)  # 2 user messages + 2 agent responses


if __name__ == "__main__":
    unittest.main()
