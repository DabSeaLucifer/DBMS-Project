from vars import *

class skill:
    def __init__(self, skill_name, skill_domain) -> None:
        self.skill_name = skill_name
        self.skill_domain = skill_domain 
    
    def __repr__(self) -> str:
        return f"{self.skill_name}_{self.skill_domain}"

class job_seeker:
    def __init__(self, id, age, name, gender, status) -> None:
        self.js_id = id
        self.age = age
        self.name = name
        self.gender = gender
        self.status = status
        self.work_exps = []
        self.qualifications = []

    def __repr__(self) -> str:
        return f"{self.js_id}"
    
class work_exp:
    def __init__(self, com_id, role, salary, duration) -> None:
        self.company_ID = com_id
        self.role = role
        self.salary = salary
        self.duration = duration
        self.associated_skills = []

class qualification:
    def __init__(self, org, deg, specialisation, year) -> None:
        self.organisation = org
        self.degree = deg
        self.specialisation = specialisation
        self.year = year
        self.associated_skills = []        

class company:
    def __init__(self, id, name, sector, rating, website) -> None:
        self.company_id = id
        self.company_name = name 
        self.sector = sector
        self.rating = rating
        self.website = website
        self.list_of_jobs = [] #list of job id's the company provides
    
    def __repr__(self) -> str:
        return f"{self.company_id}#{self.company_name}#{self.sector}#{self.website}"

class job:
    def __init__(self, id, role, salary, location, type, rating, status, company_id) -> None:
        self.job_id = id
        self.role = role
        self.salary = salary
        self.location = location
        self.type = type
        self.job_rating = rating
        self.status = status
        self.company_id = company_id
        self.skills_required = []
    
    def __repr__(self) -> str:
        return f"{self.job_id}"