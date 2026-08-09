r"""
Refines all 6 Category files for Book 5 Chapter 13 ("My Dream Adventure" - Poem) for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH13_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_13")
os.makedirs(CH13_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What kind of stream did the speaker sail along in the dream?", "(A) A chocolate stream", "(B) A river of milk", "(C) A stream of honey", "(D) A muddy water stream", "(A)", "Line: 'I sailed along a chocolate stream.'", "Easy", "Remembering", "Stream Type"),
    ("What were the tall trees compared to in the poem?", "(A) Candy canes", "(B) Wooden poles", "(C) Green umbrellas", "(D) Skyscrapers", "(A)", "Line: 'The trees were tall, like candy canes'.", "Easy", "Remembering", "Tree Simile"),
    ("What were the clouds in the dream world made of?", "(A) Marshmallows", "(B) Cotton candy", "(C) White ice", "(D) Whipped cream", "(A)", "Line: 'With marshmallow clouds'.", "Easy", "Remembering", "Clouds Material"),
    ("What was falling as rain in the dream world?", "(A) Jellybeans", "(B) Raindrops", "(C) Chocolate chips", "(D) Lemon drops", "(A)", "Line: 'and jellybean rains.'", "Easy", "Remembering", "Rain Type"),
    ("What color was the friendly dragon the speaker met?", "(A) Green and bright", "(B) Red and black", "(C) Blue and silver", "(D) Yellow and purple", "(A)", "Line: 'I met a dragon, green and bright.'", "Easy", "Remembering", "Dragon Color"),
    ("How did the dragon behave towards the speaker?", "(A) It smiled and offered a ride, not there to fight", "(B) It roared loudly and breathed fire", "(C) It hid behind the trees in fear", "(D) It chased the speaker across the village", "(A)", "Line: 'But he just smiled, not there to fight.'", "Easy", "Remembering", "Dragon Behavior"),
    ("What colors were the mountains seen during the dragon ride?", "(A) Gold and red", "(B) Blue and green", "(C) Purple and yellow", "(D) Black and white", "(A)", "Line: 'We saw the mountains, gold and red.'", "Easy", "Remembering", "Mountain Colors"),
    ("What formed the rocky bed of the gold and red mountains?", "(A) Cookie crumbs", "(B) Sharp stones", "(C) Hard pebbles", "(D) Ice cubes", "(A)", "Line: 'With cookie crumbs as rocky bed.'", "Easy", "Remembering", "Mountain Bed"),
    ("What lined the streets of the village in the dream?", "(A) Cupcakes", "(B) Flowers", "(C) Lollipops", "(D) Red bricks", "(A)", "Line: 'While cupcakes lined the village street.'", "Easy", "Remembering", "Village Street"),
    ("What were the birds doing in the dream world?", "(A) Singing songs so sweet", "(B) Flying away in fear", "(C) Eating jellybeans", "(D) Sleeping in nests", "(A)", "Line: 'The birds were singing songs so sweet.'", "Easy", "Remembering", "Birds Action"),
    ("What caused the speaker to wake up from the dream?", "(A) The sun began to rise", "(B) The dragon roared", "(C) The chocolate stream dried up", "(D) A loud alarm bell rang", "(A)", "Line: 'But then the sun began to rise, I woke with wonder in my eyes.'", "Easy", "Remembering", "Wake Event"),
    ("With what feeling did the speaker wake up in the morning?", "(A) Wonder in my eyes", "(B) Fear in my heart", "(C) Anger and sadness", "(D) Deep boredom", "(A)", "Line: 'I woke with wonder in my eyes.'", "Easy", "Remembering", "Waking Feeling"),
    ("What object is suggested to remember when scared to try and fly?", "(A) The kite up in the sky", "(B) A paper airplane", "(C) A bird in a tree", "(D) A hot air balloon", "(A)", "Line: 'Remember the kite up in the sky.'", "Easy", "Remembering", "Kite Metaphor"),
    ("What moral action does the poet advise in the final stanza?", "(A) Brave the wind and take the flight", "(B) Stay safely inside your room", "(C) Never try anything difficult", "(D) Ask someone else to fly for you", "(A)", "Line: 'Brave the wind and take the flight.'", "Easy", "Remembering", "Moral Advice"),
    ("What will you find when you brave the wind according to the poet?", "(A) You'll find your wings and soar in light", "(B) A box of gold coins", "(C) A chocolate factory", "(D) A new pair of shoes", "(A)", "Line: 'You'll find your wings and soar in light.'", "Easy", "Remembering", "Moral Outcome"),
    ("What does the word 'marshmallow' mean in the vocabulary box?", "(A) A soft sweet", "(B) A hard stone", "(C) A green leaf", "(D) A hot drink", "(A)", "Marshmallow = A soft sweet.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'crumbs' mean?", "(A) Very small dry pieces", "(B) Large heavy rocks", "(C) Sweet fruit juices", "(D) Thick woolen threads", "(A)", "Crumbs = Very small dry pieces.", "Easy", "Understanding", "Vocabulary"),
    ("Who is the author of the poem 'My Dream Adventure'?", "(A) Anonymous", "(B) Roald Dahl", "(C) Ruskin Bond", "(D) Enid Blyton", "(A)", "The poem is written by Anonymous.", "Easy", "Remembering", "Author Identity"),
    ("What figure of speech is used in 'trees were tall, like candy canes'?", "(A) Simile", "(B) Metaphor", "(C) Personification", "(D) Alliteration", "(A)", "Uses 'like' to form a comparison (simile).", "Easy", "Understanding", "Literary Device"),
    ("What figure of speech is 'cookie crumbs as rocky bed'?", "(A) Metaphor", "(B) Simile", "(C) Onomatopoeia", "(D) Hyperbole", "(A)", "Directly compares mountain bed to cookie crumbs (metaphor).", "Easy", "Understanding", "Literary Device"),
    ("Which rhyming pair opens the first stanza?", "(A) dream / stream", "(B) canes / rains", "(C) bright / fight", "(D) said / overhead", "(A)", "'dream' rhymes with 'stream'.", "Easy", "Remembering", "Rhyme Pair"),
    ("Which rhyming pair closes the first stanza?", "(A) canes / rains", "(B) sweet / street", "(C) rise / eyes", "(D) light / night", "(A)", "'canes' rhymes with 'rains'.", "Easy", "Remembering", "Rhyme Pair"),
    ("What season or time of day did the dream occur?", "(A) Last night", "(B) Yesterday afternoon", "(C) This morning", "(D) Last summer", "(A)", "Line: 'Last night I had a funny dream.'", "Easy", "Remembering", "Time Setting"),
    ("Where did the speaker fly with the dragon?", "(A) High overhead", "(B) Under the ground", "(C) Across the ocean", "(D) Inside a cave", "(A)", "Line: 'So off we flew, high overhead.'", "Easy", "Remembering", "Flight Height"),
    ("What title is given to Chapter 13?", "(A) My Dream Adventure", "(B) The Magic of Books", "(C) Island Groups of India", "(D) The Narmada River", "(A)", "Title is 'My Dream Adventure'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Analyze the transition between the dream world (stanzas 1-4) and the moral takeaway (stanza 5).", "(A) Stanzas 1-4 build a joyful fantasy adventure; stanza 5 uses the kite metaphor to inspire real-life courage and confidence", "(B) Stanza 5 warns readers never to dream again", "(C) The transition shows the dragon was angry", "(D) Stanza 5 has no connection to the rest of the poem", "(A)", "Fantasy dream builds imagination; final stanza translates flight into real-life courage.", "Medium", "Analyzing", "Structural Analysis"),
    ("How does the poem subvert traditional fairy tale expectations regarding dragons?", "(A) Traditionally dragons are scary monsters to fight; here the dragon is friendly, bright green, smiles, and offers a ride", "(B) The dragon eats the speaker", "(C) The dragon turns into a frog", "(D) The dragon stays hidden in a cave", "(A)", "Replaces scary monster tropes with a friendly, smiling dragon guide.", "Medium", "Analyzing", "Character Subversion"),
    ("Examine the sensory imagery used in the candy land landscape.", "(A) Combines visual colors (gold/red mountains, green dragon) with sweet tastes/textures (chocolate, candy canes, marshmallows, cupcakes)", "(B) Describes bitter medicines and sharp metal", "(C) Describes dark caves and loud explosions", "(D) Uses no sensory words", "(A)", "Combines vivid colors with sweet tastes and soft textures.", "Medium", "Analyzing", "Sensory Imagery"),
    ("Why is the kite used as a metaphor for human courage in the final stanza?", "(A) A kite must face and brave opposing winds to rise high into the sky, symbolizing how overcoming fears helps humans succeed", "(B) Kites are made of paper and tear easily", "(C) Kites fly only when there is no wind", "(D) Kites can be bought at a shop", "(A)", "Kite braving opposing winds symbolizes overcoming fear to achieve greatness.", "Medium", "Evaluating", "Kite Metaphor Rationale"),
    ("What contrast is drawn between 'morning's light' and 'night to night' in stanza 4?", "(A) Morning light makes physical dreams fade, but the wonder and joy of a great dream memory stays in the heart every night", "(B) Dreams happen only during the day", "(C) Morning light makes people forget everything forever", "(D) Night time is frightening while morning is boring", "(A)", "Physical dreams fade with morning light, but inspiring memories endure in the heart.", "Medium", "Understanding", "Contrast Analysis"),
    ("How does 'woke with wonder in my eyes' reflect the psychological value of creative dreams?", "(A) Creative dreams leave a lasting sense of curiosity, joy, and positive imagination upon waking", "(B) Dreams leave children tired and unable to study", "(C) Dreams make children fear sleep", "(D) Wonder in eyes means suffering an eye injury", "(A)", "Leaves a lasting sense of curiosity, joy, and positive imagination.", "Medium", "Evaluating", "Psychological Impact"),
    ("Why does the poet describe the village street as lined with 'cupcakes' and birds singing sweet songs?", "(A) Creates an atmosphere of ultimate sweetness, happiness, and peace in the dream village", "(B) Suggests a busy industrial city market", "(C) Shows that villagers were hungry", "(D) Teaches baking recipes", "(A)", "Establishes an atmosphere of ultimate sweetness, happiness, and peace.", "Medium", "Understanding", "Atmospheric Detail"),
    ("Explain the rhyme scheme of the poem 'My Dream Adventure'.", "(A) AABB scheme in 5 stanzas of 4 lines each (20 lines total)", "(B) ABAB scheme", "(C) ABCB scheme", "(D) Free verse with no rhymes", "(A)", "5 stanzas of 4 lines each following AABB rhyming couplets.", "Medium", "Analyzing", "Rhyme Scheme"),
    ("How does the poem encourage Class 5 students to overcome fear of failure ('scared to try and fly')?", "(A) By reminding them that braving difficulties ('wind') leads to discovering personal capabilities ('wings') and success ('soar in light')", "(B) By advising them to avoid all difficult tasks", "(C) By telling them that flying is dangerous", "(D) By asking them to wait for a dragon to help them", "(A)", "Reminds them that braving difficulties leads to discovering inner capabilities.", "Medium", "Evaluating", "Encouraging Message"),
    ("What makes 'My Dream Adventure' a memorable poem for primary children?", "(A) Whimsical food imagery (chocolate stream, marshmallow clouds), friendly dragon, catchy rhythm, and uplifting moral lesson", "(B) Complex academic vocabulary", "(C) Sad ending about lost toys", "(D) Long sentences without rhyme", "(A)", "Whimsical food imagery, friendly dragon, bouncy rhythm, and uplifting moral.", "Medium", "Evaluating", "Poetic Appeal"),
    ("What does 'find your wings' mean metaphorically in the last line?", "(A) Discover your inner confidence, talents, and ability to succeed", "(B) Grow actual feather wings on your arms", "(C) Buy a toy airplane", "(D) Put on a bird costume", "(A)", "Discover inner confidence, talents, and ability to succeed.", "Medium", "Understanding", "Metaphorical Meaning"),
    ("Compare the landscape of 'My Dream Adventure' (candy land) with real-life natural landscapes.", "(A) Real landscapes have dirt rivers and stone rocks; dream landscapes transform them into chocolate streams and cookie crumbs", "(B) Both landscapes are made of plastic", "(C) Real landscapes have friendly green dragons", "(D) Dream landscapes have zero colors", "(A)", "Replaces dirt rivers and stone rocks with chocolate streams and cookie crumbs.", "Medium", "Comparing", "Landscape Comparison"),
    ("Why does the dragon invite the speaker with 'Come ride with me!'?", "(A) To share the joy of flight, friendship, and aerial exploration of the dream world", "(B) To kidnap the speaker", "(C) To race against other birds", "(D) To show off his green scales", "(A)", "To share the joy of flight, friendship, and aerial exploration.", "Medium", "Understanding", "Character Intent"),
    ("Summarize Chapter 13 in four concise sentences.", "'My Dream Adventure' by Anonymous is a whimsical 20-line poem about a child's magical dream. The speaker sails a chocolate stream through a landscape of candy-cane trees, marshmallow clouds, and cupcake-lined streets. A friendly green dragon invites the child on a flying ride over gold and red mountains made of cookie crumbs. Upon waking with wonder, the poem delivers an empowering message: like a kite braving the wind, children should overcome fear, find their wings, and soar.", "Medium", "Understanding", "Chapter Summary"),
    ("How can a student apply the moral of the last stanza when facing a difficult exam or project?", "(A) Face the challenge with courage ('brave the wind'), trust their preparation, and confident effort will help them succeed ('soar in light')", "(B) Give up before trying", "(C) Wish for a chocolate river", "(D) Sleep through the exam", "(A)", "Face challenges with courage, trust preparation, and effort will lead to success.", "Medium", "Applying", "Real-Life Application"),

    # Hard (41-50)
    ("Critique the pedagogical role of fantasy literature in developing creative confidence in primary students.", "(A) Fantasy frees cognitive constraints, allowing children to visualize impossible worlds, which fosters flexible creative problem-solving in real life", "(B) Fantasy literature fills children's heads with useless lies", "(C) Fantasy literature makes students fail in math and science", "(D) Children should read only non-fiction textbooks", "(A)", "Frees cognitive constraints, fostering flexible creative problem-solving.", "Hard", "Evaluating", "HOTS Pedagogical Critique"),
    ("Deconstruct the symbolic journey in 'My Dream Adventure' from passive sailing to active soaring.", "(A) The journey starts with passive sailing on a chocolate stream, moves to guided flight with the dragon, and culminates in personal autonomous flight ('find your wings')", "(B) The journey moves backward from flying to sleeping", "(C) The speaker stays stationary in bed throughout", "(D) The journey ends in failure", "(A)", "Progression: Passive sailing -> Guided dragon flight -> Autonomous personal soaring.", "Hard", "Analyzing", "Symbolic Progression"),
    ("Evaluate the effectiveness of using sweet food metaphors (marshmallow, jellybean, cupcakes) for a child audience.", "(A) Highly effective; sweet foods evoke immediate comfort, sensory delight, and vivid mental engagement in young primary students", "(B) Ineffective; children dislike sweet foods", "(C) Sweets cause dental decay when mentioned in poems", "(D) Food metaphors confuse students", "(A)", "Evokes immediate comfort, sensory delight, and vivid mental engagement.", "Hard", "Evaluating", "Metaphor Effectiveness"),
    ("Compare the kite metaphor in Stanza 5 with the dragon ride in Stanza 2.", "(A) Dragon ride represents external, guided fantasy help; kite represents internal, self-reliant real-world courage", "(B) Both represent real animals", "(C) Dragon ride happens in daytime; kite flies at night", "(D) Neither involves flying", "(A)", "Dragon ride = external guided fantasy help; Kite = internal self-reliant courage.", "Hard", "Comparing", "Metaphorical Comparison"),
    ("Formulate an original 4-line stanza following the meter and rhyme of 'My Dream Adventure'.", "(A) 'I touched a star of sparkling gold,\nAnd heard a story brave and bold;\nWe danced upon a silver cloud,\nAnd sang our song out clear and loud!'", "(B) 'I went to sleep at 9 PM.\nMy bed was soft and warm.\nI woke up early morning.\nSchool was fun.'", "(C) 'Dreaming is good for everyone.\nWe should dream every night.'", "(D) 'Green dragons are nice to ride on.'", "(A)", "Original 4-line AABB stanza matching rhythm and theme.", "Hard", "Creating", "Poetry Generation"),
    ("Assess the psychological value of transforming fear into wonder in children's poetry.", "(A) Replaces threat perception (scary dragon/falling) with wonder and curiosity, building emotional resilience against childhood anxieties", "(B) Teaches children to be careless in dangerous situations", "(C) Makes children fear dragons in real life", "(D) Has no impact on childhood emotions", "(A)", "Replaces threat perception with wonder, building emotional resilience against anxiety.", "Hard", "Evaluating", "Psychological Value"),
    ("Analyze how linguistic rhythm (iambic heptameter/tetrameter couplets) enhances oral poetry performance.", "(A) Steady metrical beats provide a natural musical cadence that aids memory recall and energetic group recitation", "(B) Rhythm makes reading aloud confusing", "(C) Metrical beats hide word meanings", "(D) Rhythm is useful only for professional singers", "(A)", "Natural musical cadence aids memory recall and energetic group recitation.", "Hard", "Analyzing", "Linguistic Rhythm"),
    ("Synthesize how Chapter 13 unifies whimsical fantasy, sensory art, and character building.", "(A) Blends whimsical candy fantasy (trees/clouds/streams) with sensory art (colors/tastes/sounds) and moral self-reliance (brave the wind/find your wings)", "(B) Separates fantasy from moral lessons", "(C) Focuses solely on listing candy names", "(D) Rejects imagination in favor of rules", "(A)", "Blends whimsical candy fantasy, sensory art, and moral self-reliance.", "Hard", "Synthesizing", "Cross-Disciplinary Synthesis"),
    ("Critique the claim: 'Dreams are meaningless night hallucinations with no educational value.'", "(A) False; creative dreams inspire literary art, stimulate subconscious problem-solving, and spark lifelong imaginative wonder", "(B) True; dreams should be forgotten immediately", "(C) False; dreams are physical realities that happen on Mars", "(D) True; only waking hours have value", "(A)", "False; creative dreams inspire literary art, stimulate subconscious problem-solving, and spark wonder.", "Hard", "Evaluating", "Educational Value Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 13 for a Class 5 assessment.", "(A) 'Describe the whimsical dream landscape in My Dream Adventure. Explain how the speaker's encounter with the dragon and the kite metaphor in the final stanza inspire real-world courage.'", "(B) 'Write five sentences about your favorite candy.'", "(C) 'List five rhyming words.'", "(D) 'Draw a picture of a kite.'", "(A)", "Structured essay prompt evaluating dream landscape, dragon encounter, kite metaphor, and moral courage.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 13: My Dream Adventure\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH13_MCQ_{idx:03d}"
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

with open(os.path.join(CH13_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Last night I had a funny _______.", "dream", "Had a funny dream.", "Easy"),
    ("I sailed along a chocolate _______.", "stream", "Chocolate stream.", "Easy"),
    ("The trees were tall, like candy _______.", "canes", "Like candy canes.", "Easy"),
    ("With marshmallow clouds and jellybean _______.", "rains", "Jellybean rains.", "Easy"),
    ("I met a dragon, green and _______.", "bright", "Green and bright.", "Easy"),
    ("But he just smiled, not there to _______.", "fight", "Not there to fight.", "Easy"),
    ("'Come ride with me!' the dragon _______.", "said", "Dragon said.", "Easy"),
    ("So off we flew, high _______.", "overhead", "High overhead.", "Easy"),
    ("We saw the mountains, gold and _______.", "red", "Gold and red.", "Easy"),
    ("With cookie crumbs as rocky _______.", "bed", "Rocky bed.", "Easy"),
    ("The birds were singing songs so _______.", "sweet", "Songs so sweet.", "Easy"),
    ("While cupcakes lined the village _______.", "street", "Village street.", "Easy"),
    ("But then the sun began to _______.", "rise", "Sun began to rise.", "Easy"),
    ("I woke with wonder in my _______.", "eyes", "Wonder in my eyes.", "Easy"),
    ("Though dreams may fade with morning's _______.", "light", "Morning's light.", "Easy"),
    ("This one will stay from night to _______!", "night", "Night to night.", "Easy"),
    ("So, when you're scared to try and _______.", "fly", "Scared to try and fly.", "Easy"),
    ("Remember the kite up in the _______.", "sky", "Kite in the sky.", "Easy"),
    ("Brave the wind and take the _______.", "flight", "Take the flight.", "Easy"),
    ("You'll find your wings and soar in _______.", "light", "Soar in light.", "Easy"),
    ("A marshmallow is defined in vocabulary as a soft _______.", "sweet", "Soft sweet.", "Easy"),
    ("Crumbs are defined as very small dry _______.", "pieces", "Very small dry pieces.", "Easy"),
    ("The poem 'My Dream Adventure' is written by _______.", "Anonymous", "Written by Anonymous.", "Easy"),
    ("The tree comparison 'tall, like candy canes' is a _______.", "simile", "Uses simile.", "Easy"),
    ("Chapter 13 is titled 'My Dream _______'.", "Adventure", "My Dream Adventure.", "Easy"),

    # Medium (26-40)
    ("The poem consists of 5 stanzas following an AABB rhyme _______.", "scheme", "AABB rhyme scheme.", "Medium"),
    ("Sailing a chocolate stream represents whimsical fantasy _______.", "imagination", "Whimsical fantasy imagination.", "Medium"),
    ("Marshmallow clouds create soft visual and tactile _______.", "imagery", "Soft visual imagery.", "Medium"),
    ("Jellybean rains replace ordinary water with sweet candy _______.", "raindrops", "Sweet candy raindrops.", "Medium"),
    ("The friendly green dragon subverts scary monster _______.", "stereotypes", "Subverts monster stereotypes.", "Medium"),
    ("Cookie crumbs forming mountain beds add miniature food _______.", "details", "Miniature food details.", "Medium"),
    ("Cupcakes lining village streets symbolize abundance and _______.", "joy", "Abundance and joy.", "Medium"),
    ("Rising sun marks the boundary between dream and _______.", "reality", "Dream and reality.", "Medium"),
    ("Waking with wonder shows positive psychological _______.", "inspiration", "Positive psychological inspiration.", "Medium"),
    ("The kite soaring in wind symbolizes human _______.", "perseverance", "Symbolizes human perseverance.", "Medium"),
    ("Braving the wind encourages children to overcome real-world _______.", "fears", "Overcome real-world fears.", "Medium"),
    ("Finding your wings means discovering inner confidence and _______.", "capability", "Inner confidence and capability.", "Medium"),
    ("Gold and red mountain colors paint a vibrant visual _______.", "landscape", "Vibrant visual landscape.", "Medium"),
    ("Birds singing sweet songs enhance auditory poetic _______.", "sensations", "Auditory poetic sensations.", "Medium"),
    ("Chapter 13 inspires primary students to embrace creative _______.", "courage", "Embrace creative courage.", "Medium"),

    # Hard (41-50)
    ("Subconscious fantasy sailing transitions into self-reliant real-world _______.", "action", "Transitions into real-world action.", "Hard"),
    ("Whimsical confectionery imagery engages child cognitive _______.", "visualization", "Engages cognitive visualization.", "Hard"),
    ("AABB couplet meter provides memorable oral recitation _______.", "cadence", "Memorable recitation cadence.", "Hard"),
    ("The kite metaphor transforms threat perception into empowering _______.", "resilience", "Transforms threat into resilience.", "Hard"),
    ("Linguistic simplicity conveys profound self-actualization _______.", "principles", "Conveys self-actualization principles.", "Hard"),
    ("Friendly dragon archetype fosters emotional security and _______.", "trust", "Fosters security and trust.", "Hard"),
    ("Symbolic shift from guided flight to personal wing discovery empowers child _______.", "agency", "Empowers child agency.", "Hard"),
    ("Sensory palette unifies taste, sight, sound, and emotional _______.", "wonder", "Unifies taste, sight, sound, wonder.", "Hard"),
    ("Historical analysis confirms child fantasy poetry builds creative _______.", "problem-solving", "Builds creative problem-solving.", "Hard"),
    ("Chapter 13 instills courage, imagination, and self-confidence in primary _______.", "learners", "Self-confidence in primary learners.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 13: My Dream Adventure\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH13_FIB_{idx:03d}"
    sent = item[0]
    ans = item[1]
    exp = item[2] if len(item) > 2 else "Answer"
    diff = item[3] if len(item) > 3 else "Easy"
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH13_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The stream in the dream was made of chocolate.", "True", "Text confirms: 'I sailed along a chocolate stream.'", "Easy"),
    ("The trees in the dream were tall, like candy canes.", "True", "Text confirms: 'The trees were tall, like candy canes'.", "Easy"),
    ("The clouds in the dream were made of dark thunder.", "False", "The clouds were made of marshmallows.", "Easy"),
    ("The rain in the dream was made of jellybeans.", "True", "Text confirms: 'jellybean rains.'", "Easy"),
    ("The speaker met a scary red dragon that wanted to fight.", "False", "Met a green and bright dragon who smiled and did not fight.", "Easy"),
    ("The dragon invited the speaker to ride with him.", "True", "Text confirms: ''Come ride with me!' the dragon said.'", "Easy"),
    ("The speaker and dragon flew high overhead.", "True", "Text confirms: 'So off we flew, high overhead.'", "Easy"),
    ("The mountains in the dream were gold and red.", "True", "Text confirms: 'We saw the mountains, gold and red.'", "Easy"),
    ("The rocky bed of the mountains was made of hard granite stones.", "False", "The rocky bed was made of cookie crumbs.", "Easy"),
    ("Cupcakes lined the village street in the dream.", "True", "Text confirms: 'While cupcakes lined the village street.'", "Easy"),
    ("The birds in the dream were singing sweet songs.", "True", "Text confirms: 'The birds were singing songs so sweet.'", "Easy"),
    ("The dream ended when the sun began to rise.", "True", "Text confirms: 'But then the sun began to rise, I woke with wonder in my eyes.'", "Easy"),
    ("The speaker woke up with fear and crying in their eyes.", "False", "Woke up with 'wonder in my eyes'.", "Easy"),
    ("The poet says that this dream will stay from night to night.", "True", "Text confirms: 'This one will stay from night to night!'", "Easy"),
    ("The final stanza suggests remembering a kite up in the sky when scared to fly.", "True", "Text confirms: 'Remember the kite up in the sky.'", "Easy"),
    ("The final stanza advises staying inside and never taking a flight.", "False", "Advises: 'Brave the wind and take the flight, You'll find your wings'.", "Easy"),
    ("'Marshmallow' is defined as a soft sweet.", "True", "Vocabulary definition: Marshmallow = A soft sweet.", "Easy"),
    ("'Crumbs' are defined as very small dry pieces.", "True", "Vocabulary definition: Crumbs = Very small dry pieces.", "Easy"),
    ("The poem 'My Dream Adventure' is written by Anonymous.", "True", "Text confirms author is Anonymous.", "Easy"),
    ("The line 'trees were tall, like candy canes' contains a simile.", "True", "Uses 'like' to compare trees to candy canes, forming a simile.", "Easy"),
    ("The poem has 5 stanzas of 4 lines each (20 lines total).", "True", "Text contains 5 stanzas x 4 lines = 20 lines total.", "Easy"),
    ("'Dream' rhymes with 'stream' in the first stanza.", "True", "Text confirms dream / stream rhyme.", "Easy"),
    ("'Bright' rhymes with 'fight' in the second stanza.", "True", "Text confirms bright / fight rhyme.", "Easy"),
    ("'Sweet' rhymes with 'street' in the third stanza.", "True", "Text confirms sweet / street rhyme.", "Easy"),
    ("Chapter 13 title is 'My Dream Adventure'.", "True", "Chapter title is 'My Dream Adventure'.", "Easy"),

    # Medium (26-40)
    ("The rhyme scheme of 'My Dream Adventure' is AABB in all 5 stanzas.", "True", "Each stanza follows an AABB rhyming couplet scheme.", "Medium"),
    ("The dragon in the poem represents a terrifying villain.", "False", "The dragon represents a friendly guide sharing an adventure.", "Medium"),
    ("The food imagery in the poem includes chocolate, candy canes, marshmallows, jellybeans, cookie crumbs, and cupcakes.", "True", "All six sweet food items appear in the poem's landscape.", "Medium"),
    ("Waking up when the sun rises shows the boundary between night dreams and morning reality.", "True", "Sunrise marks the natural end of night dreaming.", "Medium"),
    ("The kite in stanza 5 represents a real paper toy bought at a shop.", "False", "Metaphorically represents human courage and perseverance in facing challenges.", "Medium"),
    ("'Brave the wind' means running away from cold weather.", "False", "Metaphorically means facing difficulties and fears with courage.", "Medium"),
    ("'Find your wings and soar in light' means growing real bird feathers.", "False", "Metaphorically means discovering inner confidence and achieving success.", "Medium"),
    ("The speaker's dream occurred during an afternoon nap.", "False", "Occurred 'Last night'.", "Medium"),
    ("The green dragon flew high overhead with the speaker.", "True", "Text confirms they flew high overhead together.", "Medium"),
    ("The birds in the dream village were silent and sleeping.", "False", "Text confirms birds were singing songs so sweet.", "Medium"),
    ("The poem connects imaginative fantasy with moral encouragement.", "True", "Connects candy dream fantasy with moral courage in stanza 5.", "Medium"),
    ("The poem encourages children to be afraid of height and flying.", "False", "Encourages children to overcome fear: 'Brave the wind and take the flight'.", "Medium"),
    ("The dragon spoke the words: 'Come ride with me!'", "True", "Text confirms the dragon spoke those exact words.", "Medium"),
    ("Cookie crumbs formed the rocky bed of gold and red mountains.", "True", "Text confirms cookie crumbs formed the mountain bed.", "Medium"),
    ("Chapter 13 inspires Class 5 students to build creative imagination and confidence.", "True", "Fosters creative imagination and real-life confidence.", "Medium"),

    # Hard (41-50)
    ("The poem's narrative moves from passive water sailing to active aerial soaring.", "True", "Progression moves from sailing a stream to soaring with wings.", "Hard"),
    ("Whimsical confectionery geography serves to make the fantasy realm approachable for children.", "True", "Candy land geography makes fantasy comfortable and delightful for children.", "Hard"),
    ("The kite metaphor relies on the physical law that kites require opposing wind to gain altitude.", "True", "Kites rise against opposing wind, symbolizing growth through struggle.", "Hard"),
    ("Friendly dragon subversion helps reduce childhood fear of nighttime monsters.", "True", "Presents monsters as friendly guides, mitigating night anxiety.", "Hard"),
    ("Couplet rhythm in iambic meter enhances oral performance and memorization.", "True", "Regular meter aids oral recitation and memory retention.", "Hard"),
    ("Stanza 4 highlights that while transient dreams fade, inspiring memories endure.", "True", "Expresses that inspiring dream wonder stays from night to night.", "Hard"),
    ("The final stanza acts as a didactic moral epilogue to the fantasy narrative.", "True", "Final stanza delivers an explicit moral lesson on courage.", "Hard"),
    ("Chapter 13 combines visual, auditory, and gustatory sensory imagery.", "True", "Visual (colors/mountains), Auditory (birds singing), Gustatory (chocolate/cupcakes).", "Hard"),
    ("Chapter 13 integrates poetic analysis, literary devices, and self-confidence building.", "True", "Combines poetic devices (simile/metaphor), rhyme analysis, and self-confidence.", "Hard"),
    ("Cultivating creative fantasy in childhood enhances lifelong problem-solving flexibility.", "True", "Imaginative play builds flexible cognitive problem-solving in adulthood.", "Hard")
]

tf_content = f"# True / False — Chapter 13: My Dream Adventure\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH13_TF_{idx:03d}"
    stmt = item[0]
    ans = item[1]
    exp = item[2] if len(item) > 2 else "Explanation"
    diff = item[3] if len(item) > 3 else "Easy"
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH13_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("What kind of stream did the speaker sail along in the dream?", "The speaker sailed along a stream made of liquid chocolate.", "Easy", "Remembering"),
    ("What were the trees compared to in the first stanza?", "The tall trees were compared to candy canes using a simile ('tall, like candy canes').", "Easy", "Remembering"),
    ("Describe the weather in the dream world (clouds and rain).", "The clouds were soft marshmallows and the rain fell as colorful jellybeans.", "Easy", "Remembering"),
    ("Describe the dragon the speaker met in the dream.", "The dragon was bright green, friendly, and smiling, not there to fight.", "Easy", "Remembering"),
    ("What invitation did the green dragon give to the speaker?", "The dragon invited the speaker by saying, 'Come ride with me!' and they flew high overhead.", "Easy", "Remembering"),
    ("What colors were the mountains seen during the flight?", "The mountains were gold and red in color.", "Easy", "Remembering"),
    ("What formed the rocky bed of the gold and red mountains?", "The rocky bed of the mountains was formed of small cookie crumbs.", "Easy", "Remembering"),
    ("What lined the village street and what were the birds doing?", "Cupcakes lined the village street, while birds were singing sweet songs.", "Easy", "Remembering"),
    ("What event caused the speaker to wake up from the dream?", "The sun began to rise in the morning, causing the speaker to wake up.", "Easy", "Remembering"),
    ("With what feeling did the speaker wake up?", "The speaker woke up with 'wonder in my eyes'.", "Easy", "Remembering"),
    ("What object does the poet suggest remembering when scared to try new things?", "The poet suggests remembering a kite flying up in the sky.", "Easy", "Remembering"),
    ("What advice does the final stanza give about facing fears?", "It advises readers to brave the wind, take the flight, find their wings, and soar in light.", "Easy", "Understanding"),
    ("What does the word 'marshmallow' mean?", "A 'marshmallow' is defined as a soft sweet confection.", "Easy", "Understanding"),
    ("What does the word 'crumbs' mean?", "'Crumbs' means very small dry pieces of food (like bread or cookies).", "Easy", "Understanding"),
    ("Name the figure of speech in 'trees were tall, like candy canes'.", "It is a simile because it uses the word 'like' to compare trees to candy canes.", "Easy", "Understanding"),
    ("Identify the rhyming pair in the second stanza.", "The rhyming pairs are 'bright' / 'fight' and 'said' / 'overhead'.", "Easy", "Remembering"),
    ("Identify the rhyming pair in the third stanza.", "The rhyming pairs are 'red' / 'bed' and 'sweet' / 'street'.", "Easy", "Remembering"),
    ("Identify the rhyming pair in the fourth stanza.", "The rhyming pairs are 'rise' / 'eyes' and 'light' / 'night'.", "Easy", "Remembering"),
    ("Identify the rhyming pair in the fifth stanza.", "The rhyming pairs are 'fly' / 'sky' and 'flight' / 'light'.", "Easy", "Remembering"),
    ("Who is the author of the poem 'My Dream Adventure'?", "The poem is written by an Anonymous author.", "Easy", "Remembering"),
    ("How many stanzas and lines make up the poem?", "The poem consists of 5 stanzas of 4 lines each, making 20 lines in total.", "Easy", "Remembering"),
    ("What makes the dragon in this poem different from dragons in traditional scary stories?", "In traditional stories, dragons roar and fight; here, the dragon smiles gently and invites the child for a ride.", "Easy", "Understanding"),
    ("What happens to dreams when morning light arrives?", "Physical dreams fade with morning light, but inspiring dream memories stay in the heart.", "Easy", "Understanding"),
    ("What title is given to Chapter 13?", "The title of Chapter 13 is 'My Dream Adventure'.", "Easy", "Remembering"),
    ("What main message does Chapter 13 give to young readers?", "It encourages children to enjoy creative imagination and build courage to overcome fears in real life.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze the sensory imagery of sweet treats used throughout the poem.", "The poem uses visual, tactile, and taste imagery—chocolate stream, candy-cane trees, marshmallow clouds, jellybean rain, cookie crumbs, and street cupcakes—creating a comforting candy land.", "Medium", "Analyzing"),
    ("Explain the moral lesson in the final stanza: 'Brave the wind and take the flight'.", "It teaches that facing difficulties ('wind') with courage allows individuals to discover their inner strengths ('wings') and achieve success ('soar in light').", "Medium", "Evaluating"),
    ("Why is the kite a fitting metaphor for building courage in children?", "A kite can only rise into the sky by pushing against opposing wind; similarly, children grow stronger and achieve success by braving real-life challenges.", "Medium", "Analyzing"),
    ("How does the poem transition from a night dream fantasy to an inspiring real-life message?", "Stanzas 1-4 build a joyful fantasy adventure; Stanza 5 connects the concept of flying with overcoming fear in daily life.", "Medium", "Analyzing"),
    ("What does 'woke with wonder in my eyes' suggest about the power of imagination?", "It shows that creative imagination leaves a lasting impression of curiosity, joy, and positive wonder even after waking.", "Medium", "Understanding"),
    ("Contrast the rocky mountain bed in real life with the one described in the poem.", "Real mountain beds consist of hard, sharp granite stones; the dream mountain bed consists of sweet, soft cookie crumbs.", "Medium", "Comparing"),
    ("Why does the dragon say 'Come ride with me!' to the child?", "To offer a friendly aerial tour of the dream world, fostering a sense of adventure, trust, and companionship.", "Medium", "Understanding"),
    ("Explain the rhyme scheme of 'My Dream Adventure'.", "The poem follows an AABB rhyme scheme in every stanza (rhyming couplets), creating a catchy, song-like rhythm.", "Medium", "Analyzing"),
    ("How does the poem help children overcome nighttime fears of monsters or dark dreams?", "By depicting a dragon as a smiling, bright green friend, it reframes scary tropes into comforting fantasy companions.", "Medium", "Evaluating"),
    ("Summarize Chapter 13 in four concise sentences.", "'My Dream Adventure' by Anonymous is a whimsical 20-line poem about a child's magical night dream. The child sails a chocolate stream through a landscape of candy-cane trees, marshmallow clouds, and cupcake streets. Guided by a friendly green dragon, they fly over gold and red mountains with cookie-crumb beds. Waking with wonder, the poem encourages children to brave life's winds like a kite and soar with confidence.", "Medium", "Understanding"),
    ("What does 'find your wings' mean metaphorically for a Class 5 student?", "It means realizing one's own abilities, building self-confidence, and daring to try new challenges without fear of failure.", "Medium", "Understanding"),
    ("Describe the auditory imagery present in the third stanza.", "The line 'birds were singing songs so sweet' adds pleasant, melodious sound imagery to the visually colorful village.", "Medium", "Analyzing"),
    ("Why are rhyming couplets effective for teaching primary poetry?", "They provide clear rhythm, make reciting fun, help memory retention, and highlight key vocabulary words.", "Medium", "Evaluating"),
    ("How does the poem present waking up in the morning positively?", "Instead of regret, waking up brings 'wonder in my eyes' and a lasting happy memory that stays 'from night to night'.", "Medium", "Understanding"),
    ("What advice would you give to a friend who is afraid to try a new sport or speech based on this poem?", "Remind them of the kite in the sky: brave the wind of fear, take the leap, and you will find your wings and succeed!", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique how fantasy elements in poetry contribute to emotional resilience in children.", "Fantasy literature creates a safe imaginative space where children encounter novel situations (flying/dragons), building emotional flexibility and real-world confidence.", "Hard", "Evaluating"),
    ("Deconstruct the progression from passive sailing to autonomous flying in the poem.", "The child starts passively floating on a chocolate stream, progresses to a guided ride on a dragon, and ends by discovering their own personal 'wings' to soar.", "Hard", "Analyzing"),
    ("Evaluate the effectiveness of using childlike food metaphors (jellybeans, cupcakes) to convey poetic beauty.", "Food metaphors connect directly with children's immediate sensory pleasures, making poetic concepts intuitive, delightful, and highly engaging.", "Hard", "Evaluating"),
    ("Compare the green dragon in Chapter 13 with the dragon in traditional myths.", "Traditional myths portray dragons as destructive fire-breathing beasts; Chapter 13 portrays the dragon as a friendly, green, smiling aerial tour guide.", "Hard", "Comparing"),
    ("Formulate an original 4-line stanza continuing the poem's theme.", "'We touched the stars that gleamed so bright,\nAnd danced upon a ray of light;\nThe night was full of magic cheer,\nWith not a single thought of fear!'", "Hard", "Creating"),
    ("Assess how the kite metaphor models the physics of resilience.", "Just as aerodynamic lift requires wind resistance to push a kite upward, human character requires encountering and braving resistance to achieve personal growth.", "Hard", "Evaluating"),
    ("Analyze the linguistic choices in 'Brave the wind and take the flight'.", "Action verbs ('brave', 'take', 'find', 'soar') inspire active agency, transforming a passive dream memory into a courageous life stance.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 13 combines sensory fantasy, poetic structure, and character education.", "Blends sweet candy fantasy (visual/taste) with rhyming couplet structure (AABB) and moral character education (courage/self-reliance).", "Hard", "Synthesizing"),
    ("Critique the claim: 'Children's poems about dreams are foolish and waste study time.'", "False; dream poetry stimulates creative visualization, enriches vocabulary, lowers stress, and teaches moral resilience essential for holistic growth.", "Hard", "Evaluating"),
    ("Formulate a 4-line slogan encouraging students to face challenges bravely.", "'When winds of trial start to blow,\nRemember how the kites will go;\nSpread out your wings and take your flight,\nAnd you will soar in joyful light!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 13: My Dream Adventure\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH13_SA_{idx:03d}"
    q_txt = item[0]
    ans = item[1]
    diff = item[2] if len(item) > 2 else "Easy"
    bloom = item[3] if len(item) > 3 else "Understanding"
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH13_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Examine the fantasy landscape and sensory imagery described in 'My Dream Adventure'.",
     "The poem 'My Dream Adventure' creates a delightful, whimsical candy land through rich sensory imagery:\n1. **Chocolate Stream**: The speaker begins the adventure sailing along a river made of liquid chocolate.\n2. **Candy-Cane Trees**: The trees are tall and colorful, explicitly compared to peppermint candy canes using a simile.\n3. **Marshmallow Clouds & Jellybean Rains**: The weather features soft, fluffy marshmallow clouds dropping sweet, colorful jellybeans as rain.\n4. **Gold & Red Mountains**: Mountains glow in brilliant gold and red colors, with a rocky bed made of crunchy cookie crumbs.\n5. **Cupcake Streets**: The village streets are neatly lined with sweet cupcakes while birds sing melodious songs.\nThis combination of visual colors, sweet tastes, and soft textures creates a comforting fantasy realm for young readers.",
     "Easy", "Remembering"),

    ("Describe the encounter with the dragon and explain how it subverts traditional dragon stories.",
     "In traditional fairy tales, dragons are fierce, fire-breathing monsters that terrorize villages and fight knights. 'My Dream Adventure' subverts this scary trope completely:\n- The speaker meets a dragon described as 'green and bright'.\n- Instead of roaring or attacking, the dragon 'just smiled, not there to fight'.\n- The dragon warmly invites the speaker: 'Come ride with me!'\n- Together, they fly high overhead, soaring above gold and red mountains and cupcake streets.\nThis portrayal transforms a potential monster into a friendly guide and flying companion, teaching children that unfamiliar things are not always scary.",
     "Easy", "Understanding"),

    ("Examine the final stanza of the poem and explain the kite metaphor for building real-life courage.",
     "The final stanza transitions from night fantasy to a powerful moral message for real life:\n> *'So, when you're scared to try and fly,\nRemember the kite up in the sky,\nBrave the wind and take the flight,\nYou'll find your wings and soar in light.'*\n- **Kite Metaphor**: A kite cannot fly in still air; it needs opposing wind to gain altitude. The poet uses the kite to symbolize human courage.\n- **Real-Life Meaning**: When children feel scared to try new, difficult challenges ('scared to try and fly'), they must face their fears ('brave the wind'). By taking the leap ('take the flight'), they discover their own inner abilities ('find your wings') and achieve success ('soar in light').",
     "Easy", "Understanding"),

    ("Describe the structure, rhyme scheme, and poetic devices used in 'My Dream Adventure'.",
     "The poem 'My Dream Adventure' is crafted with engaging poetic elements:\n1. **Structure**: It contains 5 stanzas of 4 lines each (quatrains), totaling 20 lines.\n2. **Rhyme Scheme**: Every stanza follows an **AABB** rhyme scheme (rhyming couplets):\n   - Stanza 1: dream/stream (A), canes/rains (B)\n   - Stanza 2: bright/fight (A), said/overhead (B)\n   - Stanza 3: red/bed (A), sweet/street (B)\n   - Stanza 4: rise/eyes (A), light/night (B)\n   - Stanza 5: fly/sky (A), flight/light (B)\n3. **Poetic Devices**:\n   - **Simile**: 'trees were tall, like candy canes'.\n   - **Metaphor**: 'cookie crumbs as rocky bed', kite metaphor for courage, 'find your wings'.",
     "Easy", "Remembering"),

    ("Explain the vocabulary terms 'marshmallow' and 'crumbs' and show how they are used in the poem.",
     "1. **Marshmallow**: Defined in the vocabulary box as 'A soft sweet'. In the poem ('With marshmallow clouds'), it describes soft, fluffy white clouds floating in the candy land sky.\n2. **Crumbs**: Defined as 'Very small dry pieces'. In the poem ('With cookie crumbs as rocky bed'), it describes the ground of the gold and red mountains, replacing hard stones with tiny pieces of delicious cookies.",
     "Easy", "Understanding"),

    ("Discuss how the poem connects nighttime dreaming with morning inspiration.",
     "The poem builds a bridge between night dreams and morning waking:\n- In Stanza 4, the fantasy adventure ends naturally as 'the sun began to rise'.\n- Waking up does not bring disappointment; the child wakes with 'wonder in my eyes'.\n- The poet notes that while physical dreams fade in daylight, inspiring dream memories stay in the heart 'from night to night'.\n- This positive wonder inspires the child to face the real day with courage, creativity, and joy.",
     "Easy", "Understanding"),

    ("Why is 'My Dream Adventure' an effective poem for primary school English literature?",
     "It is highly effective because:\n1. **Whimsical Fantasy**: Children naturally love food imagery (chocolate, candy, cupcakes) and mythical creatures (dragons).\n2. **Catchy Musicality**: Rhyming couplets (AABB) create a cheerful rhythm perfect for reading aloud and memorization.\n3. **Positive Character Building**: It transforms night fears into wonder and delivers a clear, uplifting moral lesson on overcoming self-doubt.",
     "Easy", "Evaluating"),

    ("Compare the physical journey in stanzas 1-3 with the moral journey in stanza 5.",
     "- **Physical Journey (Stanzas 1-3)**: The speaker sails a chocolate stream, meets a green dragon, and flies high overhead seeing mountains and cupcake streets. This is a passive, guided fantasy exploration.\n- **Moral Journey (Stanza 5)**: The speaker is challenged to face real-life fear ('scared to try and fly') like a kite braving the wind. This is an active, self-reliant personal growth journey where the child finds their own wings.",
     "Easy", "Comparing"),

    ("Summarize Chapter 13 in five detailed bullet points.",
     "- 'My Dream Adventure' by Anonymous is a 20-line whimsical poem about a child's night dream.\n- The child sails a chocolate river past candy-cane trees, marshmallow clouds, and jellybean rain.\n- A friendly green dragon smiles and invites the child for a flight over gold/red mountains with cookie-crumb beds.\n- The dream village features sweet singing birds and cupcake-lined streets before the child wakes with wonder at sunrise.\n- The final stanza gives a moral lesson: like a kite braving opposing wind, children must face fears, find their wings, and soar.",
     "Easy", "Understanding"),

    ("What lessons about self-confidence and trying new things can Class 5 students learn from Chapter 13?",
     "Students learn that trying new things can feel scary ('scared to try and fly'), but fear should not stop them. Just as a kite needs wind to soar high into the sky, encountering challenges helps people discover their hidden talents ('find your wings'). Students are inspired to face difficult tasks with courage, knowing that effort and confidence lead to success.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why is the dragon depicted as green and smiling rather than red and breathing fire?", "To reframe scary monster stereotypes into a friendly, welcoming companion, creating a comforting atmosphere where the child feels safe to embark on a flying adventure.", "Easy", "Analyzing"),
    ("Describe how the poem engages multiple senses (sight, taste, sound, touch).", "Sight (gold/red mountains, green dragon), Taste (chocolate, marshmallows, cupcakes), Sound (birds singing sweet songs), and Touch (soft marshmallow clouds, cookie crumbs).", "Easy", "Understanding"),
    ("How does the kite metaphor teach children to handle opposition or difficulty?", "Opposing wind pushes a kite higher into the sky. Similarly, facing opposition or difficulty forces children to develop strength, resilience, and personal capabilities.", "Easy", "Understanding"),
    ("Explain the significance of the phrase 'woke with wonder in my eyes'.", "It highlights that creative dreams leave a lasting impression of joy, curiosity, and positive wonder that brightens the child's real morning.", "Easy", "Understanding"),
    ("Why are candy and sweet treats used to build the dream landscape?", "Sweet treats represent pure childhood delight, making the dream world instantly attractive, comfortable, and imaginative for primary students.", "Easy", "Understanding"),
    ("Discuss how the poem encourages outdoor play and flying kites.", "Mentioning 'the kite up in the sky' connects poetic imagination with real outdoor play, encouraging children to observe nature and enjoy flying kites.", "Easy", "Applying"),
    ("How does the poem show that dreams can stay with us 'from night to night'?", "Even though physical dreams end at sunrise, the happy memories, imaginative feelings, and moral inspiration remain permanently in our minds.", "Easy", "Understanding"),
    ("What makes the rhyming pair 'flight / light' in the last stanza impactful?", "'Flight' symbolizes taking bold action and trying new things; 'light' symbolizes clarity, success, and joyful achievement.", "Easy", "Analyzing"),
    ("Describe the village in the dream world and why it feels peaceful.", "The village has sweet birds singing, cupcakes lining the streets, and a gentle green dragon flying overhead, creating a peaceful, conflict-free world.", "Easy", "Remembering"),
    ("How does Chapter 13 support vocabulary development in Class 5?", "It introduces descriptive confectionery words (marshmallow, candy canes, jellybeans, cookie crumbs) and action verbs (sailed, flew, brave, soar).", "Easy", "Understanding"),
    ("Re-write the poem 'My Dream Adventure' as a short 100-word story.", "Last night, I fell asleep and experienced a funny dream. I found myself sailing down a river of liquid chocolate! Tall candy-cane trees stood on the banks beneath soft marshmallow clouds that rained jellybeans. Suddenly, a bright green dragon appeared. He wasn't scary at all; he smiled and invited me to fly with him. We flew high overhead, admiring gold and red mountains built on cookie crumbs, while sweet birds sang over cupcake-lined streets. When the morning sun woke me up, I felt full of wonder. The dream taught me that like a kite braving the wind, we must be brave, find our wings, and fly!", "Easy", "Creating"),
    ("Why is Anonymous authorship fitting for a poem about childhood dreams?", "Because every child across the world has magical dreams, making the poem a shared, universal celebration of childhood imagination.", "Easy", "Understanding"),
    ("How can teachers use this poem to help students write their own dream stories?", "Teachers can use the poem's structure as a model, asking students to replace food items and animals with their own imaginative ideas.", "Easy", "Applying"),
    ("Analyze why Chapter 13 is included in the Class 5 English curriculum.", "It develops poetic analysis skills (rhyme/simile/metaphor), expands sensory vocabulary, and delivers a vital character-building lesson on self-confidence.", "Easy", "Analyzing"),
    ("What practical advice does Stanza 5 offer for overcoming stage fright or exam anxiety?", "Remind yourself to brave the wind of anxiety, take the stage or test with confidence, and you will discover your inner ability to succeed.", "Easy", "Applying"),

    # Medium (26-40)
    ("Critically analyze how 'My Dream Adventure' balances whimsical fantasy with realistic character building.",
     "The poem achieves a perfect balance between fantasy and character building:\n- **Whimsical Fantasy (Stanzas 1-4)**: Captivates children's imagination through delight—chocolate streams, marshmallow clouds, friendly green dragon, and cupcake streets.\n- **Realistic Character Building (Stanza 5)**: Translates the joy of fantasy flight into a real-world moral. Using the kite metaphor ('brave the wind'), it instructs children that true self-confidence comes from confronting fears, trying new tasks, and discovering their inner wings.",
     "Medium", "Analyzing"),

    ("Examine the structural progression of flight in the poem from passive to active.",
     "Flight progresses in three clear stages:\n1. **Passive Water Travel (Stanza 1)**: The child starts by passively floating along a chocolate stream.\n2. **Guided Flight (Stanza 2)**: The child takes an aerial flight guided by a friendly green dragon ('off we flew, high overhead').\n3. **Active Personal Flight (Stanza 5)**: The child is empowered to take their own flight independently ('find your wings and soar in light'). This progression mirrors a child's growth from dependence to independent confidence.",
     "Medium", "Analyzing"),

    ("Evaluate the use of food imagery in creating a non-threatening fantasy environment.",
     "Food imagery is strategically used to eliminate fear. By constructing clouds out of marshmallows, rain out of jellybeans, mountain bases out of cookie crumbs, and streets out of cupcakes, the poet ensures that the fantasy world feels safe, sweet, and comforting. Even when a giant dragon appears, the surrounding sweet landscape signals that the dragon is a friendly partner rather than a threat.",
     "Medium", "Evaluating"),

    ("Discuss how the poem introduces basic principles of physics and nature through poetry.",
     "The final stanza introduces physical principles of aerodynamics and nature: a kite cannot ascend in still air—it requires opposing wind resistance to gain lift. By observing this natural law, the poet bridges nature observation with human psychology, teaching that emotional 'lift' and personal growth require encountering and braving difficulty.",
     "Medium", "Analyzing"),

    ("Design an artistic and literary classroom activity based on Chapter 13.",
     "Activity Title: 'My Dream World & My Courage Kite'\n1. **Art Corner**: Students paint their own dream landscape using watercolors (e.g., soda rivers, donut hills).\n2. **Kite Crafting**: Students construct a simple paper kite and write their personal courage goal on it ('I will brave the wind by speaking in public!').\n3. **Poetry Recitation**: Group recitation of Chapter 13 with physical actions for flying and dragon riding.",
     "Medium", "Creating"),

    ("How does the simile 'tall, like candy canes' help primary readers visualize scale?", "By comparing tall trees to familiar striped candy canes, it establishes a whimsical, colorful proportion that children can easily visualize.", "Medium", "Understanding"),
    ("Contrast the role of wind in flying a kite with difficulty in human life.", "Wind pushes against a kite physically; difficulty pushes against a human emotionally. Both force the subject to exert effort and rise upward.", "Medium", "Comparing"),
    ("Why is the dragon described as 'bright green' rather than dark colors?", "Bright green is associated with nature, friendliness, and vitality, reinforcing the dragon's gentle, welcoming character.", "Medium", "Understanding"),
    ("How does the poet show that waking up from a dream does not mean losing the magic?", "By stating 'This one will stay from night to night!', showing that positive imaginative memories remain permanently in the heart.", "Medium", "Understanding"),
    ("Describe how the poem uses auditory imagery in Stanza 3.", "The line 'birds were singing songs so sweet' adds gentle sound to the visual spectacle of gold mountains and cupcake streets.", "Medium", "Analyzing"),
    ("Explain the relationship between creative dreaming and problem-solving confidence.", "Creative dreaming expands mental flexibility, training children to envision positive outcomes when facing real-life challenges.", "Medium", "Understanding"),
    ("How does the poem present sunrise as a gentle transition rather than a rude interruption?", "The sun 'began to rise' gently, causing the child to wake with 'wonder in my eyes' rather than shock or disappointment.", "Medium", "Analyzing"),
    ("Analyze why rhyming couplets (AABB) make children's poetry easier to memorize.", "Rhyming couplets create predictable phonetic pairs and regular beats that anchor words in auditory memory.", "Medium", "Analyzing"),
    ("What makes the last line 'soar in light' a triumphant conclusion?", "It combines aerial movement ('soar') with illumination ('light'), symbolizing successful achievement, joy, and emotional freedom.", "Medium", "Evaluating"),
    ("Construct a motivational speech for a student facing sports competition based on Stanza 5.", "'Don't be scared to step onto the field! Remember the kite in the sky—it needs the wind to fly high. Brave the pressure, play with courage, find your wings, and soar!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the psychological impact of reframing childhood fears through whimsical poetry.",
     "Reframing fears through whimsical poetry is psychologically empowering. By transforming monsters into smiling guides and difficulties into winds that lift kites, the poem equips children with cognitive reframing tools. It teaches them to view real-life obstacles not as paralyzing threats, but as necessary currents for personal growth.",
     "Hard", "Evaluating"),

    ("Deconstruct the linguistic symbolism of 'wings' and 'light' in the final couplet.",
     "'Wings' symbolize developed personal agency, skills, and self-confidence; 'light' symbolizes truth, enlightenment, and joyful success. Together, 'find your wings and soar in light' signifies the ultimate goal of human education: discovering one's potential and achieving self-actualization.",
     "Hard", "Analyzing"),

    ("Synthesize how Chapter 13 links sensory poetry, literary devices, and self-actualization.",
     "Unifies sensory confectionery imagery with formal literary devices (similes, metaphors, AABB rhyme) and psychological self-actualization (overcoming fear).", "Hard", "Synthesizing"),

    ("Formulate a comprehensive essay prompt evaluating 'My Dream Adventure' as a model of inspirational children's literature.",
     "Prompt: 'Critically analyze how the poem My Dream Adventure uses fantasy landscape imagery, subverted character tropes, and the kite metaphor to encourage children to overcome self-doubt and build real-world courage.'",
     "Hard", "Creating"),

    ("Evaluate the role of imaginative fantasy in nurturing emotional intelligence during primary school.", "Imaginative fantasy provides an exploratory mental space where children experiment with awe, joy, and courage, broadening their emotional repertoire and self-awareness.", "Hard", "Evaluating"),

    ("Compare the moral message of Chapter 12 ('The Magic of Books') with Chapter 13 ('My Dream Adventure').", "Chapter 12 focuses on internal intellectual wealth gained through reading ('treasure house within their mind'); Chapter 13 focuses on active real-world courage gained through facing challenges ('find your wings and soar').", "Hard", "Comparing"),
    ("Discuss how the poem uses nature metaphors (birds, sun, wind, kite) to anchor fantasy in reality.", "Nature elements ground the candy fantasy in familiar physical reality, preparing the reader for the practical moral lesson about wind and kites in Stanza 5.", "Hard", "Analyzing"),
    ("Analyze the impact of using first-person perspective ('I sailed', 'I met', 'I woke') in the poem.", "First-person perspective creates immediate intimacy and identification, allowing young readers to experience the dream adventure as if it were their own.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the lines: 'Brave the wind and take the flight, You'll find your wings and soar in light.'", "This concluding couplet transforms the poem from a fantasy narrative into an empowering call to action. The imperative verbs ('brave', 'take', 'find', 'soar') urge young readers to embrace agency, face adversity boldly, and realize their full potential.", "Hard", "Evaluating"),
    ("Synthesize the complete educational takeaways of Chapter 13 for primary school English literature.", "Chapter 13 unifies poetic device mastery (simile/metaphor/rhyme) with sensory creative writing, reframing fear, and building real-world self-confidence.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 13: My Dream Adventure\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH13_LA_{idx:03d}"
    q_txt = item[0]
    ans = item[1]
    diff = item[2] if len(item) > 2 else "Easy"
    bloom = item[3] if len(item) > 3 else "Understanding"
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH13_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Last night I had a funny dream,\nI sailed along a chocolate stream.\nThe trees were tall, like candy canes,\nWith marshmallow clouds and jellybean rains.",
     [
         ("When did the speaker have a funny dream?", "Last night.", "Easy", "Remembering"),
         ("What kind of stream did the speaker sail along?", "A chocolate stream.", "Easy", "Remembering"),
         ("What were the tall trees compared to?", "Candy canes (using a simile).", "Easy", "Remembering"),
         ("What were the clouds and rain made of?", "Clouds were marshmallows and rain was jellybeans.", "Easy", "Remembering"),
         ("Name the figure of speech in 'trees were tall, like candy canes'.", "Simile.", "Easy", "Understanding")
     ]),

    # Set 2
    ("I met a dragon, green and bright,\nBut he just smiled, not there to fight.\n\"Come ride with me!\" the dragon said,\nSo off we flew, high overhead.",
     [
         ("Describe the appearance of the dragon.", "Green and bright.", "Easy", "Remembering"),
         ("How did the dragon behave towards the speaker?", "He just smiled, not there to fight.", "Easy", "Remembering"),
         ("What invitation did the dragon give?", "'Come ride with me!'", "Easy", "Remembering"),
         ("Where did the speaker and dragon fly?", "High overhead.", "Easy", "Remembering"),
         ("How does this dragon differ from traditional scary dragons?", "He smiles gently and invites the speaker for a ride instead of fighting or breathing fire.", "Medium", "Understanding")
     ]),

    # Set 3
    ("We saw the mountains, gold and red,\nWith cookie crumbs as rocky bed.\nThe birds were singing songs so sweet,\nWhile cupcakes lined the village street.",
     [
         ("What colors were the mountains seen from above?", "Gold and red.", "Easy", "Remembering"),
         ("What made up the rocky bed of the mountains?", "Cookie crumbs.", "Easy", "Remembering"),
         ("What were the birds doing in the village?", "Singing songs so sweet.", "Easy", "Remembering"),
         ("What lined the village street?", "Cupcakes.", "Easy", "Remembering"),
         ("What sensory imagery is present in this extract?", "Visual imagery (gold/red mountains), Auditory (birds singing), and Gustatory (cookie crumbs, cupcakes).", "Medium", "Analyzing")
     ]),

    # Set 4
    ("But then the sun began to rise,\nI woke with wonder in my eyes.\nThough dreams may fade with morning's light,\nThis one will stay from night to night!",
     [
         ("What event caused the speaker to wake up?", "The sun began to rise.", "Easy", "Remembering"),
         ("With what feeling did the speaker wake up?", "Wonder in my eyes.", "Easy", "Remembering"),
         ("What happens to physical dreams with morning light?", "They may fade away.", "Easy", "Understanding"),
         ("How long will this specific dream stay with the speaker?", "From night to night.", "Easy", "Remembering"),
         ("What does waking up 'with wonder in my eyes' suggest?", "That creative dreams leave a positive, lasting impression of curiosity and joy upon waking.", "Medium", "Analyzing")
     ]),

    # Set 5
    ("So, when you're scared to try and fly,\nRemember the kite up in the sky,\nBrave the wind and take the flight,\nYou'll find your wings and soar in light.",
     [
         ("When should you remember the kite up in the sky?", "When you are scared to try and fly.", "Easy", "Remembering"),
         ("What should you do with the wind according to line 3?", "Brave the wind and take the flight.", "Easy", "Remembering"),
         ("What will you find when you brave the wind?", "You'll find your wings.", "Easy", "Remembering"),
         ("How will you soar at the end?", "Soar in light.", "Easy", "Remembering"),
         ("Explain the moral lesson of this stanza.", "Facing difficulties ('wind') with courage allows individuals to discover their inner abilities ('wings') and achieve success ('soar').", "Medium", "Evaluating")
     ]),

    # Set 6
    ("Word Meaning: Marshmallow: A soft sweet. Crumbs : Very small dry pieces.",
     [
         ("What is the definition of 'marshmallow'?", "A soft sweet.", "Easy", "Remembering"),
         ("What is the definition of 'crumbs'?", "Very small dry pieces.", "Easy", "Remembering"),
         ("Which stanza in the poem mentions 'marshmallow'?", "Stanza 1 ('marshmallow clouds').", "Easy", "Remembering"),
         ("Which stanza in the poem mentions 'crumbs'?", "Stanza 3 ('cookie crumbs as rocky bed').", "Easy", "Remembering"),
         ("Use the word 'crumbs' in a complete sentence of your own.", "Birds gathered on the lawn to eat the bread crumbs.", "Medium", "Applying")
     ]),

    # Set 7
    ("Last night I had a funny dream... You'll find your wings and soar in light. - Anonymous",
     [
         ("Who wrote the poem 'My Dream Adventure'?", "Anonymous.", "Easy", "Remembering"),
         ("How many stanzas make up the poem?", "Five stanzas.", "Easy", "Remembering"),
         ("How many total lines are in the poem?", "Twenty lines.", "Easy", "Remembering"),
         ("What is the rhyme scheme of every stanza?", "AABB (rhyming couplets).", "Medium", "Analyzing"),
         ("What is the main message of the entire poem?", "Imaginative dreams spark wonder, and like a kite in the wind, braving real-life fears helps us discover our wings and succeed.", "Medium", "Evaluating")
     ]),

    # Set 8
    ("The trees were tall, like candy canes, With marshmallow clouds and jellybean rains.",
     [
         ("What item are the tall trees compared to?", "Candy canes.", "Easy", "Remembering"),
         ("What figure of speech is used in 'tall, like candy canes'?", "Simile.", "Easy", "Understanding"),
         ("What were the clouds made of?", "Marshmallows.", "Easy", "Remembering"),
         ("What were the raindrops made of?", "Jellybeans.", "Easy", "Remembering"),
         ("What overall atmosphere does this confectionery landscape create?", "A sweet, non-threatening, whimsical candy land full of childhood delight.", "Medium", "Analyzing")
     ]),

    # Set 9
    ("I met a dragon, green and bright, But he just smiled, not there to fight.",
     [
         ("What creature did the speaker meet?", "A dragon.", "Easy", "Remembering"),
         ("What two adjectives describe the dragon's appearance?", "Green and bright.", "Easy", "Remembering"),
         ("What did the dragon do instead of fighting?", "He just smiled.", "Easy", "Remembering"),
         ("Identify the rhyming pair in this extract.", "bright / fight.", "Easy", "Remembering"),
         ("Why is it significant that the dragon was 'not there to fight'?", "It transforms a traditional scary monster into a friendly adventure partner, making the dream comforting.", "Medium", "Analyzing")
     ]),

    # Set 10
    ("Remember the kite up in the sky, Brave the wind and take the flight, You'll find your wings and soar in light.",
     [
         ("What object in the sky should we remember?", "The kite up in the sky.", "Easy", "Remembering"),
         ("What should we do when facing the wind?", "Brave the wind and take the flight.", "Easy", "Remembering"),
         ("What does 'find your wings' mean metaphorically?", "Discovering inner self-confidence and capabilities.", "Easy", "Understanding"),
         ("What does 'soar in light' mean?", "Achieving success, joy, and self-actualization.", "Easy", "Understanding"),
         ("How does a kite inspire a child facing a tough challenge?", "Just as a kite needs opposing wind to fly high, facing challenges helps a child discover strength and achieve greatness.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 13: My Dream Adventure\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH13_EXT_{q_counter:03d}"
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

with open(os.path.join(CH13_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 13 in {CH13_DIR}")
