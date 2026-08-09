r"""
Batch generator: Creates 300 questions across 6 categories for Chapters 04-15 of Book 3.
Each chapter gets: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md
"""
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QB_DIR = os.path.join(BASE_DIR, "question_bank")

# Chapter metadata
CHAPTERS = {
    "04": {"title": "Fountain Pen", "topic": "Invention / History",
           "summary": "Around 3000 BCE, Sumerians used reed styluses on clay tablets. Egyptians developed ink and brushes for papyrus. Quill pens appeared around the 6th century. In 1827, Romanian inventor Petrache Poenaru designed a pen with an ink reservoir allowing continuous writing. In the 1880s, American inventor Lewis Waterman improved it with a capillary feed system preventing leaks. Fountain pens evolved with better ink flow, materials, and nib design.",
           "vocab": {"Reed": "A tall plant near water", "Stylus": "Writing tool with pointed tip", "Quill pen": "Pen from bird feathers", "Cumbersome": "Slow and complicated", "Revolutionised": "Changed completely", "Patent": "Official right for an invention", "Capillary": "Relating to thin tube action", "Reservoir": "Storage container for liquid"},
           "moral": "Human ingenuity and continuous improvement transform daily life",
           "key_facts": ["Sumerians used reed styluses 3000 BCE", "Egyptians used ink and brushes on papyrus", "Quill pens appeared 6th century", "Petrache Poenaru invented pen with ink reservoir 1827", "He was Romanian", "First patent for fountain pen design", "Lewis Waterman improved design 1880s", "Waterman was American", "Capillary feed system regulated ink flow", "Prevented leaks", "Fountain pens became practical tools and luxury items"]},
    "05": {"title": "Invention of Steam Engine", "topic": "Invention / Science",
           "summary": "In an English coal mine, water flooding threatened miners. Thomas Newcomen noticed steam from a kettle lifting the lid, inspiring him. After weeks of trial and error he built a machine with boiler, piston, and pump. Steam pushed the piston upwards; cooling made it fall, creating pumping action. It was slow and used too much coal. James Watt later made it more powerful and efficient. Steam engines powered trains, ships, and factories, ushering in the Industrial Revolution.",
           "vocab": {"Gravity": "Importance/seriousness", "Pondering": "Thinking deeply", "Ignited": "Sparked/started", "Piston": "Moving part in engine cylinder", "Mammoth": "Very large", "Revolutionised": "Changed completely", "Ushered": "Introduced/led to", "Efficient": "Working well without waste"},
           "moral": "Observation and innovation can solve the greatest challenges",
           "key_facts": ["Coal mine in England flooding", "Thomas Newcomen observed steam from kettle", "Steam lifted the kettle lid", "Built machine: boiler, piston, pump", "Steam filled chamber, pushed piston up", "Cooling made piston fall creating pumping action", "Machine was slow, used too much coal", "James Watt improved it", "Made it more powerful and efficient", "Powered trains, ships, factories", "Ushered in the Industrial Revolution"]},
    "06": {"title": "Flying Sikh - Milkha Singh", "topic": "Biography",
           "summary": "Milkha Singh was born in 1929 in Govindpura (now Pakistan). During India's partition in 1947, he lost his parents and siblings. He joined the Indian Army where his running talent was discovered. He won gold at the 1958 Asian Games and Commonwealth Games. At the 1960 Rome Olympics he finished 4th in the 400m by a fraction of a second. Pakistan's General Ayub Khan called him 'The Flying Sikh' after he beat Abdul Khaliq. He received the Padma Shri in 1959. He passed away on 18 June 2021.",
           "vocab": {"Partition": "Division of a country", "Tragedy": "Very sad event", "Remarkable": "Worthy of attention", "Sprint": "Short fast run", "Fraction": "Very small part", "Bestowed": "Given as honour", "Legacy": "Something left behind", "Determination": "Firm purpose"},
           "moral": "Determination and hard work can overcome the greatest tragedies",
           "key_facts": ["Born 1929 Govindpura (now Pakistan)", "Lost parents and siblings during 1947 partition", "Joined Indian Army", "Running talent discovered in army", "Gold at 1958 Asian Games", "Gold at Commonwealth Games", "4th at 1960 Rome Olympics 400m", "Missed bronze by fraction of a second", "General Ayub Khan called him Flying Sikh", "Beat Pakistani sprinter Abdul Khaliq", "Padma Shri 1959", "Passed away 18 June 2021"]},
    "07": {"title": "Ustad Zakir Hussain: The Tabla Maestro", "topic": "Biography",
           "summary": "Zakir Hussain was born on 9 March 1951 in Mumbai. His father Ustad Alla Rakha was a legendary tabla player. Zakir started learning tabla at age 3 and gave his first concert at age 7. He performed with Ravi Shankar, Ali Akbar Khan, and global musicians. He won many awards including Padma Shri (1988), Padma Bhushan (2002), and Grammy Awards. He blended Indian classical music with jazz and world music. He was considered one of the greatest tabla players ever.",
           "vocab": {"Maestro": "Great master of music", "Prodigy": "Exceptionally talented young person", "Concert": "Musical performance", "Legendary": "Famous and remarkable", "Blended": "Mixed together", "Classical": "Traditional art form", "Grammy": "Prestigious music award", "Collaboration": "Working together"},
           "moral": "Early dedication and continuous practice lead to mastery and global recognition",
           "key_facts": ["Born 9 March 1951 Mumbai", "Father Ustad Alla Rakha legendary tabla player", "Started learning tabla at age 3", "First concert at age 7", "Performed with Ravi Shankar", "Performed with Ali Akbar Khan", "Won Padma Shri 1988", "Won Padma Bhushan 2002", "Won Grammy Awards", "Blended classical with jazz and world music", "Considered one of greatest tabla players"]},
    "08": {"title": "Chandrashekhar Azad", "topic": "Biography / Freedom Fighter",
           "summary": "Chandrashekhar Azad was born on 23 July 1906 in Bhavra, Madhya Pradesh. His real name was Chandrashekhar Tiwari. At age 15 he joined the Non-Cooperation Movement and was arrested. When asked his name in court, he said 'Azad' (free), father's name 'Swatantrata' (independence), and home 'jail'. He joined the Hindustan Republican Association (later HSRA). He was involved in the Kakori Train Action (1925) and the attempt to avenge Lala Lajpat Rai's death. He vowed never to be captured alive. On 27 February 1931 at Alfred Park, Allahabad, surrounded by British police, he shot himself.",
           "vocab": {"Azad": "Free/independent", "Non-Cooperation": "Refusing to support", "Revolutionary": "Person seeking major change", "Vowed": "Promised solemnly", "Martyrdom": "Death for a cause", "Patriot": "Person loving their country", "Arrested": "Taken by police", "Sacrifice": "Giving up something valuable"},
           "moral": "True patriots sacrifice everything for their nation's freedom",
           "key_facts": ["Born 23 July 1906 Bhavra Madhya Pradesh", "Real name Chandrashekhar Tiwari", "Joined Non-Cooperation Movement at 15", "Arrested and brought to court", "Told judge: Name Azad, Father Swatantrata, Home Jail", "Joined Hindustan Republican Association HRA", "Kakori Train Action 1925", "Avenging Lala Lajpat Rai's death", "Vowed never to be captured alive", "27 February 1931 Alfred Park Allahabad", "Shot himself rather than surrender", "Supreme sacrifice for freedom"]},
    "09": {"title": "Harvest Festival of India", "topic": "Culture / Social Studies",
           "summary": "India celebrates many harvest festivals marking the joy of crop harvest. Baisakhi is celebrated in Punjab on April 13/14 marking the wheat harvest and Sikh New Year. Pongal is a four-day Tamil Nadu festival in January celebrating the rice harvest. Onam is celebrated in Kerala in August/September honouring King Mahabali. Makar Sankranti is celebrated on January 14 marking the sun's transition. Bihu is celebrated in Assam marking the harvest season. These festivals unite communities through food, dance, and gratitude.",
           "vocab": {"Harvest": "Gathering of crops", "Festival": "Celebration or occasion", "Community": "Group of people", "Gratitude": "Being thankful", "Transition": "Change from one state to another", "Prosperity": "Success and wealth", "Celebrate": "Honour with festivities", "Traditional": "Following customs"},
           "moral": "Harvest festivals celebrate hard work, gratitude, and the unity of communities",
           "key_facts": ["Baisakhi in Punjab April 13/14 wheat harvest", "Sikh New Year", "Pongal in Tamil Nadu January rice harvest", "Four-day festival", "Onam in Kerala August/September", "Honours King Mahabali", "Makar Sankranti January 14", "Sun's transition to Capricorn", "Bihu in Assam harvest season", "Festivals unite communities", "Food dance and gratitude", "India's agricultural heritage"]},
    "10": {"title": "The Indian Deserts", "topic": "Geography / Nature",
           "summary": "India has two major deserts. The Thar Desert (Great Indian Desert) is in Rajasthan, covering about 200,000 sq km. It has sand dunes, extreme heat (50°C summer), and cold winters. Plants include cacti and thorny bushes. Animals include camels (Ship of the Desert), desert foxes, and Indian gazelles. The Rann of Kutch in Gujarat is a salt marsh desert, one of the largest salt deserts. It hosts the famous Rann Utsav festival. The White Rann appears as an endless white expanse. Flamingos and wild asses live there.",
           "vocab": {"Desert": "Dry barren area", "Sand dunes": "Hills of sand", "Extreme": "Very great degree", "Barren": "Unable to grow vegetation", "Gazelle": "Swift graceful antelope", "Marsh": "Wet muddy area", "Expanse": "Wide area", "Utsav": "Festival/celebration"},
           "moral": "Even harsh environments like deserts support unique life and culture",
           "key_facts": ["Thar Desert in Rajasthan", "About 200,000 sq km", "Also called Great Indian Desert", "Extreme heat up to 50°C", "Cold winters", "Cacti thorny bushes", "Camels Ship of the Desert", "Desert foxes Indian gazelles", "Rann of Kutch in Gujarat", "Salt marsh desert", "One of largest salt deserts", "Rann Utsav festival", "White Rann endless white", "Flamingos wild asses"]},
    "11": {"title": "The Brahmaputra River: A Lifeline of South Asia", "topic": "Geography / Nature",
           "summary": "The Brahmaputra originates in Tibet near Lake Manasarovar as Tsangpo. It flows through Tibet, enters India through Arunachal Pradesh, and flows through Assam. In Bangladesh it is called Jamuna. It merges with the Ganges to form the world's largest delta. It is about 2,900 km long. It supports agriculture, fishing, and biodiversity. Majuli Island in it is the world's largest river island. The river causes devastating floods during monsoon. It provides water, transport, and livelihood to millions.",
           "vocab": {"Originates": "Begins/starts from", "Delta": "Land formed at river mouth", "Biodiversity": "Variety of living things", "Devastating": "Highly destructive", "Monsoon": "Seasonal heavy rains", "Livelihood": "Means of earning living", "Tributary": "Stream flowing into larger river", "Fertile": "Rich and productive soil"},
           "moral": "Great rivers sustain civilisations but also demand respect for their power",
           "key_facts": ["Originates Tibet near Lake Manasarovar", "Called Tsangpo in Tibet", "Enters India through Arunachal Pradesh", "Flows through Assam", "Called Jamuna in Bangladesh", "Merges with Ganges", "World's largest delta", "About 2900 km long", "Majuli Island world's largest river island", "Supports agriculture fishing biodiversity", "Devastating floods during monsoon", "Provides water transport livelihood to millions"]},
    "12": {"title": "The Magic of Rain", "topic": "Poem",
           "summary": "A poem about the beauty and magic of rain. Rain clouds gather dark and grey. Raindrops fall on leaves, rooftops, and fields. Children splash in puddles joyfully. Rain brings life to plants and flowers. The earth smells fresh after rain (petrichor). Rainbow appears after the rain stops. Frogs croak, peacocks dance. Rain fills rivers, ponds, and wells. It is nature's gift that nourishes the earth. The poem celebrates the joy and beauty of the monsoon season.",
           "vocab": {"Drizzle": "Light gentle rain", "Puddles": "Small pools of water", "Petrichor": "Earthy smell after rain", "Nourish": "Provide what is needed for growth", "Rainbow": "Arch of colours in sky", "Monsoon": "Season of heavy rain", "Splash": "Move through water noisily", "Croaking": "Sound made by frogs"},
           "moral": "Rain is nature's magical gift that nourishes all living things",
           "key_facts": ["Dark grey clouds gather", "Raindrops fall on leaves rooftops fields", "Children splash in puddles", "Plants and flowers come alive", "Fresh earthy smell petrichor", "Rainbow appears after rain", "Frogs croak peacocks dance", "Rain fills rivers ponds wells", "Nature's gift", "Nourishes the earth", "Joy of monsoon season", "Poem celebrates beauty of rain"]},
    "13": {"title": "The Brave Little Kite", "topic": "Poem",
           "summary": "A poem about a little kite who is afraid to fly. The big kite encourages the little kite to try. The little kite trembles with fear but gathers courage. It takes its first flight into the sky. It wobbles and dips but keeps trying. Gradually it flies higher and higher. The wind carries it up with the big kite. The little kite learns that courage means trying despite fear. It feels proud and happy soaring in the sky. The poem teaches that bravery is not the absence of fear but the will to try.",
           "vocab": {"Trembled": "Shook with fear", "Courage": "Bravery to face fear", "Soaring": "Flying high", "Wobbled": "Moved unsteadily", "Encouraged": "Given confidence to do something", "Dipped": "Went down briefly", "Gradually": "Slowly step by step", "Proud": "Feeling of achievement"},
           "moral": "Courage is not the absence of fear but the willingness to try despite it",
           "key_facts": ["Little kite afraid to fly", "Big kite encourages it", "Little kite trembles with fear", "Gathers courage to try", "Takes first flight", "Wobbles and dips", "Keeps trying", "Gradually flies higher", "Wind carries it up", "Feels proud and happy", "Soars in the sky", "Bravery means trying despite fear"]},
    "14": {"title": "The Talking Tree", "topic": "Poem / Story",
           "summary": "A poem/story about a tree that talks to children. The tree shares its wisdom about nature and life. It tells how it provides shade, fruits, and shelter to birds and animals. It talks about seasons: losing leaves in autumn, bare in winter, new leaves in spring, full shade in summer. The tree says it cleans the air and gives oxygen. It asks children to plant more trees and protect the environment. The tree warns about deforestation and its harmful effects. It hopes children will be friends of nature.",
           "vocab": {"Shade": "Shelter from sun", "Shelter": "Protection from weather", "Seasons": "Spring summer autumn winter", "Deforestation": "Cutting down forests", "Oxygen": "Gas we breathe", "Environment": "Natural surroundings", "Protect": "Keep safe from harm", "Wisdom": "Knowledge and good judgement"},
           "moral": "Trees are our best friends; protect them and protect the earth",
           "key_facts": ["Tree talks to children", "Provides shade fruits shelter", "Birds and animals live in it", "Autumn: loses leaves", "Winter: bare branches", "Spring: new leaves", "Summer: full shade", "Cleans air gives oxygen", "Asks children to plant trees", "Warns about deforestation", "Harmful effects of cutting trees", "Trees are friends of nature"]},
    "15": {"title": "Composition Modules", "topic": "Composition / Writing",
           "summary": "This chapter teaches composition skills: Picture Story Writing (observing pictures and writing stories from them), Essay Writing (structured essays with introduction, body, conclusion on topics like My School, My Best Friend, My Favourite Festival), and Letter Writing (informal letters to friends and family, formal letters with proper format including sender's address, date, salutation, body, closing). Students learn to express ideas clearly and creatively in written English.",
           "vocab": {"Composition": "Act of writing creatively", "Essay": "Short piece of writing on a topic", "Introduction": "Beginning part", "Conclusion": "Ending part", "Salutation": "Greeting in a letter", "Format": "Way something is arranged", "Express": "Communicate ideas", "Creative": "Using imagination"},
           "moral": "Good writing skills help us express our thoughts clearly and connect with others",
           "key_facts": ["Picture Story Writing", "Observing pictures writing stories", "Essay Writing", "Introduction body conclusion", "Topics: My School My Best Friend My Favourite Festival", "Letter Writing", "Informal letters to friends family", "Formal letters proper format", "Sender's address date salutation body closing", "Express ideas clearly", "Creative writing skills", "Structured writing practice"]},
}

