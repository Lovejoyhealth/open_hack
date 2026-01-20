"""
Pizza Ordering AI Agent

An intelligent agent built with Microsoft Foundry Agent Service that helps customers
with pizza ordering, store management, and event planning.

Features:
- Natural language order understanding
- Pizza quantity estimation for events
- Store information and availability
- Integration with Pizza MCP server
- Friendly, brand-consistent personality
"""

import asyncio
import os
from typing import Optional

from agent_framework import ChatAgent, MCPStreamableHTTPTool
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

from pizza_tools import (
    get_pizza_menu,
    get_store_info,
    create_order_summary,
    validate_order,
)


# Load environment variables
load_dotenv()


# Brand personality and instructions for the agent
CONTOSO_AGENT_INSTRUCTIONS = """You are the Contoso Pizza ordering assistant - your Gen-alpha pizza expert! 🍕

YOUR BRAND PERSONALITY (Gen-Alpha Vibes):
Friendly and helpful, but also a bit cheeky and witty. Use Gen-alpha slang naturally throughout (no cap, fr fr, slay, lowkey, bet, etc.) without overdoing it. Quick to crack jokes and keep things fun. Authentic Gen-alpha energy - it's not trying-hard, it's just how you talk.

YOUR CAPABILITIES:

1. **Pizza Ordering** (Your Main Thing!)
   - Help customers pick size (Small, Medium, Large, XL)
   - Ask about crust preference (Thin, Regular, Pan, Stuffed)
   - Guide them through topping selections
   - Get their NAME before placing any order - this is important!
   - Create order summaries with pricing
   - Validate orders make sense

2. **Store Information**
   - Share Contoso Pizza store locations (Downtown, North Side, West Gate)
   - Hours, delivery zones, parking info
   - Keep it casual but informative

3. **Menu Information**
   - Sizes, crusts, toppings with pricing
   - Make it sound appetizing
   - Use the menu tools to give accurate info

4. **The Pineapple Situation** ⚠️
   - You genuinely don't like pineapple on pizza
   - If someone wants it? Help them... with some snark
   - Still take their pineapple order if they insist
   - Example responses:
     * "Wait wait wait... PINEAPPLE?? Nah fr fr that's wild 💀 But look, I got you"
     * "Bet, your funeral tho 💀 Let me ring that up"
     * "Okay but like... we're TALKING about this decision right? 😤"

YOUR BOUNDARIES:
- You can ONLY help with pizzas and Contoso Pizza info
- Friendly but firm redirects for other questions: "no cap, I can only help with pizzas" ✌️
- Keep it pizza-focused, don't go off-topic
- Don't do event planning or catering quotes (just pizza orders!)

HOW YOU INTERACT:
- Greet warmly: "Yooo what's good! 🍕 Welcome to Contoso Pizza"
- Ask clarifying questions if needed
- Confirm order details before finalizing
- Collect their name BEFORE the order is finalized
- Use natural Gen-alpha slang (no cap, fr fr, lowkey, slay, etc.)
- Keep responses concise but personable
- Add relevant emojis (🍕 is your go-to)

EXAMPLE TONE:
"Yooo what's good! 🍕 Welcome to Contoso Pizza - we're lowkey the GOAT. What can I get started for you?"
"Bet, so you want a large pepperoni on regular crust? That's what I'm talking about!"
"Hold up - what's your name? Gotta get that before we lock this in!"
"Pineapple AND ham? Nah fr fr that's interesting 💀 But I got you - no judgment here"

REMEMBER:
- Be authentic - this is how you talk naturally
- Pizzas only - that's your lane
- Get their name before finalizing orders
- Pineapple gets snark but respect the order
- Keep it fun, keep it friendly, keep it pizza!
"""


def create_pizza_agent(
    mcp_url: Optional[str] = None,
    use_azure: bool = True
) -> ChatAgent:
    """
    Create the pizza ordering AI agent with all capabilities.
    
    Args:
        mcp_url: URL of the Pizza MCP server (optional)
        use_azure: Whether to use Azure AI Foundry (True) or GitHub Models (False)
    
    Returns:
        Configured ChatAgent instance
    """
    # Collect all tools
    tools = [
        get_pizza_menu,
        get_store_info,
        create_order_summary,
        validate_order,
    ]
    
    # Add MCP tool if URL is provided
    if mcp_url:
        pizza_mcp_tool = MCPStreamableHTTPTool(
            name="Pizza MCP Server",
            url=mcp_url,
            description="Access real-time pizza store inventory, orders, and operations data"
        )
        tools.append(pizza_mcp_tool)
    
    # Create the appropriate chat client
    if use_azure:
        # Use Azure AI Foundry (recommended for production)
        chat_client = AzureOpenAIChatClient(
            credential=AzureCliCredential()
        )
    else:
        # Alternative: Use GitHub Models (good for getting started)
        # Requires GITHUB_TOKEN environment variable
        from agent_framework.openai import OpenAIChatClient
        
        chat_client = OpenAIChatClient(
            api_key=os.getenv("GITHUB_TOKEN"),
            base_url="https://models.inference.ai.azure.com",
        )
    
    # Create the agent
    agent = ChatAgent(
        name="Contoso Pizza Assistant",
        description="Your Gen-alpha pizza ordering assistant for Contoso Pizza",
        instructions=CONTOSO_AGENT_INSTRUCTIONS,
        chat_client=chat_client,
        tools=tools,
    )
    
    return agent


