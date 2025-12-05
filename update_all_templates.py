import os
import re

base_dir = r"c:\JAY\EPITA\My Projects\Web Dev\Transcript_Website\Student-Transcript-Website-main"

# Template for Population Pages
def get_population_template(title, pop_code):
    return f"""{{% extends "base.html" %}}

{{% block title %}}{title} - Population{{% endblock %}}

{{% block content %}}
<div class="space-y-6">
    
    <!-- Breadcrumb & Header -->
    <div class="flex flex-col gap-2">
        <nav class="flex text-sm text-gray-500">
            <a href="/" class="hover:text-white transition-colors">Home</a>
            <span class="mx-2">/</span>
            <span class="text-white">Population - {title}</span>
        </nav>
        <h1 class="text-2xl font-bold text-white">MSc {title}</h1>
    </div>

    <!-- Students Table Card -->
    <div class="bg-dark-card border border-dark-border rounded-xl overflow-hidden">
        <div class="px-6 py-4 border-b border-dark-border">
            <h3 class="text-lg font-bold text-white">Students List</h3>
        </div>
        <div class="overflow-x-auto">
            <table class="w-full text-left text-sm text-gray-400">
                <thead class="bg-black/20 text-xs uppercase font-semibold text-gray-500">
                    <tr>
                        <th class="px-6 py-3">Email</th>
                        <th class="px-6 py-3">First Name</th>
                        <th class="px-6 py-3">Last Name</th>
                        <th class="px-6 py-3">Progress</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-dark-border">
                    {{% for student in students %}}
                    <tr class="hover:bg-dark-hover transition-colors group">
                        <td class="px-6 py-4 font-medium text-white group-hover:text-brand-500 transition-colors">
                            {{{{ student[0] }}}}
                        </td>
                        <td class="px-6 py-4">{{{{ student[1] }}}}</td>
                        <td class="px-6 py-4">{{{{ student[2] }}}}</td>
                        <td class="px-6 py-4">
                            <span class="px-2 py-1 rounded-full text-xs font-medium bg-blue-500/10 text-blue-500 border border-blue-500/20">
                                {{{{ student[3] }}}} Passed
                            </span>
                        </td>
                    </tr> 
                    {{% endfor %}}
                </tbody>
            </table>
        </div>
    </div>

    <!-- Courses Table Card -->
    <div class="bg-dark-card border border-dark-border rounded-xl overflow-hidden">
        <div class="px-6 py-4 border-b border-dark-border">
            <h3 class="text-lg font-bold text-white">Curriculum</h3>
        </div>
        <div class="overflow-x-auto">
            <table class="w-full text-left text-sm text-gray-400">
                <thead class="bg-black/20 text-xs uppercase font-semibold text-gray-500">
                    <tr>
                        <th class="px-6 py-3">Course Code</th>
                        <th class="px-6 py-3">Course Name</th>
                        <th class="px-6 py-3">Sessions</th>
                        <th class="px-6 py-3">Action</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-dark-border">
                    {{% for course in courses %}}
                    <tr class="hover:bg-dark-hover transition-colors">
                        <td class="px-6 py-4 font-mono text-xs text-gray-500">{{{{ course[0] }}}}</td>
                        <td class="px-6 py-4 font-medium text-white">{{{{ course[1] }}}}</td>
                        <td class="px-6 py-4">{{{{ course[2] }}}}</td>
                        <td class="px-6 py-4">
                            <a href="/{pop_code}_grades/{{{{ course[0]|lower }}}}" class="text-brand-500 hover:text-brand-400 font-medium text-xs uppercase tracking-wide">
                                View Grades &rarr;
                            </a>
                        </td>
                    </tr>
                    {{% endfor %}}
                </tbody>
            </table>
        </div>
    </div>

</div>
{{% endblock %}}
"""

