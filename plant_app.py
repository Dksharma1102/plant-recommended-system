import streamlit as st
from PIL import Image
import io

# Set page config with attractive theme
st.set_page_config(
    page_title="🌿 GreenThumb Guide",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background-color: #f5faf5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    .stRadio>div {
        flex-direction: row;
        gap: 20px;
    }
    .stRadio>div>label {
        margin-right: 20px;
    }
    .stExpander {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stDownloadButton>button {
        background-color: #2196F3;
        color: white;
    }
    .stDownloadButton>button:hover {
        background-color: #0b7dda;
        color: white;
    }
    .header {
        color: #2E7D32;
        text-align: center;
        margin-bottom: 30px;
    }
    .subheader {
        color: #388E3C;
        border-bottom: 2px solid #C8E6C9;
        padding-bottom: 5px;
    }
    .area-input {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# App header with logo
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2910/2910765.png", width=100)
    st.markdown("<h1 class='header'>🌿 GreenThumb Guide</h1>", unsafe_allow_html=True)
    st.markdown("### Your personal gardening assistant")

# Function to create a text file with growing instructions
def create_instruction_file(plant_info):
    content = f"Plant Name: {plant_info['name']}\n"
    content += f"Recommended Quantity: {plant_info['total']} plants\n"
    content += f"Quick Tips: {plant_info['tips']}\n\n"
    content += "Growing Instructions:\n"
    for instruction in plant_info["growing_instructions"]:
        content += f"- {instruction}\n"
    return content

# Expanded plant database with more varieties and detailed instructions
def get_plant_database():
    return {
        "Sandy": {
            "High": [
                {
                    "name": "Carrots (Nantes)", 
                    "plants_per_sqft": 16, 
                    "tips": "Sweet and crisp, perfect for sandy soils.",
                    "growing_instructions": [
                        "🌱 Planting: Sow seeds 1/4 inch deep, 2 inches apart in rows 12 inches apart",
                        "💧 Watering: 1 inch per week, more during dry spells",
                        "☀️ Sunlight: Full sun (6-8 hours daily)",
                        "🌱 Germination: 14-21 days at 55-75°F",
                        "🔄 Thinning: Thin to 3 inches apart when 2 inches tall",
                        "🍃 Fertilizing: Low nitrogen fertilizer 5 weeks after planting",
                        "⏳ Harvest: 50-75 days when 1/2 to 1 inch diameter",
                        "🐛 Pests: Watch for carrot rust flies - use row covers"
                    ],
                    "image": "https://minnetonkaorchards.com/wp-content/uploads/2023/03/Market-display-of-carrots-SS-789443206-1080x720.jpg"
                },
                {
                    "name": "Radishes (Cherry Belle)", 
                    "plants_per_sqft": 16, 
                    "tips": "Fast-growing and perfect for beginners.",
                    "growing_instructions": [
                        "🌱 Planting: Sow seeds 1/2 inch deep, 1 inch apart",
                        "💧 Watering: Keep evenly moist (about 1 inch per week)",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "🌱 Germination: 3-10 days at 55-85°F",
                        "🔄 Succession Planting: Sow every 2 weeks for continuous harvest",
                        "⏳ Harvest: 22-30 days when 1 inch in diameter",
                        "🌡️ Temperature: Best in cool weather (60-65°F)",
                        "🍽️ Companion Plants: Plant with carrots and lettuce"
                    ],
                    "image": "https://th.bing.com/th/id/OIP.rjkZ2IpUc033uJzDCnvF9QHaIQ?rs=1&pid=ImgDetMain"
                },
                {
                    "name": "Sweet Potatoes (Beauregard)", 
                    "plants_per_sqft": 1, 
                    "tips": "Thrives in loose, sandy soil with good drainage.",
                    "growing_instructions": [
                        "🌱 Planting: Plant slips 12-18 inches apart in rows 3 feet apart",
                        "💧 Watering: 1 inch per week, reduce watering 3-4 weeks before harvest",
                        "☀️ Sunlight: Full sun (6-8 hours daily)",
                        "🌡️ Temperature: Needs warm soil (70°F+)",
                        "⏳ Growing Season: 90-120 days to maturity",
                        "🍃 Fertilizing: Use low-nitrogen, high-potassium fertilizer",
                        "🔄 Vine Care: Lift vines occasionally to prevent rooting at joints",
                        "⏳ Harvest: When leaves yellow or before first frost"
                    ],
                    "image": "https://th.bing.com/th/id/OIP.GO6VynEDVq4kjcyuT99zbAAAAA?rs=1&pid=ImgDetMain"
                }
            ],
            "Low": [
                {
                    "name": "Prickly Pear Cactus", 
                    "plants_per_sqft": 1, 
                    "tips": "Extremely drought-tolerant with edible fruits.",
                    "growing_instructions": [
                        "🌱 Planting: Plant pads 2-3 feet apart in spring",
                        "💧 Watering: Only during extended droughts once established",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "🌡️ Temperature: Hardy to 0°F when established",
                        "✂️ Pruning: Wear thick gloves and use tongs to handle",
                        "🌸 Bloom: Yellow or red flowers in late spring",
                        "🍇 Harvest: Fruits ripen in late summer to fall",
                        "⚠️ Warning: Handle with extreme care due to spines"
                    ],
                    "image": "https://gardenerspath.com/wp-content/uploads/2022/03/Ornamental-Prickly-Pear-Growing-in-the-Landscape.jpg"
                },
                {
                    "name": "Lavender (English)", 
                    "plants_per_sqft": 1, 
                    "tips": "Fragrant and drought-resistant perennial.",
                    "growing_instructions": [
                        "🌱 Planting: Space plants 18-24 inches apart",
                        "💧 Watering: Water deeply but infrequently once established",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "✂️ Pruning: Cut back by 1/3 in early spring",
                        "🌸 Bloom: Summer months (June-August)",
                        "🌿 Harvest: Cut stems when flowers just begin to open",
                        "🌱 Propagation: Take cuttings in early summer",
                        "❄️ Winter Care: Mulch in cold climates"
                    ],
                    "image": "https://th.bing.com/th/id/OIP.dIUTPj-h5y8aNVQJSo9dTwHaEK?rs=1&pid=ImgDetMain"
                },
                {
                    "name": "Yucca (Adam's Needle)", 
                    "plants_per_sqft": 1, 
                    "tips": "Architectural plant with dramatic flower spikes.",
                    "growing_instructions": [
                        "🌱 Planting: Space plants 3-4 feet apart",
                        "💧 Watering: Drought tolerant once established",
                        "☀️ Sunlight: Full sun to partial shade",
                        "🌸 Bloom: Tall white flower spikes in early summer",
                        "✂️ Maintenance: Remove dead leaves and spent flower stalks",
                        "🌱 Propagation: Divide offsets in spring",
                        "⚠️ Warning: Leaves have sharp points - handle with care",
                        "🔄 Growth Rate: Slow growing but long-lived"
                    ],
                    "image": "https://img.crocdn.co.uk/images/products2/pl/00/00/00/45/pl0000004538.jpg?width=940&height=940"
                }
            ]
        },
        "Clay": {
            "High": [
                {
                    "name": "Broccoli (Calabrese)", 
                    "plants_per_sqft": 1, 
                    "tips": "Produces large central heads and side shoots.",
                    "growing_instructions": [
                        "🌱 Planting: Start seeds indoors 6-8 weeks before last frost",
                        "💧 Watering: 1-1.5 inches per week",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "🌱 Transplant: Set plants 18 inches apart",
                        "🍃 Fertilizing: Use nitrogen-rich fertilizer",
                        "⏳ Harvest: Cut main head when florets are tight",
                        "🌱 Side Shoots: Continue harvesting side shoots for weeks",
                        "🐛 Pests: Protect from cabbage worms with row covers"
                    ],
                    "image": "https://www.gardeningknowhow.com/wp-content/uploads/2021/06/calabrese-690x518.jpg"
                },
                {
                    "name": "Cabbage (Early Jersey Wakefield)", 
                    "plants_per_sqft": 1, 
                    "tips": "Pointed heads mature earlier than round varieties.",
                    "growing_instructions": [
                        "🌱 Planting: Start seeds indoors 6-8 weeks before last frost",
                        "💧 Watering: Keep soil consistently moist",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "🌱 Transplant: Set plants 12-24 inches apart",
                        "🍃 Fertilizing: Use balanced fertilizer every 3-4 weeks",
                        "⏳ Harvest: When heads feel solid and firm",
                        "❄️ Storage: Keeps well in cool conditions",
                        "🐛 Pests: Watch for cabbage loopers and aphids"
                    ],
                    "image": "https://th.bing.com/th/id/OIP.vI52fv0-LuU91TQVZTC9tgHaF2?rs=1&pid=ImgDetMain"
                },
                {
                    "name": "Brussels Sprouts (Long Island Improved)", 
                    "plants_per_sqft": 1, 
                    "tips": "Flavor improves after frost exposure.",
                    "growing_instructions": [
                        "🌱 Planting: Start seeds indoors 16-20 weeks before first fall frost",
                        "💧 Watering: 1-1.5 inches per week",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "🌱 Transplant: Set plants 24 inches apart",
                        "🍃 Fertilizing: Side-dress with nitrogen fertilizer 4 weeks after transplanting",
                        "✂️ Pruning: Remove lower leaves as sprouts develop",
                        "⏳ Harvest: Pick sprouts from bottom up when firm",
                        "❄️ Frost Benefit: Flavor sweetens after light frosts"
                    ],
                    "image": "https://th.bing.com/th/id/OIP._odf5HTne7-O4n18EasxdQHaHa?rs=1&pid=ImgDetMain"
                }
            ],
            "Low": [
                {
                    "name": "Daylilies (Stella d'Oro)", 
                    "plants_per_sqft": 4, 
                    "tips": "Reblooming variety with golden yellow flowers.",
                    "growing_instructions": [
                        "🌱 Planting: Space plants 12-18 inches apart",
                        "💧 Watering: Weekly during first growing season",
                        "☀️ Sunlight: Full sun to partial shade",
                        "✂️ Deadheading: Remove spent blooms daily",
                        "🌸 Bloom: Reblooms throughout summer",
                        "🍃 Fertilizing: Light feeding in early spring",
                        "🔄 Division: Divide every 3-4 years in early spring",
                        "🌱 Propagation: Divide clumps or plant seeds"
                    ],
                    "image": "https://wgi-img.s3.amazonaws.com/VarietyImage/e80af674c0ec7e7545ae43dc97684ae1.jpg"
                },
                {
                    "name": "Russian Sage (Perovskia)", 
                    "plants_per_sqft": 1, 
                    "tips": "Airy purple flowers on silvery foliage.",
                    "growing_instructions": [
                        "🌱 Planting: Space plants 2-3 feet apart",
                        "💧 Watering: Water deeply but infrequently",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "✂️ Pruning: Cut back to 6 inches in early spring",
                        "🌸 Bloom: Summer to fall (July-September)",
                        "🍃 Foliage: Fragrant when crushed",
                        "🐝 Wildlife: Attracts bees and butterflies",
                        "❄️ Hardiness: Drought and cold tolerant"
                    ],
                    "image": "https://th.bing.com/th/id/OIP.co1ANUA93FwCQ76_V-1sqAHaHa?rs=1&pid=ImgDetMain"
                },
                {
                    "name": "Sedum (Autumn Joy)", 
                    "plants_per_sqft": 1, 
                    "tips": "Succulent leaves with changing flower colors.",
                    "growing_instructions": [
                        "🌱 Planting: Space plants 18-24 inches apart",
                        "💧 Watering: Only during extended drought",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "🌸 Bloom: Flowers change from pink to copper-red",
                        "✂️ Pruning: Cut back in early spring",
                        "🌱 Propagation: Divide in spring or take stem cuttings",
                        "🐝 Wildlife: Attracts butterflies",
                        "❄️ Winter Interest: Dried flower heads remain attractive"
                    ],
                    "image": "https://www.birdsandblooms.com/wp-content/uploads/2023/05/Sedum-Autumn-Joy-Herbstfreude-0002-high-res.jpg?w=1200"
                }
            ]
        },
        "Loamy": {
            "High": [
                {
                    "name": "Tomatoes (Brandywine)", 
                    "plants_per_sqft": 1, 
                    "tips": "Heirloom variety with exceptional flavor.",
                    "growing_instructions": [
                        "🌱 Planting: Start seeds indoors 6-8 weeks before last frost",
                        "💧 Watering: 1-2 inches per week (avoid wetting leaves)",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "🌱 Transplant: Set plants 24-36 inches apart",
                        "🔼 Support: Use sturdy cages or stakes",
                        "✂️ Pruning: Remove suckers below first flower cluster",
                        "⏳ Harvest: When fully colored but slightly firm",
                        "🍃 Fertilizing: Use balanced fertilizer at planting and when fruiting"
                    ],
                    "image": "https://th.bing.com/th/id/OIP.IirW1JuhXgaZUcYwsHYFeAAAAA?rs=1&pid=ImgDetMain"
                },
                {
                    "name": "Peppers (California Wonder)", 
                    "plants_per_sqft": 1, 
                    "tips": "Classic bell pepper with thick walls.",
                    "growing_instructions": [
                        "🌱 Planting: Start seeds indoors 8-10 weeks before last frost",
                        "💧 Watering: 1-2 inches per week (consistent moisture)",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "🌱 Transplant: Set plants 18-24 inches apart",
                        "🌡️ Temperature: Wait until soil is warm (65°F+)",
                        "🍃 Fertilizing: Use calcium-rich fertilizer to prevent blossom end rot",
                        "⏳ Harvest: Can pick green or wait for red color",
                        "🌶️ Varieties: Turns from green to red when fully ripe"
                    ],
                    "image": "https://th.bing.com/th/id/OIP.OGCCWW6OBEyh20wy1phouQHaHa?rs=1&pid=ImgDetMain"
                },
                {
                    "name": "Cucumbers (Straight Eight)", 
                    "plants_per_sqft": 2, 
                    "tips": "Slicing cucumber with excellent flavor.",
                    "growing_instructions": [
                        "🌱 Planting: Sow seeds directly after last frost",
                        "💧 Watering: 1-2 inches per week (consistent moisture)",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "🌱 Spacing: 12 inches apart in rows 5-6 feet apart",
                        "🔼 Trellising: Grow vertically to save space",
                        "⏳ Harvest: When 8 inches long for best flavor",
                        "🌸 Pollination: Needs pollination for fruit set",
                        "🍃 Fertilizing: Use balanced fertilizer every 3-4 weeks"
                    ],
                    "image": "https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_416,h_312/https://cucumbershop.com/wp-content/uploads/2023/11/straight-eight-cucumber_101.jpg"
                }
            ],
            "Low": [
                {
                    "name": "Rosemary (Arp)", 
                    "plants_per_sqft": 1, 
                    "tips": "Cold-hardy variety with aromatic leaves.",
                    "growing_instructions": [
                        "🌱 Planting: Space plants 24-36 inches apart",
                        "💧 Watering: Let soil dry between waterings",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "✂️ Pruning: Trim lightly after flowering",
                        "🌿 Harvest: Cut stems as needed",
                        "❄️ Winter Care: Mulch in cold climates",
                        "🌱 Propagation: Take cuttings in early summer",
                        "🍽️ Uses: Great for cooking and ornamental gardens"
                    ],
                    "image": "https://seeds2plate.com/wp-content/uploads/2021/03/Rosemary-600x602.jpeg"
                },
                {
                    "name": "Thyme (English)", 
                    "plants_per_sqft": 4, 
                    "tips": "Low-growing herb with tiny fragrant leaves.",
                    "growing_instructions": [
                        "🌱 Planting: Space plants 12 inches apart",
                        "💧 Watering: Water only when soil is dry",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "✂️ Pruning: Cut back by 1/3 in spring",
                        "🌿 Harvest: Cut stems as needed",
                        "🌸 Bloom: Tiny purple flowers attract bees",
                        "🌱 Propagation: Divide in spring or take cuttings",
                        "🍽️ Uses: Essential for French and Mediterranean cooking"
                    ],
                    "image": "https://th.bing.com/th/id/OIP.5fwZF4q9X6_YRQLWPl6cYgHaHa?rs=1&pid=ImgDetMain"
                },
                {
                    "name": "Oregano (Greek)", 
                    "plants_per_sqft": 2, 
                    "tips": "More flavorful than common oregano.",
                    "growing_instructions": [
                        "🌱 Planting: Space plants 12-18 inches apart",
                        "💧 Watering: Drought tolerant once established",
                        "☀️ Sunlight: Full sun (6+ hours daily)",
                        "✂️ Pruning: Cut back in spring to encourage bushiness",
                        "🌿 Harvest: Just before flowering for best flavor",
                        "🌸 Bloom: Small white flowers in summer",
                        "🌱 Propagation: Divide plants or take cuttings",
                        "🍽️ Uses: Essential for Italian and Greek cuisine"
                    ],
                    "image": "https://theoliveoiltaproom.com/wp-content/uploads/2020/03/36706580_m.jpg"
                }
            ]
        }
    }

# Function to get plant recommendations
def get_recommendations(soil_type, water_availability, area):
    plant_db = get_plant_database()
    recommendations = []
    
    for plant in plant_db.get(soil_type, {}).get(water_availability, []):
        total_plants = int(area * plant["plants_per_sqft"])
        recommendations.append({
            "name": plant["name"],
            "total": total_plants,
            "tips": plant["tips"],
            "growing_instructions": plant.get("growing_instructions", []),
            "image": plant.get("image", "https://cdn-icons-png.flaticon.com/512/2910/2910765.png")
        })
    
    return recommendations

# Main app function
def main():
    # Image upload section
    with st.container():
        st.markdown("<h2 class='subheader'>📸 Upload Your Planting Area</h2>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Your Planting Area", width=400)
            
            # Area input section
            with st.container():
                st.markdown("<h3 class='subheader'>📏 Planting Area Size</h3>", unsafe_allow_html=True)
                area = st.number_input(
                    "Enter your planting area size (square feet):",
                    min_value=10,
                    max_value=1000,
                    value=100,
                    step=10
                )
                st.write(f"Selected area: {area} square feet")
            
            # Soil and water selection
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("<h3 class='subheader'>🌱 Soil Type</h3>", unsafe_allow_html=True)
                soil_type = st.selectbox("", ["Sandy", "Clay", "Loamy"], label_visibility="collapsed")
            
            with col2:
                st.markdown("<h3 class='subheader'>💧 Water Availability</h3>", unsafe_allow_html=True)
                water_availability = st.radio(
                    "",
                    ["High", "Low"],
                    horizontal=True,
                    label_visibility="collapsed"
                )
            
            # Get recommendations button
            if st.button("✨ Get Personalized Recommendations", use_container_width=True):
                recommendations = get_recommendations(soil_type, water_availability, area)
                
                if recommendations:
                    st.success("🎉 Here are your customized plant recommendations!")
                    st.balloons()
                    
                    for rec in recommendations:
                        with st.expander(f"🌿 {rec['name']} (Up to {rec['total']} plants)", expanded=True):
                            col_img, col_info = st.columns([1,3])
                            with col_img:
                                st.image(rec["image"], width=150)
                            
                            with col_info:
                                st.markdown(f"**🔍 Quick Tips:** {rec['tips']}")
                                
                                st.markdown("**📝 Growing Instructions:**")
                                for instruction in rec["growing_instructions"]:
                                    st.markdown(f"- {instruction}")
                                
                                # Download button
                                instruction_content = create_instruction_file(rec)
                                st.download_button(
                                    label=f"📥 Download {rec['name']} Guide",
                                    data=instruction_content,
                                    file_name=f"{rec['name'].replace(' ', '_')}_growing_guide.txt",
                                    mime="text/plain"
                                )
                                
                                # Additional resources
                                st.markdown("**🔗 Learn More:**")
                                st.markdown(f"""
                                - [🌐 Detailed Growing Guide](https://www.google.com/search?q={rec['name'].replace(' ', '+')}+growing+guide)
                                - [🎥 Care Video Tutorial](https://www.youtube.com/results?search_query={rec['name'].replace(' ', '+')}+growing)
                                """)
                else:
                    st.warning("No recommendations found for your criteria. Please try different options.")
        else:
            st.info("👆 Upload an image of your planting area to get started")

if __name__ == "__main__":
    main()