from datetime import datetime

print("ResumeYar Pro PDF Builder")

name = input("نام: ")
last name = input("خانوادگی:")
skills = input("مهارت‌ها (با , جدا کن): ")
education = input("تحصیلات: ")
bio = input("درباره: ")

skills_list = skills.split(",")

text = f"""
========================
        RESUME
========================

Name: {name}

Skills:
"""

for s in skills_list:
    text += f" - {s.strip()}\n"

text += f"""
Education:
{education}

About:
{bio}

Created: {datetime.now()}
"""

# ساخت PDF ساده ولی تمیزتر
pdf = f"""%PDF-1.4
1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj
2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj
3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 600 800]
/Contents 4 0 R >> endobj
4 0 obj << /Length {len(text)} >> stream
{text}
endstream endobj
xref
0 5
0000000000 65535 f
trailer << /Root 1 0 R /Size 5 >>
startxref
0
%%EOF
"""

with open("resume_pro.pdf", "w") as f:
    f.write(pdf)

print("\n✔ Resume Pro ساخته شد: resume_pro.pdf")
