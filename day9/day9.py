
def add_skill(skills: list[str], skill: str) -> list[str]:
    skills.append(skill)
    return skills

def add_many_skills(skills: list[str], new_skills: list[str]) -> list[str]:
    skills.extend(new_skills)
    return skills

def remove_skill(skills: list[str], skill: str) -> list[str]:
    skills.remove(skill)
    return skills

def get_sorted_skills(skills: list[str]) -> list[str]:
    skills.sort()
    return skills

def get_long_skills(skills: list[str], min_length: int) -> list[str]:
    long_skills = []
    for skill in skills:
        if len(skill) >= min_length:
            long_skills.append(skill)
    return long_skills

def get_long_skills_test(skills: list[str], min_length: int) -> list[str]:
    return [skill for skill in skills if len(skill) >= min_length]

def normalize_skills(skills: list[str]) -> list[str]:
    return [skill.strip().title() for skill in skills]

skills = [" python ", "git", "FastAPI"]

print("Original:", skills)

print("add_skill:", add_skill(skills.copy(), "Docker"))

print("add_many_skills:", add_many_skills(skills.copy(), ["Redis", "PostgreSQL"]))

print("remove_skill:", remove_skill(["Python", "Git", "Docker"], "Git"))

print("get_sorted_skills:", get_sorted_skills(["Docker", "Python", "Git"]))

print("get_long_skills:", get_long_skills(["Git", "Python", "FastAPI", "SQL"], 5))

print("get_long_skills:", get_long_skills_test(["Git", "Python", "FastAPI", "SQL"], 5))

print("normalize_skills:", normalize_skills([" python ", "git", " fastapi "]))
