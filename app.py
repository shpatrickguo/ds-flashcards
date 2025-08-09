import streamlit as st
import os
import re
import yaml
from datetime import datetime
from markdown import markdown
from streamlit.components.v1 import html

# Configuration
CARDS_FOLDER = "cards"

# Ensure the cards folder exists
if not os.path.exists(CARDS_FOLDER):
    os.makedirs(CARDS_FOLDER)

# Local file functions
def get_flashcards():
    """Get all markdown flashcards from the local cards folder"""
    try:
        files = [f for f in os.listdir(CARDS_FOLDER) if f.endswith(".md")]
        return [{"name": f} for f in files]
    except Exception as e:
        st.error(f"Error fetching flashcards: {str(e)}")
        return []

def get_flashcard_content(filename):
    """Get the content of a specific flashcard"""
    try:
        file_path = os.path.join(CARDS_FOLDER, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        st.error(f"Error reading flashcard: {str(e)}")
        return None

def save_flashcard(filename, content):
    """Save a flashcard to the local cards folder"""
    try:
        file_path = os.path.join(CARDS_FOLDER, filename)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        st.error(f"Error saving flashcard: {str(e)}")
        return False

def delete_flashcard(filename):
    """Delete a flashcard from the local cards folder"""
    try:
        file_path = os.path.join(CARDS_FOLDER, filename)
        os.remove(file_path)
        return True
    except Exception as e:
        st.error(f"Error deleting flashcard: {str(e)}")
        return False

# Flashcard parsing functions
def parse_flashcard(content):
    """Parse markdown content to extract flashcard components"""
    result = {
        'name': 'Untitled',
        'tags': [],
        'question': 'No question found',
        'answer': 'No answer found',
        'explanation': None
    }
    
    # Extract YAML front matter
    front_matter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if front_matter_match:
        front_matter_text = front_matter_match.group(1)
        main_content = front_matter_match.group(2)
        
        # Parse front matter as YAML
        try:
            front_matter = yaml.safe_load(front_matter_text)
            result['name'] = front_matter.get('name', 'Untitled')
            result['tags'] = front_matter.get('tags', [])
        except:
            # If YAML parsing fails, use defaults
            pass
    else:
        main_content = content

    # Extract question
    question_match = re.search(r'## Q:\s*(.*?)(?=\nA:|\n###|\Z)', main_content, re.DOTALL)
    if question_match:
        result['question'] = question_match.group(1).strip()

    # Extract answer
    answer_match = re.search(r'A:\s*(.*?)(?=\n###|\Z)', main_content, re.DOTALL)
    if answer_match:
        result['answer'] = answer_match.group(1).strip()

    # Extract explanation (if exists)
    explanation_match = re.search(r'### Explanation.*?\n(.*?)(?=\Z)', main_content, re.DOTALL)
    if explanation_match:
        result['explanation'] = explanation_match.group(1).strip()

    return result

# Main app
def main():
    st.set_page_config(
        page_title="Markdown Flashcards",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("📚 Markdown Flashcards")
    st.markdown("Create and study flashcards stored as Markdown files in the 'cards' folder")
    
    # Initialize session state
    if "current_flashcard" not in st.session_state:
        st.session_state.current_flashcard = None
    if "edit_mode" not in st.session_state:
        st.session_state.edit_mode = False
    if "study_mode" not in st.session_state:
        st.session_state.study_mode = False
    if "user_answer" not in st.session_state:
        st.session_state.user_answer = ""
    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False
    
    # Sidebar
    st.sidebar.title("Navigation")
    
    # Get flashcards
    flashcards = get_flashcards()
    
    # Flashcard selection
    selected_flashcard = st.sidebar.selectbox(
        "Select a flashcard:",
        ["Create New"] + [f["name"] for f in flashcards],
        index=0 if st.session_state.current_flashcard is None else 0
    )
    
    # Navigation buttons
    if st.sidebar.button("Home"):
        st.session_state.current_flashcard = None
        st.session_state.edit_mode = False
        st.session_state.study_mode = False
        st.session_state.show_answer = False
        st.experimental_rerun()
    
    if selected_flashcard != "Create New":
        if st.sidebar.button("Edit"):
            st.session_state.edit_mode = True
            st.session_state.study_mode = False
            st.session_state.show_answer = False
            st.experimental_rerun()
        
        if st.sidebar.button("Study"):
            st.session_state.edit_mode = False
            st.session_state.study_mode = True
            st.session_state.user_answer = ""
            st.session_state.show_answer = False
            st.experimental_rerun()
        
        if st.sidebar.button("Delete"):
            if delete_flashcard(selected_flashcard):
                st.success(f"Flashcard {selected_flashcard} deleted successfully!")
                st.session_state.current_flashcard = None
                st.experimental_rerun()
    
    # Main content area
    if selected_flashcard == "Create New":
        st.header("Create New Flashcard")
        
        # Form for creating a new flashcard
        filename = st.text_input("Filename (without .md extension):", key="new_filename")
        name = st.text_input("Card Name:", key="new_name")
        tags = st.text_input("Tags (comma separated):", key="new_tags")
        question = st.text_area("Question:", height=150, key="new_question")
        answer = st.text_area("Answer:", height=150, key="new_answer")
        explanation = st.text_area("Explanation (optional):", height=150, key="new_explanation")
        
        if st.button("Save Flashcard"):
            if filename and name and question and answer:
                # Format tags as a list
                tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
                
                # Create content in the specified format
                content = f"""
                            ---
                            name: {name}
                            tags: {tag_list}
                            ---
                            ## Q: {question}
                            A: {answer}
                            """
                if explanation:
                    content += f"""
                                ### Explanation for Non-Technical Readers
                                {explanation}
                                ---
                                """
                else:
                    content += "\n---\n"
                
                if save_flashcard(f"{filename}.md", content):
                    st.success(f"Flashcard {filename}.md created successfully!")
                    st.session_state.current_flashcard = f"{filename}.md"
                    st.experimental_rerun()
            else:
                st.error("Please fill in all required fields (filename, name, question, and answer)")
    
    else:
        # Load the selected flashcard
        if st.session_state.current_flashcard != selected_flashcard:
            content = get_flashcard_content(selected_flashcard)
            st.session_state.current_flashcard = selected_flashcard
            st.session_state.flashcard_content = content
        
        content = st.session_state.get("flashcard_content", "")
        parsed = parse_flashcard(content)
        
        if st.session_state.edit_mode:
            # Edit mode
            st.header(f"Editing: {selected_flashcard}")
            
            # Edit form - show entire content
            edited_content = st.text_area(
                "Content (Markdown):",
                value=content,
                height=400,
                key="edit_content"
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Save Changes"):
                    if save_flashcard(selected_flashcard, edited_content):
                        st.success("Flashcard updated successfully!")
                        st.session_state.flashcard_content = edited_content
                        st.experimental_rerun()
            
            with col2:
                if st.button("Cancel"):
                    st.session_state.edit_mode = False
                    st.experimental_rerun()
        
        elif st.session_state.study_mode:
            # Study mode
            st.header(f"Studying: {parsed['name']}")
            
            # Display tags
            if parsed['tags']:
                tags_str = ", ".join(parsed['tags']) if isinstance(parsed['tags'], list) else parsed['tags']
                st.markdown(f"**Tags:** {tags_str}")
            
            # Display question
            st.subheader("Question:")
            st.markdown(parsed['question'])
            
            # User answer input
            st.subheader("Your Answer:")
            user_answer = st.text_area(
                "Type your answer here:",
                value=st.session_state.user_answer,
                height=150,
                key="study_answer"
            )
            
            # Show answer button
            if not st.session_state.show_answer:
                if st.button("Show Answer"):
                    st.session_state.user_answer = user_answer
                    st.session_state.show_answer = True
                    st.experimental_rerun()
            else:
                # Display the reference answer
                st.subheader("Reference Answer:")
                st.markdown(parsed['answer'])
                
                # Display explanation if available
                if parsed['explanation']:
                    with st.expander("Explanation"):
                        st.markdown(parsed['explanation'])
                
                # Compare user answer with reference
                st.subheader("Comparison:")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Your Answer:**")
                    st.markdown(user_answer)
                
                with col2:
                    st.markdown("**Reference Answer:**")
                    st.markdown(parsed['answer'])
                
                # Reset button
                if st.button("Try Again"):
                    st.session_state.user_answer = ""
                    st.session_state.show_answer = False
                    st.experimental_rerun()
        
        else:
            # View mode
            st.header(parsed['name'])
            
            # Display tags
            if parsed['tags']:
                tags_str = ", ".join(parsed['tags']) if isinstance(parsed['tags'], list) else parsed['tags']
                st.markdown(f"**Tags:** {tags_str}")
            
            # Display flashcard content
            st.subheader("Question:")
            st.markdown(parsed['question'])
            
            st.subheader("Answer:")
            st.markdown(parsed['answer'])
            
            # Display explanation if available
            if parsed['explanation']:
                with st.expander("Explanation"):
                    st.markdown(parsed['explanation'])
            
            # Edit and Study buttons
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Edit"):
                    st.session_state.edit_mode = True
                    st.experimental_rerun()
            
            with col2:
                if st.button("Study"):
                    st.session_state.study_mode = True
                    st.session_state.user_answer = ""
                    st.session_state.show_answer = False
                    st.experimental_rerun()

if __name__ == "__main__":

    main()
