def insert_user_info_into_story(user_name, favorite_food, your_city):
    # Read the contents of the short story
    with open("d:\Python Project\short_story.txt", "r") as file:
  # Replace "/path/to/short_story.txt" with the full path to your file
        story_content = file.read()

    # Replace "yoki" with the user's name, "grub" with favorite food, and "home" with your city in the story
    updated_story = story_content.replace("yoki", user_name).replace("grub", favorite_food).replace("home", your_city)

    # Write the updated story to a new file
    with open("d:\Python Project\short_story_new.txt", "w") as new_file:
        new_file.write(updated_story)

# Get user inputs
user_name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
your_city = input("Enter your city: ")

# Insert the user's information into the story and write to a new file
insert_user_info_into_story(user_name, favorite_food, your_city)

print("User information inserted into the story and saved as short_story_new.txt successfully!")

