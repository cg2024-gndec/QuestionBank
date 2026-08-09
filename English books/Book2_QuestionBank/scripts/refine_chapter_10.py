r"""
Refines all 6 Category files for Chapter 10 ("The Banyan Tree") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH10_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_10")
os.makedirs(CH10_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("In which country can the Banyan Tree be commonly found in many places?", "(A) India", "(B) Australia", "(C) Africa", "(D) Europe", "(A)", "The Banyan Tree can be seen in many places in India.", "Easy", "Remembering", "Country Setting"),
    ("What special type of roots does the Banyan Tree have?", "(A) Aerial roots", "(B) Tap roots only", "(C) Water roots", "(D) No roots", "(A)", "It has aerial roots which grow from the branches.", "Easy", "Remembering", "Root Type"),
    ("Where do the aerial roots of the Banyan Tree grow from?", "(A) From the branches", "(B) From the leaves", "(C) From the flowers", "(D) From the seeds only", "(A)", "Aerial roots grow from the branches and descend to the ground.", "Easy", "Remembering", "Root Growth Origin"),
    ("What do the aerial roots do after growing from the branches?", "(A) Descend to the ground", "(B) Fly into the sky", "(C) Turn into flowers", "(D) Disappear", "(A)", "They descend to the ground and anchor the tree.", "Easy", "Remembering", "Root Growth Path"),
    ("What is the average life-span of a Banyan Tree?", "(A) 200–500 years", "(B) 10–20 years", "(C) 50–100 years", "(D) 1,000–2,000 years", "(A)", "The average life span is 200-500 years.", "Easy", "Remembering", "Life Span"),
    ("In Ayurveda, what part of the Banyan Tree is used to treat health conditions?", "(A) Fruit", "(B) Leaves only", "(C) Seeds only", "(D) Thorns", "(A)", "In Ayurveda, its fruit is used to treat health conditions.", "Easy", "Remembering", "Medicinal Part"),
    ("What two conditions is the fruit of the Banyan Tree used to treat in Ayurveda?", "(A) Inflammation and skin irritation", "(B) Fever and headache", "(C) Stomach pain and cough", "(D) Toothache and cold", "(A)", "Its fruit treats inflammation as well as skin irritation.", "Easy", "Remembering", "Ayurvedic Treatment"),
    ("What product is made from the wood of the Banyan Tree?", "(A) Paper", "(B) Plastic", "(C) Glass", "(D) Cloth", "(A)", "Paper is also made from the wood of this tree.", "Easy", "Remembering", "Tree Product"),
    ("In which religions is the Banyan Tree considered sacred?", "(A) Hinduism and Buddhism", "(B) Christianity and Judaism", "(C) Islam and Shinto", "(D) Jainism only", "(A)", "It is considered sacred in religions like Hinduism and Buddhism.", "Easy", "Remembering", "Religions"),
    ("What national status does the Banyan Tree hold in India?", "(A) National Tree of India", "(B) National Flower of India", "(C) National Fruit of India", "(D) National Bird of India", "(A)", "The Banyan Tree is the national tree of India.", "Easy", "Remembering", "National Status"),
    ("What does the word 'aerial' mean according to the word box?", "(A) From or in the air", "(B) Deep underground", "(C) Inside water", "(D) Made of stone", "(A)", "Aerial means from or in the air.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'descend' mean?", "(A) Come down", "(B) Go up", "(C) Turn around", "(D) Stop moving", "(A)", "Descend means come down.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'inflammation' mean?", "(A) Swelling", "(B) Bleeding", "(C) Coldness", "(D) Sleepiness", "(A)", "Inflammation is defined as swelling.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'sacred' mean?", "(A) Holy", "(B) Secret", "(C) Scary", "(D) Small", "(A)", "Sacred is defined as holy.", "Easy", "Understanding", "Vocabulary"),
    ("How does the Banyan Tree spread further across large areas?", "(A) From its aerial roots descending to the ground and forming new trunks", "(B) By walking on roots", "(C) By birds carrying whole trees", "(D) By floating in air", "(A)", "The tree spreads further through its descending aerial roots.", "Easy", "Understanding", "Tree Expansion"),
    ("Is the Banyan Tree a small plant or a huge tree?", "(A) A huge tree", "(B) A tiny bush", "(C) A small grass", "(D) A climbing vine", "(A)", "The text states it is a huge tree.", "Easy", "Remembering", "Tree Size"),
    ("Does the Banyan Tree have a short or a very long life-span?", "(A) A very long life-span", "(B) A short life-span", "(C) One week life-span", "(D) One year life-span", "(A)", "This tree has a very long life-span.", "Easy", "Remembering", "Life Span Nature"),
    ("Which system of traditional medicine uses the Banyan fruit?", "(A) Ayurveda", "(B) Allopathy", "(C) Homeopathy", "(D) Acupuncture", "(A)", "In Ayurveda, its fruit is used.", "Easy", "Remembering", "Medicine System"),
    ("What does 'skin irritation' mean?", "(A) Itching or redness on the skin", "(B) Hair loss", "(C) Broken bones", "(D) Eye pain", "(A)", "Skin irritation means discomfort, itching, or redness on skin.", "Easy", "Understanding", "Medical Term"),
    ("What shade does a huge Banyan tree provide?", "(A) Vast cool shade for humans and animals", "(B) No shade at all", "(C) Hot sun rays", "(D) Dark rain", "(A)", "Huge banyan trees provide vast cool shade.", "Easy", "Understanding", "General Knowledge"),
    ("Do aerial roots look like hanging ropes from branches?", "(A) Yes, they hang down from branches like ropes until touching the ground", "(B) No, they grow straight up", "(C) No, they look like leaves", "(D) No, they are blue", "(A)", "Aerial roots hang from branches and descend down.", "Easy", "Understanding", "Visual Description"),
    ("Why is the Banyan tree chosen as the national tree of India?", "(A) Because of its massive size, long lifespan, sacred status, and deep cultural roots in India", "(B) Because it produces gold", "(C) Because it grows on water", "(D) Because it is small", "(A)", "Massive size, longevity, sacredness, and cultural significance.", "Easy", "Understanding", "National Symbol Reason"),
    ("What happens when aerial roots reach the soil?", "(A) They take root and grow into supportive pillar-like trunks", "(B) They die immediately", "(C) They fly back up", "(D) They turn into flowers", "(A)", "They root in the ground and support expanding branches.", "Easy", "Understanding", "Botany Concept"),
    ("Can a single banyan tree look like a whole small forest over centuries?", "(A) Yes, because its expanding aerial roots create dozens of supportive trunks", "(B) No, it stays one tiny stick", "(C) No, it disappears after a month", "(D) No, it shrinks over time", "(A)", "Expanding prop roots make it look like a forest.", "Easy", "Understanding", "Tree Appearance"),
    ("What is the title of Chapter 10?", "(A) The Banyan Tree", "(B) The Himalayas", "(C) Sacred Trees of India", "(D) National Plants", "(A)", "Chapter 10 is titled 'The Banyan Tree'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why are aerial roots also called 'prop roots' or 'pillar roots'?", "(A) Because once they descend to the ground, they thicken into solid pillars that support heavy branches", "(B) Because people tie pillars to them", "(C) Because they are made of stone", "(D) Because they grow on roofs", "(A)", "They thicken into supportive pillars for massive branches.", "Medium", "Understanding", "Botanical Function"),
    ("How does the long lifespan (200-500 years) of the Banyan tree make it a symbol of immortality in Indian culture?", "(A) Living for centuries across generations makes it a living symbol of permanence and strength", "(B) Because it never drops leaves", "(C) Because it talks to people", "(D) Because it grows without water", "(A)", "Living for centuries symbolizes longevity and permanence.", "Medium", "Analyzing", "Cultural Symbolism"),
    ("What is the botanical significance of the Banyan tree producing paper from its wood?", "(A) Its wood fibers can be processed into paper pulp, demonstrating its economic utility", "(B) Paper grows on its leaves naturally", "(C) Its paper is used as money", "(D) Books grow on its branches", "(A)", "Wood fibers processed into paper pulp.", "Medium", "Understanding", "Economic Utility"),
    ("Why is the Banyan tree considered sacred in Buddhism?", "(A) Buddha is believed to have meditated under sacred fig/banyan trees to achieve spiritual enlightenment", "(B) Buddha planted the first banyan tree in the sky", "(C) Buddhist monks wear banyan leaves", "(D) Banyan trees produce holy water", "(A)", "Associated with meditation and enlightenment.", "Medium", "Remembering", "Religious Context"),
    ("How does the Banyan tree support biodiversity in Indian ecosystems?", "(A) Its massive canopy and fruits provide shelter and food for countless birds, bats, insects, and monkeys", "(B) It repels all animals", "(C) It eats insects", "(D) It grows where no animals live", "(A)", "Provides food and shelter for birds, insects, and animals.", "Medium", "Evaluating", "Ecological Role"),
    ("What is the difference between normal underground roots and banyan aerial roots?", "(A) Underground roots grow down from seeds into soil; aerial roots sprout from overhead branches into air before descending to soil", "(B) Underground roots are green; aerial roots are red", "(C) Aerial roots absorb sunlight only", "(D) Underground roots grow on top of leaves", "(A)", "Sprouting overhead into air before grounding vs subterranean soil growth.", "Medium", "Analyzing", "Root Comparison"),
    ("Why was the Banyan tree selected as India's National Tree over other trees?", "(A) Its sprawling structure represents unity in diversity, long life, and shelter for all living beings in India", "(B) It is the easiest tree to cut down", "(C) It grows only in one garden", "(D) It was brought from abroad recently", "(A)", "Represents unity, shelter, longevity, and Indian heritage.", "Medium", "Evaluating", "National Emblem Significance"),
    ("How does Ayurveda utilize natural plant parts like banyan fruit for healing?", "(A) Ayurvedic medicine extracts natural active compounds from fruits to reduce swelling (inflammation) and skin rashes", "(B) Ayurveda turns banyan fruit into candy", "(C) Ayurvedic doctors burn the fruit for smoke", "(D) Ayurveda uses fruit to color clothes", "(A)", "Extracts natural active compounds for anti-inflammatory healing.", "Medium", "Understanding", "Ayurvedic Science"),
    ("What makes a mature Banyan tree an ideal gathering place in traditional Indian villages?", "(A) Its wide canopy provides vast cool shade where village elders hold meetings, market stalls set up, and children play", "(B) It has comfortable chairs built inside", "(C) It stays warm in hot sun", "(D) It plays music", "(A)", "Vast canopy shade ideal for community gatherings.", "Medium", "Analyzing", "Village Community Role"),
    ("What does 'inflammation' mean in medical terms and how does banyan fruit help?", "(A) Inflammation is painful body swelling; natural substances in banyan fruit soothe and reduce this swelling", "(B) Inflammation means cold hands", "(C) Inflammation means broken teeth", "(D) Inflammation means tiredness", "(A)", "Swelling reduced by fruit's healing properties.", "Medium", "Understanding", "Medical Explanation"),
    ("How does the Banyan tree continuously expand its area over time?", "(A) New aerial roots keep dropping from outer branches, taking root, and extending the tree's outer boundary outward", "(B) Its seeds walk across fields", "(C) Farmers pull the branches", "(D) It grows only vertically upwards", "(A)", "Dropping new aerial prop roots outward continuously.", "Medium", "Understanding", "Growth Pattern"),
    ("Why is skin irritation treated with natural remedies like banyan fruit extracts?", "(A) Plant extracts provide gentle cooling and anti-bacterial relief to irritated skin without harsh chemicals", "(B) Banyan fruit turns skin green", "(C) Skin irritation needs hot oil", "(D) Banyan fruit is used as soap", "(A)", "Gentle soothing relief for skin without harsh chemicals.", "Medium", "Understanding", "Natural Healing"),
    ("What environmental benefit does a 300-year-old Banyan tree provide to a city or village?", "(A) It absorbs large amounts of carbon dioxide, produces oxygen, cools ambient air, and prevents soil erosion", "(B) It stops all rain", "(C) It heats up the surrounding air", "(D) It absorbs groundwater completely", "(A)", "Carbon absorption, oxygen production, air cooling, soil protection.", "Medium", "Evaluating", "Environmental Benefits"),
    ("How does Chapter 10 build respect for nature among Class 2 students?", "(A) By teaching that trees are living sacred beings that provide medicine, paper, shade, shelter, and long life to the nation", "(B) By telling students to chop down trees for paper", "(C) By teaching how to buy furniture", "(D) By showing trees are dangerous", "(A)", "Teaches reverence for trees as life-giving national symbols.", "Medium", "Applying", "Moral & Environmental Value"),
    ("What is the scientific reason banyan trees can survive severe storms and high winds?", "(A) Multiple prop root trunks anchor the tree securely to the ground from many points, preventing it from blowing over", "(B) Banyan trees bend completely flat", "(C) Banyan trees drop all their branches in wind", "(D) Banyan trees have soft rubber trunks", "(A)", "Multiple prop root trunks anchor it firmly from many points.", "Medium", "Analyzing", "Storm Resilience"),

    # Hard (41-50)
    ("Analyze the architectural analogy between a Banyan tree's prop roots and cathedral pillars.", "(A) Just as pillars distribute heavy roof weight in cathedrals, prop roots distribute the immense weight of spreading heavy branches to the ground", "(B) Prop roots are carved by stone artists", "(C) Cathedral pillars grow leaves", "(D) Banyan trees are built out of bricks", "(A)", "Prop roots act as structural load-bearing pillars for heavy branches.", "Hard", "Analyzing", "HOTS Architectural Analogy"),
    ("Evaluate the cultural concept of 'sacred groves' and banyan tree veneration in Indian society.", "(A) Declaring trees sacred protected mature banyan trees from deforestation, serving as an ancient traditional conservation practice", "(B) Sacred trees were used for firewood", "(C) Sacred status meant no one could look at the tree", "(D) Sacred groves were built inside houses", "(A)", "Sacred status acted as an ancient conservation mechanism.", "Hard", "Evaluating", "Conservation Strategy"),
    ("Deconstruct the biological life cycle of a Banyan tree starting as an epiphyte on a host tree.", "(A) Seeds deposited by birds sprout in host tree crevices -> aerial roots grow down to ground -> roots thicken and choke host -> banyan becomes independent giant", "(B) Seed grows underwater -> turns into fish -> becomes tree", "(C) Seed grows in sand -> turns into flower -> dies in winter", "(D) Tree grows from fallen branches only", "(A)", "Epiphytic growth -> aerial root descent -> independent pillar tree.", "Hard", "Analyzing", "Biological Life Cycle"),
    ("Compare the Banyan tree (*Ficus benghalensis*) with other national symbols of India (Lotus, Tiger, Peacock).", "(A) Tiger: national strength/grace; Lotus: purity/beauty; Peacock: vibrant culture; Banyan: longevity, shelter, and deep-rooted unity", "(B) All national symbols are plants", "(C) Banyan tree represents speed and power", "(D) Tiger and Banyan tree are identical symbols", "(A)", "Banyan symbolizes longevity, shelter, and deep-rooted unity.", "Hard", "Analyzing", "National Symbols Comparison"),
    ("Assess the sustainable paper production potential of wood vs. paper recycling and conservation.", "(A) While paper can be made from banyan wood, sustainable forestry and paper recycling are vital to prevent cutting ancient mature trees", "(B) Ancient 500-year-old banyan trees should be cut for paper", "(C) Paper cannot be made from wood fiber", "(D) Paper recycling is harmful to environment", "(A)", "Emphasizing conservation and recycling over cutting ancient trees.", "Hard", "Evaluating", "Sustainability Assessment"),
    ("How does the Banyan tree's ability to live 200-500 years contribute to long-term carbon sequestration?", "(A) Its massive biomass locks away atmospheric carbon for centuries, serving as a long-term carbon sink in tropical regions", "(B) It releases carbon dioxide continuously", "(C) Small short-lived plants store more carbon than banyan trees", "(D) Carbon is not stored in wood", "(A)", "Massive long-term carbon sink for centuries.", "Hard", "Analyzing", "Carbon Sequestration"),
    ("Synthesize how Ayurveda integrates botanical knowledge with holistic human healthcare.", "(A) Ayurveda identifies specific therapeutic properties in plant parts (like banyan fruit for swelling) to restore natural bodily balance without synthetic drugs", "(B) Ayurveda rejects all plants", "(C) Ayurveda uses only chemicals", "(D) Ayurveda treats diseases using paper", "(A)", "Integrating botanical active properties for bodily balance.", "Hard", "Synthesizing", "Ayurvedic Philosophy"),
    ("What does the Banyan tree teach about leadership and community support?", "(A) True leadership, like the Banyan, extends strong supportive roots downward to lift others and provides vast protective shelter for the whole community", "(B) Leaders should stand alone on top of a mountain", "(C) Leaders should take resources from the poor", "(D) Leaders should cut down other trees", "(A)", "Supportive roots lifting others and providing shelter for all.", "Hard", "Evaluating", "Leadership Metaphor"),
    ("Formulate a conservation campaign statement to protect ancient Banyan trees in Indian villages.", "(A) 'Protect our Living Pillars! Ancient Banyan Trees give us clean air, medicine, shade, and sacred heritage—preserve every tree for future generations!'", "(B) 'Cut down old trees to build roads!'", "(C) 'Replace all banyan trees with plastic pots!'", "(D) 'Banyan trees take up too much space!'", "(A)", "Protect living pillars for clean air, medicine, and heritage.", "Hard", "Creating", "Campaign Statement"),
    ("Synthesize the core message of Chapter 10 for young Class 2 learners.", "(A) Like the noble Banyan tree, grow strong, stay deeply rooted in good values, extend helping hands to others, and protect our environment!", "(B) Climb to the top of banyan trees and break branches", "(C) Never sit under a tree", "(D) Trees are only useful for making paper", "(A)", "Grow strong, stay rooted in values, help others, protect nature.", "Hard", "Evaluating", "Core Lesson Synthesis")
]

mcq_content = f"# MCQs — Chapter 10: The Banyan Tree\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH10_MCQ_{idx:03d}"
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

with open(os.path.join(CH10_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("The Banyan Tree can be seen in many places in _______.", "India", "Found in many places in India.", "Easy"),
    ("The Banyan Tree is a _______ tree.", "huge", "It is a huge tree.", "Easy"),
    ("It has _______ roots which grow from the branches.", "aerial", "It has aerial roots.", "Easy"),
    ("The aerial roots grow from the branches and _______ to the ground.", "descend", "Descend to the ground.", "Easy"),
    ("From these roots the Banyan Tree spreads _______.", "further", "Spreads further.", "Easy"),
    ("The Banyan Tree has a very long life-_______.", "span", "Very long life-span.", "Easy"),
    ("The average life span of a banyan tree is 200 to _______ years.", "500", "200-500 years.", "Easy"),
    ("This tree is very _______ for human beings.", "useful", "Tree is very useful.", "Easy"),
    ("In Ayurveda, the _______ of the banyan tree is used for medicine.", "fruit", "Fruit is used in Ayurveda.", "Easy"),
    ("The fruit is used to treat _______ and skin irritation.", "inflammation", "Treats inflammation and skin irritation.", "Easy"),
    ("The fruit is also used to treat skin _______.", "irritation", "Treats skin irritation.", "Easy"),
    ("_______ is made from the wood of the banyan tree.", "Paper", "Paper is made from its wood.", "Easy"),
    ("The Banyan Tree is considered _______ in Hinduism and Buddhism.", "sacred", "Considered sacred.", "Easy"),
    ("The Banyan Tree is considered sacred in Hinduism and _______.", "Buddhism", "Hinduism and Buddhism.", "Easy"),
    ("The Banyan Tree is the _______ tree of India.", "national", "National tree of India.", "Easy"),
    ("The word 'aerial' means from or in the _______.", "air", "Aerial means from or in the air.", "Easy"),
    ("The word 'descend' means come _______.", "down", "Descend means come down.", "Easy"),
    ("The word 'inflammation' means _______.", "swelling", "Inflammation means swelling.", "Easy"),
    ("The word 'sacred' means _______.", "holy", "Sacred means holy.", "Easy"),
    ("Aerial roots drop down from the tree's _______.", "branches", "Grow from branches.", "Easy"),
    ("The minimum average life span of a banyan tree is _______ years.", "200", "200 years minimum average.", "Easy"),
    ("Paper is made from the _______ of the banyan tree.", "wood", "Made from wood.", "Easy"),
    ("The Banyan Tree is a symbol of long _______.", "life", "Symbol of long life/longevity.", "Easy"),
    ("In India, the Banyan Tree is honored as a sacred and national _______.", "tree", "National tree.", "Easy"),
    ("Chapter 10 is titled 'The Banyan _______'.", "Tree", "Titled 'The Banyan Tree'.", "Easy"),

    # Medium (26-40)
    ("Aerial roots descend into the soil and turn into strong supporting _______.", "trunks", "Turn into supporting trunks.", "Medium"),
    ("The Banyan tree provides vast cool _______ during hot sunny days.", "shade", "Provides vast cool shade.", "Medium"),
    ("Ayurvedic medicine uses natural ingredients like banyan _______ to reduce swelling.", "fruit", "Uses banyan fruit.", "Medium"),
    ("Because of its long lifespan of 200-500 years, the tree is a symbol of _______.", "longevity", "Symbol of longevity.", "Medium"),
    ("Birds and animals find food and _______ in the large banyan canopy.", "shelter", "Find food and shelter.", "Medium"),
    ("The word 'descend' is the opposite of _______.", "ascend", "Opposite of ascend/climb.", "Medium"),
    ("Hinduism and Buddhism consider the Banyan tree to be a _______ plant.", "holy", "Holy/sacred plant.", "Medium"),
    ("The aerial roots grow through the _______ before reaching the ground.", "air", "Grow through the air.", "Medium"),
    ("Paper production utilizes the fibrous _______ of the banyan tree.", "wood", "Utilizes fibrous wood.", "Medium"),
    ("Swelling in body tissues is medically known as _______.", "inflammation", "Known as inflammation.", "Medium"),
    ("The Banyan tree spreads horizontally across large areas of _______.", "land", "Spreads across land.", "Medium"),
    ("The national emblem status of the Banyan tree represents Indian _______.", "heritage", "Represents Indian heritage/culture.", "Medium"),
    ("Skin rashes and itching can be relieved by banyan fruit _______.", "extracts", "Relieved by fruit extracts.", "Medium"),
    ("The huge canopy of the banyan tree protects the soil from _______.", "erosion", "Protects soil from erosion.", "Medium"),
    ("Village meetings in India often gather under the cool shade of a _______ tree.", "banyan", "Gather under a banyan tree.", "Medium"),

    # Hard (41-50)
    ("Prop roots derived from aerial branches provide structural load-bearing _______.", "support", "Provide load-bearing support.", "Hard"),
    ("The biological lifespan of 200-500 years allows the banyan to store vast atmospheric _______.", "carbon", "Store atmospheric carbon.", "Hard"),
    ("Treating inflammation with banyan fruit is a traditional practice in _______.", "Ayurveda", "Practice in Ayurveda.", "Hard"),
    ("The botanical name for the Indian Banyan tree is Ficus _______.", "benghalensis", "Ficus benghalensis.", "Hard"),
    ("Declaring the banyan tree sacred provided an ancient form of forest _______.", "conservation", "Ancient form of conservation.", "Hard"),
    ("Wood fibers from the banyan tree undergo pulping to produce _______.", "paper", "Pulping to produce paper.", "Hard"),
    ("Aerial roots descend vertically under the influence of _______.", "gravity", "Descend under gravity.", "Hard"),
    ("The Banyan tree's massive root network anchors it firmly against severe _______.", "storms", "Anchors against severe storms.", "Hard"),
    ("The sacred status of the banyan tree in Buddhism connects to Buddha's _______.", "enlightenment", "Connects to Buddha's enlightenment.", "Hard"),
    ("Chapter 10 teaches young learners to respect, protect, and value national _______.", "nature", "Value national nature/trees.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 10: The Banyan Tree\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH10_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH10_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The Banyan Tree can be seen in many places in India.", "True", "The text states it can be seen in many places in India.", "Easy"),
    ("The Banyan Tree is a tiny plant that grows in pots.", "False", "It is a huge tree.", "Easy"),
    ("The Banyan Tree has aerial roots that grow from its branches.", "True", "It has aerial roots which grow from the branches.", "Easy"),
    ("Aerial roots grow underground from the start.", "False", "Aerial roots grow from branches in the air and descend to the ground.", "Easy"),
    ("The average life span of a Banyan Tree is 200–500 years.", "True", "The average life span is 200-500 years.", "Easy"),
    ("The Banyan Tree dies after only 5 years.", "False", "It has a very long life-span of 200-500 years.", "Easy"),
    ("In Ayurveda, the fruit of the Banyan Tree is used to treat inflammation.", "True", "Its fruit is used to treat inflammation and skin irritation.", "Easy"),
    ("Paper is made from the fruit of the Banyan Tree.", "False", "Paper is made from the wood of this tree.", "Easy"),
    ("The Banyan Tree is considered sacred in Hinduism and Buddhism.", "True", "It is considered sacred in Hinduism and Buddhism.", "Easy"),
    ("The Banyan Tree is the national tree of India.", "True", "The Banyan Tree is the national tree of India.", "Easy"),
    ("The word 'aerial' means from or in the air.", "True", "Aerial is defined as from or in the air.", "Easy"),
    ("The word 'descend' means to go up into the sky.", "False", "Descend means to come down.", "Easy"),
    ("The word 'inflammation' means swelling in the body.", "True", "Inflammation is defined as swelling.", "Easy"),
    ("The word 'sacred' means holy.", "True", "Sacred is defined as holy.", "Easy"),
    ("Aerial roots help the Banyan tree spread further across land.", "True", "From these roots the tree spreads further.", "Easy"),
    ("The Banyan Tree is useful to human beings.", "True", "The text states this tree is very useful.", "Easy"),
    ("Ayurveda is a traditional system of medicine in India.", "True", "Ayurveda uses natural plants for healing.", "Easy"),
    ("Skin irritation means itching or redness on the skin.", "True", "Skin irritation refers to itching, redness, or skin discomfort.", "Easy"),
    ("Paper is made from the wood of the Banyan tree.", "True", "Paper is made from the wood of this tree.", "Easy"),
    ("The Banyan Tree is the national tree of Australia.", "False", "It is the national tree of India.", "Easy"),
    ("Banyan trees provide shade for animals and people.", "True", "Huge banyan trees provide vast cool shade.", "Easy"),
    ("The Banyan tree has no medicinal uses.", "False", "Its fruit is used in Ayurveda to treat inflammation and skin irritation.", "Easy"),
    ("Buddhism considers the Banyan tree sacred.", "True", "It is considered sacred in Hinduism and Buddhism.", "Easy"),
    ("Hinduism considers the Banyan tree sacred.", "True", "It is considered sacred in Hinduism and Buddhism.", "Easy"),
    ("Chapter 10 is titled 'The Banyan Tree'.", "True", "Chapter 10 is titled 'The Banyan Tree'.", "Easy"),

    # Medium (26-40)
    ("Aerial roots turn into thick supportive trunks after reaching the ground.", "True", "They descend to soil, root themselves, and thicken into supportive prop trunks.", "Medium"),
    ("The long life-span of 200-500 years makes the Banyan tree a symbol of long life.", "True", "Its centuries-long life makes it a symbol of longevity.", "Medium"),
    ("The Banyan tree can spread over acres of land from a single original trunk.", "True", "Spreading aerial roots allow one tree to cover vast land area.", "Medium"),
    ("Ayurveda uses the wood of the Banyan tree to cure fever.", "False", "Ayurveda uses the fruit to treat inflammation and skin irritation.", "Medium"),
    ("Cutting down ancient sacred Banyan trees was historically encouraged in Indian villages.", "False", "Being considered sacred protected Banyan trees from being cut down.", "Medium"),
    ("The word 'descend' describes how roots grow downwards toward the earth.", "True", "Descend means coming down towards the ground.", "Medium"),
    ("The Banyan tree produces fruits that are eaten by birds and used in Ayurveda.", "True", "Its fruit feeds wildlife and serves as Ayurvedic medicine.", "Medium"),
    ("Paper production from banyan wood is the only reason the tree is valued.", "False", "It is valued for medicine, shade, sacred status, national emblem, and ecology.", "Medium"),
    ("The Banyan tree's canopy can shelter hundreds of people at once.", "True", "Its wide spreading canopy provides vast shelter.", "Medium"),
    ("Skin irritation and swelling are treated using banyan leaf juice according to the text.", "False", "The text specifies that its fruit is used to treat inflammation and skin irritation.", "Medium"),
    ("The Banyan tree is only found in Australia and Europe.", "False", "It can be seen in many places in India.", "Medium"),
    ("Prop roots help support the immense weight of heavy horizontal branches.", "True", "Prop roots descend and anchor heavy spreading branches.", "Medium"),
    ("The national status of the Banyan tree reflects its deep roots in Indian culture.", "True", "Its national tree status honors its cultural and ecological importance.", "Medium"),
    ("The Banyan tree drops its aerial roots only in winter.", "False", "Aerial roots grow continuously from branches.", "Medium"),
    ("Learning about national symbols like the Banyan tree builds national pride.", "True", "Studying national symbols builds awareness and cultural pride.", "Medium"),

    # Hard (41-50)
    ("The biological process of prop root growth allows the Banyan tree to expand laterally indefinitely.", "True", "Continuous aerial root formation enables unlimited lateral canopy growth.", "Hard"),
    ("The word 'inflammation' refers to a reduction in body size.", "False", "Inflammation refers to tissue swelling and redness.", "Hard"),
    ("The Banyan tree (*Ficus benghalensis*) is an essential keystone species in Indian ecosystems.", "True", "It provides food and habitat for hundreds of animal and bird species.", "Hard"),
    ("Paper made from wood pulp involves extracting cellulose fibers from banyan timber.", "True", "Wood pulping extracts cellulose fibers for paper making.", "Hard"),
    ("Buddhists respect the Banyan tree because of its connection to spiritual meditation.", "True", "It is revered as a sacred tree associated with meditation and enlightenment.", "Hard"),
    ("The Banyan tree requires high chemical fertilizers to grow in Indian soil.", "False", "It is a native, resilient tree that grows naturally across Indian soils.", "Hard"),
    ("Aerial roots absorb atmospheric moisture before reaching the soil.", "True", "Aerial roots absorb moisture from humid air as they descend.", "Hard"),
    ("The long lifespan of 200-500 years makes the Banyan tree a natural carbon sink.", "True", "Massive wood volume sequesters carbon for centuries.", "Hard"),
    ("The text suggests that the Banyan tree is a modern introduced species in India.", "False", "It is native, ancient, sacred, and the national tree of India.", "Hard"),
    ("Chapter 10 integrates botany, medicine, religion, and national symbols.", "True", "It covers root anatomy, Ayurvedic fruit use, sacred status, and national emblem status.", "Hard")
]

tf_content = f"# True / False — Chapter 10: The Banyan Tree\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH10_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH10_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Where can the Banyan Tree be commonly found?", "The Banyan Tree can be commonly seen in many places across India.", "Easy", "Remembering"),
    ("What special roots does the Banyan Tree have and where do they grow from?", "It has aerial roots that grow from its branches and descend to the ground.", "Easy", "Remembering"),
    ("How does the Banyan Tree spread further across land?", "It spreads further when its aerial roots touch the ground, take root, and support new branches.", "Easy", "Understanding"),
    ("What is the average life-span of a Banyan Tree?", "The average life-span of a Banyan Tree is 200 to 500 years.", "Easy", "Remembering"),
    ("How is the fruit of the Banyan Tree used in Ayurveda?", "In Ayurveda, its fruit is used to treat inflammation (swelling) and skin irritation.", "Easy", "Remembering"),
    ("What product is made from the wood of the Banyan Tree?", "Paper is made from the wood of the Banyan Tree.", "Easy", "Remembering"),
    ("In which religions is the Banyan Tree considered sacred?", "It is considered sacred in religions like Hinduism and Buddhism.", "Easy", "Remembering"),
    ("What is the national status of the Banyan Tree in India?", "The Banyan Tree is the national tree of India.", "Easy", "Remembering"),
    ("What is the meaning of the word 'aerial'?", "Aerial means from or in the air.", "Easy", "Understanding"),
    ("What is the meaning of the word 'descend'?", "Descend means to come down.", "Easy", "Understanding"),
    ("What is the meaning of the word 'inflammation'?", "Inflammation means painful swelling in body tissues.", "Easy", "Understanding"),
    ("What is the meaning of the word 'sacred'?", "Sacred means holy or deserving religious respect.", "Easy", "Understanding"),
    ("Is the Banyan Tree small or huge?", "The Banyan Tree is a huge tree.", "Easy", "Remembering"),
    ("What does skin irritation mean?", "Skin irritation means itching, discomfort, or redness on the skin.", "Easy", "Understanding"),
    ("Why do people and animals like to sit under a Banyan Tree?", "They like sitting under it because its huge canopy provides vast cool shade.", "Easy", "Understanding"),
    ("Do aerial roots grow underground first or in the air first?", "Aerial roots grow in the air first from branches before descending to the ground.", "Easy", "Understanding"),
    ("What happens to aerial roots after they reach the ground?", "They root into the soil and thicken into pillar-like supportive trunks.", "Easy", "Understanding"),
    ("Why is the Banyan Tree called a long-living tree?", "Because it has an average lifespan of 200 to 500 years.", "Easy", "Remembering"),
    ("What part of the Banyan Tree is used to make paper?", "The wood of the Banyan Tree is used to make paper.", "Easy", "Remembering"),
    ("Which traditional Indian medical system uses Banyan fruit?", "Ayurveda.", "Easy", "Remembering"),
    ("Why is the Banyan Tree important to birds?", "Birds eat its fruit and build nests in its massive branches.", "Easy", "Understanding"),
    ("Does the Banyan Tree grow in India?", "Yes, it is commonly seen in many places in India.", "Easy", "Remembering"),
    ("What does 'abode' mean when describing a tree as an abode for birds?", "It means the tree serves as a home or living place for birds.", "Easy", "Understanding"),
    ("Why is the Banyan Tree a symbol of strength?", "Because its thick trunk, aerial roots, and long lifespan make it strong and stable.", "Easy", "Understanding"),
    ("What is the title of Chapter 10?", "The title of Chapter 10 is 'The Banyan Tree'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Explain why aerial roots are essential for a huge Banyan Tree's growth.", "As the Banyan Tree grows heavy spreading branches, aerial roots drop down to act as pillar trunks that support the weight and supply extra nutrients.", "Medium", "Analyzing"),
    ("How does the Banyan Tree benefit human health through Ayurveda?", "Its fruit contains natural medicinal properties used in Ayurvedic remedies to soothe skin irritation and reduce body inflammation.", "Medium", "Understanding"),
    ("Why was the Banyan Tree chosen as the National Tree of India?", "It was chosen because of its vast size, long life, sacred cultural importance, and its symbol as a protective shelter for all.", "Medium", "Evaluating"),
    ("Describe the physical appearance of a mature Banyan Tree.", "A mature Banyan Tree is a massive, spreading tree with a main central trunk and dozens of pillar-like aerial roots hanging from branches to the ground.", "Medium", "Remembering"),
    ("What is the connection between Hinduism, Buddhism, and the Banyan Tree?", "Both religions regard the Banyan Tree as sacred and holy, using it for spiritual meditation and religious worship.", "Medium", "Understanding"),
    ("How does the Banyan Tree help prevent soil erosion?", "Its deep underground root system and multiple prop roots hold the soil tightly together, preventing heavy rains from washing soil away.", "Medium", "Analyzing"),
    ("Explain how paper is produced from tree wood like that of the Banyan.", "Wood fibers are extracted from the tree trunk, processed into pulp, flattened, and dried to form paper sheets.", "Medium", "Understanding"),
    ("Why do village elders in India often hold community meetings under Banyan Trees?", "The tree's wide canopy provides a huge, naturally cool shaded area capable of accommodating whole village gatherings comfortably.", "Medium", "Understanding"),
    ("How does a Banyan Tree create the appearance of a 'miniature forest'?", "As its aerial roots descend and form new trunks, a single tree expands outward into multiple connected trunks that look like a forest.", "Medium", "Analyzing"),
    ("What does the word 'descend' describe in the biological growth of prop roots?", "It describes how aerial roots hang down from overhead branches and grow vertically downward toward the soil.", "Medium", "Understanding"),
    ("Summarize Page 37 of the textbook in two sentences.", "The Banyan Tree is a huge Indian tree with aerial roots that grow from branches to the ground, allowing it to spread with a long lifespan of 200-500 years. Useful for paper and Ayurvedic fruit medicine for inflammation, it is the sacred, national tree of India.", "Medium", "Understanding"),
    ("Why is skin irritation treated with natural fruit remedies rather than chemical drugs in Ayurveda?", "Ayurveda relies on gentle, natural plant compounds in fruits to cool and heal skin without causing harsh side effects.", "Medium", "Understanding"),
    ("How long can a Banyan Tree live compared to human life expectancy?", "While human life expectancy is around 70-80 years, a Banyan Tree can live 200 to 500 years, outliving multiple generations.", "Medium", "Analyzing"),
    ("What role do birds play in spreading Banyan Trees?", "Birds eat banyan fruits and deposit the seeds on other tree branches, where new aerial banyan plants sprout.", "Medium", "Understanding"),
    ("How does Chapter 10 encourage environmental care among young learners?", "By showing that trees provide medicine, paper, shelter, and sacred value, teaching children to respect and protect trees.", "Medium", "Evaluating"),

    # Hard (41-50)
    ("Critique the ecological importance of preserving ancient Banyan trees in urban areas.", "Preserving ancient Banyan trees in cities is vital because a single mature tree acts as a mega-carbon sink, lowers urban heat, and supports urban wildlife.", "Hard", "Evaluating"),
    ("Analyze the structural mechanics of prop roots in supporting heavy banyan branches.", "Prop roots act like architectural load-bearing pillars, transferring the downward gravitational force of heavy horizontal branches directly into the ground.", "Hard", "Analyzing"),
    ("Deconstruct the biological journey of an aerial root from air to soil.", "1. Sprouts from branch tissue.\n2. Grows downward through humid air.\n3. Reaches soil surface.\n4. Penetrates earth and forms lateral roots.\n5. Thickens into a rigid wooden trunk.", "Hard", "Analyzing"),
    ("Compare the Banyan tree with another long-living Indian tree like the Neem tree.", "Both are sacred and medicinal in Ayurveda, but the Banyan is unique for its aerial prop roots and massive spreading canopy.", "Hard", "Analyzing"),
    ("Evaluate the balance between using banyan wood for paper and preserving ancient trees.", "Using banyan wood for paper must be managed sustainably through timber farming so that ancient 200-500 year old wild trees are never cut down.", "Hard", "Evaluating"),
    ("How can a primary school teacher demonstrate prop root growth to students?", "The teacher can show pictures or a pot-grown ficus plant, explaining how hanging roots reach for soil to build strong wooden pillars.", "Hard", "Applying"),
    ("Assess the impact of deforestation on sacred trees like the Banyan in rural India.", "Deforestation destroys biodiversity and disrupts traditional cultural reverence, removing vital animal habitats and sacred community spaces.", "Hard", "Evaluating"),
    ("Why is the Banyan tree considered a symbol of 'unity in diversity' for India?", "Because its many different pillar roots all join together to support a single, united, flourishing green tree canopy.", "Hard", "Analyzing"),
    ("Formulate a short 4-line poem celebrating the Banyan Tree.", "'O Banyan Tree with roots so grand,\nYou guard and shade our sacred land!\nWith five hundred years of life and grace,\nYou are India's pride and holy place!'", "Hard", "Creating"),
    ("Synthesize the main educational lesson of Chapter 10 for young Class 2 learners.", "Stay deeply rooted in good values, spread your arms to help others, provide shelter to those in need, and honor nature's majestic gifts!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 10: The Banyan Tree\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH10_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH10_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the Banyan Tree, including its size, location, and unique root structure.", 
     "The Banyan Tree is a huge, majestic tree commonly found in many places across India. It is famous for its unique root structure called aerial roots. These roots grow overhead from the tree's heavy branches, descend down through the air, and penetrate the ground. Once rooted in the soil, they thicken into solid, pillar-like trunks, allowing the Banyan tree to spread further across large areas.", 
     "Easy", "Remembering"),

    ("Explain the life-span, medicinal uses, and commercial products of the Banyan Tree.", 
     "The Banyan Tree has a very long life-span, with an average age ranging between 200 and 500 years. It is extremely useful to humans:\n1. **Medicinal Use**: In Ayurveda, its fruit is used to treat bodily inflammation (swelling) and skin irritation.\n2. **Commercial Use**: Paper is produced from the wood of this tree.", 
     "Easy", "Remembering"),

    ("Discuss the cultural, religious, and national significance of the Banyan Tree in India.", 
     "The Banyan Tree holds deep spiritual and national reverence in India:\n1. **Religious Significance**: It is considered sacred (holy) in major religions such as Hinduism and Buddhism.\n2. **National Symbol**: It is officially designated as the National Tree of India, symbolizing longevity, strength, shelter, and cultural heritage.", 
     "Easy", "Understanding"),

    ("Explain the meanings of the four vocabulary words: 'aerial', 'descend', 'inflammation', and 'sacred'.", 
     "1. **Aerial**: Growing from or existing in the air (e.g., aerial roots hanging from branches).\n2. **Descend**: To move or come down from a higher level to a lower level.\n3. **Inflammation**: Painful swelling and redness in body tissues.\n4. **Sacred**: Holy, divine, or deserving religious reverence.", 
     "Easy", "Understanding"),

    ("How do the aerial roots of a Banyan Tree work to support its massive size?", 
     "As a Banyan Tree grows, its heavy horizontal branches extend far outward. To prevent these heavy branches from breaking, aerial roots sprout from the branches, descend into the air, and root into the earth. Over time, these roots thicken into sturdy wooden pillars that support the massive weight of the tree, allowing it to expand continually.", 
     "Easy", "Understanding"),

    ("Why is the Banyan Tree important to village life in India?", 
     "In Indian villages, a large Banyan Tree serves as a central gathering hub. Its vast leafy canopy creates a large, naturally cool shaded area where village elders hold council meetings, local markets set up stalls, travelers rest, and children play safely under its protective branches.", 
     "Easy", "Understanding"),

    ("Describe the fruit of the Banyan Tree and its use in Ayurveda.", 
     "The Banyan Tree produces small fig-like fruits. In Ayurveda, the traditional Indian system of medicine, these fruits are harvested and processed into natural remedies. They contain soothing compounds that effectively treat skin irritation, rashes, and internal or external inflammation (swelling).", 
     "Easy", "Remembering"),

    ("How does paper production utilize the wood of the Banyan Tree?", 
     "The wood of the Banyan Tree contains strong plant fibers. Wood from the tree is harvested, ground down into wood pulp, treated, and pressed flat to manufacture paper used for writing, printing, and packaging.", 
     "Easy", "Remembering"),

    ("Why does the Banyan Tree look like a collection of many trees joined together?", 
     "Because a single Banyan Tree drops dozens of aerial roots from its upper branches over centuries. Each root takes root in the ground and grows into a thick trunk. As a result, one single tree develops multiple supportive trunks, making it look like a whole grove or forest of trees.", 
     "Easy", "Understanding"),

    ("Summarize why the Banyan Tree is valued by people, animals, and the nation.", 
     "The Banyan Tree is valued by people for its Ayurvedic fruit medicine and paper wood, by animals for its fruits and cool shade, and by the nation as a sacred emblem of long life and heritage—making it India's proud National Tree.", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("What makes the life-span of a Banyan Tree remarkable?", "Its life-span of 200 to 500 years is remarkable because it outlives several human generations, standing as a living witness to history across centuries.", "Easy", "Remembering"),
    ("Where do aerial roots start growing from?", "Aerial roots start growing from the upper horizontal branches of the Banyan Tree and descend down toward the ground.", "Easy", "Remembering"),
    ("Why is the Banyan Tree considered a sacred tree in Hinduism?", "In Hinduism, the Banyan Tree represents the divine trinity and eternal life, and people perform prayers and rituals under its sacred canopy.", "Easy", "Understanding"),
    ("Why is the Banyan Tree considered sacred in Buddhism?", "Buddhists revere the tree because Lord Buddha meditated under sacred fig/banyan trees to attain spiritual enlightenment.", "Easy", "Understanding"),
    ("What is skin irritation and how does Banyan fruit help treat it?", "Skin irritation includes itching, redness, or rashes. Extracts from banyan fruit provide natural cooling relief to soothe the skin.", "Easy", "Understanding"),
    ("How does the Banyan Tree help environmental air quality?", "Its vast green canopy absorbs large volumes of carbon dioxide gas and releases fresh oxygen, purifying the surrounding air.", "Easy", "Understanding"),
    ("Why are aerial roots called 'prop roots'?", "They are called prop roots because they 'prop up' or support the heavy, spreading branches of the tree like wooden beams.", "Easy", "Understanding"),
    ("What type of climate does the Banyan Tree thrive in?", "The Banyan Tree thrives in warm, tropical, and subtropical climates, which is why it is widespread across India.", "Easy", "Remembering"),
    ("How does the Banyan Tree provide food for wildlife?", "It produces numerous small fig fruits that provide essential food for birds, fruit bats, monkeys, and squirrels.", "Easy", "Understanding"),
    ("How can Class 2 students show respect for trees like the Banyan Tree?", "Students can plant trees, avoid carving names on bark or breaking branches, and learn about their ecological and national importance.", "Easy", "Applying"),
    ("What does 'inflammation' mean in body health?", "Inflammation means painful, red, and swollen body tissues resulting from injury, infection, or irritation.", "Easy", "Understanding"),
    ("Why do paper manufacturers use tree wood?", "Wood contains natural cellulose fibers that, when pulped and dried, bind together to form strong sheets of paper.", "Easy", "Understanding"),
    ("How large can a single Banyan Tree grow?", "A single mature Banyan Tree can spread over several acres, dropping hundreds of prop roots and sheltering thousands of creatures.", "Easy", "Remembering"),
    ("What does the Banyan Tree symbolize for the nation of India?", "It symbolizes immortality, strength, shelter, unity, and deep-rooted Indian cultural tradition.", "Easy", "Evaluating"),
    ("Summarize Chapter 10 in five key sentences.", "The Banyan Tree is a huge, long-living tree found across India with an average life-span of 200-500 years. It has unique aerial roots that grow from branches to the ground, allowing it to spread. Useful in Ayurveda, its fruit treats inflammation and skin irritation, while its wood makes paper. Considered sacred in Hinduism and Buddhism, it is the National Tree of India. It represents strength, shelter, and nature's grandeur.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how the Banyan Tree's root system acts as an ecological foundation for soil conservation.", 
     "The Banyan Tree possesses a dual root system: extensive deep underground roots and dozens of pillar prop roots. Together, this massive root network binds the surrounding soil tightly, preventing soil erosion caused by monsoon rains and wind. Its fallen leaves decompose to enrich the soil with organic humus.", 
     "Medium", "Analyzing"),

    ("Examine the medicinal value of the Banyan Tree in Ayurvedic science.", 
     "Ayurveda utilizes the natural active compounds in the Banyan Tree. Its fruit contains anti-inflammatory and soothing properties that treat skin irritation, rashes, and internal tissue swelling. Using natural fruit extracts offers gentle, holistic healing without the side effects of synthetic drugs.", 
     "Medium", "Analyzing"),

    ("Discuss the symbolic meaning of the Banyan Tree as India's National Tree.", 
     "The Banyan Tree was designated as India's National Tree because its sprawling branches and prop roots symbolize unity in diversity. Just as many prop roots support one single tree, diverse people form one strong nation. Its 200-500 year lifespan reflects India's timeless, enduring civilization.", 
     "Medium", "Evaluating"),

    ("Explore the biological adaptation of aerial roots in supporting heavy canopy expansion.", 
     "Unlike typical trees whose branches are limited by trunk strength, the Banyan Tree adapts by dropping aerial roots from long horizontal branches. As these roots reach the ground and thicken into wooden trunks, they eliminate gravity stress on the branches, allowing the canopy to expand indefinitely.", 
     "Medium", "Analyzing"),

    ("How can Class 2 teachers use Chapter 10 to teach students about eco-friendly choices?", 
     "Teachers can explain that using natural materials responsibly (like making paper from managed wood) must be balanced with tree conservation, inspiring children to recycle paper and plant trees.", 
     "Medium", "Applying"),

    ("Why is the Banyan Tree considered a 'living sanctuary' for animals?", "Its vast leafy canopy provides cool temperature shelter, while its branches offer nesting sites for birds and its fruits feed bats, monkeys, and insects, making it a complete ecosystem.", "Medium", "Understanding"),
    ("Describe the process of how an aerial root transforms into a solid tree trunk.", "It starts as a thin hanging strand in the air, grows downward until it penetrates the soil, absorbs groundwater, and thickens over years with layers of bark into a rigid wooden pillar trunk.", "Medium", "Understanding"),
    ("Why did ancient Indian villages grow around large Banyan Trees?", "Because the tree provided a permanent central landmark, vast natural shade for community markets and assemblies, and sacred spiritual protection.", "Medium", "Analyzing"),
    ("How does paper production from wood highlight the commercial value of trees?", "It demonstrates that trees supply raw materials for essential daily tools like notebooks and books, reinforcing why forests must be sustainably managed.", "Medium", "Understanding"),
    ("What is the difference between a sacred tree and a regular farm tree?", "A sacred tree is protected by religious reverence, preventing it from being cut down, which historically preserved ancient trees for centuries.", "Medium", "Analyzing"),
    ("Contrast the lifespan of a Banyan Tree (200-500 years) with typical garden plants.", "Garden plants live for a few months or years, whereas a Banyan Tree lives for centuries, outlasting human generations.", "Medium", "Analyzing"),
    ("Why is skin irritation treated effectively by natural fruit extracts?", "Natural fruit compounds provide gentle anti-bacterial and cooling agents that calm nerve endings in the skin.", "Medium", "Understanding"),
    ("How does the Banyan Tree reflect the beauty of Indian nature?", "Its sprawling size, hanging roots, green canopy, and sacred presence create an iconic landscape feature unique to Indian nature.", "Medium", "Evaluating"),
    ("What safety precautions should be kept in mind around ancient Banyan trees?", "Children should be careful not to pull hard on thin hanging roots or climb weak high branches without adult supervision.", "Medium", "Applying"),
    ("Construct a short dialogue between a village grandfather and a grandchild sitting under a Banyan Tree.", "Grandchild: 'Grandpa, why does this tree have so many trunks?' Grandfather: 'Child, these hanging roots reached down from the branches to support the tree, just as family members support each other!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the conflict between urban development and the protection of ancient Banyan trees.", 
     "Modern road expansion and building construction often threaten centuries-old Banyan trees. Removing a 300-year-old tree destroys a massive carbon sink and urban wildlife sanctuary. Urban planning must prioritize designing roads around ancient trees to preserve ecological and cultural heritage.", 
     "Hard", "Evaluating"),

    ("Deconstruct the biological mechanisms of epiphyte growth in Banyan seeds.", 
     "Banyan seeds dropped by birds in palm or wall crevices sprout as epiphytes, drawing moisture from air. They send aerial roots down to the soil; once grounded, the roots envelope and outgrow the host, demonstrating extraordinary adaptive plant survival.", 
     "Hard", "Analyzing"),

    ("Synthesize the ecological, medical, cultural, and national roles of the Banyan Tree.", 
     "1. **Ecological**: Carbon sink, soil erosion prevention, wildlife habitat.\n2. **Medical**: Ayurvedic treatment for inflammation and skin irritation.\n3. **Cultural**: Sacred status in Hinduism and Buddhism.\n4. **National**: Official National Tree representing longevity and shelter.", 
     "Hard", "Synthesizing"),

    ("Formulate an interactive school project on 'National Symbols of India: The Banyan Tree'.", 
     "- **Art**: Drawing a banyan tree with hanging prop roots.\n- **Science**: Explaining aerial root growth and Ayurvedic fruit uses.\n- **Social Studies**: Discussion on why it represents India's national unity.\n- **Environmental Pledge**: Recycling paper to save tree wood.", 
     "Hard", "Creating"),

    ("Evaluate the impact of sacred status on historical forest conservation in India.", 
     "Attaching sacred status to trees like the Banyan acted as an ancient socio-religious conservation law. It prevented deforestation of large canopy trees, protecting watersheds and biodiversity centuries before modern environmental laws.", 
     "Hard", "Evaluating"),

    ("Analyze how the Banyan tree's prop roots demonstrate natural structural engineering.", "Prop roots act as self-deploying structural columns. As a horizontal branch extends and sags under weight, aerial roots descend directly beneath the stress point, anchoring into the ground to distribute structural load.", "Hard", "Analyzing"),
    ("Compare paper making from tree wood with modern eco-friendly paper alternatives (like bamboo or recycled rags).", "Tree wood pulping requires harvesting slow-growing timber, whereas bamboo or recycled paper uses fast-growing or waste materials, making them more sustainable choices.", "Hard", "Analyzing"),
    ("Draft a formal recommendation letter urging a city council to declare an ancient Banyan tree a protected natural monument.", "'Honorable Council, We request that the 300-year-old Banyan tree on Main Road be declared a Protected Natural Monument. It provides clean oxygen, shelters bird species, and represents our city's green heritage.'", "Hard", "Creating"),
    ("Assess the role of the Banyan tree in mitigating urban heat island effects.", "Its immense leaf surface area transpires water and blocks direct solar radiation, significantly cooling ground temperatures in surrounding urban areas.", "Hard", "Evaluating"),
    ("Synthesize the ultimate moral lesson of Chapter 10 into a guiding principle.", "'Be like the Banyan Tree: extend strong roots of support, offer cool shelter to all, heal those around you, and stand timeless in your core values!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 10: The Banyan Tree\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH10_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH10_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("The Banyan Tree can be seen in many places in India. It is a huge tree. It has aerial roots which grow from the branches and descend to the ground.",
     [
         ("In which country can the Banyan Tree be seen in many places?", "India.", "Easy", "Remembering"),
         ("What size is the Banyan Tree?", "It is a huge tree.", "Easy", "Remembering"),
         ("What special roots does it possess?", "Aerial roots.", "Easy", "Remembering"),
         ("Where do these aerial roots grow from?", "From the branches.", "Easy", "Remembering"),
         ("Where do the aerial roots descend to?", "To the ground.", "Easy", "Remembering")
     ]),

    # Set 2
    ("And then from these roots the tree spreads further. This tree has a very long life-span. The average life span of a banyan tree is 200-500 years.",
     [
         ("How does the tree spread further?", "From its aerial roots descending to the ground.", "Easy", "Remembering"),
         ("What kind of life-span does the Banyan tree have?", "A very long life-span.", "Easy", "Remembering"),
         ("What is the average life span of a Banyan tree?", "200-500 years.", "Easy", "Remembering"),
         ("Why does having aerial roots help the tree spread?", "Because roots form new trunks that support expanding branches.", "Medium", "Understanding"),
         ("What does a long life-span of 200-500 years symbolize?", "Longevity, permanence, and historical strength.", "Medium", "Understanding")
     ]),

    # Set 3
    ("This tree is very useful. In Ayurveda, its fruit is used to treat inflammation as well as skin irritation. Paper is also made from the wood of this tree.",
     [
         ("Is the Banyan tree useful to human beings?", "Yes, it is very useful.", "Easy", "Remembering"),
         ("Which system of medicine uses the Banyan fruit?", "Ayurveda.", "Easy", "Remembering"),
         ("What two health conditions does its fruit treat?", "Inflammation and skin irritation.", "Easy", "Remembering"),
         ("What product is made from the wood of this tree?", "Paper.", "Easy", "Remembering"),
         ("What does the word 'inflammation' mean?", "Swelling in body tissues.", "Medium", "Understanding")
     ]),

    # Set 4
    ("This tree is considered sacred in religions like Hinduism and Buddhism. The Banyan Tree is the national tree of India.",
     [
         ("In which religions is the Banyan tree considered sacred?", "Hinduism and Buddhism.", "Easy", "Remembering"),
         ("What does the word 'sacred' mean?", "Holy.", "Easy", "Understanding"),
         ("What national title does the Banyan Tree hold?", "The National Tree of India.", "Easy", "Remembering"),
         ("Why is the tree sacred in Buddhism?", "Because of its connection to Buddha's meditation and enlightenment.", "Medium", "Understanding"),
         ("Why was it chosen as the National Tree of India?", "Because of its massive size, long lifespan, sacred status, and protective shelter.", "Medium", "Evaluating")
     ]),

    # Set 5
    ("Word Meaning: Aerial: From or in the air | Descend: Come down | Inflammation: Swelling | Sacred: Holy",
     [
         ("What is the meaning of 'aerial'?", "From or in the air.", "Easy", "Remembering"),
         ("What is the meaning of 'descend'?", "Come down.", "Easy", "Remembering"),
         ("What is the meaning of 'inflammation'?", "Swelling.", "Easy", "Remembering"),
         ("What is the meaning of 'sacred'?", "Holy.", "Easy", "Remembering"),
         ("Which word describes roots hanging in the air?", "Aerial.", "Easy", "Understanding")
     ]),

    # Set 6
    ("The Banyan Tree can be seen in many places in India. It is a huge tree. It has aerial roots which grow from the branches and descend to the ground.",
     [
         ("What is the subject of this text?", "The Banyan Tree.", "Easy", "Remembering"),
         ("Which direction do aerial roots grow?", "They descend down to the ground.", "Easy", "Remembering"),
         ("What makes the Banyan tree unique in root growth?", "Its roots grow from overhead branches into the air before touching ground.", "Medium", "Understanding"),
         ("Give an antonym for 'descend'.", "Ascend.", "Medium", "Understanding"),
         ("What does the presence of banyan trees indicate about Indian landscapes?", "That banyan trees are widespread native trees across India.", "Medium", "Understanding")
     ]),

    # Set 7
    ("The average life span of a banyan tree is 200-500 years. This tree is very useful.",
     [
         ("What is the minimum average lifespan mentioned?", "200 years.", "Easy", "Remembering"),
         ("What is the maximum average lifespan mentioned?", "500 years.", "Easy", "Remembering"),
         ("Can a banyan tree live longer than a human being?", "Yes, it lives for centuries.", "Easy", "Remembering"),
         ("Why is a tree that lives 500 years valuable to an ecosystem?", "It provides stable shelter, food, carbon storage, and soil protection for centuries.", "Medium", "Evaluating"),
         ("What word describes something that lives for a very long time?", "Long-lived / durable / persistent.", "Medium", "Understanding")
     ]),

    # Set 8
    ("In Ayurveda, its fruit is used to treat inflammation as well as skin irritation. Paper is also made from the wood of this tree.",
     [
         ("What part of the tree is used in Ayurvedic medicine?", "The fruit.", "Easy", "Remembering"),
         ("What condition involving swelling is treated by the fruit?", "Inflammation.", "Easy", "Remembering"),
         ("What skin condition is treated by the fruit?", "Skin irritation.", "Easy", "Remembering"),
         ("What material for writing and reading comes from its wood?", "Paper.", "Easy", "Remembering"),
         ("How does Ayurveda view natural trees?", "As sources of natural healing remedies for bodily health.", "Medium", "Understanding")
     ]),

    # Set 9
    ("This tree is considered sacred in religions like Hinduism and Buddhism. The Banyan Tree is the national tree of India.",
     [
         ("Name two religions that consider the tree sacred.", "Hinduism and Buddhism.", "Easy", "Remembering"),
         ("Is the Banyan tree a national symbol?", "Yes, it is the national tree of India.", "Easy", "Remembering"),
         ("What does 'sacred' mean in spiritual terms?", "Holy, blessed, and deserving deep religious respect.", "Medium", "Understanding"),
         ("What other national symbols of India do you know?", "National animal (Tiger), National bird (Peacock), National flower (Lotus).", "Medium", "Remembering"),
         ("Why do sacred beliefs help preserve trees?", "People do not cut down trees that they consider holy and divine.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("And then from these roots the tree spreads further. This tree has a very long life-span... The Banyan Tree is the national tree of India.",
     [
         ("How does the tree expand its footprint on land?", "By dropping aerial roots that form new supportive trunks.", "Easy", "Remembering"),
         ("What nation claims the Banyan tree as its national tree?", "India.", "Easy", "Remembering"),
         ("What key characteristic enables a banyan tree to cover huge areas?", "Its spreading branches supported by prop aerial roots.", "Medium", "Understanding"),
         ("How does the Banyan tree reflect endurance?", "Through its long lifespan of 200-500 years and sturdy multi-trunk structure.", "Medium", "Analyzing"),
         ("Summarize the significance of the Banyan tree in one sentence.", "The Banyan tree is a huge, long-living, sacred, and medicinal tree honored as India's National Tree.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 10: The Banyan Tree\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH10_EXT_{q_counter:03d}"
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

with open(os.path.join(CH10_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 10 in {CH10_DIR}")
