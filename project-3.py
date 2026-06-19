# Simple Recommendation System

# Dictionary containing categories and recommendations
recommendations = {
    "movies": [
        "Inception",
        "Interstellar",
        "The Dark Knight"
    ],
    "books": [
        "Atomic Habits",
        "The Alchemist",
        "Rich Dad Poor Dad"
    ],
    "sports": [
        "Football",
        "Cricket",
        "Basketball"
    ],
    "music": [
        "Pop",
        "Rock",
        "Classical"
    ],
    "technology": [
        "Artificial Intelligence",
        "Data Science",
        "Cybersecurity"
    ]
}

print("=== Simple Recommendation System ===")
print("\nAvailable Interests:")
print("Movies, Books, Sports, Music, Technology")

# Take user input
user_interest = input("\nEnter your interest: ").lower()

# Match preferences and display recommendations
if user_interest in recommendations:
    print("\nRecommended Items for You:")
    
    for item in recommendations[user_interest]:
        print("-", item)

else:
    print("\nSorry, no recommendations found for that interest.")