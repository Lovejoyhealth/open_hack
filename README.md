# Contoso Pizza Ordering AI Agent

Your Gen-alpha friendly pizza ordering assistant with a cheeky personality! 🍕

An intelligent agent built with Microsoft Foundry Agent Service that helps customers:
- Order pizzas with their preferred size, crust, and toppings
- Get information about Contoso Pizza stores
- Experience a fun, witty customer service vibe
- (Groan a little about pineapple 😤, but still help you order it)

## Features

- **Gen-Alpha Personality**: Friendly, helpful, and cheeky
- **Pizza Ordering**: Help with size, crust type, and toppings
- **Store Information**: Locations, hours, delivery info
- **Customer Names**: Always gets your name before placing orders
- **Boundaries**: Stays focused on pizza - no random tangents
- **MCP Integration**: Connects to Pizza MCP server for live data (optional)

## Prerequisites

- Python 3.10 or higher
- Azure CLI (for authentication)
- Azure AI Foundry project (or GitHub Models API key)

## Installation

1. Install dependencies:
```bash
pip install agent-framework-azure-ai --pre
```

2. Configure environment (copy .env.example to .env):
```bash
cp .env.example .env
```

3. Set up credentials in .env:
```bash
# For Azure AI Foundry
AZURE_FOUNDRY_PROJECT_ENDPOINT=https://your-project.ai.azure.com/
AZURE_FOUNDRY_PROJECT_DEPLOYMENT_NAME=gpt-4o-mini

# Optional: Pizza MCP Server
PIZZA_MCP_URL=https://your-pizza-mcp-server.com/api/mcp
```

4. Authenticate:
```bash
az login
```

## Usage

### Interactive Chat
Chat with the Contoso Pizza assistant:
```bash
python pizza_agent.py
```

### Demo Scenarios
See the agent in action with pre-built scenarios:
```bash
python pizza_agent.py --demo
```

### Quick Examples
Run curated examples:
```bash
python quick_start.py
```

## Example Conversations

### Ordering a Pizza
```
You: I want a large pepperoni with stuffed crust, my name is Alex

Contoso Pizza: Yooo, alright Alex! 🍕 Let me lock that in - 
large pepperoni with stuffed crust. That's straight up fire. 
Anything else?
```

### The Pineapple Situation
```
You: I want a large with pineapple, I'm Jordan

Contoso Pizza: Wait wait wait... PINEAPPLE?? 💀 Nah fr fr that's 
wild, but yo I respect the chaos. Your pizza, your rules Jordan. 
Let's get this legend order done! 🍍
```

### Store Info
```
You: Where are your locations?

Contoso Pizza: We got multiple spots! Let me get you that info... 
[Store details] - which one hits different for you?
```

## Key Features Explained

✅ **Always Gets Your Name** - Before any order gets placed, the agent asks for your name

✅ **Boundary Setting** - Politely redirects non-pizza questions back to pizza ordering

✅ **Cheeky Pineapple Vibes** - Has opinions about pineapple but helps you anyway 😤

✅ **Gen-Alpha Language** - Uses slang naturally ("no cap", "fr fr", "slay") without trying too hard

✅ **Contoso Pizza Focused** - All about the brand and quality

## Project Structure

```
pizza_agent.py      # Main agent with Contoso personality
pizza_tools.py      # Business tools (ordering, store info, etc.)
quick_start.py      # Example usage
QUICKSTART.md       # Setup guide
```

## Architecture

- **Framework**: Microsoft Agent Framework
- **LLM**: Azure OpenAI (via Foundry) or GitHub Models
- **MCP**: Optional Pizza MCP server integration
- **Personality**: Gen-alpha, cheeky, pizza-focused