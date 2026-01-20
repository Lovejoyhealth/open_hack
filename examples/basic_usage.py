"""Example usage of the Company Agent"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import CompanyAgent


def main():
    # Initialize the agent for your company
    agent = CompanyAgent(company_name="Lovejoy Health")
    
    print("=" * 60)
    print(f"Welcome to {agent.name}!")
    print("=" * 60)
    print()
    
    # Example interactions
    print("1. Getting help")
    print("-" * 60)
    response = agent.process("help")
    print(response)
    print()
    
    print("2. Creating tasks")
    print("-" * 60)
    response = agent.process("Create task: Review patient feedback from Q4")
    print(response)
    response = agent.process("Create task: Prepare board meeting presentation")
    print(response)
    response = agent.process("Create task: Update employee handbook")
    print(response)
    print()
    
    print("3. Listing tasks")
    print("-" * 60)
    response = agent.process("List tasks")
    print(response)
    print()
    
    print("4. Completing a task")
    print("-" * 60)
    response = agent.process("Complete task #1")
    print(response)
    print()
    
    print("5. Updated task list")
    print("-" * 60)
    response = agent.process("List tasks")
    print(response)
    print()
    
    print("6. Scheduling meetings")
    print("-" * 60)
    response = agent.process("Schedule meeting: Weekly team standup")
    print(response)
    response = agent.process("Schedule meeting: Client review session")
    print(response)
    print()
    
    print("7. Listing meetings")
    print("-" * 60)
    response = agent.process("List meetings")
    print(response)
    print()
    
    print("8. Generating report")
    print("-" * 60)
    report = agent.generate_report()
    print(report)
    print()
    
    print("=" * 60)
    print("Example completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