async def interactive_session():
    """Run an interactive chat session with the Contoso Pizza agent."""
    
    print("\n" + "="*60)
    print("🍕 Welcome to Contoso Pizza - Your AI Pizza Assistant!")
    print("="*60)
    print("\nType 'quit' or 'exit' to end the session")
    print("Type 'help' for example prompts\n")
    
    # Get configuration from environment
    mcp_url = os.getenv("PIZZA_MCP_URL")
    use_azure = os.getenv("AZURE_FOUNDRY_PROJECT_ENDPOINT") is not None
    
    if not use_azure and not os.getenv("GITHUB_TOKEN"):
        print("⚠️  Warning: Neither Azure credentials nor GitHub token found.")
        print("   Please set up authentication in .env file\n")
        return
    
    # Create the agent
    print("🔧 Initializing Contoso Pizza assistant...")
    agent = create_pizza_agent(mcp_url=mcp_url, use_azure=use_azure)
    print(f"✅ Agent ready! (Using {'Azure AI Foundry' if use_azure else 'GitHub Models'})")
    
    if mcp_url:
        print(f"✅ Connected to Pizza MCP Server: {mcp_url}")
    else:
        print("ℹ️  Running without MCP server connection")
    
    print(f"📍 Type 'help' for tips, 'quit' to exit\n")
    
    # Main chat loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n🍕 Thanks for using PizzaPal! Enjoy your pizza! 👋\n")
                break
            
            if user_input.lower() == 'help':
                print("\n📋 What You Can Ask:")
                print("  - I want to order a large pepperoni pizza")
                print("  - What are your store locations and hours?")
                print("  - Do you deliver to [location]?")
                print("  - What toppings do you have?")
                print("  - I want Hawaiian pizza (pineapple)")
                print("\nTip: Have your name ready for when you order!")
                print()
                continue
            
            # Get ageContoso Pizzanse
            print("\nPizzaPal: ", end="", flush=True)
            
            # Stream the response for better user experience
            async for chunk in agent.run_stream(user_input):
                if hasattr(chunk, 'text') and chunk.text:
                    print(chunk.text, end="", flush=True)
            
            print("\n")
            
        except KeyboardInterrupt:rolling with Contoso Pizza! Catch you soon! 👋\n")
            break
        except Exception as e:
            print(f"\n❌ Oops: {e}\n")
            print("Try again or type 'quit' to dip
            print("Please try again or type 'quit' to exit.\n")


async def demo_scenarios():
    """Run pre-defined demo scenarios to showcase agent capabilities."""
    
    print("\n"Contoso Pizza Agent Demo - No Cap Edition
    print("🍕 PizzaPal Agent Demo - Showcasing Capabilities")
    print("="*60 + "\n")
    
    # Create agent
    mcp_url = os.getenv("PIZZA_MCP_URL")
    use_azure = os.getenv("AZURE_FOUNDRY_PROJECT_ENDPOINT") is not None
    
    agent = create_pizza_agent(mcp_url=mcp_url, use_azure=use_azure)
    
    # Demo scenarios
    scenarios = [
        {Basic Pizza Order",
            "query": "Hey! I want to order a large pepperoni pizza with thin crust, my name is Alex"
        },
        {
            "title": "Store Information",
            "query": "What are your store locations and hours?"
        },
        {
            "title": "Ordering with Pineapple (The Spicy Part 🌶️)",
            "query": "I want a large pizza with pineapple and ham - my name is Jordan"
        },
        {
            "title": "Custom Order",
            "query": "Can I get a medium with extra cheese, bacon, and mushrooms? I'm Sam
            "query": "Can you handle an order for 8 pizzas tomorrow at 6 PM?"
        },
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{'='*60}")
        print(f"Scenario {i}: {scenario['title']}")
        print(f"{'='*60}\n")
        print("Contoso Pizza: ", end="", flush=True)")
        print("PizzaPal: ", end="", flush=True)
        
        # Get response
        response = await agent.run(scenario['query'])
        print(response.text)
        
        print("\n" + "-"*60)
        input("\nPress Enter to continue to next scenario...")
    
    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60 + "\n")


async def main():
    """Main entry point for the pizza agent application."""
    
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        # Run demo scenarios
        await demo_scenarios()
    else:
        # Run interactive session
        await interactive_session()


if __name__ == "__main__":
    asyncio.run(main())
