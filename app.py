import streamlit as st

# =========================
# Fish Data
# =========================
FISH_DATA = {
    "Salmon": {
        "emoji": "🐟",
        "image": "https://www.themealdb.com/images/ingredients/Salmon.png",
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
        "image": "https://www.themealdb.com/images/ingredients/Tuna.png",
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
        "image": "https://www.themealdb.com/images/ingredients/Shrimp.png",
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
    "Mackerel": {
        "emoji": "🐡",
        "image": "https://www.themealdb.com/images/ingredients/Mackerel.png",
        "best_use": "Grilled or Curry",
        "cleaning": [
            "Remove scales.",
            "Cut open belly, remove guts.",
            "Wash thoroughly with salt water."
        ],
        "benefits": [
            "High in omega-3.",
            "Supports brain and heart health.",
            "Improves skin glow."
        ],
        "recipes": {
            "Grilled Mackerel": {
                "ingredients": [
                    "Mackerel",
                    "Lemon juice, garlic, salt, pepper",
                    "Olive oil"
                ],
                "steps": [
                    "Marinate fish with spices.",
                    "Grill until golden and cooked inside.",
                    "Serve with salad or rice."
                ]
            }
        }
    }
}

# =========================
# Streamlit UI
# =========================
st.set_page_config(page_title="Smart Fish Assistant", page_icon="🐟", layout="wide")

st.markdown(
    """
    <h1 style='text-align:center; color:#1f77b4;'>🐟 Smart Fish Assistant</h1>
    <p style='text-align:center; font-size:18px; color:#555;'>
    Discover recipes, cleaning steps, and health benefits of your favorite seafood!
    </p>
    """,
    unsafe_allow_html=True
)

# Fish selection
fish_names = list(FISH_DATA.keys())
fish_choice = st.selectbox("🎣 Choose a fish:", fish_names)

if fish_choice:
    fish = FISH_DATA[fish_choice]

    st.image(fish["image"], width=200)
    st.markdown(
        f"<h2 style='color:#ff6347;'>{fish['emoji']} {fish_choice}</h2>",
        unsafe_allow_html=True
    )
    st.subheader(f"🍴 Best Use: {fish['best_use']}")

    tab1, tab2, tab3 = st.tabs(["🍲 Recipes", "🧼 Cleaning Steps", "💪 Benefits"])

    # Recipes Tab
    with tab1:
        recipe_names = list(fish["recipes"].keys())
        recipe_choice = st.radio("📌 Select a recipe:", recipe_names)
        recipe = fish["recipes"][recipe_choice]

        st.success("### 🥗 Ingredients")
        for ing in recipe["ingredients"]:
            st.checkbox(ing, key=f"{fish_choice}_{recipe_choice}_{ing}")

        st.info("### 👨‍🍳 Cooking Steps")
        progress = 0
        for step in recipe["steps"]:
            if st.checkbox(step, key=f"{fish_choice}_{recipe_choice}_{step}"):
                progress += 1

        st.progress(progress / len(recipe["steps"]))

    # Cleaning Tab
    with tab2:
        st.warning("### 🧽 How to Clean")
        for step in fish["cleaning"]:
            st.checkbox(step, key=f"{fish_choice}_clean_{step}")

    # Benefits Tab
    with tab3:
        st.success("### 🌿 Health Benefits")
        for benefit in fish["benefits"]:
            st.markdown(f"<p style='color:green;'>✅ {benefit}</p>", unsafe_allow_html=True)
