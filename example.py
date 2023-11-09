TEMPLATE = '''
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


EXAMPLE = '''
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
