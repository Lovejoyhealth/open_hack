"""Contoso Pizza business tools and helper functions."""

from typing import Annotated


def get_pizza_menu(
    category: Annotated[str, "Category: 'sizes', 'crusts', 'toppings', or 'all'"] = "all"
) -> str:
    """
    Get information about Contoso Pizza menu items.
    
    Args:
        category: What menu info to return
    
    Returns:
        Menu information
    """
    menu = {
        "sizes": {
            "Small": "8-inch, 6 slices, feeds 1-2 people",
            "Medium": "10-inch, 8 slices, feeds 2-3 people",
            "Large": "12-inch, 10 slices, feeds 3-4 people",
            "XL": "14-inch, 12 slices, feeds 4-5 people"
        },
        "crusts": {
            "Thin": "Crispy and light",
            "Regular": "Classic thickness, our standard",
            "Pan": "Deep dish, thick and fluffy",
            "Stuffed": "Crust filled with cheese - extra fire 🔥"
        },
        "toppings": {
            "Meats": ["Pepperoni", "Sausage", "Bacon", "Ham", "Chicken"],
            "Veggies": ["Mushroom", "Onion", "Bell Pepper", "Black Olives", "Spinach", "Tomato", "Broccoli"],
            "Cheese": ["Extra Cheese", "Feta", "Gouda"],
            "Special": ["Pineapple (at your own risk 😤)", "Jalapeños", "Garlic"]
        }
    }
    
    if category.lower() == "sizes":
        items = menu["sizes"]
        return "🍕 **Contoso Pizza Sizes:**\n" + "\n".join([f"• **{k}**: {v}" for k, v in items.items()])
    
    elif category.lower() == "crusts":
        items = menu["crusts"]
        return "🥖 **Crust Options:**\n" + "\n".join([f"• **{k}**: {v}" for k, v in items.items()])
    
    elif category.lower() == "toppings":
        result = "🍕 **Available Toppings:**\n"
        for cat, items in menu["toppings"].items():
            result += f"\n**{cat}**: {', '.join(items)}\n"
        return result
    
    else:  # all
        return """🍕 **CONTOSO PIZZA FULL MENU**

**Sizes:**
• Small (8\") - 6 slices
• Medium (10\") - 8 slices  
• Large (12\") - 10 slices
• XL (14\") - 12 slices

**Crusts:**
• Thin - crispy
• Regular - classic
• Pan - deep dish
• Stuffed - extra 🔥

**Toppings:**
Meats: Pepperoni, Sausage, Bacon, Ham, Chicken
Veggies: Mushroom, Onion, Bell Pepper, Olives, Spinach, Tomato, Broccoli
Cheese: Extra Cheese, Feta, Gouda
Special: Pineapple (we have thoughts 😤), Jalapeños, Garlic"""


def get_store_info(
    store_id: Annotated[str, "Store identifier or 'all' for all locations"] = "all"
) -> str:
    """
    Get information about Contoso Pizza store locations.
    
    Args:
        store_id: Store identifier or 'all'
    
    Returns:
        Store information
    """
    stores = {
        "downtown": {
            "name": "Downtown Contoso",
            "address": "123 Main Street, Downtown",
            "phone": "(555) 123-4567",
            "hours": "Mon-Thu: 11AM-10PM, Fri-Sat: 11AM-12AM, Sun: 12PM-9PM",
            "delivery": "Yes, 5 mile radius",
            "parking": "Street parking available"
        },
        "northside": {
            "name": "North Side Contoso",
            "address": "456 Oak Avenue, North District",
            "phone": "(555) 234-5678",
            "hours": "Mon-Sun: 11AM-11PM",
            "delivery": "Yes, 3 mile radius",
            "parking": "Dedicated lot"
        },
        "westgate": {
            "name": "West Gate Contoso",
            "address": "789 Park Lane, West End",
            "phone": "(555) 345-6789",
            "hours": "Mon-Sun: 10AM-11PM",
            "delivery": "Yes, 4 mile radius",
            "parking": "Mall parking"
        }
    }
    
    if store_id.lower() == "all":
        result = "📍 **CONTOSO PIZZA LOCATIONS**\n\n"
        for store_key, store_data in stores.items():
            result += f"**{store_data['name']}**\n"
            result += f"📌 {store_data['address']}\n"
            result += f"📞 {store_data['phone']}\n"
            result += f"🕐 {store_data['hours']}\n"
            result += f"🚚 {store_data['delivery']}\n"
            result += f"🅿️  {store_data['parking']}\n\n"
        return result
    
    store = stores.get(store_id.lower(), stores["downtown"])
    
    return f"""📍 **{store['name']}**
📌 Location: {store['address']}
📞 Phone: {store['phone']}
🕐 Hours: {store['hours']}
🚚 Delivery: {store['delivery']}
🅿️  Parking: {store['parking']}"""


def create_order_summary(
    customer_name: Annotated[str, "Customer's name"],
    size: Annotated[str, "Pizza size (Small, Medium, Large, XL)"],
    crust: Annotated[str, "Crust type (Thin, Regular, Pan, Stuffed)"],
    toppings: Annotated[str, "Toppings (comma-separated)"]
) -> str:
    """
    Create an order summary for confirmation.
    
    Args:
        customer_name: Customer name
        size: Pizza size
        crust: Crust type
        toppings: Toppings list
    
    Returns:
        Order summary
    """
    # Simple pricing
    size_price = {
        "small": 8.99,
        "medium": 11.99,
        "large": 14.99,
        "xl": 17.99
    }
    
    base_price = size_price.get(size.lower(), 11.99)
    topping_count = len([t.strip() for t in toppings.split(",") if t.strip()])
    topping_price = topping_count * 1.50
    total = base_price + topping_price
    tax = total * 0.08
    final_total = total + tax
    
    # Check for pineapple
    pineapple_note = ""
    if "pineapple" in toppings.lower():
        pineapple_note = "\n⚠️  *pineapple detected - your chaos, your order* 💀"
    
    return f"""✅ **ORDER SUMMARY FOR {customer_name.upper()}**

🍕 **Order Details:**
• Size: {size}
• Crust: {crust}
• Toppings: {toppings}

💰 **Pricing:**
• Base Pizza: ${base_price:.2f}
• Toppings ({topping_count}): ${topping_price:.2f}
• Subtotal: ${total:.2f}
• Tax: ${tax:.2f}
• **TOTAL: ${final_total:.2f}**

{pineapple_note}

Ready to lock this in?"""


def validate_order(
    size: Annotated[str, "Size to validate"],
    crust: Annotated[str, "Crust to validate"],
    toppings: Annotated[str, "Toppings to validate"]
) -> str:
    """
    Validate that an order has valid options.
    
    Args:
        size: Pizza size
        crust: Crust type
        toppings: Toppings list
    
    Returns:
        Validation result
    """
    valid_sizes = ["small", "medium", "large", "xl"]
    valid_crusts = ["thin", "regular", "pan", "stuffed"]
    
    issues = []
    
    if size.lower() not in valid_sizes:
        issues.append(f"❌ '{size}' is not a valid size. Try: {', '.join(valid_sizes)}")
    
    if crust.lower() not in valid_crusts:
        issues.append(f"❌ '{crust}' is not a valid crust. Try: {', '.join(valid_crusts)}")
    
    if not toppings or toppings.strip() == "":
        issues.append("⚠️  No toppings selected - want to add any?")
    
    if issues:
        return "\n".join(issues)
    else:
        return "✅ Order looks valid! Ready to confirm?"
