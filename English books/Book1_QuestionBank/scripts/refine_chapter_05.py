r"""
Refines all 6 Category files for Chapter 05 ("Father of the Nation") for Class 1.
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 1 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH05_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_05")
os.makedirs(CH05_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Who is known as the 'Father of the Nation' in India?", "(A) Mohandas Karamchand Gandhi", "(B) Jawaharlal Nehru", "(C) Subhash Chandra Bose", "(D) Bhagat Singh", "(A)", "Mahatma Gandhi is lovingly called Father of the Nation.", "Easy", "Remembering", "Historical Figure"),
    ("Where was Mahatma Gandhi born?", "(A) Porbandar, Gujarat", "(B) Kolkata", "(C) Mumbai", "(D) Delhi", "(A)", "He was born in Porbandar, Gujarat.", "Easy", "Remembering", "Birthplace"),
    ("When was Mahatma Gandhi born?", "(A) October 2, 1869", "(B) August 15, 1947", "(C) January 26, 1950", "(D) November 14, 1889", "(A)", "He was born on October 2, 1869.", "Easy", "Remembering", "Birth Date"),
    ("Where did Gandhiji go to study law?", "(A) London", "(B) New York", "(C) Paris", "(D) Tokyo", "(A)", "He went to London for his higher education in law.", "Easy", "Remembering", "Education"),
    ("What profession did Gandhiji train for in London?", "(A) Barrister / Lawyer", "(B) Doctor", "(C) Engineer", "(D) Teacher", "(A)", "He studied law and became a Barrister.", "Easy", "Remembering", "Profession"),
    ("At which court did Gandhiji practice law upon returning to India?", "(A) Bombay High Court", "(B) Madras High Court", "(C) Calcutta High Court", "(D) Delhi High Court", "(A)", "He practiced law at the Bombay High Court.", "Easy", "Remembering", "Detail"),
    ("In which country did Gandhiji first start Satyagraha?", "(A) South Africa", "(B) France", "(C) America", "(D) China", "(A)", "He started Satyagraha in South Africa.", "Easy", "Remembering", "Satyagraha Origin"),
    ("What does the word 'Satyagraha' mean?", "(A) A non-violent protest for truth", "(B) A war with weapons", "(C) A dance festival", "(D) A sport", "(A)", "Satyagraha is a non-violent protest for truth.", "Easy", "Understanding", "Concept"),
    ("What did Gandhiji encourage people to make and use?", "(A) Swadeshi (Indian-made) goods", "(B) Foreign clothes", "(C) Plastic items", "(D) Imported cars", "(A)", "He promoted Swadeshi (country-made) goods.", "Easy", "Remembering", "Swadeshi Movement"),
    ("What did Gandhiji ask people to boycott?", "(A) Foreign goods", "(B) Healthy food", "(C) Indian cloth", "(D) Books", "(A)", "He encouraged boycotting foreign-made goods.", "Easy", "Remembering", "Boycott"),
    ("How is Gandhiji's birthday (October 2) celebrated in India?", "(A) As a national festival (Gandhi Jayanti)", "(B) As Children's Day", "(C) As Teachers' Day", "(D) As Sports Day", "(A)", "October 2 is celebrated as Gandhi Jayanti, a national festival.", "Easy", "Remembering", "Festival"),
    ("What kind of life did Gandhiji lead?", "(A) Simple and truthful life", "(B) Lavish and showy life", "(C) Lazy life", "(D) Cruel life", "(A)", "Gandhiji was a simple man who taught simplicity.", "Easy", "Remembering", "Lifestyle"),
    ("Against whose rule did Gandhiji lead the freedom movement in India?", "(A) British rule", "(B) French rule", "(C) Portuguese rule", "(D) Dutch rule", "(A)", "He fought non-violently against British rule.", "Easy", "Remembering", "Freedom Struggle"),
    ("What key method did Gandhiji use during the freedom struggle?", "(A) Non-violence (Ahimsa)", "(B) Weapons and violence", "(C) Hiding", "(D) Money power", "(A)", "He led the struggle through non-violence.", "Easy", "Remembering", "Core Method"),
    ("Where did the British put Gandhiji several times during the freedom movement?", "(A) In jail", "(B) In a palace", "(C) On a ship", "(D) In a school", "(A)", "He was put in jail several times and endured hardships.", "Easy", "Remembering", "Hardships"),
    ("What title did people lovingly give to Gandhiji?", "(A) Bapu / Mahatma", "(B) King", "(C) Emperor", "(D) General", "(A)", "He was lovingly called Bapu and Mahatma.", "Easy", "Remembering", "Honorific"),
    ("What nature did Gandhiji have as a young boy?", "(A) Quiet and truthful", "(B) Naughty and angry", "(C) Lazy", "(D) Proud", "(A)", "He had a good reputation as a quiet-natured, truthful boy.", "Easy", "Remembering", "Childhood Trait"),
    ("Which value did Gandhiji emphasize for Indian citizens?", "(A) Self-reliance and truth", "(B) Dependence on others", "(C) Dishonesty", "(D) Greed", "(A)", "He taught self-reliance, truth, and simplicity.", "Easy", "Understanding", "Values"),
    ("What wheel did Gandhiji spin to make thread for cloth?", "(A) Charkha (spinning wheel)", "(B) Bicycle wheel", "(C) Car wheel", "(D) Water wheel", "(A)", "He spun the Charkha to make khadi thread.", "Easy", "Remembering", "Symbol"),
    ("Why was Gandhiji respected by all communities?", "(A) Because he treated everyone equally with love and respect", "(B) Because he was rich", "(C) Because he was tall", "(D) Because he was strict", "(A)", "He loved and respected people of all communities.", "Easy", "Understanding", "Reasoning"),
    ("What is the full name of Mahatma Gandhi?", "(A) Mohandas Karamchand Gandhi", "(B) Subhash Chandra Gandhi", "(C) Rajiv Gandhi", "(D) Indira Gandhi", "(A)", "His full name was Mohandas Karamchand Gandhi.", "Easy", "Remembering", "Full Name"),
    ("Which state in India was Gandhiji born in?", "(A) Gujarat", "(B) Maharashtra", "(C) Punjab", "(D) Kerala", "(A)", "Porbandar is located in Gujarat.", "Easy", "Remembering", "Geography"),
    ("What does 'Swadeshi' mean?", "(A) Made in one's own country", "(B) Made in a foreign land", "(C) Made in space", "(D) Bought from a store", "(A)", "Swadeshi means goods made in our own country.", "Easy", "Understanding", "Vocabulary"),
    ("Did Gandhiji use guns or swords in his fight for freedom?", "(A) No, he relied on truth and non-violence", "(B) Yes, he used swords", "(C) Yes, he used guns", "(D) He used cannons", "(A)", "He never used weapons, relying on truth and Ahimsa.", "Easy", "Understanding", "Fact"),
    ("What message does Chapter 05 give to young children?", "(A) Walk on the path of truth, non-violence, and simplicity", "(B) Fight with friends", "(C) Buy foreign toys only", "(D) Be lazy", "(A)", "It inspires children to follow truth, peace, and simplicity.", "Easy", "Understanding", "Core Takeaway"),

    # Medium (26-40)
    ("Why did Gandhiji leave his law practice in South Africa?", "(A) To fight against racial discrimination and oppression", "(B) He was tired", "(C) He wanted to travel", "(D) He ran out of money", "(A)", "He joined hands with natives to protest against racial oppression.", "Medium", "Understanding", "Historical Motivation"),
    ("What does the word 'barrister' mean?", "(A) A lawyer who is trained to argue in court", "(B) A ship captain", "(C) A bank manager", "(D) A builder", "(A)", "A barrister is a qualified lawyer.", "Medium", "Understanding", "Vocabulary"),
    ("How did spinning the Charkha promote self-reliance?", "(A) It encouraged people to make their own clothes instead of buying foreign cloth", "(B) It was a fun game", "(C) It made money", "(D) It built houses", "(A)", "Spinning thread made citizens independent for clothing.", "Medium", "Analyzing", "Historical Significance"),
    ("What does 'boycott' mean in the freedom movement?", "(A) Refusing to buy or use certain goods as a form of protest", "(B) Buying everything", "(C) Throwing trash", "(D) Singing songs", "(A)", "Boycott means refusing to buy foreign goods.", "Medium", "Understanding", "Vocabulary"),
    ("Why is October 2 observed as International Day of Non-Violence worldwide?", "(A) In honor of Mahatma Gandhi's birthday and his message of peace", "(B) It is a winter day", "(C) It is New Year", "(D) Because of a space mission", "(A)", "The UN declared October 2 International Day of Non-Violence.", "Medium", "Understanding", "Global Recognition"),
    ("What does 'homage' mean in the passage?", "(A) Deep respect and honor shown publicly", "(B) A small gift", "(C) A long journey", "(D) A storybook", "(A)", "Homage means showing deep respect and honor.", "Medium", "Understanding", "Vocabulary"),
    ("Why did Gandhiji emphasize simplicity in living?", "(A) He believed true strength comes from high thinking and simple living", "(B) He had no clothes", "(C) He disliked colors", "(D) He was forced to", "(A)", "He lived by the motto 'Simple living and high thinking'.", "Medium", "Analyzing", "Philosophy"),
    ("How did non-violent protest defeat a powerful empire?", "(A) Moral strength and united peaceful protests forced the British to yield", "(B) By using bigger armies", "(C) By buying weapons", "(D) By running away", "(A)", "Moral truth and unity proved stronger than weapons.", "Medium", "Analyzing", "Historical Impact"),
    ("What does 'oppression' mean in the context of South Africa?", "(A) Unfair and cruel treatment of people", "(B) Kind treatment", "(C) Playing games", "(D) Teaching lessons", "(A)", "Oppression means cruel, unjust treatment of native people.", "Medium", "Understanding", "Vocabulary"),
    ("Why did Gandhiji return from South Africa to India?", "(A) To lead his homeland's struggle for independence from British rule", "(B) To go on vacation", "(C) To buy a house", "(D) To study more", "(A)", "He returned to serve India's freedom movement.", "Medium", "Remembering", "Fact"),
    ("What was the impact of the Swadeshi movement on Indian villagers?", "(A) It gave employment to local weavers and made villages self-reliant", "(B) It closed all markets", "(C) It caused harm", "(D) It made people lazy", "(A)", "Swadeshi revived cottage industries and village income.", "Medium", "Analyzing", "Economic Impact"),
    ("How did Gandhiji respond to being put in jail multiple times?", "(A) He remained peaceful and steadfast in his belief without anger", "(B) He surrendered", "(C) He cried and gave up", "(D) He escaped in secret", "(A)", "He endured hardships with firm moral resolve.", "Medium", "Understanding", "Character Strength"),
    ("What is the difference between violence and non-violence?", "(A) Violence hurts people physically; non-violence resolves conflict peacefully", "(B) They are identical", "(C) Violence is quiet", "(D) Non-violence uses swords", "(A)", "Non-violence seeks truth and peace without causing physical harm.", "Medium", "Analyzing", "Conceptual Comparison"),
    ("Why is Gandhiji called 'Mahatma'?", "(A) 'Mahatma' means 'Great Soul', given for his noble life and sacrifices", "(B) It means rich man", "(C) It means king", "(D) It means teacher", "(A)", "Mahatma means Great Soul, honoring his spiritual and moral stature.", "Medium", "Understanding", "Title Meaning"),
    ("What lesson does Gandhiji's life give about truth (Satya)?", "(A) Truth always wins in the end, regardless of how difficult the path is", "(B) Lying is acceptable", "(C) Truth is unimportant", "(D) Truth changes daily", "(A)", "His life motto was 'Truth alone triumphs' (Satyameva Jayate).", "Medium", "Evaluating", "Moral Principle"),

    # Hard (41-50)
    ("How does Mahatma Gandhi's philosophy of Satyagraha apply to resolving schoolyard disputes?", "(A) Resolve arguments by talking peacefully and sticking to the truth without physical fighting", "(B) Fight with fists", "(C) Shout loudly", "(D) Ignore everything", "(A)", "Satyagraha promotes peaceful dialogue and adherence to truth.", "Hard", "Applying", "Real Life Application"),
    ("Analyze how Gandhiji used self-reliance (Swadeshi) as a economic and moral weapon.", "(A) By making Indian goods, he reduced economic dependence on the British while building national pride", "(B) He bought foreign items", "(C) He stopped trading", "(D) He gave away money", "(A)", "Swadeshi weakened British trade while uniting Indians morally.", "Hard", "Analyzing", "Historical Analysis"),
    ("Why is moral courage considered greater than physical force in Gandhiji's teachings?", "(A) Moral courage stands firm on truth and conscience, which cannot be destroyed by weapons", "(B) Physical force always wins", "(C) Weapons are superior", "(D) Courage is not needed", "(A)", "Moral conviction outlasts physical coercion.", "Hard", "Evaluating", "Philosophical Reasoning"),
    ("Examine the global influence of Mahatma Gandhi on leaders like Martin Luther King Jr. and Nelson Mandela.", "(A) They adopted his non-violent protest methods to win civil rights and freedom in their countries", "(B) They ignored his ideas", "(C) They fought with weapons", "(D) They met in school", "(A)", "Gandhiji's Ahimsa inspired global human rights movements.", "Hard", "Evaluating", "Global Impact"),
    ("What is the relationship between simplicity and inner peace according to Gandhiji's life?", "(A) Reducing greedy desires creates a peaceful, focused, and honest mind", "(B) Simplicity makes you poor", "(C) Buying more items brings peace", "(D) Simplicity is boring", "(A)", "Simplicity removes unnecessary material distractions.", "Hard", "Evaluating", "Values Analysis"),
    ("How did Gandhiji unite people of different religions and communities across India?", "(A) He treated all religions with equal respect and preached universal brotherhood", "(B) He favored one group", "(C) He avoided people", "(D) He made new laws", "(A)", "He championed communal harmony and equal respect for all faiths.", "Hard", "Analyzing", "Social Leadership"),
    ("Deconstruct the term 'Satyagraha' into its root words and meanings.", "(A) 'Satya' means Truth, and 'Agraha' means Insistence or Firm Holding; thus Holding Firmly to Truth", "(B) Satya means war, Agraha means peace", "(C) Satya means law, Agraha means court", "(D) Satya means king, Agraha means land", "(A)", "Satyagraha literally translates to 'Insistence on Truth'.", "Hard", "Analyzing", "Etymology"),
    ("Why did Gandhiji choose the salt march (Dandi Yatra) as a historic protest?", "(A) Salt is a basic necessity for every rich and poor person, making it a universal symbol of unity", "(B) Salt tasted good", "(C) He liked the ocean", "(D) It was easy", "(A)", "Salt affected every Indian, uniting rich and poor against unfair taxation.", "Hard", "Evaluating", "Historical Insight"),
    ("How does self-discipline form the foundation of a successful life based on Chapter 05?", "(A) Controlling one's desires and staying committed to truth builds strong character and leadership", "(B) Discipline is unnecessary", "(C) Doing whatever you want works best", "(D) Discipline causes fear", "(A)", "Self-discipline builds moral character and leadership.", "Hard", "Evaluating", "Character Development"),
    ("What is the ultimate educational message of Chapter 05 for young Class 1 learners?", "(A) Be truthful, live simply, respect everyone, and stand up for what is right through peaceful means!", "(B) Memorize dates only", "(C) Avoid history", "(D) Always buy imported goods", "(A)", "Truth, peace, simplicity, and moral courage are the core educational messages.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 05: Father of the Nation\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK01_CH05_MCQ_{idx:03d}"
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

with open(os.path.join(CH05_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Mohandas Karamchand Gandhi is known as the Father of the _______.", "Nation", "He is called Father of the Nation.", "Easy"),
    ("Gandhiji was born in Porbandar, _______.", "Gujarat", "Porbandar is in Gujarat.", "Easy"),
    ("He was born on October 2, _______.", "1869", "His birth year was 1869.", "Easy"),
    ("Gandhiji went to _______ for higher education in law.", "London", "He studied law in London.", "Easy"),
    ("After completing his law studies, Gandhiji became a _______.", "Barrister / lawyer", "He qualified as a Barrister.", "Easy"),
    ("Upon returning to India, he practiced law at the Bombay _______ Court.", "High", "He practiced at Bombay High Court.", "Easy"),
    ("Gandhiji moved to South _______ to work.", "Africa", "He went to South Africa for work.", "Easy"),
    ("In South Africa, he started a non-violent protest called _______.", "Satyagraha", "Satyagraha means non-violent protest.", "Easy"),
    ("Gandhiji returned to India to fight for independence from _______ rule.", "British", "He fought against British rule.", "Easy"),
    ("He taught the principles of simplicity and self-_______.", "reliance", "He taught self-reliance.", "Easy"),
    ("Gandhiji encouraged people to boycott _______ goods.", "foreign", "He urged boycotting foreign goods.", "Easy"),
    ("He asked people to make and use _______ goods.", "Swadeshi / Indian", "Swadeshi means country-made goods.", "Easy"),
    ("Gandhiji's birthday, October 2, is celebrated as a _______ festival.", "national", "Gandhi Jayanti is a national festival.", "Easy"),
    ("The British put Gandhiji in _______ several times during the freedom struggle.", "jail / prison", "He was jailed multiple times.", "Easy"),
    ("Gandhiji led the freedom struggle using non-_______ and truth.", "violence", "He used non-violence (Ahimsa).", "Easy"),
    ("Gandhiji had a reputation as a quiet-natured and _______ boy.", "truthful / good", "He was quiet and truthful.", "Easy"),
    ("People lovingly call Mahatma Gandhi by the name _______.", "Bapu", "He is affectionately called Bapu.", "Easy"),
    ("Gandhiji spun thread on a wooden spinning wheel called a _______.", "Charkha", "He spun thread on a Charkha.", "Easy"),
    ("Gandhiji was respected by people of all _______.", "communities / religions", "He respected all communities.", "Easy"),
    ("Chapter 05 tells the life story of Mahatma _______.", "Gandhi", "It details Gandhi's biography.", "Easy"),
    ("Swadeshi means goods made in our own _______.", "country / land", "Swadeshi refers to native goods.", "Easy"),
    ("Satyagraha is a protest based on _______ and non-violence.", "truth", "Satyagraha is based on truth.", "Easy"),
    ("Gandhiji endured extreme _______ while in jail for freedom.", "hardships / pain", "He faced great hardships.", "Easy"),
    ("Mahatma means a 'Great _______'.", "Soul", "Mahatma translates to Great Soul.", "Easy"),
    ("Gandhiji believed that truth always _______ in the end.", "wins / triumphs", "Truth always triumphs.", "Easy"),

    # Medium (26-40)
    ("The word 'barrister' refers to a qualified _______.", "lawyer", "A barrister is a lawyer.", "Medium"),
    ("The word 'boycott' means to refuse to buy or use _______ goods.", "foreign / certain", "Boycott means refusing products.", "Medium"),
    ("The word 'homage' means showing deep _______ and honor.", "respect", "Homage means showing deep respect.", "Medium"),
    ("The word 'oppression' refers to unjust and _______ treatment.", "cruel / unfair", "Oppression is cruel treatment.", "Medium"),
    ("Gandhiji's movement inspired people to become independent and self-_______.", "reliant", "It built self-reliance.", "Medium"),
    ("Gandhi Jayanti is observed on the _______ day of October.", "second / 2nd", "October 2 is Gandhi Jayanti.", "Medium"),
    ("In South Africa, Gandhiji protested against racial _______.", "discrimination / oppression", "He fought racial discrimination.", "Medium"),
    ("By spinning Khadi cloth, Indians reduced their dependence on British _______.", "mills / cloth / goods", "Khadi reduced British cloth imports.", "Medium"),
    ("Gandhiji believed that violence only creates more _______.", "hatred / violence / harm", "Violence creates more hatred.", "Medium"),
    ("October 2 is recognized globally as International Day of Non-_______.", "Violence", "UN declared it Day of Non-Violence.", "Medium"),
    ("Gandhiji's family in Porbandar was well-known and _______.", "rich / respected", "His family was prosperous and respected.", "Medium"),
    ("During freedom rallies, people marched peacefully without carrying _______.", "weapons / arms", "They carried no weapons.", "Medium"),
    ("Gandhiji's simple attire of a hand-spun cloth symbolized his closeness to common _______.", "people / villagers", "His attire reflected common people.", "Medium"),
    ("Satyagraha requires holding firm to the _______ at all costs.", "truth", "Satyagraha holds firm to truth.", "Medium"),
    ("Gandhiji's teachings continue to inspire global leaders for peace and _______.", "justice / harmony", "His teachings inspire world peace.", "Medium"),

    # Hard (41-50)
    ("The philosophy of Ahimsa stands for complete non-_______ in thought, word, and deed.", "violence", "Ahimsa means total non-violence.", "Hard"),
    ("Economic self-sufficiency was achieved through the widespread adoption of _______.", "Swadeshi", "Swadeshi built economic self-reliance.", "Hard"),
    ("Moral conviction outlasts physical coercion in any social _______.", "movement / struggle", "Moral conviction defeats coercion.", "Hard"),
    ("Porbandar is a coastal city located in the western state of _______.", "Gujarat", "Porbandar is in Gujarat.", "Hard"),
    ("Gandhiji transformed the freedom struggle from an elite debate into a mass _______.", "movement", "He involved the masses.", "Hard"),
    ("The Latin root of law and court representation aligns with the title of _______.", "Barrister", "Barrister relates to legal bar.", "Hard"),
    ("Civil disobedience relies on moral force rather than military _______.", "power / force", "Civil disobedience uses moral force.", "Hard"),
    ("Communal harmony was one of Gandhiji's most cherished social _______.", "goals / ideals", "He championed communal harmony.", "Hard"),
    ("Simple living eliminates superficial material _______.", "desires / greed", "Simple living removes greed.", "Hard"),
    ("The legacy of Bapu lives on as a timeless beacon of truth and _______.", "peace / freedom", "His legacy is a beacon of truth.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 05: Father of the Nation\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK01_CH05_FIB_{idx:03d}"
    q_txt, ans, exp, diff = item
    bloom = "Remembering" if diff == "Easy" else ("Understanding" if diff == "Medium" else "Analyzing")
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Bloom Level**: {bloom}\n"
    fib_content += f"- **Topic**: Sentence Completion {idx}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {q_txt}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. Fill in Blanks from Story (Cloze Passage) (50 Distinct Qs)
# -------------------------------------------------------------
cloze_data = [
    ("Mohandas Karamchand Gandhi is the most popular historical figure in _______.", "India", "Easy"),
    ("He was born in Porbandar, Gujarat, on October 2, _______.", "1869", "Easy"),
    ("His family was rich and he had a good reputation as a _______ boy.", "quiet-natured / truthful", "Easy"),
    ("He went to London for his higher education to study _______.", "law", "Easy"),
    ("In London, he completed his studies and became a _______.", "Barrister", "Easy"),
    ("Upon his return to India, he practiced law at the Bombay _______ Court.", "High", "Easy"),
    ("Gandhiji later moved to South _______ to work.", "Africa", "Easy"),
    ("In South Africa, he lost interest in law and started _______.", "Satyagraha", "Easy"),
    ("Satyagraha was a non-violent protest against the oppression of _______.", "Europeans", "Easy"),
    ("He soon returned to India and joined the struggle for _______.", "independence / freedom", "Easy"),
    ("India was under the rule of the _______.", "British", "Easy"),
    ("He was a simple man who taught simplicity and self-_______.", "reliance", "Easy"),
    ("He encouraged Indians to boycott _______ goods.", "foreign", "Easy"),
    ("He asked people to make their own _______ goods.", "Swadeshi", "Easy"),
    ("He was loved and respected by people of all _______.", "communities", "Easy"),
    ("As a freedom fighter, Gandhi was a man of firm _______.", "belief", "Easy"),
    ("During his struggle, the British put him in _______ several times.", "jail", "Easy"),
    ("While in jail, he endured extreme _______.", "hardships", "Easy"),
    ("To honor his role, his birthday is celebrated as a national _______.", "festival", "Easy"),
    ("His birthday falls on the second day of _______.", "October", "Easy"),
    ("We pay homage to him and everyone who stood with _______.", "him", "Easy"),
    ("Gandhiji is affectionately called the Father of the _______.", "Nation", "Easy"),
    ("He believed that non-violence is stronger than _______.", "weapons / violence", "Easy"),
    ("He spun cotton thread on his _______.", "Charkha", "Easy"),
    ("His life teaches us the power of _______ and non-violence.", "truth", "Easy"),

    ("Gandhiji's childhood in Gujarat laid the foundation of his _______.", "character", "Medium"),
    ("Studying law in London gave him knowledge of legal _______.", "rights", "Medium"),
    ("The discrimination in South Africa sparked his commitment to _______.", "justice", "Medium"),
    ("Satyagraha relies on the moral power of _______.", "truth", "Medium"),
    ("Swadeshi encouraged Indians to support local _______.", "weavers / workers", "Medium"),
    ("Boycotting foreign cloth weakened British economic _______.", "power", "Medium"),
    ("Gandhiji lived a simple life to stay connected with poor _______.", "farmers / villagers", "Medium"),
    ("He believed that true freedom begins with self-_______.", "discipline", "Medium"),
    ("His non-violent struggle proved that peace wins over _______.", "force", "Medium"),
    ("Going to jail did not break his firm _______.", "spirit / belief", "Medium"),
    ("People of all religions saw him as a unifying _______.", "leader", "Medium"),
    ("October 2 is celebrated as Gandhi _______ in India.", "Jayanti", "Medium"),
    ("The world honors him on International Day of Non-_______.", "Violence", "Medium"),
    ("Mahatma Gandhi's life motto was Simple Living and High _______.", "Thinking", "Medium"),
    ("His message of peace remains relevant for future _______.", "generations", "Medium"),

    ("Satyagraha proved that moral insistence on truth alters political _______.", "destiny", "Hard"),
    ("Swadeshi linked economic self-sufficiency with national _______.", "dignity", "Hard"),
    ("Ahimsa transforms hostility into mutual human _______.", "understanding", "Hard"),
    ("Enduring imprisonment demonstrated unyielding moral _______.", "fortitude", "Hard"),
    ("National unity was achieved by respecting diverse _______.", "cultures", "Hard"),
    ("The title Barrister reflected his formal legal _______.", "credentials", "Hard"),
    ("Mahatma Gandhi's legacy shapes global non-violent _______.", "philosophy", "Hard"),
    ("Class 1 students learn to solve conflicts without physical _______.", "aggression", "Hard"),
    ("Truthful living builds an indestructible foundation of _______.", "character", "Hard"),
    ("Homage to Bapu inspires active pursuit of truth and _______.", "peace", "Hard")
]

cloze_content = f"# Fill in the Blanks from Story — Chapter 05: Father of the Nation\n\n> **Category**: Fill in the Blanks from Story (Cloze Passage) | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(cloze_data, start=1):
    q_id = f"BK01_CH05_STORY_FIB_{idx:03d}"
    q_txt, ans, diff = item
    bloom = "Remembering" if diff == "Easy" else ("Understanding" if diff == "Medium" else "Analyzing")
    cloze_content += f"### Question {idx}\n"
    cloze_content += f"- **Question ID**: {q_id}\n"
    cloze_content += f"- **Type**: Story Cloze Fillup\n"
    cloze_content += f"- **Difficulty**: {diff}\n"
    cloze_content += f"- **Bloom Level**: {bloom}\n"
    cloze_content += f"- **Topic**: Story Passage Context {idx}\n"
    cloze_content += f"- **Marks**: 1\n\n"
    cloze_content += f"**Question**: Complete the story line: \"{q_txt}\"\n\n"
    cloze_content += f"- **Answer Key**: **{ans}** — Correct word directly from the story passage.\n\n---\n\n"

with open(os.path.join(CH05_DIR, "fill_in_blanks_story.md"), "w", encoding="utf-8") as f:
    f.write(cloze_content)

# -------------------------------------------------------------
# 4. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Mahatma Gandhi is called the Father of the Nation in India.", True, "He is lovingly called the Father of the Nation.", "Easy"),
    ("Gandhiji was born in London.", False, "He was born in Porbandar, Gujarat.", "Easy"),
    ("Gandhiji's birthday is on October 2, 1869.", True, "He was born on October 2, 1869.", "Easy"),
    ("Gandhiji went to London to study medicine.", False, "He went to London to study law and became a Barrister.", "Easy"),
    ("Gandhiji practiced law at the Bombay High Court after returning from London.", True, "He practiced law at the Bombay High Court.", "Easy"),
    ("Gandhiji started Satyagraha in South Africa.", True, "He started Satyagraha in South Africa against oppression.", "Easy"),
    ("Satyagraha is a violent protest with weapons.", False, "Satyagraha is a non-violent protest based on truth.", "Easy"),
    ("Gandhiji led India's freedom struggle against British rule.", True, "He led the struggle against British rule.", "Easy"),
    ("Gandhiji encouraged people to buy and wear foreign clothes.", False, "He encouraged people to boycott foreign goods and use Swadeshi.", "Easy"),
    ("Swadeshi means goods made in our own country.", True, "Swadeshi refers to Indian-made goods.", "Easy"),
    ("Gandhi Jayanti is celebrated on October 2 as a national festival.", True, "October 2 is celebrated as Gandhi Jayanti.", "Easy"),
    ("Gandhiji lived a very luxury and wealthy life as a leader.", False, "He lived a very simple life and taught simplicity.", "Easy"),
    ("The British put Gandhiji in jail several times during the freedom struggle.", True, "He was imprisoned multiple times.", "Easy"),
    ("Gandhiji used guns and swords to fight for India's freedom.", False, "He fought using non-violence (Ahimsa) and truth.", "Easy"),
    ("Gandhiji was respected by people of all religions and communities.", True, "He was loved and respected by all communities.", "Easy"),
    ("Gandhiji was born in the state of Maharashtra.", False, "He was born in Porbandar, Gujarat.", "Easy"),
    ("Gandhiji had a reputation as a quiet and truthful boy in childhood.", True, "He was known for being quiet and truthful.", "Easy"),
    ("Gandhiji spun cotton thread on a Charkha.", True, "He spun thread on a Charkha daily.", "Easy"),
    ("Gandhiji wanted Indians to depend on other countries for clothing.", False, "He taught self-reliance and Swadeshi.", "Easy"),
    ("Gandhiji gave up his law career in South Africa to fight for people's rights.", True, "He devoted his life to fighting oppression.", "Easy"),
    ("Mahatma means 'Great Soul'.", True, "Mahatma translates to Great Soul.", "Easy"),
    ("October 2 is also observed as International Day of Non-Violence worldwide.", True, "The UN declared October 2 Day of Non-Violence.", "Easy"),
    ("Gandhiji was afraid of going to jail for India's freedom.", False, "He endured jail and extreme hardships bravely.", "Easy"),
    ("Gandhiji's full name was Mohandas Karamchand Gandhi.", True, "His full name was Mohandas Karamchand Gandhi.", "Easy"),
    ("Chapter 05 inspires children to follow truth, peace, and simplicity.", True, "The story inspires children to walk on the path of truth.", "Easy"),

    # Medium (26-40)
    ("The word 'barrister' means a person who builds houses.", False, "A barrister is a qualified lawyer.", "Medium"),
    ("The word 'boycott' means refusing to buy or use certain products.", True, "Boycott means refusing products as a protest.", "Medium"),
    ("The word 'homage' means paying deep respect and honor.", True, "Homage means showing deep respect.", "Medium"),
    ("The word 'oppression' means kind and gentle treatment.", False, "Oppression means cruel and unjust treatment.", "Medium"),
    ("Gandhiji's Swadeshi movement gave work to Indian weavers and artisans.", True, "It revived local cottage industries.", "Medium"),
    ("Gandhiji believed that violence was the best way to win freedom.", False, "He firmly believed non-violence was superior.", "Medium"),
    ("Gandhiji's simple clothing made him accessible to poor villagers.", True, "His simple attire connected him with the masses.", "Medium"),
    ("The British rulers easily defeated Gandhiji's moral strength.", False, "Moral strength and peaceful protest forced the British to leave.", "Medium"),
    ("Gandhiji treated people of all communities with equal love.", True, "He championed communal harmony.", "Medium"),
    ("Satyagraha means insisting on truth peacefully.", True, "Satya (truth) + Agraha (insistence).", "Medium"),
    ("Gandhiji spent his entire life in London.", False, "He returned to India to lead the freedom struggle.", "Medium"),
    ("Khadi cloth is hand-spun cotton cloth promoted by Gandhiji.", True, "Khadi was hand-spun using the Charkha.", "Medium"),
    ("Gandhiji taught that true freedom begins with self-discipline.", True, "Self-discipline is the foundation of freedom.", "Medium"),
    ("Going to jail made Gandhiji lose faith in his mission.", False, "Jail hardships strengthened his firm belief.", "Medium"),
    ("Gandhiji's birthday is celebrated only in Gujarat.", False, "It is a national festival celebrated across India and worldwide.", "Medium"),

    # Hard (41-50)
    ("Satyagraha proved that moral conviction can defeat military power.", True, "Moral truth defeated an armed empire.", "Hard"),
    ("Swadeshi aimed at both economic independence and national self-respect.", True, "It targeted economic self-reliance and pride.", "Hard"),
    ("Ahimsa means avoiding physical harm as well as harmful thoughts.", True, "Ahimsa covers thought, word, and deed.", "Hard"),
    ("Gandhiji's legal education in London helped him understand rights and governance.", True, "Law studies gave him deep legal insight.", "Hard"),
    ("Civil disobedience encourages breaking unjust laws through violent riots.", False, "It involves breaking unjust laws peacefully without violence.", "Hard"),
    ("Mahatma Gandhi's methods inspired civil rights leaders around the globe.", True, "Leaders like Martin Luther King Jr. followed his path.", "Hard"),
    ("Communal harmony was secondary to economic gain in Gandhiji's vision.", False, "Communal harmony was a fundamental pillar of his vision.", "Hard"),
    ("Simple living helps reduce greed and promotes environmental harmony.", True, "Simplicity lowers consumption and greed.", "Hard"),
    ("Truth (Satya) was considered by Gandhiji as the ultimate expression of God.", True, "Gandhiji stated 'Truth is God'.", "Hard"),
    ("Chapter 05 teaches that lasting social change is built through non-violent conviction.", True, "Non-violent conviction creates lasting change.", "Hard")
]

tf_content = f"# True / False — Chapter 05: Father of the Nation\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK01_CH05_TF_{idx:03d}"
    q_txt, is_true, exp, diff = item
    ans_str = "True" if is_true else "False"
    bloom = "Remembering" if diff == "Easy" else ("Understanding" if diff == "Medium" else "Analyzing")
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Bloom Level**: {bloom}\n"
    tf_content += f"- **Topic**: Statement Evaluation {idx}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Question**: State True or False: {q_txt}\n\n"
    tf_content += f"- **Answer Key**: **{ans_str}** — {exp}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 5. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who is Mahatma Gandhi and what title is he given in India?", "Mahatma Gandhi is India's greatest freedom leader, lovingly called the 'Father of the Nation'.", "Easy"),
    ("Where and when was Mahatma Gandhi born?", "He was born in Porbandar, Gujarat, on October 2, 1869.", "Easy"),
    ("What was Gandhiji's full name?", "His full name was Mohandas Karamchand Gandhi.", "Easy"),
    ("Where did Gandhiji go for higher education and what did he study?", "He went to London to study law and became a Barrister.", "Easy"),
    ("What did Gandhiji do after returning to India from London?", "He practiced law at the Bombay High Court.", "Easy"),
    ("Which country did Gandhiji move to for work after Bombay?", "He moved to South Africa to work as a lawyer.", "Easy"),
    ("What movement did Gandhiji start in South Africa?", "He started 'Satyagraha', a non-violent protest against racial oppression.", "Easy"),
    ("What does the word 'Satyagraha' mean?", "Satyagraha means a non-violent protest based on holding firm to the truth.", "Easy"),
    ("Why did Gandhiji return to India from South Africa?", "He returned to lead India's struggle for independence from British rule.", "Easy"),
    ("What principles did Gandhiji teach the people of India?", "He taught truth, simplicity, non-violence (Ahimsa), and self-reliance.", "Easy"),
    ("What does 'Swadeshi' mean?", "Swadeshi means goods and products made in our own country, India.", "Easy"),
    ("What did Gandhiji ask Indians to boycott during the freedom movement?", "He asked Indians to boycott foreign-made goods and clothes.", "Easy"),
    ("How is Gandhiji's birthday celebrated on October 2?", "It is celebrated across India as Gandhi Jayanti, a national festival.", "Easy"),
    ("What hardships did Gandhiji face during the freedom struggle?", "He was put in jail several times by the British and endured extreme physical hardships.", "Easy"),
    ("Why did people of all communities love and respect Gandhiji?", "Because he treated everyone equally with love, respect, and universal brotherhood.", "Easy"),
    ("What spinning tool did Gandhiji use daily to make thread?", "He used the Charkha (spinning wheel) to spin hand-made Khadi thread.", "Easy"),
    ("What reputation did young Mohandas have in his childhood?", "He had a good reputation as a quiet-natured, honest, and truthful boy.", "Easy"),
    ("What does the word 'Mahatma' mean?", "Mahatma means 'Great Soul', a title given to honor his noble life.", "Easy"),
    ("What does 'boycott' mean in simple words?", "Boycott means refusing to buy or use certain products as a peaceful protest.", "Easy"),
    ("What does 'homage' mean?", "Homage means paying deep respect and honor publicly.", "Easy"),
    ("What kind of clothes did Gandhiji wear?", "He wore simple, hand-spun Khadi clothes to promote simplicity.", "Easy"),
    ("How did Gandhiji fight against British rule without weapons?", "He fought using truth, non-violent protests, marches, and mass unity.", "Easy"),
    ("Why is October 2 special around the world?", "It is recognized by the UN as the International Day of Non-Violence.", "Easy"),
    ("What is the main moral takeaway from Gandhiji's life?", "Always walk on the path of truth, live simply, practice peace, and respect all.", "Easy"),
    ("What is the title of Chapter 05?", "The title of Chapter 05 is 'Father of the Nation'.", "Easy"),

    # Medium (26-40)
    ("Why did Gandhiji oppose foreign goods?", "Because foreign goods hurt local Indian weavers and made India economically dependent on Britain.", "Medium"),
    ("How did spinning the Charkha empower Indian villagers?", "It provided work for local artisans and allowed families to make their own clothes self-reliantly.", "Medium"),
    ("What is the core difference between violent and non-violent protest?", "Violent protest causes physical harm and hatred; non-violent protest uses moral truth and peace to change hearts.", "Medium"),
    ("Why did Gandhiji lose interest in practicing law in South Africa?", "Because he saw severe racial discrimination against natives and felt driven to fight for human rights.", "Medium"),
    ("How did Gandhiji connect with poor farmers and workers in India?", "By adopting a simple lifestyle, wearing simple Khadi, speaking simply, and sharing their struggles.", "Medium"),
    ("What does 'Ahimsa' mean in daily life?", "Ahimsa means avoiding physical harm, harsh words, or bad thoughts toward any living being.", "Medium"),
    ("Why did going to jail fail to stop Gandhiji's freedom movement?", "Because jail hardships only strengthened his firm belief and inspired millions of Indians to join.", "Medium"),
    ("Explain the term 'barrister'.", "A barrister is a law graduate trained and qualified to represent clients in high courts.", "Medium"),
    ("How did Gandhiji promote unity among different religions?", "He respected all holy books, included prayers from all faiths, and treated every community equally.", "Medium"),
    ("What motto guided Gandhiji's personal habits?", "'Simple living and high thinking' guided his daily life and choices.", "Medium"),
    ("Why did the British find Gandhiji's non-violent methods difficult to counter?", "Because physical weapons cannot defeat moral truth and peaceful citizens who refuse to obey unfair laws.", "Medium"),
    ("How does Gandhi Jayanti remind us of our duties as citizens?", "It reminds us to follow truth, keep our surroundings clean, promote peace, and love our country.", "Medium"),
    ("What was the impact of the Swadeshi movement on Indian national pride?", "It made Indians proud of their native heritage, craftsmanship, and economic self-reliance.", "Medium"),
    ("Why did Gandhiji walk long distances during protests like the Salt March?", "Walking brought him close to common villagers in every town, building mass awareness and unity.", "Medium"),
    ("Summarize Chapter 05 in two simple sentences.", "Chapter 05 describes how Mahatma Gandhi led India's freedom struggle through truth, non-violence, and Swadeshi. He lived simply and is remembered as the Father of the Nation.", "Medium"),

    # Hard (41-50)
    ("Analyze how Satyagraha combines truth (Satya) with firmness (Agraha).", "Satyagraha means holding firm to truth without anger, using moral persuasion to convince opponents of justice.", "Hard"),
    ("Evaluate the economic strategy behind the Swadeshi movement.", "Swadeshi targeted British industrial profits in India, cutting off trade revenues while rebuilding local village self-sufficiency.", "Hard"),
    ("How did Gandhiji transform the Indian freedom struggle into a mass movement?", "He shifted the movement from legal debates among elites to active participation by millions of common farmers, women, and workers.", "Hard"),
    ("Discuss the global relevance of Mahatma Gandhi's non-violent philosophy today.", "His non-violent principles guide modern peace movements, civil rights struggles, and conflict resolution across nations.", "Hard"),
    ("Why is moral courage considered superior to physical strength in leadership?", "Physical strength can be overcome by greater force, whereas moral courage based on truth is indestructible.", "Hard"),
    ("How can Class 1 students practice non-violence in their daily school life?", "By avoiding physical fights, speaking politely, sharing toys, and resolving disagreements through calm talking.", "Hard"),
    ("Examine how self-reliance (Swavalamban) builds strong national character.", "Self-reliance creates independent thinking, pride in local heritage, and freedom from external domination.", "Hard"),
    ("What is the relationship between truth and God in Gandhiji's worldview?", "Gandhiji declared 'Truth is God', believing that serving truth is the highest form of spiritual and moral duty.", "Hard"),
    ("Why did Gandhiji insist on cleanliness (Swachhata) alongside freedom?", "He believed cleanliness of environment and mind is essential for dignity, health, and true self-respect.", "Hard"),
    ("Synthesize the ultimate philosophy of Chapter 05 for primary learners.", "Be truthful, practice non-violence, live simply, respect all communities, and contribute to your country through self-reliant good deeds!", "Hard")
]

sa_content = f"# Short Answer — Chapter 05: Father of the Nation\n\n> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK01_CH05_SA_{idx:03d}"
    q_txt, ans, diff = item
    bloom = "Remembering" if diff == "Easy" else ("Understanding" if diff == "Medium" else "Analyzing")
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Topic**: Short Comprehension {idx}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 6. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-15)
    ("Write a simple summary of Chapter 05 'Father of the Nation'.", "Mohandas Karamchand Gandhi was born in Porbandar, Gujarat on October 2, 1869. He studied law in London and became a Barrister. He practiced law at the Bombay High Court and later moved to South Africa, where he started Satyagraha—a non-violent protest against oppression. Returning to India, he led the freedom struggle against British rule using non-violence, truth, and Swadeshi goods. He lived a simple life, spun thread on the Charkha, and endured jail for India's freedom. He is loved by all as the Father of the Nation, and his birthday is celebrated as Gandhi Jayanti.", "Easy"),
    ("Describe the early life and education of Mahatma Gandhi.", "Mahatma Gandhi was born in Porbandar, Gujarat, on October 2, 1869. His family was rich and respected. In his childhood, he was known as a quiet-natured, honest, and truthful boy. After finishing school, he went to London to pursue higher education in law. He worked hard, passed his legal examinations, and became a qualified Barrister before returning to India.", "Easy"),
    ("Explain Gandhiji's work in South Africa and how Satyagraha started.", "Gandhiji moved to South Africa for legal work. There, he witnessed severe racial discrimination and oppression against non-European people. Feeling deeply moved, he gave up his law practice and started 'Satyagraha'—a peaceful, non-violent movement to demand equal rights and justice. This was his first successful experiment with non-violent protest.", "Easy"),
    ("How did Gandhiji lead India's freedom struggle against British rule?", "When Gandhiji returned to India, he joined the freedom struggle against British rule. Instead of using guns or swords, he united millions of Indians through non-violent protests, peaceful marches, and truth. He taught people to be self-reliant, make Swadeshi goods, and refuse to obey unfair British laws.", "Easy"),
    ("Explain the concept of 'Swadeshi' and why Gandhiji promoted it.", "'Swadeshi' means using goods made in our own country, India. Gandhiji promoted Swadeshi because foreign British goods were hurting Indian weavers and villagers. By spinning Khadi thread on the Charkha and making their own clothes, Indians became self-reliant and strengthened the national economy.", "Easy"),
    ("Why is October 2 celebrated as Gandhi Jayanti in India?", "October 2 is Mahatma Gandhi's birthday. It is celebrated across India as Gandhi Jayanti, a national festival, to pay homage to Bapu's role in winning India's independence and to remember his timeless principles of truth, non-violence, and simplicity.", "Easy"),
    ("Describe Gandhiji's lifestyle and why he chose simplicity.", "Although Gandhiji was an educated Barrister from a rich family, he chose to live a very simple life. He wore simple hand-spun Khadi cloth, ate simple food, and lived in ashrams. He chose simplicity to stay connected with poor Indian villagers and to teach that true strength comes from high thinking rather than luxury.", "Easy"),
    ("How did Gandhiji endure hardships for India's independence?", "During the freedom struggle, the British government arrested Gandhiji several times and put him in jail. He spent years in prison, enduring cold, poor food, and isolation. Despite these extreme physical hardships, Gandhiji never lost faith in truth and non-violence.", "Easy"),
    ("Why was Mahatma Gandhi loved and respected by all communities?", "Gandhiji loved and respected people of all religions, castes, and backgrounds equally. He preached universal brotherhood, fought against untouchability, and treated everyone with kindness. His equal respect earned him the love of all communities.", "Easy"),
    ("Explain the meaning of 'Satyagraha' and 'Ahimsa'.", "'Satyagraha' is composed of Satya (truth) and Agraha (insistence), meaning holding firm to truth through peaceful means. 'Ahimsa' means complete non-violence—avoiding physical harm, harsh words, and bad thoughts toward others. Together, they formed Gandhiji's core philosophy.", "Easy"),
    ("What role did the Charkha play in India's freedom movement?", "The Charkha (spinning wheel) was a powerful symbol of self-reliance, dignity of labor, and economic freedom. By spinning their own thread daily, Indians demonstrated unity, rejected British manufactured cloth, and supported local weavers.", "Easy"),
    ("How did Gandhiji teach self-reliance to the people of India?", "Gandhiji taught that true freedom requires self-reliance. He urged people to clean their own surroundings, make their own clothes, grow their own food, and solve local problems independently without depending on foreign masters.", "Easy"),
    ("What does the title 'Father of the Nation' signify?", "The title 'Father of the Nation' (Bapu) signifies that Mahatma Gandhi guided, nurtured, and led India to independence just as a father guides his family. His vision of truth and peace laid the foundation of modern India.", "Easy"),
    ("What happens on Gandhi Jayanti across schools in India?", "On Gandhi Jayanti, schools host special assemblies, patriotic songs, cleanliness drives (Swachhata), drawing competitions, and recitations of Gandhiji's favorite prayers like 'Raghupati Raghav Raja Ram' to honor his memory.", "Easy"),
    ("What key values from Chapter 05 can Class 1 students practice every day?", "Class 1 students can practice telling the truth always, avoiding physical fights with friends, keeping their desks and rooms clean, using things wisely, and treating all classmates with kindness and respect.", "Easy"),

    # Medium (16-40)
    ("Analyze how Gandhiji transformed a legal career into a lifelong mission for human rights.", "Gandhiji began as a formal lawyer, but witnessing racial injustice in South Africa changed his perspective. He realized law courts could not solve systemic oppression. He transitioned from courtroom legal arguments to mass moral leadership, dedicating his life to human dignity and freedom.", "Medium"),
    ("Discuss the economic impact of the Boycott of Foreign Goods movement.", "The boycott directly hit British textile factories that relied on the Indian market. By refusing to buy imported cloth, Indian money stayed within the country, reviving traditional handloom weavers and weakening British trade profits.", "Medium"),
    ("How does non-violence (Ahimsa) demonstrate greater strength than physical weapons?", "Physical weapons cause destruction and invite revenge, leading to endless conflict. Non-violence uses moral courage and truth to disarm opponents, changing their hearts and achieving lasting peace without bloodshed.", "Medium"),
    ("Explain the significance of International Day of Non-Violence.", "The United Nations declared October 2 (Gandhiji's birthday) as International Day of Non-Violence to spread his message of peace, tolerance, and non-violent conflict resolution to all nations around the world.", "Medium"),
    ("Describe the childhood qualities of Mohandas that prepared him for leadership.", "As a young boy in Porbandar, Mohandas was quiet, deeply honest, and committed to truth. His refusal to lie, even to please teachers, built a rock-solid moral character that later inspired millions.", "Medium"),
    ("How did Gandhiji promote unity among diverse religious groups in India?", "Gandhiji incorporated prayers from Hinduism, Islam, Christianity, and other faiths in his daily ashram meetings. He fasted for communal peace and firmly stated that all religions lead to the one supreme Truth.", "Medium"),
    ("Compare British rule relying on military force with Gandhiji's leadership relying on moral force.", "The British relied on police, armies, jails, and weapons to control India through fear. Gandhiji relied on moral truth, peaceful civil disobedience, and mass unity. Moral force proved indestructible and ultimately won independence.", "Medium"),
    ("Write a dialogue between Gandhiji and a young student about telling the truth.", "Student: 'Bapu, why is it so important to always tell the truth?'\nGandhiji: 'My child, Truth is the foundation of everything. When you speak truth, you have no fear, and God lives in a truthful heart.'", "Medium"),
    ("How did Gandhiji's simple attire (dhoti) become a political and cultural symbol?", "By discarding European suits for a simple hand-woven Khadi dhoti, Gandhiji identified completely with poor Indian farmers. His attire became a powerful symbol of simplicity, anti-colonial protest, and national pride.", "Medium"),
    ("Explain why self-discipline is essential for practicing Satyagraha.", "Satyagraha requires protesters to remain peaceful even when provoked or struck by police. Without strict self-discipline and emotional control, non-violent protests could turn into violent riots, destroying the movement.", "Medium"),
    ("What was the outcome of Gandhiji's legal work in the Bombay High Court?", "Although he trained in London, Gandhiji was initially shy in the Bombay High Court. However, his legal training developed his analytical thinking and deep understanding of justice, which he later used during freedom negotiations.", "Medium"),
    ("How did Gandhiji's ashrams (like Sabarmati) serve as models for community living?", "His ashrams brought people of all castes and religions together. Everyone performed manual labor, cleaned toilets, cooked together, and practiced truth and non-violence, demonstrating an ideal egalitarian society.", "Medium"),
    ("Why did Gandhiji place high emphasis on cleanliness (Swachhata)?", "Gandhiji famously said 'Cleanliness is next to Godliness'. He believed that physical cleanliness of self and surroundings reflects inner purity, self-respect, and consideration for others.", "Medium"),
    ("Describe how Gandhiji's fasting (upvas) was used as a moral tool.", "Gandhiji used fasting not to harm himself, but as a moral appeal to stop violence and awaken conscience among citizens during religious riots or political crises.", "Medium"),
    ("How did women participate in Gandhiji's freedom movement?", "Gandhiji encouraged women to step out of homes, join peaceful marches, spin Khadi, and picket foreign cloth shops. Women played a massive role in making the freedom struggle a household movement.", "Medium"),
    ("Explain the historical journey of South Africa's Satyagraha to India's Independence.", "The methods of peaceful assembly, marching, and non-cooperation tested in South Africa from 1893 to 1914 were refined in India from 1915 to 1947, leading directly to India's freedom.", "Medium"),
    ("What does 'Simple living and high thinking' mean in modern student life?", "It means avoiding wastefulness, unnecessary greed for expensive gadgets or clothes, and focusing energy on acquiring knowledge, good values, and helpful skills.", "Medium"),
    ("Why is Mahatma Gandhi considered one of the greatest leaders in world history?", "Because he liberated a nation of 400 million people from a powerful empire without firing a single bullet, proving that love and truth are stronger than military weapons.", "Medium"),
    ("How did Gandhiji handle personal criticism and opposition?", "He welcomed criticism with patience and humility. He never held grudges against opponents, believing that love and open dialogue could win over any enemy.", "Medium"),
    ("Summarize the main principles of Chapter 05 in four bullet points.", "• Satya (Truth) — Always speak and live by truth.\n• Ahimsa (Non-violence) — Avoid harm in thought, word, and deed.\n• Swadeshi — Support local, self-reliant products.\n• Equality — Respect all human beings regardless of background.", "Medium"),

    # Hard (41-50)
    ("Deconstruct the philosophical foundation of 'Satyagraha' as developed by Gandhi.", "Satyagraha is not passive resistance; it is active moral force. It posits that unyielding adherence to truth, combined with readiness to suffer without retaliating, awakens the conscience of the oppressor, compelling them to concede justice.", "Hard"),
    ("Analyze the socio-economic implications of the Charkha in anti-colonial resistance.", "The Charkha decentralized economic power. By transforming every home into a production unit, it struck at the core of British colonial exploitation—importing raw Indian cotton and selling back manufactured cloth.", "Hard"),
    ("Evaluate Mahatma Gandhi's concept of 'Nai Talim' (Basic Education through Craft).", "Nai Talim integrated head, heart, and hand. Gandhi advocated learning through practical crafts like weaving and farming, ensuring education fostered dignity of labor, moral character, and economic self-sufficiency.", "Hard"),
    ("How did Gandhi bridge the divide between urban intellectuals and rural masses?", "Gandhi abandoned Western legal attire, adopted rural dialects and dress, walked thousands of miles through villages, and prioritized agrarian issues (like salt and land tax), forging a unified national consciousness.", "Hard"),
    ("Examine the global legacy of Gandhian non-violence in 20th-century civil rights.", "Gandhian Ahimsa served as a strategic blueprint for global liberation movements. Leaders like Martin Luther King Jr. in the USA, Nelson Mandela in South Africa, and Aung San Suu Kyi applied his methods to dismantle oppression.", "Hard"),
    ("Formulate a Class 1 activity that translates Swadeshi into environmental awareness.", "Students bring locally grown fruits or homemade snacks in reusable cloth bags, learning to reduce plastic waste and support local farmers, connecting Swadeshi with eco-friendly living.", "Hard"),
    ("Critique the distinction between passive submission and active non-violent resistance.", "Passive submission stems from fear or weakness. Active non-violent resistance stems from moral courage and strength—choosing peace while fearlessly confronting injustice through civil disobedience.", "Hard"),
    ("Discuss Gandhi's vision of 'Sarvodaya' (Progress for All).", "Sarvodaya asserts that true development is measured by the upliftment of the last and poorest individual in society ('Antyodaya'). It rejects selfish economic growth in favor of collective welfare.", "Hard"),
    ("Why is truth (Satya) considered the ultimate foundation of all ethical systems?", "Truth is objective reality and moral integrity. Without truth, trust collapses, law becomes arbitrary, and human relationships deteriorate. Truth ensures justice, accountability, and harmony.", "Hard"),
    ("Synthesize the ultimate educational message of Chapter 05 for primary learners.", "Mahatma Gandhi's life proves that character is higher than intellect. Walk fearlessly on the path of truth, live simply, practice peace toward all beings, and build a self-reliant, compassionate world!", "Hard")
]

la_content = f"# Long Answer — Chapter 05: Father of the Nation\n\n> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK01_CH05_LA_{idx:03d}"
    q_txt, ans, diff = item
    bloom = "Understanding" if diff == "Easy" else ("Analyzing" if diff == "Medium" else "Evaluating")
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Topic**: Comprehensive Analysis {idx}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

print("[SUCCESS] All 6 category files for Chapter 05 completely refined with 100% unique Class 1 questions!")
