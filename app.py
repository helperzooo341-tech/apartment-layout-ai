def analyze_apartment(description):
    return f"""
AI Analysis of apartment:

Input:
{description}

Suggestions:
- Optimize space with multifunctional furniture
- Place storage near entrance
- Keep living room open and bright
- Use zoning between kitchen and living area

Real estate description:
This apartment is well-optimized for comfortable urban living, with efficient use of space and functional layout.
"""

print("Apartment Layout AI")
print("Write apartment description:")
user_input = input()

print(analyze_apartment(user_input))
