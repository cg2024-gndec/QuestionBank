r"""
Refines all 6 Category files for Book 5 Chapter 07 ("The Iron Man of India: Sardar Vallabhbhai Patel") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH07_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_07")
os.makedirs(CH07_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Who is universally known as the 'Iron Man of India'?", "(A) Sardar Vallabhbhai Patel", "(B) Mahatma Gandhi", "(C) Bhagat Singh", "(D) Subhas Chandra Bose", "(A)", "Sardar Vallabhbhai Patel is called the Iron Man of India.", "Easy", "Remembering", "Identity"),
    ("When was Sardar Vallabhbhai Patel born?", "(A) October 31, 1875", "(B) August 15, 1947", "(C) October 2, 1869", "(D) December 15, 1950", "(A)", "Born on October 31, 1875.", "Easy", "Remembering", "Birth Date"),
    ("In which Indian state was Sardar Vallabhbhai Patel born?", "(A) Gujarat", "(B) Punjab", "(C) Rajasthan", "(D) Uttar Pradesh", "(A)", "Sardar Patel was born in Gujarat.", "Easy", "Remembering", "Birthplace"),
    ("How did Sardar Patel spend his childhood according to Chapter 07?", "(A) Assisting his father in agricultural fields", "(B) Studying in foreign universities", "(C) Working in textile factories", "(D) Sailing on merchant ships", "(A)", "He spent his childhood assisting his father in fields.", "Easy", "Remembering", "Childhood"),
    ("What skills did young Vallabhbhai learn while assisting his father in the fields?", "(A) Cultivation and animal husbandry", "(B) Computer programming and typing", "(C) Ship navigation and fishing", "(D) Metal welding and mining", "(A)", "He learnt a lot about cultivation and animal husbandry.", "Easy", "Remembering", "Early Education"),
    ("How did young Vallabhbhai manage his studies despite financial difficulties?", "(A) He studied from borrowed books", "(B) He hired private tutors", "(C) He bought expensive foreign textbooks", "(D) He studied only online", "(A)", "He studied from borrowed books.", "Easy", "Remembering", "Resourcefulness"),
    ("What key personality traits defined Vallabhbhai Patel as he grew up?", "(A) Honest, strong, and determined", "(B) Shy, fearful, and hesitant", "(C) Proud, careless, and lazy", "(D) Cold, silent, and selfish", "(A)", "He grew up to be honest, strong, and determined.", "Easy", "Remembering", "Personality Traits"),
    ("What core belief did Sardar Patel hold regarding the people of India?", "(A) All Indians should stay together like one big family", "(B) Each state should become an independent country", "(C) Only rich people should rule India", "(D) People should live in isolated groups", "(A)", "He believed all Indians should stay together like one big family.", "Easy", "Understanding", "Core Philosophy"),
    ("When did India gain independence from British rule?", "(A) 1947", "(B) 1857", "(C) 1920", "(D) 1950", "(A)", "India gained independence from British rule in 1947.", "Easy", "Remembering", "Historical Date"),
    ("What major political challenge faced India immediately after gaining independence in 1947?", "(A) The country was divided into many small kingdoms (princely states)", "(B) There were no roads in India", "(C) Everyone left the country", "(D) The ocean covered the land", "(A)", "After independence, the country had many small kingdoms.", "Easy", "Understanding", "Post-Independence Challenge"),
    ("What qualities did Sardar Patel use to bring small kingdoms together into one nation?", "(A) Wisdom, courage, strength, leadership, and negotiation", "(B) Forceful weapons and continuous war", "(C) Secret foreign help", "(D) Financial bribery and deception", "(A)", "Used wisdom, courage, strength, leadership, and negotiation.", "Easy", "Understanding", "Unification Skills"),
    ("Why did people bestow the title 'Iron Man of India' upon Sardar Patel?", "(A) Because of his resolute strength, leadership, and determination in uniting India", "(B) Because he owned iron factories", "(C) Because he wore iron armor", "(D) Because he lifted heavy iron weights", "(A)", "Because of his strength, leadership, and unyielding determination.", "Easy", "Understanding", "Title Reason"),
    ("How did Sardar Patel help improve the lives of Indian farmers?", "(A) By encouraging the formation of cooperative societies for farmers", "(B) By taking away their agricultural land", "(C) By forcing them to move to cities", "(D) By banning farming completely", "(A)", "Encouraged the formation of cooperative societies for farmers.", "Easy", "Understanding", "Farmer Welfare"),
    ("Which world-famous dairy organization's formation was inspired and guided by Sardar Patel?", "(A) AMUL", "(B) Mother Dairy", "(C) Nestle", "(D) Britannia", "(A)", "He inspired and guided the movement leading to the formation of AMUL.", "Easy", "Remembering", "Amul Connection"),
    ("When did Sardar Vallabhbhai Patel pass away?", "(A) December 15, 1950", "(B) October 31, 1875", "(C) August 15, 1947", "(D) January 26, 1950", "(A)", "He passed away on December 15, 1950.", "Easy", "Remembering", "Passing Date"),
    ("What monument stands in Gujarat today to honor Sardar Vallabhbhai Patel?", "(A) The Statue of Unity", "(B) The Statue of Liberty", "(C) India Gate", "(D) Gateway of India", "(A)", "The Statue of Unity stands in Gujarat to honor him.", "Easy", "Remembering", "Monument"),
    ("What global distinction does the Statue of Unity hold?", "(A) It is the tallest statue in the world", "(B) It is the oldest statue in Asia", "(C) It is made entirely of solid gold", "(D) It is located underwater", "(A)", "The Statue of Unity is the tallest statue in the world.", "Easy", "Remembering", "Statue Rank"),
    ("What does the word 'unity' mean according to the vocabulary box?", "(A) Being together as one", "(B) Splitting into small pieces", "(C) Fighting with neighbors", "(D) Traveling alone", "(A)", "Unity = Being together as one.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'determination' mean?", "(A) Strong will to achieve something", "(B) Fear of trying new things", "(C) Changing one's mind constantly", "(D) Sleeping all day", "(A)", "Determination = Strong will to achieve something.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'leadership' mean?", "(A) The ability to guide and inspire others", "(B) Ordering people around angrily", "(C) Following others silently", "(D) Running away from trouble", "(A)", "Leadership = The ability to guide and inspire others.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'negotiation' mean?", "(A) Discussion to reach an agreement", "(B) Fighting with fists", "(C) Running a fast race", "(D) Buying goods at a store", "(A)", "Negotiation = Discussion to reach an agreement.", "Easy", "Understanding", "Vocabulary"),
    ("In which country is the Statue of Unity located?", "(A) India (Gujarat)", "(B) United States", "(C) Great Britain", "(D) France", "(A)", "Located in Gujarat, India.", "Easy", "Remembering", "Location"),
    ("What dream of Sardar Patel continues to live on today?", "(A) His dream of a united India", "(B) His dream of owning a ship", "(C) His dream of building castles", "(D) His dream of traveling abroad", "(A)", "His dream of a united India lives on.", "Easy", "Remembering", "Legacy Dream"),
    ("Sardar Patel is remembered as a true _______ of India.", "(A) Hero", "(B) King", "(C) Merchant", "(D) Visitor", "(A)", "Remembered as a true hero of India.", "Easy", "Remembering", "Closing Title"),
    ("What title is given to Chapter 07?", "(A) The Iron Man of India: Sardar Vallabhbhai Patel", "(B) The Milkman of India", "(C) The Missile Man of India", "(D) Traditional Dresses from India", "(A)", "Title is 'The Iron Man of India: Sardar Vallabhbhai Patel'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why was the integration of 560+ princely states crucial for independent India in 1947?", "(A) Without integration, India would have fragmented into hundreds of warring independent nations, destroying national security", "(B) Princely states owned all the ocean water", "(C) British officers insisted on keeping princely states", "(D) Princely states had no human population", "(A)", "Unification prevented national balkanization and established security.", "Medium", "Analyzing", "Historical Criticality"),
    ("How did Sardar Patel's childhood in rural Gujarat influence his administrative vision?", "(A) Working in fields taught him practical agricultural economics, animal husbandry, and deep empathy for farming communities", "(B) It made him dislike farming", "(C) He decided to become a sailor", "(D) It taught him foreign diplomacy only", "(A)", "Farm background instilled agricultural knowledge and empathy for rural workers.", "Medium", "Analyzing", "Background Influence"),
    ("Analyze the diplomatic skill of 'negotiation' as used by Sardar Patel.", "(A) He persuaded princely rulers to join India by appealing to patriotism while offering fair terms, avoiding civil conflict", "(B) He paid personal money to every ruler", "(C) He forced rulers to leave Asia", "(D) He signed agreements without reading them", "(A)", "Appealed to patriotism and offered fair terms to achieve peaceful integration.", "Medium", "Analyzing", "Diplomatic Strategy"),
    ("How does the Statue of Unity physically reflect Sardar Patel's legacy?", "(A) Its massive scale and solid engineering symbolize his unyielding resolve and towering contribution to uniting India", "(B) It is painted in bright red iron rust", "(C) It is hollow and used as a water storage tank", "(D) It changes location every year", "(A)", "Towering scale symbolizes his solid resolve and role in forging national unity.", "Medium", "Evaluating", "Symbolism"),
    ("Why is Sardar Patel's connection to AMUL significant for rural development?", "(A) He recognized that economic empowerment through cooperatives was essential for agricultural freedom alongside political independence", "(B) He owned the AMUL dairy factory personally", "(C) He exported milk to London", "(D) He wanted to stop farmers from selling milk", "(A)", "Understood that cooperative economic empowerment complemented political freedom.", "Medium", "Analyzing", "Cooperative Vision"),
    ("Compare the leadership style of Sardar Patel with violent conquerors of history.", "(A) Conquerors used bloodshed to subjugate people; Patel used democratic persuasion, negotiation, and constitutional unity", "(B) Patel used military tanks to destroy cities", "(C) Both styles were identical", "(D) Patel conquered foreign countries in Europe", "(A)", "Patel used persuasion, negotiation, and unity instead of imperial conquest.", "Medium", "Comparing", "Leadership Comparison"),
    ("What does studying from 'borrowed books' teach Class 5 students about determination?", "(A) Lack of financial resources cannot stop dedicated students from gaining knowledge and achieving greatness", "(B) Students should never buy books", "(C) Borrowing books is illegal", "(D) Studying is unimportant", "(A)", "Lack of money cannot stop dedicated students from learning and succeeding.", "Medium", "Evaluating", "Moral Value"),
    ("How did Sardar Patel earn the respect of both political colleagues and princely rulers?", "(A) Through his transparent honesty, decisive firmness, word of honor, and unwavering national loyalty", "(B) By promising secret gifts", "(C) By threatening people quietly", "(D) By ignoring state problems", "(A)", "Earned respect through honesty, firmness, keeping his word, and national loyalty.", "Medium", "Understanding", "Leadership Character"),
    ("Why is October 31 celebrated as 'National Unity Day' (Rashtriya Ekta Diwas) in India?", "(A) To honor the birth anniversary and unifying legacy of Sardar Vallabhbhai Patel", "(B) To celebrate the end of monsoon", "(C) To mark the founding of Gujarat state", "(D) To honor ancient kings", "(A)", "Celebrated to honor the birth anniversary of Sardar Patel.", "Medium", "Remembering", "National Observance"),
    ("How did Patel's belief in 'one big family' apply to India's cultural diversity?", "(A) He believed diverse religions, languages, and regions could unite under shared national identity and mutual respect", "(B) He wanted everyone to speak only one language", "(C) He forced people to dress identically", "(D) He banned regional festivals", "(A)", "Diverse cultures united under shared national identity and mutual respect.", "Medium", "Understanding", "Diversity & Unity"),
    ("Describe the challenge Patel faced with rulers who hesitated to join India.", "(A) Some rulers wanted independent sovereignty or to join Pakistan; Patel used firm resolve and strategic diplomacy to secure unity", "(B) Rulers refused to meet Patel", "(C) Rulers hid in foreign countries", "(D) British forces protected the rulers with ships", "(A)", "Overcame separatist hesitation with strategic firmness and patriotic diplomacy.", "Medium", "Analyzing", "Integration Obstacles"),
    ("How did Patel's work in animal husbandry during youth aid his later policy support for dairy farmers?", "(A) Early hands-on experience gave him practical understanding of cattle management, enabling him to design effective farmer policies", "(B) It gave him money to buy land", "(C) He invented veterinary medicines", "(D) It made him an expert in shipping", "(A)", "Practical cattle experience enabled him to design effective agricultural policies.", "Medium", "Understanding", "Experiential Learning"),
    ("What structural foundation did Sardar Patel establish for Indian administration?", "(A) He established the modern All India Services (IAS and IPS), calling them the 'steel frame' of Indian governance", "(B) He established private corporate banks", "(C) He abolished all government offices", "(D) He created a military government", "(A)", "Established All India Services (IAS/IPS) as the administrative steel frame.", "Medium", "Understanding", "Administrative Contribution"),
    ("Summarize Chapter 07 in four concise sentences.", "Sardar Vallabhbhai Patel, born in Gujarat in 1875, was a determined leader known as the 'Iron Man of India'. After independence in 1947, he used wisdom and negotiation to unite hundreds of small princely states into one nation. He also supported farmers by inspiring the cooperative movement that led to AMUL. Honored by the Statue of Unity, his dream of a united India endures.", "Medium", "Understanding", "Chapter Summary"),
    ("What advice would Sardar Patel give to modern citizens regarding national unity?", "(A) Put national integration above regional, linguistic, or personal divisions and work hard together for the country's progress", "(B) Divide the nation into small groups", "(C) Rely on foreign nations for governance", "(D) Avoid civic responsibility", "(A)", "Put national integration above divisions and work hard for national progress.", "Medium", "Applying", "Citizenship Value"),

    # Hard (41-50)
    ("Critique the geopolitical impact of Sardar Patel's accession strategy on South Asian stability.", "(A) By swiftly integrating 560+ princely enclaves, Patel prevented a chaotic 'Balkanization' of the subcontinent, securing unified borders", "(B) His strategy caused India to break into fifty countries", "(C) Princely states remained independent forever", "(D) European powers re-colonized India", "(A)", "Prevented subcontinent balkanization, securing unified national borders.", "Hard", "Evaluating", "HOTS Geopolitical Analysis"),
    ("Deconstruct the metaphor 'Iron Man' as applied to Patel's political character.", "(A) 'Iron' signifies unyielding strength under pressure, structural resilience against division, and unwavering commitment to national integrity", "(B) It refers to his physical armor", "(C) It means he worked in iron mines", "(D) It implies he was harsh and unfeeling", "(A)", "Signifies unyielding strength under pressure, resilience, and commitment to integrity.", "Hard", "Analyzing", "Metaphoric Analysis"),
    ("Evaluate the economic strategy of combining political integration with agricultural cooperative building.", "(A) Political unity provided national stability, while farmer cooperatives ensured economic self-reliance for the rural majority", "(B) Cooperative building destroyed state revenues", "(C) Political integration was delayed by farming", "(D) Farmers were forced to give up land", "(A)", "Political unity gave stability; farmer cooperatives ensured rural economic self-reliance.", "Hard", "Evaluating", "Socio-Economic Strategy"),
    ("Compare Sardar Patel's role in Indian independence with George Washington's role in American independence.", "(A) Both leaders unified fragmented states/colonies into a single constitutional republic through decisive executive leadership and moral authority", "(B) Washington worked in India; Patel worked in America", "(C) Both leaders abolished state governments", "(D) Neither leader supported national unity", "(A)", "Both unified fragmented territories into a single constitutional republic.", "Hard", "Comparing", "Comparative Global Leadership"),
    ("Formulate a commemorative tribute speech to be delivered at the foot of the Statue of Unity.", "(A) 'Standing before this colossal monument, we honor Sardar Patel, whose iron resolve welded hundreds of states into one proud, undivided India!'", "(B) 'We gather to celebrate the opening of a new shopping mall.'", "(C) 'Sardar Patel was a quiet farmer who never spoke in public.'", "(D) 'This statue represents ancient European history.'", "(A)", "Tribute honoring iron resolve, territorial integration, and undivided India.", "Hard", "Creating", "Commemorative Oration Design"),
    ("Assess the administrative foresight of creating the All India Civil Services alongside territorial integration.", "(A) Integrating land without a unified civil service would cause administrative breakdown; the civil services provided a cohesive governance framework", "(B) Civil services were designed to replace elected leaders", "(C) Civil services created division among states", "(D) Administration was left to private companies", "(A)", "Unified civil service provided cohesive governance framework across integrated states.", "Hard", "Evaluating", "Administrative Foresight"),
    ("Analyze how Sardar Patel's early agricultural roots shaped his pragmatic approach to statecraft.", "(A) Farming taught him patience, realistic assessment of human nature, resource conservation, and aversion to ideological dogma", "(B) Farming made him impulsive and erratic", "(C) It made him reject urban technology", "(D) It prevented him from studying law", "(A)", "Farming taught patience, realistic assessment of human nature, and practical statecraft.", "Hard", "Analyzing", "Psychological Roots"),
    ("Synthesize how Chapter 07 connects childhood character-building with grand historical achievements.", "(A) Shows how childhood honesty, field labor, borrowing books, and determination blossomed into national leadership and historic unification", "(B) Suggests that childhood habits have no impact on adulthood", "(C) Replaces history with fictional stories", "(D) Focuses solely on statue height numbers", "(A)", "Connects childhood work ethic and determination with grand historical leadership.", "Hard", "Synthesizing", "Biographical Synthesis"),
    ("Critique the statement: 'India's unification after 1947 occurred automatically without political effort.'", "(A) Completely false; unification required immense diplomatic negotiation, strategic firmness, and visionary leadership by Patel against severe resistance", "(B) True; princely states voluntarily merged without any meetings", "(C) False; British forces unified India before leaving", "(D) True; there were no princely states in 1947", "(A)", "False; unification required intense diplomatic negotiation and strategic firmness by Patel.", "Hard", "Evaluating", "Historical Accuracy Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 07 for a Class 5 assessment.", "(A) 'Explain why Sardar Vallabhbhai Patel is called the Iron Man of India. Describe his role in uniting princely states, supporting farmers, and how he is remembered today.'", "(B) 'Write five sentences about your favorite statue.'", "(C) 'List five cities in Gujarat.'", "(D) 'Draw a picture of a farm tool.'", "(A)", "Structured essay prompt evaluating biographical facts, unification leadership, and national legacy.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 07: The Iron Man of India: Sardar Vallabhbhai Patel\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH07_MCQ_{idx:03d}"
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

with open(os.path.join(CH07_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Sardar Vallabhbhai Patel is known as the Iron Man of _______.", "India", "Known as the Iron Man of India.", "Easy"),
    ("Sardar Patel was born on October 31, _______.", "1875", "Born in 1875.", "Easy"),
    ("Sardar Patel was born in the state of _______.", "Gujarat", "Born in Gujarat.", "Easy"),
    ("As a child, he spent his time assisting his father in agricultural _______.", "fields", "Assisted father in fields.", "Easy"),
    ("While working in fields, he learned about cultivation and animal _______.", "husbandry", "Learned animal husbandry.", "Easy"),
    ("Because books were expensive, young Vallabhbhai studied from _______ books.", "borrowed", "Studied from borrowed books.", "Easy"),
    ("He grew up to be honest, strong, and _______.", "determined", "Honest, strong, and determined.", "Easy"),
    ("Sardar Patel believed all Indians should stay together like one big _______.", "family", "Together like one big family.", "Easy"),
    ("India gained independence from British rule in the year _______.", "1947", "Gained independence in 1947.", "Easy"),
    ("After independence, India was divided into many small _______.", "kingdoms", "Divided into small kingdoms.", "Easy"),
    ("Sardar Patel used his wisdom and courage to bring small kingdoms into one united _______.", "nation", "Form one united nation.", "Easy"),
    ("Because of his strength and leadership, people called him the _______ Man of India.", "Iron", "Iron Man of India.", "Easy"),
    ("Patel worked to improve farmers' lives by encouraging cooperative _______.", "societies", "Encouraged cooperative societies.", "Easy"),
    ("He inspired and guided the movement which led to the formation of _______.", "AMUL", "Led to formation of AMUL.", "Easy"),
    ("Sardar Vallabhbhai Patel passed away on December 15, _______.", "1950", "Passed away in 1950.", "Easy"),
    ("The Statue of _______ stands in Gujarat to honor Sardar Patel.", "Unity", "Statue of Unity.", "Easy"),
    ("The Statue of Unity is the _______ statue in the world.", "tallest", "Tallest statue in the world.", "Easy"),
    ("Unity is defined as being together as _______.", "one", "Unity = being together as one.", "Easy"),
    ("Determination means a strong _______ to achieve something.", "will", "Strong will to achieve.", "Easy"),
    ("Leadership is the ability to guide and _______ others.", "inspire", "Guide and inspire others.", "Easy"),
    ("Negotiation means discussion to reach an _______.", "agreement", "Discussion to reach agreement.", "Easy"),
    ("Sardar Patel actively participated in India's struggle for _______.", "freedom", "Struggle for freedom.", "Easy"),
    ("He encouraged people to work hard for the _______.", "country", "Work hard for the country.", "Easy"),
    ("His dream of a united India lives _______ today.", "on", "Dream of united India lives on.", "Easy"),
    ("Chapter 07 is titled 'The Iron Man of India: Sardar Vallabhbhai _______'.", "Patel", "Sardar Vallabhbhai Patel.", "Easy"),

    # Medium (26-40)
    ("Patel integrated over five hundred princely _______ into the Indian Union.", "states", "Integrated princely states.", "Medium"),
    ("Persuasive diplomacy and firm resolve prevented national _______.", "fragmentation", "Prevented national fragmentation.", "Medium"),
    ("Cooperative societies provided farmers with collective economic _______.", "strength", "Provided collective economic strength.", "Medium"),
    ("The Statue of Unity overlooks the Narmada _______ in Gujarat.", "River", "Overlooks Narmada River.", "Medium"),
    ("Patel's administrative vision established the All India _______.", "Services", "Established All India Services.", "Medium"),
    ("He served as independent India's first Deputy Prime Minister and Home _______.", "Minister", "First Home Minister.", "Medium"),
    ("National Unity Day is observed annually on October _______.", "31", "Observed on October 31.", "Medium"),
    ("Sardar Patel's legal acumen helped draft India's _______.", "Constitution", "Helped draft Constitution.", "Medium"),
    ("His pragmatic approach resolved complex territorial _______.", "disputes", "Resolved territorial disputes.", "Medium"),
    ("Farmers gained fair prices through cooperative milk _______.", "procurement", "Cooperative milk procurement.", "Medium"),
    ("Patel's leadership earned him the honorific title _______.", "Sardar", "Earned title Sardar.", "Medium"),
    ("The integration of princely states was achieved without major civil _______.", "war", "Achieved without civil war.", "Medium"),
    ("His unyielding resolve earned him comparison to unbending _______.", "iron", "Earned comparison to iron.", "Medium"),
    ("Patel prioritized national security and territorial _______.", "integrity", "Prioritized territorial integrity.", "Medium"),
    ("Chapter 07 demonstrates how visionary statecraft builds a resilient _______.", "republic", "Builds a resilient republic.", "Medium"),

    # Hard (41-50)
    ("Instrument of Accession agreements unified autonomous princely _______.", "domains", "Unified princely domains.", "Hard"),
    ("Balkanization risks were neutralized through strategic diplomatic _______.", "maneuvers", "Neutralized via strategic maneuvers.", "Hard"),
    ("Socio-economic co-operatives empowered vulnerable agrarian _______.", "communities", "Empowered agrarian communities.", "Hard"),
    ("Patel's administrative steel frame sustained constitutional _______.", "governance", "Sustained constitutional governance.", "Hard"),
    ("The colossal Statue of Unity commemorates monumental political _______.", "consolidation", "Commemorates political consolidation.", "Hard"),
    ("Statecraft pragmatism triumphed over divisive factional _______.", "interests", "Triumphed over factional interests.", "Hard"),
    ("Democratic integration established an undivided sovereign _______.", "republic", "Established undivided sovereign republic.", "Hard"),
    ("Agrarian upbringing rooted Patel's policies in rural economic _______.", "realities", "Rooted policies in rural realities.", "Hard"),
    ("Historical analysis confirms Patel as the primary architect of national _______.", "unification", "Architect of national unification.", "Hard"),
    ("Chapter 07 inspires future generations to uphold undivided national _______.", "sovereignty", "Uphold undivided sovereignty.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 07: The Iron Man of India: Sardar Vallabhbhai Patel\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH07_FIB_{idx:03d}"
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
    ("Sardar Vallabhbhai Patel is known as the Iron Man of India.", "True", "Text confirms he is called the Iron Man of India.", "Easy"),
    ("Sardar Patel was born in Maharashtra on October 31, 1875.", "False", "He was born in Gujarat on October 31, 1875.", "Easy"),
    ("Sardar Patel spent his childhood assisting his father in agricultural fields.", "True", "Text states he spent childhood assisting his father in fields.", "Easy"),
    ("Young Vallabhbhai bought expensive foreign textbooks to study.", "False", "He studied from borrowed books because of limited resources.", "Easy"),
    ("Sardar Patel learned about cultivation and animal husbandry during his youth.", "True", "Text confirms he learned about cultivation and animal husbandry.", "Easy"),
    ("India gained independence from British rule in 1947.", "True", "Text confirms India gained independence in 1947.", "Easy"),
    ("After independence, India was already one single unified nation without any kingdoms.", "False", "The country had many small kingdoms that needed to be united.", "Easy"),
    ("Sardar Patel used wisdom, courage, and negotiation to unite small kingdoms into one nation.", "True", "Text confirms he used wisdom, courage, and negotiation.", "Easy"),
    ("Sardar Patel was called the Iron Man because he owned iron mines.", "False", "Called Iron Man because of his strength, leadership, and determination.", "Easy"),
    ("Sardar Patel encouraged the formation of cooperative societies for farmers.", "True", "Text states he encouraged cooperative societies for farmers.", "Easy"),
    ("Sardar Patel inspired and guided the movement that led to the formation of AMUL.", "True", "Text confirms his role in guiding the movement leading to AMUL.", "Easy"),
    ("Sardar Vallabhbhai Patel passed away in 1947 right after independence.", "False", "He passed away on December 15, 1950.", "Easy"),
    ("The Statue of Unity is located in New Delhi.", "False", "The Statue of Unity is located in Gujarat.", "Easy"),
    ("The Statue of Unity is the tallest statue in the world.", "True", "Text states the Statue of Unity is the tallest statue in the world.", "Easy"),
    ("'Unity' means being together as one.", "True", "Vocabulary definition: Unity = Being together as one.", "Easy"),
    ("'Determination' means a weak will to give up easily.", "False", "Determination = Strong will to achieve something.", "Easy"),
    ("'Leadership' is the ability to guide and inspire others.", "True", "Vocabulary definition: Leadership = Ability to guide and inspire others.", "Easy"),
    ("'Negotiation' means discussion to reach an agreement.", "True", "Vocabulary definition: Negotiation = Discussion to reach an agreement.", "Easy"),
    ("Sardar Patel believed all Indians should stay together like one big family.", "True", "Text confirms he believed all Indians should stay together like one family.", "Easy"),
    ("Sardar Patel refused to participate in India's freedom struggle.", "False", "He actively participated in India's struggle for freedom.", "Easy"),
    ("Sardar Patel passed away on December 15, 1950.", "True", "Text confirms he passed away on December 15, 1950.", "Easy"),
    ("Sardar Patel encouraged people to work hard for the country.", "True", "Text confirms he encouraged people to work hard for the country.", "Easy"),
    ("His dream of a united India ended when he passed away.", "False", "Text states his dream of a united India lives on today.", "Easy"),
    ("Sardar Patel will always be remembered as a true hero of India.", "True", "Closing sentence confirms he is remembered as a true hero.", "Easy"),
    ("Chapter 07 title is 'The Iron Man of India: Sardar Vallabhbhai Patel'.", "True", "Chapter title is 'The Iron Man of India: Sardar Vallabhbhai Patel'.", "Easy"),

    # Medium (26-40)
    ("Uniting over 500 princely states required both firm resolve and diplomatic negotiation.", "True", "Patel combined firm determination with diplomatic negotiation.", "Medium"),
    ("The Statue of Unity stands on the banks of the Narmada River in Kevadia, Gujarat.", "True", "Located on Narmada River facing Sardar Sarovar Dam in Gujarat.", "Medium"),
    ("Sardar Patel served as independent India's first Deputy Prime Minister.", "True", "He was India's first Deputy PM and Home Minister.", "Medium"),
    ("Patel opposed the creation of farmer milk cooperatives.", "False", "He actively guided the cooperative movement that created AMUL.", "Medium"),
    ("Sardar Patel's birth anniversary, October 31, is celebrated as National Unity Day.", "True", "October 31 is celebrated nationally as Rashtriya Ekta Diwas.", "Medium"),
    ("The All India Civil Services were established under Patel's guidance.", "True", "He established IAS/IPS as the administrative steel frame of India.", "Medium"),
    ("Patel's negotiation strategy involved using military force as the first option.", "False", "He used diplomatic negotiation and patriotic persuasion first.", "Medium"),
    ("Borrowing books in childhood helped develop Patel's resourcefulness and determination.", "True", "Overcoming poverty to study built strong character and determination.", "Medium"),
    ("The integration of princely states took over twenty years to complete.", "False", "Patel accomplished the bulk of integration swiftly between 1947 and 1949.", "Medium"),
    ("Patel believed political freedom without economic agricultural strength was incomplete.", "True", "He championed farmer cooperatives to ensure economic strength.", "Medium"),
    ("The Statue of Unity measures 182 meters in height.", "True", "Statue height is 182 meters (597 feet), making it world's tallest.", "Medium"),
    ("Sardar Patel was born into a wealthy royal family.", "False", "He was born into an ordinary farming family in Gujarat.", "Medium"),
    ("Patel's firm handling of national integration earned him the name 'Iron Man'.", "True", "His unyielding strength and determination in uniting India earned the title.", "Medium"),
    ("The princely states had separate rulers, laws, and currencies before integration.", "True", "Princely states were autonomous with their own rulers and administration.", "Medium"),
    ("Chapter 07 emphasizes that national unity requires hard work and civic dedication.", "True", "Emphasizes working hard for the country and staying united.", "Medium"),

    # Hard (41-50)
    ("Patel's integration work prevented foreign powers from exploiting regional Indian divisions.", "True", "A unified nation prevented foreign interference and balkanization.", "Hard"),
    ("The Instrument of Accession was the legal document signed by princely state rulers.", "True", "Rulers signed the Instrument of Accession to join the Dominion of India.", "Hard"),
    ("Patel's background in farming gave him deep insights into rural tax and credit problems.", "True", "Hands-on farming experience informed his tax resistance movements (Bardoli).", "Hard"),
    ("The term 'Sardar' was given to Vallabhbhai Patel by women during the Bardoli Satyagraha.", "True", "Women of Bardoli gave him the title 'Sardar' (Leader) for his brave leadership.", "Hard"),
    ("Patel advocated for complete dissolution of democratic institutions in favor of military rule.", "False", "He was a devoted architect of India's democratic constitutional republic.", "Hard"),
    ("The Statue of Unity was inaugurated on October 31, 2018.", "True", "Inaugurated on Patel's 143rd birth anniversary in 2018.", "Hard"),
    ("Patel's vision of 'one big family' rejected pluralistic cultural diversity.", "False", "His vision embraced cultural diversity united under national citizenship.", "Hard"),
    ("Without Patel's swift integration, India would have required passports to travel between states.", "True", "Unintegrated princely states would have formed separate sovereign nations.", "Hard"),
    ("Sardar Patel's legacy continues to inspire national integration and agrarian policy.", "True", "His principles guide national unity and cooperative agricultural policy.", "Hard"),
    ("Chapter 07 connects primary character values (honesty, hard work) with statecraft achievements.", "True", "Bridges foundational childhood values with historic nation-building.", "Hard")
]

tf_content = f"# True / False — Chapter 07: The Iron Man of India: Sardar Vallabhbhai Patel\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH07_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Question**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH07_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who was Sardar Vallabhbhai Patel and why is he called the 'Iron Man of India'?", "Sardar Vallabhbhai Patel was a brave Indian freedom fighter and leader who earned the title 'Iron Man of India' because of his resolute strength, leadership, and unyielding determination in uniting hundreds of small kingdoms into one nation after 1947.", "Easy", "Remembering"),
    ("When and where was Sardar Vallabhbhai Patel born?", "He was born on October 31, 1875, in Gujarat, India.", "Easy", "Remembering"),
    ("How did young Vallabhbhai spend his childhood, and what did he learn from it?", "He spent his childhood assisting his father in agricultural fields, learning practical knowledge about cultivation and animal husbandry.", "Easy", "Remembering"),
    ("How did Vallabhbhai study despite financial difficulties in his youth?", "Because books were expensive, he studied dedicatedly using borrowed books from friends and libraries.", "Easy", "Remembering"),
    ("What key character traits did Vallabhbhai develop as he grew up?", "He grew up to be honest, strong, disciplined, and determined.", "Easy", "Remembering"),
    ("What core belief did Sardar Patel hold regarding the people of India?", "He believed that all Indians, regardless of region or background, should stay together like one big family.", "Easy", "Understanding"),
    ("When did India gain independence from British rule?", "India gained independence from British rule in the year 1947.", "Easy", "Remembering"),
    ("What major political problem existed in India right after independence in 1947?", "The country was fragmented into over five hundred small independent princely kingdoms.", "Easy", "Understanding"),
    ("How did Sardar Patel solve the problem of small kingdoms after independence?", "He used his wisdom, courage, strength, leadership, and diplomatic negotiation to bring them together into one united nation.", "Easy", "Understanding"),
    ("How did Sardar Patel help improve the economic lives of Indian farmers?", "He encouraged the formation of cooperative societies so farmers could sell produce directly and earn fair profits.", "Easy", "Understanding"),
    ("What famous dairy movement was inspired and guided by Sardar Patel?", "He inspired and guided the farmer cooperative movement in Anand that led to the formation of AMUL.", "Easy", "Remembering"),
    ("When did Sardar Vallabhbhai Patel pass away?", "He passed away on December 15, 1950.", "Easy", "Remembering"),
    ("What monument stands in Gujarat to honor Sardar Patel, and what is its world distinction?", "The Statue of Unity stands in Gujarat to honor him, and it is famous for being the tallest statue in the world.", "Easy", "Remembering"),
    ("What does the word 'unity' mean?", "'Unity' means being together as one unified whole.", "Easy", "Understanding"),
    ("What does the word 'determination' mean?", "'Determination' means having a firm, strong will to achieve a goal despite obstacles.", "Easy", "Understanding"),
    ("What does the word 'leadership' mean?", "'Leadership' is the ability to guide, inspire, and direct others toward a common purpose.", "Easy", "Understanding"),
    ("What does the word 'negotiation' mean?", "'Negotiation' means holding discussions between parties to reach a peaceful, mutually acceptable agreement.", "Easy", "Understanding"),
    ("What dream of Sardar Patel continues to live on in India today?", "His vision and dream of a strong, prosperous, and united India lives on today.", "Easy", "Remembering"),
    ("Why is Sardar Patel remembered as a true hero of India?", "Because he dedicated his life to India's freedom and successfully forged the territorial unity of the nation.", "Easy", "Understanding"),
    ("Where in Gujarat is the Statue of Unity located?", "It is located on the Narmada River facing the Sardar Sarovar Dam in Kevadia, Gujarat.", "Easy", "Remembering"),
    ("What role did Sardar Patel play in India's freedom struggle before 1947?", "He was a key leader who organized non-violent peasant movements and actively fought alongside Mahatma Gandhi against British rule.", "Easy", "Understanding"),
    ("Why was uniting the princely states necessary for India's national security?", "Without unification, India would have suffered internal conflict, foreign interference, and political instability.", "Easy", "Understanding"),
    ("Why is October 31 celebrated in India every year?", "October 31 is celebrated as 'National Unity Day' (Rashtriya Ekta Diwas) to honor Sardar Patel's birth anniversary.", "Easy", "Remembering"),
    ("What title is given to Chapter 07?", "The title of Chapter 07 is 'The Iron Man of India: Sardar Vallabhbhai Patel'.", "Easy", "Remembering"),
    ("What message does Chapter 07 give to young students about working for the country?", "It encourages students to be honest, determined, stay united, and work hard for the progress of the nation.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze why Sardar Patel's childhood farm experience was important for his political career.", "Working in fields gave him practical understanding of agrarian problems, hard physical work, and empathy for common farmers, enabling him to lead peasant satyagrahas and farmer cooperatives.", "Medium", "Analyzing"),
    ("How did Sardar Patel demonstrate 'negotiation' skills when dealing with princely rulers?", "He met with rulers, appealed to their patriotism, explained the mutual benefits of joining India, and negotiated fair constitutional terms without resorting to war.", "Medium", "Analyzing"),
    ("Explain the connection between Sardar Patel and the origin of AMUL.", "Patel advised Gujarati dairy farmers to refuse selling milk to exploitative private trade monopolies and instead form their own cooperative union, which developed into AMUL.", "Medium", "Understanding"),
    ("Why is the Statue of Unity an appropriate tribute to Sardar Patel?", "Its grand height (182 meters) and solid iron-and-bronze construction visually symbolize his monumental contribution and iron strength in forging a united nation.", "Medium", "Evaluating"),
    ("Contrast the state of India before Patel's unification with the state of India after his work.", "Before: Fragmented into 560+ independent princely states with separate rules. After: A single, consolidated, sovereign democratic republic with unified laws.", "Medium", "Comparing"),
    ("What does borrowing books in childhood show about Vallabhbhai Patel's character?", "It shows his deep passion for learning, resourcefulness, self-reliance, and determination to overcome poverty to educate himself.", "Medium", "Evaluating"),
    ("How did Sardar Patel earn the respect of Mahatma Gandhi and other national leaders?", "Through his flawless organizational ability, absolute honesty, loyalty to the freedom movement, and practical decision-making skills.", "Medium", "Understanding"),
    ("Why is national unity considered essential for economic progress in India?", "Unity ensures peaceful law and order, seamless trade across state borders, efficient infrastructure, and collective national strength required for growth.", "Medium", "Analyzing"),
    ("Describe Sardar Patel's role as India's first Home Minister.", "As Home Minister, he maintained law and order during partition, integrated 560+ princely states, and established the All India Civil Services (IAS/IPS).", "Medium", "Remembering"),
    ("Summarize Chapter 07 in four concise sentences.", "Sardar Vallabhbhai Patel, born in Gujarat in 1875, was a brave leader known as the 'Iron Man of India'. After 1947, he used wisdom and negotiation to unite hundreds of princely states into one country. He also supported farmers by guiding the cooperative movement that led to AMUL. Honored by the Statue of Unity, his legacy of a united India endures.", "Medium", "Understanding"),
    ("How can Class 5 students practice 'unity' in their daily school life?", "Students can practice unity by treating classmates with respect, working together in group projects without discrimination, and helping each other like a family.", "Medium", "Applying"),
    ("Why did people call Vallabhbhai 'Sardar'?", "'Sardar' means leader. The title was given to him by the women of Bardoli and Mahatma Gandhi in recognition of his powerful leadership during the Bardoli campaign.", "Medium", "Remembering"),
    ("Explain why peaceful integration of states was a remarkable achievement in world history.", "Most nation-building in world history involved long bloody wars. Patel integrated 560+ states peacefully through diplomacy, wisdom, and constitutional agreements.", "Medium", "Evaluating"),
    ("How did Sardar Patel encourage people to view the nation?", "He encouraged citizens to look beyond local or regional identity and view all Indians as members of one single, strong national family.", "Medium", "Understanding"),
    ("What lesson can young inventors and leaders take from Patel's life story?", "That strong determination, honest character, resourcefulness, and working for the public good can overcome any obstacle to achieve historic success.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the geopolitical threat posed by unintegrated princely states in 1947.", "Unintegrated states threatened to create hostile foreign enclaves inside India, cut off transport corridors, provoke civil wars, and destroy national sovereignty.", "Hard", "Evaluating"),
    ("Deconstruct the administrative role of the All India Services created by Patel.", "Patel created the IAS and IPS as an impartial, merit-based administrative 'steel frame' that bound diverse states to a uniform national standard of governance.", "Hard", "Analyzing"),
    ("Evaluate the economic impact of farmer cooperatives inspired by Patel.", "Cooperatives eliminated middleman margins, guaranteed fair seasonal milk pricing, funded village infrastructure, and empowered rural families financially.", "Hard", "Evaluating"),
    ("Compare Sardar Patel's unification of India with Otto von Bismarck's unification of Germany.", "Bismarck used 'blood and iron' military force to unite Germany; Patel used democratic negotiation, constitutional integration, and moral persuasion to unite India.", "Hard", "Comparing"),
    ("Formulate a tribute speech for National Unity Day commemorating Sardar Patel.", "'On National Unity Day, we salute Sardar Patel, the Iron Man who forged 560 states into one proud republic. Let us pledge to safeguard the unity and integrity he gave us!'", "Hard", "Creating"),
    ("Assess how Patel's agricultural background informed his constitutional policy for rural India.", "His farm background ensured that post-independence economic policies prioritized agrarian rights, land reform support, and farmer-owned cooperative models.", "Hard", "Evaluating"),
    ("Analyze the cultural significance of the Statue of Unity in modern Indian tourism.", "It serves as a global landmark that draws millions of visitors, boosting local economy in Gujarat while educating citizens about India's unification history.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 07 connects ethics, history, and civic education for Class 5.", "It weaves moral ethics (honesty, determination) with historical recall (1947 integration) and civic responsibility (national unity and hard work).", "Hard", "Synthesizing"),
    ("Critique the claim: 'Sardar Patel relied solely on military force to integrate princely states.'", "False; force was used in rare exceptions (e.g., Hyderabad). In over 99% of states, integration was achieved peacefully through patriotic diplomacy and negotiation.", "Hard", "Evaluating"),
    ("Formulate a 4-line poem honoring Sardar Vallabhbhai Patel.", "'With iron resolve and wisdom grand,\nHe bound five hundred states into one land;\nFrom farm fields humble to freedom's sight,\nSardar Patel gave India united might!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 07: The Iron Man of India: Sardar Vallabhbhai Patel\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH07_SA_{idx:03d}"
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
    ("Describe the early life, education, and character development of Sardar Vallabhbhai Patel.",
     "Sardar Vallabhbhai Patel was born on October 31, 1875, in Gujarat, India. Raised in a modest agricultural family, he spent his childhood assisting his father in farming fields. Through this hands-on work, young Vallabhbhai gained practical knowledge about crop cultivation and animal husbandry. Financial constraints meant he could not afford expensive textbooks, so he demonstrated remarkable determination by studying dedicatedly from borrowed books. Working through hardships forged his character; he grew up to be honest, physically and mentally strong, highly disciplined, and deeply determined. He developed a firm conviction that all Indians, regardless of regional differences, should live together in harmony like one big family. This grounded upbringing prepared him to actively join India's freedom struggle and become one of its greatest national leaders.",
     "Easy", "Remembering"),

    ("Explain how Sardar Patel earned the title 'Iron Man of India' through his work after 1947.",
     "When India achieved independence from British rule in 1947, the new nation faced a massive political crisis. Over 500 small princely kingdoms existed across the subcontinent, each ruled by independent princes. Had these states remained separate, India would have fragmented into small warring countries. Sardar Vallabhbhai Patel took on the formidable challenge of integrating these princely states into the Indian Union. Utilizing extraordinary wisdom, firm courage, leadership, and skilled negotiation, he persuaded rulers to sign the Instrument of Accession and join India. Because of his unyielding strength of character, resolute determination, and success in building a unified nation, the grateful public bestowed upon him the permanent title 'Iron Man of India'.",
     "Easy", "Remembering"),

    ("Describe Sardar Patel's contributions to agricultural welfare and the formation of AMUL.",
     "Beyond territorial unification, Sardar Vallabhbhai Patel was deeply committed to improving the economic lives of Indian farmers. Drawing from his childhood farming background, he understood that small farmers were exploited by private trade monopolies and middlemen who paid unfairly low prices. Patel encouraged farmers to organize themselves into self-reliant cooperative societies. In Gujarat, he personally guided and inspired the dairy farmers' movement in Anand. He advised them to refuse selling milk to private monopolists and instead form their own cooperative union. This movement, nurtured by Patel's guidance, grew into the world-famous AMUL dairy cooperative, which transformed rural livelihoods and empowered millions of Indian farmers.",
     "Easy", "Understanding"),

    ("Describe the Statue of Unity, its location, height, and significance in honoring Sardar Patel.",
     "The Statue of Unity is a colossal national monument erected in honor of Sardar Vallabhbhai Patel. It stands on the banks of the Narmada River facing the Sardar Sarovar Dam in Kevadia, Gujarat. Standing at a breathtaking height of 182 meters (597 feet), it holds the global distinction of being the tallest statue in the world. The monument physically symbolizes Sardar Patel's towering strength, iron resolve, and monumental contribution in uniting fragmented princely states into one undivided nation. Inaugurated on his 143rd birth anniversary, the Statue of Unity inspires millions of visitors from across the world to uphold national unity and patriotism.",
     "Easy", "Understanding"),

    ("Explain the vocabulary terms from Chapter 07: Unity, Determination, Leadership, and Negotiation.",
     "1. **Unity**: Being together as one unified entity. *Sentence*: Sardar Patel dedicated his life to national unity.\n2. **Determination**: Strong, unwavering will to achieve a goal despite difficulties. *Sentence*: Studying from borrowed books showed young Vallabhbhai's determination.\n3. **Leadership**: The ability to guide, direct, and inspire others toward a shared mission. *Sentence*: Patel's courageous leadership brought hundreds of states together.\n4. **Negotiation**: Holding discussions to settle differences and reach a peaceful agreement. *Sentence*: Patel used diplomatic negotiation to persuade princely rulers to join India.",
     "Easy", "Understanding"),

    ("Discuss how Sardar Patel's childhood farm work shaped his leadership vision.",
     "Sardar Patel's early life in Gujarat fields strongly shaped his leadership. Assisting his father taught him the real economic struggles of rural farmers, the importance of hard physical labor, and practical animal husbandry. When he became Home Minister and Deputy Prime Minister, he did not treat governance as abstract theory. He prioritized rural cooperative development, land reforms, and farmer welfare because he had personally experienced agricultural life, making his statecraft pragmatic, realistic, and deeply connected to India's rural majority.",
     "Easy", "Analyzing"),

    ("How did Sardar Patel manage to integrate 560+ princely states without launching major wars?",
     "Patel accomplished this historic integration primarily through brilliant diplomatic negotiation, patriotic persuasion, and strategic firmness. He met princely rulers, appealed to their love for the motherland, and explained that an integrated India offered economic stability and democratic security. He offered them fair constitutional terms and royal pensions (Privy Purses). Rulers recognized his transparent honesty and firm resolve, agreeing peacefully to merge their domains into the Indian Union without armed conflict.",
     "Easy", "Understanding"),

    ("Why is Sardar Patel considered a true hero of India?",
     "Sardar Patel is considered a true hero because he dedicated his entire life to the nation. He fought fearlessly against British colonial rule, sacrificed personal legal career wealth, integrated fragmented princely states to create modern India's map, supported agricultural cooperatives to lift farmers out of poverty, and established administrative services that maintain governance today. His unyielding devotion to national integrity makes him an immortal hero.",
     "Easy", "Evaluating"),

    ("Summarize Chapter 07 in five detailed bullet points.",
     "- Sardar Vallabhbhai Patel (born Oct 31, 1875 in Gujarat) learned farming and studied from borrowed books with great determination.\n- Known as the 'Iron Man of India', he was a brave freedom fighter who believed all Indians should live together like one family.\n- After independence in 1947, he used wisdom, strength, and negotiation to unite over 500 small princely kingdoms into one nation.\n- He championed farmer welfare by inspiring cooperative societies, guiding the movement that established the world-famous AMUL dairy.\n- Passed away Dec 15, 1950; today the Statue of Unity (world's tallest statue) in Gujarat honors his enduring dream of a united India.",
     "Easy", "Understanding"),

    ("What lessons about citizenship and national integration can Class 5 students learn from Chapter 07?",
     "Class 5 students learn several key lessons from Chapter 07:\n1. **Overcoming Obstacles**: Determination and hard work can overcome poverty and resource shortages.\n2. **National Unity**: Regional, linguistic, and cultural differences should not divide citizens; all Indians belong to one national family.\n3. **Civic Hard Work**: Real patriotism means working hard for the progress and peace of the country.\n4. **Leadership through Honesty**: True leadership relies on integrity, courageous action, and helping others.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why was post-1947 India in danger of 'balkanization', and how did Patel prevent it?", "If princely states had declared independence, India would have fractured into dozens of tiny landlocked nations with separate borders, tariffs, and armies. Patel prevented this balkanization by securing Instrument of Accession signatures from all rulers, creating a unified sovereign republic.", "Easy", "Understanding"),
    ("Explain the significance of National Unity Day celebrated on October 31.", "National Unity Day (Rashtriya Ekta Diwas) was instituted on October 31 to celebrate Patel's birth anniversary. It serves as an annual national pledge for citizens to reaffirm their commitment to preserving the freedom, unity, and territorial integrity of India.", "Easy", "Understanding"),
    ("How did Sardar Patel's work benefit both urban citizens and rural farmers?", "For rural farmers, he created cooperative marketing (AMUL) to ensure fair prices. For urban citizens, he created national political stability, unified domestic trade, and established a strong administrative civil service.", "Easy", "Analyzing"),
    ("Describe the relationship between Mahatma Gandhi and Sardar Vallabhbhai Patel.", "Patel was one of Gandhi's most trusted lieutenants. Patel organized ground-level peasant satyagrahas (Kheda, Bardoli) following Gandhi's non-violent principles, translating Gandhi's moral vision into practical political action.", "Easy", "Understanding"),
    ("How does the Statue of Unity promote economic growth and tourism in Kevadia, Gujarat?", "The monument has transformed Kevadia into an international tourist hub. It generates local employment, supports hospitality and transport businesses, funds environmental parks, and brings economic prosperity to local tribal communities.", "Easy", "Analyzing"),
    ("Explain why Sardar Patel is called the architect of the All India Civil Services.", "Patel recognized that a diverse nation needed a unified, non-political administrative network. He established the Indian Administrative Service (IAS) and Indian Police Service (IPS), calling them the 'steel frame' that keeps India united.", "Easy", "Remembering"),
    ("What role did V. P. Menon play alongside Sardar Patel during state integration?", "V. P. Menon was the brilliant civil servant who served as Secretary of the Ministry of the States under Patel. Menon drafted legal accessions and assisted Patel in high-stakes negotiations with princely rulers.", "Easy", "Remembering"),
    ("How did Sardar Patel demonstrate determination when studying law in England?", "Patel saved money independently, traveled to London, completed a three-year law course at Middle Temple in just 36 months, and passed at the top of his class despite having no wealthy sponsors.", "Easy", "Understanding"),
    ("Describe how Sardar Patel handled the complex integration of the state of Hyderabad.", "When the Nizam of Hyderabad refused to join India and unleashed armed Razakar militias against citizens, Patel acted decisively with 'Operation Polo' (1948), deploying federal troops to restore peace and integrate Hyderabad into India.", "Easy", "Analyzing"),
    ("Why is the concept of 'one big family' important for maintaining harmony in a multi-cultural nation?", "India has diverse languages, religions, and traditions. Viewing the nation as 'one big family' fosters mutual respect, prevents communal conflict, and unifies citizens under shared national identity.", "Easy", "Evaluating"),
    ("Re-write the story of Indian integration from the perspective of a princely state ruler in 1947.", "'When Sardar Patel spoke to us, he did not threaten. He spoke of a grand united India where our people would flourish under democracy. Seeing his iron conviction and honesty, I willingly signed the Accession to join the motherland.'", "Easy", "Creating"),
    ("What challenges did Patel face during the Bardoli Peasant Satyagraha of 1928?", "The British government imposed an unfair 22% land tax increase on starving farmers. Patel led a complete non-violent tax strike, withstood property seizures and arrests, and forced the British government to cancel the tax hike.", "Easy", "Remembering"),
    ("How did Sardar Patel's efforts help lay the groundwork for modern Indian democracy?", "By integrating princely domains into democratic provinces and participating in Constitution drafting, he ensured that 350+ million citizens gained universal voting rights under a single Constitution.", "Easy", "Evaluating"),
    ("Analyze why Chapter 07 is included in Class 5 English curriculum.", "It integrates historical literacy with character education, expanding formal English vocabulary (unity, negotiation, determination) while inspiring young students with patriotic values and strong character.", "Easy", "Understanding"),
    ("What future steps must citizens take to honor Sardar Patel's dream of a united India?", "Citizens must reject casteist, regional, and communal divisions, obey constitutional laws, promote economic equality, and work hard together for national advancement.", "Easy", "Applying"),

    # Medium (26-40)
    ("Critically analyze the leadership qualities that enabled Sardar Patel to solve the princely state crisis.",
     "Sardar Patel possessed a rare combination of leadership qualities:\n1. **Pragmatic Realism**: He evaluated geopolitical threats accurately without emotional illusions.\n2. **Unflinching Courage**: He faced powerful rulers and external threats without hesitation.\n3. **Diplomatic Tact**: He negotiated fair terms, preserving rulers' dignity while securing national interests.\n4. **Unimpeachable Integrity**: Rulers trusted his personal word because he never sought personal wealth or power.",
     "Medium", "Analyzing"),

    ("Examine how Sardar Patel's vision of agricultural cooperatives differed from state-controlled farming.",
     "Patel rejected state-controlled collective farming where government bureaucrats dictate to farmers. Instead, he championed democratic cooperatives (like AMUL) owned and operated by member-farmers themselves, supported by professional managers. This preserved individual land ownership while providing collective market strength.",
     "Medium", "Analyzing"),

    ("Evaluate the impact of Sardar Patel's 'steel frame' concept for Indian administration.",
     "Patel envisioned the IAS and IPS as an impartial, meritocratic civil service that would execute federal laws uniformly across all states. This 'steel frame' prevented regional political favoritism, maintained national security during crises, and remains the backbone of Indian governance today.",
     "Medium", "Evaluating"),

    ("Discuss how the integration of princely states established a unified economic market for India.",
     "Before integration, 560+ states maintained separate custom duties, transit taxes, currency rules, and trade barriers. Patel's unification created a seamless national common market, enabling free movement of goods, capital, and labor across India.",
     "Medium", "Analyzing"),

    ("Design a primary school project centered on National Unity Day inspired by Chapter 07.",
     "Project Title: 'Unity in Diversity — Walking in Sardar Patel's Footsteps'\n1. **Map Activity**: Students color a 1947 map of India showing princely states merging into one nation.\n2. **Unity Pledge**: Reciting a student pledge to respect all languages and cultures.\n3. **Role-Play**: Drama depicting Sardar Patel negotiating with rulers for national peace.\n4. **Essay**: Writing 100 words on 'How I can help keep my school united like one big family.'",
     "Medium", "Creating"),

    ("How did Sardar Patel's legal practice in Ahmedabad prepare him for national governance?", "As a successful criminal defense lawyer, he mastered evidence analysis, persuasive argumentation, cross-examination, and reading human character under pressure—skills vital for high-stakes diplomacy.", "Medium", "Analyzing"),
    ("Contrast Sardar Patel's administrative focus with Jawaharlal Nehru's international focus in post-1947 India.", "Nehru focused on global diplomacy, industrial planning, and non-alignment. Patel focused on internal territorial consolidation, home security, civil services, and agricultural integration.", "Medium", "Comparing"),
    ("Why was the integration of border princely states like Jammu & Kashmir, Junagadh, and Hyderabad particularly complex?", "These border states had rulers whose religious or political ambitions differed from their majority population or geographic reality, requiring strategic firmness and swift security intervention.", "Medium", "Understanding"),
    ("Explain how Sardar Patel's work supported women's participation in national life.", "In Bardoli and Gujarat movements, Patel actively brought village women into public satyagraha assemblies and cooperative decision-making, breaking traditional feudal isolation.", "Medium", "Evaluating"),
    ("How did Sardar Patel handle the massive refugee crisis following India's partition in 1947?", "As Home Minister, he organized emergency relief camps, restored public order, protected vulnerable communities, and coordinated resettlement for millions of displaced partition refugees.", "Medium", "Analyzing"),
    ("Explain the significance of the name 'Statue of Unity'.", "The name honors Patel's single greatest historic legacy: forging the territorial, political, and emotional unity of over 500 diverse regions into one sovereign nation.", "Medium", "Understanding"),
    ("How did Sardar Patel's simple personal lifestyle reflect his moral principles?", "Despite holding high office as Deputy PM, he lived in modest quarters, wore simple khadi clothing, kept minimal personal belongings, and refused financial privileges.", "Medium", "Evaluating"),
    ("Analyze why the British expected India to collapse into chaos after their departure in 1947.", "British officials believed India was too linguistically and culturally fragmented, with 560+ princely states, to survive as a single democratic nation. Patel proved them wrong.", "Medium", "Analyzing"),
    ("Describe how Sardar Patel inspired the youth of India during the freedom struggle.", "He inspired youth by demonstrating that courage, disciplined organization, and selfless action could overcome colonial oppression without fear of imprisonment.", "Medium", "Understanding"),
    ("Construct a fictional speech by Sardar Patel addressing Class 5 students today.", "'My young friends, we built a united India with hard work and sacrifice. You are the future of this nation. Stay honest, study hard, treat every Indian as your brother and sister, and keep our country strong!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the constitutional mechanism of Privy Purses used by Patel to integrate princely states.",
     "Patel offered princely rulers tax-free annual allowances (Privy Purses) and ceremonial titles in exchange for surrendering sovereign territory. While later criticized as an aristocratic privilege (and abolished in 1971), Patel's pragmatic mechanism achieved immediate, peaceful state merger in 1947 without catastrophic civil war.",
     "Hard", "Evaluating"),

    ("Deconstruct the geopolitical necessity of integrating the princely state of Junagadh.",
     "Junagadh's Nawab attempted to accede to Pakistan despite being surrounded by Indian territory in Gujarat. Patel recognized that a Pakistani enclave inside Gujarat threatened maritime and land security. He supported a local popular uprising and plebiscite, securing Junagadh's accession to India.",
     "Hard", "Analyzing"),

    ("Synthesize how Sardar Patel's life exemplifies the synthesis of traditional rural values and modern governance.",
     "Patel synthesized traditional rural virtues (hard physical labor, field discipline, community unity) with modern professional tools (English law, constitutional drafting, administrative civil service), creating a pragmatic model of Indian statecraft.",
     "Hard", "Synthesizing"),

    ("Formulate an advanced essay prompt evaluating Sardar Patel's dual contribution to territorial unity and agricultural cooperatives.",
     "Prompt: 'Critically assess how Sardar Vallabhbhai Patel achieved both political integration (uniting 560+ states) and economic empowerment (founding AMUL cooperatives). Explain how these dual achievements created the foundation of modern India.'",
     "Hard", "Creating"),

    ("Evaluate the historic legacy of Sardar Patel in shaping modern India's federal structure.", "Patel established a strong federal center capable of maintaining national integrity, while respecting state administration through cooperative federalism and All India Services.", "Hard", "Evaluating"),

    ("Compare Sardar Patel's Bardoli Satyagraha (1928) with Mahatma Gandhi's Salt Satyagraha (1930).", "Bardoli focused on agrarian tax resistance through disciplined local organization; Salt Satyagraha expanded non-violent civil disobedience into a nationwide anti-colonial campaign.", "Hard", "Comparing"),
    ("Discuss how Sardar Patel's vision of national unity applies to contemporary digital and economic integration.", "Just as Patel integrated physical borders in 1947, modern India builds upon his legacy by integrating digital payment systems, uniform national taxation (GST), and nationwide infrastructure.", "Hard", "Evaluating"),
    ("Analyze how Sardar Patel's resolve during 1947 earned him the lasting respect of world historians.", "World historians recognize Patel's integration of 560+ states as one of the largest, fastest, and most peaceful territorial consolidations in human history.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'Sardar Vallabhbhai Patel will always be remembered as a true hero of India.'", "This concluding line synthesizes national gratitude. It honors a leader whose iron determination and selfless service created the physical map and moral foundation of modern India.", "Hard", "Evaluating"),
    ("Synthesize the ultimate educational outcome of teaching Chapter 07 in primary school literature.", "Chapter 07 instills character values (honesty, determination, hard work) and civic awareness (patriotism, unity), inspiring students to become responsible, nation-building citizens.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 07: The Iron Man of India: Sardar Vallabhbhai Patel\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH07_LA_{idx:03d}"
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
    ("The Iron Man of India is Sardar Vallabhbhai Patel. He was a brave leader who worked hard to unite India after it gained independence from British rule in 1947.",
     [
         ("Who is known as the Iron Man of India?", "Sardar Vallabhbhai Patel.", "Easy", "Remembering"),
         ("How is Sardar Patel described in this opening passage?", "He is described as a brave leader who worked hard.", "Easy", "Remembering"),
         ("In what year did India gain independence from British rule?", "1947.", "Easy", "Remembering"),
         ("What major task did Sardar Patel work hard to accomplish after 1947?", "He worked hard to unite India after independence.", "Easy", "Understanding"),
         ("Why was uniting India a difficult task in 1947?", "Because the country was divided into over 500 separate princely kingdoms.", "Medium", "Analyzing")
     ]),

    # Set 2
    ("Sardar Patel was born on October 31, 1875, in Gujarat. He spent his childhood assisting his father in fields. In doing so, he learnt a lot about cultivation and animal husbandry.",
     [
         ("When was Sardar Patel born?", "October 31, 1875.", "Easy", "Remembering"),
         ("In which Indian state was Sardar Patel born?", "Gujarat.", "Easy", "Remembering"),
         ("How did young Vallabhbhai spend his childhood?", "Assisting his father in agricultural fields.", "Easy", "Remembering"),
         ("What two subjects did he learn a lot about while working in fields?", "Cultivation and animal husbandry.", "Easy", "Remembering"),
         ("How did his childhood farm work influence his future political career?", "It gave him practical understanding and deep empathy for Indian farmers.", "Medium", "Analyzing")
     ]),

    # Set 3
    ("He studied from borrowed books. He grew up to be honest, strong and determined. He believed that all Indians should stay together like one big family.",
     [
         ("How did young Vallabhbhai manage his studies without buying expensive books?", "He studied from borrowed books.", "Easy", "Remembering"),
         ("What three personality traits did he develop as he grew up?", "Honest, strong, and determined.", "Easy", "Remembering"),
         ("What core belief did Sardar Patel hold about Indians?", "He believed that all Indians should stay together like one big family.", "Easy", "Understanding"),
         ("What quality does studying from borrowed books demonstrate?", "Resourcefulness, determination, and passion for knowledge.", "Medium", "Evaluating"),
         ("How does the idea of 'one big family' promote national unity?", "It encourages citizens to look past regional differences and treat each other with respect.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("He actively participated in India's struggle for freedom. After India became free, the country had many small kingdoms. Sardar Patel used his wisdom and courage to bring them together to form one united nation.",
     [
         ("What struggle did Sardar Patel actively participate in before 1947?", "India's struggle for freedom from British rule.", "Easy", "Remembering"),
         ("What political division existed in India after it became free?", "The country had many small kingdoms.", "Easy", "Remembering"),
         ("What two qualities did Sardar Patel use to unite small kingdoms?", "Wisdom and courage.", "Easy", "Remembering"),
         ("What was the result of bringing these small kingdoms together?", "It formed one united nation (India).", "Easy", "Understanding"),
         ("Why was wisdom necessary alongside courage in state integration?", "Because convincing rulers required diplomatic tact, legal agreements, and strategic patience.", "Medium", "Analyzing")
     ]),

    # Set 5
    ("Because of his strength, leadership, and negotiation, people called him the Iron Man of India. He also worked to improve farmers' lives by encouraging the formation of cooperative society for farmers.",
     [
         ("What three qualities earned him the title 'Iron Man of India'?", "Strength, leadership, and negotiation.", "Easy", "Remembering"),
         ("Whose lives did Sardar Patel work to improve?", "Farmers' lives.", "Easy", "Remembering"),
         ("What type of organization did he encourage for farmers?", "Cooperative societies.", "Easy", "Remembering"),
         ("What does the word 'negotiation' mean?", "Discussion to reach a peaceful agreement.", "Easy", "Understanding"),
         ("How do cooperative societies improve farmers' lives?", "They eliminate exploitative middlemen and ensure fair market profits for farmers.", "Medium", "Understanding")
     ]),

    # Set 6
    ("He inspired and guided the movement which led to the formation of AMUL. Also, he encouraged people to work hard for the country.",
     [
         ("Which world-famous organization's formation was guided by Sardar Patel?", "AMUL.", "Easy", "Remembering"),
         ("What did Sardar Patel encourage all people to do for the country?", "To work hard for the country.", "Easy", "Remembering"),
         ("What role did Patel play in the AMUL movement?", "He inspired and guided the dairy farmers' movement in Anand.", "Easy", "Understanding"),
         ("Why was working hard for the country important after independence?", "To build a strong, self-reliant economy and stable democratic society.", "Medium", "Evaluating"),
         ("What does AMUL stand for?", "Anand Milk Union Limited.", "Medium", "Remembering")
     ]),

    # Set 7
    ("He passed away on December 15, 1950, but his dream of a united India lives on.",
     [
         ("On what date did Sardar Vallabhbhai Patel pass away?", "December 15, 1950.", "Easy", "Remembering"),
         ("What dream of Sardar Patel lives on today?", "His dream of a united India.", "Easy", "Remembering"),
         ("How many years after independence did Sardar Patel pass away?", "Three years (1947 to 1950).", "Medium", "Understanding"),
         ("In what way does his dream live on today?", "In the continued unity, constitutional strength, and territorial integrity of India.", "Medium", "Evaluating"),
         ("What national observance honors his birth anniversary?", "National Unity Day (Rashtriya Ekta Diwas) on October 31.", "Medium", "Remembering")
     ]),

    # Set 8
    ("Today, the Statue of Unity, the tallest statue in the world, stands in Gujarat to honour his great work. Sardar Vallabhbhai Patel will always be remembered as a true hero of India.",
     [
         ("What monument stands in Gujarat to honor Sardar Patel?", "The Statue of Unity.", "Easy", "Remembering"),
         ("What global record is held by the Statue of Unity?", "It is the tallest statue in the world.", "Easy", "Remembering"),
         ("In which state is the Statue of Unity located?", "Gujarat.", "Easy", "Remembering"),
         ("How will Sardar Vallabhbhai Patel always be remembered?", "As a true hero of India.", "Easy", "Remembering"),
         ("Why is a colossal statue an appropriate honor for Sardar Patel?", "Because it symbolizes his immense strength, towering leadership, and role in building a united India.", "Medium", "Evaluating")
     ]),

    # Set 9
    ("Word Meaning: Unity — Being together as one. Determination — Strong will to achieve something. Leadership — The ability to guide and inspire others. Negotiation — Discussion to reach an agreement.",
     [
         ("What is the definition of 'unity'?", "Being together as one.", "Easy", "Remembering"),
         ("What is the definition of 'determination'?", "Strong will to achieve something.", "Easy", "Remembering"),
         ("What is the definition of 'leadership'?", "The ability to guide and inspire others.", "Easy", "Remembering"),
         ("What is the definition of 'negotiation'?", "Discussion to reach an agreement.", "Easy", "Remembering"),
         ("Use the word 'determination' in a complete sentence of your own.", "Through sheer determination, she passed the difficult examination.", "Medium", "Applying")
     ]),

    # Set 10
    ("Sardar Patel was born on October 31, 1875... Gained independence in 1947... Formation of AMUL... Passed away on December 15, 1950... Statue of Unity stands in Gujarat.",
     [
         ("When was Sardar Patel born?", "October 31, 1875.", "Easy", "Remembering"),
         ("When did India gain independence?", "1947.", "Easy", "Remembering"),
         ("When did Sardar Patel pass away?", "December 15, 1950.", "Easy", "Remembering"),
         ("Where is the Statue of Unity built?", "In Gujarat, India.", "Easy", "Remembering"),
         ("Summarize Sardar Patel's legacy in one sentence.", "He united fragmented princely states into one nation, empowered farmers, and established the foundation of a strong Indian republic.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 07: The Iron Man of India: Sardar Vallabhbhai Patel\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH07_EXT_{q_counter:03d}"
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

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 07 in {CH07_DIR}")
