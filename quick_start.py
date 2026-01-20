"""
Quick Start Guide - Contoso Pizza AI Agent

This script provides example usage of the Contoso Pizza agent for different scenarios.
"""

import asyncio
import os

from dotenv import load_dotenv
from pizza_agent import create_pizza_agent


async def quick_examples():
    """Run quick examples demonstrating key features."""
    
    load_dotenv()
    
    # Create the agent
    print("Creating Contoso Pizza agent...\n")
    agent = create_pizza_agent(
        mcp_url=os.getenv("PIZZA_MCP_URL"),
        use_azure=True  # Set to False to use GitHub Models
    )
    
    print("=" * 70)
    print("CONTOSO PIZZA - QUICK START EXAMPLES")
    print("=" * 70)
    
    # Example 1: Basic Pizza Order
    print("\n🍕 Example 1: Ordering a Pizza\n")
    print("Query: 'I want a large pepperoni pizza with thin crust, my name is Alex'")
    print("\nResponse:")
    response1 = await agent.run(
        "I want a large pepperoni pizza with thin crust, my name is Alex"
    )
    print(response1.text)
    print("\n" + "-" * 70)
    
    # Example 2: Store Information
    print("\n📍 Example 2: Getting Store Information\n")
    print("Query: 'Where are you located and what are your hours?'")
    print("\nResponse:")
    response2 = await agent.run("Where are you located and what are your hours?")
    print(response2.text)
    print("\n" + "-" * 70)
    
    # Example 3: Menu Info
    print("\n📋 Example 3: Checking Menu Options\n")
    print("Query: 'What toppings and crust types do you have?'")
    print("\nResponse:")
    response3 = await agent.run(
        "What toppings and crust types do you have?"
    )
    print(response3.text)
    print("\n" + "-" * 70)
    
    # Example 4: Pineapple Order
    print("\n🍍 Example 4: The Pineapple Situation\n")
    print("Query: 'I want a large pizza with pineapple and ham, my name is Jordan'")
    print("\nResponse:")
    response4 = await agent.run(
        "I want a large pizza with pineapple and ham, my name is Jordan"
    )
    print(response4.text)
    print("\n" + "-" * 70)
    
    print("\n✅ Examples complete!")
    print("\nTo run the full interactive agent:")
    print("  python pizza_agent.py --interactive")
    print("\nTo see demo scenarios:")
    print("  python pizza_agent.py --demo")


async def test_tools_individually():
    """Test individual tools to verify functionality."""
    
    load_dotenv()
    
    print("\n" + "=" * 70)
    print("TESTING CONTOSO PIZZA TOOLS")
    print("=" * 70)
    
    agent = create_pizza_agent(use_azure=True)
    
    # Test 1: Menu Info
    print("\n🔧 Test 1: Getting Menu Information\n")
    test1 = await agent.run(
        "Tell me about all your menu options"
    )
    print(test1.text)
    print("\n" + "-" * 70)
    
    # Test 2: Store Info
    print("\n🔧 Test 2: Store Location Information\n")
    test2 = await agent.run("Show me all your store locations")
    print(test2.text)
    print("\n" + "-" * 70)
    
    # Test 3: Order Summary
    print("\n🔧 Test 3: Creating an Order Summary\n")
    test3 = await agent.run(
        "Create an order summary for a large pizza with pepperoni and mushroom for Sarah"
    )
    print(test3.text)
    print("\n" + "-" * 70)
    
    # Test 4: Validation
    print("\n🔧 Test 4: Order Validation\n")
    test4 = await agent.run("Validate a large pan crust pizza with sausage toppings")
    print(test4.text)
    print("\n" + "-" * 70)
    
    print("\n✅ Tool testing complete!")


async def personality_showcase():
    """Showcase the agent's Gen-alpha brand personality."""
    
    load_dotenv()
    
    print("\n" + "=" * 70)
    print("CONTOSO PIZZA - GEN-ALPHA PERSONALITY SHOWCASE")
    print("=" * 70)
    
    agent = create_pizza_agent(use_azure=True)
    
    scenarios = [
        "Yo, what's good!",
        "I want to order a pizza but idk what to get",
        "What makes Contoso Pizza special?",
        "Can I get a pizza with pineapple?",
        "Do you help with non-pizza stuff?",
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{i}. Customer: {scenario}")
        print("   Contoso: ", end="")
        response = await agent.run(scenario)
        print(response.text)
        print()
    
    print("=" * 70)
    print("Notice Contoso's Gen-alpha vibes - friendly, cheeky, pizza-focused!")
    print("=" * 70)


if __name__ == "__main__":
    print("\n🍕 Contoso Pizza AI Agent - Quick Start Examples")
    print("\nWhat would you like to run?")
    print("1. Quick examples (recommended)")
    print("2. Individual tool testing")
    print("3. Personality showcase")
    print("4. All of the above")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        asyncio.run(quick_examples())
    elif choice == "2":
        asyncio.run(test_tools_individually())
    elif choice == "3":
        asyncio.run(personality_showcase())
    elif choice == "4":
        async def run_all():
            await quick_examples()
            await test_tools_individually()
            await personality_showcase()
        asyncio.run(run_all())
    else:
        print("Invalid choice. Running quick examples...")
        asyncio.run(quick_examples())
