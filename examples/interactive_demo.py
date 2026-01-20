"""Interactive demo of the Company Agent"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import CompanyAgent


def main():
    agent = CompanyAgent(company_name="Lovejoy Health")
    
    print("=" * 60)
    print(f"Welcome to {agent.name}!")
    print("=" * 60)
    print("Type 'help' for available commands, 'quit' to exit")
    print()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye! Have a great day!")
                break
            
            if user_input.lower() == 'report':
                response = agent.generate_report()
            else:
                response = agent.process(user_input)
            
            print(f"\nAgent: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! Have a great day!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
