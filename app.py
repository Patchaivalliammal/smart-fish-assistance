import streamlit as st

# Fish data (recipes, cleaning, benefits)
FISH_DATA = {
    "Salmon": {
        "emoji": "🐟",
        "best_use": "Indian Style Curry",
        "cleaning": [
            "Remove head and tail.",
            "Cut open belly, remove guts.",
            "Rinse thoroughly with water.",
            "Debone carefully before cooking."
        ],
        "benefits": [
            "Rich in omega-3 fatty acids.",
            "Good source of protein.",
            "Supports heart and brain health."
        ],
        "recipes": {
            "Indian Curry": {
                "ingredients": [
                    "Salmon pieces",
                    "Onion, tomato, ginger, garlic",
                    "Chili powder, turmeric, garam masala",
                    "Coconut milk",
                    "Coriander leaves"
                ],
                "steps": [
                    "Heat oil, sauté onion, ginger, garlic.",
                    "Add tomato and spices, cook well.",
                    "Add salmon pieces and water/coconut milk.",
                    "Simmer until salmon is cooked.",
                    "Garnish with coriander leaves and serve."
                ]
            }
        }
    },
    "Tuna": {
        "emoji": "🐠",
        "best_use": "Deep Fry",
        "cleaning": [
            "Remove scales and fins.",
            "Cut into steaks or fillets.",
            "Wash with turmeric water to reduce smell."
        ],
        "benefits": [
            "High in lean protein.",
            "Contains essential vitamins B12 and D.",
            "Boosts metabolism and immunity."
        ],
        "recipes": {
            "Fried Tuna": {
                "ingredients": [
                    "Tuna slices",
                    "Chili powder, turmeric, salt",
                    "Rice flour or gram flour",
                    "Oil for frying"
                ],
                "steps": [
                    "Marinate tuna slices with spices and flour.",
                    "Heat oil in a pan.",
                    "Fry until golden brown.",
                    "Serve hot with lemon wedges."
                ]
            }
        }
    },
    "Shrimp": {
        "emoji": "🦐",
        "best_use": "Indian Spiced Side Dish",
        "cleaning": [
            "Remove head and legs.",
            "Peel off shell carefully.",
            "Devein shrimp before cooking."
        ],
        "benefits": [
            "Low in calories, high in protein.",
            "Rich in selenium and antioxidants.",
            "Supports skin and joint health."
        ],
        "recipes": {
            "Spicy Shrimp Fry": {
                "ingredients": [
                    "Shrimp",
                    "Onion, green chili, curry leaves",
                    "Chili powder, turmeric, pepper",
                    "Oil and salt"
                ],
                "steps": [
                    "Heat oil, add onions, curry leaves, and chili.",
                    "Add shrimp with spices.",
                    "Cook until shrimp turns pink and aromatic.",
                    "Serve with rice or roti."
                ]
            }
        }
    },
    "Crab": {
        "emoji": "🦀",
        "best_use": "Soup",
        "cleaning": [
            "Remove shell and claws.",
            "Take out gills and stomach sac.",
            "Wash thoroughly under running water."
        ],
        "benefits": [
            "Rich in zinc and phosphorus.",
            "Supports bone health.",
            "Boosts immunity and metabolism."
        ],
        "recipes": {
            "Crab Soup": {
                "ingredients": [
                    "Crab meat",
                    "Onion, ginger, garlic",
                    "Black pepper, turmeric, salt",
                    "Coriander and curry leaves"
                ],
                "steps": [
                    "Boil crab meat with turmeric and salt.",
                    "Sauté onion, ginger, garlic, and spices.",
                    "Add crab stock and simmer.",
                    "Garnish with coriander and serve hot."
                ]
            }
        }
    },
    "Octopus": {
        "emoji": "🐙",
        "best_use": "Grilled Dish",
        "cleaning": [
            "Remove ink sac, beak, and internal organs.",
            "Wash thoroughly with water.",
            "Tenderize before cooking (boil or pound lightly)."
        ],
        "benefits": [
            "Low in fat, high in protein.",
            "Rich in vitamin B12 and iron.",
            "Good for red blood cell production."
        ],
        "recipes": {
            "Grilled Octopus": {
                "ingredients": [
                    "Octopus tentacles",
                    "Olive oil, garlic, lemon juice",
                    "Paprika, salt, pepper"
                ],
                "steps": [
                    "Boil octopus until tender.",
                    "Marinate with olive oil, garlic, and spices.",
                    "Grill until slightly charred.",
                    "Serve with lemon wedges."
                ]
            }
        }
    }
}

st.set_page_config(page_title="Smart Fish Assistant", page_icon="🐟", layout="wide")

st.title("🐟 Smart Fish Assistant")
st.write("Select your favorite fish to discover recipes, cleaning steps, and health benefits.")

# Fish selection
fish_names = list(FISH_DATA.keys())
fish_choice = st.selectbox("Choose a fish:", fish_names)

if fish_choice:
    fish = FISH_DATA[fish_choice]
    st.header(f"{fish['emoji']} {fish_choice}")
    st.subheader(f"Best Use: {fish['best_use']}")

    tab1, tab2, tab3 = st.tabs(["🍲 Recipes", "🧼 Cleaning Steps", "💪 Benefits"])

    # Recipes Tab
    with tab1:
        recipe_names = list(fish["recipes"].keys())
        recipe_choice = st.radio("Select a recipe:", recipe_names)
        recipe = fish["recipes"][recipe_choice]
        
        st.write("### Ingredients")
        for ing in recipe["ingredients"]:
            st.checkbox(ing, key=f"{fish_choice}_{recipe_choice}_{ing}")
        
        st.write("### Steps")
        for step in recipe["steps"]:
            st.checkbox(step, key=f"{fish_choice}_{recipe_choice}_{step}")

    # Cleaning Tab
    with tab2:
        st.write("### How to Clean")
        for step in fish["cleaning"]:
            st.checkbox(step, key=f"{fish_choice}_clean_{step}")

    # Benefits Tab
    with tab3:
        st.write("### Health Benefits")
        for benefit in fish["benefits"]:
            st.markdown(f"✅ {benefit}")
