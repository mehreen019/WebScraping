from bs4 import BeautifulSoup
import requests
import time

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="

response = requests.get(url)

#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

"""
print('--------------------------------printing first job details--------------------------------')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
first_skill = job.find('div', class_ = 'more-skills-sections').span #only returns the first span
skills = job.find('div', class_ = 'more-skills-sections') #returns all the spans
posted_date = job.find('span', class_ = 'sim-posted').span.text
print(company_name)
for skill in skills:
    print(skill.text.strip())
print(posted_date)

"""


def job_filtering():
    print('--------------------------------printing job details by skill filtration--------------------------------')
    print('Input skill you don\'t know')
    skill_input = input()
    skill_input = skill_input.split(',')
    skill_input = [skill.strip().lower() for skill in skill_input]
    print(f'Filtering jobs by {skill_input}:')


    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    valid_dates = ['0 days ago', '1 days ago', '2 days ago', '3 days ago', 'few days ago']
    for index,job in enumerate(jobs):
        posted_date = job.find('span', class_ = 'sim-posted').span.text
        skills = job.find('div', class_ = 'more-skills-sections') #returns all the spans

        if ( any(date in posted_date for date in valid_dates) ):
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            skills_list = []
            for skill in skills:
                skills_list.append(skill.text.strip().lower())
            
            #skills_list.remove('')      #removes the first empty string
            if( not any( any(input_skill in req_skill for req_skill in skills_list) for input_skill in skill_input)):   #checks for partial match

                with open(f'posts/{index}.txt', 'w') as file:      #writing to a file   
                    file.write(f'Company Name: {company_name}\n')
                    file.write(f'Skills: {skills_list}\n')
                    file.write(f'Posted Date: {posted_date}\n')
                #print(company_name)
                #for skill in skills_list:
                #    if skill != '':
                #        print(skill, end = ', ')    #ends a line with a comma
                print(f'Job {index} saved to posts folder')


if __name__ == '__main__':
    while True:
        job_filtering()
        print('Do you want to continue? (y/n)')
        user_input = input()
        if user_input == 'n':
            break
        
        print('Enter the number of seconds to wait before the next job search')
        time_input = input()
        print('Waiting for', time_input, 'seconds')
        time.sleep(int(time_input))

