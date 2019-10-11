def auth_headers(username, password):
   """
   Returns username and password using base64 encoding
   username - username to be encoded
   password - password to be encoded
   return - the encoded string
   """
   return 'Basic ' + base64.encodestring('%s:%s' % (username, password))[:-1]



def is_jenkins_job_running(job_name):
    """
    Check if job_name passed is running or not.
    It retrieve the job info xml via urllib and parsing it to get it.
    job_name - the jenkins' job name (used to create the url)
    return - true if the job is running, false otherwise
    """
    res = False
    headers = {'Authorization': auth_headers(JENKINS_USER,JENKINS_PWD)}  
    url_to_open = '%s/job/%s/lastBuild/api/xml?depth=1&xpath=*//building' % (BASE_JENKINS_URI, job_name)
    
    request = urllib2.Request(url_to_open,None, headers)
    response = None
    try:
        response = urllib2.urlopen(request)
    except urllib2.URLError as uerr:
        print(uerr.msg)
        sys.exit(2)
    content = response.read()
    if 'true' in content:
        res = True
    return res
