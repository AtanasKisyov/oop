class Programmer:

    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if not self.language == language:
            return f"{self.name} does not know {language}"
        self.skills += skills_earned
        return f"{self.name} watched {course_name}"

    def change_language(self, new_language, skills_needed):
        if self.language == new_language:
            return f"{self.name} already knows {new_language}"
        if self.skills < skills_needed:
            return f"{self.name} needs {skills_needed - self.skills} more skills"
        previous_language = self.language
        self.language = new_language
        return f"{self.name} switched from {previous_language} to {new_language}"