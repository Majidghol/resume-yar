print("=== ResumeYar v0.2 ===")

name = input("نام شما: ")
skills = input("مهارت‌ها (با کاما جدا کن): ")
education = input("تحصیلات: ")
bio = input("توضیح کوتاه درباره خودت: ")

skills_list = skills.split(",")

data = f"""
========================
        RESUME
========================

نام: {name}

مهارت‌ها:
"""

for s in skills_list:
    data += f"- {s.strip()}\n"

data += f"""
تحصیلات: {education}

درباره من:
{bio}

========================
"""

with open("resume.txt", "w", encoding="utf-8") as f:
    f.write(data)

print("\n✔ رزومه حرفه‌ای ذخیره شد (resume.txt)")
