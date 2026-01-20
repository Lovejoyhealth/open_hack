# Getting Started with Contoso Pizza Agent

Your Gen-alpha pizza ordering assistant! 🍕

## Quick Setup (2 minutes)

1. **Install dependencies**:
```bash
pip install -r requirements.txt --pre
```

2. **Configure environment**:
```bash
cp .env.example .env
```

3. **Edit .env file** with your credentials:
   - For Azure AI Foundry: Set `AZURE_FOUNDRY_ENDPOINT` and `AZURE_CHAT_MODEL`
   - For GitHub Models: Set `GITHUB_TOKEN`
   - Optional: Set `PIZZA_MCP_URL` if you have a Pizza MCP server

4. **Authenticate** (if using Azure):
```bash
az login
```

## Running the Agent

### Interactive Mode (Recommended)
Chat with Contoso Pizza assistant:
```bash
python pizza_agent.py --interactive
```

### Demo Mode
See pre-built pizza ordering scenarios:
```bash
python pizza_agent.py --demo
```

### Quick Examples
Run curated examples:
```bash
python quick_start.py
```

## Example Interactions

### Ordering a Pizza
```
You: I want to order a large pizza with pepperoni, my name is Alex

Contoso: Yooo what's good! 🍕 Large pepperoni - that's what I'm talking about!
Got you Alex, let me ring this up... 
```

### Checking Store Info
```
You: Where are you located?

Contoso: We got three spots lowkey:
📍 Downtown Contoso - 123 Main Street
📍 North Side - 456 Oak Avenue  
📍 West Gate - 789 Park Lane
```

### The Pineapple Situation
```
You: Large pizza with pineapple please, I'm Jordan

Contoso: Wait wait wait... PINEAPPLE?? Nah fr fr that's wild 💀
But look, I got you - taking your order anyway! 
```

## Key Features

✅ **Pizza Ordering** - Size, crust, toppings with natural language
✅ **Customer Names** - Gets your name before finalizing orders  
✅ **Store Info** - Hours, locations, delivery details
✅ **Menu Info** - Sizes, crusts, toppings with pricing
✅ **Pineapple Reactions** - Friendly snark on controversial choices
✅ **Gen-alpha Personality** - "no cap", "fr fr", "lowkey", "slay" vibes

## The Personality

Contoso Pizza assistant is:
- **Friendly and helpful** - Always ready to assist 🤝
- **Cheeky and witty** - Quick with jokes and fun 😄
- **Authentic Gen-alpha** - Uses slang naturally, not forced
- **Pizza-focused** - Only helps with pizza ordering and store info
- **Respectful boundaries** - Gently redirects non-pizza questions

## File Structure

```
pizza_agent.py      # Main agent with Contoso personality
pizza_tools.py      # Pizza ordering tools
quick_start.py      # Example usage
requirements.txt    # Dependencies
.env.example        # Config template
README.md           # Full documentation
```

## Tips

- Be natural - talk how you normally would
- Agent will ask clarifying questions if needed
- Name collection happens before order finalization
- Type 'help' for example prompts (in interactive mode)
- Pineapple orders get a playful reaction but are honored

## Troubleshooting

**"Authentication error"**
- Run `az login` (for Azure)
- Check .env has correct credentials

**"Agent not responding"**  
- Verify `CHAT_CLIENT` setting (azure or github)
- Check internet connection to AI service

**"MCP connection failed"**
- The MCP server connection is optional
- Agent will work fine without it for core features

**"Tool not found"**
- Make sure you installed with `--pre` flag
- Try: `pip install agent-framework-azure-ai --pre`

## Next Steps

1. Try the interactive mode: `python pizza_agent.py`
2. Explore different scenarios
3. Customize the brand personality in `pizza_agent.py`
4. Add your own tools in `pizza_tools.py`
5. Connect to your Pizza MCP server

Happy ordering! 🍕
