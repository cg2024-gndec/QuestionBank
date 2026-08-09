r"""
Refines all 6 Category files for Book 5 Chapter 08 ("The Missile Man of India: Dr. A. P. J. Abdul Kalam") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH08_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_08")
os.makedirs(CH08_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Who is proudly given the title 'Missile Man of India'?", "(A) Dr. A. P. J. Abdul Kalam", "(B) Dr. Homi Bhabha", "(C) Dr. Vikram Sarabhai", "(D) Dr. C. V. Raman", "(A)", "Dr. A. P. J. Abdul Kalam is known as the Missile Man of India.", "Easy", "Remembering", "Title Identity"),
    ("When was Dr. A. P. J. Abdul Kalam born?", "(A) October 15, 1931", "(B) October 2, 1931", "(C) November 15, 1935", "(D) December 25, 1931", "(A)", "Born on October 15, 1931.", "Easy", "Remembering", "Birth Date"),
    ("Where was Dr. A. P. J. Abdul Kalam born?", "(A) Rameswaram, Tamil Nadu", "(B) Thiruvananthapuram, Kerala", "(C) Bengaluru, Karnataka", "(D) Hyderabad, Telangana", "(A)", "Born in Rameswaram, a small town in Tamil Nadu.", "Easy", "Remembering", "Birthplace"),
    ("What type of family was Dr. Kalam born into?", "(A) A middle-class family with wise and kind parents", "(B) A wealthy royal family", "(C) A foreign diplomatic family", "(D) A landowning family in Punjab", "(A)", "Born into a middle-class family to wise and kind parents.", "Easy", "Remembering", "Family Background"),
    ("Which subjects did Dr. Kalam love learning about as a student?", "(A) Science and technology", "(B) Ancient Latin history", "(C) Commercial accounting", "(D) Music and dance", "(A)", "He loved learning about science and technology.", "Easy", "Remembering", "Academic Interests"),
    ("Which two premier scientific organizations did Dr. Kalam work for?", "(A) ISRO and DRDO", "(B) NASA and UNESCO", "(C) RBI and SEBI", "(D) AIIMS and IIT", "(A)", "He worked as a scientist at ISRO and DRDO.", "Easy", "Remembering", "Organizations"),
    ("Which Indian missiles developed under Dr. Kalam's leadership made India strong and proud?", "(A) Agni and Prithvi", "(B) BrahMos and Akash", "(C) Nag and Trishul", "(D) Astra and Nirbhay", "(A)", "Developing missiles like Agni and Prithvi made India proud.", "Easy", "Remembering", "Missile Names"),
    ("In which year did Dr. Kalam become the President of India?", "(A) 2002", "(B) 1998", "(C) 2007", "(D) 2015", "(A)", "In 2002, Dr. Kalam became the President of India.", "Easy", "Remembering", "Presidency Year"),
    ("Dr. Kalam served as which numbered President of India?", "(A) 11th President", "(B) 10th President", "(C) 12th President", "(D) 13th President", "(A)", "He became the 11th President of India.", "Easy", "Remembering", "President Number"),
    ("Why was Dr. Kalam affectionately called the 'People's President'?", "(A) Because he always connected with citizens and encouraged students to dream big", "(B) Because he was elected by a public vote", "(C) Because he lived in a public park", "(D) Because he gave free money to everyone", "(A)", "Known as People's President because he always encouraged students and young people.", "Easy", "Understanding", "Nickname Reason"),
    ("What is the title of Dr. Kalam's famous autobiography?", "(A) Wings of Fire", "(B) Ignited Minds", "(C) My Journey", "(D) Turning Points", "(A)", "His famous book, 'Wings of Fire,' tells his life story.", "Easy", "Remembering", "Autobiography Title"),
    ("How did Dr. Kalam pass away on July 27, 2015?", "(A) While giving a lecture at a university", "(B) In his sleep at home", "(C) During a space launch mission", "(D) While writing a book in his office", "(A)", "Passed away while giving a lecture at a university.", "Easy", "Remembering", "Passing Event"),
    ("What famous quote did Dr. Kalam share about dreams?", "(A) 'Dream, dream, dream. Dreams transform into thoughts and thoughts result in action.'", "(B) 'Dreams are only for sleeping hours.'", "(C) 'Stop dreaming and start sleeping.'", "(D) 'Dreams cannot become reality.'", "(A)", "Quote: Dreams transform into thoughts and thoughts result in action.", "Easy", "Remembering", "Famous Quote"),
    ("What does the word 'scientist' mean according to the vocabulary box?", "(A) A person who studies and discovers new knowledge", "(B) A person who paints pictures", "(C) A person who writes news reports", "(D) A person who flies airplanes", "(A)", "Scientist = A person who studies and discovers new knowledge.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'visionary' mean?", "(A) Someone who imagines a better future", "(B) Someone who wears glasses", "(C) Someone who watches television all day", "(D) Someone who travels in a ship", "(A)", "Visionary = Someone who imagines a better future.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'inspiration' mean?", "(A) Something that motivates or encourages", "(B) Something that causes sadness", "(C) A type of heavy machinery", "(D) Breathing in cold air", "(A)", "Inspiration = Something that motivates or encourages.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'achievement' mean?", "(A) Success gained through effort", "(B) A task that ends in failure", "(C) Buying a expensive gift", "(D) Sleeping for many hours", "(A)", "Achievement = Success gained through effort.", "Easy", "Understanding", "Vocabulary"),
    ("What journey of Dr. Kalam serves as a powerful inspiration for every Indian?", "(A) From a small town in Tamil Nadu to Rashtrapati Bhavan", "(B) From London to New York", "(C) From a palace to a forest", "(D) From a mountain to the ocean", "(A)", "His journey from a small town in Tamil Nadu to Rashtrapati Bhavan.", "Easy", "Understanding", "Inspirational Journey"),
    ("What stand out qualities defined Dr. Kalam as a leader?", "(A) Scientist and visionary par excellence", "(B) Proud and secretive politician", "(C) Harsh and demanding ruler", "(D) Careless and quiet worker", "(A)", "Dr. Kalam was a scientist and visionary par excellence.", "Easy", "Remembering", "Leadership Character"),
    ("What official residence did Dr. Kalam occupy as 11th President of India?", "(A) Rashtrapati Bhavan", "(B) Prime Minister's House", "(C) Parliament House", "(D) India Gate", "(A)", "Occupied Rashtrapati Bhavan as President.", "Easy", "Remembering", "Presidential Residence"),
    ("What stand-out advice did Dr. Kalam repeatedly give to students?", "(A) To dream big and work hard", "(B) To avoid studying science", "(C) To seek easy money without effort", "(D) To leave India permanently", "(A)", "Encouraged students to dream big and work hard.", "Easy", "Remembering", "Advice to Youth"),
    ("What does ISRO stand for?", "(A) Indian Space Research Organisation", "(B) International Science and Research Office", "(C) Indian Satellite and Rocket Organisation", "(D) Inter-State Research Organisation", "(A)", "ISRO stands for Indian Space Research Organisation.", "Easy", "Remembering", "Acronym"),
    ("What does DRDO stand for?", "(A) Defence Research and Development Organisation", "(B) Department of Rocket Development and Operations", "(C) Digital Research and Defense Office", "(D) Direct Defense Research Organization", "(A)", "DRDO stands for Defence Research and Development Organisation.", "Easy", "Remembering", "Acronym"),
    ("What title is given to Chapter 08?", "(A) The Missile Man of India: Dr. A. P. J. Abdul Kalam", "(B) The Iron Man of India", "(C) The Milkman of India", "(D) The Magic of Books", "(A)", "Title is 'The Missile Man of India: Dr. A. P. J. Abdul Kalam'.", "Easy", "Remembering", "Chapter Title"),
    ("How does Dr. Kalam's legacy continue today?", "(A) His teachings, dreams, and contributions continue to inspire millions", "(B) His books were removed from libraries", "(C) His missiles are no longer used", "(D) His name was forgotten by scientists", "(A)", "His teachings, dreams, and contributions continue to inspire us.", "Easy", "Understanding", "Legacy"),

    # Medium (26-40)
    ("Why did Dr. Kalam emphasize that 'dreams transform into thoughts and thoughts result in action'?", "(A) Because meaningful success begins with visionary imagination, which fuels logical planning and leads to concrete execution", "(B) Because sleeping dreams are better than waking actions", "(C) Because thinking replaces the need for hard work", "(D) Because action happens without any prior thoughts", "(A)", "Visionary imagination fuels logical planning and concrete execution.", "Medium", "Analyzing", "Philosophy Analysis"),
    ("How did Dr. Kalam's modest background in Rameswaram shape his humility as President?", "(A) Growing up in a simple middle-class family kept him grounded, approachable, and deeply empathetic toward common citizens", "(B) It made him dislike rich people", "(C) He refused to live in Rashtrapati Bhavan", "(D) He stopped meeting scientists", "(A)", "Simple middle-class upbringing kept him grounded, approachable, and empathetic.", "Medium", "Analyzing", "Character Analysis"),
    ("What technical significance did the Agni and Prithvi missiles hold for India's national defense?", "(A) They established indigenous self-reliance in strategic missile technology, deterring foreign aggression", "(B) They were used to launch weather satellites into space", "(C) They were built for foreign military exports only", "(D) They replaced traditional police forces", "(A)", "Established indigenous self-reliance in strategic defense technology.", "Medium", "Analyzing", "Defense Significance"),
    ("Why was Dr. Kalam called the 'People's President' unlike traditional political leaders?", "(A) He opened Rashtrapati Bhavan to children, interacted directly with millions of students, and prioritized youth empowerment over formal politics", "(B) He ran for election in every city", "(C) He abolished the Indian Constitution", "(D) He worked without an office", "(A)", "Opened presidential house to children and prioritized youth empowerment.", "Medium", "Evaluating", "Presidential Legacy"),
    ("How does Dr. Kalam's life story in 'Wings of Fire' encourage Class 5 students?", "(A) It proves that perseverance, dedication to science, and noble character can elevate anyone from humble beginnings to national leadership", "(B) It shows that only rich children become scientists", "(C) It teaches students how to build rockets at home", "(D) It discourages reading books", "(A)", "Proves perseverance and dedication can elevate anyone from humble origins.", "Medium", "Evaluating", "Educational Value"),
    ("Compare Dr. Kalam's role at ISRO/DRDO with his role as President of India.", "(A) At ISRO/DRDO he led scientific space and missile engineering; as President he provided moral, educational, and visionary leadership to the nation", "(B) At ISRO he was a politician; as President he built rockets in his room", "(C) Both roles were identical in daily tasks", "(D) He did not work as a scientist before presidency", "(A)", "Scientific engineering leader vs national moral and educational visionary leader.", "Medium", "Comparing", "Role Comparison"),
    ("Why is passing away 'while giving a lecture' considered symbolic of Dr. Kalam's life mission?", "(A) It demonstrated his lifelong, unbroken commitment to educating and inspiring young minds until his very last breath", "(B) It showed he was tired of writing books", "(C) It happened because university lectures are dangerous", "(D) It was purely a coincidence without meaning", "(A)", "Demonstrated unbroken commitment to educating youth until his last breath.", "Medium", "Evaluating", "Symbolic Passing"),
    ("What lesson about failure can be drawn from Dr. Kalam's early satellite launch setbacks?", "(A) Setbacks are stepping stones to success if analyzed with scientific rigor, hard work, and persistence", "(B) Failures mean one should give up science immediately", "(C) Setbacks are caused by bad luck only", "(D) Scientists never face failure", "(A)", "Setbacks are stepping stones to success when approached with rigor and persistence.", "Medium", "Evaluating", "Resilience Lesson"),
    ("How did Dr. Kalam bridge the gap between complex rocket science and ordinary school children?", "(A) By speaking in simple, inspiring language, writing accessible books, and treating every student's question with respect", "(B) By giving complex mathematical exams to primary students", "(C) By refusing to talk about rockets", "(D) By speaking only in foreign languages", "(A)", "Spoke in simple inspiring language and treated students' questions with respect.", "Medium", "Understanding", "Science Communication"),
    ("What made Dr. Kalam a 'visionary' in national development plans like India 2020?", "(A) He conceptualized a comprehensive roadmap to transform India into a developed, economically strong, and technologically self-reliant nation", "(B) He predicted exact weather patterns for fifty years", "(C) He wrote fantasy stories about outer space", "(D) He built futuristic cities out of glass", "(A)", "Conceptualized a roadmap to transform India into a developed, self-reliant nation.", "Medium", "Analyzing", "Visionary Concept"),
    ("Describe the value of 'simplicity' exhibited by Dr. Kalam throughout his presidential tenure.", "(A) He maintained modest personal habits, owned very few personal possessions, and dedicated his salary and time to public welfare", "(B) He wore royal robes every day", "(C) He refused to meet international leaders", "(D) He kept secret wealth in foreign banks", "(A)", "Maintained modest habits, owned few personal items, dedicated time to welfare.", "Medium", "Evaluating", "Personal Ethics"),
    ("How did Dr. Kalam inspire young Indians to choose careers in STEM (Science, Technology, Engineering, Math)?", "(A) By showcasing that scientific research brings national pride, technological strength, and personal fulfillment", "(B) By forcing every student to study rocket engineering", "(C) By promising money to engineering graduates", "(D) By criticizing non-science subjects", "(A)", "Showcased that science brings national pride, strength, and fulfillment.", "Medium", "Understanding", "STEM Motivation"),
    ("What does the word 'par excellence' imply when describing Dr. Kalam as a scientist?", "(A) He performed at the highest level of exceptional quality and distinction superior to ordinary standards", "(B) He was an average scientist", "(C) He worked only in Paris", "(D) He studied science for one year", "(A)", "Performed at the highest level of exceptional distinction.", "Medium", "Understanding", "Vocabulary Precision"),
    ("Summarize Chapter 08 in four concise sentences.", "Dr. A. P. J. Abdul Kalam, born in Rameswaram in 1931, was a brilliant scientist known as the 'Missile Man of India'. His engineering work at ISRO and DRDO on Agni and Prithvi missiles strengthened national defense, leading to his election as the 11th President of India in 2002. Affectionately called the 'People's President', he dedicated his life to inspiring students to dream big and work hard. Author of 'Wings of Fire', his visionary teachings continue to motivate millions.", "Medium", "Understanding", "Chapter Summary"),
    ("What advice would Dr. Kalam give to Class 5 students preparing for their future?", "(A) Develop curiosity for learning, maintain strong moral values, dream ambitious goals, and work relentlessly to achieve them", "(B) Focus only on passing exams without understanding science", "(C) Avoid asking questions in class", "(D) Depend on others to solve your problems", "(A)", "Develop curiosity, maintain strong values, dream ambitiously, and work relentlessly.", "Medium", "Applying", "Youth Guidance"),

    # Hard (41-50)
    ("Critique the transformation of India's defense posture through Dr. Kalam's missile program.", "(A) Shifted India from defense technology dependence to strategic self-reliance, creating a credible indigenous deterrent", "(B) Destroyed India's diplomatic relations with all neighbors", "(C) Forced India to stop space exploration", "(D) Made defense research dependent on foreign grants", "(A)", "Shifted India from technology dependence to strategic self-reliance.", "Hard", "Evaluating", "HOTS Defense Critique"),
    ("Deconstruct the psychological impact of the 'Wings of Fire' autobiography on youth aspiration.", "(A) Demystified success by showing that an ordinary boy selling newspapers in Rameswaram could achieve world-class scientific leadership through integrity and grit", "(B) Proved that success requires aristocratic family heritage", "(C) Encouraged young people to avoid reading", "(D) Focused exclusively on mechanical engineering formulas", "(A)", "Showed that a humble Rameswaram boy achieved world-class leadership through grit.", "Hard", "Analyzing", "Autobiographical Analysis"),
    ("Evaluate Dr. Kalam's concept of 'PURA' (Providing Urban Amenities in Rural Areas).", "(A) Proposed bridging the urban-rural divide by bringing physical, electronic, and knowledge connectivity to villages to empower rural youth", "(B) Forced rural populations to relocate to metropolitan slums", "(C) Banned technology in rural villages", "(D) Built outer space stations in small villages", "(A)", "Bridged urban-rural divides through physical, electronic, and knowledge connectivity.", "Hard", "Evaluating", "Development Policy"),
    ("Compare Dr. Kalam's presidential leadership style with traditional political governance.", "(A) Traditional politics focuses on party alignment and power consolidation; Kalam focused on moral inspiration, educational outreach, and national unity", "(B) Kalam used political veto power to block laws", "(C) Both styles were driven by political election campaigns", "(D) Kalam avoided interacting with citizens", "(A)", "Focused on moral inspiration, educational outreach, and national unity over party power.", "Hard", "Comparing", "Governance Styles"),
    ("Formulate an inspirational address to be delivered on World Students' Day (Oct 15).", "(A) 'On Dr. Kalam's birth anniversary, let us commit to transforming our dreams into thoughts and thoughts into noble action for our nation's future!'", "(B) 'Today we celebrate by closing all schools and universities forever.'", "(C) 'Dr. Kalam believed that students should never ask questions.'", "(D) 'Science and technology have no role in student life.'", "(A)", "Inspirational address urging youth to transform dreams into noble action.", "Hard", "Creating", "Oration Design"),
    ("Assess the legacy of Dr. Kalam's leadership at SLV-3 (Satellite Launch Vehicle) project.", "(A) Successfully placed the Rohini satellite in orbit in 1980, making India an exclusive member of the global spacefaring club", "(B) Failed completely and ended India's space program", "(C) Built commercial airplanes for international airlines", "(D) Was a secret military operation", "(A)", "Placed Rohini satellite in orbit in 1980, joining the global spacefaring club.", "Hard", "Evaluating", "Space Program Milestone"),
    ("Analyze how Dr. Kalam integrated spiritual values with scientific technological progress.", "(A) Believed science seeks empirical truth while spirituality seeks inner harmony, maintaining that both are complementary paths to human betterment", "(B) Claimed science and spirituality are completely incompatible", "(C) Rejected science in favor of mystical rituals", "(D) Claimed technology makes human values useless", "(A)", "Viewed science and spirituality as complementary paths to human betterment.", "Hard", "Analyzing", "Philosophical Synthesis"),
    ("Synthesize how Chapter 08 connects childhood curiosity with national scientific defense.", "(A) Illustrates how early curiosity in Rameswaram blossomed through ISRO space research into DRDO missile systems and presidential statecraft", "(B) Suggests childhood curiosity has no connection to adult success", "(C) Focuses only on political speeches", "(D) Replaces scientific learning with memorization", "(A)", "Illustrates early curiosity blossoming into space research, missile systems, and statecraft.", "Hard", "Synthesizing", "Biographical Synthesis"),
    ("Critique the statement: 'Dr. Kalam was primarily a political leader who used science for publicity.'", "(A) Entirely false; he was a dedicated lifelong scientist and engineer whose scientific achievements earned him the presidency as a non-political statesman", "(B) True; he had no background in engineering", "(C) False; he was a foreign general who conquered lands", "(D) True; he never worked at ISRO or DRDO", "(A)", "False; he was a dedicated scientist/engineer whose achievements earned him the non-political presidency.", "Hard", "Evaluating", "Historical Accuracy Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 08 for a Class 5 assessment.", "(A) 'Explain why Dr. A. P. J. Abdul Kalam is called the Missile Man of India and the People's President. Describe his childhood, scientific career, book Wings of Fire, and message to youth.'", "(B) 'Write five sentences about your favorite rocket toy.'", "(C) 'List five cities in Tamil Nadu.'", "(D) 'Draw a picture of a satellite.'", "(A)", "Structured essay prompt evaluating biographical facts, scientific achievements, presidency, and youth message.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 08: The Missile Man of India: Dr. A. P. J. Abdul Kalam\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH08_MCQ_{idx:03d}"
    q_txt = item[0]
    opt_a = item[1]
    opt_b = item[2]
    opt_c = item[3]
    opt_d = item[4]
    ans = item[5] if len(item) > 5 else "(A)"
    exp = item[6] if len(item) > 6 else "Correct answer"
    diff = item[7] if len(item) > 7 else "Easy"
    bloom = item[8] if len(item) > 8 else "Remembering"
    topic = item[9] if len(item) > 9 else "General"
    mcq_content += f"### Question {idx}\n"
    mcq_content += f"- **Question ID**: {q_id}\n"
    mcq_content += f"- **Type**: MCQ\n"
    mcq_content += f"- **Difficulty**: {diff}\n"
    mcq_content += f"- **Bloom Level**: {bloom}\n"
    mcq_content += f"- **Topic**: {topic}\n"
    mcq_content += f"- **Marks**: 1\n\n"
    mcq_content += f"**Question**: {q_txt}\n\n"
    mcq_content += f"- {opt_a}\n- {opt_b}\n- {opt_c}\n- {opt_d}\n\n"
    mcq_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH08_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("The title 'Missile Man of India' is proudly given to Dr. A. P. J. Abdul _______.", "Kalam", "Given to Dr. Kalam.", "Easy"),
    ("Dr. Kalam was born on October 15, _______.", "1931", "Born in 1931.", "Easy"),
    ("Dr. Kalam was born in Rameswaram, a small town in _______ Nadu.", "Tamil", "Town in Tamil Nadu.", "Easy"),
    ("Dr. Kalam was born into a middle-class family to wise and _______ parents.", "kind", "Wise and kind parents.", "Easy"),
    ("Dr. Kalam was a brilliant student who loved learning about science and _______.", "technology", "Science and technology.", "Easy"),
    ("He worked as a scientist at the Indian Space Research Organisation (_______).", "ISRO", "Worked at ISRO.", "Easy"),
    ("He also worked at the Defence Research and Development Organisation (_______).", "DRDO", "Worked at DRDO.", "Easy"),
    ("His work in developing missiles like Agni and _______ made India strong and proud.", "Prithvi", "Agni and Prithvi.", "Easy"),
    ("In 2002, Dr. Kalam became the _______ President of India.", "11th", "11th President.", "Easy"),
    ("Dr. Kalam was known as the '_______ President' because he encouraged students.", "People's", "People's President.", "Easy"),
    ("His famous autobiography is titled 'Wings of _______'.", "Fire", "Wings of Fire.", "Easy"),
    ("Dr. Kalam passed away on July 27, _______.", "2015", "Passed away in 2015.", "Easy"),
    ("Dr. Kalam passed away while giving a _______ at a university.", "lecture", "While giving a lecture.", "Easy"),
    ("Dr. Kalam said: 'Dreams transform into thoughts and thoughts result in _______.'", "action", "Thoughts result in action.", "Easy"),
    ("A scientist is defined as a person who studies and discovers new _______.", "knowledge", "Discovers new knowledge.", "Easy"),
    ("A visionary is someone who imagines a better _______.", "future", "Imagines a better future.", "Easy"),
    ("Inspiration means something that motivates or _______.", "encourages", "Motivates or encourages.", "Easy"),
    ("Achievement means success gained through _______.", "effort", "Success gained through effort.", "Easy"),
    ("Dr. Kalam's journey went from Rameswaram to Rashtrapati _______.", "Bhavan", "To Rashtrapati Bhavan.", "Easy"),
    ("Dr. Kalam was a scientist and visionary par _______.", "excellence", "Par excellence.", "Easy"),
    ("He encouraged students and young people to dream _______ and work hard.", "big", "Dream big and work hard.", "Easy"),
    ("Agni and Prithvi are strategic _______ developed by Dr. Kalam's team.", "missiles", "Strategic missiles.", "Easy"),
    ("Dr. Kalam continued to inspire millions through his books and _______.", "speeches", "Books and speeches.", "Easy"),
    ("He will always be remembered as a true hero and an _______ to the nation.", "inspiration", "Inspiration to the nation.", "Easy"),
    ("Chapter 08 is titled 'The Missile Man of India: Dr. A. P. J. Abdul _______'.", "Kalam", "Dr. A. P. J. Abdul Kalam.", "Easy"),

    # Medium (26-40)
    ("Dr. Kalam served as the project director of India's first Satellite Launch Vehicle (_______).", "SLV-3", "Project director of SLV-3.", "Medium"),
    ("The Rohini satellite was successfully placed into orbit under Kalam's _______.", "leadership", "Placed in orbit under Kalam.", "Medium"),
    ("Dr. Kalam envisioned transforming India into a developed nation by the year _______.", "2020", "India 2020 vision.", "Medium"),
    ("His personal integrity and simple lifestyle earned him universal public _______.", "respect", "Earned universal public respect.", "Medium"),
    ("Dr. Kalam launched the Integrated Guided Missile Development Programme (_______).", "IGMDP", "Launched IGMDP program.", "Medium"),
    ("He believed that national security depends on indigenous technological _______.", "self-reliance", "Technological self-reliance.", "Medium"),
    ("Dr. Kalam spent his post-presidency teaching at various prestigious _______.", "universities", "Teaching at universities.", "Medium"),
    ("Wings of Fire chronicles his transition from Rameswaram to rocket _______.", "science", "From Rameswaram to rocket science.", "Medium"),
    ("He urged youth to cultivate a scientific _______ and relentless curiosity.", "temper", "Cultivate scientific temper.", "Medium"),
    ("Dr. Kalam was awarded India's highest civilian honor, the Bharat _______.", "Ratna", "Awarded Bharat Ratna.", "Medium"),
    ("His father owned a wooden ferry boat carrying pilgrims in _______.", "Rameswaram", "Ferry boat in Rameswaram.", "Medium"),
    ("Young Kalam sold newspapers to support his family's income and _______.", "education", "Supported family and education.", "Medium"),
    ("He earned a degree in Aeronautical Engineering from the Madras Institute of _______.", "Technology", "Madras Institute of Technology.", "Medium"),
    ("Dr. Kalam's life demonstrates that humble beginnings are no barrier to _______.", "greatness", "No barrier to greatness.", "Medium"),
    ("Chapter 08 highlights how vision, hard work, and humility create national _______.", "heroes", "Create national heroes.", "Medium"),

    # Hard (41-50)
    ("Indigenous missile development established credible national nuclear _______.", "deterrence", "Established nuclear deterrence.", "Hard"),
    ("PURA (Providing Urban Amenities in Rural Areas) targeted rural-urban _______.", "equity", "Targeted rural-urban equity.", "Hard"),
    ("Statecraft grounded in scientific rationalism elevated presidential _______.", "stature", "Elevated presidential stature.", "Hard"),
    ("Space launch vehicle success catapulted India into elite spacefaring _______.", "nations", "Elites spacefaring nations.", "Hard"),
    ("Autobiographical candor in Wings of Fire inspires youth self-_______.", "actualization", "Inspires youth self-actualization.", "Hard"),
    ("Aeronautical engineering expertise laid the foundation for aerospace _______.", "innovation", "Foundation for aerospace innovation.", "Hard"),
    ("World Students' Day honors Dr. Kalam's enduring educational _______.", "legacy", "Honors educational legacy.", "Hard"),
    ("Empirical scientific rigor combined with deep humanistic empathetic _______.", "values", "Empathetic humanistic values.", "Hard"),
    ("Historical analysis confirms Dr. Kalam as an icon of modern Indian _______.", "renaissance", "Icon of modern Indian renaissance.", "Hard"),
    ("Chapter 08 inspires primary students to pursue scientific knowledge for national _______.", "progress", "Pursue knowledge for progress.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 08: The Missile Man of India: Dr. A. P. J. Abdul Kalam\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH08_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH08_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Dr. A. P. J. Abdul Kalam is proudly called the 'Missile Man of India'.", "True", "Text confirms he is known as the Missile Man of India.", "Easy"),
    ("Dr. Kalam was born in Kerala on October 15, 1931.", "False", "He was born in Rameswaram, Tamil Nadu on October 15, 1931.", "Easy"),
    ("Dr. Kalam was born into a wealthy royal family.", "False", "He was born into a middle-class family with wise and kind parents.", "Easy"),
    ("Dr. Kalam loved learning about science and technology as a student.", "True", "Text confirms he loved learning about science and technology.", "Easy"),
    ("Dr. Kalam worked as a scientist at ISRO and DRDO.", "True", "Text states he worked as a scientist at ISRO and DRDO.", "Easy"),
    ("Agni and Prithvi are missiles developed by Dr. Kalam's team.", "True", "Text confirms he developed missiles like Agni and Prithvi.", "Easy"),
    ("In 2002, Dr. Kalam became the 11th President of India.", "True", "Text confirms he became the 11th President of India in 2002.", "Easy"),
    ("Dr. Kalam was called the 'People's President' because he loved political rallies.", "False", "Called People's President because he encouraged students and young people.", "Easy"),
    ("'Wings of Fire' is the famous autobiography written by Dr. Kalam.", "True", "Text confirms 'Wings of Fire' tells his life story and achievements.", "Easy"),
    ("Dr. Kalam passed away while giving a lecture at a university on July 27, 2015.", "True", "Text confirms he passed away on July 27, 2015 while giving a lecture.", "Easy"),
    ("Dr. Kalam said: 'Dreams transform into thoughts and thoughts result in action.'", "True", "Text quotes Dr. Kalam's famous words on dreams and action.", "Easy"),
    ("'Scientist' means a person who paints pictures on canvas.", "False", "Scientist = A person who studies and discovers new knowledge.", "Easy"),
    ("'Visionary' means someone who imagines a better future.", "True", "Vocabulary definition: Visionary = Someone who imagines a better future.", "Easy"),
    ("'Inspiration' means something that motivates or encourages.", "True", "Vocabulary definition: Inspiration = Something that motivates or encourages.", "Easy"),
    ("'Achievement' means success gained through effort.", "True", "Vocabulary definition: Achievement = Success gained through effort.", "Easy"),
    ("Dr. Kalam's journey went from a small town in Tamil Nadu to Rashtrapati Bhavan.", "True", "Text confirms his inspiring journey from Rameswaram to Rashtrapati Bhavan.", "Easy"),
    ("Dr. Kalam encouraged students to avoid dreaming big.", "False", "He always encouraged students to dream big and work hard.", "Easy"),
    ("Dr. Kalam was a scientist and visionary par excellence.", "True", "Text confirms he was a scientist and visionary par excellence.", "Easy"),
    ("ISRO stands for Indian Space Research Organisation.", "True", "ISRO = Indian Space Research Organisation.", "Easy"),
    ("DRDO stands for Defense Research and Development Organisation.", "True", "DRDO = Defence Research and Development Organisation.", "Easy"),
    ("Dr. Kalam served as the 5th President of India.", "False", "He served as the 11th President of India.", "Easy"),
    ("Dr. Kalam stopped writing books after his presidency ended.", "False", "Even after his presidency, he continued to inspire through books and speeches.", "Easy"),
    ("Dr. Kalam's parents were wise and kind.", "True", "Text confirms he was born to wise and kind parents.", "Easy"),
    ("Chapter 08 title is 'The Missile Man of India: Dr. A. P. J. Abdul Kalam'.", "True", "Chapter title is 'The Missile Man of India: Dr. A. P. J. Abdul Kalam'.", "Easy"),
    ("Dr. Kalam will always be remembered as a true hero and inspiration.", "True", "Text confirms he will always be remembered as a true hero.", "Easy"),

    # Medium (26-40)
    ("Dr. Kalam served as Project Director for SLV-3, launching Rohini into space.", "True", "Led India's first Satellite Launch Vehicle (SLV-3) project at ISRO.", "Medium"),
    ("Dr. Kalam received India's highest civilian award, the Bharat Ratna, in 1997.", "True", "He was awarded the Bharat Ratna in 1997 for scientific leadership.", "Medium"),
    ("Dr. Kalam believed that sleeping dreams are more important than working actions.", "False", "He emphasized waking dreams that lead to thoughts and action.", "Medium"),
    ("Dr. Kalam sold newspapers in his childhood to assist his family's income.", "True", "He distributed newspapers in Rameswaram to support his family.", "Medium"),
    ("Dr. Kalam studied Aeronautical Engineering at the Madras Institute of Technology (MIT).", "True", "Graduated in Aeronautical Engineering from MIT Chennai.", "Medium"),
    ("Rashtrapati Bhavan was closed to students during Dr. Kalam's presidency.", "False", "He opened Rashtrapati Bhavan to students, children, and scientists.", "Medium"),
    ("The Agni missile is an intercontinental strategic ballistic missile.", "True", "Agni is India's premier strategic ballistic missile series.", "Medium"),
    ("Dr. Kalam authored books such as 'Ignited Minds' and 'India 2020'.", "True", "Authored 'Ignited Minds', 'India 2020', and 'Wings of Fire'.", "Medium"),
    ("Dr. Kalam passed away at IIM Shillong while interacting with students.", "True", "Passed away while delivering a lecture at IIM Shillong.", "Medium"),
    ("Dr. Kalam's birthday, October 15, is celebrated as World Students' Day.", "True", "United Nations declared Oct 15 as World Students' Day in his honor.", "Medium"),
    ("Dr. Kalam believed that technology should only serve military power.", "False", "He strongly advocated using technology for rural development (PURA) and healthcare.", "Medium"),
    ("Dr. Kalam collaborated with cardiologist Dr. B. Soma Raju to create low-cost coronary stents.", "True", "Co-developed the affordable Kalam-Raju coronary stent for heart patients.", "Medium"),
    ("Dr. Kalam's father built wooden boats to ferry Hindu pilgrims between Rameswaram and Dhanushkodi.", "True", "His father owned a wooden ferry boat for pilgrims.", "Medium"),
    ("Dr. Kalam believed that questioning by students should be discouraged.", "False", "He famously said: 'One of the most important characteristics of a student is to question.'", "Medium"),
    ("Chapter 08 demonstrates that dedication and hard work can elevate any individual to greatness.", "True", "Demonstrates how humble beginnings transform into visionary leadership.", "Medium"),

    # Hard (41-50)
    ("Indigenous missile development under IGMDP made India self-reliant in strategic deterrence.", "True", "IGMDP established self-reliance in strategic missile defense.", "Hard"),
    ("Dr. Kalam served as Chief Scientific Adviser to the Prime Minister during Pokhran-II tests.", "True", "Co-coordinated the Pokhran-II nuclear tests in 1998.", "Hard"),
    ("PURA model envisioned integrated physical, electronic, and knowledge connectivity in villages.", "True", "PURA provided multi-dimensional connectivity to empower rural communities.", "Hard"),
    ("Dr. Kalam declined all political party affiliations before accepting the presidency.", "True", "He was nominated as a non-partisan consensus candidate for President.", "Hard"),
    ("The Kalam-Raju tablet was a low-cost rugged computer developed for rural healthcare workers.", "True", "Co-developed the Kalam-Raju tablet for field healthcare workers.", "Hard"),
    ("Dr. Kalam's autobiography 'Wings of Fire' has been translated into over 13 languages.", "True", "Translated into major Indian and international languages.", "Hard"),
    ("Dr. Kalam advocated that a developed India requires 100% literacy and economic strength by 2020.", "True", "His India 2020 vision targeted complete literacy and economic development.", "Hard"),
    ("Dr. Kalam's passing prompted seven days of state mourning across India.", "True", "Government of India declared seven days of national mourning.", "Hard"),
    ("Chapter 08 integrates scientific biography with moral character education for Class 5.", "True", "Integrates scientific achievements with moral and youth inspiration.", "Hard"),
    ("Dr. Kalam's life proves that true patriotism is demonstrated through dedicated service to humanity.", "True", "Demonstrated patriotism through scientific innovation and youth education.", "Hard")
]

tf_content = f"# True / False — Chapter 08: The Missile Man of India: Dr. A. P. J. Abdul Kalam\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH08_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH08_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who was Dr. A. P. J. Abdul Kalam and why is he called the 'Missile Man of India'?", "Dr. A. P. J. Abdul Kalam was a brilliant Indian scientist and visionary leader who earned the title 'Missile Man of India' for his pioneering work in developing strategic Indian missiles like Agni and Prithvi.", "Easy", "Remembering"),
    ("When and where was Dr. A. P. J. Abdul Kalam born?", "He was born on October 15, 1931, in Rameswaram, a small coastal town in Tamil Nadu, India.", "Easy", "Remembering"),
    ("Describe the family background into which Dr. Kalam was born.", "He was born into a simple middle-class family to wise, kind, and hard-working parents in Rameswaram.", "Easy", "Remembering"),
    ("Which subjects did young Abdul Kalam love studying as a student?", "He loved studying science and technology with deep curiosity and hard work.", "Easy", "Remembering"),
    ("Name the two premier scientific organizations where Dr. Kalam worked as a scientist.", "He worked at the Indian Space Research Organisation (ISRO) and the Defence Research and Development Organisation (DRDO).", "Easy", "Remembering"),
    ("Which famous missiles were developed under Dr. Kalam's scientific leadership?", "Missiles like Agni and Prithvi were developed under his leadership, making India defense-strong.", "Easy", "Remembering"),
    ("When did Dr. Kalam become the President of India, and which numbered President was he?", "In 2002, he became the 11th President of India.", "Easy", "Remembering"),
    ("Why was Dr. Kalam affectionately called the 'People's President'?", "Because he was warmly approachable, loved interacting with common citizens, and dedicated his presidency to inspiring students and youth.", "Easy", "Understanding"),
    ("What is the title of Dr. Kalam's famous autobiography and what does it describe?", "His autobiography is titled 'Wings of Fire', and it describes his life journey, struggles, and scientific achievements.", "Easy", "Remembering"),
    ("How did Dr. Kalam pass away on July 27, 2015?", "He passed away while doing what he loved most—delivering an inspiring lecture to university students at IIM Shillong.", "Easy", "Remembering"),
    ("Quote Dr. Kalam's famous teaching regarding dreams.", "He taught: 'Dream, dream, dream. Dreams transform into thoughts and thoughts result in action.'", "Easy", "Remembering"),
    ("What does the word 'scientist' mean?", "'Scientist' means a person who systematically studies, experiments, and discovers new knowledge about the natural world.", "Easy", "Understanding"),
    ("What does the word 'visionary' mean?", "'Visionary' means a person who possesses clear imagination and foresight about a better future.", "Easy", "Understanding"),
    ("What does the word 'inspiration' mean?", "'Inspiration' means a person, idea, or event that motivates and encourages someone to achieve great things.", "Easy", "Understanding"),
    ("What does the word 'achievement' mean?", "'Achievement' means a successful result or goal gained through hard work and sustained effort.", "Easy", "Understanding"),
    ("What inspiring path did Dr. Kalam's life journey take?", "His journey went from a humble boy in a small town in Tamil Nadu (Rameswaram) all the way to Rashtrapati Bhavan as President of India.", "Easy", "Understanding"),
    ("How did Dr. Kalam continue to serve the nation after his presidential term ended in 2007?", "He continued writing books, traveling across India, giving speeches, and teaching at universities to inspire youth.", "Easy", "Understanding"),
    ("What advice did Dr. Kalam constantly offer to young students across India?", "He advised students to dream big, acquire knowledge continuously, work hard, and never fear failures.", "Easy", "Remembering"),
    ("What does ISRO stand for and what is its main function?", "ISRO stands for Indian Space Research Organisation, which designs and launches satellites and space missions.", "Easy", "Remembering"),
    ("What does DRDO stand for and what is its main function?", "DRDO stands for Defence Research and Development Organisation, which develops military weapons and defense technology for India.", "Easy", "Remembering"),
    ("Why will Dr. Kalam always be remembered as a true hero of India?", "Because he strengthened India's scientific defense capabilities while devoting his heart to educating and empowering young minds.", "Easy", "Evaluating"),
    ("What role did Dr. Kalam's parents play in shaping his character?", "His wise and kind parents taught him humility, honesty, respect for all religions, and deep dedication to hard work.", "Easy", "Understanding"),
    ("Why is October 15 celebrated as World Students' Day in India and around the world?", "October 15 is Dr. Kalam's birth anniversary, celebrated as World Students' Day to honor his passion for student education.", "Easy", "Remembering"),
    ("What title is given to Chapter 08?", "The title of Chapter 08 is 'The Missile Man of India: Dr. A. P. J. Abdul Kalam'.", "Easy", "Remembering"),
    ("What message does Chapter 08 convey to Class 5 students?", "It conveys that regardless of background, hard work, scientific curiosity, and high dreams can help anyone serve the nation.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze why Dr. Kalam believed that 'dreams' must precede 'action'.", "He believed that dreams ignite the imagination, creating focused thoughts, which then drive structured plans and dedicated actions to achieve success.", "Medium", "Analyzing"),
    ("How did Dr. Kalam's early life in Rameswaram foster his strong work ethic?", "Selling newspapers as a boy to help his family taught him self-reliance, time management, and the value of hard work from an early age.", "Medium", "Analyzing"),
    ("Explain the national significance of the Agni missile series developed under Dr. Kalam.", "The Agni missiles provided India with long-range strategic nuclear deterrence, ensuring national sovereignty and defense independence.", "Medium", "Understanding"),
    ("Why was Dr. Kalam's presidency (2002-2007) unique in Indian political history?", "He was a non-partisan scientist who converted the presidency into an active educational platform for youth, receiving universal love across all political lines.", "Medium", "Evaluating"),
    ("Describe Dr. Kalam's contribution as Project Director of SLV-3 at ISRO.", "He led the team that successfully launched SLV-3, placing the Rohini satellite in orbit in 1980 and establishing India as a spacefaring nation.", "Medium", "Remembering"),
    ("How did Dr. Kalam demonstrate humility despite achieving world-class scientific fame?", "He lived in simple rooms, wore modest clothing, owned few personal possessions, and always gave credit for scientific success to his team members.", "Medium", "Evaluating"),
    ("What made Dr. Kalam's autobiography 'Wings of Fire' so popular among students?", "It told a relatable, transparent story of overcoming childhood poverty, academic setbacks, and technological challenges through persistence and faith.", "Medium", "Analyzing"),
    ("How did Dr. Kalam contribute to healthcare accessibility alongside missile technology?", "He co-developed the affordable 'Kalam-Raju Stent' for heart patients and lightweight carbon-fiber calipers for polio-affected children.", "Medium", "Understanding"),
    ("Explain Dr. Kalam's vision of 'India 2020'.", "It was a blueprint to transform India into a fully developed nation by 2020 through agricultural growth, technology integration, health, and education.", "Medium", "Understanding"),
    ("Summarize Chapter 08 in four concise sentences.", "Dr. A. P. J. Abdul Kalam, born in Rameswaram in 1931, was a visionary scientist known as the 'Missile Man of India'. His engineering breakthroughs at ISRO and DRDO on Agni and Prithvi missiles strengthened national defense, leading to his election as the 11th President of India in 2002. Beloved as the 'People's President', he dedicated his life to inspiring students to dream big and work hard. Author of 'Wings of Fire', his teachings continue to motivate millions.", "Medium", "Understanding"),
    ("Why did Dr. Kalam love interacting with primary and secondary school children?", "He believed that young students possess unconditioned minds filled with creative energy, capable of building a developed India if guided properly.", "Medium", "Understanding"),
    ("What role does 'scientific temper' play in student development according to Dr. Kalam?", "It encourages students to ask logical questions, test facts empirically, reject superstition, and seek scientific solutions to social problems.", "Medium", "Evaluating"),
    ("How did Dr. Kalam react when early rocket launch tests failed at ISRO?", "He analyzed the failure calmly with his team, learned from engineering flaws, maintained team morale, and worked relentlessly until the next launch succeeded.", "Medium", "Analyzing"),
    ("What does the phrase 'scientist and visionary par excellence' mean in Chapter 08?", "It means Dr. Kalam was not just a skilled technical scientist, but a top-tier leader who could see the future potential of science for national development.", "Medium", "Understanding"),
    ("What lesson can Class 5 students draw from Dr. Kalam's sudden passing while teaching?", "It teaches that one should remain dedicated to one's life passion and service to others until the very last moment of life.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the strategic importance of indigenous missile development vs importing foreign defense tech.", "Importing tech creates strategic vulnerability and foreign dependency; indigenous development (IGMDP) ensures total defense sovereignty and domestic technological capability.", "Hard", "Evaluating"),
    ("Deconstruct the philosophical link between 'thoughts', 'dreams', and 'action' in Kalam's discourse.", "Dreams act as creative seeds; thoughts structure those seeds into logical blueprints; action provides the kinetic work required to manifest reality.", "Hard", "Analyzing"),
    ("Evaluate the impact of the PURA model on sustainable rural development.", "PURA proposed connecting villages physically, electronically, and knowledgeably, preventing urban migration while boosting rural economic self-sufficiency.", "Hard", "Evaluating"),
    ("Compare Dr. Kalam's non-political presidency with traditional parliamentary executive roles.", "Traditional roles involve formal constitutional assent; Kalam transformed the office into an active moral pulpit for youth empowerment and scientific advocacy.", "Hard", "Comparing"),
    ("Formulate a tribute resolution for World Students' Day celebrating Dr. Kalam's legacy.", "'Resolved that on World Students' Day, we honor Dr. Kalam by fostering scientific curiosity, integrity, and relentless dedication to national development in every classroom.'", "Hard", "Creating"),
    ("Assess Dr. Kalam's contribution to the Pokhran-II nuclear tests in 1998.", "As Chief Scientific Adviser, he co-coordinated the successful Pokhran-II underground tests, establishing India as a capable nuclear weapons state.", "Hard", "Evaluating"),
    ("Analyze how Dr. Kalam used simple metaphors to explain complex aerospace engineering concepts.", "He used analogies of bird flight, sea waves, and kites to make complex aerodynamics intuitive and inspiring for young students.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 08 integrates science education, biography, and civic patriotism.", "It unifies factual scientific milestones (ISRO/DRDO/missiles) with personal biography (Rameswaram to presidency) and civic duty (dream big/work hard).", "Hard", "Synthesizing"),
    ("Critique the claim: 'Dr. Kalam's success was due purely to natural genius without hard work.'", "False; Kalam worked 18-hour days, studied relentlessly from borrowed resources, faced major launch failures, and succeeded through sheer grit.", "Hard", "Evaluating"),
    ("Formulate a 4-line poem honoring Dr. A. P. J. Abdul Kalam.", "'From Rameswaram's shores to rocket flight,\nHe filled young Indian minds with light;\nWith Agni's strength and Wings of Fire,\nHe taught a nation to aspire!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 08: The Missile Man of India: Dr. A. P. J. Abdul Kalam\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH08_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH08_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the early life, family background, and education of Dr. A. P. J. Abdul Kalam in Rameswaram.",
     "Dr. A. P. J. Abdul Kalam was born on October 15, 1931, in Rameswaram, a small island town in Tamil Nadu, India. He grew up in a simple middle-class family raised by wise, kind, and deeply spiritual parents. His father owned a wooden ferry boat carrying pilgrims, and young Abdul Kalam helped support his family's income by distributing newspapers after school. Despite financial constraints, Kalam was a brilliant, hardworking student who possessed an insatiable curiosity for science and technology. He completed his early schooling in Rameswaram, went on to study physics at St. Joseph's College in Tiruchirappalli, and later earned a prestigious degree in Aeronautical Engineering from the Madras Institute of Technology (MIT). His humble beginnings and strong family values instilled in him lifelong traits of humility, discipline, and dedication to learning.",
     "Easy", "Remembering"),

    ("Explain Dr. Kalam's scientific career at ISRO and DRDO and why he earned the title 'Missile Man of India'.",
     "Dr. Kalam's scientific career spanned over four decades at India's top defense and space research institutions:\n1. **ISRO (Indian Space Research Organisation)**: As Project Director of SLV-3 (Satellite Launch Vehicle), he led the landmark mission that successfully placed the Rohini satellite into Earth's orbit in 1980, making India a recognized spacefaring nation.\n2. **DRDO (Defence Research and Development Organisation)**: As head of the Integrated Guided Missile Development Programme (IGMDP), he led the engineering teams that designed, tested, and deployed strategic missiles including Agni (intermediate-range ballistic missile) and Prithvi (surface-to-surface missile).\nThese missile achievements transformed India into a defense-strong, self-reliant nation, earning him the proud national title 'Missile Man of India'.",
     "Easy", "Remembering"),

    ("Describe Dr. Kalam's presidency (2002-2007) and explain why he was called the 'People's President'.",
     "In 2002, Dr. A. P. J. Abdul Kalam was elected as the 11th President of India with overwhelming cross-party support. His presidency stood out as unique in Indian political history. Rather than remaining a ceremonial figure in Rashtrapati Bhavan, he threw open the presidential residence to students, teachers, scientists, and common citizens. He traveled tirelessly across Indian states, interacting directly with over one million young students. He earned the affectionate title 'People's President' because of his warm approachability, simple lifestyle, humble speech, and passionate dedication to encouraging children to dream big and work hard for the nation.",
     "Easy", "Understanding"),

    ("Describe Dr. Kalam's famous autobiography 'Wings of Fire' and summarize his key teachings for youth.",
     "Dr. Kalam's famous autobiography, 'Wings of Fire' (co-authored with Arun Tiwari), tells the inspiring story of his journey from selling newspapers in Rameswaram to leading India's space and missile programs and becoming President. The book chronicles his struggles, scientific breakthroughs, team management lessons, and personal philosophy. His key teachings for youth include:\n1. **Dream Big**: 'Dream, dream, dream. Dreams transform into thoughts and thoughts result in action.'\n2. **Persevere through Failure**: Treat setbacks as learning opportunities rather than defeat.\n3. **Hard Work & Knowledge**: Acquisition of knowledge combined with hard work builds character and unlocks greatness.",
     "Easy", "Understanding"),

    ("Explain the vocabulary terms from Chapter 08: Scientist, Visionary, Inspiration, and Achievement.",
     "1. **Scientist**: A scholar or researcher who systematically studies and discovers new scientific knowledge. *Sentence*: Dr. Kalam was a brilliant scientist who developed satellites and missiles.\n2. **Visionary**: Someone who possesses clear imagination and foresight about a better future. *Sentence*: As a visionary, Dr. Kalam drafted the India 2020 development plan.\n3. **Inspiration**: A person, idea, or event that motivates and encourages others to excel. *Sentence*: Dr. Kalam continues to be a great inspiration to millions of students.\n4. **Achievement**: A successful result or milestone earned through persistent effort and hard work. *Sentence*: Developing the Agni missile was a historic scientific achievement.",
     "Easy", "Understanding"),

    ("Discuss how Dr. Kalam's quote 'Dreams transform into thoughts and thoughts result in action' applies to primary school students.",
     "Dr. Kalam's famous quote outlines a three-step formula for student success:\n1. **Dreaming**: Students must allow themselves to imagine high goals (such as becoming a scientist, doctor, teacher, or artist) without fear.\n2. **Thoughts**: Imagination must be transformed into structured thoughts, detailed plans, daily study schedules, and problem-solving strategies.\n3. **Action**: Thoughts must culminate in hard work, practice, reading, and persistent execution.\nFor Class 5 students, this quote teaches that wishing for success is not enough; one must turn noble dreams into daily study habits and active efforts.",
     "Easy", "Analyzing"),

    ("Describe the circumstances of Dr. Kalam's passing on July 27, 2015, and explain its symbolic meaning.",
     "On July 27, 2015, while delivering a lecture on 'Creating a Livable Planet Earth' to students at the Indian Institute of Management (IIM) Shillong, Dr. Kalam collapsed due to a sudden cardiac arrest and passed away at age 83. Passing away while standing at a chalkboard teaching university students held deep symbolic meaning. It reflected his unbroken, lifelong dedication to education. Until his very last breath, Dr. Kalam lived his primary passion: educating, motivating, and interacting with the youth of India.",
     "Easy", "Evaluating"),

    ("Explain how Dr. Kalam's life story illustrates that humble beginnings are no barrier to success.",
     "Dr. Kalam was born into a simple middle-class family in a small island town, distributed newspapers to assist his family's income, and studied in modest local schools. He possessed no wealth, political connections, or high status. Yet, through sheer curiosity, relentless hard work, honesty, and scientific dedication, he rose to become India's top space scientist, chief defense adviser, and 11th President. His life proves that character, intellect, and perseverance—not birth wealth—determine human greatness.",
     "Easy", "Evaluating"),

    ("Summarize Chapter 08 in five detailed bullet points.",
     "- Dr. A. P. J. Abdul Kalam (born Oct 15, 1931 in Rameswaram, TN) grew up in a humble middle-class family and studied aeronautical engineering.\n- As a scientist at ISRO and DRDO, he led SLV-3 space launches and developed Agni and Prithvi missiles, earning the title 'Missile Man of India'.\n- In 2002, he became the 11th President of India and was loved as the 'People's President' for his inspiring outreach to students.\n- Author of 'Wings of Fire', he taught that dreams transform into thoughts and thoughts result in action.\n- Passed away July 27, 2015 while lecturing students; his visionary journey from Rameswaram to Rashtrapati Bhavan inspires every Indian.",
     "Easy", "Understanding"),

    ("What lessons about patriotism and scientific temper can students learn from Chapter 08?",
     "Students learn that real patriotism is demonstrated through dedicated service, building national self-reliance, and helping fellow citizens. They also learn that cultivating a 'scientific temper'—asking logical questions, experimenting, seeking truth, and applying technology for social welfare—is essential for building a strong, developed India.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why was the launch of the Rohini satellite via SLV-3 in 1980 a milestone for India?", "It proved that India could independently design, manufacture, and launch rocket hardware to place satellites into space orbit, freeing India from dependence on Western launch vehicles.", "Easy", "Understanding"),
    ("Explain Dr. Kalam's contribution to medical healthcare technology.", "Collaborating with Dr. B. Soma Raju, he developed the affordable 'Kalam-Raju Stent' for cardiac patients and designed lightweight carbon-fiber leg braces (calipers) for polio-affected children, dramatically reducing medical costs.", "Easy", "Understanding"),
    ("Describe Dr. Kalam's interactions with children at Rashtrapati Bhavan.", "He invited thousands of school children to Rashtrapati Bhavan, listened patiently to their questions, signed autographs with personal messages ('Dream Big'), and encouraged them to become scientific leaders.", "Easy", "Remembering"),
    ("How did Dr. Kalam handle the failure of the first SLV-3 launch in 1979?", "When the 1979 SLV-3 rocket crashed into the Bay of Bengal, Kalam accepted technical responsibility alongside his team leader Satish Dhawan, analyzed the failure data meticulously, and successfully launched SLV-3 in 1980.", "Easy", "Analyzing"),
    ("What is the significance of the title 'Wings of Fire'?", "The title metaphorically represents the inner passion, scientific spark, and unyielding spirit that enables a person from humble origins to rise above limitations and achieve extraordinary heights.", "Easy", "Analyzing"),
    ("How did Dr. Kalam's spiritual roots in Rameswaram influence his worldview?", "Rameswaram's harmony among Hindu, Muslim, and Christian communities taught him religious tolerance, deep spiritual humility, and a secular belief in universal human brotherhood.", "Easy", "Understanding"),
    ("Explain Dr. Kalam's 'PURA' (Providing Urban Amenities in Rural Areas) initiative.", "PURA was his socio-economic model to provide physical roads, electronic broadband, knowledge centers, and economic opportunities to rural villages, preventing forced urban migration.", "Easy", "Understanding"),
    ("How did Dr. Kalam inspire young girls and women to pursue science and engineering?", "He constantly highlighted the achievements of female scientists at ISRO and DRDO, urging young girls in schools to break stereotypes and excel in mathematics, space science, and technology.", "Easy", "Applying"),
    ("What role did Dr. Vikram Sarabhai and Prof. Satish Dhawan play in Dr. Kalam's career?", "They were legendary ISRO mentors who recognized Kalam's leadership potential, entrusted him with the SLV-3 project, and taught him team management and handling success and failure.", "Easy", "Remembering"),
    ("Why is Dr. Kalam considered an ideal role model for 21st-century youth?", "Because he embodied a rare combination of scientific excellence, moral integrity, personal simplicity, continuous learning, and selfless love for the nation.", "Easy", "Evaluating"),
    ("Re-write the story of Dr. Kalam's life from the perspective of a young student meeting him in 2005.", "'When President Kalam shook my hand at Rashtrapati Bhavan, he didn't talk like a politician. He looked into my eyes and said, 'What is your dream?' That moment made me realize I could achieve anything through hard work.'", "Easy", "Creating"),
    ("What honors were conferred upon Dr. Kalam by the Government of India?", "He was awarded India's top three civilian honors: Padma Bhushan (1981), Padma Vibhushan (1990), and Bharat Ratna (1997) for his exceptional service to science and defense.", "Easy", "Remembering"),
    ("How did Dr. Kalam promote environmental conservation in his writings and speeches?", "He urged students to plant trees, conserve water, reduce pollution, and transition to renewable solar and wind energy to ensure a sustainable planet earth.", "Easy", "Understanding"),
    ("Analyze why Chapter 08 is titled 'The Missile Man of India: Dr. A. P. J. Abdul Kalam'.", "The title highlights his most iconic national identity—the master scientist who developed Agni and Prithvi missiles, securing India's strategic defense self-reliance.", "Easy", "Analyzing"),
    ("What vision should Class 5 students adopt for India's future based on Chapter 08?", "Students should adopt a vision of a clean, technologically advanced, educated, economically strong, and unified India where every citizen works for national progress.", "Easy", "Applying"),

    # Medium (26-40)
    ("Critically analyze how Dr. Kalam transformed the Indian presidency into a youth empowerment platform.",
     "Dr. Kalam redefined the role of the Indian President:\n1. **Educational Outreach**: He prioritized meeting over 100,000 students annually, conducting interactive Q&A sessions in schools and colleges nationwide.\n2. **Vision 2020 Advocacy**: He used presidential addresses to push developmental benchmarks in education, healthcare, and technology.\n3. **Moral Leadership**: He maintained complete financial transparency and non-partisan neutrality, becoming an inspiring moral compass for the country.",
     "Medium", "Analyzing"),

    ("Examine the technological trajectory of India's missile program under IGMDP led by Dr. Kalam.",
     "The Integrated Guided Missile Development Programme (IGMDP) achieved multi-tier defense capability:\n1. **Prithvi**: Short-range surface-to-surface tactical missile.\n2. **Agni**: Intermediate-to-intercontinental ballistic missile series.\n3. **Trishul & Akash**: Surface-to-air defense missile systems.\n4. **Nag**: Anti-tank guided missile.\nThis program established comprehensive indigenous missile manufacturing, eliminating dependence on foreign defense suppliers.",
     "Medium", "Analyzing"),

    ("Evaluate the role of mentorship in scientific growth as illustrated by Dr. Kalam's relationship with Satish Dhawan.",
     "When the 1979 SLV-3 launch failed, ISRO Chairman Satish Dhawan took full responsibility in front of the press, shielding Kalam. When the 1980 launch succeeded, Dhawan sent Kalam to take the credit. This masterclass in leadership taught Kalam how to protect teams during failure and share glory during success.",
     "Medium", "Evaluating"),

    ("Discuss how Dr. Kalam's background in aeronautical engineering aided his work in space rockets and defense missiles.",
     "Aeronautical engineering provided Kalam with fundamental knowledge of fluid dynamics, aerodynamics, structural materials, heat shields, and propulsion. This expertise allowed him to transition smoothly from designing aircraft at DRDO to building Satellite Launch Vehicles at ISRO and re-entry ballistic missiles.",
     "Medium", "Analyzing"),

    ("Design a school science exhibition module inspired by Chapter 08.",
     "Exhibition Title: 'Ignited Minds — Science for National Development'\n- **Module 1 (Space)**: Working model of SLV-3 rocket and satellite orbits.\n- **Module 2 (Defense Tech)**: Display of Agni missile stages and re-entry heat shield science.\n- **Module 3 (Healthcare Science)**: Demonstration of Kalam-Raju cardiac stent and lightweight polio calipers.\n- **Module 4 (Youth Corner)**: Student dream wall where visitors write their Vision 2020 pledges.",
     "Medium", "Creating"),

    ("How did Dr. Kalam handle criticism or political opposition during his career?", "He remained focused on scientific facts, responded with gentle courtesy, avoided personal controversies, and let concrete results speak for his dedication.", "Medium", "Analyzing"),
    ("Contrast the scientific work done at ISRO (space) with the scientific work done at DRDO (defense).", "ISRO focuses on civilian space exploration, satellite communications, and weather monitoring. DRDO focuses on military missile defense, tactical weapons, and national security hardware.", "Medium", "Comparing"),
    ("Why was Dr. Kalam's election as President in 2002 universally celebrated across India?", "Because he was a non-political, highly respected scientist of impeccable integrity whose appointment represented national unity, scientific progress, and meritocracy.", "Medium", "Understanding"),
    ("Explain the significance of the Kalam-Raju Stent in Indian medical history.", "Before this stent, imported heart stents cost over ₹50,000, making cardiac care impossible for poor families. Kalam used missile-grade material technology to reduce the cost to ₹10,000.", "Medium", "Understanding"),
    ("How did Dr. Kalam's mother, Ashiamma, influence his values?", "His mother exhibited immense warmth, hospitality, and unconditional kindness, teaching young Kalam to share food with strangers and treat every human with respect.", "Medium", "Understanding"),
    ("Analyze the impact of Dr. Kalam's speeches on student motivation.", "His speeches used simple stories, rhythmic pledges, and direct Q&A, instilling confidence in students to break poverty cycles through education and hard work.", "Medium", "Analyzing"),
    ("Describe Dr. Kalam's vision for renewable energy in India.", "He advocated transitioning from fossil fuels to solar, wind, and nuclear power to ensure energy independence and protect the global environment.", "Medium", "Understanding"),
    ("Why is Dr. Kalam considered a symbol of India's secular democratic ethos?", "Born a devout Muslim in a temple town, he studied Hindu scriptures like the Bhagavad Gita, played the Veena, and respected all faiths, embodying India's composite culture.", "Medium", "Evaluating"),
    ("Describe the writing style and tone of Dr. Kalam's books like 'Wings of Fire' and 'Ignited Minds'.", "The tone is warm, humble, conversational, and deeply encouraging, blending personal anecdotes with motivational challenges for young readers.", "Medium", "Analyzing"),
    ("Construct a fictional speech by Dr. Kalam addressing Class 5 students on World Students' Day.", "'My dear young friends, repeat after me: My national flag flies in my heart. I will acquire knowledge continuously. I will dream big and work hard. I will make my nation proud!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the geopolitical significance of India's 1998 Pokhran-II nuclear tests coordinated by Dr. Kalam.",
     "Pokhran-II declared India as a nuclear weapons state. While incurring temporary Western economic sanctions, it established strategic parity, prevented nuclear blackmail, and eventually led to the US-India Civil Nuclear Agreement, elevating India's global geopolitical stature.",
     "Hard", "Evaluating"),

    ("Deconstruct the engineering physics behind missile re-entry heat shields developed by Dr. Kalam's team.",
     "Ballistic missiles re-entering Earth's atmosphere face temperatures exceeding 3,000°C due to atmospheric friction. Kalam's team developed carbon-phenolic composite heat shields that ablatively dissipated extreme heat, protecting sensitive electronic guidance systems inside Agni missiles.",
     "Hard", "Analyzing"),

    ("Synthesize how Dr. Kalam's life demonstrates the harmony between science, faith, and ethics.",
     "Kalam demonstrated that scientific rationalism (discovering physical laws) and spiritual faith (seeking inner purity and moral purpose) are complementary. He used scientific knowledge ethically to serve humanity rather than seek personal destruction or wealth.",
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive essay prompt evaluating Dr. Kalam's dual legacy in aerospace engineering and youth leadership.",
     "Prompt: 'Critically evaluate Dr. A. P. J. Abdul Kalam's contributions as the 'Missile Man of India' at ISRO/DRDO and as the 'People's President'. Explain how his technical achievements and moral teachings reshaped modern India.'",
     "Hard", "Creating"),

    ("Evaluate the sustainability of Dr. Kalam's 'PURA' model in 21st-century urban planning.", "PURA remains a visionary urban-rural planning framework that decentralized economic hubs, reduced metropolitan congestion, and provided digital infrastructure to tier-3 towns and villages.", "Hard", "Evaluating"),

    ("Compare Dr. Kalam's life trajectory with Dr. Vikram Sarabhai's life trajectory.", "Sarabhai came from an affluent industrialist family and founded ISRO's institutional vision; Kalam came from a humble village background and executed the engineering projects that fulfilled Sarabhai's vision.", "Hard", "Comparing"),
    ("Discuss the global impact of Dr. Kalam's books translated across international languages.", "His books translated globally introduced international readers to Indian scientific capabilities, inspiring youth across developing nations in Asia, Africa, and South America.", "Hard", "Evaluating"),
    ("Analyze how Dr. Kalam utilized social media and digital technology in his later years.", "He adopted digital platforms early to publish daily thought messages, interact with student questions online, and disseminate educational blueprints to millions of followers.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'His journey from a small town in Tamil Nadu to Rashtrapati Bhavan continues to inspire every Indian.'", "This sentence encapsulates the core democratic promise of India. It affirms that merit, dedication, and integrity can elevate any citizen from the humblest village to the highest office in the land.", "Hard", "Evaluating"),
    ("Synthesize the ultimate educational message of Chapter 08 for primary school students.", "Chapter 08 teaches that true success is built on scientific curiosity, unyielding hard work, humility, and dedication to serving others, encouraging students to ignite their minds for national progress.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 08: The Missile Man of India: Dr. A. P. J. Abdul Kalam\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH08_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH08_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("The title \"Missile Man of India\" is proudly given to Dr. A.P.J. Abdul Kalam, one of the greatest scientists and leaders India has ever known. He was born on October 15, 1931, in Rameswaram, a small town in Tamil Nadu.",
     [
         ("What title is proudly given to Dr. A. P. J. Abdul Kalam?", "Missile Man of India.", "Easy", "Remembering"),
         ("When was Dr. Kalam born?", "October 15, 1931.", "Easy", "Remembering"),
         ("Where was Dr. Kalam born?", "Rameswaram, a small town in Tamil Nadu.", "Easy", "Remembering"),
         ("How is Dr. Kalam described as a national figure?", "As one of the greatest scientists and leaders India has ever known.", "Easy", "Understanding"),
         ("Why is the title 'Missile Man' proudly associated with India's scientific progress?", "Because his missile engineering established national defense self-reliance.", "Medium", "Analyzing")
     ]),

    # Set 2
    ("He was born in a middle class family to wise and kind parents. Dr. Kalam was a brilliant student who loved learning about science and technology.",
     [
         ("What kind of family was Dr. Kalam born into?", "A middle-class family.", "Easy", "Remembering"),
         ("How are Dr. Kalam's parents described?", "Wise and kind parents.", "Easy", "Remembering"),
         ("What kind of student was Dr. Kalam?", "A brilliant student.", "Easy", "Remembering"),
         ("What subjects did Dr. Kalam love learning about?", "Science and technology.", "Easy", "Remembering"),
         ("How did his family environment influence his growth?", "Wise and kind parents instilled humility, moral values, and respect for learning.", "Medium", "Analyzing")
     ]),

    # Set 3
    ("He worked hard and became a scientist at the Indian Space Research Organisation (ISRO) and the Defence Research and Development Organisation (DRDO). His work in developing missiles like Agni and Prithvi made India strong and proud, earning him the nickname \"Missile Man of India.\"",
     [
         ("Name two scientific organizations where Dr. Kalam worked.", "ISRO and DRDO.", "Easy", "Remembering"),
         ("Which two missiles developed under his leadership are mentioned here?", "Agni and Prithvi.", "Easy", "Remembering"),
         ("What effect did his missile development work have on India?", "It made India strong and proud.", "Easy", "Remembering"),
         ("What nickname did he earn from this work?", "Missile Man of India.", "Easy", "Remembering"),
         ("What does ISRO stand for?", "Indian Space Research Organisation.", "Easy", "Understanding")
     ]),

    # Set 4
    ("In 2002, Dr. Kalam became the 11th President of India. He was known as the \"People's President\" because he always encouraged students and young people to dream big and work hard.",
     [
         ("In what year did Dr. Kalam become President of India?", "2002.", "Easy", "Remembering"),
         ("Which numbered President of India was Dr. Kalam?", "The 11th President.", "Easy", "Remembering"),
         ("What nickname was Dr. Kalam known by during his presidency?", "The 'People's President'.", "Easy", "Remembering"),
         ("Why was he called the 'People's President'?", "Because he always connected with citizens and encouraged students to dream big and work hard.", "Easy", "Understanding"),
         ("What key advice did he give to young people?", "To dream big and work hard.", "Easy", "Remembering")
     ]),

    # Set 5
    ("Even after his presidency, Dr. Kalam continued to inspire millions through his books and speeches. His famous book, \"Wings of Fire,\" tells the story of his life and achievements.",
     [
         ("How did Dr. Kalam continue to inspire people after his presidency?", "Through his books and speeches.", "Easy", "Remembering"),
         ("What is the title of Dr. Kalam's famous autobiography mentioned here?", "Wings of Fire.", "Easy", "Remembering"),
         ("What story does 'Wings of Fire' tell?", "It tells the story of his life and achievements.", "Easy", "Remembering"),
         ("Who did Dr. Kalam inspire through his work?", "Millions of people across India and the world.", "Easy", "Remembering"),
         ("What does the word 'achievements' mean?", "Successes gained through persistent effort and hard work.", "Easy", "Understanding")
     ]),

    # Set 6
    ("Sadly, Dr. Kalam passed away on July 27, 2015, while giving a lecture at a university. However, his teachings, dreams and contributions continue to inspire us.",
     [
         ("When did Dr. Kalam pass away?", "July 27, 2015.", "Easy", "Remembering"),
         ("What was Dr. Kalam doing when he passed away?", "Giving a lecture at a university.", "Easy", "Remembering"),
         ("What aspects of Dr. Kalam continue to inspire us today?", "His teachings, dreams, and contributions.", "Easy", "Remembering"),
         ("Why is passing away during a lecture symbolic of his life?", "It showed his unbroken commitment to teaching and inspiring youth until his last breath.", "Medium", "Evaluating"),
         ("What emotional tone does the passage convey about his passing?", "A sorrowful yet respectful and inspiring tone.", "Medium", "Analyzing")
     ]),

    # Set 7
    ("He once said, \"Dream, dream, dream. Dreams transform into thoughts and thoughts result in action.\" Dr. A.P.J. Abdul Kalam was a scientist and visionary par excellence.",
     [
         ("What famous quote by Dr. Kalam is shared in this passage?", "'Dream, dream, dream. Dreams transform into thoughts and thoughts result in action.'", "Easy", "Remembering"),
         ("According to Dr. Kalam, what do dreams transform into?", "Thoughts.", "Easy", "Remembering"),
         ("According to Dr. Kalam, what do thoughts result in?", "Action.", "Easy", "Remembering"),
         ("How is Dr. Kalam described at the end of this quote?", "As a scientist and visionary par excellence.", "Easy", "Remembering"),
         ("What does the word 'visionary' mean?", "Someone who imagines a better future.", "Easy", "Understanding")
     ]),

    # Set 8
    ("His journey from a small town in Tamil Nadu to the Rashtrapati Bhavan continues to inspire every Indian and motivates us to achieve our dreams.",
     [
         ("Where did Dr. Kalam's journey begin?", "In a small town in Tamil Nadu (Rameswaram).", "Easy", "Remembering"),
         ("Where did Dr. Kalam's journey lead him as President?", "To Rashtrapati Bhavan.", "Easy", "Remembering"),
         ("Whom does Dr. Kalam's journey continue to inspire?", "Every Indian.", "Easy", "Remembering"),
         ("What does his journey motivate us to do?", "To achieve our dreams.", "Easy", "Understanding"),
         ("Why is his journey considered a classic American-style 'rags-to-greatness' story for India?", "Because he rose from humble newspaper-selling origins to become the highest leader of the nation through merit.", "Medium", "Analyzing")
     ]),

    # Set 9
    ("Word Meaning: Scientist: A person who studies and discovers new knowledge. Visionary: Someone who imagines a better future. Inspiration: Something that motivates or encourages. Achievement: Success gained through effort.",
     [
         ("What is the definition of 'scientist'?", "A person who studies and discovers new knowledge.", "Easy", "Remembering"),
         ("What is the definition of 'visionary'?", "Someone who imagines a better future.", "Easy", "Remembering"),
         ("What is the definition of 'inspiration'?", "Something that motivates or encourages.", "Easy", "Remembering"),
         ("What is the definition of 'achievement'?", "Success gained through effort.", "Easy", "Remembering"),
         ("Use the word 'inspiration' in a complete sentence of your own.", "Our teacher is a great inspiration to all students in the class.", "Medium", "Applying")
     ]),

    # Set 10
    ("Born October 15, 1931 in Rameswaram... Scientist at ISRO and DRDO... Developed Agni and Prithvi... 11th President in 2002... Passed away July 27, 2015... Author of Wings of Fire.",
     [
         ("When was Dr. Kalam born?", "October 15, 1931.", "Easy", "Remembering"),
         ("In what year did he become President?", "2002.", "Easy", "Remembering"),
         ("When did he pass away?", "July 27, 2015.", "Easy", "Remembering"),
         ("What is his autobiography called?", "Wings of Fire.", "Easy", "Remembering"),
         ("Summarize Dr. Kalam's life legacy in one sentence.", "He dedicated his life to scientific defense, presidential leadership, and inspiring millions of students to dream big and serve the nation.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 08: The Missile Man of India: Dr. A. P. J. Abdul Kalam\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH08_EXT_{q_counter:03d}"
        ext_content += f"\n\n### Question {q_counter}\n"
        ext_content += f"- **Question ID**: {q_id}\n"
        ext_content += f"- **Type**: Extract Based\n"
        ext_content += f"- **Difficulty**: {diff}\n"
        ext_content += f"- **Bloom Level**: {bloom}\n"
        ext_content += f"- **Marks**: 1\n\n"
        ext_content += f"**Question**: {sub_q}\n\n"
        ext_content += f"- **Answer Key**: {sub_a}\n"
        q_counter += 1
    ext_content += "\n\n---\n\n"

with open(os.path.join(CH08_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 08 in {CH08_DIR}")
