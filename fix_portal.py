import re
import os
from pathlib import Path

# Base directory
base_dir = r"c:\JAY\EPITA\My Projects\Web Dev\Transcript_Website\Student-Transcript-Website-main"

# Fix CSS - add dark mode and improve theme toggle
css_file = os.path.join(base_dir, "static", "common.css")
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add dark mode after line 41 (after :root closing)
dark_mode_css = """
/* DARK MODE - PURE BLACK/GRAY */
[data-theme="dark"] {
  --primary: #ffffff;
  --primary-hover: #e5e5e5;
  --secondary: #a3a3a3;
  --accent: #737373;
  
  --bg-body: #000000;
  --bg-card: #1a1a1a;
  --bg-header: #1a1a1a;
  
  --text-main: #f5f5f5;
  --text-muted: #a6a6a6;
  --text-light: #808080;
  
  --border-color: #333333;
  
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.9);
  --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.95);
  --shadow-lg: 0 8px 16px rgba(0, 0, 0, 1);
  --shadow-glow: 0 0 15px rgba(255, 255, 255, 0.1);
}

"""

# Insert dark mode after :root
css_content = css_content.replace('}\n\n/* Reset & Base Styles */', '}\n' + dark_mode_css + '/* Reset & Base Styles */')

# Add better theme toggle button styling and centered sections
better_styles = """
/* Theme Toggle - Improved */
.theme-toggle {
  background: transparent;
  border: none;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  color: var(--text-main);
  font-size: 20px;
  border-radius: 8px;
}

.theme-toggle:hover {
  background: var(--bg-card);
  transform: scale(1.05);
}

.navbar-flex {
  display: flex;
  justify-content: space-between;
  width: 100%;
  align-items: center;
}

/* Centered Content */
.section {
  margin: 40px auto;
  max-width: 1000px;
}

.breadcrumb-card {
  padding: 16px;
}

"""

# Add these styles after .navbar-heading
css_content = css_content.replace(
    '.navbar-heading {\n  font-size: 1.25rem;\n  font-weight: 700;\n  color: var(--text-main);\n  letter-spacing: -0.025em;\n}\n',
    '.navbar-heading {\n  font-size: 1.25rem;\n  font-weight: 700;\n  color: var(--text-main);\n  letter-spacing: -0.025em;\n}\n\n' + better_styles
)

# Write updated CSS
with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS file updated!")

# Fix all grade HTML files
grades_dirs = [
    "templates/grades/ais_grades",
    "templates/grades/cs_grades",
    "templates/grades/dsa_grades",
    "templates/grades/ism_grades",
    "templates/grades/se_grades"
]

for grades_dir in grades_dirs:
    full_dir = os.path.join(base_dir, grades_dir)
    if not os.path.exists(full_dir):
        continue
    
    for html_file in Path(full_dir).glob("*.html"):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add data-theme attribute
        content = content.replace('<html lang="en">', '<html lang="en" data-theme="light">')
        
        # Add theme toggle button in navbar
        navbar_old = r'(<h1 class="navbar-heading">Student Portal</h1>)\s*</div>\s*</nav>'
        navbar_new = r'\1\n            <button class="theme-toggle" aria-label="Toggle theme" title="Toggle theme">\n                <!-- Icon injected by JavaScript -->\n            </button>\n        </div>\n    </nav>'
        content = re.sub(navbar_old, navbar_new, content)
        
        # Add theme-toggle.js script
        if 'theme-toggle.js' not in content:
            content = content.replace(
                '<script src="{{ url_for(\'static\', filename=\'last_generation.js\') }}"></script>',
                '<script src="{{ url_for(\'static\', filename=\'theme-toggle.js\') }}"></script>\n    <script src="{{ url_for(\'static\', filename=\'last_generation.js\') }}"></script>'
            )
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated: {html_file}")

print("\nAll files updated successfully!")
