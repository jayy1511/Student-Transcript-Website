import os
import re

base_dir = r"c:\JAY\EPITA\My Projects\Web Dev\Transcript_Website\Student-Transcript-Website-main"

# 1. Add ONLY dark mode to CSS - minimal changes
css_file = os.path.join(base_dir, "static", "common.css")
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Add dark mode after :root
dark_mode = """
/* Dark Mode */
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

if '[data-theme="dark"]' not in css:
    css = css.replace('}\r\n\r\n/* Reset & Base Styles */', '}\r\n' + dark_mode + '/* Reset & Base Styles */')

# Center content
css = css.replace(
    '.section {\r\n  margin: 40px 0;\r\n}',
    '.section {\r\n  margin: 40px auto;\r\n  max-width: 1000px;\r\n}'
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("✓ CSS updated with dark mode and centered content")

# 2. Fix ALL HTML files to add theme toggle
html_files = []

# Get all templates
for root, dirs, files in os.walk(os.path.join(base_dir, "templates")):
    for file in files:
        if file.endswith('.html') and file != 'base.html':
            html_files.append(os.path.join(root, file))

for html_path in html_files:
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Add data-theme
    html = html.replace('<html lang="en">', '<html lang="en" data-theme="light">')
    
    # Add theme button if navbar exists and button doesn't
    if '<nav class="navbar">' in html and 'theme-toggle' not in html:
        html = re.sub(
            r'(<h1 class="navbar-heading">Student Portal</h1>)\s*</div>\s*</nav>',
            r'\1\n            <button class="theme-toggle" aria-label="Toggle theme">☀️</button>\n        </div>\n    </nav>',
            html
        )
    
    # Add theme script if not present
    if 'theme-toggle.js' not in html and 'last_generation.js' in html:
        html = html.replace(
            '<script src="{{ url_for(\'static\', filename=\'last_generation.js\') }}"></script>',
            '<script src="{{ url_for(\'static\', filename=\'theme-toggle.js\') }}"></script>\n    <script src="{{ url_for(\'static\', filename=\'last_generation.js\') }}"></script>'
        )
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"✓ Updated {len(html_files)} HTML files")
print("\n✅ All done! Refresh your browser.")
