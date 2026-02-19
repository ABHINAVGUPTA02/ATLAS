import os
import datetime

def save_to_document(response_text: str, directory: str = "./output"):
    """
    Saves the response text to a document in the specified directory.
    """
    os.makedirs(directory, exist_ok=True)

    markdown_content = f"""🗺️ AI Travel Plan

    # **Generated:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    # **CreatedBy:** Atlas 

    ---

    {response_text}

    ---

    *This travel plan was created using AI technology. Please verify all information before making travel arrangements.*

    """

    try:
        # Write to markdown file with UTF-8 encoding
        # Generate timestamp-based filename
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{directory}/AI_Trip_Planner_{timestamp}.md"

        print(filename)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Markdown file saved as: {filename}")
        return filename
        
    except Exception as e:
        print(f"Error saving markdown file: {e}")
        return None