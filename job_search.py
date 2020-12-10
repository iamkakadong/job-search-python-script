import urllib.request
import re

JOB_URL_PATTERN = "https://www.linkedin.com/jobs/view/[a-z-]+\d+"

class COMPANY:
    Czi = '10679415'
    Omidyar = '22806'
    Svcf = '29309'
    Candid = '35552179'
    Css_fundraising = '9832'
    Emerson_collctive = '6607084'
    C100 = '8001249'
    Arabella = '2100869'
    Common_sense_media = '28256'
    Sff = '27921'
    Tides = '598754'
    Grameen = '20681'

class FILTER:
    COMPANY = 'C'
    EXPERIENCE = 'E'
    JOB_FUNCTION = 'F'
    JOB_TYPE = "JT"

class EXPERIENCE:
    ENTRY_LEVEL = '2'
    ASSOCIATE = '3'

class JOB_FUNCTION:
    OTHER = "othr"
    LEGAL = "lgl"
    PROJECT_MANAGEMENT = "prjm"

class JOB_TYPE:
    FULL_TIME = "F"
    PART_TIME = "CP"
    CONTRACT = "CC"

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
    requirements = {
        FILTER.COMPANY: [
            COMPANY.Czi,
            COMPANY.Omidyar,
            COMPANY.Svcf,
            COMPANY.Candid,
            COMPANY.Css_fundraising,
            COMPANY.Emerson_collctive,
            COMPANY.C100,
            COMPANY.Arabella,
            COMPANY.Common_sense_media,
            COMPANY.Sff,
            COMPANY.Tides,
            COMPANY.Grameen,
        ],
        FILTER.EXPERIENCE: [EXPERIENCE.ENTRY_LEVEL],
        FILTER.JOB_TYPE: [JOB_TYPE.FULL_TIME],
        # FILTER.JOB_FUNCTION: [JOB_FUNCTION.OTHER, JOB_FUNCTION.PROJECT_MANAGEMENT]
    }
    search_query = gen_search_query(requirements)
    jobs = gen_job_lists(search_query)
    for job in jobs:
        print(job)
    
