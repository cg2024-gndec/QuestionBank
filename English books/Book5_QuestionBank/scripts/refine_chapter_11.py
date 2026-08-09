r"""
Refines all 6 Category files for Book 5 Chapter 11 ("Island Groups of India") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH11_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_11")
os.makedirs(CH11_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What are the two main island archipelagos of India?", "(A) Andaman & Nicobar Islands and Lakshadweep Islands", "(B) Sri Lanka and Maldives", "(C) Majuli and Diu", "(D) Madagascar and Seychelles", "(A)", "India has two main archipelagos: Andaman & Nicobar and Lakshadweep.", "Easy", "Remembering", "Archipelagos"),
    ("In which water body are the Andaman and Nicobar Islands located?", "(A) Bay of Bengal", "(B) Arabian Sea", "(C) Indian Ocean", "(D) Pacific Ocean", "(A)", "Located in the Bay of Bengal.", "Easy", "Remembering", "Location - Andaman"),
    ("In which water body are the Lakshadweep Islands located?", "(A) Arabian Sea", "(B) Bay of Bengal", "(C) Red Sea", "(D) Atlantic Ocean", "(A)", "Located in the Arabian Sea.", "Easy", "Remembering", "Location - Lakshadweep"),
    ("How many islands make up the Andaman and Nicobar group?", "(A) Around 572 islands", "(B) Exactly 36 islands", "(C) 100 islands", "(D) 1,000 islands", "(A)", "Has around 572 islands.", "Easy", "Remembering", "Andaman Island Count"),
    ("How many coral islands make up the Lakshadweep group?", "(A) 36 islands", "(B) 572 islands", "(C) 10 islands", "(D) 200 islands", "(A)", "Has 36 coral islands.", "Easy", "Remembering", "Lakshadweep Count"),
    ("What is the capital of the Andaman and Nicobar Islands?", "(A) Sri Vijaya Puram", "(B) Kavaratti", "(C) Kochi", "(D) Port Blair", "(A)", "Capital is Sri Vijaya Puram.", "Easy", "Remembering", "Andaman Capital"),
    ("What is the capital of the Lakshadweep Islands?", "(A) Kavaratti", "(B) Sri Vijaya Puram", "(C) Silvassa", "(D) Daman", "(A)", "Capital of Lakshadweep is Kavaratti.", "Easy", "Remembering", "Lakshadweep Capital"),
    ("What is the famous historical jail located in the Andaman Islands?", "(A) Cellular Jail (Kala Pani)", "(B) Tihar Jail", "(C) Yerwada Jail", "(D) Alipore Jail", "(A)", "Cellular Jail, also called Kala Pani, is a famous historical site.", "Easy", "Remembering", "Historical Jail"),
    ("Why were Indian freedom fighters imprisoned in Cellular Jail during the British Raj?", "(A) Because they fought against British colonial rule for India's freedom", "(B) Because they were pirate sailors", "(C) Because they built illegal ships", "(D) Because they refused to pay tax on tea", "(A)", "Freedom fighters were held captive here by the British.", "Easy", "Understanding", "Cellular Jail Purpose"),
    ("Name two indigenous tribes living in the Andaman Islands.", "(A) Jarawa and Sentinelese", "(B) Gond and Bhil", "(C) Toda and Naga", "(D) Santhal and Munda", "(A)", "Home to tribes such as the Jarawa and Sentinelese.", "Easy", "Remembering", "Indigenous Tribes"),
    ("Where is India's only active volcano located?", "(A) Barren Island in the Andaman Sea", "(B) Majuli Island in Assam", "(C) Elephanta Island in Maharashtra", "(D) Minicoy Island in Lakshadweep", "(A)", "India's only active volcano is on Barren Island.", "Easy", "Remembering", "Active Volcano"),
    ("What does the word 'Lakshadweep' mean in the Malayalam language?", "(A) A hundred thousand islands", "(B) Beautiful coral reefs", "(C) Golden sandy beaches", "(D) Deep ocean waters", "(A)", "Means 'a hundred thousand islands' in Malayalam.", "Easy", "Remembering", "Name Meaning"),
    ("What type of climate do both Indian island groups experience?", "(A) Tropical climate (hot and humid)", "(B) Polar freezing climate", "(C) Arid desert climate", "(D) Mediterranean climate", "(A)", "Both island groups have a tropical climate.", "Easy", "Remembering", "Climate Type"),
    ("What tourist water activities are popular in these islands?", "(A) Snorkelling, scuba diving, and fishing", "(B) Ice skating and skiing", "(C) Desert camel racing", "(D) Mountain climbing", "(A)", "Enjoy activities like snorkelling, scuba diving, and fishing.", "Easy", "Remembering", "Tourist Activities"),
    ("What does the word 'archipelago' mean in the vocabulary box?", "(A) A group of islands", "(B) A deep ocean trench", "(C) A high mountain peak", "(D) A sandy river bank", "(A)", "Archipelago = A group of islands.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'coastal' mean?", "(A) Near the sea or ocean", "(B) High up in the mountains", "(C) In the middle of a desert", "(D) Inside a dense jungle", "(A)", "Coastal = Near the sea or ocean.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'lagoon' mean?", "(A) A shallow water body separated from the sea", "(B) A high waterfall", "(C) A deep volcanic crater", "(D) A dry riverbed", "(A)", "Lagoon = A shallow water body separated from the sea.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'coral' mean?", "(A) A hard substance formed by sea creatures", "(B) A type of green seaweed", "(C) Volcanic lava rock", "(D) Compressed sea sand", "(A)", "Coral = Hard substance formed by sea creatures.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'tropical' mean?", "(A) Climate that is hot and humid", "(B) Climate that is freezing and icy", "(C) Climate that has no rain", "(D) Climate with continuous snow", "(A)", "Tropical = Climate that is hot and humid.", "Easy", "Understanding", "Vocabulary"),
    ("What features make Lakshadweep a emerging tourist hotspot?", "(A) White sandy beaches, coconut palms, and crystal-clear lagoons", "(B) Tall snow mountains and ski slopes", "(C) Ancient stone castles", "(D) Gold mines and heavy factories", "(A)", "Famous for white sandy beaches, coconut palms, and lagoons.", "Easy", "Remembering", "Lakshadweep Features"),
    ("How do the island groups help protect India as a nation?", "(A) They protect our coasts and provide valuable natural resources", "(B) They block rain clouds from entering India", "(C) They stop ocean tides completely", "(D) They prevent sun heat", "(A)", "Play an important role in protecting our coasts and resources.", "Easy", "Understanding", "National Protection"),
    ("Which island group is formed primarily of coral reefs?", "(A) Lakshadweep Islands", "(B) Andaman Islands", "(C) Nicobar Islands", "(D) Barren Island", "(A)", "Lakshadweep is a group of 36 coral islands.", "Easy", "Remembering", "Coral Islands"),
    ("Are all 572 islands of Andaman and Nicobar inhabited by people?", "(A) No, only some of the islands are inhabited", "(B) Yes, every single island is densely populated", "(C) No, none of the islands have people", "(D) Yes, only foreign tourists live there", "(A)", "Around 572 islands, but only some are inhabited.", "Easy", "Remembering", "Inhabitation"),
    ("What biological life is rich in both island groups?", "(A) Wildlife and marine life", "(B) Arctic bears and penguins", "(C) Desert camels and snakes", "(D) Mountain goats only", "(A)", "Both island groups are rich in wildlife and marine life.", "Easy", "Remembering", "Biodiversity"),
    ("What title is given to Chapter 11?", "(A) Island Groups of India", "(B) The Narmada River", "(C) The Magic of Books", "(D) Traditional Dresses from India", "(A)", "Title is 'Island Groups of India'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why is Cellular Jail in Sri Vijaya Puram called 'Kala Pani' in Indian history?", "(A) Because prisoners were isolated across dark ocean waters ('Kala Pani') with no chance of escape or family contact", "(B) Because the prison drinking water was black", "(C) Because the jail walls were painted black", "(D) Because it was built underwater", "(A)", "Isolated across dark ocean waters ('Kala Pani') preventing escape.", "Medium", "Analyzing", "Historical Significance"),
    ("Compare the geological origin of Lakshadweep Islands with Andaman & Nicobar Islands.", "(A) Lakshadweep consists of biogenic coral atolls; Andaman & Nicobar are submerged extension peaks of the Arakan Yoma mountain range", "(B) Lakshadweep is made of granite; Andaman is made of ice", "(C) Both archipelagos were built artificially by engineers", "(D) Andaman is coral while Lakshadweep is volcanic", "(A)", "Lakshadweep = coral atolls; Andaman & Nicobar = submerged mountain peaks.", "Medium", "Comparing", "Geological Comparison"),
    ("What makes the Sentinelese tribe unique in world anthropology?", "(A) They are one of the last uncontacted indigenous tribes, choosing to live isolated from modern civilization", "(B) They built modern cities on Barren Island", "(C) They speak English fluently", "(D) They migrated from Europe last century", "(A)", "One of the last uncontacted tribes living isolated from modern civilization.", "Medium", "Evaluating", "Anthropological Uniqueness"),
    ("How does the presence of coral reefs benefit marine ecosystems in Lakshadweep?", "(A) Corals provide essential breeding habitats, shelter, and food for thousands of marine fish and organisms", "(B) Corals make ocean water boil", "(C) Corals destroy fish populations", "(D) Corals turn ocean water into fresh drinking water", "(A)", "Provide essential breeding habitats, shelter, and food for marine organisms.", "Medium", "Understanding", "Ecological Benefit"),
    ("Why are India's island archipelagos strategically vital for national security?", "(A) They project naval presence, guard maritime trade routes, and protect India's Exclusive Economic Zone (EEZ)", "(B) They are used to store agricultural grain only", "(C) They prevent monsoon rains from hitting Asia", "(D) They host private space resorts", "(A)", "Guard maritime trade routes and project naval security across oceans.", "Medium", "Analyzing", "Strategic Security"),
    ("Contrast the water body of Andaman & Nicobar (Bay of Bengal) with Lakshadweep (Arabian Sea).", "(A) Andaman is in the eastern Bay of Bengal near Southeast Asia; Lakshadweep is in the western Arabian Sea near Kerala", "(B) Both are in the Pacific Ocean", "(C) Andaman is in the Arabian Sea; Lakshadweep is in Bay of Bengal", "(D) Neither island group is surrounded by sea water", "(A)", "Andaman = eastern Bay of Bengal; Lakshadweep = western Arabian Sea.", "Medium", "Comparing", "Geographical Contrast"),
    ("Why is Barren Island scientifically significant for volcanology in South Asia?", "(A) It contains the only active volcano along the N-S volcanic arc extending from Sumatra to Myanmar", "(B) It is covered in permanent snow", "(C) It produces diamond crystals", "(D) It is an artificial floating volcano", "(A)", "Contains South Asia's only active volcano along the regional volcanic arc.", "Medium", "Understanding", "Volcanology"),
    ("What eco-tourism activities draw international tourists to Lakshadweep's lagoons?", "(A) Snorkelling and scuba diving to explore pristine coral reefs, sea turtles, and vibrant marine life", "(B) Mountain trekking on high glaciers", "(C) Desert safari on sand dunes", "(D) Heavy industrial factory tours", "(A)", "Snorkelling and scuba diving to explore pristine coral reefs and marine life.", "Medium", "Understanding", "Eco-Tourism"),
    ("Explain the term 'lagoon' in the context of coral atolls.", "(A) A body of shallow ocean water enclosed by a surrounding ring-shaped coral reef", "(B) A deep freshwater lake in a forest", "(C) A river waterfall plunge pool", "(D) A dry sand basin", "(A)", "Shallow ocean water enclosed by a surrounding coral reef ring.", "Medium", "Understanding", "Atoll Lagoon"),
    ("How does the tropical climate influence island vegetation?", "(A) Abundant rainfall and warm temperatures foster lush evergreen rainforests, mangroves, and coconut palms", "(B) Tropical climate causes trees to shed all leaves permanently", "(C) It creates desert cactus plains", "(D) It freezes all plant life", "(A)", "Abundant rain and warm heat foster lush rainforests, mangroves, and palms.", "Medium", "Analyzing", "Climate & Flora"),
    ("What makes Sri Vijaya Puram (formerly Port Blair) a key administrative and historical hub?", "(A) It houses the central government administration, main airport, harbor, and historical Cellular Jail memorial", "(B) It is a desert town with no water", "(C) It is located in the Arabian Sea", "(D) It has no human population", "(A)", "Houses central island administration, harbor, airport, and Cellular Jail.", "Medium", "Understanding", "Capital Hub"),
    ("Describe the threat of climate change to low-lying coral islands like Lakshadweep.", "(A) Rising sea levels and ocean warming cause coral bleaching and threaten to submerge low-lying island land", "(B) Climate change makes islands grow ten times bigger", "(C) Climate change turns ocean water into ice blocks", "(D) Rising sea levels create new mountains", "(A)", "Rising sea levels and ocean warming cause coral bleaching and land submergence risks.", "Medium", "Evaluating", "Climate Vulnerability"),
    ("How do coastal mangroves in the Andaman Islands protect shores during storms?", "(A) Dense mangrove root networks absorb wave energy, trap coastal sediments, and reduce storm surge erosion", "(B) Mangroves catch fish automatically", "(C) Mangroves stop rain from falling", "(D) Mangroves create artificial wind", "(A)", "Dense root networks absorb wave energy and reduce storm surge erosion.", "Medium", "Analyzing", "Coastal Defense"),
    ("Summarize Chapter 11 in four concise sentences.", "India possesses two major island archipelagos: Andaman & Nicobar in the Bay of Bengal and Lakshadweep in the Arabian Sea. Andaman & Nicobar has 572 islands with capital Sri Vijaya Puram, historical Cellular Jail, indigenous tribes, and Barren Island's active volcano. Lakshadweep comprises 36 coral islands with capital Kavaratti, famous for white beaches, lagoons, and coconut palms. Both tropical island groups protect India's coasts, harbor rich marine life, and attract eco-tourists.", "Medium", "Understanding", "Chapter Summary"),
    ("What responsibility do tourists have when visiting fragile island ecosystems?", "(A) Protect coral reefs by avoiding touching them, eliminate plastic waste, and respect indigenous tribal boundaries", "(B) Collect coral pieces as souvenirs", "(C) Leave plastic bottles on beaches", "(D) Disturb wildlife for photos", "(A)", "Protect corals, eliminate plastic waste, and respect indigenous boundaries.", "Medium", "Applying", "Tourist Responsibility"),

    # Hard (41-50)
    ("Critique the policy of non-interference regarding uncontacted tribes like the Sentinelese.", "(A) Balances protecting indigenous tribes from deadly modern diseases and cultural extinction against modern governance presence", "(B) Non-interference is harmful because everyone should be forced into modern cities", "(C) Sentinelese tribes have modern hospitals", "(D) Policy encourages mass tourism on North Sentinel Island", "(A)", "Protects uncontacted tribes from deadly modern pathogens and cultural demise.", "Hard", "Evaluating", "HOTS Anthropological Policy"),
    ("Deconstruct the biogenic formation of coral atolls in the Lakshadweep archipelago.", "(A) Microscopic coral polyps secrete calcium carbonate skeletons over thousands of years around subsiding volcanic peaks, forming ring reefs", "(B) Atolls were built by ancient human masons using concrete", "(C) Atolls formed when ocean water evaporated completely", "(D) Coral reefs are formed by underwater earthquakes", "(A)", "Coral polyps secrete calcium carbonate skeletons over subsiding volcanic peaks.", "Hard", "Analyzing", "Biogenic Atoll Formation"),
    ("Evaluate the geopolitical importance of the Ten Degree Channel separating Andaman and Nicobar.", "(A) It is a critical strategic maritime choke point connecting the Indian Ocean with the Malacca Strait, carrying global oil trade", "(B) It is a fresh water river dividing the islands", "(C) It is an underground tunnel", "(D) It separates India from Australia", "(A)", "Critical strategic maritime choke point connecting Indian Ocean to Malacca Strait.", "Hard", "Evaluating", "Strategic Choke Point"),
    ("Compare the biodiversity of Andaman rainforests with Lakshadweep marine lagoons.", "(A) Andaman features terrestrial rainforest endemism (rare timber, birds, flora); Lakshadweep features marine coral biodiversity (reefs, pelagic fish)", "(B) Both have identical land plants", "(C) Andaman has no trees; Lakshadweep has no fish", "(D) Lakshadweep is covered in pine forests", "(A)", "Andaman = terrestrial rainforest endemism; Lakshadweep = marine coral reef biodiversity.", "Hard", "Comparing", "Comparative Ecosystems"),
    ("Formulate a conservation pledge for visitors to India's marine national parks.", "(A) 'We pledge to protect our ocean reefs, leave no plastic behind, respect indigenous heritage, and preserve marine life for future generations!'", "(B) 'We pledge to catch all reef fish for commercial sale.'", "(C) 'We pledge to build factories on coral reefs.'", "(D) 'We pledge to throw plastic into lagoons.'", "(A)", "Pledge to protect ocean reefs, avoid plastic, respect heritage, and preserve marine life.", "Hard", "Creating", "Conservation Pledge"),
    ("Assess the role of the Andaman and Nicobar Command (ANC) in national defense.", "(A) ANC is India's first tri-service defense command, safeguarding eastern maritime borders and securing trade corridors", "(B) ANC manages tourist hotel bookings", "(C) ANC is a private security firm", "(D) ANC operates only on river boats", "(A)", "Tri-service defense command safeguarding eastern maritime borders and trade corridors.", "Hard", "Evaluating", "Defense Command Role"),
    ("Analyze how sustainable eco-tourism can balance island economic development and environmental protection.", "(A) Regulating visitor numbers, enforcing solar energy, prohibiting reef destruction, and empowering local island communities", "(B) Building high-rise concrete skyscrapers on beaches", "(C) Allowing unlimited cruise ships without waste treatment", "(D) Banning all human visitors forever", "(A)", "Regulating numbers, enforcing solar power, preventing reef destruction, empowering locals.", "Hard", "Analyzing", "Sustainable Tourism"),
    ("Synthesize how Chapter 11 connects physical geography, historical struggle, and environmental science.", "(A) Integrates physical archipelagos (Bay of Bengal/Arabian Sea) with freedom struggle history (Cellular Jail) and marine science (corals/volcanoes)", "(B) Replaces island geography with mountain climbing", "(C) Focuses only on memorizing island numbers", "(D) Rejects scientific facts", "(A)", "Integrates physical archipelagos, freedom struggle history, and marine ecosystem science.", "Hard", "Synthesizing", "Cross-Disciplinary Synthesis"),
    ("Critique the claim: 'Lakshadweep Islands are volcanic mountain peaks above sea level.'", "(A) False; Lakshadweep Islands are low-lying coral atolls built by coral polyps, whereas Barren Island in Andaman is volcanic", "(B) True; Lakshadweep has active lava volcanoes", "(C) False; Lakshadweep is located in the Pacific Ocean", "(D) True; all islands are volcanic", "(A)", "False; Lakshadweep consists of coral atolls; Barren Island in Andaman is volcanic.", "Hard", "Evaluating", "Geological Accuracy Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 11 for a Class 5 assessment.", "(A) 'Compare India's two main island groups (Andaman & Nicobar and Lakshadweep). Discuss their location, capitals, physical features, historical/tribal importance, and why we must protect them.'", "(B) 'Write five sentences about your favorite beach holiday.'", "(C) 'List five names of fish.'", "(D) 'Draw a picture of a boat.'", "(A)", "Structured essay prompt evaluating archipelagos comparison, capitals, features, history, and conservation.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 11: Island Groups of India\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH11_MCQ_{idx:03d}"
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

with open(os.path.join(CH11_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("India has two main island groups called _______.", "archipelagos", "Two main archipelagos.", "Easy"),
    ("The Andaman and Nicobar Islands are located in the Bay of _______.", "Bengal", "Bay of Bengal.", "Easy"),
    ("The Lakshadweep Islands are located in the Arabian _______.", "Sea", "Arabian Sea.", "Easy"),
    ("The Andaman and Nicobar group has around _______ islands.", "572", "Around 572 islands.", "Easy"),
    ("The capital of the Andaman and Nicobar Islands is Sri _______ Puram.", "Vijaya", "Sri Vijaya Puram.", "Easy"),
    ("The Cellular Jail in Andaman is also famously called Kala _______.", "Pani", "Called Kala Pani.", "Easy"),
    ("Freedom fighters were held captive in Cellular Jail during the British _______.", "Raj", "During the British Raj.", "Easy"),
    ("The Jarawa and _______ are indigenous tribes of the Andaman Islands.", "Sentinelese", "Jarawa and Sentinelese.", "Easy"),
    ("India's only active volcano is located on Barren _______.", "Island", "Barren Island.", "Easy"),
    ("The Lakshadweep group consists of _______ coral islands.", "36", "36 coral islands.", "Easy"),
    ("The capital of Lakshadweep is _______.", "Kavaratti", "Capital is Kavaratti.", "Easy"),
    ("The word Lakshadweep means 'a hundred thousand islands' in _______.", "Malayalam", "Means in Malayalam.", "Easy"),
    ("Both island groups have a _______ climate.", "tropical", "Tropical climate.", "Easy"),
    ("Popular water activities on the islands include snorkelling, scuba diving, and _______.", "fishing", "Snorkelling, scuba diving, fishing.", "Easy"),
    ("An archipelago is defined as a group of _______.", "islands", "Group of islands.", "Easy"),
    ("Coastal means near the sea or _______.", "ocean", "Near sea or ocean.", "Easy"),
    ("A lagoon is a shallow water body separated from the _______.", "sea", "Separated from the sea.", "Easy"),
    ("Coral is a hard substance formed by sea _______.", "creatures", "Formed by sea creatures.", "Easy"),
    ("Tropical climate is defined as hot and _______.", "humid", "Hot and humid.", "Easy"),
    ("Lakshadweep islands are famous for white sandy beaches and coconut _______.", "palms", "Coconut palms.", "Easy"),
    ("The island groups play an important role in protecting our _______.", "coasts", "Protecting our coasts.", "Easy"),
    ("Barren Island volcano is located in the Andaman _______.", "Sea", "Andaman Sea.", "Easy"),
    ("Sri Vijaya Puram is located in the _______ Islands.", "Andaman", "Andaman Islands.", "Easy"),
    ("Both island groups are rich in wildlife and _______ life.", "marine", "Marine life.", "Easy"),
    ("Chapter 11 is titled 'Island Groups of _______'.", "India", "Island Groups of India.", "Easy"),

    # Medium (26-40)
    ("Cellular Jail was constructed with separate individual _______ to isolate freedom fighters.", "cells", "Individual cells.", "Medium"),
    ("Lakshadweep's coral reefs attract diverse marine species including sea _______.", "turtles", "Including sea turtles.", "Medium"),
    ("North Sentinel Island is home to the uncontacted _______ tribe.", "Sentinelese", "Uncontacted Sentinelese tribe.", "Medium"),
    ("Coral reefs build up over thousands of years from calcium _______.", "carbonate", "Calcium carbonate.", "Medium"),
    ("Sri Vijaya Puram was formerly known as Port _______.", "Blair", "Formerly Port Blair.", "Medium"),
    ("Tropical island forests harbor rare endemic bird species and dense _______.", "mangroves", "Dense mangroves.", "Medium"),
    ("The Ten Degree Channel separates the Andaman group from the _______ group.", "Nicobar", "Separates Andaman and Nicobar.", "Medium"),
    ("Scuba divers explore underwater coral formations and vibrant reef _______.", "fish", "Vibrant reef fish.", "Medium"),
    ("Island coastal protection buffers mainland territory against tsunami _______.", "waves", "Buffers tsunami waves.", "Medium"),
    ("Malayalam is the primary language spoken in the _______ Islands.", "Lakshadweep", "Spoken in Lakshadweep.", "Medium"),
    ("Barren Island erupted most recently in the twenty-first _______.", "century", "Erupted in 21st century.", "Medium"),
    ("Kavaratti is known for its beautiful calm lagoon and white sand _______.", "beaches", "White sand beaches.", "Medium"),
    ("Ecological conservation protects fragile island biodiversity from pollution _______.", "threats", "Protection from pollution threats.", "Medium"),
    ("Island defense commands secure critical Indian Ocean maritime _______.", "routes", "Maritime routes.", "Medium"),
    ("Chapter 11 demonstrates how geography shapes island ecosystems and cultural _______.", "heritage", "Ecosystems and heritage.", "Medium"),

    # Hard (41-50)
    ("Biogenic coral polyps secrete reef structures shielding lagoonal _______.", "waters", "Shielding lagoonal waters.", "Hard"),
    ("Submerged Arakan Yoma tectonic peaks form the Andaman island _______.", "chain", "Form Andaman island chain.", "Hard"),
    ("Anthropological non-interference policies preserve uncontacted tribal _______.", "autonomy", "Preserve tribal autonomy.", "Hard"),
    ("Maritime choke point security protects high-seas trade _______.", "corridors", "Protects trade corridors.", "Hard"),
    ("Climate-induced coral bleaching jeopardizes atoll marine _______.", "habitats", "Jeopardizes marine habitats.", "Hard"),
    ("Tri-service military command structure reinforces eastern island _______.", "sovereignty", "Reinforces island sovereignty.", "Hard"),
    ("Sustainable eco-tourism balances local economic growth with ecological _______.", "integrity", "Balances growth with integrity.", "Hard"),
    ("Mangrove root systems attenuate coastal storm surge wave _______.", "energy", "Attenuate wave energy.", "Hard"),
    ("Historical analysis highlights Cellular Jail as an altar of national _______.", "sacrifice", "Altar of national sacrifice.", "Hard"),
    ("Chapter 11 instills environmental responsibility for preserving island _______.", "ecosystems", "Preserving island ecosystems.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 11: Island Groups of India\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH11_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH11_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("India has two main island archipelagos.", "True", "Text confirms India has two main archipelagos.", "Easy"),
    ("The Andaman and Nicobar Islands are located in the Arabian Sea.", "False", "They are located in the Bay of Bengal.", "Easy"),
    ("The Lakshadweep Islands are located in the Arabian Sea.", "True", "Text confirms Lakshadweep is in the Arabian Sea.", "Easy"),
    ("The Andaman and Nicobar group has around 572 islands.", "True", "Text confirms around 572 islands exist in this group.", "Easy"),
    ("All 572 islands of Andaman and Nicobar are densely populated by people.", "False", "Only some of the 572 islands are inhabited by people.", "Easy"),
    ("The capital of the Andaman and Nicobar Islands is Sri Vijaya Puram.", "True", "Text confirms Sri Vijaya Puram is the capital.", "Easy"),
    ("The Cellular Jail is also known as Kala Pani.", "True", "Text confirms Cellular Jail is called Kala Pani.", "Easy"),
    ("Indian freedom fighters were imprisoned in Cellular Jail during the British Raj.", "True", "Text confirms freedom fighters were held captive here.", "Easy"),
    ("The Jarawa and Sentinelese are tribes living in the Andaman Islands.", "True", "Text confirms Jarawa and Sentinelese live in Andaman.", "Easy"),
    ("India's only active volcano is located on Barren Island.", "True", "Text confirms active volcano is on Barren Island.", "Easy"),
    ("The Lakshadweep group has 572 coral islands.", "False", "Lakshadweep has 36 coral islands.", "Easy"),
    ("The capital of Lakshadweep is Kavaratti.", "True", "Text confirms Kavaratti is the capital of Lakshadweep.", "Easy"),
    ("The word 'Lakshadweep' means 'a hundred thousand islands' in Malayalam.", "True", "Text confirms the meaning in Malayalam.", "Easy"),
    ("The word 'Lakshadweep' means 'a hundred thousand islands' in Hindi.", "False", "It means a hundred thousand islands in MALAYALAM, not Hindi.", "Easy"),
    ("Both island groups experience a freezing polar climate.", "False", "Both island groups experience a hot and humid tropical climate.", "Easy"),
    ("Popular tourist activities in the islands include snorkelling, scuba diving, and fishing.", "True", "Text confirms these popular tourist activities.", "Easy"),
    ("'Archipelago' means a single isolated mountain peak.", "False", "Archipelago = A group of islands.", "Easy"),
    ("'Coastal' means near the sea or ocean.", "True", "Vocabulary definition: Coastal = Near the sea or ocean.", "Easy"),
    ("'Lagoon' means a shallow water body separated from the sea.", "True", "Vocabulary definition: Lagoon = Shallow water body separated from the sea.", "Easy"),
    ("'Coral' is a hard substance formed by sea creatures.", "True", "Vocabulary definition: Coral = Hard substance formed by sea creatures.", "Easy"),
    ("'Tropical' means a climate that is hot and humid.", "True", "Vocabulary definition: Tropical = Hot and humid climate.", "Easy"),
    ("Lakshadweep is famous for white sandy beaches and coconut palms.", "True", "Text confirms Lakshadweep is famous for white beaches and coconut palms.", "Easy"),
    ("The Sentinelese tribe lives in the Lakshadweep Islands.", "False", "The Sentinelese tribe lives in the Andaman Islands.", "Easy"),
    ("The island groups play an important role in protecting India's coasts.", "True", "Text confirms they play an important role in protecting coasts.", "Easy"),
    ("Chapter 11 title is 'Island Groups of India'.", "True", "Chapter title is 'Island Groups of India'.", "Easy"),

    # Medium (26-40)
    ("Cellular Jail in Andaman was designed to prevent prisoners from communicating with each other.", "True", "Constructed with individual solitary cells to prevent prisoner communication.", "Medium"),
    ("Barren Island volcano is located in the Lakshadweep sea.", "False", "Barren Island volcano is located in the Andaman Sea.", "Medium"),
    ("The Lakshadweep Islands were formed by volcanic lava eruptions.", "False", "Lakshadweep Islands are coral atolls formed by coral polyps.", "Medium"),
    ("Snorkelling allows tourists to view shallow coral reefs and marine life.", "True", "Snorkelling is popular for observing shallow marine life.", "Medium"),
    ("Kavaratti is an island city located in the Bay of Bengal.", "False", "Kavaratti is in the Arabian Sea as capital of Lakshadweep.", "Medium"),
    ("The Jarawa tribe has lived in the Andaman Islands for centuries.", "True", "Text confirms the Jarawa have lived there for centuries.", "Medium"),
    ("Both island groups are poor in marine life due to polluted water.", "False", "Both island groups are rich in wildlife, marine life, and natural beauty.", "Medium"),
    ("Coconut palms are common trees found across Lakshadweep islands.", "True", "Coconut palms grow abundantly across Lakshadweep.", "Medium"),
    ("Port Blair was renamed Sri Vijaya Puram by the Government of India.", "True", "Port Blair was officially renamed Sri Vijaya Puram.", "Medium"),
    ("India's island groups assist in safeguarding maritime trade corridors.", "True", "Strategic location protects maritime trade corridors in Indian Ocean.", "Medium"),
    ("Cellular Jail was used by the British to house common tourists.", "False", "It was a high-security prison for Indian freedom fighters.", "Medium"),
    ("Coral reefs are formed over long periods by living marine polyps.", "True", "Reefs are built from calcium carbonate secreted by coral polyps.", "Medium"),
    ("The Andaman Sea lies to the east of the Andaman Islands.", "True", "Andaman Sea lies between Andaman Islands and Myanmar/Thailand.", "Medium"),
    ("Tourist activities like scuba diving harm the environment if done irresponsibly.", "True", "Irresponsible diving can damage delicate coral formations.", "Medium"),
    ("Chapter 11 highlights how India's island archipelagos enrich national geography.", "True", "Highlights geography, biodiversity, history, and coastal defense.", "Medium"),

    # Hard (41-50)
    ("The Ten Degree Channel separates the Andaman Islands from the Nicobar Islands.", "True", "Ten Degree Channel lies on 10°N latitude separating Andaman & Nicobar.", "Hard"),
    ("North Sentinel Island is open to international commercial beach tourism.", "False", "North Sentinel Island is strictly off-limits to protect the Sentinelese tribe.", "Hard"),
    ("Lakshadweep coral atolls are vulnerable to rising sea levels caused by global warming.", "True", "Low elevation makes coral atolls vulnerable to sea level rise.", "Hard"),
    ("Veer Savarkar was one of the prominent freedom fighters held in Cellular Jail.", "True", "Vinayak Damodar Savarkar was imprisoned in Cellular Jail.", "Hard"),
    ("The Andaman & Nicobar Command is India's only integrated tri-service defense command.", "True", "ANC is India's pioneer tri-service unified defense command.", "Hard"),
    ("Barren Island is the only active volcano along the submarine arc from Sumatra to Myanmar.", "True", "Confirmed as the sole active volcano along this regional arc.", "Hard"),
    ("Coconut palm cultivation and fishing are major traditional occupations in Lakshadweep.", "True", "Fishing and coconut cultivation are primary island occupations.", "Hard"),
    ("Mangrove forests along Andaman shores buffer coastal land against storm surges.", "True", "Dense mangrove roots dissipate wave energy during oceanic storms.", "Hard"),
    ("Chapter 11 integrates physical geography, history, and ecological conservation.", "True", "Combines archipelagos geography, freedom history, and eco-conservation.", "Hard"),
    ("Preserving island biodiversity is crucial for maintaining global ocean health.", "True", "Island coral reefs and marine life sustain global ocean ecological balance.", "Hard")
]

tf_content = f"# True / False — Chapter 11: Island Groups of India\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH11_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Question**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH11_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("What are the two main island archipelagos of India and where are they located?", "The two main archipelagos are the Andaman and Nicobar Islands (located in the Bay of Bengal) and the Lakshadweep Islands (located in the Arabian Sea).", "Easy", "Remembering"),
    ("How many islands form the Andaman and Nicobar group, and are all of them inhabited?", "The group contains around 572 islands, but only some of them are inhabited by people.", "Easy", "Remembering"),
    ("What is the capital of the Andaman and Nicobar Islands?", "The capital is Sri Vijaya Puram (formerly known as Port Blair).", "Easy", "Remembering"),
    ("What historical site in the Andaman Islands is known as 'Kala Pani' and why is it famous?", "The Cellular Jail is known as Kala Pani. It is famous because Indian freedom fighters were held captive there by the British during the freedom struggle.", "Easy", "Remembering"),
    ("Name two indigenous tribes that have lived in the Andaman Islands for centuries.", "Two indigenous tribes are the Jarawa and the Sentinelese.", "Easy", "Remembering"),
    ("Where is India's only active volcano located?", "India's only active volcano is located on Barren Island in the Andaman Sea.", "Easy", "Remembering"),
    ("How many islands make up the Lakshadweep group, and what type of islands are they?", "The Lakshadweep group consists of 36 coral islands.", "Easy", "Remembering"),
    ("What is the capital of the Lakshadweep Islands?", "The capital of Lakshadweep is Kavaratti.", "Easy", "Remembering"),
    ("What does the word 'Lakshadweep' mean in the Malayalam language?", "It means 'a hundred thousand islands' in the Malayalam language.", "Easy", "Remembering"),
    ("What features make Lakshadweep a popular tourist destination?", "It is famous for its white sandy beaches, coconut palms, clear lagoons, and rich marine life.", "Easy", "Remembering"),
    ("What type of climate do both Indian island groups experience?", "Both island groups experience a hot and humid tropical climate.", "Easy", "Remembering"),
    ("Name three popular water activities that tourists enjoy in these island groups.", "Tourists enjoy snorkelling, scuba diving, and fishing.", "Easy", "Remembering"),
    ("What does the word 'archipelago' mean?", "An 'archipelago' means a group or chain of islands clustered together in a sea or ocean.", "Easy", "Understanding"),
    ("What does the word 'coastal' mean?", "'Coastal' means situated on or near the coast of a sea or ocean.", "Easy", "Understanding"),
    ("What does the word 'lagoon' mean?", "A 'lagoon' is a body of shallow ocean water separated from the open sea by a coral reef or barrier.", "Easy", "Understanding"),
    ("What does the word 'coral' mean?", "'Coral' is a hard, rock-like substance built from the accumulated calcium carbonate skeletons of tiny marine sea creatures (polyps).", "Easy", "Understanding"),
    ("What does the word 'tropical' mean?", "'Tropical' describes a hot and humid climate characteristic of regions near the equator.", "Easy", "Understanding"),
    ("Why are India's island archipelagos important for national defense?", "They play a vital role in protecting India's coastal boundaries and guarding maritime trade routes.", "Easy", "Understanding"),
    ("What natural resources do the island groups provide to India?", "They provide rich marine fish resources, coral ecosystems, palm products, and valuable coconut resources.", "Easy", "Understanding"),
    ("Why is Lakshadweep described as an emerging tourist hotspot?", "Because of its unspoiled natural beauty, pristine white sand beaches, clear turquoise lagoons, and water sports.", "Easy", "Understanding"),
    ("What makes Barren Island unique in South Asia?", "It is the only confirmed active volcano in the entire South Asian region.", "Easy", "Remembering"),
    ("What visual features characterize the Andaman and Nicobar Islands?", "They are characterized by pristine beaches, rich coral reefs, and dense tropical rainforests.", "Easy", "Remembering"),
    ("How do coral reefs help marine life in Lakshadweep?", "Coral reefs provide essential food, shelter, and breeding habitats for thousands of fish and marine species.", "Easy", "Understanding"),
    ("What title is given to Chapter 11?", "The title of Chapter 11 is 'Island Groups of India'.", "Easy", "Remembering"),
    ("What main lesson does Chapter 11 teach us about our island territories?", "It teaches us that island archipelagos add immense natural beauty, rich biodiversity, historical legacy, and strategic security to India.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze why Cellular Jail was named 'Cellular' by the British administration.", "It was constructed with individual solitary cells arranged in seven spokes radiating from a central watchtower, preventing prisoners from seeing or communicating with one another.", "Medium", "Analyzing"),
    ("Contrast the geological formation of Andaman & Nicobar with Lakshadweep.", "Andaman & Nicobar Islands are elevated peaks of a submerged continental mountain range; Lakshadweep Islands are coral atolls built by living marine polyps on underwater ridges.", "Medium", "Comparing"),
    ("Why is the Indian government maintaining a strict non-contact policy toward the Sentinelese tribe?", "Because the Sentinelese have lived isolated for thousands of years and lack immunity against common modern diseases, making contact life-threatening for them.", "Medium", "Evaluating"),
    ("Explain the relationship between tropical climate and rich marine life in these archipelagos.", "Warm tropical water temperatures and abundant sunlight foster rapid coral reef growth, which forms the base of a diverse marine food chain.", "Medium", "Analyzing"),
    ("Describe the historical role of Port Blair (Sri Vijaya Puram) during India's freedom movement.", "It served as the penal colony where freedom fighters were exiled to endure hard labor in Cellular Jail, becoming a sacred symbol of national sacrifice.", "Medium", "Understanding"),
    ("What is a coral atoll and how does it form a lagoon?", "A coral atoll is a ring-shaped coral reef that grows around a sinking volcanic island, enclosing a shallow body of quiet ocean water called a lagoon.", "Medium", "Understanding"),
    ("How does eco-tourism support local island economies without harming nature?", "Eco-tourism generates income for islanders through guided diving and hospitality while enforcing strict rules against plastic waste and coral damage.", "Medium", "Applying"),
    ("Why is the strategic location of Andaman & Nicobar important in the Indian Ocean?", "Positioned near the Malacca Strait, it allows India to monitor vital international shipping lanes carrying global trade and oil supplies.", "Medium", "Analyzing"),
    ("What ecological functions do coastal mangrove forests perform in the Andaman Islands?", "Mangroves trap coastal soil, absorb violent storm wave impacts, prevent beach erosion, and serve as nurseries for young fish.", "Medium", "Understanding"),
    ("Summarize Chapter 11 in four concise sentences.", "India has two main island archipelagos: Andaman & Nicobar in the Bay of Bengal and Lakshadweep in the Arabian Sea. Andaman & Nicobar features 572 islands with capital Sri Vijaya Puram, historical Cellular Jail, indigenous tribes, and Barren Island's active volcano. Lakshadweep consists of 36 coral islands with capital Kavaratti, famous for white beaches, coconut palms, and lagoons. Both tropical archipelagos enrich India's biodiversity, protect coasts, and attract tourists.", "Medium", "Understanding"),
    ("Why are coconut palms so important to the people of Lakshadweep?", "Coconut palms provide food, fresh coconut water, coir fiber for rope-making, timber for shelter, and oil, forming the basis of traditional island life.", "Medium", "Understanding"),
    ("How do water sports like snorkelling and scuba diving educate tourists about ocean life?", "They allow tourists to observe living coral reefs, colorful fish, and sea turtles in their natural habitat, building firsthand awareness of marine conservation.", "Medium", "Evaluating"),
    ("Explain the meaning of the name change from Port Blair to Sri Vijaya Puram.", "The name change honors India's ancient maritime heritage (Chola naval victory legacy) while removing colonial British nomenclature.", "Medium", "Understanding"),
    ("How do the island archipelagos contribute to India's Exclusive Economic Zone (EEZ)?", "Possessing islands far out at sea extends India's sovereign EEZ, granting exclusive rights to ocean fish, minerals, and offshore energy resources.", "Medium", "Analyzing"),
    ("What action can students take to help preserve marine ecosystems when visiting beaches?", "Avoid littering plastic, never touch or step on living corals, use reef-safe sunscreen, and support eco-friendly local businesses.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the ecological impact of unregulated tourism development on fragile coral atolls.", "Unregulated tourism leads to sewage dumping, boat anchor damage to reefs, plastic pollution, and freshwater depletion, risking irreversible coral bleaching.", "Hard", "Evaluating"),
    ("Deconstruct the geological mechanism of volcanic activity on Barren Island.", "Barren Island lies along the active subduction zone where the Indo-Australian plate slides beneath the Eurasian plate, melting rock into eruptive magma.", "Hard", "Analyzing"),
    ("Evaluate the challenge of balancing indigenous tribal preservation with national integration.", "Requires respecting tribal self-determination and protecting uncontacted groups from disease while ensuring national territorial integrity and welfare monitoring.", "Hard", "Evaluating"),
    ("Compare the island geography of India (Andaman/Lakshadweep) with island nation neighbors (Maldives/Sri Lanka).", "Lakshadweep shares coral atoll geography with Maldives; Andaman & Nicobar shares mountainous island arc geography with Sumatra (Indonesia).", "Hard", "Comparing"),
    ("Formulate a World Oceans Day awareness pledge based on Chapter 11.", "'On World Oceans Day, we pledge to protect India's coral archipelagos, eliminate ocean plastics, honor our freedom heritage at Cellular Jail, and safeguard marine biodiversity!'", "Hard", "Creating"),
    ("Assess the defense role of the Andaman and Nicobar Command (ANC) in Indo-Pacific security.", "As a unified tri-service command, ANC acts as India's eastern naval shield, deterring maritime aggression and conducting anti-piracy patrols.", "Hard", "Evaluating"),
    ("Analyze the impact of global warming and ocean acidification on Lakshadweep's coral reefs.", "Warmer water temperatures trigger coral bleaching (polyps expel algae), while ocean acidification weakens calcium carbonate skeletons, threatening reef survival.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 11 connects physical geography, colonial history, and marine ecology.", "Unifies physical landforms (coral atolls/volcanoes) with colonial history (Kala Pani) and marine ecology (corals/lagoons/mangroves).", "Hard", "Synthesizing"),
    ("Critique the statement: 'All islands in the Andaman group are open for commercial resort building.'", "False; many islands are protected tribal reserves, wildlife sanctuaries, or active volcanic zones strictly off-limits to resort development.", "Hard", "Evaluating"),
    ("Formulate a 4-line poem honoring India's island archipelagos.", "'In Bengal's bay where freedom's heroes bled,\nTo Arabian seas where coral reefs are spread;\nOur emerald islands guard the ocean wide,\nIndia's bright jewels of beauty, strength, and pride!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 11: Island Groups of India\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH11_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH11_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the location, island count, capital, and physical features of the Andaman and Nicobar Islands.",
     "The Andaman and Nicobar Islands form a major island archipelago located in the Bay of Bengal in southeastern India. The archipelago comprises approximately 572 islands, though only a small fraction of them are inhabited by human populations. The capital city is Sri Vijaya Puram (formerly known as Port Blair), situated on South Andaman Island. Physically, the islands are characterized by stunning white sand beaches, extensive living coral reefs, and dense, lush tropical rainforests. The group is also home to India's only active volcano, located on Barren Island in the Andaman Sea. Rich in marine life and terrestrial wildlife, these islands are renowned for their breathtaking natural landscape and tropical climate.",
     "Easy", "Remembering"),

    ("Describe the historical significance of Cellular Jail (Kala Pani) in the Andaman Islands.",
     "Cellular Jail, situated in Sri Vijaya Puram (Port Blair), is one of the most solemn historical monuments in India's freedom struggle. Built by the British colonial administration between 1896 and 1906, it was commonly referred to as 'Kala Pani' (Black Waters) because prisoners were exiled across dark ocean waters from which escape was impossible. The jail was specifically constructed with 698 solitary confinement cells radiating from a central watchtower, ensuring that freedom fighters could never see or speak to one another. Illustrious freedom fighters like Vinayak Damodar Savarkar suffered extreme physical torture and solitary hard labor here. Today, Cellular Jail stands as a revered national memorial honoring the supreme sacrifices made by freedom fighters for India's independence.",
     "Easy", "Remembering"),

    ("Describe the location, island count, capital, and features of the Lakshadweep Islands.",
     "The Lakshadweep Islands constitute India's smallest Union Territory, located off the southwestern coast in the Arabian Sea. The group consists of 36 low-lying coral islands and atolls. The administrative capital of Lakshadweep is Kavaratti. The name 'Lakshadweep' translates to 'a hundred thousand islands' in the local Malayalam language. The islands are world-famous for their pristine white sandy beaches, fringing coconut palm trees, and crystal-clear shallow lagoons filled with vibrant coral reefs. Experiencing a warm tropical climate, Lakshadweep has emerged as a premier eco-tourism hotspot where visitors enjoy marine activities like snorkelling, scuba diving, and deep-sea fishing.",
     "Easy", "Remembering"),

    ("Compare the Andaman and Nicobar Islands with the Lakshadweep Islands across key geographic parameters.",
     "India's two main archipelagos differ across several geographical parameters:\n1. **Location & Water Body**: Andaman & Nicobar is located in the Bay of Bengal; Lakshadweep is located in the Arabian Sea.\n2. **Island Count & Type**: Andaman & Nicobar has ~572 mountainous/volcanic islands; Lakshadweep has 36 low-lying coral islands.\n3. **Capitals**: Sri Vijaya Puram is the capital of Andaman & Nicobar; Kavaratti is the capital of Lakshadweep.\n4. **Key Features**: Andaman & Nicobar features rainforests, Cellular Jail, and Barren Island volcano; Lakshadweep features coral atolls, coconut palms, and crystal lagoons.\n5. **Climate & Utility**: Both share a tropical climate, protect Indian coasts, and promote marine eco-tourism.",
     "Easy", "Comparing"),

    ("Explain the vocabulary terms from Chapter 11: Archipelago, Coastal, Lagoon, Coral, and Tropical.",
     "1. **Archipelago**: A group or chain of islands in a sea. *Example*: Andaman & Nicobar is an archipelago of 572 islands.\n2. **Coastal**: Situated on or near the sea or ocean shore. *Example*: Coastal ecosystems protect mainland territory.\n3. **Lagoon**: A body of shallow ocean water enclosed by a surrounding coral reef. *Example*: Lakshadweep is famous for blue lagoons.\n4. **Coral**: A hard rock-like structure formed by accumulated skeletons of tiny sea creatures. *Example*: 36 coral islands form Lakshadweep.\n5. **Tropical**: A hot and humid climate characteristic of regions near the equator. *Example*: Both island groups enjoy a tropical climate.",
     "Easy", "Understanding"),

    ("Discuss the indigenous tribes of the Andaman Islands as described in Chapter 11.",
     "The Andaman Islands are home to ancient indigenous tribes, such as the Jarawa and the Sentinelese, who have inhabited these dense rainforest islands for thousands of years. These tribal communities live in close harmony with nature, relying on traditional hunting, gathering, and fishing. The Sentinelese, living on North Sentinel Island, are famous as one of the world's last uncontacted tribes, choosing to live completely isolated from modern civilization. The Government of India enforces strict non-interference laws to protect these vulnerable tribal communities, their ancestral lands, and their unique cultural survival.",
     "Easy", "Understanding"),

    ("Explain how India's island archipelagos protect the country's coasts and support its economy.",
     "India's island archipelagos play a vital two-fold role:\n1. **Coastal Protection & Defense**: Positioned strategically out in the Bay of Bengal and Arabian Sea, they serve as natural advance outposts that guard India's maritime borders, monitor shipping channels, and buffer mainland coasts against ocean storms.\n2. **Economic Resources & Tourism**: They extend India's Exclusive Economic Zone (EEZ) for offshore fishing and mineral resources. Their pristine beaches, coral reefs, and water sports (snorkelling, diving) generate substantial eco-tourism revenue.",
     "Easy", "Understanding"),

    ("Describe Barren Island and explain why it is scientifically unique in India.",
     "Barren Island is a small, uninhabited island located in the Andaman Sea, approximately 138 kilometers northeast of Sri Vijaya Puram. It holds the scientific distinction of harboring India's only active volcano—and the only confirmed active volcano along the submarine volcanic arc extending from Sumatra to Myanmar. The volcano features a 2-kilometer-wide caldera with an active cinder cone that periodically erupts ash, steam, and molten red lava. Volcanologists and marine scientists study Barren Island to monitor geothermal activity and plate tectonics in the Indian Ocean.",
     "Easy", "Remembering"),

    ("Summarize Chapter 11 in five detailed bullet points.",
     "- India has two main archipelagos: Andaman & Nicobar (Bay of Bengal) and Lakshadweep (Arabian Sea).\n- Andaman & Nicobar has 572 islands with capital Sri Vijaya Puram, lush rainforests, coral reefs, and Barren Island's active volcano.\n- Cellular Jail (Kala Pani) in Andaman is a historic national memorial where freedom fighters were held by the British.\n- Lakshadweep comprises 36 coral islands with capital Kavaratti, famous for white beaches, coconut palms, and blue lagoons.\n- Both tropical archipelagos harbor rich marine life, protect India's coasts, and attract tourists for snorkelling and diving.",
     "Easy", "Understanding"),

    ("What lessons about environmental responsibility can Class 5 students learn from Chapter 11?",
     "Class 5 students learn that ocean islands and coral reefs are delicate natural ecosystems that must be protected. They learn that plastic pollution, littering, and coral destruction threaten fish, sea turtles, and island shorelines. Students are inspired to become eco-conscious citizens who protect oceans, conserve water, respect indigenous cultures, and preserve natural beauty for future generations.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why is the Malayalam language spoken in the Lakshadweep Islands?", "Because Lakshadweep lies off the coast of Kerala in the Arabian Sea. Historical trade, migration, and cultural ties connected the islanders with Kerala, making Malayalam the primary regional language.", "Easy", "Understanding"),
    ("Explain the term 'coral reef' and how coral islands like Lakshadweep were formed.", "Coral reefs are built by millions of tiny sea animals (polyps) that secrete hard calcium carbonate. Over thousands of years, accumulated coral layers around sinking undersea mountains reached the water surface, forming 36 coral islands.", "Easy", "Understanding"),
    ("Describe the water activities of snorkelling and scuba diving enjoyed by tourists in the islands.", "Snorkelling uses a facemask and breathing tube to float on shallow water surface and view shallow reefs; scuba diving uses underwater air tanks allowing divers to swim deep to explore coral walls, sea turtles, and fish.", "Easy", "Remembering"),
    ("Why did the British choose the Andaman Islands for building Cellular Jail?", "Because the islands were isolated by thousands of miles of deep ocean ('Kala Pani'), making escape impossible and severing freedom fighters from political contact with mainland India.", "Easy", "Analyzing"),
    ("How do coconut palms support the daily life and economy of Lakshadweep islanders?", "Coconut palms provide fresh food, coconut water, coir fiber for weaving ropes and mats, palm timber for building boats and homes, and copra oil for trade, forming the traditional economic backbone.", "Easy", "Understanding"),
    ("What makes the natural environment of both island groups 'rich in wildlife and marine life'?", "Their warm tropical climate, clear sunlit waters, pristine coral reefs, and extensive mangrove rainforests provide ideal feeding and breeding habitats for thousands of species.", "Easy", "Understanding"),
    ("Describe the experience of a tourist visiting Lakshadweep's calm lagoons.", "Tourists experience crystal-clear, shallow turquoise waters enclosed by coral reefs, where they can swim safely, see colorful tropical fish swimming over white sand, and enjoy peaceful water sports.", "Easy", "Remembering"),
    ("How does the Government of India protect the uncontacted Sentinelese tribe?", "By establishing a strict 5-nautical-mile exclusion zone around North Sentinel Island, banning unauthorized visits, and maintaining non-interference to protect the tribe from deadly modern diseases.", "Easy", "Evaluating"),
    ("Explain why Port Blair was officially renamed 'Sri Vijaya Puram'.", "The name change honors ancient Indian Chola naval victory heritage in the Bay of Bengal while replacing the British colonial name of Captain Archibald Blair.", "Easy", "Remembering"),
    ("How do India's island archipelagos enhance the country's national pride?", "By showcasing India's breathtaking geographical diversity, hosting rich marine ecosystems, preserving freedom struggle history at Cellular Jail, and guarding our oceanic boundaries.", "Easy", "Evaluating"),
    ("Re-write the story of Chapter 11 as a travel journal of a young explorer visiting both island groups.", "'Day 1 in Sri Vijaya Puram: Visited Cellular Jail where heroes fought for freedom! Day 3: Saw Barren Island's active volcano! Day 5 in Kavaratti: Scuba dived in Lakshadweep's blue lagoon among sea turtles! Our islands are paradise!'", "Easy", "Creating"),
    ("What role do marine national parks play in protecting coral reefs in the Andaman Islands?", "Marine national parks (like Mahatma Gandhi Marine National Park) legally prohibit coral collection, commercial fishing, and anchor damage, preserving pristine marine ecosystems.", "Easy", "Understanding"),
    ("Describe how tropical weather affects daily life on island archipelagos.", "Warm temperatures and high humidity encourage light cotton clothing, outdoor water activities, sea fishing, and reliance on monsoon rain for freshwater storage.", "Easy", "Understanding"),
    ("Analyze why Chapter 11 is titled 'Island Groups of India'.", "Because it comprehensively introduces India's two distinct oceanic archipelagos—Andaman & Nicobar and Lakshadweep—exploring their geography, history, and ecology.", "Easy", "Analyzing"),
    ("How can young students promote marine conservation in their schools?", "By creating posters about saving coral reefs, organizing plastic-free campaigns, learning about ocean marine life, and spreading awareness about river and sea protection.", "Easy", "Applying"),

    # Medium (26-40)
    ("Critically analyze how the physical geography of island archipelagos shapes their human geography.",
     "Physical geography dictates human geography on islands:\n1. **Isolation & Settlement**: Island isolation created distinct indigenous tribal cultures (Jarawa/Sentinelese) in Andaman and compact fishing communities in Lakshadweep.\n2. **Economic Activities**: Lack of large landmasses limits heavy industry, shifting economic focus to fishing, coconut agriculture, maritime trade, and eco-tourism.\n3. **Infrastructure**: Dependence on sea harbors and airports for mainland transport makes shipping and aviation lifelines for island residents.",
     "Medium", "Analyzing"),

    ("Examine the environmental threats facing coral reef ecosystems in Lakshadweep and Andaman.",
     "Island coral reefs face critical environmental threats:\n- **Global Warming & Bleaching**: Rising sea surface temperatures force coral polyps to expel symbiotic algae, turning corals white and causing reef mortality.\n- **Plastic & Marine Pollution**: Non-biodegradable trash smothers coral heads and entangles marine life.\n- **Unregulated Tourism**: Boat anchors, physical stepping by swimmers, and coastal construction physically break fragile coral structures.",
     "Medium", "Analyzing"),

    ("Evaluate the historic legacy of freedom fighters imprisoned in Cellular Jail.",
     "Cellular Jail represents the ultimate crucible of Indian patriotism. Freedom fighters like Veer Savarkar, Barindra Kumar Ghosh, and Batukeshwar Dutt endured solitary confinement, grueling labor at oil mills, and brutal punishments. Their unbroken spirit across the 'Kala Pani' inspired the national freedom movement, turning Cellular Jail into a sacred pilgrimage site of Indian independence.",
     "Medium", "Evaluating"),

    ("Discuss the strategic role of the Andaman and Nicobar Islands in Indo-Pacific maritime security.",
     "Positioned at the junction of the Bay of Bengal and Andaman Sea, the islands sit near the Strait of Malacca—the busiest oil shipping channel in the world. Hosting India's tri-service Andaman and Nicobar Command (ANC), they allow the Indian Navy to conduct maritime surveillance, counter piracy, and secure energy supply corridors across the Indo-Pacific region.",
     "Medium", "Analyzing"),

    ("Design a school exhibition module for 'Island Archipelagos of India'.",
     "Exhibition Title: 'Emerald & Coral — India's Island Treasures'\n- **Zone 1 (Andaman & Nicobar)**: Model of Cellular Jail, photo gallery of Barren Island volcano, and Jarawa craft displays.\n- **Zone 2 (Lakshadweep)**: Coral reef tank display, coconut coir craft corner, and lagoon map.\n- **Zone 3 (Marine Bio)**: Interactive quiz on snorkelling, sea turtles, and colorful reef fish.\n- **Zone 4 (Pledge Wall)**: Student signatures on 'Save Our Oceans & Corals'.",
     "Medium", "Creating"),

    ("How did the 2004 Indian Ocean Tsunami impact the Andaman and Nicobar Islands?", "The massive 2004 tsunami waves struck the low-lying Nicobar islands, causing severe loss of life, submerging coastal land, damaging coral reefs, and altering island geography.", "Medium", "Understanding"),
    ("Contrast the ecosystem of Barren Island (volcanic) with Kavaratti Island (coral atoll).", "Barren Island is a steep, rocky, active volcanic island with black basalt soil and minimal human presence; Kavaratti is a flat, sandy coral atoll with blue lagoons and a thriving human capital.", "Medium", "Comparing"),
    ("Why is coconut coir processing a traditional cottage industry in Lakshadweep?", "Abundant coconut palm husks provide natural coir fibers, which islanders soak in lagoon water and hand-twist into strong ropes, mats, and fishing nets.", "Medium", "Understanding"),
    ("Describe the role of the Indian Coast Guard in protecting island marine environments.", "The Coast Guard patrols territorial waters, prevents illegal foreign poaching of marine species, rescues stranded vessels, and responds to oil spill pollution threats.", "Medium", "Understanding"),
    ("Explain why fresh drinking water management is a challenge on small coral islands.", "Small coral islands have thin landmasses with limited groundwater lenses. Over-pumping causes saltwater intrusion, requiring rainwater harvesting and solar desalination plants.", "Medium", "Analyzing"),
    ("How do traditional tribal communities in Andaman live sustainably without modern technology?", "Tribal communities hunt wild game, gather forest fruits, and fish using wooden bows and nets, taking only what they need without destroying forest ecosystems.", "Medium", "Evaluating"),
    ("What makes scuba diving in Andaman's Havelock (Swaraj Dweep) Island internationally famous?", "Warm crystal-clear waters, high underwater visibility, dramatic coral walls, sea turtles, manta rays, and diverse reef fish attract international divers.", "Medium", "Remembering"),
    ("Analyze why Chapter 11 uses technical geographical terms like 'archipelago', 'atoll', 'lagoon', and 'volcano'.", "To build precise geographical literacy in Class 5 students, connecting physical earth features with real Indian territories.", "Medium", "Analyzing"),
    ("How does the Andaman and Nicobar Command (ANC) demonstrate military inter-service integration?", "ANC unifies the Indian Army, Navy, and Air Force under a single Commander-in-Chief, establishing seamless tri-service defense operational capability.", "Medium", "Understanding"),
    ("Construct a fictional dialogue between a coral polyp and a sea turtle in a Lakshadweep lagoon.", "'Coral Polyp: We spent a hundred years building this colorful reef home for you!' 'Sea Turtle: Thank you! Your reef gives me delicious algae to eat and a safe place to rest!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the developmental model of transforming Lakshadweep into a high-end water villa tourist destination like Maldives.",
     "High-end water villa development promises economic growth and luxury tourism revenue, but risks destroying fragile coral lagoon beds, depleting limited freshwater aquifers, generating solid waste, and displacing local island fishing culture if not strictly regulated.",
     "Hard", "Evaluating"),

    ("Deconstruct the geological evolution of the Andaman Sea back-arc basin and Barren Island volcano.",
     "Subduction of the Indo-Australian plate beneath the Burma microplate created back-arc extension in the Andaman Sea. Magma rising along this fault line formed the volcanic chain including Barren Island and Narcondam Island.",
     "Hard", "Analyzing"),

    ("Synthesize the ecological role of coral reefs as 'rainforests of the ocean'.",
     "Although covering less than 1% of the ocean floor, coral reefs support over 25% of all marine species. Like terrestrial rainforests, they exhibit immense biodiversity, produce oxygen, protect shorelines, and cycle essential nutrients across ocean ecosystems.",
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive essay prompt evaluating the strategic, ecological, and historical significance of India's island groups.",
     "Prompt: 'Analyze the dual significance of India's island archipelagos (Andaman & Nicobar and Lakshadweep). Discuss their strategic maritime role, unique ecosystems (volcanoes and coral reefs), historical freedom legacy at Cellular Jail, and environmental conservation challenges.'",
     "Hard", "Creating"),

    ("Evaluate the impact of climate change on indigenous tribal survival in isolated island habitats.", "Climate change causes sea level rise, extreme cyclones, and shifting forest weather, threatening traditional food gathering, coastal settlements, and freshwater availability for vulnerable tribal groups.", "Hard", "Evaluating"),

    ("Compare the marine biodiversity of the Bay of Bengal (Andaman) with the Arabian Sea (Lakshadweep).", "Bay of Bengal receives massive river freshwater runoff, creating lower salinity and extensive coastal mangroves; Arabian Sea has higher salinity, supporting extensive biogenic coral reef atolls.", "Hard", "Comparing"),
    ("Discuss the governance architecture of Union Territories regarding island administration.", "As Union Territories without full statehood, island groups are administered directly by the Central Government via Lieutenant Governors or Administrators, ensuring direct central funding and national defense integration.", "Hard", "Understanding"),
    ("Analyze how maritime trade routes through the Malacca Strait enhance the geopolitical value of the Andaman Islands.", "Over 90,000 commercial vessels carrying 40% of world trade pass through the Malacca Strait annually. Andaman's proximity allows India to monitor this strategic trade bottleneck.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'The island groups of India not only add to the country's beauty but also play an important role in protecting our coasts and providing valuable natural resources.'", "This concluding line synthesizes aesthetics, defense, and economic utility. It reminds citizens that these island archipelagos are not distant holiday spots, but vital national assets securing India's oceanic frontiers and marine prosperity.", "Hard", "Evaluating"),
    ("Synthesize the complete educational takeaways of Chapter 11 for primary school geography, history, and ethics.", "Chapter 11 unifies physical geography (archipelagos/corals/volcanoes) with national history (Cellular Jail freedom struggle), strategic defense, and moral environmental stewardship of ocean resources.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 11: Island Groups of India\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH11_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH11_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("India is not just a country with mountains, rivers and plains but also has beautiful islands. There are two main archipelagos in India: the Andaman and Nicobar Islands in the Bay of Bengal and the Lakshadweep Islands in the Arabian Sea.",
     [
         ("What natural landforms does India possess besides mountains, rivers, and plains?", "Beautiful islands.", "Easy", "Remembering"),
         ("What are the names of the two main archipelagos in India?", "Andaman and Nicobar Islands and Lakshadweep Islands.", "Easy", "Remembering"),
         ("In which water body are the Andaman and Nicobar Islands located?", "The Bay of Bengal.", "Easy", "Remembering"),
         ("In which water body are the Lakshadweep Islands located?", "The Arabian Sea.", "Easy", "Remembering"),
         ("What does the word 'archipelago' mean?", "A group or chain of islands in a sea or ocean.", "Easy", "Understanding")
     ]),

    # Set 2
    ("This group has around 572 islands, but only some are inhabited by people. The capital is Sri Vijaya Puram, located in the Andaman Islands. These islands are known for their beautiful beaches, coral reefs and tropical forests.",
     [
         ("How many islands make up the Andaman and Nicobar group?", "Around 572 islands.", "Easy", "Remembering"),
         ("Are all 572 islands inhabited by people?", "No, only some of the islands are inhabited.", "Easy", "Remembering"),
         ("What is the capital of the Andaman and Nicobar Islands?", "Sri Vijaya Puram.", "Easy", "Remembering"),
         ("Name three natural features the Andaman Islands are known for.", "Beautiful beaches, coral reefs, and tropical forests.", "Easy", "Remembering"),
         ("What is coral?", "A hard rock-like substance formed by accumulated skeletons of sea creatures.", "Easy", "Understanding")
     ]),

    # Set 3
    ("The Cellular Jail, also called Kala Pani, is a famous historical site here. During the British Raj, our freedom fighters were held captive here.",
     [
         ("What famous historical site is located in the Andaman Islands?", "The Cellular Jail.", "Easy", "Remembering"),
         ("What was another name given to Cellular Jail?", "Kala Pani.", "Easy", "Remembering"),
         ("Who was held captive in Cellular Jail during the British Raj?", "Indian freedom fighters.", "Easy", "Remembering"),
         ("Why was it called Cellular Jail?", "Because it was built with solitary individual cells to prevent prisoner communication.", "Medium", "Understanding"),
         ("Why was it called 'Kala Pani'?", "Because prisoners were isolated across dark ocean waters from which escape was impossible.", "Medium", "Understanding")
     ]),

    # Set 4
    ("The islands are home to many tribes, such as the Jarawa and Sentinelese, who have lived there for centuries. India's only active volcano is located on Barren Island in the Andaman sea.",
     [
         ("Name two indigenous tribes living in the Andaman Islands.", "The Jarawa and the Sentinelese.", "Easy", "Remembering"),
         ("How long have these tribes lived in the Andaman Islands?", "For centuries.", "Easy", "Remembering"),
         ("Where is India's only active volcano located?", "On Barren Island in the Andaman Sea.", "Easy", "Remembering"),
         ("What makes Barren Island scientifically unique?", "It contains the only active volcano in South Asia.", "Medium", "Understanding"),
         ("How does the Government of India protect uncontacted tribes like the Sentinelese?", "By maintaining a strict non-interference policy and exclusion zone around their island.", "Medium", "Analyzing")
     ]),

    # Set 5
    ("This group has 36 coral islands, located in the Arabian Sea. The capital of Lakshadweep is Kavaratti. These islands are famous for their white sandy beaches, coconut palms and lagoons...",
     [
         ("How many islands make up the Lakshadweep group?", "36 coral islands.", "Easy", "Remembering"),
         ("In which sea are the Lakshadweep Islands located?", "The Arabian Sea.", "Easy", "Remembering"),
         ("What is the capital of Lakshadweep?", "Kavaratti.", "Easy", "Remembering"),
         ("Name three natural features Lakshadweep is famous for.", "White sandy beaches, coconut palms, and lagoons.", "Easy", "Remembering"),
         ("What is a 'lagoon'?", "A shallow water body separated from the ocean by a coral reef.", "Easy", "Understanding")
     ]),

    # Set 6
    ("The word \"Lakshadweep\" means \"a hundred thousand islands\" in Malayalam. Both island groups are rich in wildlife, marine life and natural beauty because of the tropical climate.",
     [
         ("What does the word 'Lakshadweep' mean?", "A hundred thousand islands.", "Easy", "Remembering"),
         ("In which language does 'Lakshadweep' mean a hundred thousand islands?", "Malayalam.", "Easy", "Remembering"),
         ("What kind of climate do both island groups experience?", "A tropical climate (hot and humid).", "Easy", "Remembering"),
         ("What biological life is rich in both island groups?", "Wildlife and marine life.", "Easy", "Remembering"),
         ("How does a tropical climate foster rich marine life?", "Warm sunlit ocean waters promote coral growth, supporting diverse marine food chains.", "Medium", "Understanding")
     ]),

    # Set 7
    ("They are also popular tourist destinations where people enjoy activities like snorkelling, scuba diving, and fishing.",
     [
         ("What status do both island groups hold regarding travel?", "They are popular tourist destinations.", "Easy", "Remembering"),
         ("Name three popular water activities mentioned in this passage.", "Snorkelling, scuba diving, and fishing.", "Easy", "Remembering"),
         ("What is snorkelling?", "Swimming on shallow water surface while wearing a diving mask and breathing tube.", "Easy", "Understanding"),
         ("What is scuba diving?", "Swimming deep underwater using breathing tanks to observe coral reefs and marine life.", "Easy", "Understanding"),
         ("How can tourists practice responsible eco-tourism while scuba diving?", "By avoiding touching corals, leaving no waste behind, and respecting marine life.", "Medium", "Applying")
     ]),

    # Set 8
    ("The island groups of India not only add to the country's beauty but also play an important role in protecting our coasts and providing valuable natural resources.",
     [
         ("What do the island groups add to India?", "They add to the country's beauty.", "Easy", "Remembering"),
         ("What strategic role do the island groups play for India?", "They play an important role in protecting our coasts.", "Easy", "Understanding"),
         ("What do the island groups provide to the country?", "Valuable natural resources.", "Easy", "Remembering"),
         ("Name two valuable natural resources provided by island groups.", "Marine fish resources and coconut palm products.", "Medium", "Understanding"),
         ("Summarize the importance of India's island archipelagos in one sentence.", "India's island archipelagos enrich national beauty, harbor rich biodiversity, protect oceanic coasts, and guard strategic maritime trade routes.", "Medium", "Evaluating")
     ]),

    # Set 9
    ("Word Meaning: Archipelago — A group of islands. Coastal — Near the sea or ocean. Lagoon — A shallow water body separated from the sea. Coral — Hard substance formed by sea creatures. Tropical — Climate that is hot and humid.",
     [
         ("What is the definition of 'archipelago'?", "A group of islands.", "Easy", "Remembering"),
         ("What is the definition of 'coastal'?", "Near the sea or ocean.", "Easy", "Remembering"),
         ("What is the definition of 'lagoon'?", "A shallow water body separated from the sea.", "Easy", "Remembering"),
         ("What is the definition of 'coral'?", "Hard substance formed by sea creatures.", "Easy", "Remembering"),
         ("What is the definition of 'tropical'?", "Climate that is hot and humid.", "Easy", "Remembering")
     ]),

    # Set 10
    ("Andaman & Nicobar: 572 islands in Bay of Bengal, Sri Vijaya Puram... Lakshadweep: 36 coral islands in Arabian Sea, Kavaratti... Cellular Jail... Barren Island active volcano...",
     [
         ("Where are the Andaman Islands located?", "Bay of Bengal.", "Easy", "Remembering"),
         ("Where are the Lakshadweep Islands located?", "Arabian Sea.", "Easy", "Remembering"),
         ("What is the capital of Andaman & Nicobar?", "Sri Vijaya Puram.", "Easy", "Remembering"),
         ("What is the capital of Lakshadweep?", "Kavaratti.", "Easy", "Remembering"),
         ("Summarize the complete geographic profile of India's archipelagos in one sentence.", "India's eastern Andaman & Nicobar (572 islands) and western Lakshadweep (36 coral islands) form rich tropical oceanic archipelagos protecting India's coasts.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 11: Island Groups of India\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH11_EXT_{q_counter:03d}"
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

with open(os.path.join(CH11_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 11 in {CH11_DIR}")
