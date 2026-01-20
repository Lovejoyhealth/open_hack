# Company Agent

A Python-based intelligent agent system designed to help with various business and company tasks.

## Features

- **Task Management**: Create, list, and complete tasks
- **Meeting Scheduling**: Schedule and manage meetings
- **Conversation History**: Tracks all interactions for context
- **Business Communication**: Natural language interface for business activities
- **Report Generation**: Generate summary reports of agent activity

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Lovejoyhealth/open_hack.git
cd open_hack
```

2. No external dependencies required! The agent uses only Python standard library.

## Usage

### Basic Usage Example

```python
from agent import CompanyAgent

# Create an agent for your company
agent = CompanyAgent(company_name="Your Company")

# Interact with the agent
response = agent.process("Create task: Review quarterly reports")
print(response)

# List tasks
response = agent.process("List tasks")
print(response)

# Complete a task
response = agent.process("Complete task #1")
print(response)

# Schedule meetings
response = agent.process("Schedule meeting: Team standup")
print(response)
```

### Running the Examples

#### Basic Usage Example
```bash
python examples/basic_usage.py
```

#### Interactive Demo
```bash
python examples/interactive_demo.py
```

## Available Commands

The agent understands natural language commands including:

- **Task Management**
  - "Create task: [description]"
  - "List tasks"
  - "Complete task #[id]"

- **Meeting Management**
  - "Schedule meeting: [details]"
  - "List meetings"

- **Help & Information**
  - "help" - Show available capabilities
  - "report" - Generate activity report

## Running Tests

Run the test suite:
```bash
python -m unittest tests/test_company_agent.py
```

Or run with verbose output:
```bash
python -m unittest tests/test_company_agent.py -v
```

## Architecture

The system consists of two main components:

1. **BaseAgent**: Core agent functionality including:
   - Conversation history management
   - Message processing interface
   - Capability definition

2. **CompanyAgent**: Business-specific implementation with:
   - Task management system
   - Meeting scheduling
   - Natural language understanding
   - Report generation

## Extending the Agent

To create a custom agent, extend the `BaseAgent` class:

```python
from agent import BaseAgent

class MyCustomAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="My Agent", description="Custom agent")
    
    def get_capabilities(self):
        return ["Capability 1", "Capability 2"]
    
    def process(self, message):
        # Your custom logic here
        self.add_to_history("user", message)
        response = "Your response"
        self.add_to_history("agent", response)
        return response
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.