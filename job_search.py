import urllib.request
import re

JOB_URL_PATTERN = "https://www.linkedin.com/jobs/view/[a-z-]+\d+"

class FILTER:
    COMPANY = 'C'
    EXPERIENCE = 'E'
    JOB_FUNCTION = 'F'

class EXPERIENCE:
    ENTRY_LEVEL = '2'
    ASSOCIATE = '3'

class JOB_FUNCTION:
    OTHER = "othr"
    LEGAL = "lgl"
    PROJECT_MANAGEMENT = "prjm"

def combine_filters(entries):
    return "%2C".join(entries)

def gen_search_query(requirements):
    # requirements: dict<FILTER, list>
    assert (FILTER.COMPANY in requirements.keys()), "Must include company ids in the requirement!"
    base_str = "https://www.linkedin.com/jobs/search/?"
    conditions = []
    for dim, entries in requirements.items():
        conditions.append("f_{dim}={filters}".format(dim=dim, filters=combine_filters(entries)))
    return base_str + "&".join(conditions)

def gen_job_lists(search_url):
    try: 
        response = urllib.request.urlopen(search_url)
    except Exception as e:
        print("Error: {}. Job search URL is: {}".format(e, search_url))
        return []
    http_raw = str(response.read())
    matches = re.findall(JOB_URL_PATTERN, http_raw)
    return matches
    

if __name__ == "__main__":
    # To Use: Update your job search requirements here
    requirements = {
        FILTER.COMPANY: ['10679415', '22806', '27921', '35552179', '598754', '20681', '6607084'],
        FILTER.EXPERIENCE: [EXPERIENCE.ENTRY_LEVEL],
        FILTER.JOB_FUNCTION: [JOB_FUNCTION.OTHER, JOB_FUNCTION.PROJECT_MANAGEMENT]
    }
    search_query = gen_search_query(requirements)
    jobs = gen_job_lists(search_query)
    print(jobs)
    

