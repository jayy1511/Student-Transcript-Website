import os
import re

# Base directory for templates
templates_dir = r"c:\JAY\EPITA\My Projects\Web Dev\Transcript_Website\Student-Transcript-Website-main\templates"

# Patterns to replace
replacements = [
    (
        r'style="display: flex; justify-content: space-between; width: 100%; align-items: center;"',
        'class="navbar-flex"'
    ),
    (
        r'style="padding: 16px;"',
        'class="breadcrumb-card"'
    ),
]

def update_file(filepath):
    """Update a single HTML file with the replacements"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath}")
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Process all HTML files in templates directory"""
    updated_count = 0
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if update_file(filepath):
                    updated_count += 1
    
    print(f"\nTotal files updated: {updated_count}")

if __name__ == "__main__":
    main()
