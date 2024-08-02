import re
import json

def parse_resume(resume_text):
    sections = ["Name", "Contact", "Summary", "Experience", "Education", "Skills", "Certifications", "Projects", "Languages"]
    resume_json = {}
    
    for section in sections:
        pattern = re.compile(rf"{section}.*?:\n(.*?)(?=\n\n|\n{2,}|$)", re.DOTALL | re.IGNORECASE)
        match = pattern.search(resume_text)
        if match:
            resume_json[section.lower()] = match.group(1).strip()
    
    return json.dumps(resume_json, indent=4)

resume_text = """
Name: John Doe
Contact: johndoe@example.com | (123) 456-7890 | linkedin.com/in/johndoe

Summary:
Experienced software engineer with a strong background in developing scalable web applications and working with cross-functional teams to deliver high-quality software products.

Experience:
Software Engineer at TechCorp (Jan 2020 - Present)
- Developed and maintained web applications using Python, Django, and React.
- Collaborated with designers and product managers to deliver features on time.
- Implemented RESTful APIs and integrated third-party services.

Education:
B.S. in Computer Science from University XYZ (2015 - 2019)

Skills:
- Programming: Python, JavaScript, C++
- Frameworks: Django, React, Node.js
- Tools: Git, Docker, AWS

Certifications:
- AWS Certified Solutions Architect
- Certified Kubernetes Administrator (CKA)

Projects:
- Chatbot: Developed a chatbot using Python and Flask that handles customer queries.
- E-commerce Website: Built an e-commerce platform with Django and React.

Languages:
- English (Fluent)
- Spanish (Intermediate)
"""

parsed_resume = parse_resume(resume_text)
print(parsed_resume)
