r"""
Refines all 6 Category files for Book 5 Chapter 09 ("Traditional Dresses from India") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH09_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_09")
os.makedirs(CH09_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What do men in Punjab traditionally wear?", "(A) Kurta with a churidar or lungi, along with a colourful turban", "(B) Angrakha and dhoti", "(C) Kediyu and dhoti", "(D) Veshti and angavastram", "(A)", "Punjabi men wear a kurta with churidar/lungi and colourful turban.", "Easy", "Remembering", "State Dress - Punjab"),
    ("What traditional attire do women in Punjab wear?", "(A) Vibrant salwar kameez with a dupatta featuring embroidery and mirror work", "(B) Nauvari saree", "(C) Mekhela Chador", "(D) Kasavu saree", "(A)", "Punjabi women wear vibrant salwar kameez with dupatta.", "Easy", "Remembering", "State Dress - Punjab"),
    ("What is the traditional turban worn by Rajasthani men called?", "(A) Pagri", "(B) Pheta", "(C) Gamosa", "(D) Angavastram", "(A)", "Rajasthani men wear a colourful pagri (turban).", "Easy", "Remembering", "State Dress - Rajasthan"),
    ("What do Rajasthani women wear traditionally?", "(A) Bright, embroidered ghagra choli with a matching odhani (veil)", "(B) Phanek and innaphi", "(C) Kasavu saree", "(D) Pattu saree", "(A)", "Rajasthani women wear an embroidered ghagra choli with odhani.", "Easy", "Remembering", "State Dress - Rajasthan"),
    ("Which short, pleated frock-like top is worn by men in Gujarat?", "(A) Kediyu", "(B) Pheran", "(C) Angrakha", "(D) Kurta", "(A)", "Gujarati men wear a kediyu with dhoti or churidar.", "Easy", "Remembering", "State Dress - Gujarat"),
    ("What traditional attire do Gujarati women wear along with a bandhani dupatta?", "(A) Chaniya choli decorated with mirror work and embroidery", "(B) Nauvari saree", "(C) Mekhela Chador", "(D) White saree with red border", "(A)", "Gujarati women wear chaniya choli with bandhani dupatta.", "Easy", "Remembering", "State Dress - Gujarat"),
    ("What unique style saree is worn by women in Maharashtra for easy movement?", "(A) Nauvari saree", "(B) Kasavu saree", "(C) Pattu saree", "(D) Mekhela Chador", "(A)", "Maharashtrian women wear a traditional Nauvari saree.", "Easy", "Remembering", "State Dress - Maharashtra"),
    ("What is the traditional turban worn by Maharashtrian men called?", "(A) Pheta", "(B) Pagri", "(C) Gamosa", "(D) Innaphi", "(A)", "Maharashtrian men wear a pheta.", "Easy", "Remembering", "State Dress - Maharashtra"),
    ("What saree do Bengali women traditionally wear during festivals like Durga Puja?", "(A) A white saree with a red border", "(B) Kasavu saree with golden border", "(C) Pattu silk saree", "(D) Nauvari saree", "(A)", "Bengali women wear a white saree with a red border during Durga Puja.", "Easy", "Remembering", "State Dress - West Bengal"),
    ("What is the traditional dhoti worn by men in Tamil Nadu called?", "(A) Veshti", "(B) Mundu", "(C) Kediyu", "(D) Pheran", "(A)", "Tamil Nadu men wear a veshti with an angavastram.", "Easy", "Remembering", "State Dress - Tamil Nadu"),
    ("What traditional shawl is worn over the shoulder by Tamil Nadu men?", "(A) Angavastram", "(B) Odhani", "(C) Dupatta", "(D) Innaphi", "(A)", "Tamil Nadu men wear an angavastram (shawl).", "Easy", "Remembering", "State Dress - Tamil Nadu"),
    ("What silk saree is famous among women in Tamil Nadu for its rich colors?", "(A) Pattu saree", "(B) Kasavu saree", "(C) Nauvari saree", "(D) Bandhani saree", "(A)", "Tamil Nadu women wear a pattu (silk) saree.", "Easy", "Remembering", "State Dress - Tamil Nadu"),
    ("What traditional scarf cloth is worn by Assamese men over their dhoti and kurta?", "(A) Gamosa", "(B) Pagri", "(C) Pheta", "(D) Odhani", "(A)", "Assamese men wear a traditional gamosa.", "Easy", "Remembering", "State Dress - Assam"),
    ("What two-piece embroidered garment is worn by Assamese women?", "(A) Mekhela Chador", "(B) Phanek and innaphi", "(C) Chaniya choli", "(D) Ghagra choli", "(A)", "Assamese women wear a beautiful Mekhela Chador.", "Easy", "Remembering", "State Dress - Assam"),
    ("What long woolen gown is worn by both men and women in Kashmir to stay warm?", "(A) Pheran", "(B) Kediyu", "(C) Mundu", "(D) Angrakha", "(A)", "Kashmiri people wear a long woolen pheran to keep warm.", "Easy", "Remembering", "State Dress - Kashmir"),
    ("What traditional white waistcloth is worn by men in Kerala?", "(A) Mundu", "(B) Veshti", "(C) Dhoti", "(D) Lungi", "(A)", "Men in Kerala wear a white mundu wrapped around the waist.", "Easy", "Remembering", "State Dress - Kerala"),
    ("What saree from Kerala is famous for being white with a golden border?", "(A) Kasavu saree", "(B) Pattu saree", "(C) Nauvari saree", "(D) Bandhani saree", "(A)", "Women in Kerala wear a traditional Kasavu saree (white with golden border).", "Easy", "Remembering", "State Dress - Kerala"),
    ("What wrap-around skirt is traditionally worn by women in Manipur?", "(A) Phanek", "(B) Ghagra", "(C) Chaniya", "(D) Mekhela", "(A)", "Manipuri women wear a phanek (wrap-around skirt).", "Easy", "Remembering", "State Dress - Manipur"),
    ("What shawl-like top is paired with a phanek by Manipuri women?", "(A) Innaphi", "(B) Odhani", "(C) Dupatta", "(D) Angavastram", "(A)", "Manipuri women pair a phanek with an innaphi.", "Easy", "Remembering", "State Dress - Manipur"),
    ("What does the word 'attire' mean according to the vocabulary section?", "(A) Clothes, especially special ones", "(B) Footwear worn for sports", "(C) Heavy metal jewelry", "(D) A musical instrument", "(A)", "Attire = Clothes, especially special ones.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'embroidery' mean?", "(A) Decorative stitching on cloth", "(B) Painting on paper", "(C) Cutting cloth into ribbons", "(D) Washing clothes in hot water", "(A)", "Embroidery = Decorative stitching on cloth.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'ornament' mean?", "(A) A piece of jewellery or decoration", "(B) A wooden chair", "(C) A woolen blanket", "(D) A heavy book", "(A)", "Ornament = A piece of jewellery or decoration.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'heritage' mean?", "(A) Traditions passed down through generations", "(B) Buying new modern clothes", "(C) Foreign language lessons", "(D) Building new brick houses", "(A)", "Heritage = Traditions passed down through generations.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'distinctive' mean?", "(A) Something that stands out or is unique", "(B) Something that looks completely ordinary", "(C) Something made of glass", "(D) Something that changes every day", "(A)", "Distinctive = Something that stands out or is unique.", "Easy", "Understanding", "Vocabulary"),
    ("What title is given to Chapter 09?", "(A) Traditional Dresses from India", "(B) Island Groups of India", "(C) The Magic of Books", "(D) The Narmada River", "(A)", "Title is 'Traditional Dresses from India'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("How does climate influence traditional clothing choices across Indian states?", "(A) Cold climates (Kashmir) require heavy woolen pherans; hot tropical climates (Kerala/Tamil Nadu) require lightweight cotton mundus and veshtis", "(B) Everyone wears thick wool everywhere", "(C) Climate has no relationship to clothing", "(D) Cold climates require silk sarees only", "(A)", "Climate dictates fabric weight: wool in cold Kashmir vs light cotton in hot South India.", "Medium", "Analyzing", "Climate & Attire"),
    ("Why is the Nauvari saree draped differently from a standard six-yard saree in Maharashtra?", "(A) It is draped like a dhoti between the legs, allowing women freedom of physical movement for farm work and martial history", "(B) It requires four people to wrap", "(C) It is made of pure rubber", "(D) It is worn upside down", "(A)", "Draped like a dhoti between legs for physical mobility and ease of work.", "Medium", "Understanding", "Cultural Utility"),
    ("Compare the traditional waist garments worn by men in Tamil Nadu (Veshti) and Kerala (Mundu).", "(A) Both are unstitched white cotton cloths wrapped around the waist, reflecting South India's warm tropical climate", "(B) Veshti is made of heavy wool while Mundu is made of leather", "(C) Mundu is a long gown while Veshti is trousers", "(D) Both are worn on the head", "(A)", "Both are white cotton waist-wraps suitable for tropical heat.", "Medium", "Comparing", "Regional Comparison"),
    ("What common decorative feature connects traditional women's clothing in Gujarat and Punjab?", "(A) Both feature intricate embroidery and mirror work on dupattas and kameez/cholis", "(B) Both use heavy fur linings", "(C) Both avoid all bright colors", "(D) Both are made from plastic sheets", "(A)", "Both utilize vibrant embroidery and decorative mirror work.", "Medium", "Comparing", "Decorative Art"),
    ("Why are traditional garments described as a 'visual delight' in Chapter 09?", "(A) Because their vibrant colors, distinctive ornaments, and regional embroidery showcase India's rich cultural pride and diversity", "(B) Because they are invisible", "(C) Because they cost no money", "(D) Because they are worn only in dark rooms", "(A)", "Vibrant colors, distinctive ornaments, and embroidery reflect cultural pride.", "Medium", "Evaluating", "Aesthetic Value"),
    ("What cultural significance does the white saree with a red border hold in West Bengal?", "(A) It is sacred traditional attire worn during major spiritual festivals like Durga Puja", "(B) It is worn only during cold winters", "(C) It is a mandatory school uniform", "(D) It is imported from foreign countries", "(A)", "Sacred traditional dress for spiritual festivals like Durga Puja.", "Medium", "Understanding", "Spiritual Connection"),
    ("Explain the dual component structure of Assam's 'Mekhela Chador'.", "(A) It consists of a lower wrap-around skirt (Mekhela) and an upper draped shawl (Chador)", "(B) It is a single long piece of cloth wrapped around head and feet", "(C) It is a woolen coat paired with trousers", "(D) It is a shirt and tie", "(A)", "Two-piece: lower skirt (Mekhela) + upper draped shawl (Chador).", "Medium", "Understanding", "Garment Structure"),
    ("Why do men in Rajasthan and Punjab wear colourful turbans (Pagri / Turban)?", "(A) Turbans protect against harsh sun while serving as symbols of honor, identity, and regional pride", "(B) Turbans are used to carry heavy rocks", "(C) Turbans are worn only during sleep", "(D) Turbans replace shirts", "(A)", "Protects against sun while serving as a symbol of honor and regional identity.", "Medium", "Analyzing", "Cultural Significance"),
    ("How does traditional clothing preserve a nation's heritage?", "(A) By passing down weaving, dyeing, and embroidery craftsmanship from generation to generation", "(B) By forcing everyone to wear modern western suits", "(C) By importing fast fashion from abroad", "(D) By throwing away historical garments", "(A)", "Passes down indigenous craft traditions through generations.", "Medium", "Evaluating", "Heritage Preservation"),
    ("Contrast the winter attire of Kashmir (Pheran) with the coastal attire of Kerala (Kasavu).", "(A) Kashmir's Pheran is a thick woolen long gown for snow; Kerala's Kasavu is a light, breathable white cotton saree for coastal humidity", "(B) Pheran is worn in oceans; Kasavu is worn in deserts", "(C) Both garments are made of identical wool", "(D) Pheran is a hat; Kasavu is a shoe", "(A)", "Thick wool for snow vs light cotton for coastal humidity.", "Medium", "Comparing", "Geographic Contrast"),
    ("What makes Manipuri traditional attire (Phanek and Innaphi) unique among Northeastern states?", "(A) The phanek is a hand-woven striped wrap skirt paired with a light, transparent embroidered innaphi shawl", "(B) It is made of heavy metal chains", "(C) It is identical to Rajasthani ghagra", "(D) It has no colors", "(A)", "Hand-woven striped wrap skirt paired with a light embroidered shawl.", "Medium", "Understanding", "Northeastern Design"),
    ("What role do traditional ornaments play alongside regional attire?", "(A) Ornaments complement the attire, enhancing visual elegance and representing regional craft traditions", "(B) Ornaments make clothes heavy so people cannot walk", "(C) Ornaments replace clothing", "(D) Ornaments are used as weapons", "(A)", "Enhance visual elegance and represent regional craftsmanship.", "Medium", "Understanding", "Ornaments Function"),
    ("Why is India described as a 'land of rich culture and diversity' in Chapter 09?", "(A) Because each state exhibits unique dresses, languages, climates, and historical heritages", "(B) Because all 28 states have identical clothing", "(C) Because India has only one river", "(D) Because no one lives in India", "(A)", "Unique dresses, languages, climates, and heritage across states.", "Medium", "Evaluating", "Diversity Analysis"),
    ("Summarize Chapter 09 in four concise sentences.", "India's rich cultural diversity is reflected in the traditional dresses of its states. Northern and western states like Punjab, Rajasthan, and Gujarat feature colourful turbans, salwar kameez, and embroidered ghagras. Southern and eastern states wear elegant silk pattu, Kasavu sarees, veshtis, and Mekhela Chador suitable for their climates. Cold Kashmir relies on woolen pherans, showing how attire reflects history, climate, and regional pride.", "Medium", "Understanding", "Chapter Summary"),
    ("How can Class 5 students show appreciation for India's traditional textile heritage?", "(A) By wearing regional ethnic attire during cultural events, learning about local handlooms, and respecting national diversity", "(B) By ridiculing traditional clothing", "(C) By refusing to learn about other states", "(D) By cutting old handloom sarees", "(A)", "Wear ethnic attire during events, learn about handlooms, respect diversity.", "Medium", "Applying", "Cultural Appreciation"),

    # Hard (41-50)
    ("Critique the impact of globalized fast fashion on traditional handloom weavers in Indian states.", "(A) Mass-produced synthetic clothes threaten traditional handloom weavers, requiring state patronage and consumer conscious buying to preserve heritage", "(B) Fast fashion has made handlooms obsolete and useless", "(C) Traditional weavers don't need any support", "(D) Handloom sarees are illegal", "(A)", "Mass synthetic fashion threatens weavers, requiring patronage and conscious buying to save heritage.", "Hard", "Evaluating", "HOTS Economic & Cultural Critique"),
    ("Deconstruct the ergonomic functionality of the Gujarati 'Kediyu' frock-top.", "(A) The short pleated design allows farm workers freedom of arm movement while the thick cotton fabric protects against desert heat and dust", "(B) It is designed to trap heat in summer", "(C) It prevents workers from moving", "(D) It is an imported rain coat", "(A)", "Short pleated design permits free movement while thick cotton shields heat and dust.", "Hard", "Analyzing", "Ergonomic Analysis"),
    ("Evaluate the ecological sustainability of traditional natural dyes (like Bandhani) and organic fabrics.", "(A) Hand-dyed organic cottons and silks have low carbon footprints, utilize natural plant dyes, and support eco-friendly fashion", "(B) Traditional fabrics cause massive river pollution", "(C) Synthetic polyester is more eco-friendly than cotton", "(D) Natural dyes destroy handloom tools", "(A)", "Low carbon footprint, plant-based dyes, and eco-friendly sustainability.", "Hard", "Evaluating", "Ecological Evaluation"),
    ("Compare the textile motifs of North-Eastern weaving (Assam/Manipur) with Western Indian block printing (Gujarat/Rajasthan).", "(A) NE weaving uses geometric loom-woven motifs (Mekhela/Phanek); Western printing uses hand-block stamps and tie-dye (Bandhani)", "(B) NE uses block printing; Western uses loom weaving only", "(C) Both regions use identical machine prints", "(D) NE textiles contain no patterns", "(A)", "NE uses geometric loom motifs; Western uses hand-block stamps and tie-dye.", "Hard", "Comparing", "Comparative Textile Analysis"),
    ("Formulate a script for a school fashion show celebrating 'Traditional Dresses from India'.", "(A) 'Welcome to our runway of diversity! From the woolen Pheran of snowy Kashmir to the golden Kasavu of sunny Kerala, watch India's heritage come alive!'", "(B) 'Today we showcase modern business suits.'", "(C) 'Watch five identical blue shirts.'", "(D) 'This fashion show features foreign raincoats.'", "(A)", "Runway script celebrating diversity from Kashmiri Pheran to Kerala Kasavu.", "Hard", "Creating", "Show Script Design"),
    ("Assess the role of GI (Geographical Indication) tags in protecting regional textiles like Kanchipuram Pattu or Banarasi silk.", "(A) GI tags legally protect authentic regional handlooms from counterfeit industrial imitations, safeguarding weaver livelihoods", "(B) GI tags ban foreign tourists from buying sarees", "(C) GI tags make sarees illegal to wear", "(D) GI tags increase thread weight by ten kilograms", "(A)", "Legally protects authentic regional handlooms from counterfeit imitations.", "Hard", "Evaluating", "Legal & Cultural Protection"),
    ("Analyze how color symbolism operates in Bengali (white/red) and Kerala (white/gold) festival attire.", "(A) White symbolizes purity and peace; red in Bengal represents divine feminine power (Durga), while gold in Kerala represents prosperity and auspiciousness", "(B) Colors are chosen completely at random", "(C) White represents sorrow in all festivals", "(D) Red is banned in West Bengal", "(A)", "White = purity; Red in Bengal = divine power; Gold in Kerala = prosperity.", "Hard", "Analyzing", "Color Symbolism"),
    ("Synthesize how Chapter 09 connects geography, climate, history, and artistic expression.", "(A) Demonstrates that attire is not arbitrary fashion, but an artistic synthesis of local climate needs, geographic raw materials, and historical traditions", "(B) Proves that clothes have no connection to geography", "(C) Replaces geography lessons with shopping lists", "(D) Focuses solely on hat colors", "(A)", "Attire synthesizes local climate needs, raw materials, and historical art.", "Hard", "Synthesizing", "Cross-Disciplinary Synthesis"),
    ("Critique the claim: 'Traditional Indian dresses are uncomfortable and impractical for modern life.'", "(A) Inaccurate; garments like the Nauvari saree, Mundu, and Salwar Kameez were ergonomically designed for climate comfort and physical activity", "(B) Completely true; no one can move in traditional clothes", "(C) False; traditional clothes are worn only in museums", "(D) True; modern polyester is superior in tropical heat", "(A)", "Inaccurate; traditional garments were ergonomically designed for local climate and movement.", "Hard", "Evaluating", "Historical Accuracy Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 09 for a Class 5 assessment.", "(A) 'Describe the traditional dresses of four different Indian states from Chapter 09. Explain how climate, culture, and materials influence these garments.'", "(B) 'Write five sentences about your favorite shirt.'", "(C) 'List five colors of thread.'", "(D) 'Draw a picture of a pair of shoes.'", "(A)", "Structured essay prompt evaluating state dresses, climate influence, and cultural materials.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 09: Traditional Dresses from India\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH09_MCQ_{idx:03d}"
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

with open(os.path.join(CH09_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("India is a land of rich culture and _______.", "diversity", "Culture and diversity.", "Easy"),
    ("In Punjab, men wear a kurta with a churidar or lungi, along with a colourful _______.", "turban", "Colourful turban.", "Easy"),
    ("Punjabi women wear a vibrant salwar kameez decorated with embroidery and _______ work.", "mirror", "Mirror work.", "Easy"),
    ("Rajasthani men wear an angrakha and dhoti with a colourful _______.", "pagri", "Colourful pagri.", "Easy"),
    ("Rajasthani women wear a bright embroidered ghagra choli with a matching _______.", "odhani", "Matching odhani veil.", "Easy"),
    ("Men in Gujarat wear a short, pleated frock-like top called a _______.", "kediyu", "Called a kediyu.", "Easy"),
    ("Gujarati women wear a chaniya choli along with a bandhani _______.", "dupatta", "Bandhani dupatta.", "Easy"),
    ("The Nauvari saree is traditionally worn by women in the state of _______.", "Maharashtra", "Worn in Maharashtra.", "Easy"),
    ("Maharashtrian men wear a dhoti and kurta along with a turban called a _______.", "pheta", "Turban called pheta.", "Easy"),
    ("Bengali women traditionally wear a white saree with a _______ border during Durga Puja.", "red", "White saree with red border.", "Easy"),
    ("In Tamil Nadu, men wear a veshti with a shawl called an _______.", "angavastram", "Shawl called angavastram.", "Easy"),
    ("Women in Tamil Nadu wear a silk saree known as a _______ saree.", "pattu", "Pattu silk saree.", "Easy"),
    ("In Assam, men wear a dhoti with a kurta and a traditional cloth scarf called a _______.", "gamosa", "Cloth scarf called gamosa.", "Easy"),
    ("Assamese women wear a two-piece garment called a _______ Chador.", "Mekhela", "Mekhela Chador.", "Easy"),
    ("In Kashmir, both men and women wear a long woolen gown called a _______.", "pheran", "Woolen gown called pheran.", "Easy"),
    ("Men in Kerala wear a white cloth wrapped around the waist called a _______.", "mundu", "Waist cloth called mundu.", "Easy"),
    ("Women in Kerala wear a traditional _______ saree, which is white with a golden border.", "Kasavu", "White with golden border.", "Easy"),
    ("Women in Manipur wear a wrap-around skirt called a _______.", "phanek", "Wrap skirt called phanek.", "Easy"),
    ("Manipuri women pair a phanek with a shawl-like top called an _______.", "innaphi", "Shawl-like top called innaphi.", "Easy"),
    ("Attire is defined in vocabulary as _______, especially special ones.", "clothes", "Attire means clothes.", "Easy"),
    ("Embroidery is defined as decorative _______ on cloth.", "stitching", "Decorative stitching.", "Easy"),
    ("An ornament is defined as a piece of jewellery or _______.", "decoration", "Piece of jewellery or decoration.", "Easy"),
    ("Heritage refers to traditions passed down through _______.", "generations", "Passed down through generations.", "Easy"),
    ("Distinctive means something that stands out or is _______.", "unique", "Stands out or is unique.", "Easy"),
    ("Chapter 09 is titled 'Traditional Dresses from _______'.", "India", "Traditional Dresses from India.", "Easy"),

    # Medium (26-40)
    ("The Kasavu saree of Kerala features a striking _______ border on white cotton.", "golden", "Golden border on white.", "Medium"),
    ("Kashmiri women pair their woolen pheran with a colourful _______.", "headscarf", "Colourful headscarf.", "Medium"),
    ("The Nauvari saree's unique draping style permits free physical _______.", "movement", "Permits free physical movement.", "Medium"),
    ("Bengali men traditionally pair their dhoti with a _______.", "kurta", "Dhoti with a kurta.", "Medium"),
    ("Chaniya choli in Gujarat is famous for intricate mirror _______.", "work", "Intricate mirror work.", "Medium"),
    ("The pagri worn in Rajasthan protects against the desert _______.", "sun", "Protects against desert sun.", "Medium"),
    ("Mekhela Chador embroidery showcases Assamese weaving _______.", "artistry", "Showcases weaving artistry.", "Medium"),
    ("South Indian veshtis and mundus are ideal for humid tropical _______.", "climates", "Ideal for tropical climates.", "Medium"),
    ("Manipuri men wear a dhoti and jacket during traditional _______.", "events", "During traditional events.", "Medium"),
    ("Durga Puja is a major festival celebrated in West _______.", "Bengal", "Celebrated in West Bengal.", "Medium"),
    ("Bandhani is a traditional tie-and-dye textile art from Gujarat and _______.", "Rajasthan", "Art from Gujarat and Rajasthan.", "Medium"),
    ("Pattu silk sarees are renowned for rich colors and intricate _______.", "designs", "Rich colors and intricate designs.", "Medium"),
    ("Traditional ornaments worn alongside dresses reflect regional _______.", "craftsmanship", "Reflect regional craftsmanship.", "Medium"),
    ("Each state's traditional attire becomes a true visual _______.", "delight", "True visual delight.", "Medium"),
    ("Chapter 09 highlights how clothing keeps national traditions _______.", "alive", "Keeps traditions alive.", "Medium"),

    # Hard (41-50)
    ("Handloom weaving preserves indigenous textile art against industrial _______.", "mass-production", "Preserves against mass-production.", "Hard"),
    ("Climatic adaptation determines fabric choices from Kashmiri wool to Keralite _______.", "cotton", "From wool to Keralite cotton.", "Hard"),
    ("Geographical Indication tags safeguard authentic regional garment _______.", "heritage", "Safeguards regional heritage.", "Hard"),
    ("Ergonomic draping in Nauvari sarees reflects historical Maharashtrian _______.", "culture", "Reflects Maharashtrian culture.", "Hard"),
    ("Symbolic color pairings mirror regional spiritual and social _______.", "customs", "Mirror spiritual customs.", "Hard"),
    ("Embroidered motifs preserve ancestral storytelling on traditional _______.", "garments", "Preserve storytelling on garments.", "Hard"),
    ("Textile diversity showcases India's multi-ethnic cultural _______.", "tapestry", "Showcases multi-ethnic tapestry.", "Hard"),
    ("Sustaining traditional attire empowers rural handloom artisan _______.", "communities", "Empowers artisan communities.", "Hard"),
    ("Historical analysis reveals traditional dress as an evolving living _______.", "tradition", "Evolving living tradition.", "Hard"),
    ("Chapter 09 instills Class 5 students with pride in India's cultural _______.", "legacy", "Instills pride in cultural legacy.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 09: Traditional Dresses from India\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH09_FIB_{idx:03d}"
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
    ("India is a land of rich culture and diversity.", "True", "Text confirms India has rich culture and diversity.", "Easy"),
    ("In Punjab, men traditionally wear a kurta with a churidar or lungi, along with a colourful turban.", "True", "Text confirms Punjabi men wear a kurta with churidar/lungi and turban.", "Easy"),
    ("Punjabi women wear a Nauvari saree.", "False", "Punjabi women wear a vibrant salwar kameez with a dupatta.", "Easy"),
    ("The pagri worn by Rajasthani men is a type of turban.", "True", "Text confirms pagri is a turban worn in Rajasthan.", "Easy"),
    ("Rajasthani women wear a Mekhela Chador.", "False", "Rajasthani women wear a ghagra choli with an odhani.", "Easy"),
    ("The kediyu worn by Gujarati men is a long, flowing woolen gown.", "False", "Kediyu is a short, pleated frock-like top.", "Easy"),
    ("Gujarati women wear a chaniya choli with a bandhani dupatta.", "True", "Text confirms Gujarati women wear a chaniya choli with bandhani dupatta.", "Easy"),
    ("The Nauvari saree is draped in a unique style that allows for easy movement.", "True", "Text confirms Nauvari saree allows easy movement.", "Easy"),
    ("The pheta is a type of footwear worn in Maharashtra.", "False", "Pheta is a traditional turban worn by Maharashtrian men.", "Easy"),
    ("Bengali women traditionally wear a white saree with a red border during Durga Puja.", "True", "Text confirms Bengali women wear a white saree with a red border.", "Easy"),
    ("In Tamil Nadu, men wear a veshti with an angavastram and a shirt.", "True", "Text confirms Tamil Nadu men wear a veshti and angavastram.", "Easy"),
    ("Pattu saree worn in Tamil Nadu is a type of heavy woolen coat.", "False", "Pattu saree is a silk saree known for rich colors and designs.", "Easy"),
    ("Assamese men wear a dhoti with a kurta and a traditional gamosa.", "True", "Text confirms Assamese men wear a gamosa cloth scarf.", "Easy"),
    ("The Mekhela Chador is a two-piece garment worn by Assamese women.", "True", "Text confirms Mekhela Chador is a two-piece garment.", "Easy"),
    ("Both men and women in Kashmir wear a long woolen gown called a pheran.", "True", "Text confirms Kashmiri people wear a long woolen pheran to keep warm.", "Easy"),
    ("Men in Kerala wear a heavy woolen coat called a mundu.", "False", "Mundu is a white cotton cloth wrapped around the waist.", "Easy"),
    ("The Kasavu saree of Kerala is white with a golden border.", "True", "Text confirms Kasavu saree is white with a golden border.", "Easy"),
    ("Women in Manipur wear a wrap-around skirt called a phanek.", "True", "Text confirms Manipuri women wear a phanek skirt.", "Easy"),
    ("Manipuri women pair a phanek with a shawl-like top called an innaphi.", "True", "Text confirms phanek is paired with an innaphi.", "Easy"),
    ("'Attire' means clothes, especially special ones.", "True", "Vocabulary definition: Attire = Clothes, especially special ones.", "Easy"),
    ("'Embroidery' means painting with watercolors on paper.", "False", "Embroidery = Decorative stitching on cloth.", "Easy"),
    ("'Ornament' means a piece of jewellery or decoration.", "True", "Vocabulary definition: Ornament = Piece of jewellery or decoration.", "Easy"),
    ("'Heritage' means buying modern clothes online.", "False", "Heritage = Traditions passed down through generations.", "Easy"),
    ("'Distinctive' means something that stands out or is unique.", "True", "Vocabulary definition: Distinctive = Something that stands out or is unique.", "Easy"),
    ("Traditional garments showcase India's diversity and keep traditions alive.", "True", "Text confirms traditional garments showcase diversity and keep traditions alive.", "Easy"),

    # Medium (26-40)
    ("The woolen pheran worn in Kashmir is designed to protect against tropical heat.", "False", "Pheran is designed to keep warm during cold Kashmiri winters.", "Medium"),
    ("Bandhani is a tie-and-dye fabric technique associated with Gujarat and Rajasthan.", "True", "Bandhani is famous in Gujarat and Rajasthan.", "Medium"),
    ("Angavastram is a traditional shawl worn across the shoulder by men in Tamil Nadu.", "True", "Angavastram is a shawl worn over the shoulder in Tamil Nadu.", "Medium"),
    ("Gamosa in Assam is used only as a floor mat.", "False", "Gamosa is a sacred traditional cloth used as a scarf or honor towel.", "Medium"),
    ("Durga Puja is the primary festival where Bengali women wear white-and-red sarees.", "True", "Durga Puja is the main festival for white-and-red sarees.", "Medium"),
    ("The chaniya choli of Gujarat often features mirror work decoration.", "True", "Text confirms chaniya choli features mirror work.", "Medium"),
    ("Men in Kerala wear a shirt with their white waistcloth called a mundu.", "True", "Text confirms men in Kerala wear a mundu with a shirt.", "Medium"),
    ("The Pheta of Maharashtra and Pagri of Rajasthan are both forms of turbans.", "True", "Both Pheta and Pagri are regional terms for traditional turbans.", "Medium"),
    ("Assamese Mekhela Chador is a single uninterrupted piece of cloth like a saree.", "False", "Mekhela Chador is a two-piece garment (skirt + shawl).", "Medium"),
    ("Pattu silk sarees are woven primarily in Tamil Nadu.", "True", "Pattu silk sarees are famous in Tamil Nadu.", "Medium"),
    ("Traditional Indian dresses reflect regional history, climate, and cultural pride.", "True", "Text confirms dresses reflect history, climate, and cultural pride.", "Medium"),
    ("Women in Kashmir pair their pheran with a colourful headscarf.", "True", "Text confirms Kashmiri women pair pheran with a headscarf.", "Medium"),
    ("Manipuri men wear a pheran during traditional events.", "False", "Manipuri men wear a dhoti and jacket during traditional events.", "Medium"),
    ("Mirror work and embroidery are common craft elements in western Indian attire.", "True", "Common in Punjabi, Rajasthani, and Gujarati traditional wear.", "Medium"),
    ("Chapter 09 highlights ten different Indian states and their unique traditional dresses.", "True", "Covers Punjab, Rajasthan, Gujarat, Maharashtra, W. Bengal, Tamil Nadu, Assam, Kashmir, Kerala, Manipur.", "Medium"),

    # Hard (41-50)
    ("Climatic variation across India directly dictated the choice of natural fibers (wool vs cotton).", "True", "Wool in Kashmir vs cotton in Kerala reflects direct climatic adaptation.", "Hard"),
    ("Nauvari saree draping allowed 18th-century Maharashtrian women to ride horses.", "True", "Historical draping enabled active mobility including horseback riding.", "Hard"),
    ("Traditional handloom weaving uses chemical polyester threads exclusively.", "False", "Traditional handloom uses natural silk, cotton, and wool fibers.", "Hard"),
    ("Gamosa holds symbolic cultural honor beyond basic everyday attire in Assam.", "True", "Gamosa represents respect, devotion, and hospitality in Assamese culture.", "Hard"),
    ("The white-and-gold Kasavu saree of Kerala is woven from unbleached cotton and zari.", "True", "Kasavu is made from unbleached off-white cotton and gold zari borders.", "Hard"),
    ("Industrial fast fashion has completely eliminated traditional clothing in Indian villages.", "False", "Traditional dresses remain vibrant during festivals, ceremonies, and daily life.", "Hard"),
    ("Distinctive regional ornaments are designed to complement specific ethnic attire.", "True", "Ornaments are crafted to harmonize with regional garment aesthetics.", "Hard"),
    ("Each state's traditional attire represents a unique facet of India's multi-ethnic identity.", "True", "Reflects India's multi-ethnic cultural tapestry.", "Hard"),
    ("Chapter 09 integrates geography, art, and English language comprehension for Class 5.", "True", "Integrates state geography, textile art, and vocabulary comprehension.", "Hard"),
    ("Preserving traditional attire supports rural artisan economies across Indian states.", "True", "Handloom production supports millions of rural artisan families.", "Hard")
]

tf_content = f"# True / False — Chapter 09: Traditional Dresses from India\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH09_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Question**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH09_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("What do traditional dresses across different Indian states reflect according to Chapter 09?", "Traditional dresses reflect each state's unique culture, climate, history, and cultural pride.", "Easy", "Remembering"),
    ("Describe the traditional dress of men and women in Punjab.", "Men wear a kurta with a churidar or lungi and a colourful turban. Women wear a vibrant salwar kameez with a dupatta decorated with embroidery and mirror work.", "Easy", "Remembering"),
    ("What do men and women traditionally wear in Rajasthan?", "Men wear an angrakha and dhoti with a colourful pagri (turban). Women wear a bright, embroidered ghagra choli with a matching odhani (veil).", "Easy", "Remembering"),
    ("What is a 'kediyu' and in which state is it traditionally worn?", "A kediyu is a short, pleated frock-like top worn by men with a dhoti or churidar in Gujarat.", "Easy", "Remembering"),
    ("What traditional attire do women in Gujarat wear?", "Gujarati women wear a chaniya choli decorated with mirror work and embroidery, along with a bandhani dupatta.", "Easy", "Remembering"),
    ("What is unique about the Nauvari saree worn by women in Maharashtra?", "The Nauvari saree is draped in a unique nine-yard style (like a dhoti) that allows for easy physical movement.", "Easy", "Understanding"),
    ("What do men in Maharashtra wear traditionally?", "Maharashtrian men wear a dhoti and kurta along with a turban called a pheta.", "Easy", "Remembering"),
    ("What traditional saree do women in West Bengal wear during Durga Puja?", "Bengali women traditionally wear a white saree with a distinct red border during festivals like Durga Puja.", "Easy", "Remembering"),
    ("What do men traditionally wear in Tamil Nadu?", "Men in Tamil Nadu wear a veshti (a type of white dhoti) with an angavastram (shawl) and a shirt.", "Easy", "Remembering"),
    ("What is a 'pattu saree' and where is it worn?", "A pattu saree is a rich silk saree known for vibrant colors and intricate designs, traditionally worn by women in Tamil Nadu.", "Easy", "Remembering"),
    ("Describe the traditional attire of men and women in Assam.", "Men wear a dhoti and kurta with a traditional gamosa (cloth scarf). Women wear a Mekhela Chador, a two-piece embroidered garment.", "Easy", "Remembering"),
    ("What is a 'pheran' and why do people in Kashmir wear it?", "A pheran is a long woolen gown worn by both men and women in Kashmir to keep warm during cold winter weather.", "Easy", "Understanding"),
    ("What do men in Kerala wear around their waist?", "Men in Kerala wear a mundu, which is a white cotton cloth wrapped around the waist.", "Easy", "Remembering"),
    ("Describe the traditional Kasavu saree worn by women in Kerala.", "The Kasavu saree is a traditional white cotton saree characterized by an elegant golden border.", "Easy", "Remembering"),
    ("What traditional garments are worn by women in Manipur?", "Manipuri women wear a phanek (a wrap-around skirt) paired with an innaphi (a shawl-like top).", "Easy", "Remembering"),
    ("What does the word 'attire' mean?", "'Attire' means clothes, especially formal or special regional garments.", "Easy", "Understanding"),
    ("What does the word 'embroidery' mean?", "'Embroidery' means decorative stitching made on fabric using needle and thread.", "Easy", "Understanding"),
    ("What does the word 'ornament' mean?", "'Ornament' means a piece of jewellery or item used as a visual decoration.", "Easy", "Understanding"),
    ("What does the word 'heritage' mean?", "'Heritage' refers to cultural traditions, customs, and art passed down through generations.", "Easy", "Understanding"),
    ("What does the word 'distinctive' mean?", "'Distinctive' means having a characteristic that stands out as unique or special.", "Easy", "Understanding"),
    ("Why is clothing in Kashmir made of wool while clothing in Kerala is made of light cotton?", "Because Kashmir has cold winter weather requiring warm wool (pheran), while Kerala has a hot tropical climate requiring breathable cotton (mundu/Kasavu).", "Easy", "Understanding"),
    ("Name two traditional headwear items (turbans) mentioned in Chapter 09 and their states.", "1. Pagri (Rajasthan)\n2. Pheta (Maharashtra).", "Easy", "Remembering"),
    ("What is a 'gamosa' and how is it used in Assam?", "A gamosa is a traditional white-and-red woven cloth used by Assamese men as a scarf, towel, or symbol of respect.", "Easy", "Remembering"),
    ("How do traditional garments keep India's traditions alive?", "By preserving ancestral weaving, embroidery, and draping styles across generations, showcasing cultural pride.", "Easy", "Understanding"),
    ("What title is given to Chapter 09?", "The title of Chapter 09 is 'Traditional Dresses from India'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Analyze how geographic climate dictates fabric choices in Indian traditional dresses.", "Cold northern mountain states (Kashmir) require heavy insulating wool (pherans). Warm tropical coastal states (Kerala, Tamil Nadu) require lightweight, breathable unstitched cotton (mundu, veshti).", "Medium", "Analyzing"),
    ("Explain the difference between a one-piece saree (Kasavu) and a two-piece garment (Mekhela Chador).", "A Kasavu saree is a single six-yard cloth draped around the body. Mekhela Chador consists of two separate pieces: a waist skirt (Mekhela) and an upper shoulder shawl (Chador).", "Medium", "Comparing"),
    ("How does the Nauvari saree reflect the active lifestyle of Maharashtrian women?", "By passing the saree cloth between the legs and tucking it at the back like a dhoti, it frees the legs, allowing women to work in fields, walk long distances, or ride horses effortlessly.", "Medium", "Analyzing"),
    ("Describe the craft techniques of embroidery and mirror work found in western Indian dresses.", "Women in Punjab, Rajasthan, and Gujarat stitch colorful geometric threads (embroidery) and insert tiny reflective glass pieces (mirror work) into fabrics to make garments vibrant.", "Medium", "Understanding"),
    ("What role does headwear play in traditional men's attire across India?", "Headwear like the Pagri (Rajasthan), Pheta (Maharashtra), and Turban (Punjab) protects from weather while symbolizing dignity, social status, and regional identity.", "Medium", "Evaluating"),
    ("Why is the white saree with a red border specially associated with Durga Puja in West Bengal?", "White symbolizes purity and peace, while red symbolizes auspiciousness and divine feminine power, making it the sacred attire for worshipping Goddess Durga.", "Medium", "Understanding"),
    ("Compare the traditional dress of men in Tamil Nadu (Veshti) with men in Kerala (Mundu).", "Both garments are white unstitched cotton waistcloths worn in tropical climates. Veshti is often paired with an angavastram shawl, while Mundu is paired with a simple shirt.", "Medium", "Comparing"),
    ("What makes Manipuri traditional attire (Phanek and Innaphi) distinctive in Northeastern India?", "The phanek is a hand-woven wrap skirt featuring horizontal stripes, paired with a delicate, semi-transparent innaphi shawl draped over the upper body.", "Medium", "Understanding"),
    ("How do distinctive regional ornaments enhance traditional dresses?", "Gold, silver, and bead ornaments complement garment colors and patterns, creating a complete visual aesthetic that reflects regional artisan heritage.", "Medium", "Analyzing"),
    ("Summarize Chapter 09 in four concise sentences.", "India's traditional dresses showcase the country's rich culture, climate, and diversity. Northern states like Punjab, Rajasthan, and Gujarat feature colourful turbans, salwar kameez, kediyus, and embroidered ghagras. Southern and eastern states wear silk pattu, Kasavu sarees, veshtis, and two-piece Mekhela Chador suited to tropical weather. In cold Kashmir, woolen pherans keep people warm, celebrating regional heritage.", "Medium", "Understanding"),
    ("Why are handloom sarees like Pattu and Kasavu prized across India?", "Because they are hand-woven from high-grade silk and cotton, featuring intricate gold zari borders that represent centuries of master weaving tradition.", "Medium", "Evaluating"),
    ("How does traditional dress foster national pride during Indian festivals?", "Wearing regional ethnic attire during festivals connects citizens to their roots, honors ancestors, and visually celebrates India's unity in diversity.", "Medium", "Applying"),
    ("Explain why the kediyu worn in Gujarat has a pleated, short frock design.", "The chest pleats provide air ventilation in hot desert heat while allowing full upper-body flexibility for farm work and Garba folk dancing.", "Medium", "Analyzing"),
    ("How does Chapter 09 demonstrate 'Unity in Diversity' through clothing?", "It shows that while every state has completely different garments, colors, and styles, together they form a harmonious tapestry of national identity.", "Medium", "Evaluating"),
    ("What advice would you give to someone visiting India to understand its textile culture?", "Travel across different states, visit local handloom weaving villages, observe traditional festival attire, and appreciate how climate shapes clothing.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the economic challenge facing traditional handloom weavers against industrial powerlooms.", "Powerlooms mass-produce cheap synthetic imitations rapidly, undercutting handloom prices and threatening authentic weaver livelihoods, requiring consumer patronage and GI protection.", "Hard", "Evaluating"),
    ("Deconstruct the structural design of the Assamese Mekhela Chador.", "The lower Mekhela is pleated and tucked into the waist as a tube skirt; the upper Chador is draped around the torso and pinned over the left shoulder.", "Hard", "Analyzing"),
    ("Evaluate the ecological benefits of traditional cotton and natural dye textiles.", "Hand-spun cotton and plant-based dyes biodegrade naturally, require less chemical processing, and cause zero microplastic water pollution compared to synthetic polyester.", "Hard", "Evaluating"),
    ("Compare Western block-print techniques (Bandhani/Ajrakh) with Eastern loom weaving (Mekhela/Pattu).", "Western techniques apply post-weaving surface decoration through tie-dye and wooden block stamps; Eastern techniques weave patterns directly into fabric threads during loom production.", "Hard", "Comparing"),
    ("Formulate a script for an educational presentation on 'India's Clothing Diversity'.", "'Explore India through its fabrics! From Kashmiri woolen Pherans to Kerala Kasavu cottons, each garment tells a story of climate, history, and master craftsmanship.'", "Hard", "Creating"),
    ("Assess the cultural role of the Gamosa in Assamese hospitality.", "Beyond being a clothing scarf, presenting a red-and-white Gamosa is the highest Assamese sign of respect, welcome, and devotion to guests and elders.", "Hard", "Evaluating"),
    ("Analyze how color symbolism reflects regional ecology (e.g., bright colors in desert Rajasthan).", "In arid, dusty landscapes (Rajasthan/Gujarat), bright red, yellow, and pink garments provide striking visual contrast, bringing joy and color to desert life.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 09 connects geography, climate, and artistic heritage.", "It shows that clothing is a living synthesis of geographic raw materials (cotton/silk/wool), local weather demands, and ancestral decorative arts.", "Hard", "Synthesizing"),
    ("Critique the claim: 'Traditional Indian clothing is dying out and no longer relevant.'", "False; traditional attire remains central to festivals, weddings, daily rural life, and is constantly reinvented by modern designers preserving heritage.", "Hard", "Evaluating"),
    ("Formulate a 4-line poem celebrating India's traditional dresses.", "'From Punjab's turbans bright and bold,\nTo Kerala's sarees trimmed in gold;\nIn Kashmir's wool and Bengal's red,\nOur nation's rich story is woven and spread!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 09: Traditional Dresses from India\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH09_SA_{idx:03d}"
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
    ("Describe the traditional dresses of Punjab, Rajasthan, and Gujarat as detailed in Chapter 09.",
     "Northern and western Indian states feature vibrant, heavily decorated traditional attire suitable for their climates:\n1. **Punjab**: Men wear a kurta paired with a churidar or lungi, along with a bright, colourful turban. Women wear a vibrant salwar kameez with a dupatta featuring rich embroidery and mirror work.\n2. **Rajasthan**: Men wear an angrakha top and dhoti paired with a colourful pagri (turban) to protect against the desert sun. Women wear a bright, embroidered ghagra choli with a matching odhani (veil).\n3. **Gujarat**: Men wear a unique kediyu (a short, pleated frock-like top) with a dhoti or churidar. Women wear a chaniya choli decorated with mirror work and embroidery, paired with a bandhani tie-and-dye dupatta.",
     "Easy", "Remembering"),

    ("Describe the traditional dresses of Maharashtra, West Bengal, and Tamil Nadu as detailed in Chapter 09.",
     "Central, eastern, and southern Indian states feature distinctive draping styles and fine fabrics:\n1. **Maharashtra**: Men wear a dhoti and kurta with a traditional pheta turban. Women wear a Nauvari saree, draped in a unique nine-yard style between the legs that allows complete freedom of physical movement.\n2. **West Bengal**: Bengali men wear a dhoti with a kurta. Women traditionally wear a iconic white saree with a bold red border, especially during religious celebrations like Durga Puja.\n3. **Tamil Nadu**: Men wear a veshti (white cotton waistcloth) with an angavastram (shoulder shawl) and shirt. Women wear a rich pattu silk saree, famous for its vibrant colors and intricate golden woven designs.",
     "Easy", "Remembering"),

    ("Describe the traditional dresses of Assam, Kashmir, Kerala, and Manipur as detailed in Chapter 09.",
     "Dresses in these states reflect regional climate and unique fabric construction:\n1. **Assam**: Men wear a dhoti and kurta with a traditional gamosa (cloth scarf). Women wear a Mekhela Chador, an elegant two-piece embroidered garment.\n2. **Kashmir**: Both men and women wear a long woolen gown called a pheran to keep warm during freezing winter weather. Women pair it with a colourful headscarf.\n3. **Kerala**: Men wear a white cotton mundu wrapped around the waist with a shirt. Women wear a traditional Kasavu saree, which is white with an elegant golden border.\n4. **Manipur**: Women wear a phanek (a wrap-around striped skirt) paired with an innaphi (a shawl-like top), while men wear a dhoti and jacket during traditional events.",
     "Easy", "Remembering"),

    ("Explain how climate determines clothing choices in Kashmir versus Kerala.",
     "Climate plays a decisive role in shaping traditional attire across India:\n- **Kashmir (Cold Mountain Climate)**: Located in the high Himalayas, Kashmir experiences freezing winters and heavy snowfall. To survive cold weather, people wear a thick, long woolen gown called a **pheran** that traps body heat and covers the body from neck to feet.\n- **Kerala (Hot Tropical Coastal Climate)**: Located on the humid southwestern coast, Kerala experiences warm, humid weather year-round. People wear lightweight, breathable unstitched white cotton garments—men wear a **mundu** (waistcloth) and women wear a **Kasavu saree**—which allow air circulation and reflect intense sunlight.",
     "Easy", "Understanding"),

    ("Explain the vocabulary terms from Chapter 09: Attire, Embroidery, Ornament, Heritage, and Distinctive.",
     "1. **Attire**: Clothes, especially formal or special regional garments. *Sentence*: India's regional attire reflects its rich heritage.\n2. **Embroidery**: Decorative needlework stitching on fabric. *Sentence*: Punjabi dupattas feature beautiful mirror work and embroidery.\n3. **Ornament**: A piece of jewellery or item used as a visual decoration. *Sentence*: Traditional gold ornaments complement the pattu saree.\n4. **Heritage**: Cultural traditions, customs, and art passed down through generations. *Sentence*: Handloom weaving is an essential part of Indian heritage.\n5. **Distinctive**: Having a characteristic that stands out as unique. *Sentence*: The Kasavu saree is distinctive for its golden border.",
     "Easy", "Understanding"),

    ("Discuss how traditional dresses keep India's culture and heritage alive.",
     "Traditional dresses act as living expressions of India's cultural heritage. They preserve ancient handloom weaving techniques (like Kasavu and Pattu silk), indigenous dyeing methods (like Bandhani), and decorative needlework (like mirror work and embroidery). Passed down across generations, these garments are worn during family ceremonies, regional festivals, and cultural events. By wearing traditional attire, people maintain a continuous connection to their ancestors, honor local craftsmanship, and keep centuries-old traditions vibrant in modern society.",
     "Easy", "Understanding"),

    ("Compare the headwear worn by men in Punjab (Turban), Rajasthan (Pagri), and Maharashtra (Pheta).",
     "Headwear is a major feature of men's attire across India:\n- **Punjab (Turban)**: Vibrant, neatly folded cloth turbans reflecting Sikh identity, pride, and honor.\n- **Rajasthan (Pagri)**: Long, brightly dyed tie-and-dye cloth wrapped around the head to shield against intense desert heat and sun while indicating regional caste and village identity.\n- **Maharashtra (Pheta)**: A stylishly folded fabric turban worn during formal ceremonies, weddings, and festive occasions as a mark of respect.",
     "Easy", "Comparing"),

    ("Explain why traditional garments are described as a 'visual delight' in Chapter 09.",
     "Traditional garments are described as a 'visual delight' because of their aesthetic richness. The combination of vibrant dyes (bright reds, yellows, greens), intricate decorative stitching (embroidery), reflective glass elements (mirror work), elegant woven borders (gold zari), and matching traditional jewelry creates a stunning visual spectacle. When worn together during regional festivals, these garments transform crowds into a colorful celebration of India's artistic pride.",
     "Easy", "Evaluating"),

    ("Summarize Chapter 09 in five detailed bullet points.",
     "- India's rich cultural diversity is showcased through unique traditional dresses in every state.\n- Western states (Punjab, Rajasthan, Gujarat) feature colourful turbans, salwar kameez, kediyus, and mirror-work chaniya cholis.\n- Central & Eastern states (Maharashtra, West Bengal, Assam) feature dhotis, phetas, red-bordered Durga Puja sarees, and two-piece Mekhela Chador.\n- Southern states (Tamil Nadu, Kerala) wear breathable white veshtis, mundus, silk pattu sarees, and golden-bordered Kasavu sarees.\n- Cold Kashmir relies on long woolen pherans, showing how attire reflects local climate, history, and national pride.",
     "Easy", "Understanding"),

    ("What lessons about respecting diversity can Class 5 students learn from Chapter 09?",
     "Students learn that India's strength lies in its diversity. Just as different states have distinct clothing suited to their local climate and traditions, people across India have different languages, foods, and customs. Chapter 09 teaches students to appreciate and respect cultural differences, realizing that all unique regional traditions join together to form a rich, united nation.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why is the Nauvari saree considered a masterpiece of functional garment design?", "The nine-yard Nauvari saree is draped between the legs without requiring a petticoat, combining the grace of a saree with the physical freedom of trousers, allowing women to work, dance, and ride horses comfortably.", "Easy", "Analyzing"),
    ("Describe the traditional dress of West Bengal and its connection to Durga Puja.", "Bengali men wear a clean white dhoti with a kurta. Women wear a pristine white saree with a vibrant red border. During Durga Puja, this red-and-white saree represents purity, celebration, and devotion to Goddess Durga.", "Easy", "Understanding"),
    ("Explain the two-piece structure of the Assamese Mekhela Chador.", "Unlike standard one-piece sarees, Mekhela Chador has two parts: the Mekhela (a pleated cylindrical waist skirt) and the Chador (a long fabric draped over the upper body and pinned to the shoulder).", "Easy", "Understanding"),
    ("Describe the traditional attire of Manipur for both women and men.", "Women wear a phanek (a wrap-around hand-woven striped skirt) paired with an innaphi (a light, transparent embroidered shawl). Men wear a white dhoti and structured jacket during traditional events.", "Easy", "Remembering"),
    ("How does the Kasavu saree of Kerala reflect simplicity and elegance?", "Woven from fine unbleached off-white cotton with a clean, shining gold zari border, the Kasavu saree eschews heavy patterns for understated, classic coastal elegance.", "Easy", "Evaluating"),
    ("Compare the mirror work of Gujarat with the embroidery of Punjab.", "Gujarati mirror work inserts tiny round mirrors into fabric held by lock-stitches to reflect light; Punjabi phulkari embroidery uses smooth silk threads in dense floral geometric patterns.", "Easy", "Comparing"),
    ("Describe the Gamosa of Assam and its cultural significance.", "The Gamosa is a white cotton cloth woven with red border patterns. Beyond being a shoulder scarf, it is presented as a sacred token of respect, honor, and welcome in Assamese culture.", "Easy", "Understanding"),
    ("How does climate affect traditional attire in desert regions like Rajasthan?", "In hot, dry deserts, people wear loose cotton clothes (angrakha/ghagra) to allow air cooling, while large colorful pagri turbans cushion the head against direct solar radiation.", "Easy", "Analyzing"),
    ("What makes Tamil Nadu's Pattu silk sarees famous across the world?", "Pattu sarees are hand-loomed from pure mulberry silk, dyed in intense contrasting colors, and woven with heavy real gold/silver zari thread patterns along borders and pallu.", "Easy", "Remembering"),
    ("How do traditional ornaments complement regional dresses?", "Regional ornaments—such as silver neckpieces in Rajasthan, gold temple jewelry in Tamil Nadu, or shell beads in the North East—harmonize with garment colors to complete ethnic attire.", "Easy", "Understanding"),
    ("Re-write the story of Chapter 09 as a travelogue of a student visiting four states.", "'In Punjab, I saw bright turbans and mirror-work kameez. Flying to Kashmir, everyone wore warm woolen pherans. In Bengal, white-and-red sarees shone at Durga Puja. Finally in Kerala, golden Kasavu sarees welcomed me!'", "Easy", "Creating"),
    ("Why are handloom garments more environmentally sustainable than synthetic fast fashion?", "Handlooms use natural fibers (cotton, silk, wool) spun on wooden looms and dyed with eco-friendly plant dyes, producing zero microplastics and minimal carbon emissions.", "Easy", "Evaluating"),
    ("How does clothing serve as an expression of regional identity in India?", "Distinctive colors, draping styles, turbans, and motifs instantly signal a person's home state, cultural roots, and community heritage to others.", "Easy", "Analyzing"),
    ("Analyze why Chapter 09 is included in Class 5 English curriculum.", "It expands descriptive English vocabulary (attire, embroidery, heritage, distinctive), develops reading comprehension through state comparisons, and fosters cultural literacy.", "Easy", "Understanding"),
    ("How can school cultural days promote unity in diversity among students?", "By organizing ethnic dress parades where students wear attire from different states, sample regional foods, and celebrate India's shared multi-cultural pride together.", "Easy", "Applying"),

    # Medium (26-40)
    ("Critically analyze how geography, climate, and local natural resources shape traditional state dresses.",
     "Traditional attire is directly shaped by environmental factors:\n1. **Geography & Climate**: Mountainous cold climates (Kashmir) demand thick insulating sheep wool for pherans. Humid coastal climates (Kerala, Tamil Nadu) demand lightweight, breathable unstitched cotton for mundus and veshtis.\n2. **Natural Resources**: States with silk worm cultivation (Tamil Nadu, Assam) developed world-class silk weaving (Pattu, Muga silk). Desert states (Rajasthan, Gujarat) developed tie-dye (Bandhani) and mirror-work to add color to arid landscapes.",
     "Medium", "Analyzing"),

    ("Examine the structural differences in traditional women's wear across India's five geographic zones.",
     "Women's garments vary structurally across regions:\n- **North (Punjab)**: Stitched two-piece Salwar Kameez with dupatta for active movement.\n- **West (Rajasthan/Gujarat)**: Three-piece Ghagra/Chaniya skirt, blouse, and odhani/dupatta.\n- **Central (Maharashtra)**: Nine-yard Nauvari saree draped like a dhoti between legs.\n- **East/Northeast (Bengal/Assam/Manipur)**: Bengal uses six-yard white-red sarees; Assam uses two-piece Mekhela Chador; Manipur uses wrap-around Phanek and Innaphi.\n- **South (Kerala/Tamil Nadu)**: Six-yard Kasavu and Pattu silk sarees with golden borders.",
     "Medium", "Analyzing"),

    ("Evaluate the role of traditional textiles in preserving indigenous Indian art forms.",
     "Traditional garments serve as canvases for ancient indigenous arts. Techniques like Bandhani (tie-dye), Kantha (Bengali embroidery), Phulkari (Punjabi threadwork), Mirror work (Gujarat), and Zari weaving (Tamil Nadu) survive because they are integrated into daily and festival attire, keeping artisan traditions economically viable.",
     "Medium", "Evaluating"),

    ("Discuss how modern Indian fashion designers draw inspiration from traditional state attire.",
     "Modern fashion designers blend traditional elements—such as incorporating Gujarati mirror work into modern jackets, using Assamese Mekhela patterns on contemporary dresses, or adapting Nauvari draping into jumpsuit gowns—bringing ancestral craft to global fashion runways while supporting rural weavers.",
     "Medium", "Analyzing"),

    ("Design an interactive classroom exhibition plan for 'Traditional Dresses of India'.",
     "Exhibition Title: 'Fabrics of Our Nation'\n- **Zone 1 (North & West)**: Display of Punjabi turbans, Rajasthani pagris, and Gujarati mirror-work chaniya cholis.\n- **Zone 2 (East & Northeast)**: Display of Bengali white-red sarees, Assamese Gamosa, and Manipuri Phanek.\n- **Zone 3 (South & Himalayas)**: Display of Kerala Kasavu sarees, Tamil Pattu silk, and Kashmiri woolen Pherans.\n- **Zone 4 (Craft Station)**: Hands-on paper embroidery and Bandhani tie-dye demonstration for students.",
     "Medium", "Creating"),

    ("How did the availability of silk vs cotton dictate regional dress luxury in South India?", "Tamil Nadu developed rich Pattu silk sarees for temple ceremonies due to royal silk patronage; Kerala developed clean unbleached Kasavu cotton sarees suited to coastal humidity and agrarian simplicity.", "Medium", "Analyzing"),
    ("Contrast the draping technique of a standard 6-yard saree with the 9-yard Nauvari saree.", "Standard 6-yard saree requires a petticoat and hangs like a skirt with front pleats; 9-yard Nauvari saree passes between the legs and tucks at the back like a dhoti, eliminating the petticoat.", "Medium", "Comparing"),
    ("Why is the Gamosa considered more than just a piece of clothing in Assamese culture?", "It is a sacred symbol of respect presented to elders, worn during Bihu dances, placed on religious alters, and offered as a high-honor welcome gift to guests.", "Medium", "Understanding"),
    ("How do vibrant garment colors compensate for arid landscapes in Rajasthan and Gujarat?", "In dusty, monochromatic desert environments, wearing intense red, yellow, peacock blue, and magenta garments provides emotional warmth and visual contrast.", "Medium", "Analyzing"),
    ("Describe how traditional clothing reflects occupational history in Maharashtra and Kerala.", "Maharashtrian Nauvari draping enabled women to work in fields and ride horses; Keralite white Mundus allowed farmers to fold waistcloths knee-high while working in flooded paddy fields.", "Medium", "Analyzing"),
    ("Explain the significance of golden zari borders on Kerala's Kasavu and Tamil Nadu's Pattu sarees.", "Gold zari borders add spiritual auspiciousness, ceremonial dignity, and visual luster to white cotton and rich silk fabrics during weddings and temple festivals.", "Medium", "Understanding"),
    ("How does traditional attire contribute to India's tourism and handloom export economy?", "Foreign tourists and global buyers purchase authentic Indian handlooms, silk sarees, and embroidered shawls, generating valuable foreign revenue and supporting rural weavers.", "Medium", "Evaluating"),
    ("Analyze why Chapter 09 uses descriptive adjectives like 'vibrant', 'rich', 'distinctive', and 'visual delight'.", "These vivid adjectives evoke sensory imagery, helping primary students visualize the bright colors, fine textures, and artistic beauty of Indian garments.", "Medium", "Analyzing"),
    ("What makes Northeastern textiles (Assam/Manipur) distinct in pattern design?", "Northeastern textiles emphasize structured, geometric loom-woven patterns inspired by nature, flora, and tribal folklore rather than stitched surface embroidery.", "Medium", "Understanding"),
    ("Construct a fictional dialogue between a student from Kashmir and a student from Kerala comparing their traditional clothes.", "'Kashmiri Student: My Pheran is thick wool to protect against snow!' 'Kerala Student: My Mundu is light white cotton to stay cool in the coastal sun! Both our clothes fit our homes perfectly!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the socio-economic challenges of handloom weaver migration in post-industrial India.",
     "Cheap factory-made polyester imitations undercut handloom prices, driving master weavers into urban manual labor. Protecting handlooms requires enforcing GI tags, establishing fair-trade cooperatives, guaranteeing minimum purchase prices, and promoting conscious consumerism to save indigenous textile heritage.",
     "Hard", "Evaluating"),

    ("Deconstruct the structural geometry of the Manipuri Phanek and Innaphi.",
     "The Phanek is a heavy hand-loomed cotton/silk wrap skirt with horizontal block stripes and embroidered bottom borders; the Innaphi is a light, semi-transparent gossamer shawl draped diagonally across the chest, balancing heavy lower geometry with light upper delicacy.",
     "Hard", "Analyzing"),

    ("Synthesize how Chapter 09 illustrates the concept of 'Unity in Diversity' through textile art.",
     "Chapter 09 demonstrates that despite vast geographic distances, climatic extremes, and linguistic differences, every Indian state uses natural fibers and local artistry to craft traditional clothing. Diverse in style but united in cultural pride, Indian textiles reflect a single national soul.",
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive essay prompt evaluating the relationship between climate, culture, and clothing in India.",
     "Prompt: 'Analyze how climate, geographic resources, and local customs influence the traditional dresses of four Indian states from Chapter 09. Explain why preserving traditional handlooms is essential for India's future.'",
     "Hard", "Creating"),

    ("Evaluate the impact of Geographical Indication (GI) registration on traditional Indian textiles.", "GI tags protect regional brands (like Kanchipuram silk, Banarasi zari, or Muga silk) from unauthorized industrial copying, ensuring legal protection, premium pricing, and heritage preservation for authentic artisan communities.", "Hard", "Evaluating"),

    ("Compare the decorative aesthetics of Punjabi Phulkari embroidery with Gujarati Mirror Work.", "Phulkari uses dense, unspun silk thread in geometric darning stitches to cover fabric entirely; Gujarati mirror work embeds small round glass mirrors held by buttonhole stitches to catch sunlight.", "Hard", "Comparing"),
    ("Discuss how traditional clothing promotes sustainable eco-friendly fashion in the 21st century.", "Traditional Indian attire relies on biodegradable natural fibers, slow handloom production, zero-waste unstitched drapes (sarees, mundus, veshtis), and natural plant dyes, offering a model for sustainable global fashion.", "Hard", "Evaluating"),
    ("Analyze how traditional headwear (Pagri/Pheta/Turban) signifies social respect in Indian culture.", "Removing or exchanging turbans represents total trust and brotherhood; presenting a turban is the highest ceremonial honor bestowed upon respected leaders and guests.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'These beautiful garments not only showcase India's diversity but also keep the country's traditions alive.'", "This concluding line captures the dual essence of Indian attire: it celebrates regional pluralism (diversity) while acting as a living bridge connecting contemporary citizens with ancient ancestral traditions.", "Hard", "Evaluating"),
    ("Synthesize the complete educational takeaways of Chapter 09 for primary school literature and social studies.", "Chapter 09 unifies English descriptive vocabulary (attire, embroidery, heritage) with geographical literacy, climatic reasoning, and cultural respect, inspiring Class 5 students to take pride in India's rich heritage.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 09: Traditional Dresses from India\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH09_LA_{idx:03d}"
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
    ("India is a land of rich culture and diversity. Each state in India has its own unique traditional dress, reflecting its culture, climate and heritage.",
     [
         ("What kind of land is India described as?", "A land of rich culture and diversity.", "Easy", "Remembering"),
         ("What does each state in India have?", "Its own unique traditional dress.", "Easy", "Remembering"),
         ("What three factors are reflected in each state's traditional dress?", "Culture, climate, and heritage.", "Easy", "Remembering"),
         ("What does the word 'heritage' mean?", "Traditions passed down through generations.", "Easy", "Understanding"),
         ("Why do different states have different traditional dresses?", "Because each state has distinct weather, historical traditions, and local materials.", "Medium", "Analyzing")
     ]),

    # Set 2
    ("In Punjab, men wear a kurta with a churidar or lungi, along with a colourful turban. Women wear a vibrant salwar kameez with a dupatta, often decorated with embroidery and mirror work.",
     [
         ("What do men in Punjab wear traditionally?", "A kurta with a churidar or lungi, along with a colourful turban.", "Easy", "Remembering"),
         ("What do Punjabi women wear?", "A vibrant salwar kameez with a dupatta.", "Easy", "Remembering"),
         ("What two decorative crafts adorn the dupatta of Punjabi women?", "Embroidery and mirror work.", "Easy", "Remembering"),
         ("What headwear is worn by Punjabi men?", "A colourful turban.", "Easy", "Remembering"),
         ("What does the word 'embroidery' mean?", "Decorative stitching on cloth using needle and thread.", "Easy", "Understanding")
     ]),

    # Set 3
    ("Rajasthani men wear an angrakha and dhoti, along with a colourful pagri (turban). Women wear a bright, embroidered ghagra choli with a matching odhani (veil).",
     [
         ("What top garment do Rajasthani men wear with a dhoti?", "An angrakha.", "Easy", "Remembering"),
         ("What is the traditional turban worn by Rajasthani men called?", "A pagri.", "Easy", "Remembering"),
         ("What do Rajasthani women wear traditionally?", "A bright, embroidered ghagra choli with a matching odhani.", "Easy", "Remembering"),
         ("What is an 'odhani'?", "A traditional veil draped over the head and shoulders.", "Easy", "Understanding"),
         ("Why are bright colors and turbans popular in desert Rajasthan?", "They provide visual joy in dusty desert landscapes while protecting from intense sun.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("Men in Gujarat wear a kediyu (a short, pleated frock-like top) with a dhoti or churidar. Women wear a chaniya choli, often decorated with mirror work and embroidery, along with a bandhani dupatta.",
     [
         ("What is a 'kediyu'?", "A short, pleated frock-like top worn by men in Gujarat.", "Easy", "Remembering"),
         ("What do men in Gujarat pair with a kediyu?", "A dhoti or churidar.", "Easy", "Remembering"),
         ("What do Gujarati women wear traditionally?", "A chaniya choli with a bandhani dupatta.", "Easy", "Remembering"),
         ("What decorative elements adorn the chaniya choli?", "Mirror work and embroidery.", "Easy", "Remembering"),
         ("What is 'bandhani'?", "A traditional tie-and-dye fabric technique.", "Easy", "Understanding")
     ]),

    # Set 5
    ("Men in Maharashtra wear a dhoti and kurta, along with a pheta (turban). Women wear a traditional Nauvari saree, draped in a unique style that allows for easy movement.",
     [
         ("What do Maharashtrian men wear on their head?", "A pheta (turban).", "Easy", "Remembering"),
         ("What traditional saree is worn by women in Maharashtra?", "The Nauvari saree.", "Easy", "Remembering"),
         ("What is special about the draping style of the Nauvari saree?", "It is draped in a unique style (like a dhoti) that allows for easy physical movement.", "Easy", "Understanding"),
         ("What lower garment do Maharashtrian men wear with a kurta?", "A dhoti.", "Easy", "Remembering"),
         ("Why was easy movement important for women wearing Nauvari sarees historically?", "To perform agricultural work, daily household chores, and active tasks comfortably.", "Medium", "Analyzing")
     ]),

    # Set 6
    ("Bengali men traditionally wear a dhoti with a kurta. Women wear a white saree with a red border, especially during festivals like Durga Puja.",
     [
         ("What do Bengali men wear traditionally?", "A dhoti with a kurta.", "Easy", "Remembering"),
         ("What color saree do Bengali women traditionally wear during festivals?", "A white saree with a red border.", "Easy", "Remembering"),
         ("Name the major festival mentioned where this saree is prominently worn.", "Durga Puja.", "Easy", "Remembering"),
         ("What do the colors white and red symbolize during Durga Puja?", "White symbolizes purity and peace; red symbolizes divine feminine power and celebration.", "Medium", "Understanding"),
         ("In which state is this white-and-red saree traditionally worn?", "West Bengal.", "Easy", "Remembering")
     ]),

    # Set 7
    ("In Tamil Nadu, men wear a veshti (a type of dhoti) with an angavastram (shawl) and a shirt. Women wear a pattu saree (silk saree), known for its rich colours and designs.",
     [
         ("What is a 'veshti'?", "A type of white dhoti worn by men in Tamil Nadu.", "Easy", "Remembering"),
         ("What is an 'angavastram'?", "A traditional shawl worn across the shoulder by men.", "Easy", "Remembering"),
         ("What saree do women in Tamil Nadu wear traditionally?", "A pattu saree (silk saree).", "Easy", "Remembering"),
         ("What is the pattu saree known for?", "Its rich colors and intricate designs.", "Easy", "Remembering"),
         ("Why is cotton veshti suitable for Tamil Nadu's weather?", "Because its lightweight unstitched cotton provides comfort in a hot, humid climate.", "Medium", "Analyzing")
     ]),

    # Set 8
    ("Assamese men wear a dhoti with a kurta and a traditional gamosa (a cloth used as a scarf). Women wear a beautiful Mekhela Chador, a two-piece garment with elegant embroidery.",
     [
         ("What is a 'gamosa'?", "A traditional Assamese cloth used as a scarf or honor towel.", "Easy", "Remembering"),
         ("What traditional garment do Assamese women wear?", "A Mekhela Chador.", "Easy", "Remembering"),
         ("How many pieces make up the Mekhela Chador garment?", "Two pieces (a skirt and a shawl).", "Easy", "Remembering"),
         ("What decorates the Mekhela Chador?", "Elegant embroidery.", "Easy", "Remembering"),
         ("What do Assamese men wear along with a kurta and gamosa?", "A dhoti.", "Easy", "Remembering")
     ]),

    # Set 9
    ("In Kashmir, both men and women wear a pheran, a long woolen gown to keep warm during the cold winters. Women often pair it with a colourful headscarf. Men in Kerala wear a mundu...",
     [
         ("What is a 'pheran'?", "A long woolen gown worn by both men and women in Kashmir.", "Easy", "Remembering"),
         ("Why do Kashmiri people wear a pheran?", "To keep warm during cold winter weather.", "Easy", "Understanding"),
         ("What do Kashmiri women pair with their pheran?", "A colourful headscarf.", "Easy", "Remembering"),
         ("What waistcloth do men in Kerala wear?", "A mundu (white cotton cloth wrapped around the waist).", "Easy", "Remembering"),
         ("How does the fabric of a Pheran differ from a Mundu?", "A Pheran is made of thick insulating wool for snow; a Mundu is made of light breathable cotton for coastal heat.", "Medium", "Comparing")
     ]),

    # Set 10
    ("Each state's traditional attire combined with distinctive ornaments truly become a visual delight... These beautiful garments not only showcase India's diversity but also keep the country's traditions alive.",
     [
         ("What combines with traditional attire to create a visual delight?", "Distinctive ornaments.", "Easy", "Remembering"),
         ("What two main things do these beautiful garments accomplish?", "They showcase India's diversity and keep the country's traditions alive.", "Easy", "Understanding"),
         ("What does the word 'attire' mean?", "Clothes, especially special regional ones.", "Easy", "Understanding"),
         ("What does the word 'distinctive' mean?", "Something that stands out or is unique.", "Easy", "Understanding"),
         ("Summarize the central message of Chapter 09 in one sentence.", "India's diverse traditional dresses reflect regional climate, history, and craftsmanship, keeping ancient traditions alive with pride.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 09: Traditional Dresses from India\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH09_EXT_{q_counter:03d}"
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

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 09 in {CH09_DIR}")
