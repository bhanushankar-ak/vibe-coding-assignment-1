import uuid
from datetime import datetime


# ---------------- Resume Summary Generator ----------------
def generate_summary(role, experience, skills, goal):
    skills_list = [s.strip() for s in skills.split(",") if s.strip()]
    skills_text = ", ".join(skills_list[:6])

    if experience == 0:
        summary = f"Entry-level {role}"
    else:
        summary = f"{role} with {experience}+ years of experience"

    if skills_text:
        summary += f", skilled in {skills_text}"

    summary += "."

    if goal:
        summary += f" Focused on {goal.lower()}."

    return summary


# ---------------- Resume File Generator ----------------
def create_resume_file(data):
    filename = f"resume_{uuid.uuid4().hex}.txt"

    lines = []
    lines.append(data["name"].upper())
    lines.append("=" * len(data["name"]))
    lines.append("")
    lines.append(f"Email: {data['email']}")
    lines.append(f"Phone: {data['phone']}")
    lines.append(f"Location: {data['location']}")

    if data["linkedin"]:
        lines.append(f"Profile: {data['linkedin']}")

    lines.append("\nPROFESSIONAL SUMMARY")
    lines.append("-" * 22)
    lines.append(data["summary"])

    lines.append("\nTECHNICAL SKILLS")
    lines.append("-" * 16)
    for skill in data["skills"].split(","):
        if skill.strip():
            lines.append(f"- {skill.strip()}")

    if data["soft_skills"]:
        lines.append("\nSOFT SKILLS")
        lines.append("-" * 11)
        for skill in data["soft_skills"].split(","):
            if skill.strip():
                lines.append(f"- {skill.strip()}")

    lines.append("\nEDUCATION")
    lines.append("-" * 9)
    lines.append(data["education"])

    if data["achievements"]:
        lines.append("\nACHIEVEMENTS")
        lines.append("-" * 12)
        for item in data["achievements"].split(","):
            if item.strip():
                lines.append(f"- {item.strip()}")

    lines.append("\n---")
    lines.append(f"Generated on {datetime.now().strftime('%Y-%m-%d')}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return filename


# ---------------- Main Program ----------------
def main():
    print("\n=== Resume Generator (Pure Python) ===\n")

    name = input("Full Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone Number: ").strip()
    location = input("Location: ").strip()
    linkedin = input("LinkedIn / GitHub (optional): ").strip()

    role = input("Current Role / Background: ").strip()
    experience = int(input("Years of Experience (0-30): ").strip())

    skills = input("Technical Skills (comma-separated): ").strip()
    soft_skills = input("Soft Skills (comma-separated): ").strip()
    education = input("Education: ").strip()
    achievements = input("Achievements (optional): ").strip()
    goal = input("Career Goal: ").strip()

    if not name or not email or not role or not skills or not education:
        print("\n❌ Error: Missing required fields.")
        return

    if "@" not in email:
        print("\n❌ Error: Invalid email address.")
        return

    summary = generate_summary(role, experience, skills, goal)

    resume_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "location": location,
        "linkedin": linkedin,
        "summary": summary,
        "skills": skills,
        "soft_skills": soft_skills,
        "education": education,
        "achievements": achievements
    }

    file_path = create_resume_file(resume_data)

    print("\n✅ Resume generated successfully!")
    print(f"📄 File saved as: {file_path}")


if __name__ == "__main__":
    main()