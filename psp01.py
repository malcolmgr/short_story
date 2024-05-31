import os

def insert_user_info_into_story(user_name, favorite_food, your_city, social_media_app):
    # Get the directory of the current Python script
    current_directory = os.path.dirname(os.path.realpath(__file__))
    
    # Construct the path to the input file in the same directory
    input_file_path = os.path.join(current_directory, "short_story.txt")
    
    # Construct the path to the output file in the same directory
    output_file_path = os.path.join(current_directory, "short_story_new.txt")

    try:
        # Read the contents of the short story
        with open(input_file_path, "r") as file:
            story_content = file.read()

        # Replace placeholders with user inputs in the story
        updated_story = story_content.replace("yoki", user_name).replace("grub", favorite_food).replace("home", your_city).replace("social_media_app", social_media_app)

        # Write the updated story to a new file
        with open(output_file_path, "w") as new_file:
            new_file.write(updated_story)

        print("User information inserted into the story and saved as short_story_new.txt successfully!")
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get user inputs
user_name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
your_city = input("Enter your city: ")
social_media_app = input("Enter your favorite social media app: ")

# Insert the user's information into the story and write to a new file
insert_user_info_into_story(user_name, favorite_food, your_city, social_media_app)
