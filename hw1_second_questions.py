#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#



#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(cvs,job_title):
    dictionary = {}
    for cv in cvs:
        if job_title in cv['jobs']:
            dictionary[cv['user']] = job_title
    return dictionary
        
cv_list=[{'user': 'john', 'jobs': ['analyst', 'engineer']},
  {'user': 'jane', 'jobs': ['finance', 'software']},
  {'user': 'dani', 'jobs': ['finance']}]

has_experience_as(cv_list,'finance')

#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(cvs):
    job_dictionary={}
    for cv in cvs:
        jobs= cv.get('jobs')
        for job in jobs:
            if job in job_dictionary:
                job_dictionary[job] += 1
            else:
                job_dictionary[job] = 1

    return job_dictionary

cv_list=[{'user': 'john', 'jobs': ['analyst', 'engineer']},
  {'user': 'jane', 'jobs': ['finance', 'software']},
  {'user': 'dani', 'jobs': ['finance']}]
job_counts(cv_list)

#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.


def job_counts(cvs):
    job_dictionary={}
    for cv in cvs:
        jobs= cv.get('jobs')
        for job in jobs:
            if job in job_dictionary:
                job_dictionary[job] += 1
            else:
                job_dictionary[job] = 1

    return job_dictionary

def most_popular_job(cvs):
    job_dictionary=job_counts(cvs)
    most_popular = max(job_dictionary.items(),key=lambda x:x[1])
    return most_popular 

cv_list=[{'user': 'john', 'jobs': ['analyst', 'engineer']},
  {'user': 'jane', 'jobs': ['finance', 'software']},
  {'user': 'dani', 'jobs': ['finance']}]
most_popular_job(cv_list)