# Template for Grade Pages
def get_grade_template(pop_code, pop_name):
    return f"""{{% extends "base.html" %}}

{{% block title %}}Grades - {pop_name}{{% endblock %}}

{{% block content %}}
<div class="space-y-6">
    
    <!-- Breadcrumb & Header -->
    <div class="flex flex-col gap-2">
        <nav class="flex text-sm text-gray-500">
            <a href="/" class="hover:text-white transition-colors">Home</a>
            <span class="mx-2">/</span>
            <a href="/populations/{pop_code}" class="hover:text-white transition-colors">MSc {pop_name}</a>
            <span class="mx-2">/</span>
            <span class="text-white">Grades</span>
        </nav>
        <h1 class="text-2xl font-bold text-white">Course Grades</h1>
        <div class="flex items-center gap-2 text-sm text-gray-400">
            <span class="px-2 py-0.5 rounded bg-gray-800 border border-gray-700 font-mono text-xs">FALL 2021</span>
        </div>
    </div>

    <!-- Grades Table Card -->
    <div class="bg-dark-card border border-dark-border rounded-xl overflow-hidden shadow-lg">
        <div class="overflow-x-auto">
            <table class="w-full text-left text-sm text-gray-400">
                <thead class="bg-black/20 text-xs uppercase font-semibold text-gray-500">
                    <tr>
                        <th class="px-6 py-3">Student</th>
                        <th class="px-6 py-3">Email</th>
                        <th class="px-6 py-3">Exam Type</th>
                        <th class="px-6 py-3 text-right">Grade (20)</th>
                        <th class="px-6 py-3 text-right">Status</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-dark-border">
                    {{% for grade in grades %}}
                    <tr class="hover:bg-dark-hover transition-colors">
                        <td class="px-6 py-4 font-medium text-white">
                            {{{{ grade[1] }}}} {{{{ grade[2] }}}}
                        </td>
                        <td class="px-6 py-4 text-gray-500">{{{{ grade[0] }}}}</td>
                        <td class="px-6 py-4">
                            <span class="px-2 py-1 rounded text-xs bg-gray-800 text-gray-300 border border-gray-700">
                                {{{{ grade[3] }}}}
                            </span>
                        </td>
                        <td class="px-6 py-4 text-right font-mono font-bold text-white">
                            {{{{ grade[4] }}}}
                        </td>
                        <td class="px-6 py-4 text-right">
                            {{% if grade[4] >= 10 %}}
                            <span class="px-2 py-1 rounded-full text-xs font-medium bg-green-500/10 text-green-500 border border-green-500/20">Passed</span>
                            {{% else %}}
                            <span class="px-2 py-1 rounded-full text-xs font-medium bg-red-500/10 text-red-500 border border-red-500/20">Failed</span>
                            {{% endif %}}
                        </td>
                    </tr>
                    {{% endfor %}}
                </tbody>
            </table>
        </div>
    </div>

</div>
{{% endblock %}}
"""

# Update Populations
populations = {
    'msc-cs.html': ('MSc CS F2021', 'cs'),
    'msc-dsa.html': ('MSc DSA F2021', 'dsa'),
    'msc-ism.html': ('MSc ISM F2021', 'ism'),
    'msc-se.html': ('MSc SE F2021', 'se')
}

for filename, (title, code) in populations.items():
    path = os.path.join(base_dir, 'templates', 'populations', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(get_population_template(title, code))
    print(f"Updated {filename}")

# Update Grades
grade_folders = {
    'cs_grades': ('cs', 'CS'),
    'dsa_grades': ('dsa', 'DSA'),
    'ism_grades': ('ism', 'ISM'),
    'se_grades': ('se', 'SE')
}

for folder, (code, name) in grade_folders.items():
    folder_path = os.path.join(base_dir, 'templates', 'grades', folder)
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith('.html'):
                with open(os.path.join(folder_path, file), 'w', encoding='utf-8') as f:
                    f.write(get_grade_template(code, name))
                print(f"Updated grades/{folder}/{file}")

print("All templates updated to Modern Design!")
