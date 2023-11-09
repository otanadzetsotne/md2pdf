from reportlab.pdfgen.canvas import Canvas


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

p = '/Users/otana/Development/md2pdf/test.pdf'


c = Canvas(p)
c.drawString(50, 500, "Hello, I am a PDF document created with Python!")
c.save()
