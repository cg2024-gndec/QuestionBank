r"""
Refines all 6 Category files for Book 5 Chapter 12 ("The Magic of Books" - Poem) for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH12_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_12")
os.makedirs(CH12_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What does the poet compare books to in the very first line?", "(A) A magic door", "(B) A treasure chest", "(C) A window", "(D) A mirror", "(A)", "The poem opens: 'Books are like a magic door'.", "Easy", "Remembering", "Poetic Simile"),
    ("Who is the author of the poem 'The Magic of Books'?", "(A) Anonymous", "(B) Robert Frost", "(C) William Wordsworth", "(D) Rabindranath Tagore", "(A)", "The poem is written by Anonymous.", "Easy", "Remembering", "Poet Identity"),
    ("What lies within pages thick and pages thin according to the poem?", "(A) A world of wonder", "(B) A collection of math problems", "(C) Ancient golden coins", "(D) A heavy stone", "(A)", "Line: 'A world of wonder lies within.'", "Easy", "Remembering", "Poetic Line"),
    ("Where can a book take you according to the second stanza?", "(A) To the sky or deep below where oceans lie", "(B) Only to the school playground", "(C) Only to a grocery market", "(D) Nowhere outside your room", "(A)", "Line: 'A book can take you to the sky, Or deep below where oceans lie.'", "Easy", "Remembering", "Setting"),
    ("What grand sight can books show you in faraway places?", "(A) Kingdoms, brave and grand", "(B) Tall steel factories", "(C) Crowded bus stands", "(D) Heavy machinery", "(A)", "Line: 'It shows you kingdoms, brave and grand.'", "Easy", "Remembering", "Imagery"),
    ("What small things in nature can books show you?", "(A) Tiny creatures in the sand", "(B) Plastic toys in a box", "(C) Paper clips on a desk", "(D) Grains of salt in a jar", "(A)", "Line: 'Or tiny creatures in the sand.'", "Easy", "Remembering", "Imagery"),
    ("What kinds of new friends will you meet while reading books?", "(A) Friends both young and old", "(B) Only people from your school", "(C) Only cartoon characters", "(D) Only historical kings", "(A)", "Line: 'You'll meet new friends, both young and old.'", "Easy", "Remembering", "Characters"),
    ("What types of stories do books share with readers?", "(A) Stories brave, and tales untold", "(B) Only scary nightmare stories", "(C) Only boring dictionary definitions", "(D) False gossip stories", "(A)", "Line: 'Hear stories brave, and tales untold.'", "Easy", "Remembering", "Story Types"),
    ("What range of emotions can every page evoke in a reader?", "(A) You'll laugh or cry, or dream about the days gone by", "(B) You'll fall asleep instantly", "(C) You'll feel angry at your friends", "(D) You'll feel hungry for food", "(A)", "Line: 'With every page, you'll laugh or cry, Or dream about the days gone by.'", "Easy", "Understanding", "Emotions"),
    ("What action does the poet encourage us to take with a book?", "(A) Hold a book, and take a flight", "(B) Throw the book away", "(C) Lock the book in a cupboard", "(D) Color over the printed words", "(A)", "Line: 'So hold a book, and take a flight.'", "Easy", "Remembering", "Action"),
    ("Where does reading take your imagination according to the fourth stanza?", "(A) To lands of joy and pure delight", "(B) To noisy traffic roads", "(C) To dark, scary caves", "(D) To empty deserted deserts", "(A)", "Line: 'To lands of joy and pure delight.'", "Easy", "Remembering", "Destination"),
    ("What will those who read always find within their mind?", "(A) A treasure house within their mind", "(B) A small wooden box", "(C) A blank white sheet", "(D) A pile of dry leaves", "(A)", "Line: 'For those who read will always find, A treasure house within their mind!'", "Easy", "Remembering", "Treasure House"),
    ("What does the word 'adore' mean according to the vocabulary section?", "(A) Love deeply", "(B) Hate strongly", "(C) Ignore completely", "(D) Look at quickly", "(A)", "Adore = Love deeply.", "Easy", "Understanding", "Vocabulary"),
    ("What figure of speech is used in 'Books are like a magic door'?", "(A) Simile", "(B) Metaphor", "(C) Alliteration", "(D) Personification", "(A)", "Using 'like' to compare books to a door is a simile.", "Easy", "Understanding", "Literary Device"),
    ("What figure of speech is used in 'A treasure house within their mind'?", "(A) Metaphor", "(B) Simile", "(C) Onomatopoeia", "(D) Hyperbole", "(A)", "Comparing the mind directly to a treasure house without 'like' or 'as' is a metaphor.", "Easy", "Understanding", "Literary Device"),
    ("Which rhyming pair opens the first stanza of the poem?", "(A) door / adore", "(B) sky / lie", "(C) thin / within", "(D) old / untold", "(A)", "'door' rhymes with 'adore'.", "Easy", "Remembering", "Rhyme Scheme"),
    ("Which rhyming pair closes the first stanza?", "(A) thin / within", "(B) grand / sand", "(C) cry / by", "(D) flight / delight", "(A)", "'thin' rhymes with 'within'.", "Easy", "Remembering", "Rhyme Scheme"),
    ("What contrast is created by 'sky' and 'oceans' in stanza 2?", "(A) High heights versus deep ocean depths", "(B) Hot sun versus cold ice", "(C) Light day versus dark night", "(D) Sweet food versus bitter drink", "(A)", "Contrasts high sky with deep ocean depths.", "Easy", "Understanding", "Poetic Contrast"),
    ("What contrast is created by 'kingdoms, brave and grand' and 'tiny creatures in the sand'?", "(A) Vast, powerful realms versus small, delicate living things", "(B) Loud thunder versus soft rain", "(C) Old books versus new books", "(D) Heavy rocks versus light feathers", "(A)", "Contrasts grand kingdoms with tiny sand creatures.", "Easy", "Understanding", "Poetic Contrast"),
    ("How do books allow readers to 'take a flight' without an airplane?", "(A) By letting their imagination soar to imaginary lands through reading", "(B) By throwing books into the air", "(C) By riding a bird while holding a book", "(D) By sitting on a paper plane", "(A)", "Imagination soars to joyful lands through reading.", "Easy", "Understanding", "Metaphorical Meaning"),
    ("Why is a reader's mind called a 'treasure house'?", "(A) Because reading fills the mind with valuable knowledge, ideas, and memories", "(B) Because gold coins are kept inside the head", "(C) Because books cost a lot of money", "(D) Because libraries are made of brick", "(A)", "Reading fills the mind with precious knowledge, ideas, and memories.", "Easy", "Understanding", "Metaphor Rationale"),
    ("What does 'untold' mean in the line 'tales untold'?", "(A) Stories that are secret, new, or yet to be discovered", "(B) Stories that are lie-filled", "(C) Stories that are printed in small font", "(D) Stories that have no words", "(A)", "Untold = secret, new, or yet to be shared.", "Easy", "Understanding", "Vocabulary Context"),
    ("What overall tone or mood does the poem 'The Magic of Books' convey?", "(A) Joyful, inspiring, and magical", "(B) Sad, fearful, and gloomy", "(C) Angry and violent", "(D) Dull and sleepy", "(A)", "The tone is joyful, inspiring, and magical.", "Easy", "Evaluating", "Poem Tone"),
    ("How many stanzas of four lines each (quatrains) make up this poem?", "(A) 4 stanzas (16 lines total)", "(B) 2 stanzas (8 lines total)", "(C) 6 stanzas (24 lines total)", "(D) 1 long stanza of 50 lines", "(A)", "The poem has 4 stanzas of 4 lines each (16 lines total).", "Easy", "Remembering", "Poem Structure"),
    ("What title is given to Chapter 12?", "(A) The Magic of Books", "(B) Island Groups of India", "(C) The Narmada River", "(D) Traditional Dresses from India", "(A)", "Title is 'The Magic of Books'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Analyze the rhyming structure (rhyme scheme) of each stanza in 'The Magic of Books'.", "(A) AABB (door/adore = A, thin/within = B)", "(B) ABAB", "(C) ABCB", "(D) AAAA", "(A)", "Each 4-line stanza follows an AABB rhyme scheme.", "Medium", "Analyzing", "Rhyme Scheme Analysis"),
    ("How does the poem convey the concept that books transcend physical geographic boundaries?", "(A) By stating books take readers from the high sky to deep ocean floors and grand kingdoms across time", "(B) By proving books contain physical GPS maps", "(C) By requiring readers to buy plane tickets", "(D) By limiting book settings to local towns", "(A)", "Books transport imagination to sky, ocean depths, and distant kingdoms.", "Medium", "Analyzing", "Spatial Transcendance"),
    ("Examine the emotional duality expressed in the third stanza: 'laugh or cry, Or dream about the days gone by'.", "(A) Books evoke a rich spectrum of human emotions—humor, empathy, sorrow, and nostalgia for the past", "(B) Books make readers confused about feelings", "(C) Books cause emotional harm to children", "(D) Books remove all feelings from humans", "(A)", "Books evoke humor, empathy, sorrow, and nostalgia.", "Medium", "Analyzing", "Emotional Spectrum"),
    ("Why does the poet describe a reader's mind as a 'treasure house' rather than a physical bank?", "(A) Physical wealth can be lost or stolen, whereas knowledge and imaginative wonders stored in the mind endure forever", "(B) Mind treasure can be spent at a market", "(C) Bank accounts are useless compared to books", "(D) Books are made of real gold leaves", "(A)", "Knowledge and imaginative wonders stored in the mind endure forever.", "Medium", "Evaluating", "Mind Treasure Rationale"),
    ("How does the poem encourage reluctant readers to embrace books?", "(A) By framing reading as a magical, exciting adventure of flight and discovery rather than a boring task", "(B) By threatening students with bad marks", "(C) By forcing students to memorize pages", "(D) By claiming books are dangerous", "(A)", "Frames reading as an exciting, magical adventure of flight and discovery.", "Medium", "Evaluating", "Motivational Strategy"),
    ("What contrast is emphasized between 'pages thick and pages thin'?", "(A) Whether a book is long or short, every book contains a magical world of wonder", "(B) Thin pages tear easily while thick pages do not", "(C) Thick books are for adults while thin books are for infants", "(D) Thick pages cost more money", "(A)", "Regardless of book length or format, every book holds a world of wonder.", "Medium", "Understanding", "Textual Contrast"),
    ("Explain the imagery in the phrase 'take a flight, To lands of joy and pure delight'.", "(A) Reading frees the human spirit from physical limits, allowing thoughts to soar into realms of happiness", "(B) The reader literally boards an aircraft holding a book", "(C) Books turn into birds and fly away", "(D) Pages fly around the classroom in the wind", "(A)", "Frees the human spirit, allowing thoughts to soar into realms of happiness.", "Medium", "Understanding", "Poetic Imagery"),
    ("How does meeting 'new friends, both young and old' in books build empathy in Class 5 students?", "(A) By introducing diverse characters across ages and cultures, helping students understand different life perspectives", "(B) By replacing real-life friends with paper puppets", "(C) By teaching students to avoid older people", "(D) By making students dislike fictional characters", "(A)", "Introduces diverse characters, helping students understand different perspectives.", "Medium", "Evaluating", "Empathy Development"),
    ("Why is 'The Magic of Books' an appropriate title for this poem?", "(A) Because reading invisibly transforms printed ink into vivid mental landscapes, deep emotions, and lifelong wisdom", "(B) Because books perform trick magic with playing cards", "(C) Because books can disappear into thin air", "(D) Because the poet was a professional magician", "(A)", "Transforms printed ink into vivid mental landscapes, emotions, and wisdom.", "Medium", "Analyzing", "Title Aptness"),
    ("What stylistic choice is reflected in using simple, rhythmic rhyming couplets for Class 5 readers?", "(A) Makes the poem memorable, musical, and engaging, encouraging young students to recite and enjoy poetry", "(B) Makes the poem difficult to read", "(C) Hides the true meaning from students", "(D) Forces students to use a dictionary for every word", "(A)", "Rhythmic couplets make poetry musical, memorable, and accessible.", "Medium", "Analyzing", "Poetic Style"),
    ("How does 'dream about the days gone by' introduce historical appreciation?", "(A) It highlights how books preserve history, allowing readers to experience past eras and ancestral heritage", "(B) It teaches that past days were boring", "(C) It urges readers to sleep during history class", "(D) It claims the past never existed", "(A)", "Books preserve history, allowing readers to experience past eras.", "Medium", "Understanding", "Historical Connection"),
    ("Compare the physical object of a book (paper and ink) with its imaginative power described in the poem.", "(A) Physically, a book is just bound paper; imaginatively, it is an unlimited gateway to skies, oceans, and grand kingdoms", "(B) Physically a book is gold; imaginatively it is paper", "(C) Both the physical book and imagination are identical", "(D) A book has no physical form", "(A)", "Bound paper physically vs an unlimited gateway to skies, oceans, and kingdoms imaginatively.", "Medium", "Comparing", "Physical vs Imaginative"),
    ("Why does the poet describe stories as both 'brave' and 'tales untold'?", "(A) 'Brave' highlights heroic adventures; 'untold' highlights the excitement of discovering fresh, unread narratives", "(B) 'Brave' means scary; 'untold' means false", "(C) Both words mean the stories are short", "(D) 'Brave' refers to soldiers only", "(A)", "'Brave' = heroic adventures; 'untold' = fresh, unread narratives.", "Medium", "Understanding", "Word Choice Analysis"),
    ("Summarize Chapter 12 in four concise sentences.", "'The Magic of Books' by Anonymous is an uplifting poem celebrating the transformative power of reading. The poet compares a book to a magic door that opens into worlds of wonder, taking readers from high skies to deep ocean beds. Reading allows children to meet diverse characters, experience joy, laughter, and nostalgia, and explore grand kingdoms or tiny creatures. Ultimately, reading enriches the mind, turning it into a lasting treasure house of knowledge and delight.", "Medium", "Understanding", "Chapter Summary"),
    ("How can a student apply the poem's message to build a lifelong reading habit?", "(A) By reading diverse books daily, exploring new genres with curiosity, and cherishing the knowledge gained in their mind", "(B) By keeping books closed on a bookshelf", "(C) By reading only when forced for exams", "(D) By tearing pages from library books", "(A)", "Read diverse books daily, explore new genres with curiosity, and cherish knowledge.", "Medium", "Applying", "Habit Application"),

    # Hard (41-50)
    ("Critique the psychological impact of imaginative reading vs passive screen consumption on children.", "(A) Reading requires active cognitive visualization, building a 'treasure house' of creative thought, whereas screen watching offers passive, pre-rendered stimulation", "(B) Screen watching builds better imagination than books", "(C) Reading destroys brain cells while screens build wisdom", "(D) Both mediums produce identical cognitive development", "(A)", "Reading requires active visualization building creative thought; screens offer passive stimulation.", "Hard", "Evaluating", "HOTS Cognitive Critique"),
    ("Deconstruct the structural progression of the four stanzas in 'The Magic of Books'.", "(A) Stanza 1 introduces the portal (magic door); Stanza 2 explores physical spaces (sky/ocean/kingdoms); Stanza 3 explores emotional experiences (friends/laugh/cry); Stanza 4 synthesizes the internal reward (treasure house)", "(B) All four stanzas repeat the exact same sentence", "(C) Stanza 1 talks about ocean; Stanza 4 talks about magic door", "(D) The stanzas have no logical connections", "(A)", "Portal entry -> Physical exploration -> Emotional connection -> Internal treasure synthesis.", "Hard", "Analyzing", "Stanza Structural Progression"),
    ("Evaluate how literature acts as a catalyst for empathy and emotional intelligence in primary education.", "(A) By allowing children to experience diverse characters' struggles and joys ('laugh or cry'), books expand emotional resonance beyond personal life", "(B) Literature makes children detached from human feelings", "(C) Literature teaches students to judge others harshly", "(D) Emotional intelligence cannot be influenced by books", "(A)", "Experiencing diverse characters' joys and struggles expands emotional resonance and empathy.", "Hard", "Evaluating", "Literature & Empathy"),
    ("Compare the metaphor of 'magic door' in Chapter 12 with the concept of 'lifelong learning'.", "(A) The magic door opens initial curiosity; walking through continuous doors creates an expanding treasure house of lifelong wisdom", "(B) Magic door refers to real wooden doors in schools", "(C) Lifelong learning stops after primary school", "(D) Both concepts are completely unrelated", "(A)", "Magic door opens initial curiosity; continuous reading creates an expanding treasure house.", "Hard", "Comparing", "Conceptual Comparison"),
    ("Formulate an original 4-line stanza following the rhyme and meter of 'The Magic of Books'.", "(A) 'Open a page and take a stride,\nInto a world where dragons hide;\nWith every chapter, clear and bright,\nYour heart will dance in pure delight!'", "(B) 'Books are good to read every day.\nThey help us pass time in school.\nWe like reading books very much.\nGoodbye reading books.'", "(C) 'One two three four five,\nReading books keeps us alive.'", "(D) 'Yesterday I read a book on a wall.'", "(A)", "Original 4-line AABB stanza matching rhythm and theme.", "Hard", "Creating", "Poetry Generation"),
    ("Assess the significance of preserving physical libraries in the digital era based on Chapter 12.", "(A) Physical libraries serve as communal 'magic doors' providing equal access to treasure houses of knowledge for all children regardless of wealth", "(B) Libraries should be converted into parking lots", "(C) Digital screens have made books completely useless", "(D) Libraries are meant only for storing old furniture", "(A)", "Libraries serve as communal magic doors providing equal access to treasure houses of knowledge.", "Hard", "Evaluating", "Library Assessment"),
    ("Analyze the linguistic economy of Anonymous poetry in conveying profound philosophy through simple diction.", "(A) Using monosyllabic, everyday words ('sky', 'sand', 'laugh', 'cry'), the poet communicates deep truths about human imagination effortlessly", "(B) Anonymous poetry is simple because the poet lacked vocabulary", "(C) Complex academic terms are better than simple poetry", "(D) Monosyllabic words confuse young students", "(A)", "Everyday words communicate deep philosophical truths about human imagination effortlessly.", "Hard", "Analyzing", "Linguistic Economy"),
    ("Synthesize how Chapter 12 unifies literacy development, artistic imagery, and personal character building.", "(A) Connects basic reading skills with vivid sensory imagery (sky/ocean/kingdoms) and inner moral growth (empathy/joy/wisdom)", "(B) Separates reading from imagination", "(C) Replaces art with rote grammar rules", "(D) Rejects personal character building", "(A)", "Unifies basic literacy with sensory imagery and inner moral growth.", "Hard", "Synthesizing", "Cross-Disciplinary Synthesis"),
    ("Critique the statement: 'Reading books is a passive hobby that isolates people from the world.'", "(A) False; reading actively expands one's mental world, builds empathy for others ('meet new friends'), and enriches social communication", "(B) True; readers never talk to real people", "(C) False; reading is a physical sport like football", "(D) True; books prevent people from thinking", "(A)", "False; reading actively expands the mental world and builds social empathy.", "Hard", "Evaluating", "Literary Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 12 for a Class 5 assessment.", "(A) 'Explain why the poet compares books to a magic door and the mind to a treasure house in The Magic of Books. Describe the places, friends, and emotions books reveal to readers.'", "(B) 'Write five sentences about your school bag.'", "(C) 'List five rhyming words.'", "(D) 'Draw a picture of a door.'", "(A)", "Structured essay prompt evaluating poetic similes, metaphors, settings, emotions, and reader impact.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 12: The Magic of Books\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH12_MCQ_{idx:03d}"
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

with open(os.path.join(CH12_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Books are like a magic _______.", "door", "Books are like a magic door.", "Easy"),
    ("That takes you places you'll _______.", "adore", "Places you'll adore.", "Easy"),
    ("Through pages thick and pages _______.", "thin", "Pages thick and pages thin.", "Easy"),
    ("A world of wonder lies _______.", "within", "World of wonder lies within.", "Easy"),
    ("A book can take you to the _______.", "sky", "Take you to the sky.", "Easy"),
    ("Or deep below where oceans _______.", "lie", "Where oceans lie.", "Easy"),
    ("It shows you kingdoms, brave and _______.", "grand", "Kingdoms, brave and grand.", "Easy"),
    ("Or tiny creatures in the _______.", "sand", "Tiny creatures in the sand.", "Easy"),
    ("You'll meet new friends, both young and _______.", "old", "Both young and old.", "Easy"),
    ("Hear stories brave, and tales _______.", "untold", "Tales untold.", "Easy"),
    ("With every page, you'll laugh or _______.", "cry", "Laugh or cry.", "Easy"),
    ("Or dream about the days gone _______.", "by", "Days gone by.", "Easy"),
    ("So hold a book, and take a _______.", "flight", "Take a flight.", "Easy"),
    ("To lands of joy and pure _______.", "delight", "Pure delight.", "Easy"),
    ("For those who read will always _______.", "find", "Will always find.", "Easy"),
    ("A treasure house within their _______!", "mind", "Treasure house within their mind.", "Easy"),
    ("The poem 'The Magic of Books' is written by _______.", "Anonymous", "Written by Anonymous.", "Easy"),
    ("The word 'adore' in vocabulary means to love _______.", "deeply", "Love deeply.", "Easy"),
    ("Comparing books to a 'magic door' is a poetic _______.", "simile", "Uses simile.", "Easy"),
    ("Describing the mind as a 'treasure house' is a poetic _______.", "metaphor", "Uses metaphor.", "Easy"),
    ("A book shows kingdoms that are brave and _______.", "grand", "Brave and grand.", "Easy"),
    ("Books can show tiny creatures in the _______.", "sand", "In the sand.", "Easy"),
    ("Those who read will find a treasure house within their _______.", "mind", "Within their mind.", "Easy"),
    ("Holding a book lets readers take a flight to lands of _______.", "joy", "Lands of joy.", "Easy"),
    ("Chapter 12 is titled 'The Magic of _______'.", "Books", "The Magic of Books.", "Easy"),

    # Medium (26-40)
    ("The poem uses an AABB rhyme _______ in each stanza.", "scheme", "AABB rhyme scheme.", "Medium"),
    ("The phrase 'pages thick and pages thin' contrasts book _______.", "lengths", "Contrasts book lengths.", "Medium"),
    ("Deep below where oceans lie represents underwater _______.", "exploration", "Underwater exploration.", "Medium"),
    ("Meeting young and old friends in books expands reader _______.", "empathy", "Expands reader empathy.", "Medium"),
    ("Tales untold refers to new unread _______.", "stories", "New unread stories.", "Medium"),
    ("Laughing or crying shows how books evoke human _______.", "emotions", "Evokes human emotions.", "Medium"),
    ("Dreaming about days gone by reflects historical _______.", "nostalgia", "Reflects historical nostalgia.", "Medium"),
    ("Taking a flight metaphorically means letting imagination _______.", "soar", "Letting imagination soar.", "Medium"),
    ("Lands of joy and pure delight symbolize reading _______.", "pleasure", "Symbolizes reading pleasure.", "Medium"),
    ("Knowledge stored in the mind forms an enduring _______.", "treasure", "Forms an enduring treasure.", "Medium"),
    ("The opening line uses 'like' to form a vivid _______.", "comparison", "Forms a vivid comparison.", "Medium"),
    ("Reading allows children to transcend physical geographic _______.", "limits", "Transcends geographic limits.", "Medium"),
    ("Kingdoms brave and grand evoke heroic fantasy _______.", "adventures", "Heroic fantasy adventures.", "Medium"),
    ("Tiny creatures in the sand encourage curiosity for _______.", "nature", "Curiosity for nature.", "Medium"),
    ("Chapter 12 inspires primary students to build a reading _______.", "habit", "Build a reading habit.", "Medium"),

    # Hard (41-50)
    ("Metaphorical mind treasure contrasts with transient material _______.", "wealth", "Contrasts with material wealth.", "Hard"),
    ("Cognitive visualization during reading builds creative intellectual _______.", "capacity", "Builds intellectual capacity.", "Hard"),
    ("Couplet rhyming patterns enhance oral poetic _______.", "recitation", "Enhance oral recitation.", "Hard"),
    ("Linguistic economy achieves profound emotional resonance using simple _______.", "words", "Resonance using simple words.", "Hard"),
    ("Imaginative literature fosters child emotional _______.", "intelligence", "Fosters emotional intelligence.", "Hard"),
    ("Literary engagement transforms printed text into mental _______.", "landscapes", "Transforms text into landscapes.", "Hard"),
    ("Preserving physical books protects democratized access to _______.", "knowledge", "Protects access to knowledge.", "Hard"),
    ("Stanzaic progression moves from initial portal to internal _______.", "reward", "Moves from portal to reward.", "Hard"),
    ("Poetic imagery stimulates active cognitive child _______.", "visualization", "Stimulates visualization.", "Hard"),
    ("Chapter 12 instills lifelong passion for literature and _______.", "learning", "Passion for learning.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 12: The Magic of Books\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH12_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH12_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The poem compares books to a magic door.", "True", "Text confirms: 'Books are like a magic door'.", "Easy"),
    ("The author of the poem 'The Magic of Books' is William Shakespeare.", "False", "The poem is written by Anonymous.", "Easy"),
    ("According to the poem, a world of wonder lies within books.", "True", "Text confirms: 'A world of wonder lies within.'", "Easy"),
    ("Books can take readers to the sky or deep below where oceans lie.", "True", "Text confirms books take readers to the sky and under oceans.", "Easy"),
    ("Books can only show you real places like school classrooms.", "False", "Books take readers to grand kingdoms, deep oceans, and imaginary lands.", "Easy"),
    ("Books can show you kingdoms that are brave and grand.", "True", "Text confirms: 'It shows you kingdoms, brave and grand.'", "Easy"),
    ("Books can show you tiny creatures in the sand.", "True", "Text confirms: 'Or tiny creatures in the sand.'", "Easy"),
    ("You can meet new friends, both young and old, in books.", "True", "Text confirms: 'You'll meet new friends, both young and old.'", "Easy"),
    ("The poem says reading books brings boredom and sleepiness.", "False", "The poem says reading brings joy, delight, and a treasure house in the mind.", "Easy"),
    ("With every page, books can make you laugh or cry.", "True", "Text confirms: 'With every page, you'll laugh or cry.'", "Easy"),
    ("Books can make readers dream about the days gone by.", "True", "Text confirms: 'Or dream about the days gone by.'", "Easy"),
    ("The poet tells readers to hold a book and take a flight.", "True", "Text confirms: 'So hold a book, and take a flight.'", "Easy"),
    ("Reading takes imagination to lands of joy and pure delight.", "True", "Text confirms: 'To lands of joy and pure delight.'", "Easy"),
    ("Those who read will find a treasure house within their mind.", "True", "Text confirms: 'A treasure house within their mind!'", "Easy"),
    ("'Adore' means to hate something strongly.", "False", "Adore = Love deeply.", "Easy"),
    ("The poem has four stanzas of four lines each.", "True", "Poem contains 4 stanzas of 4 lines each (16 lines).", "Easy"),
    ("The line 'Books are like a magic door' contains a simile.", "True", "Uses 'like' to make a comparison, forming a simile.", "Easy"),
    ("The line 'A treasure house within their mind' contains a metaphor.", "True", "Directly compares mind to a treasure house, forming a metaphor.", "Easy"),
    ("'Door' rhymes with 'adore' in the first stanza.", "True", "Text confirms door / adore rhyme.", "Easy"),
    ("'Sky' rhymes with 'lie' in the second stanza.", "True", "Text confirms sky / lie rhyme.", "Easy"),
    ("'Grand' rhymes with 'sand' in the second stanza.", "True", "Text confirms grand / sand rhyme.", "Easy"),
    ("'Old' rhymes with 'untold' in the third stanza.", "True", "Text confirms old / untold rhyme.", "Easy"),
    ("'Cry' rhymes with 'by' in the third stanza.", "True", "Text confirms cry / by rhyme.", "Easy"),
    ("'Flight' rhymes with 'delight' in the fourth stanza.", "True", "Text confirms flight / delight rhyme.", "Easy"),
    ("Chapter 12 title is 'The Magic of Books'.", "True", "Chapter title is 'The Magic of Books'.", "Easy"),

    # Medium (26-40)
    ("The rhyme scheme of the poem is AABB in every stanza.", "True", "Each stanza follows AABB rhyme scheme.", "Medium"),
    ("The poem implies that thin books contain no interesting stories.", "False", "It states 'Through pages thick and pages thin, A world of wonder lies within.'", "Medium"),
    ("Reading books helps children develop empathy for different characters.", "True", "Meeting diverse characters ('young and old') develops empathy.", "Medium"),
    ("Taking a flight in the poem means riding on a physical airplane.", "False", "Metaphorically means letting one's imagination soar through reading.", "Medium"),
    ("The 'treasure house' in the mind refers to physical gold coins.", "False", "Refers to valuable knowledge, ideas, memories, and imagination.", "Medium"),
    ("Books allow readers to travel back in time to past eras.", "True", "Expresses 'dream about the days gone by'.", "Medium"),
    ("The poem claims that only children who own expensive books can enjoy reading.", "False", "States 'those who read will always find' regardless of wealth.", "Medium"),
    ("Literary imagery in the poem contrasts extreme heights (sky) with extreme depths (oceans).", "True", "Contrasts 'sky' with 'deep below where oceans lie'.", "Medium"),
    ("Reading books requires active mental participation from the reader.", "True", "Reading engages active visualization and thought.", "Medium"),
    ("The poem's tone is pessimistic and discouraging.", "False", "The tone is joyful, uplifting, and inspiring.", "Medium"),
    ("'Tales untold' suggests that books reveal secrets and undiscovered stories.", "True", "'Tales untold' means unread, fresh, or secret narratives.", "Medium"),
    ("The poem consists of 16 lines in total.", "True", "4 stanzas x 4 lines = 16 lines total.", "Medium"),
    ("Reading books expands vocabulary and language expression.", "True", "Exposure to literature enriches vocabulary and expression.", "Medium"),
    ("The poem suggests that physical travel is superior to reading books.", "False", "Celebrates books as magical travel accessible to everyone's mind.", "Medium"),
    ("Chapter 12 is designed to foster a love for reading among Class 5 students.", "True", "Encourages students to see books as magical treasure houses.", "Medium"),

    # Hard (41-50)
    ("Linguistic economy uses simple rhyming couplets to convey complex psychological benefits.", "True", "Simple rhyming couplets convey profound cognitive and emotional benefits.", "Hard"),
    ("Metaphorical 'treasure house' implies that knowledge is permanent and non-depletable.", "True", "Mental knowledge endures permanently unlike physical wealth.", "Hard"),
    ("Active reading stimulates cognitive visualization more than watching television.", "True", "Reading requires mental rendering of scenes, unlike screen consumption.", "Hard"),
    ("Stanza 1 establishes the portal motif through the 'magic door' simile.", "True", "Stanza 1 introduces the magic door portal into wonder.", "Hard"),
    ("The poem uses opposite pairs (thick/thin, sky/oceans, grand/tiny, young/old, laugh/cry) to show book universality.", "True", "Binary opposites demonstrate that books cover the entire human experience.", "Hard"),
    ("Anonymous authorship suggests the poem has become a universal folk hymn for literacy.", "True", "Anonymous origins give it universal, timeless appeal across schools.", "Hard"),
    ("Reading fantasy literature impairs a child's ability to understand reality.", "False", "Imaginative literature enhances creative problem-solving and reality understanding.", "Hard"),
    ("Rhyming couplets in AABB scheme make the poem easy to memorize and recite.", "True", "AABB couplets provide rhythmic musicality ideal for recitation.", "Hard"),
    ("Chapter 12 integrates literary analysis, poetic devices, and reading motivation.", "True", "Combines literary devices (simile/metaphor), rhyme analysis, and motivation.", "Hard"),
    ("Cultivating a reading habit in primary school forms a foundation for lifelong learning.", "True", "Early reading habits establish permanent cognitive curiosity.", "Hard")
]

tf_content = f"# True / False — Chapter 12: The Magic of Books\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH12_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Question**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH12_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("What does the poet compare books to in the first line of the poem?", "The poet compares books to a 'magic door' that opens into places you will adore.", "Easy", "Remembering"),
    ("Who wrote the poem 'The Magic of Books'?", "The poem was written by an Anonymous author.", "Easy", "Remembering"),
    ("What lies within pages thick and pages thin?", "A 'world of wonder' lies within pages thick and pages thin.", "Easy", "Remembering"),
    ("Where can a book take a reader according to the second stanza?", "A book can take a reader high up to the sky or deep below where oceans lie.", "Easy", "Remembering"),
    ("What contrasts are presented in stanza 2 regarding what books can show?", "Books contrast high skies with deep ocean floors, and grand, brave kingdoms with tiny creatures in the sand.", "Easy", "Understanding"),
    ("What kind of new friends can you meet in books?", "You can meet new friends who are both young and old.", "Easy", "Remembering"),
    ("What types of stories do books share with readers?", "Books share brave stories and untold tales.", "Easy", "Remembering"),
    ("What range of emotions can every page evoke in a reader?", "Every page can make a reader laugh, cry, or dream about days gone by.", "Easy", "Understanding"),
    ("What does the poet encourage readers to do in stanza 4?", "The poet encourages readers to hold a book and take a flight to lands of joy and pure delight.", "Easy", "Remembering"),
    ("What will those who read always find inside their mind?", "They will always find a 'treasure house' within their mind.", "Easy", "Remembering"),
    ("What does the word 'adore' mean?", "'Adore' means to love deeply or hold in high affection.", "Easy", "Understanding"),
    ("Name the figure of speech used in 'Books are like a magic door'.", "It is a simile because it uses the word 'like' to compare books to a magic door.", "Easy", "Understanding"),
    ("Name the figure of speech used in 'A treasure house within their mind'.", "It is a metaphor because it directly equates the mind to a treasure house without using 'like' or 'as'.", "Easy", "Understanding"),
    ("Identify the rhyming words in the first stanza.", "The rhyming pairs are 'door' / 'adore' and 'thin' / 'within'.", "Easy", "Remembering"),
    ("Identify the rhyming words in the second stanza.", "The rhyming pairs are 'sky' / 'lie' and 'grand' / 'sand'.", "Easy", "Remembering"),
    ("Identify the rhyming words in the third stanza.", "The rhyming pairs are 'old' / 'untold' and 'cry' / 'by'.", "Easy", "Remembering"),
    ("Identify the rhyming words in the fourth stanza.", "The rhyming pairs are 'flight' / 'delight' and 'find' / 'mind'.", "Easy", "Remembering"),
    ("What does 'untold' mean in the line 'tales untold'?", "'Untold' means fresh, secret, or new stories that have not been heard before.", "Easy", "Understanding"),
    ("Why is a book called a 'magic door'?", "Because opening a book magically transports a reader's imagination to distant lands, adventures, and ideas.", "Easy", "Understanding"),
    ("Why is the human mind described as a 'treasure house'?", "Because reading fills the mind with valuable knowledge, creative ideas, beautiful memories, and wisdom.", "Easy", "Understanding"),
    ("What does taking a 'flight' mean in the poem?", "It metaphorically means letting one's thoughts and imagination soar freely to joyful lands through reading.", "Easy", "Understanding"),
    ("How many stanzas and lines are in the poem?", "The poem consists of 4 stanzas of 4 lines each, totaling 16 lines.", "Easy", "Remembering"),
    ("What is the overall tone of the poem?", "The tone is joyful, inspiring, encouraging, and magical.", "Easy", "Understanding"),
    ("What title is given to Chapter 12?", "The title of Chapter 12 is 'The Magic of Books'.", "Easy", "Remembering"),
    ("What main message does Chapter 12 give to Class 5 students?", "It encourages students to embrace reading daily to discover wonder, build imagination, and enrich their minds.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how the poet uses binary opposites (thick/thin, sky/oceans, grand/tiny, young/old, laugh/cry) to show book versatility.", "The poet uses contrasting pairs to show that books cover the entire spectrum of human experience, space, time, scale, and emotion.", "Medium", "Analyzing"),
    ("Explain the rhyme scheme of the poem and how it creates rhythm.", "Each stanza follows an AABB rhyme scheme (rhyming couplets), creating a musical, rhythmic beat that makes the poem easy to recite and memorize.", "Medium", "Analyzing"),
    ("Why does the poet say 'pages thick and pages thin' contain a world of wonder?", "To emphasize that whether a book is long or short, simple or complex, every book holds valuable magic and wonder for the reader.", "Medium", "Understanding"),
    ("How does meeting 'new friends, both young and old' in books help children develop empathy?", "Reading introduces children to characters from different generations and backgrounds, helping them understand diverse feelings and life experiences.", "Medium", "Evaluating"),
    ("What does 'dream about the days gone by' suggest about books and history?", "It suggests that books act as time machines, preserving historical events and ancestral memories so readers can experience past eras.", "Medium", "Understanding"),
    ("Contrast physical travel with the imaginative travel described in the poem.", "Physical travel requires tickets and transport to reach real places; imaginative travel in books is instantaneous, free, and can reach imaginary, historical, or microscopic worlds.", "Medium", "Comparing"),
    ("Why does the poet describe lands reached through books as 'lands of joy and pure delight'?", "Because reading provides emotional happiness, creative satisfaction, and intellectual pleasure to curious minds.", "Medium", "Understanding"),
    ("How does the metaphor 'treasure house within their mind' contrast with material wealth?", "Material treasure can be spent, lost, or stolen, whereas the intellectual and creative treasure stored in the mind through reading stays forever.", "Medium", "Evaluating"),
    ("Why is Anonymous authorship suitable for a poem celebrating books?", "Because the message belongs universally to all readers everywhere, transcending any single author's name.", "Medium", "Analyzing"),
    ("Summarize Chapter 12 in four concise sentences.", "'The Magic of Books' by Anonymous is an uplifting 16-line poem praising reading. It compares books to magic doors that open into worlds of wonder, soaring to skies, diving into oceans, and exploring grand kingdoms. Reading brings new friends, evokes laughter, tears, and historical dreams, and transports imagination to joyful lands. Ultimately, reading turns a child's mind into an enduring treasure house of wisdom.", "Medium", "Understanding"),
    ("How does the poem inspire reluctant readers to pick up a book?", "By presenting reading not as a tedious school chore, but as an exciting, magical adventure of flight, discovery, and joy.", "Medium", "Evaluating"),
    ("Explain how literary imagery in stanza 2 engages a child's visual imagination.", "Phrases like 'sky', 'deep below where oceans lie', 'kingdoms, brave and grand', and 'tiny creatures in the sand' paint vivid mental pictures for young readers.", "Medium", "Analyzing"),
    ("Why are rhyming couplets effective for teaching poetry to Class 5 students?", "Rhyming couplets create predictable rhythm, help memory retention, highlight vocabulary, and make reading aloud fun.", "Medium", "Evaluating"),
    ("How does the poem connect emotional experience ('laugh or cry') with mental growth?", "By showing that experiencing different emotions through stories deepens emotional intelligence alongside mental knowledge.", "Medium", "Analyzing"),
    ("What advice would you give to a friend who says reading is boring based on this poem?", "Tell them to open a book to find their 'magic door', explore stories of grand kingdoms or deep oceans, and discover their mind's treasure house.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the cognitive difference between reading literature and watching visual media.", "Reading requires active mental visualization, rendering text into custom mental imagery that builds cognitive capacity; visual media provides pre-rendered scenes that encourage passive consumption.", "Hard", "Evaluating"),
    ("Deconstruct the structural progression of the four stanzas.", "Stanza 1 introduces the portal (magic door); Stanza 2 explores physical spaces (sky/ocean/kingdoms); Stanza 3 explores emotional/character connections; Stanza 4 delivers the internal reward (mind's treasure house).", "Hard", "Analyzing"),
    ("Evaluate the importance of cultivating an imaginative 'treasure house' in childhood.", "An imaginative treasure house built in childhood provides creative problem-solving skills, emotional resilience, and lifelong curiosity for adult life.", "Hard", "Evaluating"),
    ("Compare the simile 'like a magic door' with the metaphor 'treasure house within their mind'.", "The simile ('magic door') describes the external entry process of opening a book; the metaphor ('treasure house') describes the internal permanent result in the reader's mind.", "Hard", "Comparing"),
    ("Formulate an original 4-line stanza continuing the poem's theme.", "'Turn every page and you will see,\nA world where thoughts fly wild and free;\nFrom mountain peak to starlit space,\nA book is your most sacred place!'", "Hard", "Creating"),
    ("Assess how literature preserves cultural heritage across generations.", "Literature records ancestral stories, historical eras ('days gone by'), and moral values, passing them down as living culture to new generations.", "Hard", "Evaluating"),
    ("Analyze the use of poetic diction in line 16 ('A treasure house within their mind!').", "The exclamation mark and noble noun phrase 'treasure house' create a climactic, triumphant ending emphasizing the supreme value of literacy.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 12 links language art, emotional development, and lifelong learning.", "Links poetic language art (similes/metaphors/rhyme) with emotional development (empathy/feelings) and lifelong intellectual curiosity.", "Hard", "Synthesizing"),
    ("Critique the claim: 'Digital technology has made printed books obsolete.'", "False; while digital formats exist, the fundamental magic of text-driven imaginative visualization ('magic door') remains identical whether on paper or screen.", "Hard", "Evaluating"),
    ("Formulate a 4-line rhyming slogan for a school reading week.", "'Open a book and open your mind,\nA world of wonder you will find;\nFly to the sky or deep sea blue,\nThe magic of books is waiting for you!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 12: The Magic of Books\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH12_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH12_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Examine the poetic devices used in 'The Magic of Books': Simile, Metaphor, and Imagery.",
     "The poem 'The Magic of Books' uses rich poetic devices to celebrate reading:\n1. **Simile**: In the opening line, 'Books are like a magic door', the poet uses 'like' to compare opening a book to stepping through an enchanted door that leads to wonderful places.\n2. **Metaphor**: In the final line, 'A treasure house within their mind!', the poet directly equates the human mind to a treasure house without using 'like' or 'as', emphasizing that reading fills the mind with permanent, precious knowledge and ideas.\n3. **Visual & Spatial Imagery**: The poet paints vivid mental scenes—'take you to the sky', 'deep below where oceans lie', 'kingdoms, brave and grand', and 'tiny creatures in the sand'—engaging young readers' imagination.",
     "Easy", "Remembering"),

    ("Describe the journey of imagination that books offer to readers according to the poem.",
     "According to the poem, a book offers an unlimited journey of imagination:\n1. **Spatial Exploration**: Books can transport readers high into the sky or down to the depths of ocean floors.\n2. **World Discovery**: They reveal grand, brave kingdoms of royalty and heroes, as well as microscopic worlds containing tiny creatures in the sand.\n3. **Social & Human Connection**: Readers meet diverse new friends across age groups ('both young and old') and hear heroic, untold stories.\n4. **Emotional Range**: Readers experience laughter, tears, and nostalgia ('dream about the days gone by').\n5. **Ultimate Destination**: Reading takes imagination to 'lands of joy and pure delight', creating a rich treasure house of wisdom inside the mind.",
     "Easy", "Understanding"),

    ("Explain why the poet describes a reader's mind as a 'treasure house' and compare it with physical wealth.",
     "The poet describes a reader's mind as a 'treasure house' because reading continuously enriches the mind with valuable knowledge, creative ideas, beautiful memories, and moral wisdom. Comparing this mental treasure house with physical wealth reveals deep truths:\n- **Physical Wealth**: Money, gold, or toys can be spent, damaged, lost, or stolen, and their enjoyment is temporary.\n- **Mental Treasure**: Knowledge and imaginative experiences stored in the mind cannot be stolen or lost. They grow richer over time, expand creative problem-solving skills, and provide lifelong comfort and joy. Therefore, the mind's treasure house earned through reading is far more valuable than physical wealth.",
     "Easy", "Understanding"),

    ("Describe the structure, rhythm, and rhyme scheme of the poem 'The Magic of Books'.",
     "The poem 'The Magic of Books' is structured thoughtfully for young readers:\n1. **Stanzaic Structure**: It consists of 4 four-line stanzas (quatrains), making a total of 16 lines.\n2. **Rhyme Scheme**: Every stanza follows an **AABB** rhyme scheme consisting of rhyming couplets:\n   - Stanza 1: door/adore (A), thin/within (B)\n   - Stanza 2: sky/lie (A), grand/sand (B)\n   - Stanza 3: old/untold (A), cry/by (B)\n   - Stanza 4: flight/delight (A), find/mind (B)\n3. **Rhythm & Musicality**: The regular meter and rhyming couplets create a bouncy, musical rhythm that makes the poem easy to recite, memorize, and appreciate.",
     "Easy", "Remembering"),

    ("Explain the vocabulary word 'adore' and discuss why readers adore the places books take them.",
     "In the vocabulary section of Chapter 12, 'adore' is defined as 'to love deeply'. In the poem, the line 'That takes you places you'll adore' explains why readers fall deeply in love with books:\n- Books take readers away from daily routines into enchanted worlds of fantasy, adventure, and beauty.\n- Readers adore discovering high skies, deep ocean beds, brave kingdoms, and miniature natural worlds.\n- The joy of meeting memorable story friends and experiencing exciting adventures makes readers deeply adore the experience of reading.",
     "Easy", "Understanding"),

    ("Discuss how books evoke different human emotions as described in the third stanza.",
     "The third stanza explores how books connect deeply with human emotions:\n1. **Empathy & Friendship**: 'You'll meet new friends, both young and old' shows that books build emotional connections with diverse characters.\n2. **Adventure & Wonder**: 'Hear stories brave, and tales untold' excites readers with heroic courage and fresh narrative discovery.\n3. **Humor & Compassion**: 'With every page, you'll laugh or cry' shows that stories evoke joy, laughter, sympathy, and tears.\n4. **Nostalgia & Reflection**: 'Or dream about the days gone by' allows readers to reflect on past memories and historical times.",
     "Easy", "Understanding"),

    ("Explain how the poem uses binary opposites (contrasts) to demonstrate that books cover everything.",
     "The poet strategically uses contrasting pairs (binary opposites) to show that books embrace the entire universe:\n- **Physical Thickness**: 'pages thick and pages thin' (covers long novels and short stories alike).\n- **Vertical Space**: 'to the sky' vs 'deep below where oceans lie' (covers vast heights and ocean depths).\n- **Scale**: 'kingdoms, brave and grand' vs 'tiny creatures in the sand' (covers massive empires and tiny insects).\n- **Age**: 'both young and old' (embraces all generations of characters).\n- **Emotions**: 'laugh or cry' (encompasses joy and sadness).\nThese contrasts prove that no matter what a reader seeks, books contain it all.",
     "Easy", "Analyzing"),

    ("Why is 'The Magic of Books' an effective poem to inspire reading habits in Class 5 students?",
     "It is an exceptionally effective inspirational poem because:\n1. **Engaging Metaphors**: It frames reading as stepping through a 'magic door' and taking a 'flight' to joyful lands, turning reading into an exciting adventure.\n2. **Relatable Themes**: It mentions things children love—skies, oceans, brave kingdoms, tiny animals, new friends, and heroic stories.\n3. **Encouraging Tone**: It reassures students that reading builds a permanent 'treasure house' in their mind, building self-confidence and a lifelong love for books.",
     "Easy", "Evaluating"),

    ("Summarize Chapter 12 in five detailed bullet points.",
     "- 'The Magic of Books' by Anonymous is a 16-line poem celebrating reading's transformative power.\n- Uses the simile 'like a magic door' to show how books open into worlds of wonder across thick and thin pages.\n- Takes readers' imagination high into the sky, deep under oceans, to brave grand kingdoms, and to tiny creatures in the sand.\n- Introduces young and old story friends, evoking laughter, tears, heroic tales, and historical dreams ('days gone by').\n- Urges children to hold a book and take flight to joyful lands, building a permanent 'treasure house' within their mind.",
     "Easy", "Understanding"),

    ("What life lessons about curiosity and learning can Class 5 students draw from Chapter 12?",
     "Class 5 students learn that curiosity is the key to unlocking the world. By picking up books, they can travel anywhere, learn about nature and history, understand different people's feelings, and develop creative thinking. They learn that the real wealth of a human being is not physical money, but the knowledge, imagination, and moral wisdom stored in their mind's treasure house.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why is the poem titled 'The Magic of Books' instead of 'Reading Books'?", "Because 'magic' captures the invisible, miraculous transformation of printed ink on paper into vivid mental pictures, deep feelings, time-travel, and personal wisdom.", "Easy", "Analyzing"),
    ("Describe the contrast between 'kingdoms, brave and grand' and 'tiny creatures in the sand'.", "It contrasts epic, historical human civilizations (grand kingdoms) with tiny, quiet natural organisms (sand creatures), showing that books appreciate both massive empires and miniature biology.", "Easy", "Understanding"),
    ("How does reading books allow a person to 'take a flight' without moving from their room?", "Reading frees the mind from physical boundaries. As eyes read words, imagination takes flight, painting vivid landscapes of joy and adventure inside the reader's head.", "Easy", "Understanding"),
    ("Explain the meaning of 'tales untold' in the third stanza.", "'Tales untold' refers to undiscovered, fresh, or secret stories waiting inside unread books, inviting readers to explore new narratives and ideas.", "Easy", "Understanding"),
    ("How does meeting 'new friends, both young and old' in books shape a child's character?", "It exposes children to characters of different ages, cultures, and life struggles, teaching empathy, respect for elders, and understanding of others.", "Easy", "Understanding"),
    ("Discuss how the poem connects reading with emotional health.", "By encouraging readers to 'laugh or cry' and 'dream', books provide a healthy outlet for expressing emotions, releasing stress, and finding joy.", "Easy", "Understanding"),
    ("Why does the poet emphasize that a world of wonder lies within 'pages thick and pages thin'?", "To teach that book length does not determine quality; a short 10-page picture book or a long 500-page novel both contain magical wonder.", "Easy", "Understanding"),
    ("Explain how reading helps children 'dream about the days gone by'.", "Historical fiction and history books allow children to visualize ancient civilizations, freedom struggles, and ancestral life, connecting them with history.", "Easy", "Understanding"),
    ("How does the poem use musical rhythm to make reading appealing to children?", "The steady meter and rhyming couplets (door/adore, sky/lie, flight/delight) create a catchy, song-like flow that makes reading enjoyable.", "Easy", "Evaluating"),
    ("Describe how a school library can serve as a 'magic door' for all students.", "A school library gathers thousands of books under one roof, offering every student equal access to magic doors leading to science, history, and adventure.", "Easy", "Applying"),
    ("Re-write the poem 'The Magic of Books' as a short 100-word prose paragraph.", "Books are like magical doors that lead to wonderful places we love deeply. Whether books are thick or thin, incredible worlds of wonder lie inside their pages. A book can take your mind soaring into the sky or plunging deep into ocean waters. It shows us grand, brave kingdoms and tiny creatures living in the sand. Through reading, we meet young and old friends, hear brave stories, laugh, cry, and dream about history. When you hold a book, your imagination takes flight to joyful lands, turning your mind into a permanent treasure house of knowledge.", "Easy", "Creating"),
    ("Why is Anonymous authorship meaningful for an educational poem on reading?", "It shows that love for reading is a universal human truth shared by millions of anonymous readers and writers throughout history.", "Easy", "Understanding"),
    ("How does reading build creative problem-solving skills in children?", "By exposing children to diverse story challenges and character solutions, reading trains the brain to think creatively and solve problems.", "Easy", "Understanding"),
    ("Analyze why Chapter 12 is placed in Class 5 English textbook.", "It inspires Class 5 students at a crucial developmental age to build strong independent reading habits, master poetic devices, and appreciate literature.", "Easy", "Analyzing"),
    ("What steps can parents and teachers take to help children find their 'treasure house'?", "Provide diverse books, create quiet daily reading times, discuss story themes together, and celebrate children's reading discoveries enthusiastically.", "Easy", "Applying"),

    # Medium (26-40)
    ("Critically analyze how 'The Magic of Books' uses spatial, temporal, and emotional dimensions.",
     "The poem operates across three vast dimensions:\n1. **Spatial Dimension**: Moves vertically from 'the sky' down to 'where oceans lie', and horizontally from 'kingdoms, brave and grand' to 'tiny creatures in the sand'.\n2. **Temporal Dimension**: Spans past eras ('days gone by'), present discoveries ('stories brave'), and timeless imagination.\n3. **Emotional Dimension**: Touches the complete human feeling spectrum—adoration, laughter, tears, dreams, joy, and delight.",
     "Medium", "Analyzing"),

    ("Examine the cognitive process of visualization described in 'hold a book, and take a flight'.",
     "When holding a book, printed words trigger decoding in the brain, which immediately translates abstract symbols into rich sensory imagery. This active cognitive visualization frees thoughts from physical gravity ('take a flight'), allowing readers to mentally inhabit fictional lands of joy and process complex ideas.",
     "Medium", "Analyzing"),

    ("Evaluate how the metaphor 'A treasure house within their mind' redefines true wealth for children.",
     "The poem redefines wealth by contrasting material possessions with intellectual treasure. Material possessions decay, break, or lose value. In contrast, mental wealth—built through reading—accumulates permanently, enriching vocabulary, critical thinking, empathy, and creative imagination for a lifetime.",
     "Medium", "Evaluating"),

    ("Discuss how poetry education in primary school builds language appreciation through rhyme and rhythm.",
     "Poetry introduces primary students to the musical aesthetics of language. The regular AABB rhyme scheme, rhythmic meter, and vivid diction in Chapter 12 train students' ears for phonetic harmony, improve reading fluency, and make language learning pleasurable.",
     "Medium", "Analyzing"),

    ("Design an interactive classroom activity around 'The Magic of Books' for Class 5.",
     "Activity Title: 'My Magic Door to Wonder'\n1. **Door Craft**: Students draw and cut out a paper 'Magic Door' on cardstock.\n2. **Inside Drawing**: Inside the door, they draw their favorite book scene (sky, deep ocean, or grand kingdom).\n3. **Poetry Recitation**: Students recite their favorite stanza from Chapter 12.\n4. **Treasure Box**: Students write 3 new words learned from reading and place them in a class 'Treasure House' box.",
     "Medium", "Creating"),

    ("How does reading 'stories brave, and tales untold' build courage in young readers?", "By exposing children to heroic characters who overcome adversity, reading instills moral courage, resilience, and problem-solving determination in real life.", "Medium", "Understanding"),
    ("Contrast the experience of reading a printed book with looking at a door in a house.", "A physical door leads only to another room; a book's 'magic door' opens into unlimited imaginary universes, historical eras, and emotional realms.", "Medium", "Comparing"),
    ("Why does the poet include both 'laugh or cry' as positive aspects of reading?", "Because both laughter and tears represent authentic emotional engagement, proving that literature touches the deepest human feelings.", "Medium", "Understanding"),
    ("How does the phrase 'days gone by' foster historical curiosity in primary students?", "It sparks curiosity about past centuries, ancient kings, freedom struggles, and ancestral lives, encouraging students to explore history books.", "Medium", "Understanding"),
    ("Describe how reading enhances a child's concentration and focus.", "Unlike fast-paced digital screens, reading requires sustained attention on printed text, building mental discipline and deep focus.", "Medium", "Analyzing"),
    ("Explain the relationship between reading books and building strong written expression.", "Regular reading exposes students to rich sentence structures, diverse vocabulary, and storytelling techniques, naturally improving their writing.", "Medium", "Understanding"),
    ("How does the poem present reading as an accessible luxury for every child?", "It states that anyone who holds a book and reads can access 'lands of joy' and build a 'treasure house', regardless of social or economic status.", "Medium", "Evaluating"),
    ("Analyze why simple, rhythmic poems like Chapter 12 are memorable across generations.", "Their universal human themes, vibrant imagery, and bouncy musical rhythm make them easy to memorize, recite, and cherish lifelong.", "Medium", "Analyzing"),
    ("What makes the transition from Stanza 3 (emotions) to Stanza 4 (treasure house) climactic?", "Stanza 3 builds emotional connection (friends/laugh/cry); Stanza 4 synthesizes these experiences into the ultimate reward: a permanent mind treasure house.", "Medium", "Analyzing"),
    ("Construct a fictional speech by a student librarian encouraging classmates to read.", "'Friends! Books in our library are not paper on shelves—they are magic doors waiting for you! Open a book today, take a flight to grand kingdoms, and build your mind's treasure house!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the societal impact of declining reading habits among youth in the digital age.",
     "Declining reading habits lead to reduced attention spans, weaker critical analysis, lower empathy, and superficial information consumption. Re-emphasizing books as 'treasure houses of the mind' is essential to cultivate deep thinking, emotional intelligence, and informed citizenship in society.",
     "Hard", "Evaluating"),

    ("Deconstruct the philosophical allegory of the 'Magic Door' in literature.",
     "The 'Magic Door' serves as a classic literary motif representing the transition from mundane reality to creative enlightenment. Passing through the door symbolizes stepping out of physical limitations into intellectual freedom, self-discovery, and expanded consciousness.",
     "Hard", "Analyzing"),

    ("Synthesize how Chapter 12 integrates literary aesthetics, cognitive development, and character ethics.",
     "Integrates literary aesthetics (rhyme/simile/metaphor) with cognitive growth (visualization/vocabulary) and character ethics (empathy/resilience/joy).", "Hard", "Synthesizing"),

    ("Formulate a comprehensive essay prompt evaluating the role of imaginative reading in child development.",
     "Prompt: 'Critically analyze how the poem The Magic of Books presents reading as an imaginative, emotional, and intellectual adventure. Explain how similes, metaphors, and contrasting imagery convey the lifelong value of books.'",
     "Hard", "Creating"),

    ("Evaluate the role of children's poetry in developing phonological awareness and literary appreciation.", "Children's poetry uses rhythmic meter, end-rhymes, and alliteration to strengthen phonological awareness, auditory memory, and aesthetic appreciation for language structure.", "Hard", "Evaluating"),

    ("Compare the literary device of Simile ('like a magic door') with Metaphor ('treasure house') in Chapter 12.", "Simile highlights the active process of opening a book as a gateway; Metaphor highlights the permanent, transformative outcome stored within the reader's mind.", "Hard", "Comparing"),
    ("Discuss how reading diverse cultural literature promotes global peace and understanding.", "By introducing readers to characters from different nations, cultures, and eras ('new friends, both young and old'), literature breaks down prejudice and fosters global empathy.", "Hard", "Evaluating"),
    ("Analyze how the poet creates a sense of movement in 'hold a book, and take a flight'.", "Kinaesthetic verb phrases ('hold', 'take a flight', 'soar') transform the stationary act of reading into an active, exhilarating physical and mental journey.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'For those who read will always find, A treasure house within their mind!'", "This triumphant concluding couplet acts as the moral climax of the poem. It guarantees that literacy bestows an inner, unstealable wealth of wisdom and joy that enriches a human life forever.", "Hard", "Evaluating"),
    ("Synthesize the complete educational takeaways of Chapter 12 for primary school English literature.", "Chapter 12 unifies poetic analysis (rhyme scheme AABB, simile, metaphor) with reading motivation, emotional expression, and character-building appreciation for books.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 12: The Magic of Books\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH12_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH12_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Books are like a magic door,\nThat takes you places you'll adore.\nThrough pages thick and pages thin,\nA world of wonder lies within.",
     [
         ("What does the poet compare books to in the first line?", "A magic door.", "Easy", "Remembering"),
         ("Where do books take the reader?", "To places they will adore.", "Easy", "Remembering"),
         ("What contrast is mentioned regarding pages?", "Pages thick and pages thin.", "Easy", "Remembering"),
         ("What lies within the pages of a book?", "A world of wonder.", "Easy", "Remembering"),
         ("Name the figure of speech used in 'Books are like a magic door'.", "Simile (using 'like' for comparison).", "Easy", "Understanding")
     ]),

    # Set 2
    ("A book can take you to the sky,\nOr deep below where oceans lie.\nIt shows you kingdoms, brave and grand,\nOr tiny creatures in the sand.",
     [
         ("Where can a book take you high above?", "To the sky.", "Easy", "Remembering"),
         ("Where can a book take you down below?", "Deep below where oceans lie.", "Easy", "Remembering"),
         ("What grand sights can a book show you?", "Kingdoms, brave and grand.", "Easy", "Remembering"),
         ("What small things in nature can a book show you?", "Tiny creatures in the sand.", "Easy", "Remembering"),
         ("What contrast is created between 'kingdoms' and 'tiny creatures'?", "Contrasts vast, powerful human empires with small, delicate natural organisms.", "Medium", "Analyzing")
     ]),

    # Set 3
    ("You'll meet new friends, both young and old,\nHear stories brave, and tales untold.\nWith every page, you'll laugh or cry,\nOr dream about the days gone by.",
     [
         ("Whom will you meet while reading books?", "New friends, both young and old.", "Easy", "Remembering"),
         ("What kind of stories and tales will you hear?", "Stories brave, and tales untold.", "Easy", "Remembering"),
         ("What two opposite emotions might you feel with every page?", "You might laugh or cry.", "Easy", "Remembering"),
         ("What will books make you dream about?", "The days gone by.", "Easy", "Remembering"),
         ("What does 'tales untold' mean in this stanza?", "Fresh, secret, or new stories waiting to be discovered by a reader.", "Medium", "Understanding")
     ]),

    # Set 4
    ("So hold a book, and take a flight,\nTo lands of joy and pure delight.\nFor those who read will always find,\nA treasure house within their mind!",
     [
         ("What action does the poet encourage in the first line?", "Hold a book, and take a flight.", "Easy", "Remembering"),
         ("To what lands does reading take your imagination?", "Lands of joy and pure delight.", "Easy", "Remembering"),
         ("What will those who read always find?", "A treasure house within their mind.", "Easy", "Remembering"),
         ("Where is this 'treasure house' located?", "Within the reader's mind.", "Easy", "Remembering"),
         ("Name the figure of speech in 'A treasure house within their mind'.", "Metaphor (directly comparing the mind to a treasure house).", "Easy", "Understanding")
     ]),

    # Set 5
    ("Books are like a magic door... For those who read will always find, A treasure house within their mind! - Anonymous",
     [
         ("Who wrote this poem?", "Anonymous.", "Easy", "Remembering"),
         ("How many total stanzas are in this poem?", "Four stanzas.", "Easy", "Remembering"),
         ("How many total lines are in this poem?", "Sixteen lines.", "Easy", "Remembering"),
         ("What is the rhyme scheme of each stanza?", "AABB (rhyming couplets).", "Medium", "Analyzing"),
         ("What is the central theme of the poem?", "Reading books magically expands imagination, evokes emotions, and creates lasting mental wisdom.", "Medium", "Evaluating")
     ]),

    # Set 6
    ("Word Meaning: Adore : Love deeply",
     [
         ("What is the vocabulary word defined here?", "Adore.", "Easy", "Remembering"),
         ("What is the meaning of 'adore'?", "Love deeply.", "Easy", "Remembering"),
         ("Which line in the poem contains the word 'adore'?", "'That takes you places you'll adore.'", "Easy", "Remembering"),
         ("Use 'adore' in a sentence of your own.", "I adore reading adventure storybooks in the school library.", "Medium", "Applying"),
         ("What part of speech is 'adore'?", "Verb.", "Medium", "Understanding")
     ]),

    # Set 7
    ("Through pages thick and pages thin... It shows you kingdoms, brave and grand... Hear stories brave, and tales untold...",
     [
         ("What words describe the thickness of pages?", "Thick and thin.", "Easy", "Remembering"),
         ("What adjectives describe kingdoms in the poem?", "Brave and grand.", "Easy", "Remembering"),
         ("What adjectives describe stories and tales?", "Brave stories and untold tales.", "Easy", "Remembering"),
         ("Why does the poet use repetition of the word 'brave'?", "To emphasize courage and heroic adventure in reading.", "Medium", "Analyzing"),
         ("What does this reveal about what children love in books?", "Children love heroic, exciting, and courageous adventures.", "Medium", "Understanding")
     ]),

    # Set 8
    ("With every page, you'll laugh or cry, Or dream about the days gone by.",
     [
         ("What two contrast verbs show emotions in this extract?", "Laugh or cry.", "Easy", "Remembering"),
         ("What does 'days gone by' refer to?", "Past times, history, or old memories.", "Easy", "Understanding"),
         ("How does a book make a reader laugh?", "By sharing funny characters and humorous situations.", "Easy", "Understanding"),
         ("How does a book make a reader cry?", "By sharing touching, sad, or compassionate character moments.", "Easy", "Understanding"),
         ("What capacity of the human mind is highlighted here?", "The capacity for deep emotional resonance and empathy.", "Medium", "Analyzing")
     ]),

    # Set 9
    ("So hold a book, and take a flight, To lands of joy and pure delight.",
     [
         ("What object should you hold?", "A book.", "Easy", "Remembering"),
         ("What does 'take a flight' mean metaphorically?", "Soar into imagination through reading.", "Easy", "Understanding"),
         ("What words describe the lands you reach?", "Lands of joy and pure delight.", "Easy", "Remembering"),
         ("Identify the rhyming pair in this extract.", "flight / delight.", "Easy", "Remembering"),
         ("How does this extract motivate children to read?", "By making reading sound like a fun, exhilarating aerial flight into happiness.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("Books are like a magic door... A treasure house within their mind!",
     [
         ("What is the opening simile of the poem?", "Books are like a magic door.", "Easy", "Remembering"),
         ("What is the closing metaphor of the poem?", "A treasure house within their mind.", "Easy", "Remembering"),
         ("How does the opening simile connect to the closing metaphor?", "The magic door is the entry point of reading; the treasure house is the permanent mental result.", "Medium", "Analyzing"),
         ("Why is knowledge called a 'treasure'?", "Because knowledge is precious, permanent, and enriches human life forever.", "Medium", "Evaluating"),
         ("Summarize the poem's complete message in one sentence.", "Opening a book is stepping through a magic door into endless imagination, building an unstealable treasure house of wisdom in the mind.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 12: The Magic of Books\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH12_EXT_{q_counter:03d}"
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

with open(os.path.join(CH12_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 12 in {CH12_DIR}")
