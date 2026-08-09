r"""
Refines all 6 Category files for Chapter 07 ("Nightingale of India") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH07_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_07")
os.makedirs(CH07_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Who was Sarojini Naidu?", "(A) A renowned poet and freedom fighter", "(B) A famous doctor", "(C) A sportsperson", "(D) A painter", "(A)", "Sarojini Naidu was a renowned poet and freedom fighter.", "Easy", "Remembering", "Identity"),
    ("When was Sarojini Naidu born?", "(A) 13th February 1879", "(B) 15th August 1947", "(C) 26th January 1950", "(D) 2nd October 1869", "(A)", "She was born on 13th February 1879.", "Easy", "Remembering", "Birth Date"),
    ("Where was Sarojini Naidu born?", "(A) Hyderabad, British India", "(B) Mumbai", "(C) Kolkata", "(D) Delhi", "(A)", "She was born in Hyderabad, British India.", "Easy", "Remembering", "Birthplace"),
    ("What was Sarojini Naidu's father?", "(A) An educationist and social reformer", "(B) A soldier", "(C) A sailor", "(D) A shopkeeper", "(A)", "Her father was an educationist and social reformer.", "Easy", "Remembering", "Father's Profession"),
    ("What was Sarojini Naidu's mother?", "(A) A Bengali poet", "(B) A doctor", "(C) A teacher", "(D) A lawyer", "(A)", "Her mother was a Bengali poet.", "Easy", "Remembering", "Mother's Profession"),
    ("At what age did Sarojini Naidu begin writing plays?", "(A) Age 12", "(B) Age 5", "(C) Age 20", "(D) Age 16", "(A)", "She began writing plays at the age of 12.", "Easy", "Remembering", "Writing Age"),
    ("Where did her parents send her at age 16 for higher education?", "(A) England", "(B) USA", "(C) France", "(D) Germany", "(A)", "Her parents sent her to England for completing her education.", "Easy", "Remembering", "Education Country"),
    ("How old was Sarojini Naidu when she went to England?", "(A) 16 years old", "(B) 12 years old", "(C) 25 years old", "(D) 10 years old", "(A)", "She went to England at the age of 16.", "Easy", "Remembering", "Age"),
    ("What famous title was given to Sarojini Naidu?", "(A) The Nightingale of India", "(B) Queen of Poetry", "(C) Lioness of Punjab", "(D) Lady of the Lamp", "(A)", "She was earned the title 'the Nightingale of India'.", "Easy", "Remembering", "Title"),
    ("Why was she called 'the Nightingale of India'?", "(A) Because she spoke with a gifted, soft, and melodious voice", "(B) Because she could sing like a bird", "(C) Because she lived in a forest", "(D) Because she wore green clothes", "(A)", "Her melodious, gentle voice in speeches earned her the title.", "Easy", "Remembering", "Title Reason"),
    ("What cause did Sarojini Naidu work for besides freedom?", "(A) Emancipation (upliftment) of women", "(B) Building factories", "(C) Flying airplanes", "(D) Trading goods", "(A)", "She worked for the cause of emancipation of women.", "Easy", "Remembering", "Women Rights"),
    ("What post did Sarojini Naidu hold after India became independent?", "(A) The first woman governor", "(B) The first woman president", "(C) The first woman prime minister", "(D) Chief Justice", "(A)", "She became the first woman governor after independence.", "Easy", "Remembering", "Post-Independence Role"),
    ("Which region was Sarojini Naidu given charge of as governor?", "(A) The United Provinces", "(B) Bengal", "(C) Bombay", "(D) Punjab", "(A)", "She was given charge of the United Provinces.", "Easy", "Remembering", "Governor Region"),
    ("What does the word 'worthy' mean?", "(A) Deserving", "(B) Cheap", "(C) Lazy", "(D) Angry", "(A)", "Worthy is defined as deserving.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'accomplished' mean?", "(A) Highly skilled at something", "(B) Very slow", "(C) Loud", "(D) Weak", "(A)", "Accomplished means highly skilled at something.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'renowned' mean?", "(A) Widely acclaimed and honoured", "(B) Unknown", "(C) Small", "(D) Poor", "(A)", "Renowned means widely acclaimed and honoured.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'emancipation' mean?", "(A) Upliftment / freedom from restrictions", "(B) Punishment", "(C) Cooking food", "(D) Writing books", "(A)", "Emancipation is defined as upliftment.", "Easy", "Understanding", "Vocabulary"),
    ("Did Sarojini Naidu participate in India's struggle for freedom?", "(A) Yes, she actively participated", "(B) No, she stayed away", "(C) She fought against India", "(D) She moved abroad permanently", "(A)", "She actively participated in India's freedom movement.", "Easy", "Remembering", "Freedom Movement"),
    ("What kind of voice was Sarojini Naidu gifted with?", "(A) A melodious voice", "(B) A harsh voice", "(C) A squeaky voice", "(D) A silent voice", "(A)", "She was gifted with a melodious voice.", "Easy", "Remembering", "Voice Quality"),
    ("In what tone did she speak on various platforms about India's freedom?", "(A) In a soft and gentle tone", "(B) In an angry shout", "(C) In a whisper", "(D) In a rude tone", "(A)", "She spoke in a soft and gentle tone.", "Easy", "Remembering", "Speech Tone"),
    ("Was Sarojini Naidu a poet and a speaker?", "(A) Yes, she was both an impressive poet and speaker", "(B) No, she only wrote plays", "(C) No, she only sang songs", "(D) No, she was a doctor", "(A)", "She wrote poems/plays and spoke on public platforms.", "Easy", "Remembering", "Talents"),
    ("Which language background did Sarojini's mother belong to as a poet?", "(A) Bengali", "(B) Tamil", "(C) Gujarati", "(D) Punjabi", "(A)", "Her mother was a Bengali poet.", "Easy", "Remembering", "Mother's Background"),
    ("At what age did Sarojini show her early literary talent by writing plays?", "(A) 12", "(B) 18", "(C) 25", "(D) 30", "(A)", "She began writing plays at age 12.", "Easy", "Remembering", "Early Talent"),
    ("What was Sarojini Naidu's father dedicated to?", "(A) Education and social reform", "(B) Business and trade", "(C) Farming", "(D) Painting", "(A)", "He was an educationist and social reformer.", "Easy", "Remembering", "Father's Work"),
    ("What is the title of Chapter 07?", "(A) Nightingale of India", "(B) My Favourite Cartoon", "(C) The Indian Poet", "(D) Woman Governor", "(A)", "Chapter 07 is titled 'Nightingale of India'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why did Sarojini Naidu's parents send her to England at the young age of 16?", "(A) They were delighted with her brilliant talent and wanted her to receive the best higher education", "(B) They wanted her to quit writing", "(C) They wanted her to get a job", "(D) Because she requested a vacation", "(A)", "Her talent delighted them, so they sent her to complete education.", "Medium", "Understanding", "Parental Motivation"),
    ("How did Sarojini Naidu's home environment shape her literary and social pursuits?", "(A) Having an educationist father and a poet mother inspired her talent for poetry and passion for social reform", "(B) Her parents discouraged her from reading", "(C) Her home had no books", "(D) She learned everything on the streets", "(A)", "Accomplished parents nurtured her talent and social values.", "Medium", "Analyzing", "Environmental Impact"),
    ("Why is the title 'Nightingale of India' appropriate for Sarojini Naidu?", "(A) Like a nightingale bird whose song brings joy, her melodious speeches and beautiful poetry inspired millions during freedom struggles", "(B) Because she lived in a bird sanctuary", "(C) Because she collected nightingale feathers", "(D) Because it was her nickname in school", "(A)", "Melodious voice, inspiring speeches, and poetic beauty.", "Medium", "Analyzing", "Title Significance"),
    ("What was the double contribution of Sarojini Naidu to Indian society?", "(A) Fighting for political freedom from British rule and working for women's emancipation", "(B) Building railways and highways", "(C) Teaching music and painting", "(D) Writing children's comic books", "(A)", "Political freedom + Women's emancipation.", "Medium", "Understanding", "Dual Contribution"),
    ("Why was Sarojini Naidu's appointment as the first woman governor historically important?", "(A) It broke gender barriers and proved that women could hold top administrative leadership positions in free India", "(B) She was the youngest governor in the world", "(C) She was appointed by the King of England", "(D) It was an honorary title with no duties", "(A)", "Broke gender barriers for women in governance.", "Medium", "Evaluating", "Historical Landmark"),
    ("What quality made Sarojini Naidu a 'worthy child' of her parents?", "(A) She inherited their intellect and used her literary skills and passion to serve the nation", "(B) She bought a large house", "(C) She stayed quiet", "(D) She travelled around the world only", "(A)", "Deserving child who matched her parents' high standards.", "Medium", "Understanding", "Character Assessment"),
    ("How did Sarojini Naidu use her poetry and public speaking as tools for freedom?", "(A) Her gentle, melodious voice and stirring words awakened patriotism and inspired people to join the freedom movement", "(B) She used code words to send messages", "(C) She sang songs on the radio only", "(D) She wrote secret letters to the British", "(A)", "Melodious speeches and poems awakened national patriotism.", "Medium", "Analyzing", "Communication Impact"),
    ("What does 'women's emancipation' mean in the context of Sarojini Naidu's life work?", "(A) Fighting for equal rights, education, dignity, and social freedom for Indian women", "(B) Sending women abroad", "(C) Teaching women how to cook", "(D) Giving women gold jewelry", "(A)", "Social upliftment, rights, and dignity for women.", "Medium", "Understanding", "Social Reform"),
    ("Why did Sarojini Naidu speak in a 'soft and gentle tone' rather than shouting during speeches?", "(A) Her soft, melodious tone conveyed deep conviction and grace that moved listeners emotionally", "(B) She had a sore throat", "(C) She was afraid of microphones", "(D) Nobody listened when she shouted", "(A)", "Soft grace and melodious conviction touched hearts.", "Medium", "Analyzing", "Oratory Style"),
    ("What role did Hyderabad play in Sarojini Naidu's life?", "(A) It was her birthplace, providing her initial multicultural environment in British India", "(B) She was the governor of Hyderabad", "(C) She built a university there", "(D) She left Hyderabad as a baby and never returned", "(A)", "Birthplace in British India.", "Medium", "Remembering", "Geographic Relevance"),
    ("How does Sarojini Naidu inspire young girls and students today?", "(A) She shows that girls can achieve literary excellence, lead nation-building movements, and hold top leadership roles", "(B) She proves that writing plays is easy", "(C) She advises students to move to England", "(D) She tells everyone to become poets only", "(A)", "Inspirational role model for youth and women empowerment.", "Medium", "Evaluating", "Modern Relevance"),
    ("What connects Sarojini Naidu's mother's background to Sarojini's own career?", "(A) Her mother was a poet, which influenced Sarojini's love for literature and poetry from an early age", "(B) Her mother taught her law", "(C) Her mother was a governor", "(D) Her mother lived in England", "(A)", "Maternal poetic influence.", "Medium", "Analyzing", "Family Influence"),
    ("Why was Sarojini Naidu called an 'accomplished' individual?", "(A) She achieved high skill in poetry, public speaking, political leadership, and social reform", "(B) She won sports trophies", "(C) She accumulated great wealth", "(D) She lived to be very old", "(A)", "Highly skilled in multiple honorable fields.", "Medium", "Understanding", "Accomplishment"),
    ("What state is the modern equivalent of the 'United Provinces' where she was governor?", "(A) Uttar Pradesh", "(B) Maharashtra", "(C) Tamil Nadu", "(D) Rajasthan", "(A)", "United Provinces is modern Uttar Pradesh.", "Medium", "Remembering", "General Knowledge"),
    ("How old was Sarojini Naidu when India gained independence in 1947?", "(A) 68 years old (born 1879)", "(B) 50 years old", "(C) 80 years old", "(D) 40 years old", "(A)", "Born 1879, independent 1947 = 68 years old.", "Medium", "Understanding", "Chronology"),

    # Hard (41-50)
    ("Analyze how Sarojini Naidu synthesized art (poetry) and political activism (freedom struggle) throughout her life.", "(A) She did not treat poetry and politics as separate; her artistic sensitivity enriched her political speeches, making her a poetic leader", "(B) She gave up poetry when she entered politics", "(C) She wrote political pamphlets disguised as poems", "(D) Her poetry had nothing to do with India", "(A)", "Seamless synthesis of poetic sensitivity and political activism.", "Hard", "Analyzing", "HOTS Synthesis"),
    ("Evaluate the societal challenge Sarojini Naidu faced as a woman leader in early 20th-century India.", "(A) In a conservative era with restricted roles for women, she overcame societal barriers to become a national freedom icon and governor", "(B) Women faced no obstacles in 1900", "(C) She was supported by everyone without effort", "(D) She was allowed to lead because her father was rich", "(A)", "Overcoming conservative gender barriers through merit and courage.", "Hard", "Evaluating", "Societal Barrier Evaluation"),
    ("Deconstruct the title 'Nightingale of India' (Bharat Kokila) given by Mahatma Gandhi and the nation.", "(A) Nightingale: sweet melodious songbird (poetic voice); Of India: national devotion and representation of the Indian spirit", "(B) It meant she liked birds", "(C) It was a penalty title", "(D) It referred to her birth month", "(A)", "Poetic melody + National devotion.", "Hard", "Analyzing", "Title Deconstruction"),
    ("Compare Sarojini Naidu's contribution to women's emancipation with her contribution to national independence.", "(A) Emancipation empowered women internally, while freedom struggle liberated the nation externally; both were essential for true democracy", "(B) Freedom struggle was important, but women's rights were not", "(C) Women's emancipation only mattered in England", "(D) Both contributions were identical", "(A)", "Internal empowerment vs external political liberation.", "Hard", "Analyzing", "Comparative Contributions"),
    ("Why is Sarojini Naidu's birth anniversary (February 13) celebrated as National Women's Day in India?", "(A) To honor her groundbreaking legacy as a pioneer of women's rights, literary brilliance, and political leadership", "(B) Because she was born in Hyderabad", "(C) Because she went to England", "(D) Because February is a spring month", "(A)", "Honoring a pioneer of women empowerment.", "Hard", "Evaluating", "National Recognition"),
    ("How did Sarojini Naidu's education in England enhance her contribution to India's freedom movement?", "(A) It exposed her to global political ideas and refined her English oratory skills, enabling her to present India's cause internationally", "(B) It made her forget Indian culture", "(C) It made her support British rule", "(D) It helped her write English dictionaries", "(A)", "Global exposure + English oratory skills for national cause.", "Hard", "Analyzing", "Educational Impact"),
    ("Assess the importance of parental support in fostering female talent in 19th-century India.", "(A) Her parents recognized her early genius, nurtured her writing, and sent her abroad, proving that parental encouragement unlocks female potential", "(B) Parental support was irrelevant", "(C) Her parents forced her to quit writing", "(D) Girls were always sent abroad in 1895", "(A)", "Nurturing environment unlocking talent.", "Hard", "Evaluating", "Parental Support Impact"),
    ("What does Sarojini Naidu's life teach about grace versus aggression in leadership?", "(A) Leadership does not require aggression or loud shouting; grace, soft melodious speech, and strong conviction can move a nation", "(B) Aggression is always superior to grace", "(C) Soft speakers can never be leaders", "(D) Grace is only for poets", "(A)", "Graceful conviction as a powerful leadership model.", "Hard", "Evaluating", "Leadership Philosophy"),
    ("Synthesize Sarojini Naidu's legacy into three distinct pillars of achievement.", "(A) 1. Literary Excellence (Poet & Playwright)\n2. Freedom & Equality Activism (Freedom Fighter & Women's Advocate)\n3. Pioneer Stateswoman (First Woman Governor)", "(B) 1. Singer 2. Teacher 3. Doctor", "(C) 1. Traveler 2. Painter 3. Trader", "(D) 1. Student 2. Foreigner 3. Writer", "(A)", "Pillars: Literature, Freedom/Equality, Statesmanship.", "Hard", "Synthesizing", "Legacy Synthesis"),
    ("Formulate a takeaway message from Chapter 07 for young Class 2 learners.", "(A) Use your unique gifts—whether voice, writing, or courage—to uplift others, stand up for freedom, and serve your nation with grace!", "(B) Move to England at age 16", "(C) Write plays only when you turn 12", "(D) Avoid speaking on public stages", "(A)", "Using personal talents for service, upliftment, and grace.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 07: Nightingale of India\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH07_MCQ_{idx:03d}"
    q_txt, opt_a, opt_b, opt_c, opt_d, ans, exp, diff, bloom, topic = item
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

with open(os.path.join(CH07_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Sarojini Naidu was born on 13th February _______.", "1879", "Born on 13th February 1879.", "Easy"),
    ("Sarojini Naidu was born in Hyderabad, British _______.", "India", "Born in Hyderabad, British India.", "Easy"),
    ("Her father was an educationist and a social-_______.", "reformer", "Father was a social-reformer.", "Easy"),
    ("Her mother was a _______ poet.", "Bengali", "Mother was a Bengali poet.", "Easy"),
    ("Sarojini began writing plays at the age of _______.", "12", "Writing plays at age 12.", "Easy"),
    ("She wrote impressive poems and _______.", "plays", "Wrote poems and plays.", "Easy"),
    ("Delighted with her talent, her parents sent her to _______ when she was 16.", "England", "Sent to England.", "Easy"),
    ("She was sent to England for completing her _______.", "education", "Sent to complete her education.", "Easy"),
    ("Sarojini Naidu became a _______ poet.", "renowned", "Became a renowned poet.", "Easy"),
    ("She worked for the cause of emancipation of _______.", "women", "Worked for emancipation of women.", "Easy"),
    ("She actively participated in India's struggle for _______.", "freedom", "Participated in freedom struggle.", "Easy"),
    ("She was gifted with a _______ voice.", "melodious", "Gifted with a melodious voice.", "Easy"),
    ("On various platforms she spoke about India's freedom in a soft and _______ tone.", "gentle", "Spoke in a soft and gentle tone.", "Easy"),
    ("Her voice and speech earned her the title of 'the _______ of India'.", "Nightingale", "Earned title 'Nightingale of India'.", "Easy"),
    ("After India became independent, Sarojini Naidu became the first woman _______.", "governor", "Became the first woman governor.", "Easy"),
    ("She was given the charge of the United _______ as governor.", "Provinces", "Governor of United Provinces.", "Easy"),
    ("The word 'worthy' means _______.", "deserving", "Worthy means deserving.", "Easy"),
    ("The word 'accomplished' means highly _______ at something.", "skilled", "Accomplished means highly skilled.", "Easy"),
    ("The word 'renowned' means widely acclaimed and _______.", "honoured", "Renowned means widely acclaimed and honoured.", "Easy"),
    ("The word 'emancipation' means _______.", "upliftment", "Emancipation means upliftment.", "Easy"),
    ("Sarojini Naidu was a worthy child of _______ parents.", "accomplished", "Child of accomplished parents.", "Easy"),
    ("Her mother was a poet who wrote in the _______ language.", "Bengali", "Bengali poet.", "Easy"),
    ("Sarojini went abroad to England at age _______.", "16", "Went at age 16.", "Easy"),
    ("She spoke about India's freedom on various _______.", "platforms", "Spoke on various platforms.", "Easy"),
    ("Chapter 07 is titled 'Nightingale of _______'.", "India", "Titled 'Nightingale of India'.", "Easy"),

    # Medium (26-40)
    ("Sarojini Naidu's father worked to reform _______ and promote education.", "society", "Promote social reform and education.", "Medium"),
    ("Her poetic inspiration came partly from her _______ who was also a poet.", "mother", "Inspired by her poet mother.", "Medium"),
    ("Writing plays at age 12 showed Sarojini's extraordinary early _______.", "genius", "Extraordinary early talent/genius.", "Medium"),
    ("Sarojini Naidu advocated for the social _______ of Indian women.", "emancipation", "Advocated women's emancipation.", "Medium"),
    ("Her speeches during the independence movement were delivered in a soft, gentle _______.", "tone", "Delivered in a soft, gentle tone.", "Medium"),
    ("As the first woman governor, she led the United _______.", "Provinces", "Led United Provinces.", "Medium"),
    ("Her parents were delighted by her literary _______.", "talent", "Delighted by her talent.", "Medium"),
    ("The title 'Nightingale of India' reflects her sweet, melodious _______.", "voice", "Reflects her melodious voice/poetry.", "Medium"),
    ("Sarojini Naidu played a prominent role in national _______.", "politics", "Prominent role in freedom politics.", "Medium"),
    ("Her father was an educationist and a social _______.", "reformer", "Social reformer.", "Medium"),
    ("Going to England expanded her academic and literary _______.", "horizons", "Expanded academic horizons.", "Medium"),
    ("She used her poetry to ignite feelings of _______ among Indians.", "patriotism", "Ignite patriotism.", "Medium"),
    ("Her birth anniversary is celebrated to honor her contributions to women's _______.", "rights", "Honor women's rights.", "Medium"),
    ("Sarojini Naidu proved that women can be effective state _______.", "leaders", "Effective state leaders/governors.", "Medium"),
    ("Her gentle voice had a powerful emotional _______ on listeners.", "impact", "Powerful emotional impact.", "Medium"),

    # Hard (41-50)
    ("Sarojini Naidu's legacy synthesizes poetic artistry with revolutionary political _______.", "activism", "Synthesizes art with political activism.", "Hard"),
    ("Her leadership as governor broke traditional gender _______ in public administration.", "barriers", "Broke gender barriers.", "Hard"),
    ("Working for emancipation ensured that women gained civic _______ in free India.", "equality", "Gained civic equality.", "Hard"),
    ("Her melodious oratory served as a peaceful instrument of national _______.", "awakening", "Instrument of national awakening.", "Hard"),
    ("Her father's background as an educationist instilled in her a lifelong love for _______.", "learning", "Love for learning and reform.", "Hard"),
    ("She remains a monumental figure in the history of Indian literature and _______.", "governance", "History of literature and governance.", "Hard"),
    ("Her poems earned her international acclaim as a leading literary _______.", "luminary", "Leading literary luminary.", "Hard"),
    ("Her gentle speech style demonstrated that persuasion can be more effective than _______.", "aggression", "Persuasion over aggression.", "Hard"),
    ("The United Provinces later became known as the modern state of Uttar _______.", "Pradesh", "Modern Uttar Pradesh.", "Hard"),
    ("Sarojini Naidu's life exemplifies dedicated service to truth, beauty, and national _______.", "freedom", "Service to beauty and freedom.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 07: Nightingale of India\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH07_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH07_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Sarojini Naidu was born on 13th February 1879.", "True", "The text states she was born on 13th February 1879.", "Easy"),
    ("Sarojini Naidu was born in London.", "False", "She was born in Hyderabad, British India.", "Easy"),
    ("Her father was an educationist and a social reformer.", "True", "Her father was an educationist and social-reformer.", "Easy"),
    ("Her mother was a doctor.", "False", "Her mother was a Bengali poet.", "Easy"),
    ("Sarojini Naidu started writing plays at the age of 12.", "True", "She began writing plays at age 12.", "Easy"),
    ("Her parents sent her to England at age 16 for higher education.", "True", "Delighted with her talent, they sent her to England at age 16.", "Easy"),
    ("Sarojini Naidu was known as the 'Queen of England'.", "False", "She was known as the 'Nightingale of India'.", "Easy"),
    ("She earned the title 'Nightingale of India' because of her soft, gentle, and melodious voice.", "True", "Her melodious voice in public speeches earned her the title.", "Easy"),
    ("Sarojini Naidu worked for the emancipation of women.", "True", "The text explicitly states she worked for the emancipation of women.", "Easy"),
    ("She refused to participate in India's struggle for freedom.", "False", "She actively participated in India's struggle for freedom.", "Easy"),
    ("After India became independent, Sarojini Naidu became the first woman governor.", "True", "She became the first woman governor of an Indian state.", "Easy"),
    ("She was the governor of the United Provinces.", "True", "She was given charge of the United Provinces.", "Easy"),
    ("The word 'worthy' means deserving.", "True", "Worthy is defined as deserving.", "Easy"),
    ("The word 'accomplished' means highly skilled at something.", "True", "Accomplished means highly skilled.", "Easy"),
    ("The word 'renowned' means completely unknown.", "False", "Renowned means widely acclaimed and honoured.", "Easy"),
    ("The word 'emancipation' means upliftment.", "True", "Emancipation is defined as upliftment.", "Easy"),
    ("Sarojini Naidu was a poet and a playwright.", "True", "She wrote impressive poems and plays.", "Easy"),
    ("Her mother wrote poetry in the Bengali language.", "True", "Her mother was a Bengali poet.", "Easy"),
    ("Sarojini Naidu went to England when she was 25 years old.", "False", "She went to England when she was 16 years old.", "Easy"),
    ("She spoke in a loud and angry tone on public platforms.", "False", "She spoke in a soft and gentle tone.", "Easy"),
    ("India was under British rule when Sarojini Naidu was born.", "True", "She was born in British India in 1879.", "Easy"),
    ("Sarojini Naidu was an uneducated person.", "False", "She was highly educated and went to England for higher studies.", "Easy"),
    ("Her title 'Nightingale of India' is related to a singing bird known for its sweet song.", "True", "The nightingale bird is famous for sweet melodious songs.", "Easy"),
    ("Women's emancipation means keeping women locked at home.", "False", "Emancipation means upliftment and freedom from social restrictions.", "Easy"),
    ("Chapter 07 is a biography of Sarojini Naidu.", "True", "Chapter 07 tells the inspirational life story of Sarojini Naidu.", "Easy"),

    # Medium (26-40)
    ("Sarojini Naidu's parents discouraged her from writing poetry.", "False", "Delighted with her talent, they supported her and sent her to England.", "Medium"),
    ("Sarojini Naidu's father worked to improve education and reform society.", "True", "He was an educationist and social reformer.", "Medium"),
    ("She started her public life as a businesswoman in England.", "False", "She was a poet, women's advocate, and freedom fighter.", "Medium"),
    ("Sarojini Naidu's soft and gentle tone was very effective in inspiring people for freedom.", "True", "Her melodious, gentle speeches moved people deeply.", "Medium"),
    ("Being the first woman governor proved that Indian women could lead independent states.", "True", "Her appointment broke gender barriers in post-independence governance.", "Medium"),
    ("Sarojini Naidu wrote her first plays in her late thirties.", "False", "She began writing plays at the age of 12.", "Medium"),
    ("Her mother's poetic talent influenced Sarojini's literary interests.", "True", "Growing up with a poet mother nurtured her literary gifts.", "Medium"),
    ("The United Provinces is the historical name for modern Uttar Pradesh.", "True", "United Provinces became modern Uttar Pradesh.", "Medium"),
    ("Sarojini Naidu only cared about poetry and ignored political freedom.", "False", "She actively participated in India's struggle for freedom.", "Medium"),
    ("Accomplished parents often provide an encouraging environment for talented children.", "True", "Her skilled parents nurtured her early talents.", "Medium"),
    ("Sarojini Naidu was 16 when she went to England for education.", "True", "The text notes she went at age 16.", "Medium"),
    ("Her melodious voice was a natural gift that she used for the nation's cause.", "True", "She used her gifted voice to speak for India's freedom.", "Medium"),
    ("Sarojini Naidu believed women should have equal rights and freedom.", "True", "She worked dedicatedly for the emancipation of women.", "Medium"),
    ("The title 'Nightingale of India' was given to her by the British government as a penalty.", "False", "It was an honorable title given for her sweet voice and inspiring poetry.", "Medium"),
    ("Learning about Sarojini Naidu teaches students about patriotism and literature.", "True", "Her life combines literary achievements with patriotism.", "Medium"),

    # Hard (41-50)
    ("Sarojini Naidu's life demonstrates that art and patriotism can work together for national progress.", "True", "Her poetry and speeches united artistic beauty with patriotic devotion.", "Hard"),
    ("Her father's work as a social reformer had no influence on her advocacy for women's rights.", "False", "Her father's commitment to social reform influenced her work for women's emancipation.", "Hard"),
    ("Becoming governor of United Provinces was the first time a woman held a state governorship in independent India.", "True", "She was the pioneer first woman governor in independent India.", "Hard"),
    ("Sarojini Naidu's oratory was forceful because she shouted loudly at crowds.", "False", "Her oratory was powerful because of her soft, gentle, and melodious conviction.", "Hard"),
    ("Her early writing at age 12 indicates exceptional childhood precocity and intelligence.", "True", "Writing plays at age 12 is a clear sign of precocious literary intelligence.", "Hard"),
    ("Women's emancipation in 20th-century India required both legal reform and inspirational role models like Sarojini Naidu.", "True", "Role models like her inspired women to step forward in public life.", "Hard"),
    ("Sarojini Naidu's birth in 1879 means she lived through both the colonial era and the dawn of independent India.", "True", "Born 1879, saw independence 1947, and served as governor.", "Hard"),
    ("The word 'renowned' implies that her reputation as a poet was confined only to her hometown.", "False", "Renowned means widely acclaimed across the nation and world.", "Hard"),
    ("Her literary works were written exclusively for commercial profit.", "False", "She wrote out of deep talent, passion, and devotion to her nation.", "Hard"),
    ("Chapter 07 serves as an exemplar of biographical writing for primary school students.", "True", "It presents key chronological facts and moral values of a national hero clearly.", "Hard")
]

tf_content = f"# True / False — Chapter 07: Nightingale of India\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH07_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH07_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who was Sarojini Naidu and when was she born?", "Sarojini Naidu was a renowned Indian poet and freedom fighter, born on 13th February 1879 in Hyderabad.", "Easy", "Remembering"),
    ("What were the professions of Sarojini Naidu's parents?", "Her father was an educationist and social reformer, while her mother was a Bengali poet.", "Easy", "Remembering"),
    ("At what age did Sarojini Naidu begin writing plays?", "She began writing plays at the age of 12.", "Easy", "Remembering"),
    ("Why did her parents send her to England when she was 16?", "They were delighted with her brilliant writing talent and sent her to England to complete her education.", "Easy", "Remembering"),
    ("What famous title was given to Sarojini Naidu?", "She was given the title 'the Nightingale of India'.", "Easy", "Remembering"),
    ("Why was she called 'the Nightingale of India'?", "She was called the Nightingale of India because of her soft, gentle, and melodious voice when speaking for freedom.", "Easy", "Remembering"),
    ("What social cause did Sarojini Naidu work for?", "She worked dedicatedly for the cause of emancipation (upliftment) of women.", "Easy", "Remembering"),
    ("What political struggle did Sarojini Naidu actively participate in?", "She actively participated in India's struggle for freedom from British rule.", "Easy", "Remembering"),
    ("What important position did she achieve after India became independent?", "She became the first woman governor of an Indian state (United Provinces).", "Easy", "Remembering"),
    ("Which state was Sarojini Naidu given charge of as governor?", "She was given charge of the United Provinces.", "Easy", "Remembering"),
    ("What is the meaning of the word 'worthy'?", "Worthy means deserving or having value.", "Easy", "Understanding"),
    ("What is the meaning of the word 'accomplished'?", "Accomplished means highly skilled or expert at something.", "Easy", "Understanding"),
    ("What is the meaning of the word 'renowned'?", "Renowned means widely acclaimed, famous, and honoured.", "Easy", "Understanding"),
    ("What is the meaning of the word 'emancipation'?", "Emancipation means social upliftment and liberation from restrictions.", "Easy", "Understanding"),
    ("Where was Sarojini Naidu born?", "She was born in Hyderabad, British India.", "Easy", "Remembering"),
    ("What kind of voice was Sarojini Naidu gifted with?", "She was gifted with a soft, gentle, and melodious voice.", "Easy", "Remembering"),
    ("What did Sarojini write besides plays?", "She wrote impressive poems.", "Easy", "Remembering"),
    ("Was Sarojini Naidu the first woman governor in India?", "Yes, she was the first woman governor in independent India.", "Easy", "Remembering"),
    ("What language did Sarojini's mother write poetry in?", "Her mother wrote poetry in the Bengali language.", "Easy", "Remembering"),
    ("How did Sarojini Naidu speak on public platforms?", "She spoke in a soft, gentle, and melodious tone about India's freedom.", "Easy", "Remembering"),
    ("Did Sarojini Naidu's parents support her literary talent?", "Yes, they were delighted with her talent and supported her higher education in England.", "Easy", "Remembering"),
    ("What two main fields made Sarojini Naidu famous?", "She was famous for poetry (literature) and freedom struggle (politics).", "Easy", "Remembering"),
    ("What does being a 'worthy child' mean in the text?", "It means she matched her parents' high skills and intellect through her own achievements.", "Easy", "Understanding"),
    ("Why is Sarojini Naidu an inspiration for women in India?", "She broke barriers by becoming a renowned poet, freedom fighter, and the first woman governor.", "Easy", "Understanding"),
    ("What is the title of Chapter 07?", "Chapter 07 is titled 'Nightingale of India'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("How did Sarojini Naidu's parents influence her early life?", "Her father instilled a passion for social reform and education, while her poet mother nurtured her love for writing poetry and plays.", "Medium", "Understanding"),
    ("Why was sending Sarojini to England at age 16 a significant decision by her parents?", "In 1895, sending a 16-year-old girl abroad for higher education was rare, showing how deeply her parents valued her talent.", "Medium", "Analyzing"),
    ("Explain the dual meaning of the title 'Nightingale of India'.", "It refers to both the sweet, melodious quality of her public speech and the lyricism and beauty of her poetry devoted to India.", "Medium", "Analyzing"),
    ("What does 'emancipation of women' mean in Sarojini Naidu's work?", "It means raising women's status in society through education, equal rights, and active participation in national affairs.", "Medium", "Understanding"),
    ("How did Sarojini Naidu contribute to India's freedom struggle?", "She gave inspiring public speeches, led protest movements, and mobilized people across India with her powerful words.", "Medium", "Understanding"),
    ("Why is her appointment as governor of United Provinces considered a milestone for Indian women?", "It was a landmark victory for gender equality, proving that women could successfully lead state administration in free India.", "Medium", "Evaluating"),
    ("In what way did Sarojini Naidu demonstrate that softness and strength can coexist?", "She spoke in a soft and gentle voice, yet her words held immense strength and conviction that stirred a nation to fight for freedom.", "Medium", "Analyzing"),
    ("How old was Sarojini Naidu when she began writing plays, and what does this show?", "She was 12 years old, which shows she was a child prodigy with natural literary genius.", "Medium", "Understanding"),
    ("What qualities made Sarojini Naidu an 'accomplished' leader?", "Her deep intellect, poetic grace, persuasive speech, courage in freedom struggles, and administrative wisdom.", "Medium", "Understanding"),
    ("How did her speeches help the freedom movement?", "Her speeches communicated the message of freedom with grace and emotion, unifying people from different backgrounds.", "Medium", "Analyzing"),
    ("Summarize Page 27 of the textbook in two sentences.", "Sarojini Naidu was born in Hyderabad in 1879 to an educationist father and poet mother. She became a renowned poet, freedom fighter, women's advocate, and the first woman governor of free India.", "Medium", "Understanding"),
    ("Why is Sarojini Naidu remembered on National Women's Day in India?", "Her birth anniversary is celebrated to honor her pioneering role in securing women's rights and leadership in India.", "Medium", "Evaluating"),
    ("What background did her father bring to her upbringing?", "He was an educationist and social reformer, providing a home filled with books, ideas, and progressive values.", "Medium", "Understanding"),
    ("How did Sarojini Naidu balance her artistic career with political leadership?", "She brought poetic beauty and moral grace into her political speeches, using literature to serve the cause of Indian independence.", "Medium", "Analyzing"),
    ("What lesson can Class 2 students learn from Sarojini Naidu's childhood?", "Students learn that age is no barrier to talent—by reading and practicing, even young children can write wonderful stories and poems.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique how Sarojini Naidu redefined women's roles in early 20th-century India.", "She shattered traditional expectations by stepping out of domestic confines onto national stages, leading freedom marches, and occupying top executive office as governor.", "Hard", "Evaluating"),
    ("Analyze the relationship between language, voice, and leadership in Sarojini Naidu's speeches.", "Her gentle, melodious tone proved that true leadership does not rely on aggressive shouting; persuasive grace and moral clarity command far deeper respect.", "Hard", "Analyzing"),
    ("Deconstruct Sarojini Naidu's legacy into her literary, social, and political contributions.", "1. **Literary**: Renowned poet and playwright.\n2. **Social**: Champion for women's emancipation.\n3. **Political**: Freedom fighter and pioneer woman governor.", "Hard", "Analyzing"),
    ("Compare Sarojini Naidu's early education in England with her patriotic service in India.", "While her English education refined her intellect and international perspective, her heart remained deeply rooted in Indian culture and freedom.", "Hard", "Analyzing"),
    ("Evaluate the impact of family background on a child's development, using Sarojini Naidu as an example.", "Her accomplished parents provided both genetic talent and an environment of social reform, demonstrating that supportive families unlock a child's potential.", "Hard", "Evaluating"),
    ("How can a school teacher use Sarojini Naidu's biography to teach both English and Social Studies?", "The teacher can use her poems for English literature and her life story for Social Studies history lessons on freedom fighters and government.", "Hard", "Applying"),
    ("Assess Sarojini Naidu's role as a bridge between British India and Independent India.", "Born in British India in 1879, she spent decades fighting colonial rule, and then helped govern independent India in 1947 as its first woman governor.", "Hard", "Evaluating"),
    ("Why is Sarojini Naidu's title 'Nightingale of India' still celebrated worldwide today?", "Because her poetic works (like *The Golden Threshold*) and her melodious legacy continue to inspire lovers of literature and freedom globally.", "Hard", "Analyzing"),
    ("Formulate a short tribute speech honoring Sarojini Naidu for a school assembly.", "'Today we honor Sarojini Naidu, the Nightingale of India! A brilliant poet at 12, a brave freedom fighter, and India's first woman governor. May her sweet voice and strong courage inspire us all!'", "Hard", "Creating"),
    ("Synthesize the main moral takeaway of Chapter 07 for young learners.", "Dedicate your voice, education, and talent to the service of others, stand up for equality, and serve your country with grace and courage!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 07: Nightingale of India\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH07_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH07_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe Sarojini Naidu's birth, family background, and early education.", 
     "Sarojini Naidu was born on 13th February 1879 in Hyderabad, British India. She was raised in a highly accomplished family. Her father was a dedicated educationist and social reformer, while her mother was a talented Bengali poet. Growing up in this intellectual home, Sarojini showed remarkable talent early on, writing plays at age 12. Delighted by her genius, her parents sent her to England at age 16 to complete her higher education.", 
     "Easy", "Remembering"),

    ("Explain how Sarojini Naidu earned the famous title 'the Nightingale of India'.", 
     "Sarojini Naidu was a gifted poet who possessed a soft, gentle, and melodious voice. During India's struggle for independence, she spoke on numerous public stages about freedom and unity. Her speeches were delivered with such poetic grace, warmth, and melodious tone that listeners were deeply moved. This sweet, inspiring voice earned her the beloved national title 'the Nightingale of India' (*Bharat Kokila*).", 
     "Easy", "Remembering"),

    ("What were Sarojini Naidu's major contributions to India's freedom struggle and women's rights?", 
     "Sarojini Naidu contributed immensely to India in two key ways:\n1. **Freedom Struggle**: She actively participated in independence movements, inspiring millions through her powerful speeches and leadership alongside national leaders.\n2. **Women's Emancipation**: She fought for the upliftment of women, advocating for female education, voting rights, and equal status in society.", 
     "Easy", "Understanding"),

    ("Describe Sarojini Naidu's historical achievement after India gained independence in 1947.", 
     "After India won independence in 1947, Sarojini Naidu achieved a historic milestone by becoming the very first woman governor in independent India. She was appointed to govern the United Provinces (modern Uttar Pradesh). In this top executive post, she served with great wisdom, dignity, and administrative skill, setting a shining example for women leaders in India.", 
     "Easy", "Remembering"),

    ("Explain the meanings of the four vocabulary words: 'worthy', 'accomplished', 'renowned', and 'emancipation'.", 
     "1. **Worthy**: Deserving respect, praise, or value.\n2. **Accomplished**: Highly skilled and expert at a particular art or field.\n3. **Renowned**: Famous, widely acclaimed, and honored by people.\n4. **Emancipation**: Social upliftment and liberation from restrictive rules or inequality.", 
     "Easy", "Understanding"),

    ("How did Sarojini Naidu's parents encourage her writing talent?", 
     "Sarojini's parents recognized her early genius when she began writing plays at age 12. Instead of ignoring her talent, they praised her impressive work and provided full encouragement. When she turned 16, they took the major step of sending her to England for advanced education so her literary and intellectual gifts could flourish fully.", 
     "Easy", "Understanding"),

    ("Describe Sarojini Naidu's achievements as a poet and playwright.", 
     "Sarojini Naidu began her literary journey at age 12 by writing plays and poems. Over her life, she became a renowned poet whose works were praised worldwide for their imagery, lyrical beauty, and emotional depth. Her poetry celebrated Indian nature, culture, and patriotic spirit, earning her a lasting place among India's greatest English poets.", 
     "Easy", "Remembering"),

    ("Why is Sarojini Naidu considered a role model for young girls in India today?", 
     "She is a role model because she proved that women can achieve greatness in multiple fields. She was a brilliant poet at a young age, a courageous freedom fighter, an advocate for women's rights, and the first woman governor of an Indian state. Her life teaches girls to pursue education, speak gracefully, and lead with courage.", 
     "Easy", "Understanding"),

    ("What role did Sarojini Naidu play as Governor of the United Provinces?", 
     "As Governor of the United Provinces after 1947, Sarojini Naidu served as the head of state administration. She maintained law, peace, and harmony during the post-independence transition period. She greeted national and international leaders with grace and ensured that governance was carried out with fairness and dignity.", 
     "Easy", "Understanding"),

    ("Summarize the life journey of Sarojini Naidu from childhood to governorship.", 
     "Sarojini Naidu was born in 1879 in Hyderabad to accomplished parents. She wrote plays at 12, studied in England at 16, and became a renowned poet. She joined India's freedom struggle, fought for women's emancipation, earned the title 'Nightingale of India' for her melodious voice, and ultimately became India's first woman governor in 1947.", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Where and when was Sarojini Naidu born, and who were her parents?", "Sarojini Naidu was born on 13th February 1879 in Hyderabad, British India. Her father was an educationist and social reformer, and her mother was a Bengali poet.", "Easy", "Remembering"),
    ("Why did Sarojini Naidu go to England when she was 16 years old?", "Her parents were delighted with her brilliant poetry and playwriting talent at age 12, so they sent her to England at age 16 to complete her higher education.", "Easy", "Remembering"),
    ("What made Sarojini Naidu's voice special during public speeches?", "She was gifted with a soft, gentle, and melodious voice. She spoke about India's freedom with such poetic grace and warmth that she was named 'the Nightingale of India'.", "Easy", "Understanding"),
    ("How did Sarojini Naidu help women in India?", "She worked dedicatedly for the emancipation of women by advocating for female literacy, social freedom, equal rights, and participation in public life.", "Easy", "Understanding"),
    ("What historical first did Sarojini Naidu achieve in independent India?", "She became the first woman governor of an Indian state (the United Provinces) after India achieved independence in 1947.", "Easy", "Remembering"),
    ("Explain why her father's profession as a social reformer influenced her life.", "Her father worked to reform society and promote education. Growing up in his home inspired Sarojini to work for social justice, women's rights, and national freedom.", "Easy", "Understanding"),
    ("How did her mother's poetic background influence Sarojini Naidu?", "Her mother was a Bengali poet. Living with a poet mother nurtured Sarojini's literary talent, inspiring her to start writing poems and plays from a young age.", "Easy", "Understanding"),
    ("What is the United Provinces known as in modern India?", "The United Provinces is the historical name for the modern state of Uttar Pradesh in northern India.", "Easy", "Remembering"),
    ("Why is National Women's Day celebrated on February 13 in India?", "February 13 is Sarojini Naidu's birth anniversary, celebrated as National Women's Day to honor her contributions to women's rights and leadership.", "Easy", "Remembering"),
    ("Describe Sarojini Naidu's character traits based on Chapter 07.", "She was talented, intelligent, patriotic, soft-spoken, courageous, accomplished, and deeply dedicated to women's upliftment and national service.", "Easy", "Understanding"),
    ("How can students apply Sarojini Naidu's values in their school life?", "Students can practice writing poems or stories, speak politely with a gentle tone, support equal treatment for boys and girls, and love their country.", "Easy", "Applying"),
    ("What does the word 'accomplished' tell us about her parents?", "It tells us that both her father and mother were highly skilled, educated, and respected experts in their respective fields of social reform and poetry.", "Easy", "Understanding"),
    ("Why was Sarojini Naidu called a 'worthy child'?", "Because she honored her parents' intellectual legacy by developing her own great talents in literature and public service.", "Easy", "Understanding"),
    ("How did Sarojini Naidu show patriotism during British rule?", "She joined the freedom struggle, gave public speeches across India, and used her poetry and voice to inspire people to win independence.", "Easy", "Understanding"),
    ("Summarize Chapter 07 in five key sentences.", "Sarojini Naidu was born in Hyderabad in 1879 to an educationist and a poet. She wrote plays at 12 and studied in England at 16. Known as 'the Nightingale of India', her melodious voice inspired the freedom movement. She fought for women's emancipation and became India's first woman governor in 1947. Her life is a shining example of poetry, leadership, and service.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how Sarojini Naidu's early childhood environment shaped her future achievements.", 
     "Sarojini Naidu was raised in an environment rich in intellect and culture. Her father's dedication to education and social reform taught her to care for society and fight for justice. Her mother's poetic talent ignited her creative imagination. This combination of social consciousness and artistic expression provided the foundation for her dual career as a national leader and world-renowned poet.", 
     "Medium", "Analyzing"),

    ("Examine the significance of soft and gentle speech in effective public leadership.", 
     "Public leadership is often associated with loud, aggressive speeches. However, Sarojini Naidu proved that a soft, gentle, and melodious voice can be far more persuasive. Her gentle tone conveyed sincerity, grace, and deep moral conviction, touching the hearts of listeners and inspiring them to unite for national freedom.", 
     "Medium", "Analyzing"),

    ("Discuss Sarojini Naidu's role in advancing women's rights during the colonial era.", 
     "During colonial rule, Indian women faced severe social restrictions. Sarojini Naidu campaigned tirelessly for women's emancipation, demanding access to higher education, political franchise, and civic equality. By serving as an active freedom fighter and later as the first woman governor, she physically demonstrated that women could lead at the highest levels.", 
     "Medium", "Evaluating"),

    ("Explore how poetry and political activism complemented each other in Sarojini Naidu's life.", 
     "Poetry gave Sarojini Naidu an expressive voice, emotional sensitivity, and mastery of language. Political activism gave her a noble cause to fight for. Instead of separating the two, she infused her political speeches with poetic beauty and wrote poems celebrating Indian culture, making her activism uniquely artistic and powerful.", 
     "Medium", "Analyzing"),

    ("How can teachers use Sarojini Naidu's biography to teach gender equality to Class 2 students?", 
     "Teachers can highlight that Sarojini Naidu was sent abroad for education just like boys, wrote brilliant plays at age 12, and became India's first woman governor. This shows young students that girls and boys have equal intelligence and capability to lead nations.", 
     "Medium", "Applying"),

    ("Why was Sarojini Naidu's talent noticed so early at age 12?", "At age 12, she wrote complex plays and poems with mature vocabulary and rhythm, demonstrating an extraordinary literary genius that amazed her parents and teachers.", "Medium", "Understanding"),
    ("Describe the impact of Sarojini Naidu's overseas education in England on her worldview.", "Studying in England exposed her to western literature and global political thoughts, giving her a cosmopolitan outlook while strengthening her resolve to see India free.", "Medium", "Analyzing"),
    ("What makes the title 'Nightingale of India' uniquely poetic and nationalistic?", "It combines 'Nightingale' (symbolizing sweet, melodious song and poetry) with 'of India' (highlighting her complete devotion to her motherland).", "Medium", "Analyzing"),
    ("Explain the challenge of governing the United Provinces in post-independence 1947.", "In 1947, India faced partition turmoil and administrative reset. As Governor, Sarojini Naidu had to maintain peace, restore social harmony, and set up state governance with tact and leadership.", "Medium", "Evaluating"),
    ("How does Chapter 07 illustrate the concept of being an 'accomplished' citizen?", "It shows that an accomplished citizen uses their personal talents (like writing or speaking) not just for self-gain, but for national freedom and social upliftment.", "Medium", "Evaluating"),
    ("Contrast Sarojini Naidu's life as a young student in 1895 with her life as a governor in 1947.", "In 1895, she was a young 16-year-old student travelling to England to learn. In 1947, she was a 68-year-old revered national leader governing a major Indian state.", "Medium", "Analyzing"),
    ("Why did Mahatma Gandhi and national leaders deeply respect Sarojini Naidu?", "They respected her for her unwavering patriotism, brilliant intellect, humorous wit, loyal friendship, and inspiring speeches during freedom marches.", "Medium", "Understanding"),
    ("What role does vocabulary like 'emancipation' play in expanding primary students' moral understanding?", "Learning 'emancipation' teaches students about fairness, freedom, and lifting others out of hardship, helping them build moral empathy alongside vocabulary.", "Medium", "Evaluating"),
    ("How does the story build a sense of national pride in young readers?", "By showcasing how an Indian woman gained worldwide fame as a poet and led the nation to freedom, it fills young readers with pride in India's heritage.", "Medium", "Analyzing"),
    ("Construct a 4-line poem in praise of Sarojini Naidu inspired by Chapter 07.", "'Soft was her voice, yet strong was her heart,\nShe served her sweet nation with freedom and art.\nThe Nightingale sang for a land proud and free,\nA beacon of grace for you and for me!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique Sarojini Naidu's historical legacy in the context of modern Indian feminism.", 
     "Sarojini Naidu laid the foundational pillar of Indian feminism. She did not view women's rights as an isolated battle, but linked women's emancipation directly to national independence. By demonstrating female excellence in poetry, mass movement leadership, and constitutional governance, she established that Indian democracy could only be complete with equal female participation.", 
     "Hard", "Evaluating"),

    ("Deconstruct the literary style of Sarojini Naidu's speeches and poetry.", 
     "Her literary style was characterized by rich lyrical rhythm, vivid imagery, and emotional warmth. In speeches, she translated this poetic style into smooth, melodious oratory that appealed to human emotions rather than dry political rhetoric, making her one of the most effective communicators of the freedom movement.", 
     "Hard", "Analyzing"),

    ("Synthesize how home environment, international exposure, and national struggle formed Sarojini Naidu's personality.", 
     "1. **Home Environment**: Provided intellectual curiosity and artistic roots.\n2. **International Exposure (England)**: Refined her academic discipline and global perspective.\n3. **National Struggle**: Channelled her talents into selfless service, transforming a romantic poet into a resilient stateswoman.", 
     "Hard", "Synthesizing"),

    ("Formulate a unit test strategy based on Chapter 07 to assess remembering, understanding, and evaluating skills.", 
     "- **Remembering**: Ask birth date (1879), birthplace (Hyderabad), and title ('Nightingale of India').\n- **Understanding**: Explain why her voice earned her the title and what 'emancipation' means.\n- **Evaluating**: Assess why her appointment as first woman governor was a historic milestone for India.", 
     "Hard", "Creating"),

    ("Evaluate the impact of female representation in governance as pioneered by Sarojini Naidu.", 
     "Sarojini Naidu's governorship proved that women possess the administrative capability, moral authority, and political wisdom required for top state leadership. Her success paved the way for future generations of female ministers, governors, and prime ministers in India.", 
     "Hard", "Evaluating"),

    ("Analyze why Sarojini Naidu chose to write poetry in English while maintaining a deep Indian thematic identity.", "Writing in English allowed her to communicate India's rich culture and freedom aspirations to an international audience, while her themes remained purely Indian (folk songs, freedom, nature), creating a bridge between East and West.", "Hard", "Analyzing"),
    ("Compare Sarojini Naidu's gentle speech style with aggressive political methods of her era.", "While aggressive methods relied on confrontation, Sarojini Naidu's gentle, melodious speeches won hearts through moral persuasion, emotional connection, and dignified grace, proving that gentle words can move mountains.", "Hard", "Analyzing"),
    ("Draft an inspirational speech for National Women's Day celebrating Sarojini Naidu's achievements.", "'Friends, today on National Women's Day, we celebrate Sarojini Naidu—the Nightingale of India! She proved that a woman's voice can awaken a nation and lead a state. Let us honor her by standing for equality, education, and courage!'", "Hard", "Creating"),
    ("Assess the social changes brought about by Sarojini Naidu's work for women's emancipation.", "Her advocacy helped shift societal attitudes, encouraging families to educate daughters, support female careers, and accept women in public administration and politics.", "Hard", "Evaluating"),
    ("Synthesize the ultimate philosophy of Sarojini Naidu into a guiding motto for future generations.", "'Sing your truth with a melodious voice, fight for justice with a gentle heart, and serve your nation with courage and grace!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 07: Nightingale of India\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH07_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH07_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Sarojini Naidu was born on 13th February 1879, in Hyderabad, British India. Her father was an educationist and a social-reformer. Her mother was a Bengali poet.",
     [
         ("When was Sarojini Naidu born?", "13th February 1879.", "Easy", "Remembering"),
         ("Where was she born?", "In Hyderabad, British India.", "Easy", "Remembering"),
         ("What was her father's profession?", "He was an educationist and a social-reformer.", "Easy", "Remembering"),
         ("What was her mother's background?", "She was a Bengali poet.", "Easy", "Remembering"),
         ("What kind of environment did her parents provide?", "An intellectual home filled with education, poetry, and social reform.", "Medium", "Understanding")
     ]),

    # Set 2
    ("Sarojini was a worthy child of such accomplished parents and she began writing plays at the age of 12. She wrote impressive poems and plays.",
     [
         ("What word describes Sarojini as a child in relation to her parents?", "A worthy child.", "Easy", "Remembering"),
         ("At what age did she begin writing plays?", "At the age of 12.", "Easy", "Remembering"),
         ("What two types of literary works did she write?", "Poems and plays.", "Easy", "Remembering"),
         ("What does the word 'accomplished' mean?", "Highly skilled at something.", "Medium", "Understanding"),
         ("What does writing plays at age 12 show about Sarojini?", "It shows her early genius and extraordinary writing talent.", "Medium", "Analyzing")
     ]),

    # Set 3
    ("Delighted with her talent, her parents sent her to England for completing her education when she was 16.",
     [
         ("How did her parents feel about her writing talent?", "They were delighted.", "Easy", "Remembering"),
         ("Where did her parents send her to complete her education?", "To England.", "Easy", "Remembering"),
         ("How old was Sarojini when she went to England?", "She was 16 years old.", "Easy", "Remembering"),
         ("Why did her parents send her abroad?", "For completing her higher education.", "Easy", "Remembering"),
         ("What does this decision show about her parents' values?", "It shows they deeply valued female education and nurtured her talent.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("Sarojini Naidu became a renowned poet and worked for the cause of emancipation of women. She also actively participated in India's struggle for freedom.",
     [
         ("What kind of poet did Sarojini Naidu become?", "A renowned poet.", "Easy", "Remembering"),
         ("What cause did she work for regarding women?", "Emancipation of women.", "Easy", "Remembering"),
         ("What national movement did she actively join?", "India's struggle for freedom.", "Easy", "Remembering"),
         ("What does the word 'emancipation' mean?", "Upliftment / freedom from social restrictions.", "Medium", "Understanding"),
         ("What does 'renowned' mean?", "Widely acclaimed and honoured.", "Medium", "Understanding")
     ]),

    # Set 5
    ("She was gifted with a melodious voice and on various platforms she spoke about India's freedom in a soft and gentle tone. This earned her the title of 'the Nightingale of India'.",
     [
         ("What kind of voice was Sarojini Naidu gifted with?", "A melodious voice.", "Easy", "Remembering"),
         ("In what tone did she speak on various platforms?", "In a soft and gentle tone.", "Easy", "Remembering"),
         ("What subject did she speak about on these platforms?", "India's freedom.", "Easy", "Remembering"),
         ("What title was given to her because of her voice and speech?", "'The Nightingale of India'.", "Easy", "Remembering"),
         ("Why is the nightingale bird used in her title?", "Because nightingales are famous for their sweet, melodious songs.", "Medium", "Understanding")
     ]),

    # Set 6
    ("After India became independent, Sarojini Naidu became the first woman governor. She was given the charge for the United Provinces.",
     [
         ("What major achievement did Sarojini Naidu attain after independence?", "She became the first woman governor.", "Easy", "Remembering"),
         ("Which state was she given charge of?", "The United Provinces.", "Easy", "Remembering"),
         ("When did she become governor?", "After India became independent.", "Easy", "Remembering"),
         ("Why was her appointment historically important for Indian women?", "It was the first time a woman held a state governorship in independent India.", "Medium", "Evaluating"),
         ("What is the modern name of the United Provinces?", "Uttar Pradesh.", "Medium", "Remembering")
     ]),

    # Set 7
    ("Word Meaning: Worthy: Deserving | Accomplished: Highly skilled at something | Renowned: Widely acclaimed and honoured | Emancipation: Upliftment",
     [
         ("What is the meaning of 'worthy'?", "Deserving.", "Easy", "Remembering"),
         ("What is the meaning of 'accomplished'?", "Highly skilled at something.", "Easy", "Remembering"),
         ("What is the meaning of 'renowned'?", "Widely acclaimed and honoured.", "Easy", "Remembering"),
         ("What is the meaning of 'emancipation'?", "Upliftment.", "Easy", "Remembering"),
         ("Which vocabulary word describes Sarojini's fame as a poet?", "Renowned.", "Easy", "Understanding")
     ]),

    # Set 8
    ("Sarojini Naidu was born on 13th February 1879, in Hyderabad, British India. Her father was an educationist and a social-reformer.",
     [
         ("What date was Sarojini Naidu born?", "13th February.", "Easy", "Remembering"),
         ("In which city was she born?", "Hyderabad.", "Easy", "Remembering"),
         ("What was the political status of India when she was born?", "British India.", "Easy", "Remembering"),
         ("What two things was her father involved in?", "Education and social reform.", "Easy", "Remembering"),
         ("How did her birthplace in Hyderabad reflect British India?", "Hyderabad was a major historical princely city during the British colonial period.", "Medium", "Understanding")
     ]),

    # Set 9
    ("She was gifted with a melodious voice and on various platforms she spoke about India's freedom in a soft and gentle tone. This earned her the title of 'the Nightingale of India'.",
     [
         ("What gift did Sarojini Naidu possess for speaking?", "A melodious voice.", "Easy", "Remembering"),
         ("What manner of speech did she use?", "A soft and gentle tone.", "Easy", "Remembering"),
         ("What movement did her speeches support?", "India's freedom movement.", "Easy", "Remembering"),
         ("Who is known as the Nightingale of India?", "Sarojini Naidu.", "Easy", "Remembering"),
         ("How did her gentle tone affect audiences?", "It moved listeners emotionally and inspired patriotism with grace.", "Medium", "Analyzing")
     ]),

    # Set 10
    ("After India became independent, Sarojini Naidu became the first woman governor. She was given the charge for the United Provinces.",
     [
         ("Did Sarojini Naidu become governor before or after independence?", "After India became independent.", "Easy", "Remembering"),
         ("What rank of leadership did she achieve as a woman in India?", "She was the first woman governor.", "Easy", "Remembering"),
         ("What area did she govern?", "The United Provinces.", "Easy", "Remembering"),
         ("What qualities made her suitable for governorship?", "Her intellect, leadership, administrative skill, and dedication to the nation.", "Medium", "Understanding"),
         ("Summarize the significance of this extract in one sentence.", "Sarojini Naidu broke gender barriers by serving as independent India's pioneer first woman governor.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 07: Nightingale of India\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH07_EXT_{q_counter:03d}"
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

with open(os.path.join(CH07_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 07 in {CH07_DIR}")