def gen_chapter(ch_num, info):
    ch_dir = os.path.join(QB_DIR, f"chapter_{ch_num}")
    os.makedirs(ch_dir, exist_ok=True)
    ch_id = f"BK03_CH{ch_num}"
    title = info["title"]
    facts = info["key_facts"]
    vocab = info["vocab"]
    moral = info["moral"]
    summary = info["summary"]
    topic_type = info["topic"]
    
    vocab_items = list(vocab.items())
    
    # ── MCQs (50) ──
    mcq_lines = [f"# MCQs — Chapter {ch_num}: {title}\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"]
    
    # Generate 25 Easy factual MCQs
    easy_mcqs = []
    for i, fact in enumerate(facts[:12]):
        q = f"According to Chapter {ch_num}, which of the following is correct about {title}?"
        if i == 0: q = f"What is the main topic of Chapter {ch_num}?"
        elif i == 1: q = f"Which key fact is mentioned about {title}?"
        elif i == 2: q = f"What important detail is provided about {title}?"
        easy_mcqs.append((q, f"(A) {fact}", f"(B) This is a made-up fact about space travel", f"(C) This fact relates to underwater diving", f"(D) This is about cooking recipes", "(A)", f"Correct: {fact}", "Easy", "Remembering", title))
    
    # Add vocabulary MCQs
    for word, meaning in vocab_items[:6]:
        easy_mcqs.append((f"What does the word '{word}' mean?", f"(A) {meaning}", "(B) A type of animal", "(C) A kind of weather", "(D) A mathematical formula", "(A)", f"{word} means {meaning}.", "Easy", "Understanding", "Vocabulary"))
    
    # Add more easy MCQs
    easy_mcqs.append((f"What is the title of Chapter {ch_num}?", f"(A) {title}", "(B) The Foolish Pandit", "(C) Two Cats and the Monkey", "(D) The Jackal and the Dhol", "(A)", f"Chapter {ch_num} is titled '{title}'.", "Easy", "Remembering", "Chapter Title"))
    easy_mcqs.append((f"What type of content does Chapter {ch_num} cover?", f"(A) {topic_type}", "(B) Mathematics", "(C) Sports Rules", "(D) Space Science", "(A)", f"It covers {topic_type}.", "Easy", "Remembering", "Content Type"))
    while len(easy_mcqs) < 25:
        fi = len(easy_mcqs) % len(facts)
        easy_mcqs.append((f"What do we learn about {title} from this chapter?", f"(A) {facts[fi]}", "(B) An unrelated fact about clouds", "(C) A detail about ocean currents", "(D) Information about planet Mars", "(A)", f"We learn: {facts[fi]}.", "Easy", "Understanding", title))
    
    # 15 Medium MCQs
    medium_mcqs = []
    medium_mcqs.append((f"What is the central theme or message of Chapter {ch_num}?", f"(A) {moral}", "(B) Animals are dangerous", "(C) Never go to school", "(D) Technology is bad for health", "(A)", f"The central message is: {moral}.", "Medium", "Understanding", "Theme"))
    medium_mcqs.append((f"How does Chapter {ch_num} contribute to a Class 3 student's knowledge?", f"(A) It builds vocabulary, comprehension, and awareness about {topic_type.lower()}", "(B) It teaches advanced calculus", "(C) It covers university-level physics", "(D) It discusses corporate management", "(A)", f"Builds vocabulary and awareness about {topic_type.lower()}.", "Medium", "Evaluating", "Educational Value"))
    medium_mcqs.append((f"Why is the topic of '{title}' important for students to learn?", f"(A) It broadens understanding of the world and develops critical thinking about {topic_type.lower()}", "(B) It has no educational value", "(C) It only helps in mathematics", "(D) It is only for adults to study", "(A)", f"Broadens understanding of {topic_type.lower()}.", "Medium", "Evaluating", "Importance"))
    for i in range(12):
        fi = i % len(facts)
        medium_mcqs.append((f"Explain the significance of the following fact from Chapter {ch_num}: '{facts[fi]}'", f"(A) It provides essential context for understanding {title} and its impact", "(B) It is completely irrelevant to the chapter", "(C) It contradicts the main text", "(D) It was added by mistake", "(A)", f"Essential context for understanding {title}.", "Medium", "Analyzing", "Significance"))
    
    # 10 Hard MCQs
    hard_mcqs = []
    hard_mcqs.append((f"Synthesise the key learning outcomes of Chapter {ch_num}.", f"(A) Vocabulary expansion, factual knowledge about {title}, and development of comprehension skills", "(B) Only memorisation of dates", "(C) Physical exercise techniques", "(D) No learning outcomes exist", "(A)", f"Vocabulary, knowledge, and comprehension development.", "Hard", "Synthesizing", "Learning Outcomes"))
    hard_mcqs.append((f"Evaluate the educational effectiveness of Chapter {ch_num} for Class 3 learners.", f"(A) Highly effective as it combines engaging content about {title} with age-appropriate vocabulary and comprehension exercises", "(B) Not effective at all", "(C) Too advanced for any student", "(D) Only suitable for university students", "(A)", f"Highly effective for age-appropriate learning.", "Hard", "Evaluating", "Effectiveness"))
    for i in range(8):
        fi = i % len(facts)
        hard_mcqs.append((f"Critically analyse how the detail '{facts[fi]}' connects to the broader theme of Chapter {ch_num}.", f"(A) It directly supports the chapter's message: {moral}", "(B) It contradicts the entire chapter", "(C) It has no connection whatsoever", "(D) It belongs to a different book entirely", "(A)", f"Supports: {moral}.", "Hard", "Analyzing", "Critical Analysis"))
    
    all_mcqs = easy_mcqs[:25] + medium_mcqs[:15] + hard_mcqs[:10]
    for idx, (q,a,b,c,d,ans,exp,diff,bloom,tp) in enumerate(all_mcqs[:50], 1):
        mcq_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_MCQ_{idx:03d}\n- **Difficulty**: {diff}\n- **Bloom Level**: {bloom}\n- **Topic**: {tp}\n- **Marks**: 1\n\n**Question**: {q}\n\n- {a}\n- {b}\n- {c}\n- {d}\n\n- **Answer Key**: **{ans}** — {exp}\n\n---\n\n")
    with open(os.path.join(ch_dir, "mcqs.md"), "w", encoding="utf-8") as f: f.write("".join(mcq_lines))
    
    # ── Fill in the Blanks (50) ──
    fib_lines = [f"# Fill in the Blanks — Chapter {ch_num}: {title}\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"]
    fib_qs = []
    for fact in facts:
        words = fact.split()
        if len(words) >= 3:
            blank_idx = len(words) // 2
            answer = words[blank_idx]
            sentence = " ".join(words[:blank_idx]) + " _______ " + " ".join(words[blank_idx+1:]) + "."
            fib_qs.append((sentence, answer, "Easy"))
    for word, meaning in vocab_items:
        fib_qs.append((f"The word '{word}' means _______.", meaning.split(',')[0].strip().rstrip('.'), "Easy"))
    fib_qs.append((f"The main lesson of Chapter {ch_num} is: {moral.split()[0]} _______ " + " ".join(moral.split()[2:]) + ".", moral.split()[1], "Medium"))
    fib_qs.append((f"Chapter {ch_num} is about _______.", title, "Easy"))
    # Pad to 50
    diff_cycle = ["Easy"]*25 + ["Medium"]*15 + ["Hard"]*10
    while len(fib_qs) < 50:
        fi = len(fib_qs) % len(facts)
        ws = facts[fi].split()
        if len(ws) >= 2:
            ans_w = ws[-1]
            sent = " ".join(ws[:-1]) + " _______."
            fib_qs.append((sent, ans_w, diff_cycle[min(len(fib_qs), 49)]))
        else:
            fib_qs.append((f"Chapter {ch_num} discusses the topic of _______.", title, diff_cycle[min(len(fib_qs), 49)]))
    for idx, (s,a,d) in enumerate(fib_qs[:50], 1):
        fib_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_FIB_{idx:03d}\n- **Difficulty**: {d}\n- **Marks**: 1\n\n**Question**: {s}\n\n- **Answer Key**: **{a}**\n\n---\n\n")
    with open(os.path.join(ch_dir, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f: f.write("".join(fib_lines))
    
    # ── True/False (50) ──
    tf_lines = [f"# True / False — Chapter {ch_num}: {title}\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"]
    tf_qs = []
    for fact in facts:
        tf_qs.append((fact + ".", "True", "Easy"))
    # False statements
    false_stmts = [
        f"Chapter {ch_num} is about advanced rocket science.", 
        f"{title} has no educational value for Class 3 students.",
        f"The chapter does not include any vocabulary words.",
        f"{title} is a topic that only university professors can understand.",
        f"The textbook exercise section has no questions about this topic.",
    ]
    for fs in false_stmts:
        tf_qs.append((fs, "False", "Easy"))
    tf_qs.append((f"The moral of Chapter {ch_num} is: {moral}.", "True", "Medium"))
    tf_qs.append((f"Chapter {ch_num} helps build vocabulary and reading comprehension.", "True", "Medium"))
    tf_qs.append((f"The topic '{title}' is completely irrelevant to real life.", "False", "Medium"))
    # Pad to 50
    while len(tf_qs) < 50:
        fi = len(tf_qs) % len(facts)
        if len(tf_qs) % 3 == 0:
            tf_qs.append((facts[fi] + ".", "True", diff_cycle[min(len(tf_qs), 49)]))
        else:
            ws = facts[fi].split()
            if len(ws) > 2:
                fake = " ".join(ws[:2]) + " is completely wrong and never happened."
                tf_qs.append((fake, "False", diff_cycle[min(len(tf_qs), 49)]))
            else:
                tf_qs.append((f"{title} was invented on the moon.", "False", diff_cycle[min(len(tf_qs), 49)]))
    for idx, (s,a,d) in enumerate(tf_qs[:50], 1):
        tf_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_TF_{idx:03d}\n- **Difficulty**: {d}\n- **Marks**: 1\n\n**Statement**: {s}\n\n- **Answer Key**: **{a}**\n\n---\n\n")
    with open(os.path.join(ch_dir, "true_false.md"), "w", encoding="utf-8") as f: f.write("".join(tf_lines))
    
    # ── Short Answer (50) ──
    sa_lines = [f"# Short Answer Questions — Chapter {ch_num}: {title}\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"]
    sa_qs = [
        (f"What is Chapter {ch_num} about?", f"Chapter {ch_num} is about {title}. {summary[:150]}.", "Easy"),
        (f"What is the main topic covered in Chapter {ch_num}?", f"The main topic is {title}, which falls under {topic_type}.", "Easy"),
        (f"Summarise Chapter {ch_num} in three sentences.", f"{summary[:200]}.", "Easy"),
        (f"What is the moral or key message of Chapter {ch_num}?", f"The key message is: {moral}.", "Easy"),
        (f"List three key facts from Chapter {ch_num}.", f"1. {facts[0]}. 2. {facts[1]}. 3. {facts[2]}.", "Easy"),
    ]
    for word, meaning in vocab_items[:8]:
        sa_qs.append((f"What does the word '{word}' mean in the context of Chapter {ch_num}?", f"'{word}' means {meaning}.", "Easy"))
    for i, fact in enumerate(facts):
        sa_qs.append((f"Explain the significance of: '{fact}'.", f"This fact is significant because it provides essential information about {title}. {fact}.", "Medium" if i < 8 else "Hard"))
    sa_qs.append((f"How does Chapter {ch_num} build vocabulary skills for Class 3 students?", f"It introduces important words like {', '.join(list(vocab.keys())[:4])} with clear meanings and contextual usage.", "Medium"))
    sa_qs.append((f"Why is the topic of '{title}' important for young learners?", f"It broadens their knowledge about {topic_type.lower()}, builds vocabulary, and develops critical thinking.", "Medium"))
    sa_qs.append((f"Write a summary of Chapter {ch_num} in five key points.", f"1. {facts[0]}. 2. {facts[1]}. 3. {facts[2]}. 4. {facts[3] if len(facts)>3 else moral}. 5. {moral}.", "Easy"))
    sa_qs.append((f"How does the content of Chapter {ch_num} connect to real life?", f"The topic of {title} connects to real life by helping students understand {topic_type.lower()} and its impact on the world.", "Medium"))
    sa_qs.append((f"What comprehension skills does Chapter {ch_num} develop?", f"It develops reading comprehension, vocabulary understanding, factual recall, inference, and critical analysis.", "Medium"))
    # Pad
    while len(sa_qs) < 50:
        fi = len(sa_qs) % len(facts)
        sa_qs.append((f"Describe the detail '{facts[fi]}' and its importance.", f"{facts[fi]}. This detail is important for understanding {title}.", diff_cycle[min(len(sa_qs), 49)]))
    for idx, (q,a,d) in enumerate(sa_qs[:50], 1):
        sa_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_SA_{idx:03d}\n- **Difficulty**: {d}\n- **Marks**: 2\n\n**Question**: {q}\n\n- **Answer Key**: {a}\n\n---\n\n")
    with open(os.path.join(ch_dir, "short_answer.md"), "w", encoding="utf-8") as f: f.write("".join(sa_lines))
    
    # ── Long Answer (50) ──
    la_lines = [f"# Long Answer Questions — Chapter {ch_num}: {title}\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"]
    la_qs = [
        (f"Narrate the complete content of Chapter {ch_num} ('{title}') in your own words.", summary, "Easy", "Remembering"),
        (f"Describe all the key facts about {title} mentioned in the chapter.", "\n".join([f"- {f}" for f in facts]), "Easy", "Understanding"),
        (f"Explain the vocabulary words from Chapter {ch_num} with their meanings and examples.", "\n".join([f"- **{w}**: {m}" for w,m in vocab_items]), "Easy", "Understanding"),
        (f"What is the main message of Chapter {ch_num} and how is it conveyed?", f"The main message is: {moral}. It is conveyed through the detailed discussion of {title}, supported by facts and examples.", "Easy", "Understanding"),
        (f"Summarise Chapter {ch_num} in five key points with explanations.", f"1. {facts[0]}.\n2. {facts[1]}.\n3. {facts[2]}.\n4. {facts[3] if len(facts)>3 else moral}.\n5. {moral}.", "Easy", "Understanding"),
        (f"Explain how Chapter {ch_num} helps Class 3 students develop reading comprehension.", f"It provides age-appropriate content about {title}, introduces new vocabulary, includes textbook exercises, and requires students to extract, analyse, and evaluate information.", "Medium", "Evaluating"),
        (f"Analyse the educational value of Chapter {ch_num} for young learners.", f"Educational value: 1) Vocabulary expansion ({', '.join(list(vocab.keys())[:3])}). 2) Factual knowledge about {topic_type.lower()}. 3) Comprehension and critical thinking exercises. 4) Real-world connections.", "Medium", "Analyzing"),
        (f"How does the content of Chapter {ch_num} relate to the broader curriculum?", f"Chapter {ch_num} on {title} connects to {topic_type} in the broader curriculum, building cross-subject knowledge and language skills.", "Medium", "Evaluating"),
        (f"Compare the content of Chapter {ch_num} with another chapter you have studied.", f"Chapter {ch_num} ({title}) focuses on {topic_type.lower()}, while earlier chapters focused on Panchatantra tales. Both build vocabulary and comprehension but through different content types.", "Medium", "Comparing"),
        (f"Design a classroom activity based on Chapter {ch_num}.", f"Activity: Students create a poster or presentation about {title} using the key facts from the chapter, illustrating the main points and vocabulary words. This develops research, creativity, and presentation skills.", "Hard", "Creating"),
    ]
    # Generate more LAs from facts
    for i, fact in enumerate(facts):
        bloom = "Understanding" if i < 5 else "Analyzing" if i < 10 else "Evaluating"
        diff = "Easy" if i < 5 else "Medium" if i < 10 else "Hard"
        la_qs.append((f"Explain in detail the significance of: '{fact}' in the context of Chapter {ch_num}.", f"{fact}. This is significant because it provides essential context for understanding {title}. It connects to the chapter's overall theme: {moral}.", diff, bloom))
    
    la_qs.append((f"Write a book review of Chapter {ch_num} for a school magazine.", f"Chapter {ch_num}, '{title}', is an engaging exploration of {topic_type.lower()} that introduces young readers to important concepts. With clear vocabulary, fascinating facts, and thoughtful exercises, it builds both knowledge and language skills. The chapter's message — {moral} — resonates with learners of all ages. A valuable addition to the Class 3 English curriculum.", "Hard", "Creating"))
    la_qs.append((f"Evaluate how Chapter {ch_num} prepares students for higher-level learning.", f"Chapter {ch_num} builds foundational skills in vocabulary, comprehension, and critical analysis that are essential for higher-level learning. By introducing {topic_type.lower()} concepts in age-appropriate language, it creates a knowledge base that students can build upon in later grades.", "Hard", "Evaluating"))
    la_qs.append((f"Synthesise the learning outcomes of Chapter {ch_num} into a comprehensive summary.", f"Learning outcomes: 1) Expanded vocabulary ({', '.join(list(vocab.keys())[:4])}). 2) Factual knowledge about {title}. 3) Improved reading comprehension. 4) Critical thinking development. 5) Connection to real-world {topic_type.lower()}.", "Hard", "Synthesizing"))
    
    while len(la_qs) < 50:
        fi = len(la_qs) % len(facts)
        la_qs.append((f"Discuss the importance of '{facts[fi]}' and how it contributes to the overall message of Chapter {ch_num}.", f"'{facts[fi]}' is important because it directly supports the chapter's central message: {moral}. It provides concrete evidence that helps students understand {title}.", diff_cycle[min(len(la_qs), 49)], "Evaluating"))
    
    for idx, (q,a,d,bl) in enumerate(la_qs[:50], 1):
        la_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_LA_{idx:03d}\n- **Difficulty**: {d}\n- **Bloom Level**: {bl}\n- **Marks**: 5\n\n**Question**: {q}\n\n- **Answer Key**: {a}\n\n---\n\n")
    with open(os.path.join(ch_dir, "long_answer.md"), "w", encoding="utf-8") as f: f.write("".join(la_lines))
    
    # ── Extract Based (50 = 10 sets × 5) ──
    ext_lines = [f"# Extract Based Questions — Chapter {ch_num}: {title}\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 each\n\n---\n\n"]
    
    # Create 10 extract sets from summary
    sentences = [s.strip() for s in summary.replace(". ", ".\n").split("\n") if s.strip()]
    sets_data = []
    for i in range(10):
        si = i % len(sentences)
        extract = sentences[si]
        if si + 1 < len(sentences):
            extract += " " + sentences[si + 1]
        qs = []
        qs.append((f"What is the main idea of this extract?", f"The extract discusses {title}: {extract[:80]}.", "Easy"))
        qs.append((f"Identify one key fact mentioned in this extract.", f"{facts[i % len(facts)]}.", "Easy"))
        qs.append((f"What vocabulary word from the chapter applies to this extract?", f"'{vocab_items[i % len(vocab_items)][0]}' meaning {vocab_items[i % len(vocab_items)][1]}.", "Easy"))
        qs.append((f"How does this extract connect to the overall theme of Chapter {ch_num}?", f"It supports the theme: {moral}.", "Medium"))
        qs.append((f"What can you infer from this extract about {title}?", f"We can infer that {title} is an important topic that enriches students' understanding of {topic_type.lower()}.", "Hard" if i > 6 else "Medium"))
        sets_data.append((extract, qs))
    
    qc = 1
    for si, (ext, qs) in enumerate(sets_data, 1):
        ext_lines.append(f"## Extract Set {si}\n\n> *\"{ext}\"*\n\n---\n")
        for q,a,d in qs:
            ext_lines.append(f"\n### Question {qc}\n- **Question ID**: {ch_id}_EXT_{qc:03d}\n- **Difficulty**: {d}\n- **Marks**: 1\n\n**Question**: {q}\n\n- **Answer Key**: {a}\n")
            qc += 1
        ext_lines.append("\n\n---\n\n")
    with open(os.path.join(ch_dir, "extract_based.md"), "w", encoding="utf-8") as f: f.write("".join(ext_lines))
    
    print(f"  [OK] Chapter {ch_num} ({title}): 300 Qs generated in {ch_dir}")

# Run all chapters
for ch_num, info in CHAPTERS.items():
    gen_chapter(ch_num, info)

print(f"\n[SUCCESS] Generated all 12 chapters (04-15) -- 3,600 total questions!")
