import os

def insert_user_info_into_story(user_name, favorite_food, your_city, social_media_app, input_file="short_story.txt", output_file="short_story_new.txt"):
    """
    Insert user information into a story and save it to a new file.

    Args:
        user_name (str): User's name.
        favorite_food (str): User's favorite food.
        your_city (str): User's city.
        social_media_app (str): User's favorite social media app.
        input_file (str): The name of the input file containing the story template.
        output_file (str): The name of the output file to save the updated story.
    """
    try:
        # Get the directory of the current Python script
        current_directory = os.path.dirname(os.path.realpath(__file__))
        
        # Construct the full path to the input and output files
        input_file_path = os.path.join(current_directory, input_file)
        output_file_path = os.path.join(current_directory, output_file)

        # Read the contents of the short story
        with open(input_file_path, "r") as file:
            story_content = file.read()

        # Replace placeholders with user inputs in the story
        updated_story = story_content.format(user_name=user_name, favorite_food=favorite_food, your_city=your_city, social_media_app=social_media_app)

        # Write the updated story to a new file
        with open(output_file_path, "w") as new_file:
            new_file.write(updated_story)

        print(f"User information inserted into the story and saved as {output_file} successfully!")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get user inputs
user_name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
your_city = input("Enter your city: ")
social_media_app = input("Enter your favorite social media app: ")

# Insert the user's information into the story and write to a new file
insert_user_info_into_story(user_name, favorite_food, your_city, social_media_app)
