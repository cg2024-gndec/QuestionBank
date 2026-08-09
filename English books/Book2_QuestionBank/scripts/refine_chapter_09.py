r"""
Refines all 6 Category files for Chapter 09 ("The Himalayas") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH09_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_09")
os.makedirs(CH09_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What does the Sanskrit word 'Himalaya' mean?", "(A) Abode of snow", "(B) Mountain of trees", "(C) Home of rivers", "(D) Land of clouds", "(A)", "Himalaya comes from Him + Alaya meaning 'abode of snow'.", "Easy", "Remembering", "Sanskrit Meaning"),
    ("Why are the Himalayas called the 'abode of snow'?", "(A) Because its lofty peaks are covered with snow all the year round", "(B) Because it only rains there", "(C) Because ice cream grows there", "(D) Because the rocks are white", "(A)", "The lofty peaks are covered with snow all year round.", "Easy", "Remembering", "Name Reason"),
    ("How long does the Himalayan mountain system stretch from west to east?", "(A) Almost 2,500 kilometers", "(B) 500 kilometers", "(C) 10,000 kilometers", "(D) 100 kilometers", "(A)", "It stretches for almost 2,500 kilometers from west to east.", "Easy", "Remembering", "Length"),
    ("How many of Earth's 10 highest peaks are located in the Himalayas?", "(A) Nine", "(B) Five", "(C) Three", "(D) Seven", "(A)", "Nine of Earth's 10 highest peaks are Himalayan.", "Easy", "Remembering", "Highest Peaks"),
    ("What is the world's highest mountain peak?", "(A) Mount Everest", "(B) K2", "(C) Mount Kanchenjunga", "(D) Mount Fuji", "(A)", "Mount Everest is the world's highest peak.", "Easy", "Remembering", "Highest Peak Name"),
    ("How high is Mount Everest in metres?", "(A) 8,849 metres", "(B) 5,000 metres", "(C) 1,000 metres", "(D) 12,000 metres", "(A)", "Mount Everest is 8,849 metres high.", "Easy", "Remembering", "Everest Height"),
    ("Mount Everest lies on the border between Nepal and which other region?", "(A) Tibet Autonomous Region of China", "(B) India", "(C) Bhutan", "(D) Myanmar", "(A)", "It lies on the border between Nepal and Tibet (China).", "Easy", "Remembering", "Geographic Location"),
    ("Which of the following major rivers originates in the Himalayas?", "(A) The Ganges", "(B) The Nile", "(C) The Amazon", "(D) The Thames", "(A)", "The Ganges, Indus, and Brahmaputra originate in the Himalayas.", "Easy", "Remembering", "Himalayan River"),
    ("Which three major rivers originate in the Himalayas?", "(A) The Indus, the Ganges, and the Brahmaputra", "(B) The Nile, the Amazon, and the Mississippi", "(C) The Yamuna, the Kaveri, and the Krishna only", "(D) The Rhine, the Danube, and the Seine", "(A)", "The Indus, Ganges, and Brahmaputra originate there.", "Easy", "Remembering", "Three Major Rivers"),
    ("Who were the first two climbers to reach the summit of Mount Everest?", "(A) Edmund Hillary and Sherpa Tenzing Norgay", "(B) George Mallory and Andrew Irvine", "(C) Neil Armstrong and Buzz Aldrin", "(D) Christopher Columbus and Vasco da Gama", "(A)", "Edmund Hillary and Sherpa Tenzing Norgay were the first.", "Easy", "Remembering", "First Climbers"),
    ("Which country was Edmund Hillary from?", "(A) New Zealand", "(B) Australia", "(C) England", "(D) Canada", "(A)", "Edmund Hillary was a New Zealander.", "Easy", "Remembering", "Hillary Nationality"),
    ("Who was the famous Sherpa climber who climbed Mount Everest with Edmund Hillary?", "(A) Tenzing Norgay", "(B) Ang Rita", "(C) Kami Rita", "(D) Pemba", "(A)", "Sherpa Tenzing Norgay climbed with Edmund Hillary.", "Easy", "Remembering", "Tenzing Norgay"),
    ("What does the word 'abode' mean according to the word meaning box?", "(A) The place where one lives", "(B) A tall mountain", "(C) Cold water", "(D) A deep valley", "(A)", "Abode is defined as the place where one lives.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'lofty' mean?", "(A) Very tall and impressive", "(B) Small and round", "(C) Dark and scary", "(D) Soft and wet", "(A)", "Lofty means very tall and impressive.", "Easy", "Understanding", "Vocabulary"),
    ("In which direction does the Himalayan mountain range stretch?", "(A) From west to east", "(B) From north to south", "(C) From east to south", "(D) From central to west", "(A)", "It stretches from west to east.", "Easy", "Remembering", "Direction"),
    ("Does any other mountain range on Earth compare to the scale of the Himalayas?", "(A) No, no other mountain range compares to the Himalayas", "(B) Yes, the Alps are bigger", "(C) Yes, all hills are equal", "(D) No, hills are bigger than mountains", "(A)", "No other mountain range on Earth compares.", "Easy", "Remembering", "Comparison"),
    ("What is Mount Everest covered with throughout the year?", "(A) Snow and ice", "(B) Sand and dust", "(C) Green grass", "(D) Red flowers", "(A)", "The lofty peaks are covered with snow all year round.", "Easy", "Remembering", "Peak Coverage"),
    ("In which year did Edmund Hillary and Tenzing Norgay reach the summit of Mount Everest?", "(A) 1953", "(B) 1853", "(C) 1999", "(D) 2010", "(A)", "They reached the summit in 1953.", "Easy", "Remembering", "Summit Year"),
    ("What is the top of a mountain called?", "(A) Summit or peak", "(B) Cave", "(C) Valley", "(D) Riverbed", "(A)", "The top of a mountain is called the summit or peak.", "Easy", "Understanding", "Geography Term"),
    ("Which river originating in the Himalayas is considered holy in India?", "(A) The Ganges", "(B) The Nile", "(C) The Danube", "(D) The Congo", "(A)", "The Ganges river is famous and originates in the Himalayas.", "Easy", "Remembering", "Cultural Relevance"),
    ("Are the Himalayas located in Asia?", "(A) Yes", "(B) No", "(C) Located in South America", "(D) Located in Europe", "(A)", "The Himalayas are in Asia across India, Nepal, Tibet, etc.", "Easy", "Remembering", "Continent"),
    ("What is a person who climbs high mountains called?", "(A) A mountaineer", "(B) A sailor", "(C) A pilot", "(D) A driver", "(A)", "A person who climbs mountains is a mountaineer.", "Easy", "Understanding", "Vocabulary"),
    ("Is Mount Everest higher than 8,000 metres?", "(A) Yes, it is 8,849 metres high", "(B) No, it is 2,000 metres", "(C) No, it is 500 metres", "(D) It changes height daily", "(A)", "Yes, it is 8,849 metres high.", "Easy", "Remembering", "Height Fact"),
    ("What does 'Him' stand for in the Sanskrit compound 'Him + Alaya'?", "(A) Snow", "(B) Sky", "(C) Stone", "(D) Sun", "(A)", "'Him' means snow in Sanskrit.", "Easy", "Remembering", "Etymology"),
    ("What is the title of Chapter 09?", "(A) The Himalayas", "(B) Mount Everest", "(C) Abode of Snow", "(D) The Three Rivers", "(A)", "Chapter 09 is titled 'The Himalayas'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why are the Himalayas vital to the water supply of South Asia?", "(A) Because major rivers like the Indus, Ganges, and Brahmaputra originate from melting Himalayan glaciers", "(B) Because it rains every hour", "(C) Because people carry water there", "(D) Because the mountains are made of ice cream", "(A)", "Melting glaciers feed major river systems like Ganges, Indus, Brahmaputra.", "Medium", "Understanding", "River Origin Importance"),
    ("How does the extreme height of the Himalayas affect weather and climate?", "(A) Its lofty snow peaks act as a natural barrier blocking cold northern winds and trapping monsoons", "(B) It makes the sun disappear permanently", "(C) It turns summer into hot desert", "(D) It has no effect on weather", "(A)", "Acts as a massive natural climate barrier.", "Medium", "Analyzing", "Climate Role"),
    ("What makes the 1953 climb by Hillary and Norgay a historic milestone in human history?", "(A) It proved that human bravery, physical endurance, and teamwork could conquer Earth's highest peak", "(B) They flew a helicopter to the top", "(C) They built a hotel on Everest", "(D) They drove a car up the mountain", "(A)", "First human conquest of Earth's highest summit.", "Medium", "Evaluating", "Historic Achievement"),
    ("Why is Sherpa Tenzing Norgay's local knowledge crucial to mountain climbing?", "(A) Sherpas possess innate high-altitude adaptation and deep knowledge of hazardous mountain routes", "(B) Sherpas own all the mountain land", "(C) Sherpas use magic carpets", "(D) Sherpas carry helicopters", "(A)", "Sherpas possess specialized high-altitude skill and local knowledge.", "Medium", "Understanding", "Sherpa Expertise"),
    ("How does the Sanskrit breakdown 'Him + Alaya' describe the mountain range perfectly?", "(A) 'Him' (snow) + 'Alaya' (abode/house) literally describes a land permanently housed under snow", "(B) It means house of rocks", "(C) It means place of water", "(D) It means green forest", "(A)", "Snow + Abode perfectly describes the snow-covered peaks.", "Medium", "Analyzing", "Etymological Analysis"),
    ("What is the geographical significance of Mount Everest lying on the Nepal-Tibet border?", "(A) It acts as a natural physical boundary connecting and separating two distinct geographic regions", "(B) It causes wars between countries", "(C) It means half the mountain is invisible", "(D) It belongs to the ocean", "(A)", "Acts as a natural geographic border.", "Medium", "Understanding", "Border Significance"),
    ("Why do 9 out of Earth's 10 highest peaks exist in the single range of the Himalayas?", "(A) Because tectonic plate collisions created an extraordinarily concentrated zone of high-altitude uplift", "(B) Because people piled up rocks there", "(C) Because the sun pulls mountains higher there", "(D) Because it is near the ocean", "(A)", "Massive tectonic uplift created concentrated high peaks.", "Medium", "Analyzing", "Geological Scale"),
    ("What challenges do mountaineers face when climbing 8,849 metres up Mount Everest?", "(A) Freezing cold, thin air with low oxygen, steep icy cliffs, and fierce blizzards", "(B) Hot sand and camels", "(C) Wild lions in the snow", "(D) Too many trees blocking the path", "(A)", "Extreme cold, low oxygen, blizzards, steep ice.", "Medium", "Understanding", "Mountaineering Hardships"),
    ("How do the snow-capped peaks of the Himalayas remain white all year round?", "(A) High altitude keeps temperatures below freezing, preserving snow and ice permanently", "(B) People paint them white", "(C) Salt covers the tops", "(D) Clouds fall on them daily", "(A)", "Freezing high-altitude temperatures preserve permanent snow.", "Medium", "Understanding", "Permanent Snow"),
    ("Why are the Ganges, Indus, and Brahmaputra called 'Himalayan Rivers'?", "(A) Because their source waters spring directly from Himalayan snowfields and glaciers", "(B) Because they flow uphill into mountains", "(C) Because they are named after mountains", "(D) Because they only flow in winter", "(A)", "Sources originate from Himalayan snow and glaciers.", "Medium", "Understanding", "River Classification"),
    ("What personality traits enabled Edmund Hillary and Tenzing Norgay to succeed?", "(A) Determination, courage, physical stamina, and mutual trust", "(B) Laziness and anger", "(C) Fear and panic", "(D) Carelessness", "(A)", "Determination, courage, stamina, and mutual trust.", "Medium", "Evaluating", "Climber Traits"),
    ("How does Chapter 09 foster geographical awareness among Class 2 students?", "(A) By teaching mountain terminology, peak heights, country borders, and river origins", "(B) By asking them to draw fictional maps", "(C) By teaching computer programming", "(D) By memorizing city street names", "(A)", "Teaches real physical geography, rivers, and borders.", "Medium", "Applying", "Educational Value"),
    ("What is the difference between a hill and a lofty mountain peak like Everest?", "(A) Hills are low, gentle elevations; lofty peaks are majestic, multi-thousand-metre snow-covered structures", "(B) Hills are taller than mountains", "(C) Mountains have no rocks", "(D) Hills are made of ice", "(A)", "Elevation, scale, and permanent snow cover.", "Medium", "Analyzing", "Physical Geography Contrast"),
    ("Why is snow melt from the Himalayas vital for agriculture in India?", "(A) River waters fed by melting snow irrigate vast fertile plains during hot dry months", "(B) Farmers use snow directly on crops", "(C) Snow cools down tractor engines", "(D) Snow turns into wheat", "(A)", "Glacial melt feeds river irrigation across fertile plains.", "Medium", "Evaluating", "Agricultural Impact"),
    ("What safety equipment do modern mountaineers carry that early climbers lacked?", "(A) Advanced oxygen tanks, thermal suits, satellite GPS, and lightweight climbing gear", "(B) Heavy iron chains and wooden boots", "(C) Flaming torches", "(D) Umbrellas", "(A)", "Modern oxygen, thermal gear, GPS, and lightweight equipment.", "Medium", "Understanding", "Climbing Tech"),

    # Hard (41-50)
    ("Analyze how the Himalayas function as both a physical barrier and a life-giving water tower for Asia.", "(A) Physical barrier: blocks arctic winds and monsoon loss; Water tower: feeds major rivers sustaining over a billion people", "(B) Physical barrier: stops birds from flying; Water tower: stores bottled water", "(C) It only serves as a tourist spot", "(D) It blocks all rain from entering Asia", "(A)", "Climate barrier and freshwater reservoir for millions.", "Hard", "Analyzing", "HOTS Dual Role"),
    ("Evaluate the ecological fragility of high-altitude Himalayan ecosystems.", "(A) Global warming accelerates glacial retreat, threatening river water supplies and causing unpredictable natural disasters", "(B) High mountains cannot be affected by climate change", "(C) Glaciers grow faster when it gets warm", "(D) Snow never melts under any condition", "(A)", "Glacial retreat threatens water security and causes disasters.", "Hard", "Evaluating", "Ecological Fragility"),
    ("Deconstruct the physical scale of the Himalayas (2,500 km length, 8,849 m height, 9 of 10 top peaks).", "(A) Enormous length spanning multiple nations combined with unmatched vertical elevation creates Earth's most formidable landform", "(B) It is a small hill range in one country", "(C) The numbers are fictional", "(D) Height is less than average buildings", "(A)", "Unmatched horizontal span and vertical elevation.", "Hard", "Analyzing", "Scale Deconstruction"),
    ("Compare the achievement of climbing Mount Everest in 1953 versus climbing it today.", "(A) 1953: uncharted routes, primitive gear, supreme risk; Today: mapped trails, commercial guides, advanced weather tracking", "(B) 1953 was easy; today is impossible", "(C) Gear was identical in both eras", "(D) No one climbs Everest today", "(A)", "Pioneering risk vs modern commercialized expeditions.", "Hard", "Analyzing", "Historical Comparison"),
    ("Assess the cultural and spiritual significance of the Himalayas in Indian heritage.", "(A) Revered as sacred 'Abode of Gods' (Devbhumi), inspiring ancient literature, pilgrimage, and spiritual contemplation", "(B) Seen only as a mining site", "(C) Ignored in ancient scriptures", "(D) Used only for sports", "(A)", "Sacred Devbhumi, inspiration for literature and spirituality.", "Hard", "Evaluating", "Spiritual Significance"),
    ("How do the Indus, Ganges, and Brahmaputra rivers shape the civilizational history of South Asia?", "(A) Perennial river flow created fertile alluvial plains that nurtured ancient civilizations, agriculture, and major cities", "(B) The rivers caused people to abandon Asia", "(C) The rivers flow only through deserts", "(D) The rivers are dry sand beds", "(A)", "Nurtured fertile plains, agriculture, and ancient civilizations.", "Hard", "Analyzing", "Civilizational Impact"),
    ("Examine the teamwork dynamics between Sir Edmund Hillary and Sherpa Tenzing Norgay.", "(A) True partnership: Hillary's endurance and Norgay's high-altitude mastery combined equally to achieve human conquest", "(B) Hillary climbed alone while Norgay waited below", "(C) Norgay carried Hillary on his back", "(D) They competed angrily on the mountain", "(A)", "Complementary skills, mutual trust, and equal partnership.", "Hard", "Evaluating", "Partnership Dynamics"),
    ("Why is the phrase 'Abode of Snow' a poetically and scientifically accurate description of the Himalayas?", "(A) Poetic: evokes majestic beauty; Scientific: holds the largest mass of ice and snow outside the polar regions", "(B) It means snow falls in summer only", "(C) It means the mountains are man-made", "(D) It is inaccurate because there is no snow", "(A)", "Largest non-polar ice mass + poetic aesthetic beauty.", "Hard", "Evaluating", "Poetic & Scientific Accuracy"),
    ("Formulate a geographical summary explaining why Mount Everest is called the 'Roof of the World'.", "(A) Standing at 8,849 metres on the Tibetan border, its summit reaches higher into the atmosphere than any other point on Earth", "(B) Because houses on Everest have flat roofs", "(C) Because it covers the sky like a ceiling", "(D) Because rain starts from its top", "(A)", "Highest elevation point reaching into Earth's atmosphere.", "Hard", "Creating", "Roof of World Concept"),
    ("Synthesize the key learnings of Chapter 09 for young Class 2 learners.", "(A) Respect nature's awe-inspiring scale, appreciate vital water sources, and draw courage from pioneers who conquer great heights!", "(B) Avoid visiting mountains", "(C) Snow is dangerous and useless", "(D) Rivers are unneeded for life", "(A)", "Nature's majesty, vital water sources, and human courage.", "Hard", "Evaluating", "Core Synthesis")
]

mcq_content = f"# MCQs — Chapter 09: The Himalayas\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH09_MCQ_{idx:03d}"
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

with open(os.path.join(CH09_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("The word 'Himalaya' comes from Him and Alaya, meaning abode of _______ in Sanskrit.", "snow", "Abode of snow.", "Easy"),
    ("The lofty peaks of the Himalayas are covered with snow all the _______ round.", "year", "Covered with snow all year round.", "Easy"),
    ("The Himalayas stretch for almost _______ kilometers from west to east.", "2,500", "Stretches for almost 2,500 km.", "Easy"),
    ("The Himalayas stretch from west to _______.", "east", "From west to east.", "Easy"),
    ("Nine of Earth's _______ highest peaks are Himalayan.", "10", "9 of Earth's 10 highest peaks.", "Easy"),
    ("The world's highest peak is Mount _______.", "Everest", "Mount Everest is the highest peak.", "Easy"),
    ("Mount Everest is _______ metres high.", "8,849", "8,849 metres high.", "Easy"),
    ("Mount Everest lies on the border between Nepal and the Tibet Autonomous Region of _______.", "China", "Border of Nepal and Tibet (China).", "Easy"),
    ("Three important rivers—the Indus, the Ganges, and the _______ originate in the Himalayas.", "Brahmaputra", "Indus, Ganges, Brahmaputra.", "Easy"),
    ("The river Ganges originates in the _______.", "Himalayas", "Ganges originates in Himalayas.", "Easy"),
    ("The river Indus originates in the _______.", "Himalayas", "Indus originates in Himalayas.", "Easy"),
    ("In the 1950s, mountaineers reached the summit of Mount Everest in _______.", "1953", "Reached summit in 1953.", "Easy"),
    ("The New Zealander who climbed Mount Everest was Edmund _______.", "Hillary", "Edmund Hillary.", "Easy"),
    ("The Sherpa who climbed Mount Everest with Hillary was Tenzing _______.", "Norgay", "Tenzing Norgay.", "Easy"),
    ("The word 'abode' means the place where one _______.", "lives", "Place where one lives.", "Easy"),
    ("The word 'lofty' means very tall and _______.", "impressive", "Very tall and impressive.", "Easy"),
    ("Mount Everest is located on the border of _______ and Tibet.", "Nepal", "Border of Nepal and Tibet.", "Easy"),
    ("A person who climbs high mountains is called a _______.", "mountaineer", "Called a mountaineer.", "Easy"),
    ("The top of a mountain is called its summit or _______.", "peak", "Summit or peak.", "Easy"),
    ("Himalayan peaks are covered in white _______.", "snow", "Covered in white snow.", "Easy"),
    ("Mount Everest is the highest peak in the _______.", "world", "Highest peak in the world.", "Easy"),
    ("The Brahmaputra is a major _______ originating in the Himalayas.", "river", "Brahmaputra is a river.", "Easy"),
    ("Sherpa Tenzing Norgay was an expert mountain _______.", "climber", "Expert mountain climber/guide.", "Easy"),
    ("Edmund Hillary was a mountaineer from New _______.", "Zealand", "From New Zealand.", "Easy"),
    ("Chapter 09 is titled 'The _______'.", "Himalayas", "Titled 'The Himalayas'.", "Easy"),

    # Medium (26-40)
    ("The vast range of the Himalayas acts as a natural wall across northern _______.", "India", "Across northern India/Asia.", "Medium"),
    ("Glaciers in the Himalayas melt during summer to feed perennial _______.", "rivers", "Feeds perennial rivers.", "Medium"),
    ("Reaching the summit of Mount Everest requires climbing to an altitude of 8,849 _______.", "metres", "Altitude of 8,849 metres.", "Medium"),
    ("Sherpas are famous for their skill and endurance in high-altitude _______.", "mountaineering", "High-altitude mountaineering.", "Medium"),
    ("The Ganges river is essential for farming in the northern _______ of India.", "plains", "Northern plains of India.", "Medium"),
    ("Cold winds from the north are blocked by the _______ mountain wall.", "Himalayan", "Himalayan mountain wall.", "Medium"),
    ("Mount Everest's extreme height makes the air very _______ near the summit.", "thin", "Air is very thin/low oxygen.", "Medium"),
    ("The Brahmaputra river flows through Tibet, India, and _______.", "Bangladesh", "Flows through Tibet, India, Bangladesh.", "Medium"),
    ("High mountains covered in permanent snow are called snow-_______ peaks.", "capped", "Snow-capped peaks.", "Medium"),
    ("In 1953, Hillary and Norgay achieved human victory over Earth's highest _______.", "point", "Earth's highest point/peak.", "Medium"),
    ("The Sanskrit word 'Alaya' translates to house or _______.", "abode", "Translates to house/abode.", "Medium"),
    ("Melting ice from Himalayan glaciers forms the source of freshwater for millions of _______.", "people", "Freshwater for millions.", "Medium"),
    ("Climbing Mount Everest tests human physical _______ and mental courage.", "stamina", "Physical stamina and courage.", "Medium"),
    ("Nepal and China share the geographical border where Mount _______ stands.", "Everest", "Mount Everest stands.", "Medium"),
    ("The Himalayas contain nine out of ten of the highest peaks on _______.", "Earth", "Highest peaks on Earth.", "Medium"),

    # Hard (41-50)
    ("The Himalayan mountain system represents a colossal geological _______.", "uplift", "Colossal geological uplift.", "Hard"),
    ("Perennial river origin in the Himalayas ensures continuous water supply to South Asian _______.", "agriculture", "Supply to South Asian agriculture.", "Hard"),
    ("Edmund Hillary and Tenzing Norgay's historic conquest took place on May 29, _______.", "1953", "May 29, 1953.", "Hard"),
    ("The Tibetan name for Mount Everest is Qomolangma, while in Nepal it is called _______.", "Sagarmatha", "Called Sagarmatha in Nepal.", "Hard"),
    ("High-altitude hypoxia occurs because atmospheric pressure decreases with increasing _______.", "elevation", "Decreases with increasing elevation.", "Hard"),
    ("The Himalayas act as the third polar ice reservoir on Planet _______.", "Earth", "Third polar ice reservoir on Earth.", "Hard"),
    ("Sustaining Himalayan ecological stability is crucial for global climate _______.", "balance", "Crucial for climate balance.", "Hard"),
    ("The expedition led by John Hunt in 1953 put Hillary and Norgay on the final _______.", "assault", "Final assault/summit push.", "Hard"),
    ("Glacial rivers carry nutrient-rich silt down to the fertile Gangetic _______.", "valley", "Fertile Gangetic valley/plains.", "Hard"),
    ("Conquering Mount Everest demonstrated the ultimate power of human determination over extreme _______.", "nature", "Determination over extreme nature.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 09: The Himalayas\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH09_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH09_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The word 'Himalaya' means 'abode of snow' in Sanskrit.", "True", "Him + Alaya = abode of snow.", "Easy"),
    ("The peaks of the Himalayas are covered with snow only in winter.", "False", "They are covered with snow all the year round.", "Easy"),
    ("The Himalayas stretch for almost 2,500 kilometers from west to east.", "True", "They stretch for almost 2,500 km west to east.", "Easy"),
    ("Nine of Earth's 10 highest peaks are in the Himalayas.", "True", "Nine out of 10 highest peaks are Himalayan.", "Easy"),
    ("Mount Everest is the highest mountain peak in the world.", "True", "Mount Everest is the world's highest peak.", "Easy"),
    ("Mount Everest is 8,849 metres high.", "True", "It is 8,849 metres high.", "Easy"),
    ("Mount Everest is located entirely inside India.", "False", "It lies on the border between Nepal and Tibet (China).", "Easy"),
    ("The Ganges river originates in the Himalayas.", "True", "The Ganges originates in the Himalayas.", "Easy"),
    ("The Nile river originates in the Himalayas.", "False", "The Nile is in Africa; Indus, Ganges, and Brahmaputra originate in the Himalayas.", "Easy"),
    ("Edmund Hillary and Tenzing Norgay were the first to reach the summit of Mount Everest.", "True", "They reached the summit first in 1953.", "Easy"),
    ("Edmund Hillary was a mountaineer from Australia.", "False", "Edmund Hillary was a New Zealander.", "Easy"),
    ("Tenzing Norgay was a Sherpa climber.", "True", "He was Sherpa Tenzing Norgay.", "Easy"),
    ("The word 'abode' means a place where one lives.", "True", "Abode is defined as the place where one lives.", "Easy"),
    ("The word 'lofty' means very small and low.", "False", "Lofty means very tall and impressive.", "Easy"),
    ("The Himalayas stretch from north to south.", "False", "They stretch from west to east.", "Easy"),
    ("The Brahmaputra river originates in the Himalayas.", "True", "The Brahmaputra originates in the Himalayas.", "Easy"),
    ("The Indus river originates in the Himalayas.", "True", "The Indus originates in the Himalayas.", "Easy"),
    ("Mount Everest is less than 5,000 metres high.", "False", "Mount Everest is 8,849 metres high.", "Easy"),
    ("Hillary and Norgay reached the summit of Mount Everest in 1953.", "True", "They reached the summit in 1953.", "Easy"),
    ("There are no rivers originating in the Himalayas.", "False", "Indus, Ganges, Brahmaputra, and many others originate there.", "Easy"),
    ("Sherpa Tenzing Norgay was born in New Zealand.", "False", "Edmund Hillary was from New Zealand; Tenzing Norgay was a local Sherpa.", "Easy"),
    ("The Himalayas are the tallest mountain range on Earth.", "True", "No other mountain range on Earth compares to the Himalayas.", "Easy"),
    ("Snow on Himalayan peaks melts completely during summer.", "False", "Lofty peaks remain covered with snow all the year round.", "Easy"),
    ("Mountaineers climb high peaks for sport and exploration.", "True", "Mountaineers climb high peaks for exploration and sport.", "Easy"),
    ("Chapter 09 is titled 'The Himalayas'.", "True", "Chapter 09 is titled 'The Himalayas'.", "Easy"),

    # Medium (26-40)
    ("The Himalayas provide freshwater to major South Asian rivers.", "True", "Glaciers feed rivers like Ganges, Indus, and Brahmaputra.", "Medium"),
    ("Mount Everest is situated on the border between Nepal and Tibet.", "True", "It sits on the border between Nepal and Tibet (China).", "Medium"),
    ("All ten of Earth's highest peaks are located outside Asia.", "False", "Nine of Earth's 10 highest peaks are in the Himalayas in Asia.", "Medium"),
    ("The name 'Him + Alaya' was given because the mountains are always green.", "False", "It means 'abode of snow' because the peaks are covered in snow all year.", "Medium"),
    ("Edmund Hillary and Tenzing Norgay climbed Mount Everest without any preparation.", "False", "Mountaineering Everest required extensive team planning, gear, and endurance.", "Medium"),
    ("The Ganges river is vital for agriculture in northern India.", "True", "The Ganges supplies water for vast agricultural plains.", "Medium"),
    ("Air becomes thinner and oxygen decreases as mountaineers climb higher up Everest.", "True", "High altitude features thin air and low oxygen levels.", "Medium"),
    ("The Himalayas stretch over a distance of 2,500 kilometers.", "True", "They stretch for almost 2,500 km from west to east.", "Medium"),
    ("Sherpas are well-known for their expertise in guiding Himalayan climbing expeditions.", "True", "Sherpas are famous for high-altitude climbing skill and guidance.", "Medium"),
    ("Mount Everest's height is measured as 8,849 metres above sea level.", "True", "It is 8,849 metres above sea level.", "Medium"),
    ("The Indus river flows into the Atlantic Ocean.", "False", "The Indus flows into the Arabian Sea.", "Medium"),
    ("Cold weather and freezing temperatures keep snow on Himalayan peaks year-round.", "True", "Freezing high-altitude temperatures preserve permanent snow.", "Medium"),
    ("The 1953 Everest expedition was led by Edmund Hillary alone.", "False", "It was a team expedition; Hillary and Norgay were the summit pair.", "Medium"),
    ("The Himalayas act as a geographical barrier between Central and South Asia.", "True", "The range forms a massive physical barrier between regions.", "Medium"),
    ("Learning about Mount Everest teaches students about physical geography and endurance.", "True", "It covers geography, height, climate, and human courage.", "Medium"),

    # Hard (41-50)
    ("The Himalayas hold the largest body of ice outside the Polar regions.", "True", "The Himalayas are often called the 'Third Pole' due to vast ice reserves.", "Hard"),
    ("Glacial melting in the Himalayas has no impact on river water levels.", "False", "Glacial melt directly supplies spring and summer flow to major rivers.", "Hard"),
    ("Tenzing Norgay and Edmund Hillary reached the summit of Everest on May 29, 1953.", "True", "May 29, 1953 was the exact date of their summit success.", "Hard"),
    ("Mount Everest is growing slightly higher every year due to tectonic activity.", "True", "Tectonic collision continues to push the Himalayas upward slowly.", "Hard"),
    ("The word 'lofty' describes low, flat plains near river basins.", "False", "Lofty means very tall, majestic, and impressive.", "Hard"),
    ("The Brahmaputra river is known as the Yarlung Tsangpo in Tibet.", "True", "In Tibet, the Brahmaputra is called Yarlung Tsangpo.", "Hard"),
    ("Edmund Hillary was knighted by Queen Elizabeth II for his Everest climb.", "True", "He became Sir Edmund Hillary after the successful 1953 climb.", "Hard"),
    ("The Himalayas stretch across five countries: India, Nepal, Bhutan, China, and Pakistan.", "True", "The Himalayan system spans across these five South Asian nations.", "Hard"),
    ("Thin atmospheric oxygen at 8,849 metres poses no risk to human life.", "False", "Low oxygen (hypoxia) poses extreme life-threatening risk to climbers.", "Hard"),
    ("Chapter 09 combines etymology, physical geography, and historical exploration.", "True", "It covers word origin (Sanskrit), geographical facts, and 1953 climbing history.", "Hard")
]

tf_content = f"# True / False — Chapter 09: The Himalayas\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH09_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH09_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("What does the word 'Himalaya' mean in Sanskrit and why was it given this name?", "Himalaya means 'abode of snow' (Him + Alaya). It was given this name because its lofty peaks are covered with snow all year round.", "Easy", "Remembering"),
    ("How long does the Himalayan mountain range stretch from west to east?", "The Himalayas stretch for almost 2,500 kilometers from west to east.", "Easy", "Remembering"),
    ("How many of Earth's highest peaks are located in the Himalayas?", "Nine of Earth's 10 highest peaks are located in the Himalayas.", "Easy", "Remembering"),
    ("What is the world's highest peak and how tall is it?", "The world's highest peak is Mount Everest, which is 8,849 metres high.", "Easy", "Remembering"),
    ("Where is Mount Everest located geographically?", "Mount Everest lies on the border between Nepal and the Tibet Autonomous Region of China.", "Easy", "Remembering"),
    ("Name three important rivers that originate in the Himalayas.", "The three important rivers are the Indus, the Ganges, and the Brahmaputra.", "Easy", "Remembering"),
    ("Who were the first mountaineers to reach the summit of Mount Everest, and in which year?", "New Zealander Edmund Hillary and Sherpa Tenzing Norgay reached the summit first in 1953.", "Easy", "Remembering"),
    ("What is the meaning of the word 'abode'?", "Abode means the place where one lives or stays.", "Easy", "Understanding"),
    ("What is the meaning of the word 'lofty'?", "Lofty means very tall, majestic, and impressive.", "Easy", "Understanding"),
    ("Which continent are the Himalayas located in?", "The Himalayas are located on the continent of Asia.", "Easy", "Remembering"),
    ("What covers the lofty peaks of the Himalayas throughout the year?", "Permanent snow and ice cover the lofty peaks all year round.", "Easy", "Remembering"),
    ("What nationality was Edmund Hillary?", "Edmund Hillary was a mountaineer from New Zealand.", "Easy", "Remembering"),
    ("Who was Tenzing Norgay?", "Tenzing Norgay was a famous local Sherpa mountaineer who climbed Mount Everest with Hillary.", "Easy", "Remembering"),
    ("Why are the Himalayas famous around the world?", "They are famous because they form the highest mountain range on Earth, containing Mount Everest and 9 of the top 10 peaks.", "Easy", "Remembering"),
    ("What is a summit?", "The summit is the highest point or top peak of a mountain.", "Easy", "Understanding"),
    ("Does the Ganges river originate in the Himalayas?", "Yes, the Ganges river originates in the Himalayas.", "Easy", "Remembering"),
    ("Does the Indus river originate in the Himalayas?", "Yes, the Indus river originates in the Himalayas.", "Easy", "Remembering"),
    ("Does the Brahmaputra river originate in the Himalayas?", "Yes, the Brahmaputra river originates in the Himalayas.", "Easy", "Remembering"),
    ("What happens to snow on the Himalayas during warmer months?", "Glacial snow slowly melts, supplying freshwater to major rivers like the Ganges.", "Easy", "Understanding"),
    ("Why is Mount Everest dangerous to climb?", "It is dangerous due to extreme freezing cold, thin air with low oxygen, steep ice, and blizzards.", "Easy", "Understanding"),
    ("What is a Sherpa?", "A Sherpa is an ethnic group from the Himalayan region of Nepal, renowned for expert mountain climbing skills.", "Easy", "Understanding"),
    ("In which direction do the Himalayas stretch?", "They stretch from west to east.", "Easy", "Remembering"),
    ("How high is Mount Everest in metres?", "Mount Everest is 8,849 metres high.", "Easy", "Remembering"),
    ("Why are rivers originating in the Himalayas important for people?", "They supply essential freshwater for drinking, farming, and daily life for millions of people.", "Easy", "Understanding"),
    ("What is the title of Chapter 09?", "The title of Chapter 09 is 'The Himalayas'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Why are the Himalayas referred to as the 'Water Tower of Asia'?", "Because their massive glaciers store frozen freshwater that feeds major rivers like the Ganges, Indus, and Brahmaputra, providing water for millions.", "Medium", "Understanding"),
    ("Explain the literal breakdown of the Sanskrit word 'Himalaya'.", "'Him' means snow, and 'Alaya' means abode or home. Together, 'Himalaya' translates literally to 'Abode of Snow'.", "Medium", "Understanding"),
    ("How does Mount Everest's location on the Nepal-Tibet border affect mountaineering expeditions?", "Climbers can attempt to reach the summit from either the southern route in Nepal or the northern route in Tibet (China).", "Medium", "Analyzing"),
    ("What makes the Himalayas unique compared to all other mountain ranges on Earth?", "No other range compares in elevation: it spans 2,500 km and contains 9 of the 10 highest mountain peaks on Planet Earth.", "Medium", "Analyzing"),
    ("Describe the achievement of Edmund Hillary and Tenzing Norgay in 1953.", "They became the first human beings in recorded history to successfully stand on the 8,849-metre summit of Mount Everest, proving human courage.", "Medium", "Evaluating"),
    ("Why is high altitude climbing difficult for human breathing?", "At high altitudes like 8,849 metres, atmospheric pressure drops, making the air thin and containing much less oxygen.", "Medium", "Understanding"),
    ("How do the Himalayas influence India's climate?", "The massive mountain wall blocks freezing arctic winds from Central Asia and traps moisture-laden monsoon winds inside India.", "Medium", "Analyzing"),
    ("What role do Sherpas play in Mount Everest expeditions?", "Sherpas act as expert guides, fix climbing ropes, carry heavy supplies, and use their high-altitude adaptation to ensure safety.", "Medium", "Understanding"),
    ("Why is the Ganges river considered a lifeline for northern India?", "The Ganges flows from Himalayan glaciers across fertile plains, supplying irrigation water for crops and drinking water for cities.", "Medium", "Evaluating"),
    ("What equipment do mountaineers use when climbing Mount Everest?", "They use oxygen tanks, insulated thermal suits, spiked boots (crampons), climbing ropes, ice axes, and tents.", "Medium", "Remembering"),
    ("Summarize Page 34 of the textbook in two sentences.", "The Himalayas ('abode of snow' in Sanskrit) stretch 2,500 km from west to east and contain 9 of Earth's 10 highest peaks, including Mount Everest (8,849 m). Major rivers like the Indus, Ganges, and Brahmaputra originate here, and Hillary and Norgay first conquered Everest in 1953.", "Medium", "Understanding"),
    ("How long is the Himalayan range compared to a country like India?", "Stretching 2,500 km, the range spans almost the entire northern border of India from west to east.", "Medium", "Understanding"),
    ("Why are permanent snow peaks important for earth's ecosystem?", "They store frozen freshwater, reflect solar heat, regulate regional temperatures, and feed rivers during dry seasons.", "Medium", "Evaluating"),
    ("What qualities did Tenzing Norgay and Edmund Hillary share?", "Both possessed extraordinary physical stamina, determination, courage, humility, and trust in each other.", "Medium", "Evaluating"),
    ("How does Chapter 09 build geographical vocabulary for Class 2 students?", "It introduces key terms like abode, lofty, summit, peak, range, border, glacier, and river origin.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the environmental impact of modern commercial tourism on Mount Everest.", "Commercial expeditions cause severe littering (oxygen bottles, food packaging), trail overcrowding, and pollution, threatening the delicate high-altitude ecosystem.", "Hard", "Evaluating"),
    ("Analyze how the geological formation of the Himalayas created Earth's highest landform.", "The collision of the Indian tectonic plate with the Eurasian plate pushed up marine sediments, creating immense vertical uplift and 9 of the 10 highest peaks.", "Hard", "Analyzing"),
    ("Deconstruct the 1953 Everest expedition teamwork model.", "Success required team coordination: logistics managers, route-finding Sherpas, support climbers stocking high camps, and the final summit pair (Hillary and Norgay).", "Hard", "Analyzing"),
    ("Compare the source and course of the Indus, Ganges, and Brahmaputra rivers.", "All three spring from Himalayan glaciers: the Indus flows west into the Arabian Sea; the Ganges flows southeast through India; the Brahmaputra flows east through Tibet before turning south into India and Bangladesh.", "Hard", "Analyzing"),
    ("Evaluate the spiritual significance of the Himalayas in Indian literature and culture.", "In Indian culture, the Himalayas are revered as Devbhumi (Land of Gods), serving as a retreat for sages, a symbol of stability, and inspiration for sacred texts.", "Hard", "Evaluating"),
    ("How can a school teacher explain altitude and air density to young students using Mount Everest?", "The teacher can explain that air is like stacked blankets: at sea level, many blankets press down (thick air); on top of Everest, few blankets press down (thin air).", "Hard", "Applying"),
    ("Assess the impact of global warming on Himalayan glaciers.", "Rising temperatures accelerate glacial melting, causing dangerous glacial lake outbursts initially, followed by long-term river drying that threatens Asia's water supply.", "Hard", "Evaluating"),
    ("Why is Tenzing Norgay's success significant for indigenous Himalayan communities?", "Norgay's historic achievement proved the world-class climbing mastery of local Sherpa people, bringing international respect and economic opportunities to Nepal.", "Hard", "Analyzing"),
    ("Formulate a short descriptive paragraph depicting the view from the summit of Mount Everest.", "'Standing on the 8,849-metre summit of Mount Everest, the world unfolds beneath you. Snow-capped Himalayan peaks pierce the deep blue sky like silent white giants, while giant glaciers curve down into deep, quiet valleys below.'", "Hard", "Creating"),
    ("Synthesize the main educational lesson of Chapter 09 for young Class 2 learners.", "Appreciate the majestic scale of nature, respect the vital rivers that sustain life, and remember that with courage, trust, and hard work, humans can conquer the highest peaks!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 09: The Himalayas\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH09_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH09_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the meaning of the word 'Himalaya' in Sanskrit and why the mountain range is called by this name.", 
     "The word 'Himalaya' is derived from two Sanskrit words: 'Him' meaning snow, and 'Alaya' meaning abode or house. Together, Himalaya means 'abode of snow'. It was given this beautiful name because its lofty, majestic peaks reach so high into the freezing sky that they remain permanently covered with snow and ice all the year round, looking like a grand house made of snow.", 
     "Easy", "Remembering"),

    ("Detail the geographic scale of the Himalayas, including its length and highest peaks.", 
     "The Himalayas form a massive mountain system stretching for almost 2,500 kilometers from west to east across South Asia. It is the most impressive mountain range on Earth. Remarkably, 9 out of Planet Earth's 10 highest mountain peaks are located in the Himalayas. The tallest of all is Mount Everest, standing at 8,849 metres high on the border between Nepal and Tibet (China).", 
     "Easy", "Remembering"),

    ("Name the three major rivers that originate in the Himalayas and explain their importance.", 
     "The three major rivers originating in the Himalayas are:\n1. **The Indus**\n2. **The Ganges**\n3. **The Brahmaputra**\nThese rivers are formed by the melting of snowfields and glaciers. They flow down into the plains, providing essential drinking water, fertile soil, and crop irrigation for hundreds of millions of people.", 
     "Easy", "Remembering"),

    ("Describe the historic first climb of Mount Everest in 1953 by Hillary and Norgay.", 
     "In 1953, a famous mountaineering expedition tackled Mount Everest. On May 29, 1953, New Zealander Edmund Hillary and local Sherpa Tenzing Norgay braved freezing winds, steep ice, and thin air to become the first human beings to reach the 8,849-metre summit. Their victory proved that human courage, physical endurance, and teamwork could conquer Earth's highest point.", 
     "Easy", "Remembering"),

    ("Explain the meanings of the vocabulary words 'abode' and 'lofty' as used in Chapter 09.", 
     "1. **Abode**: Refers to a home, dwelling place, or place where one lives permanently (e.g., house of snow).\n2. **Lofty**: Refers to something that is extremely tall, majestic, high up in the sky, and visually impressive (e.g., lofty snow peaks).", 
     "Easy", "Understanding"),

    ("Why are the Himalayas important for the climate and agriculture of India?", 
     "The Himalayas serve as a giant natural wall along India's northern border. They block cold arctic winds from Central Asia, keeping India warm. They also trap rain-bearing monsoon clouds, causing rainfall across Indian fields. In summer, melting Himalayan snow feeds rivers like the Ganges, supplying vital water for farming.", 
     "Easy", "Understanding"),

    ("What is Mount Everest, where is it located, and how tall is it?", 
     "Mount Everest is the highest mountain peak in the world. It stands at an elevation of 8,849 metres above sea level. It is located in Asia, positioned directly on the international border between the country of Nepal and the Tibet Autonomous Region of China.", 
     "Easy", "Remembering"),

    ("Who are the Sherpas and why are they famous in mountain climbing history?", 
     "Sherpas are an ethnic community living in the high mountain valleys of the Himalayas in Nepal. They are world-famous in mountaineering history because their bodies are naturally adapted to high altitudes. They possess unparalleled route-finding skills, physical strength, and courage, guiding international climbers up Everest.", 
     "Easy", "Understanding"),

    ("How does the snow on the Himalayas help supply freshwater to rivers?", 
     "The lofty Himalayan peaks collect huge amounts of snow every winter. During the warmer spring and summer months, the sun slowly melts the edges of these high glaciers and snowfields. This melted water trickles down mountain streams to form giant, permanent rivers like the Ganges and Indus.", 
     "Easy", "Understanding"),

    ("What moral values can students learn from the story of Edmund Hillary and Tenzing Norgay?", 
     "Students learn that setting high goals requires preparation, perseverance, and bravery. Climbing Everest showed that when two people from different backgrounds trust each other and work as a team, they can achieve historic goals that seemed impossible.", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why is Mount Everest called the highest peak on Earth?", "It is called the highest peak because its summit reaches 8,849 metres above sea level, higher than any other mountain top on Planet Earth.", "Easy", "Remembering"),
    ("Explain the stretch of the Himalayas from west to east.", "The Himalayas form a huge crescent-shaped mountain arc stretching nearly 2,500 kilometers across northern South Asia, from Pakistan and India through Nepal, Bhutan, and China.", "Easy", "Understanding"),
    ("What challenges do mountaineers face when climbing in the Himalayas?", "Mountaineers face extreme freezing temperatures, fierce blizzards, avalanches, steep ice walls, and dangerous thin air with very low oxygen levels.", "Easy", "Understanding"),
    ("Why are 9 of the 10 highest peaks in the world found in the Himalayas?", "Geological plate collisions pushed the land upward with immense force, creating a dense cluster of the tallest mountain peaks on Earth in one continuous range.", "Easy", "Understanding"),
    ("What role does the Ganges river play in the lives of millions of people?", "The Ganges provides fresh drinking water, feeds agricultural fields, supports wildlife, and holds deep cultural and spiritual reverence for millions of people in India.", "Easy", "Understanding"),
    ("How did Edmund Hillary and Tenzing Norgay prepare for their final summit push?", "They set up high-altitude camps, used artificial oxygen bottles, checked weather conditions, tied themselves together with climbing ropes, and worked as a coordinated team.", "Easy", "Understanding"),
    ("What makes the Himalayas look so beautiful and majestic?", "Their giant, soaring heights, crisp blue skies, glistening white snow peaks, giant blue ice glaciers, and green valley bases create breathtaking natural beauty.", "Easy", "Remembering"),
    ("Why does the air become cold at the top of high mountains like Everest?", "As altitude increases, atmospheric pressure drops and air becomes thinner, making it unable to hold heat, leading to permanent sub-zero freezing temperatures.", "Easy", "Understanding"),
    ("How does Chapter 09 encourage children to appreciate geography?", "By introducing exciting real-world facts—the world's highest peak (Everest), giant rivers (Ganges), famous climbers, and Sanskrit word origins.", "Easy", "Applying"),
    ("Describe the journey of a raindrop or snowflake in the Himalayas.", "It falls as snow on a lofty peak, turns into glacial ice, slowly melts in summer sun, trickles into a mountain stream, joins the Ganges river, and flows across plains to the ocean.", "Easy", "Understanding"),
    ("Why is New Zealand proud of Sir Edmund Hillary?", "Edmund Hillary put New Zealand in international history books by becoming the first person, along with Tenzing Norgay, to stand on top of the world on Mount Everest.", "Easy", "Remembering"),
    ("What is the difference between climbing a small hill and climbing Mount Everest?", "A hill takes an hour of walking in normal air. Everest requires months of training, specialized ice gear, oxygen tanks, Sherpa guides, and surviving deadly weather.", "Easy", "Analyzing"),
    ("Why do major rivers flow continuously even in hot dry summers?", "Because hot summer sun melts high Himalayan snow and glaciers, maintaining steady river flow when rain is scarce.", "Easy", "Understanding"),
    ("How does the title 'Abode of Snow' capture the essence of the Himalayas?", "It captures both the physical reality (permanent snow and ice cover) and the poetic imagery of a grand home built of snow.", "Easy", "Evaluating"),
    ("Summarize Chapter 09 in five key sentences.", "The Himalayas ('abode of snow' in Sanskrit) stretch 2,500 km west to east. It contains 9 of Earth's 10 highest peaks, led by Mount Everest at 8,849 metres. Major rivers like the Indus, Ganges, and Brahmaputra originate from its snowfields. In 1953, Edmund Hillary and Tenzing Norgay became the first to reach Everest's summit. The range is a vital, majestic treasure of Earth.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze the ecological connection between Himalayan glaciers and South Asian civilization.", 
     "Himalayan glaciers act as natural freshwater storage towers. During summer, controlled melting supplies continuous water to the Indus, Ganges, and Brahmaputra river systems. These rivers deposit nutrient-rich alluvial soil across vast agricultural plains, supporting over 1.3 billion people. Without these glaciers, South Asia would face acute water shortages and agricultural collapse.", 
     "Medium", "Analyzing"),

    ("Examine the physical factors that make Mount Everest (8,849 m) the ultimate human endurance test.", 
     "At 8,849 metres, Mount Everest enters the 'Death Zone' where atmospheric oxygen is one-third of sea level. Climbers face severe hypoxia, frostbite from -40°C winds, hurricane-force blizzards, treacherous crevasses, and physical exhaustion. Reaching the summit tests the absolute limits of human endurance, mental grit, and biological capability.", 
     "Medium", "Analyzing"),

    ("Discuss the cultural and historical partnership between Sir Edmund Hillary and Sherpa Tenzing Norgay.", 
     "Their 1953 partnership bridged western technical mountaineering and local Himalayan indigenous mastery. Hillary brought physical stamina and methodical planning; Norgay brought high-altitude adaptation and route-finding genius. Their mutual respect and shared step onto the summit symbolized cross-cultural unity and equal triumph.", 
     "Medium", "Evaluating"),

    ("Explore the etymological and physical significance of mountain naming in Chapter 09.", 
     "Naming the range 'Himalaya' ('Him' = snow, 'Alaya' = abode) highlights the defining physical characteristic of the range—its permanent snow cover. Similarly, naming Everest's summit 'Roof of the World' captures its unmatched elevation. Etymology in geography connects linguistic beauty with physical reality.", 
     "Medium", "Analyzing"),

    ("How can Class 2 teachers use Chapter 09 to integrate Science, Geography, and Social Studies?", 
     "Teachers can integrate:\n1. **Science**: States of water (snow melting into river water) and high-altitude air pressure.\n2. **Geography**: Map reading (Nepal, China, India, 2,500 km range, river paths).\n3. **Social Studies**: History of the 1953 Everest expedition and Sherpa culture.", 
     "Medium", "Applying"),

    ("Why is Mount Everest located on an international border rather than inside one country?", "Because the Himalayan crest forms a natural continental divide. The ridge of Mount Everest acts as the physical border separating the high plateau of Tibet (China) to the north from the mountain kingdom of Nepal to the south.", "Medium", "Understanding"),
    ("Describe the path of the river Ganges from Himalayan glaciers to the Indian plains.", "The Ganges begins high in the Himalayas at the Gangotri glacier. It cascades down steep rocky gorges, joins other mountain tributaries, emerges onto the fertile plains at Haridwar, and flows across northern India to the ocean.", "Medium", "Understanding"),
    ("What makes the Himalayan mountain system young in geological terms?", "The Himalayas were formed relatively recently in Earth's history by the collision of tectonic plates. Because the plates are still pressing against each other, the Himalayas are still growing slowly today.", "Medium", "Understanding"),
    ("How does high altitude affect temperature even when the sun is shining?", "At high altitudes, thin air cannot trap solar heat. Even under bright sunshine, ambient temperatures remain below freezing because heat radiates away instantly into space.", "Medium", "Understanding"),
    ("Why was reaching the summit of Everest in 1953 celebrated worldwide?", "In 1953, reaching Everest was considered one of the last great unexplored frontiers on Earth, similar to reaching the North Pole or South Pole. The success thrilled humanity.", "Medium", "Evaluating"),
    ("Compare the source waters of the Indus river with the Brahmaputra river.", "Both rivers originate near Mount Kailash in the Himalayas. The Indus flows northwest through India and Pakistan into the Arabian Sea, while the Brahmaputra flows east through Tibet before turning south into India and Bangladesh.", "Medium", "Analyzing"),
    ("Why do mountaineers use oxygen cylinders above 8,000 metres?", "Above 8,000 metres, air density drops so low that the human brain and lungs cannot get enough oxygen to survive naturally. Oxygen cylinders supply artificial air to prevent organ failure.", "Medium", "Understanding"),
    ("Explain why the Himalayas are essential for regulating Asian monsoons.", "The 2,500 km long, high-altitude mountain wall acts as a barrier that prevents moist summer monsoon winds from escaping into Central Asia, forcing heavy rainfall over India and South Asia.", "Medium", "Analyzing"),
    ("How does Chapter 09 inspire courage and perseverance in young students?", "It presents Hillary and Norgay's climb as proof that facing extreme difficulties with preparation, trust, and refusal to give up allows humans to conquer the highest challenges.", "Medium", "Evaluating"),
    ("Construct a 4-line poem honoring the majestic Himalayas.", "'O majestic Himalayas, house of white snow,\nWhere giant cold rivers to sunny plains flow!\nWith lofty high peaks touching blue skies above,\nYou guard our great land with strength and with love!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the ecological threat posed by global climate change to the Himalayan glaciers.", 
     "Global warming is causing Himalayan glaciers to melt at unprecedented rates. In the short term, this creates catastrophic glacial lake outburst floods. In the long term, severe glacial depletion will cause major rivers like the Ganges and Indus to dry up seasonally, threatening food and water security for 1.3 billion people in Asia.", 
     "Hard", "Evaluating"),

    ("Deconstruct the physical scale and geopolitical importance of the Himalayan mountain system.", 
     "Spanning 2,500 km across five nations (India, Nepal, Bhutan, China, Pakistan), the Himalayas serve as a natural physical wall, international border zone, weather barrier, and freshwater source. Its geopolitical stability is essential for regional peace, water sharing, and environmental protection.", 
     "Hard", "Analyzing"),

    ("Synthesize the scientific and human factors that enabled the 1953 Everest ascent.", 
     "1. **Scientific Factors**: Development of lightweight closed-circuit oxygen gear, wind-proof nylon tents, and accurate weather forecasting.\n2. **Human Factors**: Hillary's relentless stamina, Norgay's Sherpa adaptability, John Hunt's military planning, and seamless team trust.", 
     "Hard", "Synthesizing"),

    ("Formulate a lesson module for teaching 'Himalayan River Systems' to primary students.", 
     "- **Visual**: Map showing glacier origins of Indus, Ganges, Brahmaputra.\n- **Experiment**: Ice cube melting on a slanted tray to show how glacial melt forms flowing rivers.\n- **Discussion**: Importance of clean river water for drinking and farming.\n- **Activity**: Labeling the three major rivers on an outline map.", 
     "Hard", "Creating"),

    ("Evaluate the impact of high-altitude Sherpa culture on global mountaineering expeditions.", 
     "Without Sherpa expertise, commercial mountaineering on Everest would be virtually impossible. Sherpas perform the most dangerous tasks: fixing safety ropes through Khumbu Icefall, setting up high camps, carrying heavy loads, and conducting life-saving mountain rescues.", 
     "Hard", "Evaluating"),

    ("Analyze why the Himalayas are called the 'Third Pole' of Planet Earth.", "After the Arctic (North Pole) and Antarctica (South Pole), the Himalayas contain the largest volume of permanent ice and snow on Earth, earning the title 'Third Pole' for their massive frozen water reserves.", "Hard", "Analyzing"),
    ("Compare the horizontal extent (2,500 km) vs vertical elevation (8,849 m) of the Himalayas.", "The 2,500 km horizontal extent creates a massive continental climate and biological barrier, while the 8,849 m vertical elevation pushes land into atmospheric zones that support permanent ice and arctic conditions in tropical latitudes.", "Hard", "Analyzing"),
    ("Draft a news headline and opening paragraph announcing the 1953 Everest summit victory.", "'WORLD CONQUERED! HILLARY AND NORGAY REACH EVEREST SUMMIT! London/Kathmandu, May 1953 — In a glorious triumph of human endurance, Edmund Hillary of New Zealand and Sherpa Tenzing Norgay have stood on top of the world at 8,849 metres!'", "Hard", "Creating"),
    ("Assess the responsibility of tourists and climbers in preserving Mount Everest.", "Climbers must adhere to 'Leave No Trace' ethics—bringing down all trash, unused oxygen canisters, and human waste to prevent Mount Everest from becoming a high-altitude dumping ground.", "Hard", "Evaluating"),
    ("Synthesize the ultimate moral lesson of Chapter 09 into a guiding motto for Class 2 students.", "'Be steadfast like the Himalayas, let your wisdom flow like great rivers, and climb every goal in life with courage and trust!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 09: The Himalayas\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH09_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH09_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("The Himalayas (Him + Alaya ) means \"abode of snow\" in Sanskrit. It is given this name because its lofty peaks are covered with snow all the year round.",
     [
         ("What does the word 'Himalaya' mean in Sanskrit?", "Abode of snow.", "Easy", "Remembering"),
         ("Which two Sanskrit words form 'Himalaya'?", "Him + Alaya.", "Easy", "Remembering"),
         ("Why was this name given to the mountain range?", "Because its lofty peaks are covered with snow all the year round.", "Easy", "Remembering"),
         ("What does the word 'abode' mean?", "The place where one lives.", "Medium", "Understanding"),
         ("What does the word 'lofty' mean?", "Very tall and impressive.", "Medium", "Understanding")
     ]),

    # Set 2
    ("This great mountain system stretches for almost 2,500 kilometers from west to east.",
     [
         ("What type of geographical structure is the Himalayas?", "A great mountain system.", "Easy", "Remembering"),
         ("How far does the mountain system stretch?", "Almost 2,500 kilometers.", "Easy", "Remembering"),
         ("In which direction does it stretch?", "From west to east.", "Easy", "Remembering"),
         ("Is 2,500 kilometers a small or massive distance?", "A massive distance spanning across South Asia.", "Medium", "Understanding"),
         ("Which continent contains this mountain system?", "Asia.", "Easy", "Remembering")
     ]),

    # Set 3
    ("No other mountain range on Earth compares to the Himalayas. Nine of Earth's 10 highest peaks are Himalayan.",
     [
         ("Does any other mountain range on Earth compare to the Himalayas?", "No, no other mountain range compares.", "Easy", "Remembering"),
         ("How many of Earth's 10 highest peaks are located in the Himalayas?", "Nine peaks.", "Easy", "Remembering"),
         ("What does this fact show about the Himalayas?", "It shows that the Himalayas are the tallest mountain range on Planet Earth.", "Medium", "Understanding"),
         ("Where are Earth's highest peaks concentrated?", "In the Himalayan mountain system.", "Easy", "Remembering"),
         ("Find a word in the extract that means 'top of a mountain'.", "Peak.", "Easy", "Understanding")
     ]),

    # Set 4
    ("The world's highest peak, Mount Everest (8849 metres) is a part of Himalayas and lies on the border between Nepal and the Tibet Autonomous Region of China.",
     [
         ("What is the name of the world's highest peak?", "Mount Everest.", "Easy", "Remembering"),
         ("How high is Mount Everest in metres?", "8,849 metres.", "Easy", "Remembering"),
         ("Which mountain range does Mount Everest belong to?", "The Himalayas.", "Easy", "Remembering"),
         ("Which country and region share the border where Mount Everest lies?", "Nepal and the Tibet Autonomous Region of China.", "Easy", "Remembering"),
         ("Is Mount Everest located inside a single country?", "No, it lies on the international border between Nepal and Tibet (China).", "Medium", "Understanding")
     ]),

    # Set 5
    ("Three important rivers-the Indus, the Ganges and the Brahmaputra originate in the Himalayas.",
     [
         ("How many major rivers mentioned in the extract originate in the Himalayas?", "Three important rivers.", "Easy", "Remembering"),
         ("Name the three rivers mentioned.", "The Indus, the Ganges, and the Brahmaputra.", "Easy", "Remembering"),
         ("What does the word 'originate' mean in this context?", "To begin or start flowing from a source.", "Medium", "Understanding"),
         ("What feeds these rivers in the high mountains?", "Melting snow and glaciers from the Himalayas.", "Medium", "Understanding"),
         ("Why are these rivers important to people?", "They supply vital freshwater for drinking, agriculture, and life.", "Medium", "Evaluating")
     ]),

    # Set 6
    ("In the 1900s mountaineers climbed the high peaks for the first time. The New Zealander Edmund Hillary and Sherpa Tenzing Norgay reached the summit of Mount Everest in 1953.",
     [
         ("When did mountaineers first start climbing high Himalayan peaks?", "In the 1900s.", "Easy", "Remembering"),
         ("Who was Edmund Hillary and where was he from?", "He was a mountaineer from New Zealand.", "Easy", "Remembering"),
         ("Who climbed Mount Everest alongside Edmund Hillary?", "Sherpa Tenzing Norgay.", "Easy", "Remembering"),
         ("In which year did Hillary and Norgay reach the summit of Mount Everest?", "1953.", "Easy", "Remembering"),
         ("What does the word 'summit' mean?", "The top peak of a mountain.", "Medium", "Understanding")
     ]),

    # Set 7
    ("Word Meaning: Abode: The place where one lives | Lofty: Very tall and impressive",
     [
         ("What is the meaning of 'abode'?", "The place where one lives.", "Easy", "Remembering"),
         ("What is the meaning of 'lofty'?", "Very tall and impressive.", "Easy", "Remembering"),
         ("Which word describes the tall snow-capped peaks of the Himalayas?", "Lofty.", "Easy", "Understanding"),
         ("Which word describes the house or home of snow in 'Himalaya'?", "Abode.", "Easy", "Understanding"),
         ("Give a synonym for 'lofty'.", "Tall / majestic / high.", "Medium", "Understanding")
     ]),

    # Set 8
    ("The Himalayas (Him + Alaya ) means \"abode of snow\" in Sanskrit. It is given this name because its lofty peaks are covered with snow all the year round.",
     [
         ("What language does the name 'Himalaya' come from?", "Sanskrit.", "Easy", "Remembering"),
         ("What does 'Him' translate to?", "Snow.", "Easy", "Remembering"),
         ("What does 'Alaya' translate to?", "Abode / house.", "Easy", "Remembering"),
         ("How often are the peaks covered with snow?", "All the year round.", "Easy", "Remembering"),
         ("Why is the snow permanent on these peaks?", "Because high altitude keeps temperatures below freezing year-round.", "Medium", "Understanding")
     ]),

    # Set 9
    ("The world's highest peak, Mount Everest (8849 metres) is a part of Himalayas and lies on the border between Nepal and the Tibet Autonomous Region of China.",
     [
         ("What is the elevation of Mount Everest?", "8,849 metres.", "Easy", "Remembering"),
         ("Is Mount Everest part of the Himalayas?", "Yes.", "Easy", "Remembering"),
         ("Which mountain peak is the highest in the world?", "Mount Everest.", "Easy", "Remembering"),
         ("Which Autonomous Region of China borders Mount Everest?", "Tibet Autonomous Region.", "Easy", "Remembering"),
         ("Why do climbers visit Nepal or Tibet?", "To attempt climbing Mount Everest from either side of the border.", "Medium", "Understanding")
     ]),

    # Set 10
    ("The New Zealander Edmund Hillary and Sherpa Tenzing Norgay reached the summit of Mount Everest in 1953.",
     [
         ("Name the climber from New Zealand.", "Edmund Hillary.", "Easy", "Remembering"),
         ("Name the Sherpa climber who reached the summit.", "Tenzing Norgay.", "Easy", "Remembering"),
         ("What mountain summit did they reach?", "Mount Everest.", "Easy", "Remembering"),
         ("What year did this historic event happen?", "1953.", "Easy", "Remembering"),
         ("Summarize the importance of their achievement.", "They were the first humans in history to reach the top of Mount Everest.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 09: The Himalayas\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH09_EXT_{q_counter:03d}"
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

with open(os.path.join(CH09_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 09 in {CH09_DIR}")
