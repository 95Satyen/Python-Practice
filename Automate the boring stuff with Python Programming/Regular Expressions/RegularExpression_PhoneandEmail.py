# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 03:15:25 2020

@author: satye
"""

document = """By continuing to use this site, you agree to the use of cookies in accordance with our privacy policy.

Dismiss
Skip to Content
Syracuse University Home
About	Admissions	Academics	Life	Athletics	More	
Search the University...
Popular searches
myslice human resources academic calendar directory tuition registrar
Search people (directory)Go to local nav
Home  About  Help & Contacts
In this Section
Emergencies
Status
Help and Contacts
Campus Address and Phone
Syracuse University
900 South Crouse Ave
Syracuse, NY 13244
315.443.1870

Campus status Emergencies A-Z index

Safety
Department of Public Safety (DPS) - Emergency
315.443.2224
(or #78 from cell phone)
711@syr.edu
Department of Public Safety (DPS)
315.443.2224
dpsadmin@syr.edu
Admissions and Financial Aid
​Undergraduate Admissions
315.443.3611
orange@syr.edu
​Graduate Admissions
315.443.4492
grad@syr.edu
​Law Admissions
315.443.1962
admissions@law.syr.edu
University College (Part-Time Study)
315.443.9378
parttime@uc.syr.edu
Veterans Admissions
315.443.6124
rwb@syr.edu
Study Abroad
1.800.235.3472
suabroad@syr.edu
​Financial Aid and Scholarship Programs
315.443.1513
Contact Form
Computing
​Information Technology Services (ITS)
315.443.2677
help@syr.edu
Communications and Alumni
​Syracuse University News
315.443.3784
​sunews@syr.edu
Correspondence for Syracuse University Magazine
315.443.2872
syracusemagazine@syr.edu
Alumni/Magazine Change of Address
315.443.2432
records@syr.edu
Notices of Death
315.443.2432
records@syr.edu
​Office of Alumni Engagement
315.443.3258
sualumni@syr.edu
Employment and Human Resources
​Human Resources
315.443.4042
hrservic@syr.edu
Ombuds
Providing faculty, staff, and graduate students with an informal, confidential, impartial, and independent resource to address University-related conflicts, concerns, and/or questions without fear of retaliation or judgment.

Office of the University Ombuds
315.443.1087
ombuds@syr.edu
Additional Resources
A-Z Index
Academic Department Directory
Campus Map
People Directory
Search
Website Feedback​
Related Pages
Request More Information
​Tell us a little about yourself and we'll provide you with more information about attending Syracuse University.

Syracuse University News
Stay up-to-date with news and events on campus, as well as in the surrounding City of Syracuse.

Social Media Directory
Connect with the Syracuse University community across campus and around the world! Catch the latest posts, photos, and news.

Send Website Feedback
Send us your comments and questions about Syracuse.edu. We value your feedback and are always working to improve your experience on our site.

Popular
Academic Calendar
Campus Map
Careers
Libraries
Majors and Minors
Visit and Tour
A-Z
Find People (Directory)
Academic Departments
Schools and Colleges
Sitemap
Search
Contact
Admissions
Financial Aid
Emergency Contacts
Human Resources
Website Feedback
Make a Gift
Login
MySlice
Blackboard
Student Email
Faculty & Staff Email
Syracuse University Seal
Syracuse University
900 South Crouse Ave.
Syracuse, NY 13244

Phone: +1.315.443.1870
   
© Syracuse University. Knowledge crowns those who seek her.Accessibility Accreditation Emergencies Privacy """


# Create regex for phone numbers
import re
#regPhoneNumber = re.compile(r'''
#(\+\d.)*   #country code
#(\d\d\d)   #area code
#(.|/s)*    #separator
#(\d\d\d)   #first 3 digits
#(.|/s)*    #separator
#(\d\d\d\d) #last 4 digits
#''', re.VERBOSE)
#print(regPhoneNumber.findall(document)) #findall creates a list of tuples for groups
#solution is to put everything in one large group

regPhoneNumber = re.compile(r'''
(
(\+\d.)*   #country code
(\d\d\d)   #area code
(.|/s)*    #separator
(\d\d\d)   #first 3 digits
(.|/s)*    #separator
(\d\d\d\d) #last 4 digits
)
''', re.VERBOSE)
print(regPhoneNumber.findall(document)) #0th element is the complete number in each tuple

# Create regex for email address
regEmailId = re.compile(r'''
[a-zA-Z0-9_.+]+    #name part
\@{1}              #@ symbol
[a-zA-Z0-9_.+]+    #domain name part
''', re.VERBOSE)
print(regEmailId.findall(document))


# Extract phone numbers from text
extractedPhoneNumbers = regPhoneNumber.findall(document)
allPhoneNumbers = []
for phoneNumber in extractedPhoneNumbers:
    allPhoneNumbers.append(phoneNumber[0])
print(allPhoneNumbers)

# Extract email ids from text
extractedEmailIds = regEmailId.findall(document)
allEmailIds = []
for email in extractedEmailIds:
    allEmailIds.append(email)
print(allEmailIds)

# Merging all phone numbers
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allEmailIds)
print('Results:',results, sep='\n')