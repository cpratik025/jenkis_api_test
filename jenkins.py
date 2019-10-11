import jenkins

server = jenkins.Jenkins('http://localhost:8080')
print server.jobs_count()
