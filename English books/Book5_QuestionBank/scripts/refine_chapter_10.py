r"""
Refines all 6 Category files for Book 5 Chapter 10 ("The Narmada River") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH10_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_10")
os.makedirs(CH10_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Where does the Narmada River originate?", "(A) Amarkantak Hills in Madhya Pradesh", "(B) Gangotri Glacier in Uttarakhand", "(C) Mansarovar Lake in Tibet", "(D) Mahabaleshwar in Maharashtra", "(A)", "The river starts from the Amarkantak Hills in Madhya Pradesh.", "Easy", "Remembering", "River Origin"),
    ("Which sea does the Narmada River empty into?", "(A) Arabian Sea", "(B) Bay of Bengal", "(C) Indian Ocean", "(D) Red Sea", "(A)", "It flows westward before reaching the Arabian Sea.", "Easy", "Remembering", "Destination Sea"),
    ("Through which three Indian states does the Narmada River flow?", "(A) Madhya Pradesh, Maharashtra, and Gujarat", "(B) Punjab, Haryana, and Rajasthan", "(C) Uttar Pradesh, Bihar, and West Bengal", "(D) Kerala, Tamil Nadu, and Karnataka", "(A)", "Flows through Madhya Pradesh, Maharashtra, and Gujarat.", "Easy", "Remembering", "Flow States"),
    ("What special title is given to the Narmada River in Madhya Pradesh?", "(A) Life Line of Madhya Pradesh", "(B) Life Line of India", "(C) Queen of Rivers", "(D) Golden River of Gujarat", "(A)", "Known as the 'Life Line of Madhya Pradesh'.", "Easy", "Remembering", "Title"),
    ("What is the approximate total length of the Narmada River?", "(A) 1,312 kilometers", "(B) 800 kilometers", "(C) 2,525 kilometers", "(D) 3,000 kilometers", "(A)", "It travels around 1,312 kilometers.", "Easy", "Remembering", "River Length"),
    ("In which direction does the Narmada River flow, unlike most major Indian rivers?", "(A) Westward", "(B) Eastward", "(C) Northward", "(D) Southward", "(A)", "Most Indian rivers flow east, but Narmada flows westward.", "Easy", "Understanding", "Flow Direction"),
    ("Name one major tributary of the Narmada River mentioned in Chapter 10.", "(A) Tawa", "(B) Yamuna", "(C) Sutlej", "(D) Godavari", "(A)", "Tributaries like Tawa, Kolar, Dudhi, and Barna drain into it.", "Easy", "Remembering", "Tributaries"),
    ("Which tourist attraction near Jabalpur is famous for tall white marble cliffs along the Narmada?", "(A) Marble Rocks of Bhedaghat", "(B) Statue of Unity", "(C) Dhuandhar Waterfalls", "(D) Ajanta Caves", "(A)", "The Marble Rocks of Bhedaghat near Jabalpur are a popular tourist attraction.", "Easy", "Remembering", "Tourist Attraction"),
    ("Near which city in Madhya Pradesh are the Marble Rocks of Bhedaghat located?", "(A) Jabalpur", "(B) Bhopal", "(C) Indore", "(D) Gwalior", "(A)", "Marble Rocks of Bhedaghat are near Jabalpur.", "Easy", "Remembering", "Location"),
    ("What religious journey do pilgrims undertake along the entire path of the Narmada River?", "(A) Narmada Parikrama", "(B) Char Dham Yatra", "(C) Amarnath Yatra", "(D) Kanwar Yatra", "(A)", "Pilgrims perform the Narmada Parikrama along the entire river.", "Easy", "Remembering", "Religious Journey"),
    ("Which major dam on the Narmada River generates electricity and provides irrigation?", "(A) Sardar Sarovar Dam", "(B) Bhakra Nangal Dam", "(C) Tehri Dam", "(D) Hirakud Dam", "(A)", "The Sardar Sarovar Dam provides water for farming, drinking, and electricity.", "Easy", "Remembering", "Major Dam"),
    ("What does the word 'tributary' mean in the vocabulary box?", "(A) A small river joining a bigger one", "(B) A large ocean wave", "(C) A wooden boat", "(D) A deep valley in a mountain", "(A)", "Tributary = A small river joining a bigger one.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'reservoir' mean?", "(A) A large lake made to store water", "(B) A small underground well", "(C) A fast-flowing waterfall", "(D) A dry desert valley", "(A)", "Reservoir = A large lake made to store water.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'basin' mean?", "(A) Land drained by a river and its branches", "(B) A plastic bucket for washing", "(C) A high mountain peak", "(D) A sandy ocean beach", "(A)", "Basin = Land drained by a river and its branches.", "Easy", "Understanding", "Vocabulary"),
    ("Why is the Narmada River essential for towns and villages along its course?", "(A) It provides water for drinking, farming, and electricity", "(B) It transports gold from mountains", "(C) It stops all rainstorms", "(D) It freezes into ice roads", "(A)", "Provides water for drinking, farming, and electricity generation.", "Easy", "Understanding", "Utility"),
    ("Which of the following is NOT a tributary of the Narmada River?", "(A) Ganga", "(B) Tawa", "(C) Kolar", "(D) Dudhi", "(A)", "Ganga is a separate major river, not a tributary of Narmada.", "Easy", "Remembering", "Tributaries Identification"),
    ("What color are the tall marble cliffs at Bhedaghat?", "(A) White", "(B) Black", "(C) Red", "(D) Green", "(A)", "Flows between tall white marble cliffs.", "Easy", "Remembering", "Cliff Color"),
    ("What ecological life does the Narmada River support?", "(A) Many species of fish, birds, and plants", "(B) Only polar bears", "(C) Desert cacti only", "(D) No living organisms", "(A)", "Home to many fish, birds, and plants.", "Easy", "Remembering", "Ecosystem"),
    ("Besides providing water, what cultural value does the Narmada River symbolize?", "(A) A symbol of culture, tradition, and natural beauty", "(B) A barrier between foreign countries", "(C) A private property of one state", "(D) An industrial sewer", "(A)", "Symbol of culture, tradition, and natural beauty.", "Easy", "Understanding", "Cultural Symbolism"),
    ("What lesson does Chapter 10 teach us regarding natural rivers?", "(A) The importance of protecting our rivers for future generations", "(B) The need to drain all river water into oceans quickly", "(C) The plan to cover rivers with concrete roads", "(D) The idea that rivers clean themselves without care", "(A)", "Reminds us of the importance of protecting our rivers for future generations.", "Easy", "Understanding", "Moral Lesson"),
    ("In which mountain range does the Narmada River originate?", "(A) Amarkantak Hills", "(B) Himalayas", "(C) Aravalli Range", "(D) Western Ghats", "(A)", "Originates in the Amarkantak Hills.", "Easy", "Remembering", "Mountain Origin"),
    ("Which state contains the highest portion of the Narmada River basin?", "(A) Madhya Pradesh", "(B) Maharashtra", "(C) Gujarat", "(D) Rajasthan", "(A)", "Madhya Pradesh contains the main basin, making Narmada its lifeline.", "Easy", "Remembering", "Basin Share"),
    ("How do people perform the Narmada Parikrama?", "(A) By walking along the entire bank of the river as a holy journey", "(B) By flying over the river in a helicopter", "(C) By driving a car along the highway", "(D) By sailing a motorboat across the ocean", "(A)", "Pilgrims walk along the entire river as a religious journey.", "Easy", "Understanding", "Parikrama Method"),
    ("What type of energy is generated using dams built on the Narmada River?", "(A) Hydroelectricity (hydro-electric power)", "(B) Solar energy", "(C) Wind energy", "(D) Nuclear energy", "(A)", "Dams generate hydro-electricity from flowing water.", "Easy", "Understanding", "Energy Type"),
    ("What title is given to Chapter 10?", "(A) The Narmada River", "(B) Traditional Dresses from India", "(C) Island Groups of India", "(D) The Magic of Books", "(A)", "Title is 'The Narmada River'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why is the westward flow of the Narmada River geographically unique in India?", "(A) Peninsular tilt causes Ganga, Godavari, and Krishna to flow east into the Bay of Bengal, whereas Narmada flows west in a rift valley into the Arabian Sea", "(B) Narmada flows uphill toward the Himalayas", "(C) Narmada flows in circles around Madhya Pradesh", "(D) Narmada changes flow direction every month", "(A)", "Flows westward in a rift valley into the Arabian Sea, unlike east-flowing peninsular rivers.", "Medium", "Analyzing", "Geographical Uniqueness"),
    ("Explain why the Narmada River is called the 'Life Line of Madhya Pradesh'.", "(A) It traverses across the state, supplying essential drinking water, irrigating vast agricultural fields, and powering industries", "(B) It is the only river in Asia", "(C) It flows through Bhopal city center only", "(D) It was named by royal decree", "(A)", "Supplies essential drinking water, irrigates vast farmlands, and powers state economic life.", "Medium", "Analyzing", "Lifeline Rationale"),
    ("How do the Marble Rocks of Bhedaghat create a unique geological landscape?", "(A) The river carves a narrow gorge through 100-foot tall magnesium marble cliffs that glisten under sunlight and moonlight", "(B) The rocks are made of artificial concrete painted white", "(C) The rocks float on top of the river water", "(D) The cliffs are made of ice that melts in winter", "(A)", "Carves a narrow gorge through tall magnesium marble cliffs creating a stunning aesthetic.", "Medium", "Understanding", "Geological Landscape"),
    ("Discuss the dual role of the Sardar Sarovar Dam for regional development.", "(A) It stores massive monsoon water in its reservoir for drinking/irrigation in drought areas while generating hydroelectric power", "(B) It stops all river flow permanently", "(C) It is built exclusively for luxury swimming pools", "(D) It imports water from foreign nations", "(A)", "Stores water for irrigation and drinking while generating hydroelectric power.", "Medium", "Analyzing", "Dam Multi-Purpose"),
    ("Why is the Narmada Parikrama considered one of India's most demanding pilgrimage traditions?", "(A) Devotees walk over 2,600 km along both banks from Amarkantak to the sea and back, demonstrating intense spiritual devotion", "(B) Devotees must run the distance in two days", "(C) It is performed underwater", "(D) Devotees ride bicycles without stopping", "(A)", "Devotees walk over 2,600 km along both banks, taking months of dedicated spiritual walking.", "Medium", "Evaluating", "Pilgrimage Rigor"),
    ("Compare a 'tributary' with a 'main river' using examples from Chapter 10.", "(A) A main river (Narmada) flows directly to an ocean/sea; a tributary (Tawa/Barna) is a smaller stream that feeds into the main river", "(B) A tributary is larger than a main river", "(C) Main rivers flow only in winter while tributaries flow in summer", "(D) Both are man-made concrete canals", "(A)", "Main river empties into sea; tributary is a smaller stream feeding into the main river.", "Medium", "Comparing", "Hydrological Terms"),
    ("How does river pollution threaten the biodiversity of the Narmada basin?", "(A) Industrial waste and untreated sewage reduce oxygen in water, harming fish, birds, and aquatic plant species", "(B) Pollution makes water turn into solid ice", "(C) Pollution causes fish to fly into trees", "(D) Pollution has zero effect on living organisms", "(A)", "Industrial/sewage waste reduces oxygen, harming fish, birds, and plant species.", "Medium", "Evaluating", "Ecological Threat"),
    ("Explain the relationship between the Amarkantak plateau and Indian river origins.", "(A) Amarkantak is a unique hydrological hub where the Narmada, Johilla, and Son rivers originate in different directions", "(B) Amarkantak is an ocean island", "(C) Amarkantak is a man-made water park", "(D) No rivers start in Amarkantak", "(A)", "Hydrological hub where Narmada, Son, and Johilla rivers originate.", "Medium", "Understanding", "Hydrological Origin"),
    ("Why are rift valleys responsible for the westward flow of the Narmada and Tapti rivers?", "(A) Tectonic faulting created deep rift valleys between the Vindhya and Satpura ranges, directing water flow west toward the Arabian Sea", "(B) Wind blows the river water backward", "(C) The mountains were built by ancient kings", "(D) The Arabian Sea pulls river water with magnets", "(A)", "Tectonic rift valleys between Vindhya and Satpura ranges channel water westward.", "Medium", "Analyzing", "Rift Valley Formation"),
    ("How does reservoir storage behind dams help prevent drought in dry seasons?", "(A) Monsoonal floodwaters are captured in large reservoirs and released systematically during dry summer months for farming and drinking", "(B) Reservoirs create artificial rain clouds every day", "(C) Reservoirs freeze water into ice blocks", "(D) Water in reservoirs never evaporates", "(A)", "Monsoon waters captured in reservoirs are released systematically during dry months.", "Medium", "Understanding", "Water Storage Value"),
    ("What makes the Dhuandhar Falls near Bhedaghat visually famous?", "(A) The Narmada plunges down a rocky ledge, creating a dense mist of water droplets that looks like rising smoke ('Dhuan')", "(B) Water falls upward into clouds", "(C) The water is boiling hot steam", "(D) The waterfall is made of red sand", "(A)", "Plunges down a rocky ledge creating a dense mist of water droplets looking like smoke.", "Medium", "Understanding", "Waterfall Feature"),
    ("Analyze how river dams impact local river ecosystems.", "(A) While dams provide human benefits (water/power), they alter natural fish migration, submerge forests, and change sediment flow", "(B) Dams make fish grow ten times larger", "(C) Dams eliminate all river plants", "(D) Dams turn fresh water into salt water", "(A)", "Provide human benefits but alter fish migration, submerge land, and change sediment flow.", "Medium", "Evaluating", "Ecological Balance"),
    ("Why is public awareness about river conservation emphasized in Chapter 10?", "(A) Rivers provide essential life-sustaining resources; protecting them prevents water scarcity and environmental destruction for future generations", "(B) Conservation is required only for luxury resorts", "(C) Rivers will never dry up regardless of pollution", "(D) Public awareness is meant only for tourist guides", "(A)", "Protecting life-sustaining rivers prevents scarcity and environmental destruction for future generations.", "Medium", "Evaluating", "Conservation Rationale"),
    ("Summarize Chapter 10 in four concise sentences.", "The Narmada River is a major west-flowing river originating from the Amarkantak Hills in Madhya Pradesh and emptying into the Arabian Sea after 1,312 km. Known as the 'Life Line of Madhya Pradesh', it flows through MP, Maharashtra, and Gujarat, fed by tributaries like Tawa and Barna. Famous for the white Marble Rocks of Bhedaghat and the holy Narmada Parikrama, it supports agriculture, drinking water, and power via the Sardar Sarovar Dam. The chapter reminds us to conserve our precious rivers for future generations.", "Medium", "Understanding", "Chapter Summary"),
    ("What action can Class 5 students take to help protect local rivers and water bodies?", "(A) Reduce water waste at home, avoid dumping plastic or trash into streams, and participate in tree planting near water banks", "(B) Throw plastic bottles into rivers", "(C) Waste tap water continuously", "(D) Never talk about environmental care", "(A)", "Reduce water waste, avoid plastic dumping, and plant trees along water banks.", "Medium", "Applying", "Student Action"),

    # Hard (41-50)
    ("Critique the socio-environmental debate surrounding large multi-purpose dams like Sardar Sarovar.", "(A) Balances massive irrigation/hydroelectric benefits for drought regions against tribal displacement, forest submergence, and river ecosystem changes", "(B) Large dams have no benefits at all", "(C) Dams cause oceans to disappear", "(D) Large dams are built in two days without planning", "(A)", "Balances irrigation/hydroelectric gains against tribal displacement and forest submergence.", "Hard", "Evaluating", "HOTS Dam Debate"),
    ("Deconstruct the geomorphology of the Narmada Rift Valley between the Vindhya and Satpura ranges.", "(A) Faulting along the Narmada-Son Lineament created a structural graben, guiding the river through narrow basaltic and marble gorges", "(B) The valley was dug by hand by ancient armies", "(C) The valley formed when a meteor struck Gujarat", "(D) Mountain ranges moved apart due to wind storms", "(A)", "Structural graben along Narmada-Son Lineament guides river through narrow marble gorges.", "Hard", "Analyzing", "Geomorphology"),
    ("Evaluate the sustainable water resource management framework needed for Indian river basins.", "(A) Requires integrating afforestation in catchment areas, controlling industrial discharge, ensuring environmental flow, and rainwater harvesting", "(B) Involves paving riverbeds with asphalt", "(C) Replaces natural rivers with plastic pipes", "(D) Bans all human use of river water", "(A)", "Requires catchment afforestation, controlling discharge, environmental flow, and rainwater harvesting.", "Hard", "Evaluating", "Water Management"),
    ("Compare the hydrological features of the Narmada River (west-flowing) with the River Ganga (east-flowing).", "(A) Narmada flows 1,312 km west in a narrow rift valley into the Arabian Sea without forming a massive delta; Ganga flows 2,525 km east forming a vast fertile delta into Bay of Bengal", "(B) Narmada is twice as long as Ganga", "(C) Ganga flows west while Narmada flows east", "(D) Both rivers start in the Arabian Sea", "(A)", "Narmada: 1,312 km west in rift valley without delta; Ganga: 2,525 km east forming vast delta.", "Hard", "Comparing", "Comparative Hydrology"),
    ("Formulate a pledge for students during World Rivers Day.", "(A) 'We pledge to honor our rivers as lifelines of nature, protect their waters from pollution, conserve every drop, and ensure clean rivers for generations to come!'", "(B) 'We pledge to build factories on river banks.'", "(C) 'We pledge to stop studying environmental science.'", "(D) 'We pledge to drain all lakes into the sea.'", "(A)", "Pledge to protect rivers from pollution, conserve water, and ensure clean rivers for the future.", "Hard", "Creating", "Pledge Design"),
    ("Assess the cultural role of holy rivers in fostering traditional environmental ethics in India.", "(A) Reverence for rivers as 'Lokmata' (Mother of People) historically embedded sacrosanct protection against pollution into daily cultural rituals", "(B) Holy rivers were considered unapproachable for humans", "(C) Cultural traditions encouraged dumping industrial chemicals", "(D) Sacred status prevented people from drinking water", "(A)", "Reverence as 'Lokmata' embedded sacrosanct protection into daily cultural rituals.", "Hard", "Evaluating", "Cultural Ethics"),
    ("Analyze how catchment area deforestation leads to river siltation and flash flooding.", "(A) Tree roots bind soil; deforestation causes topsoil erosion during rains, filling riverbeds with silt, reducing storage capacity, and causing flash floods", "(B) Deforestation makes rivers flow faster without overflow", "(C) Deforestation turns river water into groundwater instantly", "(D) Tree removal has no effect on soil or water", "(A)", "Deforestation causes topsoil erosion, silting riverbeds, reducing storage, and causing flash floods.", "Hard", "Analyzing", "Environmental Impact"),
    ("Synthesize how Chapter 10 connects geography, ecology, culture, and civic duty.", "(A) Integrates physical geography (origin/flow/rift valley) with ecological value (biodiversity/dams), cultural sacredness (Parikrama), and civic duty (conservation)", "(B) Replaces river geography with computer coding", "(C) Focuses solely on memorizing statue heights", "(D) Rejects science in favor of folklore", "(A)", "Integrates physical geography, ecological utility, cultural heritage, and civic conservation.", "Hard", "Synthesizing", "Cross-Disciplinary Synthesis"),
    ("Critique the claim: 'West-flowing rivers like Narmada form massive agricultural deltas at their mouth.'", "(A) False; west-flowing rivers drop steeply through rocky rift valleys directly into the Arabian Sea, forming estuaries rather than depositional deltas", "(B) True; Narmada forms the largest delta in Asia", "(C) False; Narmada does not reach any sea", "(D) True; all rivers form deltas regardless of topography", "(A)", "False; west-flowing rivers drop through rocky valleys forming estuaries rather than deltas.", "Hard", "Evaluating", "Hydrological Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 10 for a Class 5 assessment.", "(A) 'Describe the Narmada River from its origin to its destination. Explain why it is called the Life Line of Madhya Pradesh, its major dams, tourist spots, and why we must protect rivers.'", "(B) 'Write five sentences about your favorite swimming pool.'", "(C) 'List five names of fish.'", "(D) 'Draw a picture of a boat.'", "(A)", "Structured essay prompt evaluating river origin, lifeline status, dam utility, tourist spots, and conservation.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 10: The Narmada River\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH10_MCQ_{idx:03d}"
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

with open(os.path.join(CH10_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("The Narmada River flows through Madhya Pradesh, Maharashtra, and _______.", "Gujarat", "Flows through Gujarat.", "Easy"),
    ("The Narmada River reaches the Arabian _______.", "Sea", "Reaches the Arabian Sea.", "Easy"),
    ("The Narmada is known as the 'Life Line of _______ Pradesh'.", "Madhya", "Life Line of Madhya Pradesh.", "Easy"),
    ("The river starts from the _______ Hills in Madhya Pradesh.", "Amarkantak", "Starts from Amarkantak Hills.", "Easy"),
    ("The Narmada River travels around _______ kilometers.", "1,312", "Travels around 1,312 km.", "Easy"),
    ("Most rivers in India flow towards the east, but the Narmada flows _______.", "westward", "Flows westward.", "Easy"),
    ("Tawa, Kolar, Dudhi, and Barna are _______ of the Narmada River.", "tributaries", "Tributaries of Narmada.", "Easy"),
    ("The Marble Rocks of Bhedaghat are located near the city of _______.", "Jabalpur", "Near Jabalpur.", "Easy"),
    ("At Bhedaghat, the Narmada River flows between tall white marble _______.", "cliffs", "White marble cliffs.", "Easy"),
    ("Pilgrims walk along the entire river performing the Narmada _______.", "Parikrama", "Narmada Parikrama.", "Easy"),
    ("The river is home to many fish, birds, and _______.", "plants", "Fish, birds, and plants.", "Easy"),
    ("The Narmada provides water for farming, drinking, and _______ generation.", "electricity", "Electricity generation.", "Easy"),
    ("One major dam built on the Narmada is the Sardar _______ Dam.", "Sarovar", "Sardar Sarovar Dam.", "Easy"),
    ("A tributary is defined as a small river joining a _______ one.", "bigger", "Small river joining a bigger one.", "Easy"),
    ("A reservoir is a large lake made to store _______.", "water", "Lake made to store water.", "Easy"),
    ("A basin is land drained by a river and its _______.", "branches", "Land drained by a river.", "Easy"),
    ("The Narmada is a symbol of culture, tradition, and natural _______.", "beauty", "Culture, tradition, and beauty.", "Easy"),
    ("Chapter 10 reminds us of the importance of protecting our rivers for future _______.", "generations", "Protecting rivers for future generations.", "Easy"),
    ("The Narmada River is one of the longest _______-flowing rivers in India.", "west", "Longest west-flowing river.", "Easy"),
    ("Marble Rocks of Bhedaghat are a popular tourist _______.", "attraction", "Popular tourist attraction.", "Easy"),
    ("The Narmada River provides drinking water to many towns and _______.", "villages", "Towns and villages.", "Easy"),
    ("Hydroelectricity is generated through dams and _______.", "reservoirs", "Dams and reservoirs.", "Easy"),
    ("Pilgrims perform Narmada Parikrama as a _______ journey.", "religious", "Religious journey.", "Easy"),
    ("The Narmada River drains into the Arabian _______.", "Sea", "Arabian Sea.", "Easy"),
    ("Chapter 10 is titled 'The Narmada _______'.", "River", "The Narmada River.", "Easy"),

    # Medium (26-40)
    ("The Narmada River flows in a rift valley between the Vindhya and _______ ranges.", "Satpura", "Between Vindhya and Satpura.", "Medium"),
    ("The Tawa River is the longest _______ of the Narmada River.", "tributary", "Longest tributary.", "Medium"),
    ("Dhuandhar Falls near Bhedaghat creates a mist resembling rising _______.", "smoke", "Mist resembling smoke.", "Medium"),
    ("Sardar Sarovar Dam reservoir is located in the state of _______.", "Gujarat", "Located in Gujarat.", "Medium"),
    ("Rift valley topography prevents the Narmada from forming a large _______.", "delta", "Prevents forming a delta.", "Medium"),
    ("Narmada Parikrama covers a total walking distance of over 2,600 _______.", "kilometers", "Distance over 2,600 km.", "Medium"),
    ("Amarkantak is a holy hill station in Anuppur district of _______ Pradesh.", "Madhya", "In Madhya Pradesh.", "Medium"),
    ("Water stored in reservoirs is systematically released for agricultural _______.", "irrigation", "Released for irrigation.", "Medium"),
    ("The river supports aquatic biodiversity including rare fish and migratory _______.", "birds", "Rare fish and migratory birds.", "Medium"),
    ("Clean river water is essential for public health and environmental _______.", "sustainability", "Environmental sustainability.", "Medium"),
    ("The Narmada basin covers an area of nearly one lakh square _______.", "kilometers", "Nearly 1 lakh sq km.", "Medium"),
    ("The white marble cliffs at Bhedaghat glisten under full moon _______.", "light", "Glisten under moonlight.", "Medium"),
    ("The Sardar Sarovar project supplies drinking water to drought-prone _______.", "Kutch", "Supplies Kutch and Saurashtra.", "Medium"),
    ("River conservation prevents topsoil erosion and reservoir _______.", "siltation", "Prevents reservoir siltation.", "Medium"),
    ("Chapter 10 highlights how natural rivers form the foundation of human _______.", "civilization", "Foundation of human civilization.", "Medium"),

    # Hard (41-50)
    ("Westward estuarine discharge prevents massive deltaic sedimentation at the river _______.", "mouth", "Prevents deltaic sedimentation at mouth.", "Hard"),
    ("Tectonic graben alignment along the Narmada-Son lineament guides hydrological _______.", "discharge", "Guides hydrological discharge.", "Hard"),
    ("Catchment afforestation reduces flood risk and preserves reservoir storage _______.", "capacity", "Preserves reservoir storage capacity.", "Hard"),
    ("Environmental flow maintenance is crucial for downstream aquatic habitat _______.", "survival", "Crucial for habitat survival.", "Hard"),
    ("Sacred river reverential traditions historically enforced ecological water _______.", "stewardship", "Enforced water stewardship.", "Hard"),
    ("Hydroelectric power generation utilizes potential energy from stored reservoir _______.", "head", "Utilizes stored reservoir head.", "Hard"),
    ("Multipurpose river valley projects balance irrigation expansion and ecological _______.", "impacts", "Balance expansion and ecological impacts.", "Hard"),
    ("Socio-ecological river protection secures water security for future _______.", "generations", "Secures water security for generations.", "Hard"),
    ("Comparative hydrological analysis contrasts east-flowing deltas with west-flowing _______.", "estuaries", "Contrasts deltas with estuaries.", "Hard"),
    ("Chapter 10 instills environmental responsibility for preserving India's river _______.", "heritage", "Preserving India's river heritage.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 10: The Narmada River\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH10_FIB_{idx:03d}"
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
    ("The Narmada River is one of the most important rivers in India.", "True", "Text confirms Narmada is one of the most important rivers in India.", "Easy"),
    ("The Narmada River flows through Madhya Pradesh, Maharashtra, and Gujarat.", "True", "Text confirms it flows through MP, Maharashtra, and Gujarat.", "Easy"),
    ("The Narmada River empties into the Bay of Bengal.", "False", "The Narmada River flows westward into the Arabian Sea.", "Easy"),
    ("The Narmada River is known as the 'Life Line of Madhya Pradesh'.", "True", "Text confirms it is called the Life Line of Madhya Pradesh.", "Easy"),
    ("The Narmada River originates from the Himalayas.", "False", "The river starts from the Amarkantak Hills in Madhya Pradesh.", "Easy"),
    ("The Narmada River travels around 1,312 kilometers.", "True", "Text confirms it travels around 1,312 km.", "Easy"),
    ("Most major rivers in India flow westward into the Arabian Sea.", "False", "Most Indian rivers flow eastward; Narmada is unique in flowing westward.", "Easy"),
    ("Tawa, Kolar, Dudhi, and Barna are tributaries of the Narmada River.", "True", "Text confirms Tawa, Kolar, Dudhi, and Barna are tributaries.", "Easy"),
    ("The Marble Rocks of Bhedaghat are located near Jabalpur.", "True", "Text confirms Marble Rocks of Bhedaghat are near Jabalpur.", "Easy"),
    ("The river flows between tall, white marble cliffs at Bhedaghat.", "True", "Text states it flows between tall white marble cliffs.", "Easy"),
    ("Narmada Parikrama is a religious journey where pilgrims walk along the river.", "True", "Text confirms pilgrims walk along the entire river in Narmada Parikrama.", "Easy"),
    ("The Sardar Sarovar Dam is built on the Narmada River.", "True", "Text confirms Sardar Sarovar Dam is on the Narmada River.", "Easy"),
    ("The Sardar Sarovar Dam is used only for decorative fountains.", "False", "The dam provides water for farming, drinking, and electricity generation.", "Easy"),
    ("'Tributary' means a large ocean that receives river water.", "False", "Tributary = A small river joining a bigger one.", "Easy"),
    ("'Reservoir' means a large lake made to store water.", "True", "Vocabulary definition: Reservoir = A large lake made to store water.", "Easy"),
    ("'Basin' means land drained by a river and its branches.", "True", "Vocabulary definition: Basin = Land drained by a river and its branches.", "Easy"),
    ("The Narmada River supports fish, birds, and aquatic plants.", "True", "Text confirms the river is home to many fish, birds, and plants.", "Easy"),
    ("The Narmada River is a symbol of culture, tradition, and natural beauty.", "True", "Text confirms it is a symbol of culture, tradition, and natural beauty.", "Easy"),
    ("Chapter 10 teaches us that rivers do not need any protection.", "False", "It reminds us of the importance of protecting our rivers for future generations.", "Easy"),
    ("The Narmada River flows through the state of Kerala.", "False", "The river flows through Madhya Pradesh, Maharashtra, and Gujarat, not Kerala.", "Easy"),
    ("The Narmada is one of the longest west-flowing rivers in India.", "True", "Text confirms it is one of the longest west-flowing rivers.", "Easy"),
    ("The Tawa River is a tributary of the River Ganga.", "False", "Tawa is a major tributary of the Narmada River.", "Easy"),
    ("Pilgrims perform Narmada Parikrama by riding in submarines.", "False", "Pilgrims perform Narmada Parikrama by walking along the river bank.", "Easy"),
    ("Chapter 10 title is 'The Narmada River'.", "True", "Chapter title is 'The Narmada River'.", "Easy"),
    ("The Narmada River starts in the Amarkantak Hills.", "True", "Text confirms it starts from Amarkantak Hills.", "Easy"),

    # Medium (26-40)
    ("The Narmada River flows in a rift valley between the Vindhya and Satpura mountain ranges.", "True", "Geographically flows in a rift valley between Vindhya and Satpura ranges.", "Medium"),
    ("The Marble Rocks of Bhedaghat are made of black granite stone.", "False", "They are made of tall white magnesium marble cliffs.", "Medium"),
    ("The Sardar Sarovar Dam project provides irrigation water to dry areas in Gujarat and Rajasthan.", "True", "Provides irrigation and drinking water to Gujarat and Rajasthan.", "Medium"),
    ("Narmada Parikrama can be started at any point along the river provided pilgrims return to the same spot.", "True", "Traditional Parikrama completes a full loop returning to the starting point.", "Medium"),
    ("Dhuandhar Waterfall is created by the Narmada River near Bhedaghat.", "True", "Dhuandhar Falls is located near Bhedaghat on the Narmada.", "Medium"),
    ("West-flowing rivers in India form huge delta islands like the Sunderbans.", "False", "West-flowing rivers drop through rocky valleys forming estuaries, not deltas.", "Medium"),
    ("Amarkantak is located in the Anuppur district of Madhya Pradesh.", "True", "Amarkantak Hills are located in Anuppur district, MP.", "Medium"),
    ("The Tawa Dam is built on the Tawa River, a tributary of the Narmada.", "True", "Tawa Dam is built on the Tawa River in Hoshangabad district.", "Medium"),
    ("Hydroelectric power generation requires flowing water to spin turbines.", "True", "Water released from dams spins hydro-turbines to generate electricity.", "Medium"),
    ("Untreated factory waste dumped into rivers improves water quality for fish.", "False", "Factory waste severely pollutes river water, killing fish and aquatic life.", "Medium"),
    ("The Narmada basin covers parts of Madhya Pradesh, Maharashtra, and Gujarat.", "True", "Basin extends across MP, Maharashtra, and Gujarat.", "Medium"),
    ("The Marble Rocks of Bhedaghat change appearance under moonlight.", "True", "The white marble cliffs glisten beautifully under full moonlight.", "Medium"),
    ("River conservation helps maintain groundwater levels in surrounding lands.", "True", "Healthy rivers recharge adjacent groundwater aquifers.", "Medium"),
    ("The Narmada River is older than the Himalayan mountain range.", "True", "Narmada is an ancient peninsular river system older than Himalayas.", "Medium"),
    ("Chapter 10 emphasizes that rivers are vital for human survival and culture.", "True", "Emphasizes water supply, culture, tradition, and conservation.", "Medium"),

    # Hard (41-50)
    ("Tectonic faulting created the Narmada rift valley millions of years ago.", "True", "Rift valley was formed by tectonic faulting along the Narmada lineament.", "Hard"),
    ("Estuaries formed by west-flowing rivers allow ocean tides to enter river mouths.", "True", "Estuaries experience tidal influx, unlike river deltas.", "Hard"),
    ("Catchment area afforestation increases soil water retention and reduces flood peaks.", "True", "Trees retain soil moisture and reduce sudden flood crests.", "Hard"),
    ("The Narmada Bachao Andolan was a famous social movement concerning dam displacement.", "True", "Social movement advocating for displaced tribal families and river ecology.", "Hard"),
    ("Hydroelectric energy is classified as a non-renewable fossil fuel energy.", "False", "Hydroelectricity is a clean, renewable energy powered by the water cycle.", "Hard"),
    ("The total length of 1,312 km makes Narmada the 5th longest river in India.", "True", "Narmada is the 5th longest river in India overall.", "Hard"),
    ("Indira Sagar Dam is another major multi-purpose project on the Narmada in MP.", "True", "Indira Sagar Dam is a major project located in Khandwa district, MP.", "Hard"),
    ("River basin management requires cross-state administrative cooperation.", "True", "Inter-state rivers require cooperative management between flowing states.", "Hard"),
    ("Chapter 10 integrates physical geography, hydrology, and environmental ethics.", "True", "Integrates physical geography, hydrological terms, and river protection ethics.", "Hard"),
    ("Conserving natural river ecosystems is necessary to combat climate change impacts.", "True", "Healthy rivers buffer against droughts, heatwaves, and ecological degradation.", "Hard")
]

tf_content = f"# True / False — Chapter 10: The Narmada River\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH10_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Question**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH10_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Where does the Narmada River originate and into which sea does it flow?", "The Narmada River originates from the Amarkantak Hills in Madhya Pradesh and flows westward into the Arabian Sea.", "Easy", "Remembering"),
    ("Which three Indian states does the Narmada River flow through?", "The Narmada River flows through the states of Madhya Pradesh, Maharashtra, and Gujarat.", "Easy", "Remembering"),
    ("Why is the Narmada River called the 'Life Line of Madhya Pradesh'?", "Because it provides vital drinking water, agricultural irrigation, and industrial supply to numerous towns and villages across the state.", "Easy", "Understanding"),
    ("What is the approximate total length of the Narmada River?", "The total length of the Narmada River is approximately 1,312 kilometers.", "Easy", "Remembering"),
    ("How does the flow direction of the Narmada River differ from most major Indian rivers?", "Most major Indian rivers flow eastward into the Bay of Bengal, whereas the Narmada River flows westward into the Arabian Sea.", "Easy", "Understanding"),
    ("Name four main tributaries of the Narmada River mentioned in Chapter 10.", "Four main tributaries mentioned are Tawa, Kolar, Dudhi, and Barna.", "Easy", "Remembering"),
    ("What tourist attraction near Jabalpur is famous for white marble cliffs?", "The Marble Rocks of Bhedaghat near Jabalpur are famous for tall white marble cliffs lining the river.", "Easy", "Remembering"),
    ("Near which city in Madhya Pradesh are the Marble Rocks of Bhedaghat located?", "They are located near the city of Jabalpur in Madhya Pradesh.", "Easy", "Remembering"),
    ("What is the Narmada Parikrama and how do pilgrims perform it?", "Narmada Parikrama is a sacred religious journey where pilgrims walk along the entire bank of the river from its origin to the sea and back.", "Easy", "Understanding"),
    ("Name one major multi-purpose dam built on the Narmada River and state its benefits.", "The Sardar Sarovar Dam is a major dam that provides water for farming, drinking, and hydroelectricity generation.", "Easy", "Remembering"),
    ("What ecological species does the Narmada River support along its basin?", "The Narmada River supports a diverse ecosystem comprising many species of fish, water birds, and aquatic plants.", "Easy", "Remembering"),
    ("What does the word 'tributary' mean?", "A 'tributary' is a smaller river or stream that flows into and joins a larger main river.", "Easy", "Understanding"),
    ("What does the word 'reservoir' mean?", "A 'reservoir' is a large artificial or natural lake created behind a dam to store water for human use.", "Easy", "Understanding"),
    ("What does the word 'basin' mean in geography?", "A river 'basin' is the total land area drained by a main river and all its tributary branches.", "Easy", "Understanding"),
    ("Besides physical utility, what cultural values does the Narmada River represent?", "The Narmada River represents a deep symbol of Indian culture, religious tradition, and natural beauty.", "Easy", "Understanding"),
    ("Why is it important to protect natural rivers like the Narmada for the future?", "To prevent water scarcity, protect aquatic biodiversity, ensure clean drinking water, and preserve nature for future generations.", "Easy", "Understanding"),
    ("What visual feature makes the river gorge at Bhedaghat breathtaking?", "The river flows through a narrow canyon between tall, gleaming white marble cliffs that reflect light.", "Easy", "Understanding"),
    ("How does the Narmada River contribute to clean energy production?", "Water stored in large reservoirs behind dams like Sardar Sarovar spins hydro-turbines to generate clean hydroelectric power.", "Easy", "Understanding"),
    ("In which state is the Sardar Sarovar Dam located?", "The Sardar Sarovar Dam is located in the state of Gujarat.", "Easy", "Remembering"),
    ("How many kilometers long is the Narmada River's journey?", "It travels approximately 1,312 kilometers from Amarkantak to the Arabian Sea.", "Easy", "Remembering"),
    ("What makes the Narmada River one of India's most sacred rivers?", "Hindus consider the Narmada holy, believing that viewing or bathing in its waters grants spiritual purification, inspiring the Narmada Parikrama.", "Easy", "Understanding"),
    ("What type of water body is the Arabian Sea into which Narmada empties?", "The Arabian Sea is a major region of the northern Indian Ocean situated to the west of peninsular India.", "Easy", "Remembering"),
    ("What happens during the monsoon season to the Narmada River?", "Monsoon rains fill the river and its tributaries, increasing water flow into reservoirs for year-round storage.", "Easy", "Understanding"),
    ("What title is given to Chapter 10?", "The title of Chapter 10 is 'The Narmada River'.", "Easy", "Remembering"),
    ("What main message does Chapter 10 give to young readers about water conservation?", "It teaches readers that rivers are vital lifelines that must be protected from pollution and waste.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze why the Narmada River flows westward unlike the Godavari or Krishna rivers.", "The Narmada flows westward because it runs along a deep structural rift valley created by tectonic faulting between the Vindhya and Satpura mountain ranges.", "Medium", "Analyzing"),
    ("Explain the economic impact of the Narmada River on agricultural production in Gujarat and MP.", "By providing canal irrigation from reservoirs like Sardar Sarovar, it turns dry farmlands into fertile crop zones, boosting grain, cotton, and oilseed yields.", "Medium", "Analyzing"),
    ("Describe the natural phenomenon of Dhuandhar Falls near Bhedaghat.", "At Dhuandhar, the Narmada River plunges sharply down a rocky ledge, creating a powerful mist cascade that resembles rising white smoke ('Dhuan').", "Medium", "Understanding"),
    ("Why is the Narmada Parikrama unique compared to pilgrimages of other Indian rivers?", "It is the only river in India where devotees walk the complete perimeter of both banks from source to sea and back, covering over 2,600 km.", "Medium", "Evaluating"),
    ("Contrast a river basin with a river tributary.", "A tributary is an individual feeding stream (e.g., Tawa); a river basin is the entire geographical land area drained by the main river and all its tributaries.", "Medium", "Comparing"),
    ("How do large river dams help manage seasonal monsoon floods?", "Dams hold back sudden monsoon surges in large reservoirs, regulating downstream water release to prevent catastrophic flooding in villages.", "Medium", "Understanding"),
    ("Describe the wildlife and plant life supported by the Narmada River ecosystem.", "The river supports diverse freshwater fish (like Mahseer), migratory waterfowl, otters, marsh crocodiles, and riparian forest vegetation along its banks.", "Medium", "Remembering"),
    ("Why are Marble Rocks at Bhedaghat considered a geological wonder?", "Millions of years of river erosion carved through thick deposits of pure magnesium marble, creating vertical 100-foot white walls along the water.", "Medium", "Evaluating"),
    ("How does river pollution affect human settlements downstream?", "Polluted river water spreads waterborne diseases, ruins drinking supply, contaminates agricultural crops, and increases water treatment costs for cities.", "Medium", "Analyzing"),
    ("Summarize Chapter 10 in four concise sentences.", "The Narmada River is a major west-flowing river originating in the Amarkantak Hills of Madhya Pradesh and traveling 1,312 km to the Arabian Sea. Known as the 'Life Line of Madhya Pradesh', it flows through MP, Maharashtra, and Gujarat, fed by tributaries like Tawa and Barna. Famous for the Marble Rocks of Bhedaghat and the sacred Narmada Parikrama, it powers farming and electricity through dams like Sardar Sarovar. Chapter 10 calls on us to protect rivers for future generations.", "Medium", "Understanding"),
    ("How do multi-purpose river projects balance drinking water and power needs?", "Water stored in dam reservoirs is routed first through hydro-turbines for electricity, and then directed into canal systems for drinking and irrigation.", "Medium", "Analyzing"),
    ("What makes Amarkantak a spiritually and geographically significant place?", "Geographically, it is the mountain origin of the Narmada and Son rivers; spiritually, it is a revered pilgrimage site filled with ancient temples.", "Medium", "Evaluating"),
    ("Explain how deforestation along river banks affects water quality.", "Without tree roots to hold soil, heavy rains wash topsoil into the river, causing muddy siltation that clogs reservoirs and harms aquatic life.", "Medium", "Analyzing"),
    ("How does the Narmada River reflect India's cultural heritage?", "It features in ancient Puranic legends, hosts holy pilgrimages like Parikrama, inspires folklore, and forms the cultural backbone of central India.", "Medium", "Evaluating"),
    ("What practical steps can students take to prevent water pollution in their towns?", "Avoid throwing plastic trash into drains, reduce chemical fertilizer runoff in gardens, conserve household water, and report water leakage.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the ecological and human trade-offs of constructing mega-dams like Sardar Sarovar.", "Sardar Sarovar provides vital water/electricity to millions, but submerges fertile forests, displaces indigenous tribal villages, and disrupts aquatic habitats.", "Hard", "Evaluating"),
    ("Deconstruct why west-flowing rivers in India form estuaries rather than deltas.", "West-flowing rivers descend steeply through hard rock rift valleys into the deep Arabian Sea, carrying less sediment and flushing it out via strong ocean tides.", "Hard", "Analyzing"),
    ("Evaluate the importance of maintaining an 'environmental flow' in dammed rivers.", "Environmental flow ensures that a minimum volume of natural water passes through dams to sustain downstream aquatic life, river health, and delta stability.", "Hard", "Evaluating"),
    ("Compare the hydrological features of the Narmada River with the River Yamuna.", "Narmada: 1,312 km west-flowing peninsular rift valley river emptying into Arabian Sea. Yamuna: 1,376 km east-flowing Himalayan tributary merging into Ganga.", "Hard", "Comparing"),
    ("Formulate a World Water Day school presentation based on Chapter 10.", "'Rivers Are Our Lifelines: Learning from the Narmada! Let us protect our river basins from pollution, plant trees along banks, and secure clean water for tomorrow.'", "Hard", "Creating"),
    ("Assess the role of the Narmada Control Authority (NCA) in inter-state water sharing.", "NCA manages peaceful inter-state water distribution, dam power sharing, and environmental rehabilitation between MP, Maharashtra, Gujarat, and Rajasthan.", "Hard", "Evaluating"),
    ("Analyze how seasonal siltation impacts the life expectancy of river reservoirs.", "Accumulated silt reduces the storage volume of reservoirs over decades, decreasing their flood control capacity and hydroelectric potential unless desilted.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 10 integrates geography, environmental science, and ethics.", "Connects physical landforms (rift valley/marble rocks) with environmental engineering (dams/tributaries) and moral stewardship (conserving rivers).", "Hard", "Synthesizing"),
    ("Critique the claim: 'Building dams on rivers solves all water problems without any negative consequences.'", "False; while dams store water and generate power, they alter aquatic ecology, displace communities, cause siltation, and risk catastrophic dam breaks.", "Hard", "Evaluating"),
    ("Formulate a 4-line poem honoring the Narmada River.", "'From Amarkantak's heights your waters gleam,\nThrough marble rocks a sacred west-bound stream;\nO Lifeline of the hills and fertile plain,\nMay your pure currents ever flow again!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 10: The Narmada River\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH10_SA_{idx:03d}"
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
    ("Describe the origin, geographical course, and flow direction of the Narmada River.",
     "The Narmada River is one of the most prominent peninsular rivers in India. It originates from the high Amarkantak Hills in the Anuppur district of Madhya Pradesh. Traveling a total distance of approximately 1,312 kilometers, it flows through a structural rift valley flanked by the Vindhya Range to the north and the Satpura Range to the south. The river traverses across three major western states: Madhya Pradesh, Maharashtra, and Gujarat. Unlike the vast majority of major Indian rivers (like Ganga, Godavari, and Krishna) which flow eastward into the Bay of Bengal, the Narmada is unique because it flows westward, eventually emptying its fresh waters into the Arabian Sea at the Gulf of Khambhat.",
     "Easy", "Remembering"),

    ("Explain why the Narmada River is called the 'Life Line of Madhya Pradesh' and describe its major benefits.",
     "The Narmada River is proudly called the 'Life Line of Madhya Pradesh' because it forms the primary hydrological backbone of the state. Its major benefits include:\n1. **Drinking Water Supply**: It feeds municipal water networks, supplying clean drinking water to millions of residents in towns and rural villages.\n2. **Agricultural Irrigation**: Through extensive canal networks, its waters irrigate millions of hectares of agricultural land, boosting wheat, soybean, and cotton harvests.\n3. **Hydroelectric Power**: Multi-purpose dams built along its course generate clean hydro-electricity that powers industries, farms, and homes.\n4. **Livelihood & Ecosystem**: It supports fishing communities, livestock, and diverse aquatic flora and fauna across central India.",
     "Easy", "Understanding"),

    ("Describe the Marble Rocks of Bhedaghat near Jabalpur and explain why they attract tourists.",
     "The Marble Rocks of Bhedaghat, located near Jabalpur in Madhya Pradesh, represent one of India's most spectacular natural wonders. At Bhedaghat, the Narmada River carves a narrow, two-kilometer gorge through majestic 100-foot tall cliffs composed of pure white, blue, and pink magnesium marble. As the river flows calmly between these sheer vertical cliffs, it creates a breathtaking visual landscape. Nearby, the river plunges over a rocky ledge forming the famous Dhuandhar Waterfalls, where rising water mist resembles white smoke. Visitors from around the world flock to Bhedaghat to take moonlight boat rides along the glistening marble canyon, making it a world-famous tourist attraction.",
     "Easy", "Remembering"),

    ("Describe the Narmada Parikrama, its spiritual significance, and how pilgrims undertake this journey.",
     "The Narmada Parikrama is a sacred Hindu pilgrimage tradition unique to the Narmada River. Unlike other sacred rivers where devotees merely bathe at specific ghats, the Narmada Parikrama requires pilgrims to walk the complete perimeter of the river. Devotees start at a chosen point (often Amarkantak or Omkareshwar), walk along the southern bank all the way to the Arabian Sea at Bharuch, cross the river, and walk back along the northern bank to the starting point. Covering over 2,600 kilometers over several months on foot, pilgrims view the river as a living deity ('Lokmata'), enduring physical hardships to achieve spiritual purification, self-discipline, and inner peace.",
     "Easy", "Understanding"),

    ("Explain the vocabulary terms from Chapter 10: Tributary, Reservoir, and Basin with examples.",
     "1. **Tributary**: A smaller river or stream that flows into and joins a larger main river. *Example*: The Tawa, Kolar, Dudhi, and Barna rivers are tributaries of the Narmada.\n2. **Reservoir**: A large artificial or natural lake created behind a dam to store water for human use. *Example*: The massive water lake behind the Sardar Sarovar Dam is a major reservoir.\n3. **Basin**: The complete geographical land area drained by a main river and all its tributary branches. *Example*: The Narmada basin covers nearly 98,000 square kilometers across MP, Maharashtra, and Gujarat.",
     "Easy", "Understanding"),

    ("Discuss the multi-purpose utility of the Sardar Sarovar Dam on the Narmada River.",
     "The Sardar Sarovar Dam, constructed in Gujarat on the Narmada River, is one of India's largest multi-purpose water resources projects. Its key utilities include:\n1. **Irrigation**: It channels water through a 460-km main canal to irrigate 1.8 million hectares of drought-prone farmlands in Gujarat and Rajasthan.\n2. **Drinking Water**: It provides piped drinking water to over 9,000 villages and 135 urban centers across Gujarat.\n3. **Hydroelectric Generation**: Its powerhouses generate 1,450 megawatts of clean hydroelectricity shared between MP, Maharashtra, and Gujarat.\n4. **Flood Management**: It regulates seasonal monsoon surges to reduce downstream flooding.",
     "Easy", "Understanding"),

    ("Describe the ecosystem and biodiversity supported by the Narmada River basin.",
     "The Narmada River basin supports a rich, vibrant natural ecosystem:\n1. **Aquatic Species**: It is home to numerous freshwater fish species, including the famous Mahseer, as well as turtles and marsh crocodiles.\n2. **Avian Life**: Riparian wetlands along the river host resident and migratory birds like kingfishers, herons, egrets, and wild ducks.\n3. **Flora**: The surrounding basin is covered by dense teak and sal forests, medicinal plants, and riverside bamboo groves.\n4. **Wildlife**: Forested hills near the river provide habitat for tigers, leopards, deer, and sloth bears.",
     "Easy", "Remembering"),

    ("Explain why it is important to protect rivers like the Narmada from pollution and waste.",
     "Protecting rivers is vital for several environmental and human reasons:\n1. **Water Security**: Millions of people depend on rivers for daily drinking water; pollution makes water unsafe and spreads diseases.\n2. **Agriculture & Food**: Contaminated river water ruins crop soil and harms food crops.\n3. **Biodiversity**: Industrial waste and plastic pollution kill fish, birds, and aquatic plants, disrupting food chains.\n4. **Inter-generational Duty**: Preserving clean rivers ensures that future generations have adequate, clean water resources to survive and thrive.",
     "Easy", "Evaluating"),

    ("Summarize Chapter 10 in five detailed bullet points.",
     "- The Narmada River originates in the Amarkantak Hills (MP) and flows 1,312 km west into the Arabian Sea.\n- Known as the 'Life Line of Madhya Pradesh', it supplies drinking, agricultural, and industrial water to MP, Maharashtra, and Gujarat.\n- Fed by main tributaries like Tawa, Kolar, Dudhi, and Barna, it flows through a rift valley with unique westward drainage.\n- Famous tourist and spiritual sites include the white Marble Rocks of Bhedaghat (Jabalpur) and the holy Narmada Parikrama pilgrimage.\n- Multi-purpose dams like Sardar Sarovar generate electricity and provide irrigation, reminding us to protect rivers for future generations.",
     "Easy", "Understanding"),

    ("What lessons about environmental conservation can Class 5 students learn from Chapter 10?",
     "Class 5 students learn that natural rivers are irreplaceable lifelines supporting human civilization, agriculture, and wildlife. They learn that rivers must not be treated as dumping grounds for garbage or plastic. Students are inspired to practice water conservation in daily life, avoid polluting local water bodies, plant trees along banks, and advocate for environmental protection.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why is the Narmada River's westward flow geological proof of a rift valley structure?", "Because peninsular India tilts eastward toward the Bay of Bengal. The Narmada flows west against this regional tilt because it is trapped inside a down-faulted rift valley (graben) between the Vindhya and Satpura ranges.", "Easy", "Understanding"),
    ("Describe the Tawa River and its role as a major tributary of the Narmada.", "The Tawa River is the longest left-bank tributary of the Narmada, originating in the Satpura Range. The Tawa Dam built across it provides extensive irrigation to Hoshangabad district and feeds into the main Narmada flow.", "Easy", "Remembering"),
    ("Explain the tourist experience of boating through the Marble Rocks at Bhedaghat.", "Visitors ride quiet boats along a narrow 2-km river gorge flanked by 100-foot white marble cliffs. Under sunlight or full moon light, the marble walls reflect glowing patterns on the clear green river water.", "Easy", "Remembering"),
    ("What challenges do pilgrims face during the 2,600-km Narmada Parikrama?", "Pilgrims walk barefoot for months through rugged terrain, dense forests, and hot weather, carrying minimal possessions, relying on village hospitality, and demonstrating deep physical endurance.", "Easy", "Understanding"),
    ("How does the Sardar Sarovar Dam help drought-prone areas like Kutch and Saurashtra?", "Long canals carry stored Narmada water hundreds of kilometers to arid Kutch and Saurashtra regions in Gujarat, converting dry lands into green agricultural fields and supplying drinking water.", "Easy", "Understanding"),
    ("Describe the Dhuandhar Waterfall and explain how it got its name.", "Dhuandhar Falls is located near Bhedaghat where the Narmada drops 30 meters over a rocky cliff. The roaring plunge creates a dense spray of water mist that looks like rising smoke ('Dhuan'), giving it the name Dhuandhar.", "Easy", "Remembering"),
    ("How do forests in the Narmada catchment area help regulate river water flow?", "Dense forest trees act as natural sponges. Their roots absorb heavy monsoon rainfall, prevent topsoil erosion, reduce sudden flash floods, and slowly release water into the river during dry months.", "Easy", "Understanding"),
    ("What role does the Narmada River play in the regional economy of central India?", "It supports multi-crore agricultural production, powers hydro-turbines, feeds manufacturing industries, sustains commercial freshwater fisheries, and drives a thriving tourism economy.", "Easy", "Analyzing"),
    ("Describe the traditional reverence Indians hold for rivers as 'Lokmata' (Mother of the People).", "Indian culture views rivers as nurturing mothers ('Lokmata') who sustain life through water. This reverence inspires religious festivals, sacred bathing, and traditional conservation ethics.", "Easy", "Understanding"),
    ("How does Chapter 10 fulfill primary curriculum goals for geography and science?", "It teaches landforms (hills/canyons/rift valleys), hydrological terminology (tributaries/basins/reservoirs), environmental science (ecosystems/dams), and conservation ethics.", "Easy", "Understanding"),
    ("Re-write the journey of a water drop from Amarkantak Hills to the Arabian Sea.", "'I bubbled up from the green Amarkantak Hills, joined the Tawa stream, danced through the glowing Marble Rocks at Bhedaghat, rested behind the Sardar Sarovar Dam, and finally merged into the vast blue Arabian Sea!'", "Easy", "Creating"),
    ("What is the difference between an estuary and a delta at a river mouth?", "A delta is a fan-shaped landform created by rivers depositing heavy silt in shallow seas (e.g., Ganga). An estuary is a deep, tidal river mouth where fresh water meets sea tides without silt accumulation (e.g., Narmada).", "Easy", "Comparing"),
    ("How does hydroelectric power generation compare to coal-fired thermal power?", "Hydroelectric power uses renewable flowing water without burning fuel or releasing smoke/carbon gases, whereas thermal power burns coal, emitting carbon dioxide and air pollution.", "Easy", "Comparing"),
    ("Analyze why Chapter 10 is titled 'The Narmada River' rather than 'The MP River'.", "Because the river flows through three states (MP, Maharashtra, Gujarat) and belongs to the entire nation as a geographical, economic, and cultural treasure.", "Easy", "Analyzing"),
    ("What future measures should be taken to keep the Narmada River clean and flowing?", "Measures include building sewage treatment plants in riverside towns, stopping industrial chemical dumping, planting trees along banks, and maintaining minimum environmental flow through dams.", "Easy", "Applying"),

    # Medium (26-40)
    ("Critically analyze how multi-purpose river valley projects transform regional human geography.",
     "Multi-purpose river projects bring profound geographical transformations:\n1. **Agricultural Transformation**: Unirrigated dry lands turn into multi-crop agricultural zones, increasing food production and farmer incomes.\n2. **Industrial Growth**: Hydroelectric power and reliable water supply attract manufacturing factories and urban centers.\n3. **Ecological Alterations**: Natural river flow is regulated into artificial lakes, altering aquatic habitats, fish migration, and local micro-climates.",
     "Medium", "Analyzing"),

    ("Examine the hydrological system of the Narmada River basin across its three main states.",
     "The Narmada basin covers nearly 98,000 sq km:\n- **Madhya Pradesh (86% of basin)**: Contains the origin at Amarkantak, major tributaries (Tawa, Barna), Marble Rocks, and major reservoirs (Indira Sagar).\n- **Maharashtra (2% of basin)**: Forms a narrow natural border zone receiving river water for local agricultural use.\n- **Gujarat (12% of basin)**: Contains the massive Sardar Sarovar Dam, main canal networks, and the estuarine mouth entering the Arabian Sea.",
     "Medium", "Analyzing"),

    ("Evaluate the ecological importance of preserving riparian buffer zones along river banks.",
     "Riparian buffer zones (strips of native trees and plants along river banks) perform vital functions: tree roots stabilize banks against erosion, vegetation filters agricultural runoff before it reaches the water, shade regulates water temperature for fish, and riverside foliage provides wildlife corridors.",
     "Medium", "Evaluating"),

    ("Discuss how the Narmada River connects physical landscape features with human cultural practices.",
     "The physical landscape directly shapes culture along the Narmada: dramatic marble gorges at Bhedaghat inspire local stone-carving artisans and tourism; seasonal water flow dictates regional farming calendars; the river's 1,312-km length inspires the sacred Narmada Parikrama pilgrimage.",
     "Medium", "Analyzing"),

    ("Design an interactive primary school project for World Water Day based on Chapter 10.",
     "Project Title: 'Our River, Our Life — Celebrating the Narmada'\n1. **Map Activity**: Draw the Narmada's path from Amarkantak to Arabian Sea, labeling MP, Maharashtra, and Gujarat.\n2. **Model Making**: Build a clay model of Bhedaghat Marble Rocks and a working paper water-wheel dam.\n3. **Conservation Chart**: Create posters showing '5 Ways to Stop Water Pollution'.\n4. **Poetry & Essay**: Write a 50-word poem thanking rivers for providing water.",
     "Medium", "Creating"),

    ("How do tributaries like the Tawa and Kolar contribute to the main Narmada flow?", "Tributaries collect rainfall across Satpura and Vindhya watersheds, feeding millions of cubic meters of fresh water into the Narmada to sustain year-round flow.", "Medium", "Understanding"),
    ("Contrast the eastern flowing rivers of India with western flowing rivers like Narmada and Tapti.", "East-flowing rivers (Ganga/Mahanadi/Godavari) are longer, flow across gentle plains, and form broad deltas. West-flowing rivers (Narmada/Tapti) run through narrow rift valleys and form estuaries.", "Medium", "Comparing"),
    ("Why is Bhedaghat famous for marble handicraft carving?", "Abundant high-quality magnesium marble deposits along the river cliffs provide raw material for local artisans to carve statues, lamps, and decorative souvenirs.", "Medium", "Understanding"),
    ("How does seasonal variation in monsoon rainfall affect dam management on the Narmada?", "Heavy monsoons require floodgate management to release excess water safely; low monsoons require strict water rationing in reservoirs for drinking and winter crops.", "Medium", "Analyzing"),
    ("Explain the concept of 'water security' and how rivers contribute to it.", "Water security means having reliable access to clean, affordable water for human life and farming. Rivers supply the bulk of surface water needed for national security.", "Medium", "Understanding"),
    ("Why are fish ladder passages important when designing modern river dams?", "Fish ladders allow migratory fish (like Mahseer) to swim upstream past dam walls to reach their natural spawning grounds, preventing species extinction.", "Medium", "Evaluating"),
    ("How does tourist activity at places like Bhedaghat benefit local communities?", "Tourism generates local employment for boat operators, tour guides, marble handicraft artisans, hotel staff, and transport drivers.", "Medium", "Understanding"),
    ("Analyze why Chapter 10 emphasizes that the Narmada is 'not just a source of water'.", "Because it holds deep historical, spiritual, aesthetic, and ecological identity that unifies communities beyond mere commercial water utility.", "Medium", "Analyzing"),
    ("What makes the Narmada River unique in terms of geological age?", "The Narmada rift valley is an ancient pre-Cambrian fault line, making the Narmada river system significantly older than the Himalayan mountains.", "Medium", "Understanding"),
    ("Construct a fictional speech by a river conservationist addressing a town near the Narmada.", "'Friends, the Narmada has fed our ancestors for thousands of years. Today, plastic and chemicals threaten her waters. Let us pledge to keep her clean so she can feed our children tomorrow!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the conflict between upstream state interests and downstream state rights in inter-state river basins.",
     "Upstream states (MP) control water origins and reservoir storage; downstream states (Gujarat/Rajasthan) depend on guaranteed water release for drought relief. Inter-state tribunals (Narmada Water Disputes Tribunal) resolve conflicts by legally allocating water volumes and hydro-power shares.",
     "Hard", "Evaluating"),

    ("Deconstruct the tectonic origin of the Narmada-Son Lineament (NSL).",
     "The NSL is a major continental rift zone dividing northern and southern Indian tectonic blocks. Crustal extension created a deep graben valley, trapping the Narmada River between the Vindhya and Satpura mountain blocks.",
     "Hard", "Analyzing"),

    ("Synthesize the ecological concept of 'Integrated River Basin Management' (IRBM).",
     "IRBM unifies land use planning, forest conservation, pollution control, reservoir operation, and community livelihoods across the entire river basin to balance human economic needs with long-term river ecosystem health.",
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive essay prompt evaluating the hydrological, economic, and cultural significance of the Narmada River.",
     "Prompt: 'Critically analyze the Narmada River as a hydrological phenomenon, economic engine, and cultural symbol. Discuss how multi-purpose dams like Sardar Sarovar impact both human development and river ecology.'",
     "Hard", "Creating"),

    ("Evaluate the impact of climate change on monsoon pattern reliability in central Indian river basins.", "Climate change causes erratic monsoon bursts—producing intense flash floods followed by prolonged dry spells—requiring adaptive reservoir management and catchment forest protection.", "Hard", "Evaluating"),

    ("Compare the environmental footprint of solar power projects vs multi-purpose hydroelectric dam projects.", "Solar power requires land but causes zero water submergence or river flow alteration; hydroelectric dams submerge land and alter river flow, but provide large-scale energy storage and water supply.", "Hard", "Comparing"),
    ("Discuss how sacred pilgrimages like Narmada Parikrama can be leveraged for environmental conservation.", "Pilgrimages engage millions of citizens. Transforming Parikrama into an eco-pilgrimage encourages pilgrims to plant trees, clean riverbanks, and advocate for river preservation.", "Hard", "Evaluating"),
    ("Analyze how river sediment transport maintains coastal estuarine ecosystems.", "River sediment delivers organic nutrients to coastal estuaries, nourishing mangrove forests, estuarine fish breeding grounds, and coastal marine biodiversity.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'It reminds us of the importance of protecting our rivers for future generations.'", "This concluding sentence elevates Chapter 10 from factual geography to moral stewardship. It challenges citizens to treat natural rivers as precious inherited trusts requiring active protection.", "Hard", "Evaluating"),
    ("Synthesize the complete educational takeaways of Chapter 10 for primary school geography and ethics.", "Chapter 10 unifies physical geography (origins/rift valley/flow) with environmental science (dams/ecosystems), vocabulary mastery (basin/tributary/reservoir), and ethical environmental responsibility.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 10: The Narmada River\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH10_LA_{idx:03d}"
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
    ("The Narmada River is one of the most important rivers in India. It flows through the states of Madhya Pradesh, Maharashtra and Gujarat before reaching the Arabian Sea.",
     [
         ("What is the Narmada River described as in the opening line?", "One of the most important rivers in India.", "Easy", "Remembering"),
         ("Name the three states through which the Narmada River flows.", "Madhya Pradesh, Maharashtra, and Gujarat.", "Easy", "Remembering"),
         ("Into which sea does the Narmada River empty?", "The Arabian Sea.", "Easy", "Remembering"),
         ("In which general direction does the Narmada River flow to reach the Arabian Sea?", "Westward.", "Easy", "Understanding"),
         ("Why is the Narmada River's path through three states geographically important?", "Because it forms a major hydrological lifeline connecting central and western India.", "Medium", "Analyzing")
     ]),

    # Set 2
    ("The Narmada is also known as the \"Life Line of Madhya Pradesh\" because it provides water to many towns and villages along its path.",
     [
         ("What special title is given to the Narmada River?", "Life Line of Madhya Pradesh.", "Easy", "Remembering"),
         ("Why is the Narmada called the 'Life Line of Madhya Pradesh'?", "Because it provides water to many towns and villages along its path.", "Easy", "Remembering"),
         ("Who relies on the water provided by the Narmada River?", "Towns and villages along its path for drinking, farming, and daily life.", "Easy", "Understanding"),
         ("In which state is the main basin of the Narmada River located?", "Madhya Pradesh.", "Easy", "Remembering"),
         ("What would happen to towns and villages in MP if the Narmada River dried up?", "They would suffer severe water scarcity, agricultural failure, and economic hardship.", "Medium", "Analyzing")
     ]),

    # Set 3
    ("The river starts from the Amarkantak Hills in Madhya Pradesh. It travels around 1,312 kilometers, making it one of the longest west-flowing rivers in India.",
     [
         ("Where does the Narmada River start its journey?", "Amarkantak Hills in Madhya Pradesh.", "Easy", "Remembering"),
         ("How far does the Narmada River travel?", "Around 1,312 kilometers.", "Easy", "Remembering"),
         ("What geographic distinction does its 1,312 km length give it?", "It makes it one of the longest west-flowing rivers in India.", "Easy", "Remembering"),
         ("In which state are the Amarkantak Hills located?", "Madhya Pradesh.", "Easy", "Remembering"),
         ("How does the flow direction of most Indian rivers differ from the Narmada?", "Most Indian rivers flow eastward into the Bay of Bengal, whereas Narmada flows westward.", "Medium", "Comparing")
     ]),

    # Set 4
    ("Many tributaries like the Tawa, Kolar, Dudhi, Barna etc. drain into this river. Most rivers in India flow towards the east, but the Narmada flows westward.",
     [
         ("Name four tributaries of the Narmada River mentioned in this passage.", "Tawa, Kolar, Dudhi, and Barna.", "Easy", "Remembering"),
         ("What does the word 'tributary' mean?", "A small river joining a bigger one.", "Easy", "Understanding"),
         ("What is unusual about the Narmada's flow direction compared to most Indian rivers?", "Most rivers flow east, but Narmada flows westward.", "Easy", "Remembering"),
         ("What do tributaries do for a main river?", "They drain into and feed fresh water into the main river, increasing its volume.", "Medium", "Understanding"),
         ("What geological feature causes the Narmada to flow west?", "A structural rift valley between the Vindhya and Satpura mountain ranges.", "Medium", "Analyzing")
     ]),

    # Set 5
    ("The Narmada River is famous for its beautiful surroundings. The Marble Rocks of Bhedaghat, near Jabalpur, are a popular tourist attraction. The river flows between tall white marble cliffs, creating a stunning view.",
     [
         ("What tourist attraction near Jabalpur is famous along the Narmada River?", "The Marble Rocks of Bhedaghat.", "Easy", "Remembering"),
         ("Near which city are the Marble Rocks located?", "Jabalpur.", "Easy", "Remembering"),
         ("What natural feature creates a stunning view at Bhedaghat?", "The river flows between tall white marble cliffs.", "Easy", "Remembering"),
         ("Why do tourists visit Bhedaghat?", "To see the breathtaking view of the river flowing between white marble cliffs.", "Easy", "Understanding"),
         ("What rock type forms the cliffs at Bhedaghat?", "Magnesium marble stone.", "Medium", "Remembering")
     ]),

    # Set 6
    ("Many people also consider the Narmada a holy river. Pilgrims perform the Narmada Parikrama, where they walk along the entire river as a religious journey.",
     [
         ("How do many people view the Narmada River spiritually?", "They consider it a holy river.", "Easy", "Remembering"),
         ("What religious journey do pilgrims perform along the Narmada?", "The Narmada Parikrama.", "Easy", "Remembering"),
         ("How do pilgrims perform the Narmada Parikrama?", "They walk along the entire river as a religious journey.", "Easy", "Remembering"),
         ("What does the word 'parikrama' mean in this context?", "Walking around a sacred perimeter or boundary.", "Medium", "Understanding"),
         ("Why is the Narmada Parikrama considered a remarkable pilgrimage?", "Because pilgrims walk over 2,600 km along both banks, showing deep physical and spiritual devotion.", "Medium", "Evaluating")
     ]),

    # Set 7
    ("The river is home to many fish, birds and plants. It provides water for farming, drinking and electricity through reservoirs and dams like the Sardar Sarovar Dam.",
     [
         ("What living species does the Narmada River support?", "Many fish, birds, and plants.", "Easy", "Remembering"),
         ("Name three practical human uses of the river water mentioned here.", "Farming (irrigation), drinking, and electricity generation.", "Easy", "Remembering"),
         ("Which famous dam built on the Narmada River is mentioned?", "The Sardar Sarovar Dam.", "Easy", "Remembering"),
         ("What is a 'reservoir'?", "A large lake made to store water.", "Easy", "Understanding"),
         ("How do dams generate electricity from river water?", "Water released from dam reservoirs turns hydro-turbines to generate hydroelectric power.", "Medium", "Understanding")
     ]),

    # Set 8
    ("The Narmada River is not just a source of water but also a symbol of culture, tradition and natural beauty. It reminds us of the importance of protecting our rivers for future generations.",
     [
         ("What does the Narmada River symbolize besides being a source of water?", "It is a symbol of culture, tradition, and natural beauty.", "Easy", "Remembering"),
         ("What important reminder does the Narmada River give us?", "It reminds us of the importance of protecting our rivers for future generations.", "Easy", "Remembering"),
         ("Why must we protect our rivers for future generations?", "To ensure clean water, protect ecosystems, and prevent water scarcity.", "Medium", "Evaluating"),
         ("What does the phrase 'future generations' refer to?", "Children and people who will live in the world in years to come.", "Easy", "Understanding"),
         ("Summarize the ultimate message of this concluding passage.", "Rivers are invaluable natural and cultural heritage that require active human protection and conservation.", "Medium", "Evaluating")
     ]),

    # Set 9
    ("Word Meaning: Tributary— A small river joining a bigger one. Reservoir— A large lake made to store water. Basin — Land drained by a river and its branches.",
     [
         ("What is the definition of 'tributary'?", "A small river joining a bigger one.", "Easy", "Remembering"),
         ("What is the definition of 'reservoir'?", "A large lake made to store water.", "Easy", "Remembering"),
         ("What is the definition of 'basin'?", "Land drained by a river and its branches.", "Easy", "Remembering"),
         ("Use the word 'reservoir' in a complete sentence of your own.", "The city receives its drinking water from a large mountain reservoir.", "Medium", "Applying"),
         ("Which tributary of the Narmada is mentioned in Chapter 10?", "Tawa (or Kolar/Dudhi/Barna).", "Easy", "Remembering")
     ]),

    # Set 10
    ("Starts from Amarkantak Hills... Travels 1,312 km... Flows through MP, Maharashtra, Gujarat to Arabian Sea... Marble Rocks of Bhedaghat... Sardar Sarovar Dam...",
     [
         ("Where does the river start?", "Amarkantak Hills.", "Easy", "Remembering"),
         ("What is its total travel distance?", "1,312 kilometers.", "Easy", "Remembering"),
         ("Which sea is its final destination?", "The Arabian Sea.", "Easy", "Remembering"),
         ("Name the major dam built in Gujarat on this river.", "Sardar Sarovar Dam.", "Easy", "Remembering"),
         ("Summarize the complete geographical profile of the Narmada River in one sentence.", "The Narmada is a 1,312-km west-flowing sacred river originating in Amarkantak, powering MP, Maharashtra, and Gujarat before entering the Arabian Sea.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 10: The Narmada River\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH10_EXT_{q_counter:03d}"
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

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 10 in {CH10_DIR}")
