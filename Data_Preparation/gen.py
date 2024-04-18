from classes import *
from random import *
import csv
from collections import defaultdict


if __name__ == '__main__':
    # initialising set of all skills
    set_of_skills = set()
    skill_file = open("skills.txt")
    for skill_line in skill_file:
        skill_line = skill_line[skill_line.index('.')+1:]
        skill_name, skill_domain = skill_line.split(' - ')
        skill_name = skill_name.strip()
        skill_domain = skill_domain.strip()
        # print(f"#{skill_name}#{skill_domain}")
        set_of_skills.add(skill(skill_name, skill_domain))
    print("###########################################################")
    print(set_of_skills)
    skill_list = list(set_of_skills)
    # Specify the file path for the CSV file
    csv_file_path = "skills.csv"

    # Define the field names for the CSV file
    field_names = ["Proficiency", "Domain"]

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        
        # Write the header
        writer.writeheader()
        
        # Write data for each skill
        for SKILL in skill_list:
            writer.writerow({
                "Proficiency": SKILL.skill_name,
                "Domain": SKILL.skill_domain,
            })

    print("CSV file created successfully.")
    print("###########################################################")
    skill_file.close()
    set_of_skills = list(set_of_skills)
    # initialising the set of all names, seperated by gender
    set_of_male_names = set()
    set_of_female_names = set()
    male_name_file = open("male_names.txt")
    for name in male_name_file:
        name = name[name.index('.')+1:]
        name = name.strip()
        set_of_male_names.add(name)
    male_name_file.close()
    female_name_file = open("female_names.txt")
    for name in female_name_file:
        name = name = name[name.index('.')+1:]
        name = name.strip()
        set_of_female_names.add(name)
    female_name_file.close()
    set_of_female_names = list(set_of_female_names)
    set_of_male_names = list(set_of_male_names)
    print(set_of_male_names)
    print("#######################################################################")
    print(set_of_female_names)
    print("#######################################################################")
    list_of_companies = []
    company_file = open("company_names.txt")
    used_company_ids = set()
    for company_details in company_file:
        id = randint(0, 10**5)
        while id in used_company_ids:
            id = randint(0, 10**5)
        company_details = company_details[company_details.index('.')+1:]
        name, sector = company_details.split(' - ')
        name = name.strip()
        sector = sector.strip()
        rating = randint(1, 10)
        website = "www." + ("_").join(name.split()) + ".com"
        used_company_ids.add(id)
        list_of_companies.append(company(id, name, sector, rating, website))
    company_file.close()
    print("#####################################################################")
    print(list_of_companies)
    # Specify the file path for the CSV file
    csv_file_path = "companies.csv"

    # Define the field names for the CSV file
    field_names = ["Com_ID", "Com_Name", "Sector", "Com_Rating", "Official_Website"]

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        
        # Write the header
        writer.writeheader()
        
        # Write data for each company
        for Company in list_of_companies:
            writer.writerow({
                "Com_ID": Company.company_id,
                "Com_Name": Company.company_name,
                "Sector": Company.sector,
                "Com_Rating": Company.rating,
                "Official_Website": Company.website
            })

    print("CSV file created successfully.")
    print("#####################################################################")
    print(len(used_company_ids)-len(list_of_companies))
    used_js_id = set()
    list_of_colleges = []
    college_file = open("colleges.txt")
    for college in college_file:
        college = college[college.index('.')+1:]
        college, _ = college.split(' - ')
        college = college.strip()
        list_of_colleges.append(college)
    print(list_of_colleges)
    deg_spec = {}
    deg_spec['BE'] = ['Comp Sci', 'Electrical', 'Mechanical', 'Civil', 'Manu']
    deg_spec['B.Pharm'] = ['Medicine']
    deg_spec['B.Tech'] = deg_spec['BE']
    deg_spec['M.Tech'] = deg_spec['BE']
    deg_spec['B.A'] = ['English', 'History', 'Psychology', 'Sociology']
    deg_spec['Ph.D'] = deg_spec['BE'] + deg_spec['B.Pharm'] + deg_spec['B.A']
    locations = []
    location_file = open("locations.txt")
    for location in location_file:
        location = location[location.index('.')+1:]
        location = location.strip()
        locations.append(location)
    location_file.close()
    print(locations)
    roles = []
    role_file = open("roles.txt")
    for role in role_file:
        role = role[role.index('.')+1:]
        role = role.strip()
        roles.append(role)
    role_file.close()
    print(roles)
    list_of_jobs = []
    used_job_ids = set()
    for i in range(1000):
        id = randint(0, 10**5)
        while id in used_job_ids:
            id = randint(0, 10**5)
        used_job_ids.add(id)
        role = choice(roles)
        salary = randint(10**3, 10**5)*100
        location = choice(locations)
        type = choice(list(job_type))
        rating = randint(1, 10)
        status = job_status.vacant
        comp =  choice(list_of_companies)
        company_id = comp.company_id
        jb = job(id, role, salary, location, type, rating, status, company_id)
        no_of_skills = randint(1, 5)
        for i in range(no_of_skills):
            jb.skills_required.append(choice(set_of_skills))
        list_of_jobs.append(jb)
        comp.list_of_jobs.append(jb)
    print("################################################################################")
    csv_file_path = "skills_required.csv"
    field_names = ["Job_ID", "Proficiency", "Domain", "Years of experience"]
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for jb in list_of_jobs:
            for ski in jb.skills_required:
                writer.writerow({
                    "Job_ID": jb.job_id,
                    "Proficiency": ski.skill_name,
                    "Domain": ski.skill_domain,
                    "Years of experience": randint(0, 20)
                })
        print("CSV created successfully")
    print("################################################################################")
    print(list_of_jobs)
    # Specify the file path for the CSV file
    csv_file_path = "jobs.csv"

    # Define the field names for the CSV file
    field_names = ["Job_ID", "Role", "Salary", "Location", "Type", "Status", "Company_ID"]

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        
        # Write the header
        writer.writeheader()
        
        # Write data for each job
        for JOB in list_of_jobs:
            writer.writerow({
                "Job_ID": JOB.job_id,
                "Role": JOB.role,
                "Salary": JOB.salary,
                "Location": JOB.location,
                "Type": JOB.type,
                "Status": JOB.status,
                "Company_ID": JOB.company_id
            })

    print("CSV file created successfully.")
    print("################################################################################")
    print(len(used_job_ids)-len(list_of_jobs))
    job_seeker_list = []
    st = [seeker_status.searching]
    set_of_qualifications = set()
    set_of_work_exp = set()
    skills_used_table = []
    skills_learnt_table = []
    for i in range(1000):
        id = randint(0, 10**5)
        while id in used_js_id:
            id = randint(0, 10**5)
        used_js_id.add(id)
        age = randint(18, 65)
        gen = choice(list(gender))
        if gen == gender.male:
            name = choice(set_of_male_names)
        else:
            name = choice(set_of_female_names)
        sts = choice(st)
        js = job_seeker(id, age, name, gen, sts)
        no_of_qualifications = randint(0, 5)
        for qualint in range(0,no_of_qualifications):
            org = choice(list_of_colleges) 
            degree = choice(list((deg_spec.keys())))
            spl = choice(deg_spec[degree])
            year = randint(1980, 2022)
            quali = qualification(org, degree, spl, year)
            set_of_qualifications.add(quali)
            no_of_skills = randint(1, 5)
            for i in range(no_of_skills):
                quali.associated_skills.append(choice(set_of_skills))
            quali.associated_skills = list(set(quali.associated_skills))

            js.qualifications.append(quali)
        no_of_we = randint(0, 5)
        for we in range(0, no_of_we):
            comp_id = choice(list_of_companies).company_id 
            jb = choice(list_of_jobs)
            role = jb.role
            salary = jb.salary
            duration = randint(1, 10)
            wexp = work_exp(comp_id, role, salary, duration)
            set_of_work_exp.add(wexp)
            no_of_skills = randint(1, 5)
            for i in range(no_of_skills):
                wexp.associated_skills.append(choice(set_of_skills))
            wexp.associated_skills = list(set(wexp.associated_skills))
            js.work_exps.append(wexp)
        job_seeker_list.append(js)
    print("#####################################################################")
    csv_file_path = "skills_used.csv"
    field_names = ["JS_ID", "Com_ID", "WE_Role", "Proficiency", "Domain"]
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for js in job_seeker_list:
            for we in js.work_exps:
                for skill in we.associated_skills:
                    writer.writerow({
                        "JS_ID": js.js_id,
                        "Com_ID": we.company_ID,
                        "WE_Role": we.role,
                        "Proficiency": skill.skill_name,
                        "Domain": skill.skill_domain
                    })  
        print("CSV created successfully")
    print("#####################################################################")
    csv_file_path = "skills_learnt.csv"
    field_names = ["JS_ID", "Year", "Proficiency", "Domain"]
    with open(csv_file_path, mode = 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for js in job_seeker_list:
            for qual in js.qualifications:
                for skill in qual.associated_skills:
                    writer.writerow({
                        "JS_ID": js.js_id,
                        "Year": qual.year,
                        "Proficiency": skill.skill_name,
                        "Domain": skill.skill_domain
                    })
    print("#####################################################################")
    list_of_we = list(set_of_work_exp)
    # Specify the file path for the CSV file
    csv_file_path = "workexps.csv"

    # Define the field names for the CSV file
    field_names = ["Com_ID", "WE_Role", "WE_Salary", "Duration"]

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        
        # Write the header
        writer.writeheader()
        
        # Write data for each qualification
        for qual in list_of_we:
            writer.writerow({
                "Com_ID": qual.company_ID,
                "WE_Role": qual.role,
                "WE_Salary": qual.salary,
                "Duration": qual.duration
            })

    print("CSV file created successfully.")
    print("#####################################################################")
    list_of_quals = list(set_of_qualifications)
    # Specify the file path for the CSV file
    csv_file_path = "qualifications.csv"

    # Define the field names for the CSV file
    field_names = ["Organization", "Degree", "Specialisation", "Year"]

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        
        # Write the header
        writer.writeheader()
        
        # Write data for each qualification
        for qual in list_of_quals:
            writer.writerow({
                "Organization": qual.organisation,
                "Degree": qual.degree,
                "Specialisation": qual.specialisation,
                "Year": qual.year
            })

    print("CSV file created successfully.")
    print("#####################################################################")
    print(job_seeker_list)
    # Specify the file path for the CSV file
    csv_file_path = "job_seekers.csv"
    # Define the field names for the CSV file
    field_names = ["JS_ID", "Name", "Age", "Gender", "Status"]

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        
        # Write the header
        writer.writeheader()
        
        # Write data for each job seeker
        for JobSeek in job_seeker_list:
            writer.writerow({
                "JS_ID": JobSeek.js_id,
                "Name": JobSeek.name,
                "Age": JobSeek.age,
                "Gender": JobSeek.gender,
                "Status": JobSeek.status
            })

    print("CSV file created successfully.")
    print("#####################################################################")
    print(len(used_js_id)-len(job_seeker_list))
    print()
    print()
    print()
    print("Here we go!")
    # print(list_of_jobs)
    # print(job_seeker_list)
    for jb in list_of_jobs:
        print(jb.skills_required)
    applied = defaultdict(lambda : [])
    offered = defaultdict(lambda : [])
    for job_s in job_seeker_list:
        skl = set()
        for exp in job_s.work_exps:
            skl.update(exp.associated_skills)
        for l in job_s.qualifications:
            skl.update(l.associated_skills)
        # print(skl)
        for job_ in list_of_jobs:
            if set(job_.skills_required) <= skl:
                continue
            ch = randint(0,3)
            if ch == 3:
                applied[job_s.js_id].append(job_.job_id)
            elif ch == 2:
                offered[job_s.js_id].append(job_.job_id)
    # print(applied)
    # print(offered)
    acceptedjs = []
    acceptedjb = []
    for js in job_seeker_list:
        possible = list(filter(lambda x : x not in acceptedjb, (applied[js.js_id] + offered[js.js_id])))
        if possible:
            taken = choice(possible)
            acceptedjs.append(js.js_id)
            acceptedjb.append(taken)
    # print(acceptedjs)
    # print(acceptedjb)
    
    csv_file_path = "offered.csv"
    field_names = ["JS_ID", "Job_ID"]
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for i in offered:
            for j in offered[i]:
                writer.writerow({
                    "JS_ID": i,
                    "Job_ID": j
                })

    csv_file_path = "applied.csv"
    field_names = ["JS_ID", "Job_ID"]
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for i in applied:
            for j in applied[i]:
                writer.writerow({
                    "JS_ID": i,
                    "Job_ID": j
                })

    csv_file_path = "accepted.csv"
    field_names = ["JS_ID", "Job_ID"]
    with open(csv_file_path, mode = 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for i in range(0, len(acceptedjb)):
            writer.writerow({
                    "JS_ID": acceptedjs[i],
                    "Job_ID": acceptedjb[i]
                })
            
    print("It's finally over")