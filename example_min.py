EXPERIENCE = '''
Education: incomplete law, currently studying at the Faculty of Mathematics

OT Commerce:
Full Stack developer (2018 - 2021):
Engaged in the development of CMS system for an online store
Conducted almost complete refactoring and optimization of the side and the entire CMS

OT Commerce:
Machine learning developer (2020 - 2021):
Developed a neural network for photo search
Implemented a vector data encoder, reducing the amount of stored data for photo search by 4 times

AlanAI:
Python SDE (2022 - Present):
Optimized the learning speed of the speech to text model by setting up a learning algorithm using multiple GPUs
Created a system for distributed dataset augmentation on VertexAI
Created a pipeline for training the speech to text model
Implemented a pipeline for automatic tagging of audio data datasets using mfa
Created a system for lazy calculation of model training statistics to speed up resource downtime during model training
Involved in improving the internal service for viewing model training statistics
Studied the capabilities of VoIP telephony to create an automated customer support system

AlanAI:
Senior Python SDE (2022 - Present):
Created a system for recognizing key data in text
Created an infrastructure for storing, preparing and marking data for training models
Task distribution
Development management
People management
June training
Project management
'''

VACANCY = '''
About Matific

Matific is a leading global education technology provider, delivering an adaptive online learning platform for primary school mathematics. With our product being utilised by millions of students, teachers and parents in 100+ countries we are helping educate the youth and bring equality to education. With over $50M USD invested and a global team of over 150 employees, we are committed to achieving our goals. We’ve also picked up a number of awards including numerous CODiEs, Academics’ Choice and Edtech Digest to name a few.

THE ROLE

Matific is seeking a great Tech Lead experienced in server side development to join the Matific web team in our Colombo office, as part of our cutting-edge global web group.

This will involve working closely with our product and development teams to create an easy to use teacher interface, bring joy and happiness to students worldwide and build and enhance our public websites.

Given the start-up nature of the company, you will need to be flexible and inventive in the delivery of your outcomes.

This role is based out of our office in Colombo Sri Lanka.

Responsibilities:

Design, build and maintain efficient, reusable and reliable code
Identify and rectify bottlenecks and bugs in the code
Provide technical guidance and mentorship to junior developers
Ensure the security and scalability of the applications
Ensure that all code is tested and integrated properly

Requirements:

At least 5-6 years of experience in software development
Strong understanding of web protocols and web technologies
Knowledge of object-oriented programming (OOP) and software design principles
Proficient in HTML, CSS, and JavaScript
Knowledge of server-side scripting languages (e.g. PHP, Ruby, Python)
Familiarity with relational databases (e.g. MySQL, PostgreSQL)
'''

STRUCTURE_TEMPLATE = '''
{
header {
person "Tsotne Otanadze"
header "$VacancyPosition"
}
info {
full name "Tsotne Otanadze"
address "Viktor Kupradze st. 18, Tbilisi, Georgia, 0163"
phone "+995 579 159 169"
email "otanadzetsotne@yahoo.com"
linkedIn "https://www.linkedin.com/in/otanadzetsotne/"
}
content [
{
subhead "Objective"
content "$CandidateSummaryForVacation"
}
{
subhead "Professional Experience"
content {
company "$CompanyName"
position "$PositionName"
dates "($WorkingFrom - $WorkingTill)"
content "$PositionSummaryAndAchievementsMatchingVacancyPosition"
}
}
{
subhead "Technical Skills"
content "$TechnicalSkillsMatchingVacancyPosition"
}
...
]
}
'''


STRUCTURE_EXAMPLE = '''
{
header {
person "Tsotne Otanadze"
header "Vacancy position"
}
info {
full name "Tsotne Otanadze"
address "Viktor Kupradze st. 18, Tbilisi, Georgia, 0163"
phone "+995 579 159 169"
email "otanadzetsotne@yahoo.com"
linkedIn "https://www.linkedin.com/in/otanadzetsotne/"
}
content [
{
subhead "Objective"
content "Experienced IT professional with over 5 years in software development, including a strong background in server-side scripting and web technologies. Seeking the Tech Lead role at Matific to leverage my expertise in coding, system architecture, and team leadership to contribute to innovative educational technology solutions."
}
{
subhead "Professional Experience"
content [
{
company "AlanAI"
position "Tech Lead"
dates "(2023 - Present)"
content "* Developed an advanced data recognition system, demonstrating strong coding skills and the ability to maintain efficient, reusable, and reliable code.
* Established a data infrastructure optimized for machine learning, showcasing my capacity for ensuring the security and scalability of applications."
}
{
company "AlanAI"
position "Python SDE"
dates "(2022 - Present)"
content "Enhanced the training speed of AI models, reflecting my proficiency in optimizing performance and integrating complex software solutions."
}
]
}
{
subhead "Technical Skills"
content "* Proficient in HTML, CSS, JavaScript, and server-side scripting languages including PHP and Python.
* Experienced with relational databases such as MySQL."
}
]
}
'''

Structure format is not JSON
You are chief HR, your task is to adapt work experience to a specific vacancy and create a unique resume that is suitable specifically for this vacancy, in the structure of a given format.

a = {
    "header": {
        "person": "Tsotne Otanadze",
        "header": "Tech Lead"
    },
    "info": {
        "full name": "Tsotne Otanadze",
        "address": "Viktor Kupradze st. 18, Tbilisi, Georgia, 0163",
        "phone": "+995 579 159 169",
        "email": "otanadzetsotne@yahoo.com",
        "linkedIn": "https://www.linkedin.com/in/otanadzetsotne/"
    },
    "content": [
        {
            "subhead": "Objective",
            "content": "As a seasoned developer with a strong foundation in mathematics and extensive experience in full-stack development and machine learning, I am eager to bring my technical expertise, leadership skills, and innovative approach to the Tech Lead role at Matific, where I can contribute to advancing educational technology and fostering joy in learning."
        },
        {
            "subhead": "Professional Experience",
            "content": [
                {
                    "company": "AlanAI",
                    "position": "Senior Python SDE",
                    "dates": "(2022 - Present)",
                    "content": "* Led the development of key data recognition systems, aligning with Matific's commitment to effective educational tools. * Built robust infrastructure for data handling and model training, demonstrating my ability to maintain secure and scalable applications. * Mentored junior developers, providing the technical guidance and leadership sought by Matific."
                },
                {
                    "company": "AlanAI",
                    "position": "Python SDE",
                    "dates": "(2022 - Present)",
                    "content": "* Optimized AI model training, relevant to Matific's adaptive learning platform. * Implemented a distributed dataset augmentation system, indicative of my skills in ensuring efficient, reusable, and reliable code."
                },
                {
                    "company": "OT Commerce",
                    "position": "Machine learning developer",
                    "dates": "(2020 - 2021)",
                    "content": "* Developed a neural network for photo search, which could be analogous to creating adaptive learning algorithms for Matific's platform."
                },
                {
                    "company": "OT Commerce",
                    "position": "Full Stack developer",
                    "dates": "(2018 - 2021)",
                    "content": "* Engaged in the development and optimization of a CMS for online stores, showcasing my foundation in server-side scripting and web technologies as required by Matific."
                }
            ]
        },
        {
            "subhead": "Technical Skills",
            "content": "* Proficient in HTML, CSS, JavaScript, and server-side scripting languages such as Python, with a strong understanding of web protocols and technologies. * Skilled in relational databases like MySQL, aligning with Matific's tech stack requirements. * Demonstrated ability in leading projects, managing teams, and delivering training, matching the mentorship and guidance responsibilities of the Tech Lead role."
        }
    ]
}
