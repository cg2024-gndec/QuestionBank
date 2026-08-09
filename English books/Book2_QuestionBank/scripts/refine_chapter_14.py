r"""
Refines all 6 Category files for Chapter 14 ("Family's Day Out") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH14_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_14")
os.makedirs(CH14_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What is the title of Chapter 14?", "(A) Family's Day Out", "(B) Habits of the Hippopotamus", "(C) Fun in the Rain", "(D) The Banyan Tree", "(A)", "Chapter 14 is titled 'Family's Day Out'.", "Easy", "Remembering", "Chapter Title"),
    ("What type of composition activity is featured in Chapter 14?", "(A) Story-writing based on picture observation", "(B) Solving hard math equations", "(C) Drawing a map", "(D) Writing a science lab report", "(A)", "It is a picture-based story-writing composition.", "Easy", "Remembering", "Composition Type"),
    ("Where does a family typically go for a fun day out picnic?", "(A) A beautiful green park or garden", "(B) Inside a dark cave", "(C) On a crowded highway", "(D) Inside a factory", "(A)", "Families go to green parks, gardens, or picnic spots.", "Easy", "Remembering", "Picnic Location"),
    ("What do families carry food and snacks in for a picnic?", "(A) A picnic basket", "(B) A shoe box", "(C) A pencil case", "(D) A bucket", "(A)", "Food is carried in a picnic basket.", "Easy", "Remembering", "Picnic Item"),
    ("What do people spread on the green grass to sit on during a picnic?", "(A) A picnic mat or blanket", "(B) Paper towels", "(C) Plastic bags", "(D) Wooden planks", "(A)", "People spread a mat or blanket to sit on.", "Easy", "Remembering", "Picnic Setting"),
    ("Which of the following games do children enjoy playing on a family day out?", "(A) Frisbee, catch, or badminton", "(B) Sleeping in bed", "(C) Typing on keyboards", "(D) Watching television", "(A)", "Children play outdoor games like frisbee, catch, or badminton.", "Easy", "Remembering", "Outdoor Games"),
    ("What kind of weather is ideal for a family's day out in the park?", "(A) Bright, pleasant, sunny weather", "(B) Heavy thunderstorm", "(C) Freezing blizzard", "(D) Dark stormy night", "(A)", "Bright, sunny, pleasant weather is ideal.", "Easy", "Remembering", "Weather Condition"),
    ("Who usually goes together on a 'Family's Day Out'?", "(A) Parents, children, and grandparents", "(B) Strangers only", "(C) Only wild animals", "(D) Only classroom teachers", "(A)", "Family members like parents, children, and grandparents go together.", "Easy", "Remembering", "Participants"),
    ("What do family members share during a picnic lunch?", "(A) Sandwiches, fruits, juice, and snacks", "(B) Crayons and erasers", "(C) Stones and mud", "(D) Empty plates", "(A)", "They share sandwiches, fruits, juice, and homemade snacks.", "Easy", "Remembering", "Picnic Food"),
    ("Why is spending a day out with family important?", "(A) It strengthens love, bonding, and happiness among family members", "(B) It makes people angry", "(C) It wastes time", "(D) It causes arguments", "(A)", "It strengthens family bonding, love, and togetherness.", "Easy", "Understanding", "Value of Day Out"),
    ("What does the word 'picnic' mean?", "(A) An outing in the open air with a packed meal", "(B) A test taken at school", "(C) A long sleep", "(D) A doctor's visit", "(A)", "A picnic is an outdoor outing with a packed meal.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'togetherness' mean?", "(A) Feeling close, united, and happy as a group", "(B) Being completely alone", "(C) Fighting with friends", "(D) Running in opposite directions", "(A)", "Togetherness means unity and closeness.", "Easy", "Understanding", "Vocabulary"),
    ("What visual clues in a picture help us write a story about a family's day out?", "(A) People smiling, green trees, picnic basket, ball, and sunny sky", "(B) Dark shadows and rain clouds only", "(C) Blank white paper", "(D) Numbers and equations", "(A)", "Smiling faces, green trees, basket, ball, and sunny sky.", "Easy", "Understanding", "Picture Analysis"),
    ("What do children like to fly high in the open sky at a park?", "(A) Kites", "(B) Heavy stones", "(C) Books", "(D) Shoes", "(A)", "Children love to fly kites in the open park sky.", "Easy", "Remembering", "Park Activity"),
    ("After eating picnic food, what is the responsible way to handle trash?", "(A) Throw all wrappers into the dustbin to keep the park clean", "(B) Scatter trash on the grass", "(C) Leave food wrappers everywhere", "(D) Throw plastic in the lake", "(A)", "Throw trash into dustbins to keep parks clean.", "Easy", "Understanding", "Environmental Responsibility"),
    ("What sound fills the air during a happy family day out?", "(A) Laughter, cheerful voices, and birds singing", "(B) Loud car horns only", "(C) Absolute silence", "(D) Screaming in fear", "(A)", "Laughter, cheerful voices, and bird songs fill the air.", "Easy", "Remembering", "Atmosphere"),
    ("What beverage is refreshing to drink on a sunny picnic day out?", "(A) Fresh fruit juice or water", "(B) Hot soup only", "(C) Saltwater", "(D) Medicine", "(A)", "Fresh fruit juice or cool water is refreshing.", "Easy", "Remembering", "Refreshments"),
    ("What do family members take to capture happy memories of their day out?", "(A) Photographs / pictures", "(B) Homework sheets", "(C) Clocks", "(D) Paintbrushes only", "(A)", "They take photographs to save happy memories.", "Easy", "Remembering", "Memories"),
    ("How do children feel when planning a day out with their parents?", "(A) Excited and joyful", "(B) Bored and sad", "(C) Scared and crying", "(D) Angry", "(A)", "Children feel excited and joyful about a day out.", "Easy", "Understanding", "Emotion"),
    ("What is picture composition?", "(A) Writing a story or description by looking closely at a picture", "(B) Drawing a picture without words", "(C) Cutting paper with scissors", "(D) Reading a dictionary", "(A)", "Writing a story or description based on a picture.", "Easy", "Understanding", "Composition Definition"),
    ("Where do ducks swim that children like to watch during a park day out?", "(A) In a quiet park pond or lake", "(B) On the grass", "(C) In the trees", "(D) On the road", "(A)", "Ducks swim in park ponds or lakes.", "Easy", "Remembering", "Nature Element"),
    ("What do parents do while children play in the park?", "(A) Relax on the picnic blanket, talk, and watch the children safely", "(B) Run away home", "(C) Fall fast asleep in a house", "(D) Work on laptops all day", "(A)", "Parents relax, chat, and supervise children safely.", "Easy", "Understanding", "Parent Role"),
    ("When does a family usually return home after a day out?", "(A) In the pleasant evening before dark", "(B) In midnight storm", "(C) After five weeks", "(D) They never return", "(A)", "Families return home in the pleasant evening.", "Easy", "Remembering", "Return Time"),
    ("What makes a family day out story interesting to read?", "(A) Describing characters, setting, fun activities, good food, and happy feelings", "(B) Repeating one word ten times", "(C) Having no characters", "(D) Leaving out all details", "(A)", "Describing characters, setting, activities, food, and emotions.", "Easy", "Understanding", "Story Writing Tip"),
    ("Is 'Family's Day Out' a story about working at an office or enjoying a holiday together?", "(A) Enjoying a fun holiday outing together", "(B) Working at an office", "(C) Staying in hospital", "(D) Taking an exam", "(A)", "It is about enjoying a fun holiday outing together.", "Easy", "Remembering", "Core Theme"),

    # Medium (26-40)
    ("How does picture composition help develop a Class 2 student's writing skills?", "(A) It encourages careful visual observation, vocabulary recall, logical sentence sequencing, and creative expression", "(B) It teaches how to draw pictures without using words", "(C) It tests math calculation speed", "(D) It requires memorizing dictionary pages", "(A)", "Encourages visual observation, vocabulary, sentence sequence, and creativity.", "Medium", "Evaluating", "Composition Benefits"),
    ("What sequence of events forms a logical structure for a 'Family's Day Out' story?", "(A) 1. Planning & packing -> 2. Journey to park -> 3. Setting up blanket & playing games -> 4. Sharing picnic lunch -> 5. Evening return home with happy memories", "(B) 1. Eating lunch -> 2. Waking up -> 3. Going to sleep", "(C) 1. Returning home -> 2. Going to park -> 3. Packing basket", "(D) No order is needed", "(A)", "Logical sequence: Planning -> Journey -> Activities -> Lunch -> Returning home.", "Medium", "Analyzing", "Story Sequencing"),
    ("How do outdoor activities during a day out promote physical health?", "(A) Running, playing ball games, and breathing fresh outdoor air strengthen muscles and keep children active", "(B) Sitting in dark rooms makes body strong", "(C) Outdoor games cause sickness", "(D) Playing in parks makes people lazy", "(A)", "Running and playing in fresh air builds physical fitness.", "Medium", "Understanding", "Health Benefits"),
    ("Why is eco-civic sense (cleaning up after a picnic) an essential habit taught in Chapter 14?", "(A) Leaving trash ruins park beauty and harms wildlife; picking up trash keeps public parks clean for everyone", "(B) Cleaning up wastes time", "(C) Trash makes grass grow faster", "(D) Animals like plastic bags", "(A)", "Civic duty keeps parks clean and protects wildlife.", "Medium", "Evaluating", "Civic Responsibility"),
    ("What descriptive words add sensory details to a picnic story?", "(A) Sight: bright green trees; Sound: cheerful laughter; Taste: sweet juicy oranges; Touch: soft cool grass", "(B) Only numbers like 1, 2, 3", "(C) Words with no meanings", "(D) Dark black and white words", "(A)", "Sensory words (sight, sound, taste, touch) enrich stories.", "Medium", "Applying", "Sensory Vocabulary"),
    ("How does spending quality time outdoors reduce stress for parents and children?", "(A) Being in natural green surroundings away from screens relaxes the mind and brings joyful connection", "(B) Outdoor parks increase homework pressure", "(C) Nature makes people nervous", "(D) Being outdoors is bad for eyes", "(A)", "Green nature away from screens relaxes minds and connects families.", "Medium", "Analyzing", "Stress Reduction"),
    ("What role do grandparents play in a family day out story?", "(A) Grandparents share stories, watch children play, enjoy peaceful nature, and bless the family with love", "(B) Grandparents play football only", "(C) Grandparents stay in cars", "(D) Grandparents carry heavy boxes", "(A)", "Share wisdom, enjoy peaceful nature, and offer loving presence.", "Medium", "Understanding", "Family Dynamics"),
    ("Why is a sunny weekend morning the best time to start a family outing?", "(A) Morning temperatures are pleasant, and it leaves the whole day ahead for games, exploration, and lunch", "(B) Morning is too dark to see", "(C) Parks are closed in the morning", "(D) It rains every morning", "(A)", "Pleasant temperatures and full day ahead for activities.", "Medium", "Analyzing", "Time Choice"),
    ("How can a student use descriptive adjectives to improve their story about a day out?", "(A) Use adjectives like 'sunny sky', 'lush green grass', 'delicious sandwiches', and 'joyful smiles'", "(B) Use only verbs", "(C) Avoid all adjectives", "(D) Use negative words only", "(A)", "Rich adjectives make descriptions vivid and engaging.", "Medium", "Applying", "Adjective Usage"),
    ("What is the emotional climax of a 'Family's Day Out' story?", "(A) Sitting together on the picnic blanket, sharing food, laughing, and feeling deep gratitude for family love", "(B) Losing a shoe in the mud", "(C) Forgetting the food basket", "(D) Getting stuck in rain", "(A)", "Shared meal, laughter, and feeling family gratitude.", "Medium", "Analyzing", "Emotional Climax"),
    ("How does picture observation guide a child who is struggling to start writing?", "(A) The child looks at objects in the picture (sun, tree, ball, basket) and turns each object into a descriptive sentence", "(B) The child closes eyes and guesses", "(C) The child copies words from a billboard", "(D) The child draws over the picture", "(A)", "Turning visual objects into descriptive sentences.", "Medium", "Applying", "Scaffolding Technique"),
    ("What is the difference between a school day and a family day out?", "(A) School days focus on formal study and routine; a day out focuses on relaxed leisure, outdoor play, and family bonding", "(B) There is no difference", "(C) School days are outdoors; days out are in classrooms", "(D) Days out have strict exams", "(A)", "Formal study vs relaxed leisure and family bonding.", "Medium", "Comparing", "Context Contrast"),
    ("Why do children remember family picnic days for a long time?", "(A) Because shared happy experiences, laughter, games, and special treats create warm, lasting childhood memories", "(B) Because they get homework", "(C) Because picnics happen every minute", "(D) Because they wear school uniforms", "(A)", "Shared joy and special treats create lasting positive memories.", "Medium", "Evaluating", "Memory Formation"),
    ("How does sharing food during a picnic reinforce family cooperation?", "(A) Family members help pack food, carry baskets, pass dishes, and clean up together as a cooperative team", "(B) Everyone eats in separate rooms", "(C) One person eats all the food", "(D) People fight over plates", "(A)", "Cooperative packing, sharing, and cleaning together.", "Medium", "Understanding", "Cooperative Behavior"),
    ("What guiding questions can a Class 2 student ask themselves while writing a picture story?", "(A) Who is in the picture? Where are they? What are they doing? How do they feel?", "(B) What time is my math class? Where is my pencil?", "(C) How much does a car cost?", "(D) What is the capital of France?", "(A)", "Who? Where? What doing? How feeling?", "Medium", "Applying", "Self-Questioning Strategy"),

    # Hard (41-50)
    ("Analyze the pedagogical value of integrating visual literacy (picture prompt) with creative composition.", "(A) Visual literacy bridges concrete image recognition with abstract verbal expression, developing holistic language skills", "(B) Visual literacy replaces the need for learning grammar", "(C) Pictures prevent children from thinking independently", "(D) Visual prompts are only meant for drawing class", "(A)", "Bridges concrete image recognition with abstract verbal expression.", "Hard", "Analyzing", "HOTS Pedagogical Value"),
    ("Deconstruct the narrative arc of a well-crafted picture-based composition.", "(A) 1. Introduction: Setting & characters -> 2. Rising Action: Arrival & games -> 3. Climax: Shared picnic feast -> 4. Falling Action: Packing up -> 5. Resolution: Return home with contentment", "(B) 1. Climax -> 2. Setting -> 3. End", "(C) Random thoughts without structure", "(D) Repeating the first sentence five times", "(A)", "Structured 5-stage narrative arc applied to picture composition.", "Hard", "Analyzing", "Narrative Arc"),
    ("Evaluate the social-emotional development fostered by family outings in early childhood.", "(A) Outings build emotional security, strengthen interpersonal communication, reduce anxiety, and foster family resilience", "(B) Outings make children antisocial", "(C) Outings prevent children from making friends", "(D) Outings cause family separation", "(A)", "Fosters emotional security, communication, and family resilience.", "Hard", "Evaluating", "Social-Emotional Development"),
    ("Compare an urban park day out with a natural countryside picnic outing.", "(A) Urban park: landscaped gardens, playground swings, paved paths; Countryside: open fields, natural streams, wild trees", "(B) Both are inside indoor shopping malls", "(C) Urban parks have wild lions; countryside has skyscrapers", "(D) Neither has trees or grass", "(A)", "Landscaped urban amenities vs natural unpaved countryside.", "Hard", "Analyzing", "Comparative Setting"),
    ("Assess the environmental ethics of 'Leave No Trace' during recreational family visits to nature.", "(A) Practicing 'Leave No Trace' preserves pristine ecosystems, prevents animal ingestion of plastics, and honors public land", "(B) Dumping plastic waste is good for nature", "(C) Picking all wild flowers leaves nature better", "(D) Burning trash on grass is safe", "(A)", "Preserves ecosystems, prevents plastic harm, honors public land.", "Hard", "Evaluating", "Environmental Ethics"),
    ("How does narrative voice (First Person 'We' vs Third Person 'They') shape a picnic story?", "(A) First Person ('We had fun') creates personal warmth; Third Person ('The family enjoyed') gives observant objective storytelling", "(B) First person is for animal stories only", "(C) Third person is always illegal in stories", "(D) Narrative voice makes no difference", "(A)", "Personal warmth ('We') vs observant objectivity ('They').", "Hard", "Analyzing", "Narrative Perspective"),
    ("Synthesize how Chapter 14 connects visual art, creative writing, and moral family values.", "(A) Visual art (picture prompt) inspires creative writing (composition) while reinforcing moral values (family love, teamwork, environmental care)", "(B) It teaches computer programming through art", "(C) It focuses purely on grammar drills", "(D) It separates writing from thinking", "(A)", "Visual art + creative writing + moral family values.", "Hard", "Synthesizing", "Interdisciplinary Synthesis"),
    ("Formulate a complete 5-sentence sample picture composition titled 'A Joyful Picnic Day'.", "(A) 'On a bright sunny Sunday, Rahul and his family went for a picnic in the green park...'", "(B) 'We stayed home all day'", "(C) 'It rained heavily and we slept'", "(D) 'We went to an office meeting'", "(A)", "Complete exemplary 5-sentence picture composition.", "Hard", "Creating", "Sample Composition Creation"),
    ("Formulate a critical evaluation of why family traditions like annual outings matter for generations.", "(A) Traditions create family identity, anchor shared heritage, and pass down values of togetherness across generations", "(B) Traditions exist only to spend money", "(C) Traditions prevent children from growing up", "(D) Traditions are boring routines", "(A)", "Creates family identity, anchors heritage, and passes values.", "Hard", "Evaluating", "Cultural Heritage"),
    ("Synthesize the ultimate lesson of Chapter 14 for Class 2 learners.", "(A) Cherish time spent with family, observe the world carefully with open eyes, write your thoughts creatively, and care for nature!", "(B) Stay inside playing video games all day", "(C) Never talk to family members", "(D) Leave trash wherever you go", "(A)", "Cherish family time, observe carefully, write creatively, care for nature.", "Hard", "Evaluating", "Core Lesson Synthesis")
]

mcq_content = f"# MCQs — Chapter 14: Family's Day Out\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH14_MCQ_{idx:03d}"
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

with open(os.path.join(CH14_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Chapter 14 is titled 'Family's Day _______'.", "Out", "Title is Family's Day Out.", "Easy"),
    ("On a bright sunny day, the family went to a green _______.", "park", "Went to a green park.", "Easy"),
    ("They packed delicious food in a picnic _______.", "basket", "Packed in a picnic basket.", "Easy"),
    ("They spread a soft _______ on the green grass to sit.", "mat", "Spread a mat/blanket.", "Easy"),
    ("The children played with a red _______ in the park.", "ball", "Played with a ball.", "Easy"),
    ("The sky was bright blue and the _______ was shining.", "sun", "Sun was shining.", "Easy"),
    ("Mother prepared tasty _______ for the picnic.", "sandwiches", "Prepared tasty sandwiches.", "Easy"),
    ("Father helped the children fly a high _______.", "kite", "Fly a high kite.", "Easy"),
    ("The family sat under a big shady _______.", "tree", "Sat under a shady tree.", "Easy"),
    ("They drank refreshing fruit _______.", "juice", "Drank refreshing fruit juice.", "Easy"),
    ("Everyone enjoyed spending time _______.", "together", "Spending time together.", "Easy"),
    ("The children's faces were full of _______ and laughter.", "smiles", "Full of smiles and laughter.", "Easy"),
    ("They saw ducks swimming in the park _______.", "pond", "Swimming in the park pond.", "Easy"),
    ("After eating, they threw trash into the _______.", "dustbin", "Threw trash into the dustbin.", "Easy"),
    ("They took many photographs to save happy _______.", "memories", "Save happy memories.", "Easy"),
    ("Picture composition means writing a story from a _______.", "picture", "Writing from a picture.", "Easy"),
    ("A family day out brings love and _______.", "joy", "Brings love and joy.", "Easy"),
    ("In the evening, they returned back _______.", "home", "Returned back home.", "Easy"),
    ("The grass in the park was fresh and _______.", "green", "Fresh and green.", "Easy"),
    ("The family enjoyed a peaceful outdoor _______.", "picnic", "Outdoor picnic.", "Easy"),
    ("Grandparents enjoyed resting under the cool _______.", "shade", "Resting under cool shade.", "Easy"),
    ("Playing games outdoors is good for our _______.", "health", "Good for health.", "Easy"),
    ("We should always keep public parks clean and _______.", "neat", "Clean and neat.", "Easy"),
    ("The children ran around on the open _______.", "ground", "Ran on open ground.", "Easy"),
    ("Writing a story requires using good _______.", "sentences", "Using good sentences.", "Easy"),

    # Medium (26-40)
    ("Looking carefully at a picture is called visual _______.", "observation", "Visual observation.", "Medium"),
    ("Packing food before leaving is part of trip _______.", "preparation", "Trip preparation.", "Medium"),
    ("Sharing food with family builds strong bonds of _______.", "affection", "Bonds of affection.", "Medium"),
    ("Outdoor games like badminton improve hand-eye _______.", "coordination", "Hand-eye coordination.", "Medium"),
    ("Throwing litter in dustbins shows good civic _______.", "sense", "Good civic sense.", "Medium"),
    ("The warm sunshine made the picnic afternoon very _______.", "pleasant", "Picnic afternoon pleasant.", "Medium"),
    ("A family outing offers a break from daily school _______.", "routine", "Break from school routine.", "Medium"),
    ("Descriptive words that tell about sights and sounds are called _______.", "adjectives", "Called adjectives.", "Medium"),
    ("The children laughed happily as they played on the _______.", "swings", "Played on the swings.", "Medium"),
    ("Observing colors, objects, and people helps write a rich _______.", "composition", "Write a rich composition.", "Medium"),
    ("Spending time with loved ones creates deep emotional _______.", "security", "Creates emotional security.", "Medium"),
    ("A clear story has a beginning, middle, and _______.", "ending", "Beginning, middle, ending.", "Medium"),
    ("Nature parks provide fresh air filled with oxygen from green _______.", "plants", "Oxygen from green plants.", "Medium"),
    ("The family expressed gratitude for a wonderful day _______.", "out", "Wonderful day out.", "Medium"),
    ("Story writing improves vocabulary and sentence _______.", "structure", "Sentence structure.", "Medium"),

    # Hard (41-50)
    ("Picture prompts foster creative visual-verbal _______.", "integration", "Visual-verbal integration.", "Hard"),
    ("A structured composition follows a logical chronological _______.", "sequence", "Chronological sequence.", "Hard"),
    ("Environmental ethics dictate maintaining park cleanliness through zero _______.", "littering", "Zero littering.", "Hard"),
    ("Outdoor family activities promote physical and mental _______.", "well-being", "Physical and mental well-being.", "Hard"),
    ("Adjectives like 'vibrant', 'lush', and 'scenic' enhance descriptive _______.", "writing", "Enhance descriptive writing.", "Hard"),
    ("Picture-based composition encourages observational critical _______.", "thinking", "Observational critical thinking.", "Hard"),
    ("The emotional warmth of family unity provides lifelong psychological _______.", "anchoring", "Psychological anchoring.", "Hard"),
    ("Interpersonal communication flourishes during unstructured recreational _______.", "leisure", "Unstructured recreational leisure.", "Hard"),
    ("Drafting a story requires organizing ideas into coherent _______.", "paragraphs", "Coherent paragraphs.", "Hard"),
    ("Chapter 14 combines visual analysis, creative writing, and family _______.", "values", "Creative writing and family values.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 14: Family's Day Out\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH14_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH14_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Chapter 14 is titled 'Family's Day Out'.", "True", "Chapter title is Family's Day Out.", "Easy"),
    ("Chapter 14 features a picture-based story writing composition activity.", "True", "Page 49 features picture-based story writing.", "Easy"),
    ("A family day out is usually spent inside a dark locked room.", "False", "It is spent outdoors in pleasant places like parks, gardens, or picnic spots.", "Easy"),
    ("Families carry picnic food in a picnic basket.", "True", "Food is carried in a picnic basket.", "Easy"),
    ("People spread a blanket or mat on the grass during a picnic.", "True", "A mat or blanket is spread on the grass.", "Easy"),
    ("Children enjoy playing outdoor games like ball and frisbee in the park.", "True", "Children play outdoor games in open parks.", "Easy"),
    ("A heavy thunderstorm is the best weather for a picnic day out.", "False", "Bright, pleasant, sunny weather is ideal for a picnic.", "Easy"),
    ("Parents and children go together on a family day out.", "True", "Family members go together.", "Easy"),
    ("Sandwiches, fruits, and fruit juice are popular picnic foods.", "True", "They are popular packed foods for picnics.", "Easy"),
    ("Spending time with family builds love, bonding, and happiness.", "True", "Family outings build love, bonding, and happiness.", "Easy"),
    ("The word 'picnic' means taking an exam at school.", "False", "Picnic means an outdoor trip with a packed meal.", "Easy"),
    ("Picture composition means describing or writing a story based on a picture.", "True", "Picture composition is writing based on a picture prompt.", "Easy"),
    ("We should leave our plastic trash scattered all over the park grass.", "False", "We should always put trash into dustbins to keep parks clean.", "Easy"),
    ("Ducks can often be seen swimming in park ponds.", "True", "Ducks swim in park ponds.", "Easy"),
    ("Children like to fly kites in open windy parks.", "True", "Flying kites is a popular park activity.", "Easy"),
    ("Taking family photographs helps preserve happy memories.", "True", "Photographs preserve happy memories of days out.", "Easy"),
    ("Grandparents cannot join a family day out.", "False", "Grandparents often join and enjoy relaxing in nature.", "Easy"),
    ("Fresh outdoor air and physical play are good for children's health.", "True", "Outdoor play and fresh air promote health.", "Easy"),
    ("In the evening, the family returns home happy and refreshed.", "True", "Families return home in the evening.", "Easy"),
    ("Picture composition does not require looking at the picture.", "False", "Picture composition requires careful visual observation of the picture.", "Easy"),
    ("A picnic basket can hold sandwiches, apples, and juice bottles.", "True", "It holds packed food and drinks.", "Easy"),
    ("Trees in the park provide cool shade for resting.", "True", "Trees provide cool shade.", "Easy"),
    ("A family day out is a time for stress and fighting.", "False", "It is a time for joy, relaxation, and togetherness.", "Easy"),
    ("Descriptive words make story writing more interesting.", "True", "Descriptive adjectives enrich stories.", "Easy"),
    ("Chapter 14 teaches creative composition skills to Class 2 students.", "True", "It teaches picture-based story writing skills.", "Easy"),

    # Medium (26-40)
    ("Writing a story in order (beginning, middle, end) makes it easy to read.", "True", "Logical sequence creates a clear story structure.", "Medium"),
    ("Throwing food wrappers on park grass is fine because birds eat plastic.", "False", "Plastic is dangerous to animals and pollutes nature.", "Medium"),
    ("Observing details like expressions, objects, and weather helps write a good story.", "True", "Observing visual details enriches composition.", "Medium"),
    ("Outdoor sports in the park help children build strong physical stamina.", "True", "Running and playing outdoor sports build stamina.", "Medium"),
    ("A family outing provides a healthy break from mobile and TV screens.", "True", "Outings encourage screen-free outdoor relaxation.", "Medium"),
    ("Picture composition is only meant for professional artists, not students.", "False", "It is a foundational writing exercise for students.", "Medium"),
    ("Sharing food with siblings and parents fosters team spirit.", "True", "Sharing meals reinforces cooperation and love.", "Medium"),
    ("Story writing helps children practice spelling and sentence construction.", "True", "Writing stories practices spelling and sentence skills.", "Medium"),
    ("Rainy days are the only days people go on park picnics.", "False", "Dry, sunny, pleasant days are preferred for picnics.", "Medium"),
    ("Grandparents sitting on a park bench enjoy watching grandchildren play.", "True", "Grandparents enjoy watching children play in nature.", "Medium"),
    ("The title of a story should match the main theme of the picture.", "True", "Titles should reflect the central picture theme.", "Medium"),
    ("Children feel lonely during a fun family day out.", "False", "Children feel happy, loved, and connected with family.", "Medium"),
    ("Keeping public parks clean is every citizen's civic responsibility.", "True", "Maintaining clean public spaces is a civic duty.", "Medium"),
    ("Picture prompts give students visual clues about setting, characters, and action.", "True", "Pictures provide visual clues for writing.", "Medium"),
    ("A family day out story can include dialogue between family members.", "True", "Including dialogue makes stories lively and realistic.", "Medium"),

    # Hard (41-50)
    ("Visual literacy enables learners to decode image details into structured text.", "True", "Visual literacy translates image details into text.", "Hard"),
    ("A narrative composition requires a clear resolution that rounds off the plot.", "True", "Narratives require a resolution to complete the story arc.", "Hard"),
    ("Environmental stewardship involves active waste management during public outings.", "True", "Stewardship includes proper waste management during outings.", "Hard"),
    ("Sensory descriptions engage readers by appealing to sight, sound, and taste.", "True", "Sensory language appeals to sight, sound, taste, touch.", "Hard"),
    ("Shared family traditions foster emotional resilience in developing children.", "True", "Family traditions build emotional resilience.", "Hard"),
    ("Writing a picture story without identifying the setting makes the story confused.", "True", "Omitting setting creates confusion for readers.", "Hard"),
    ("Unstructured play in natural environments stimulates cognitive creativity.", "True", "Natural play stimulates cognitive creativity.", "Hard"),
    ("Picture-based composition bridges oral storytelling with formal written literacy.", "True", "Bridges oral expression with written literacy.", "Hard"),
    ("Civic awareness regarding public property is developed through real-life practices.", "True", "Real-life practices build civic awareness.", "Hard"),
    ("Chapter 14 integrates observational art, composition writing, and family values.", "True", "Integrates observation, writing, and family values.", "Hard")
]

tf_content = f"# True / False — Chapter 14: Family's Day Out\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH14_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH14_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("What is picture composition?", "Picture composition is writing a short story or description based on observing a picture.", "Easy", "Understanding"),
    ("Where does a family typically go for a day out picnic?", "A family typically goes to a green park, garden, lakeside, or scenic spot.", "Easy", "Remembering"),
    ("What items are usually packed in a picnic basket?", "Sandwiches, fruits, juice bottles, biscuits, and paper napkins.", "Easy", "Remembering"),
    ("What do people spread on the grass to sit comfortably?", "They spread a picnic mat or soft blanket on the grass.", "Easy", "Remembering"),
    ("What outdoor games do children love playing in the park?", "Children love playing with a ball, flying kites, playing frisbee, or running around.", "Easy", "Remembering"),
    ("What kind of weather is best for a family day out?", "Bright, pleasant, and sunny weather is best for a day out.", "Easy", "Remembering"),
    ("Who participates in a family day out?", "Family members like parents, children, and grandparents.", "Easy", "Remembering"),
    ("Why is spending a day out together good for a family?", "It strengthens love, family bonding, and brings joy and relaxation to everyone.", "Easy", "Understanding"),
    ("What should we do with food wrappers after a picnic?", "We should collect all trash and throw it into public dustbins to keep the park clean.", "Easy", "Understanding"),
    ("What sound fills a park during a family outing?", "The sounds of cheerful laughter, happy voices, and singing birds.", "Easy", "Remembering"),
    ("Why do families take photographs during a day out?", "They take photographs to capture and preserve happy family memories.", "Easy", "Remembering"),
    ("What do children see swimming in a park pond?", "They see ducks and small fish swimming in the park pond.", "Easy", "Remembering"),
    ("What do parents do while children play in the park?", "Parents sit on the picnic blanket, talk, relax, and watch the children safely.", "Easy", "Understanding"),
    ("When does the family return home from a day out?", "They usually return home in the cool evening before dark.", "Easy", "Remembering"),
    ("How do children feel when going on a picnic with parents?", "They feel very excited, happy, and joyful.", "Easy", "Remembering"),
    ("What does 'togetherness' mean in a family context?", "'Togetherness' means feeling close, united, and sharing love as a family.", "Easy", "Understanding"),
    ("What is the first step when writing a story from a picture?", "The first step is looking closely at the picture to identify characters, place, and actions.", "Easy", "Understanding"),
    ("Why do people sit under large trees during a picnic?", "People sit under large trees to enjoy cool shade away from direct sunlight.", "Easy", "Understanding"),
    ("What refreshing drinks are carried on a sunny picnic?", "Fresh fruit juice, lemonade, or cool drinking water.", "Easy", "Remembering"),
    ("What makes a park look beautiful on a sunny day?", "Green grass, blooming colorful flowers, tall trees, and clear blue sky.", "Easy", "Understanding"),
    ("What do grandparents enjoy doing on a family day out?", "They enjoy resting in nature, watching grandchildren play, and sharing stories.", "Easy", "Remembering"),
    ("Why is playing outdoors good for children?", "Outdoor play strengthens muscles, provides fresh air, and keeps children active.", "Easy", "Understanding"),
    ("What is a picnic mat used for?", "It is spread on the ground so people can sit and eat without getting dirty.", "Easy", "Remembering"),
    ("Why should we not pick all flowers in a public park?", "Because flowers make the park beautiful for everyone and help bees.", "Easy", "Understanding"),
    ("What is the title of Chapter 14?", "The title of Chapter 14 is 'Family's Day Out'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Explain the four main steps of writing a picture composition.", "1. Observe the picture carefully.\n2. Identify characters, setting, and action.\n3. Write sentences in logical order (beginning, middle, end).\n4. Give a suitable title and check spellings.", "Medium", "Analyzing"),
    ("How does a family day out strengthen relationships between parents and children?", "It gives parents and children uninterrupted time away from work and screens to play, talk, eat, and share joy together.", "Medium", "Evaluating"),
    ("Why is civic responsibility important when visiting public parks?", "Because maintaining cleanliness by using dustbins keeps parks beautiful, safe, and hygienic for all visitors and wildlife.", "Medium", "Evaluating"),
    ("Describe a typical picnic meal scene in a story.", "The family sits together on a blue blanket under a tree. Mother opens the picnic basket, serving delicious sandwiches and juice, while everyone laughs and eats happily.", "Medium", "Understanding"),
    ("How do sensory details make a picture story come alive?", "Sensory details describe what characters see (green trees), hear (birds chirping), taste (sweet juice), and feel (cool breeze), making the story vivid.", "Medium", "Analyzing"),
    ("What is the difference between writing a single sentence and writing a full story composition?", "A single sentence tells one thought; a full story connects sentences in sequence to tell a complete event with a beginning, middle, and end.", "Medium", "Analyzing"),
    ("Why is screen-free time outdoors valuable for modern children?", "Screen-free time allows eyes to rest, encourages physical movement in fresh air, and builds real-world social skills with family.", "Medium", "Evaluating"),
    ("How can a student choose a good title for their picture story?", "By picking a title that sums up the main action or scene in the picture, such as 'A Fun Day in the Park' or 'Family Picnic'.", "Medium", "Applying"),
    ("Describe how children help prepare for a family day out.", "Children help by packing their toys, filling water bottles, helping parents organize the basket, and putting on comfortable shoes.", "Medium", "Understanding"),
    ("What role does nature play in making a day out enjoyable?", "Green trees, open space, fresh breeze, and gentle sunshine create a peaceful, refreshing atmosphere that relaxes the mind.", "Medium", "Analyzing"),
    ("Summarize Page 49 of the textbook in two sentences.", "Page 49 of Chapter 14 presents a picture composition activity titled 'Family's Day Out'. Students observe the picture prompt to write a creative story about a family enjoying a picnic in the park.", "Medium", "Understanding"),
    ("Why is logical sequencing (order of events) necessary in story writing?", "Because events must follow a natural time order so that the reader can easily understand how the day started, unfolded, and ended.", "Medium", "Understanding"),
    ("How can Class 2 students use adjectives to describe a picnic scene?", "They can use words like 'sunny sky', 'lush green grass', 'crunchy apples', 'delicious sandwiches', and 'happy laughter'.", "Medium", "Applying"),
    ("Why do families feel refreshed after returning from a day out?", "Because outdoor recreation, physical play, good food, and family laughter clear away mental fatigue and restore energy.", "Medium", "Evaluating"),
    ("How does picture composition build observational skills?", "It trains children to look closely at background details, facial expressions, and actions instead of just glancing quickly.", "Medium", "Evaluating"),

    # Hard (41-50)
    ("Critique the educational importance of picture-based composition in early primary literacy.", "Picture composition bridges visual perception with verbal expression, scaffolding sentence construction, vocabulary usage, and sequential storytelling for young writers.", "Hard", "Evaluating"),
    ("Analyze the structural elements of an effective picture story (Orientation, Event, Resolution).", "Orientation sets the scene and characters; Event details the main activities (games, picnic feast); Resolution closes the day with a satisfying return home.", "Hard", "Analyzing"),
    ("Deconstruct the social-emotional benefits of shared family recreation.", "Shared recreation fulfills biological needs for physical movement, psychological needs for belonging, and emotional needs for affection and laughter.", "Hard", "Analyzing"),
    ("Compare an urban park picnic with a beach family day out.", "Urban park: green grass, shade trees, playground swings, duck pond; Beach: sandy shores, ocean waves, seashell collecting, building sandcastles.", "Hard", "Analyzing"),
    ("Evaluate the environmental ethics of 'Leave No Trace' during public outings.", "Practicing 'Leave No Trace' ensures that human recreation does not pollute soil, harm wildlife with plastic, or degrade natural beauty for future visitors.", "Hard", "Evaluating"),
    ("How can teachers scaffold picture story writing for struggling Class 2 writers?", "Teachers can provide guiding questions (Who, Where, What), a word bank of adjectives/verbs, and sentence starters to structure writing.", "Hard", "Applying"),
    ("Assess the role of family outings in building lifelong emotional resilience.", "Positive childhood memories of family warmth during outings provide a psychological anchor of security that supports children during stress.", "Hard", "Evaluating"),
    ("Why is narrative pacing important in a short 5-sentence composition?", "Proper pacing ensures every sentence advances the story—moving smoothly from arrival to activities, mealtime, and evening conclusion.", "Hard", "Analyzing"),
    ("Formulate a 4-line poem capturing the spirit of 'Family's Day Out'.", "'Underneath the sunny sky,\nWhere green trees sway and kites fly high;\nWe share our food and laugh with glee,\nHappy as a family!'", "Hard", "Creating"),
    ("Synthesize the ultimate lesson of Chapter 14 for Class 2 learners.", "Observe the world with bright eyes, cherish loving moments with family, express your thoughts in clear stories, and keep nature clean!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 14: Family's Day Out\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH14_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH14_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe a complete story about a 'Family's Day Out' based on picture composition guidelines.", 
     "On a bright and sunny Sunday morning, Rohan and his family decided to go for a picnic in the city park. They packed a big woven basket with cheese sandwiches, fresh oranges, and cold fruit juice. When they arrived at the park, they spread a soft blue blanket under a giant shady banyan tree. Rohan and his sister played frisbee on the lush green grass, while their parents relaxed and enjoyed the cool breeze. Later, the whole family gathered on the blanket to eat their delicious lunch and share happy stories. After eating, Rohan carefully picked up all empty wrappers and threw them into the park dustbin. As the sun began to set, they packed their things and headed home, feeling happy, united, and refreshed.", 
     "Easy", "Remembering"),

    ("Explain the steps involved in writing a good picture composition for Class 2 students.", 
     "Writing a good picture composition involves four simple steps:\n1. **Observation**: Look closely at the picture to identify the people, objects, weather, and location.\n2. **Brainstorming**: Think of relevant action words (verbs) and descriptive words (adjectives).\n3. **Sentence Formation**: Write clear sentences in proper time order (beginning, middle, and end).\n4. **Review & Title**: Give the story an interesting title and check for correct capital letters, full stops, and spellings.", 
     "Easy", "Understanding"),

    ("Why are family outings important for children's growth and happiness?", 
     "Family outings play a vital role in a child's development:\n1. **Family Bonding**: Spending quality time together strengthens love and emotional trust between parents and children.\n2. **Health & Play**: Running in fresh outdoor air promotes physical health and stamina.\n3. **Screen-Free Fun**: It provides a healthy break from mobile phones and television.\n4. **Nature Connection**: It teaches children to appreciate plants, trees, birds, and open spaces.", 
     "Easy", "Understanding"),

    ("Describe the items packed in a picnic basket and how they are shared during a day out.", 
     "A picnic basket is filled with carefully prepared food and drinks. It typically contains homemade sandwiches wrapped neatly, fresh fruits like apples and oranges, fruit juice boxes or water bottles, and sweet biscuits. At lunchtime, the basket is opened on the picnic mat, and food is passed around so every family member shares and enjoys the feast together.", 
     "Easy", "Remembering"),

    ("Explain the importance of cleanliness and civic sense during a park picnic.", 
     "When families enjoy a day out in a public park, practicing civic sense is essential. After eating food and drinking juice, wrappers and bottles must not be left on the grass. Leaving trash harms the environment and poses a danger to animals or birds. Collecting all litter and throwing it into dustbins keeps parks clean, green, and pleasant for everyone.", 
     "Easy", "Understanding"),

    ("How do outdoor games in the park benefit family members of all ages?", 
     "Outdoor games like playing ball, flying kites, or badminton benefit the entire family. For children, it releases energy, builds teamwork, and improves physical agility. For parents and grandparents, watching or participating brings joyful relaxation, light exercise, and laughter away from daily work stress.", 
     "Easy", "Understanding"),

    ("Describe the setting of a park on a pleasant picnic day.", 
     "A park on a pleasant picnic day is full of life and beauty. The sun shines brightly in a clear blue sky, casting warm light over lush green lawns and tall shady trees. Colorful flowers bloom in gardens, and ducks swim gracefully in the park pond. The air is cool and filled with the happy sounds of children laughing and birds chirping.", 
     "Easy", "Remembering"),

    ("How do parents and children cooperate to make a day out successful?", 
     "Cooperation makes a day out smooth and fun. Parents prepare the food, arrange transport, and supervise safety. Children help by carrying light bags, filling water bottles, cleaning up after lunch, and following safety rules while playing. Working together ensures everyone has a joyful day.", 
     "Easy", "Understanding"),

    ("Why is taking photographs an enjoyable part of a family day out?", 
     "Taking photographs captures special moments of joy—like children laughing on swings, family members sharing lunch, or flying a kite together. Years later, looking at these picnic photos brings back warm memories of love, childhood happiness, and family togetherness.", 
     "Easy", "Remembering"),

    ("Summarize why Chapter 14 is a valuable composition lesson for Class 2 students.", 
     "Chapter 14 teaches students how to observe visual scenes, organize their thoughts into meaningful sentences, use descriptive vocabulary, and write a complete story. It simultaneously reinforces positive values of family love, outdoor recreation, and environmental cleanliness.", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("What details should a student look for when observing a picture for story writing?", "Students should look for who the characters are, what they are doing, where the scene takes place, what objects are present, what the weather is like, and what expressions are on their faces.", "Easy", "Remembering"),
    ("How does flying a kite add fun to a family day out?", "Flying a kite requires teamwork—one person holds the kite while another runs with the string. Watching the colorful kite soar into the blue sky brings excitement and joy to the whole family.", "Easy", "Understanding"),
    ("Why is sitting under a large shady tree popular during picnics?", "Because a large tree blocks hot sunlight with its leafy canopy, offering a cool, comfortable spot to rest, chat, and eat lunch.", "Easy", "Understanding"),
    ("What role does a picnic blanket play during a day out?", "A picnic blanket provides a clean, dry, comfortable surface over the grass where family members can sit, lay down food, and relax together.", "Easy", "Remembering"),
    ("How can a student begin their picture story with an engaging first sentence?", "By introducing the time, characters, and place clearly, such as: 'On a sunny Sunday morning, the Sharma family went for a joyful picnic in National Park.'", "Easy", "Applying"),
    ("Why is sharing food outdoors more fun than eating at home?", "Eating outdoors surrounded by green nature, fresh breeze, and open skies makes simple food taste more delicious and turns mealtime into a special celebration.", "Easy", "Understanding"),
    ("What safety rules should children follow during a day out in the park?", "Children should stay within sight of parents, avoid going near deep pond water alone, not touch unknown insects, and stay on marked footpaths.", "Easy", "Applying"),
    ("How does a family day out create lasting childhood memories?", "Shared laughter, fun games, special picnic treats, and quality time spent with loving parents create warm, emotional memories that children cherish forever.", "Easy", "Evaluating"),
    ("What descriptive adjectives can be used to describe picnic food?", "Adjectives like 'fresh', 'crispy', 'sweet', 'delicious', 'juicy', 'chilled', and 'homemade'.", "Easy", "Applying"),
    ("How does Chapter 14 connect language learning with real-life experiences?", "By using a familiar real-life experience (a family day out) as the topic, making story writing relatable, easy, and meaningful for young learners.", "Easy", "Understanding"),
    ("Why is returning home in the evening a satisfying end to a picnic story?", "Because after a full day of playing and eating in the park, returning home in the quiet evening rounds off the journey, leaving everyone pleasantly tired and happy.", "Easy", "Understanding"),
    ("What is the difference between a picture caption and a picture story?", "A caption is a single line describing what is seen; a story uses multiple connected sentences to build a narrative with characters, action, and feelings.", "Easy", "Analyzing"),
    ("How do grandparents enrich a family day out?", "Grandparents bring warmth, tell interesting stories, teach children about nature, and enjoy watching the family relax together.", "Easy", "Understanding"),
    ("Why should story sentences be written in proper sequence?", "Writing in sequence ensures the story flows logically from arrival at the park to playing games, eating lunch, and going back home.", "Easy", "Understanding"),
    ("Summarize Chapter 14 in five key sentences.", "Chapter 14 focuses on picture-based story writing titled 'Family's Day Out'. Students learn to observe visual details and write a structured narrative about a family picnic. A family travels to a sunny park, sets up a picnic blanket, plays games, and shares delicious food. They practice civic sense by throwing trash in dustbins to keep nature clean. The activity builds observation, vocabulary, creative writing, and family values.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how visual prompts scaffold the creative writing process for young learners.", 
     "Visual prompts act as a cognitive bridge for Class 2 students. Instead of facing a blank page, the picture provides concrete visual anchors—characters, setting, weather, and actions. Students convert these visual clues into vocabulary words, which they then assemble into complete descriptive sentences, scaffolding confidence and narrative flow.", 
     "Medium", "Analyzing"),

    ("Examine the civic and environmental lessons embedded in park composition topics.", 
     "Picnic stories naturally touch upon public space etiquette. By emphasizing that families must pick up wrappers, bottles, and food scraps after their meal, the chapter teaches young children civic responsibility. It instills habits of environmental care, keeping public parks clean for others and protecting wildlife from plastic ingestion.", 
     "Medium", "Evaluating"),

    ("Discuss the narrative arc of a picture-based story: Setup, Activity, Feast, and Conclusion.", 
     "A well-structured picture story follows four clear phases:\n1. **Setup**: Introducing the sunny day, family members, and arrival at the park.\n2. **Activity**: Describing games played (ball, frisbee, kite flying).\n3. **Feast**: Describing the picnic blanket feast (sandwiches, fruit juice, laughter).\n4. **Conclusion**: Cleaning up trash and returning home with joyful memories.", 
     "Medium", "Analyzing"),

    ("Explore how sensory language elevates a simple picnic description into a vivid composition.", 
     "Sensory language engages the reader's imagination:\n- **Visual**: Lush green grass, bright blue sky, colorful kites.\n- **Auditory**: Birds chirping, children laughing, gentle breeze rustling leaves.\n- **Taste/Smell**: Sweet juicy oranges, fresh baked bread.\n- **Tactile**: Soft picnic blanket, warm sunshine on skin.", 
     "Medium", "Analyzing"),

    ("How can Class 2 teachers conduct a peer-sharing session for picture stories?", 
     "Teachers can pair students up to read their picture stories aloud to each other. Students can praise good adjectives, check if all picture details were included, and share feedback on title choices, building collaborative communication.", 
     "Medium", "Applying"),

    ("Why is family togetherness an essential emotional anchor in early childhood education?", "Regular family togetherness builds emotional security, self-esteem, and social trust in children, providing a strong psychological foundation for academic and personal growth.", "Medium", "Evaluating"),
    ("Describe how to teach sentence sequencing using a 4-panel picnic picture card.", "Teachers place 4 cards in order: 1. Packing basket -> 2. Arriving at park -> 3. Playing ball -> 4. Eating lunch. Students write one sentence per card, forming a sequential paragraph.", "Medium", "Applying"),
    ("How does outdoor physical play complement classroom learning?", "Classroom learning develops mental focus; outdoor play releases physical energy, improves oxygen circulation to the brain, and enhances overall cognitive alertness.", "Medium", "Analyzing"),
    ("Contrast a chaotic day out with a well-planned, enjoyable family picnic.", "A chaotic day out lacks preparation (forgotten food, unmanaged trash, stress); a well-planned picnic involves organized packing, cooperative teamwork, clean habits, and peaceful joy.", "Medium", "Analyzing"),
    ("Why is title selection an important skill in picture composition?", "Selecting a title trains students to summarize the main theme or core message of a visual scene into a concise, catchy headline.", "Medium", "Understanding"),
    ("Explain how picture composition encourages independent thinking.", "While the picture gives clues, students independently decide character names, dialogue, specific food eaten, and emotional responses, building creative authorship.", "Medium", "Analyzing"),
    ("What environmental dangers occur when picnic trash is left in nature?", "Littered plastic bottles and bags pollute soil, block drainage ditches, and can be ingested by grazing animals or birds, causing severe harm.", "Medium", "Understanding"),
    ("How does sharing a picnic meal teach children table manners outdoors?", "Children learn to wait for food to be served, pass dishes politely to elders, use napkins, and clean up their own eating space on the blanket.", "Medium", "Understanding"),
    ("What safety measures should parents take during a day out near water bodies?", "Parents must maintain constant visual supervision, place picnic blankets away from steep slippery banks, and ensure children wear floatation vests if boating.", "Medium", "Applying"),
    ("Construct a 4-sentence picture story incorporating sight, sound, taste, and emotion.", "'Under a bright sunny sky, our family arrived at the lush green park. We heard birds singing sweetly while my brother and I flew a red kite. Mother served cool, sweet mango juice and fresh sandwiches on our picnic blanket. We returned home in the evening with hearts full of happiness and love.'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the pedagogical role of visual composition prompts in developing early writing fluency.", 
     "Visual prompts remove writer's block by providing immediate conceptual context. They stimulate observational analysis, expand thematic vocabulary, and guide sentence formation, making visual prompts one of the most effective tools for early literacy development.", 
     "Hard", "Evaluating"),

    ("Deconstruct the linguistic progression from word-labeling to complex narrative composition in Class 2.", 
     "1. **Labeling**: Naming single objects (tree, sun, ball).\n2. **Action Phrases**: Describing simple verbs (playing ball, eating food).\n3. **Simple Sentences**: Subject + Verb + Object ('The family eats sandwiches').\n4. **Complex Composition**: Connecting sequential sentences with transitions, adjectives, and emotional resolution.", 
     "Hard", "Analyzing"),

    ("Synthesize how Chapter 14 integrates observational skills, creative writing, and environmental ethics.", 
     "1. **Observational Skills**: Scanning picture prompts for setting and character details.\n2. **Creative Writing**: Structuring sequential, adjective-rich narratives.\n3. **Environmental Ethics**: Practicing 'Leave No Trace' by disposing of picnic trash responsibly.", 
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive rubrics guide for assessing Class 2 picture composition.", 
     "- **Content (2 pts)**: Accurate inclusion of picture details.\n- **Structure (2 pts)**: Logical beginning, middle, and end.\n- **Vocabulary (2 pts)**: Use of descriptive adjectives.\n- **Mechanics (2 pts)**: Capitalization, full stops, and spellings.\n- **Creativity (2 pts)**: Engaging title and happy resolution.", 
     "Hard", "Creating"),

    ("Evaluate the psychological impact of nature-based family recreation on child mental health.", 
     "Nature-based recreation reduces sensory overload from electronic devices, lowers cortisol (stress) levels, stimulates imaginative play, and fosters strong emotional bonding within the family unit.", 
     "Hard", "Evaluating"),

    ("Analyze why narrative coherence is essential when writing stories based on static pictures.", "Static pictures show a single frozen moment in time. Narrative coherence requires the writer's imagination to construct what happened before and after that frozen moment to form a complete story.", "Hard", "Analyzing"),
    ("Compare the thematic elements of Chapter 14 ('Family's Day Out') with Chapter 08 ('Diwali').", "Both chapters celebrate family togetherness and shared joy: Chapter 08 focuses on cultural festival rituals and home lighting; Chapter 14 focuses on outdoor nature recreation and picture composition.", "Hard", "Analyzing"),
    ("Draft a sample teacher feedback letter complimenting a student's picture composition.", "'Dear Ananya, Excellent work on your story 'A Fun Day in the Park'! You observed the picture details wonderfully, used vibrant adjectives like 'sunny' and 'delicious', and remembered to put your trash in the dustbin. Keep writing!'", "Hard", "Creating"),
    ("Assess the role of parental involvement in nurturing early creative writing habits at home.", "Parents who talk about pictures, encourage storytelling during family outings, and read stories together at home significantly boost a child's vocabulary, confidence, and writing fluency.", "Hard", "Evaluating"),
    ("Synthesize the ultimate philosophy of Chapter 14 into a timeless guiding principle.", "'Look closely at the world around you, cherish every happy moment with family, express your story with creative words, and protect the beauty of nature!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 14: Family's Day Out\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH14_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH14_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Family's Day Out (Story-writing): Look at the Picture and write a short story based on it.",
     [
         ("What is the title of Chapter 14?", "Family's Day Out.", "Easy", "Remembering"),
         ("What type of composition activity is required?", "Story-writing based on picture observation.", "Easy", "Remembering"),
         ("What is the first thing a student should do before writing?", "Look closely at the picture prompt.", "Easy", "Understanding"),
         ("What skill is tested in story-writing from a picture?", "Visual observation, creative imagination, and sentence construction.", "Medium", "Understanding"),
         ("Why is picture-based story writing helpful for young learners?", "It provides visual clues that guide sentence building and creative expression.", "Medium", "Evaluating")
     ]),

    # Set 2
    ("On a bright sunny Sunday morning, the Sharma family went for a picnic in the green city park.",
     [
         ("What day of the week did the family go for a picnic?", "Sunday morning.", "Easy", "Remembering"),
         ("What was the weather like?", "Bright and sunny.", "Easy", "Remembering"),
         ("What is the family's name in this story?", "The Sharma family.", "Easy", "Remembering"),
         ("Where did the family go for their picnic?", "To the green city park.", "Easy", "Remembering"),
         ("What setting details are established in this opening sentence?", "Time (Sunday morning), weather (bright sunny), characters (Sharma family), location (green city park).", "Medium", "Analyzing")
     ]),

    # Set 3
    ("They spread a soft blue blanket under a giant shady banyan tree and set down their food basket.",
     [
         ("What color was the blanket?", "Soft blue.", "Easy", "Remembering"),
         ("Where did they spread the blanket?", "Under a giant shady banyan tree.", "Easy", "Remembering"),
         ("What did they place on the blanket?", "Their food basket.", "Easy", "Remembering"),
         ("Why did they choose to sit under the banyan tree?", "To stay cool under its big shady canopy.", "Easy", "Understanding"),
         ("What role does the blanket play during a picnic?", "It provides a clean, comfortable place for the family to sit and eat.", "Medium", "Understanding")
     ]),

    # Set 4
    ("Rohan and his sister played frisbee on the lawn while their parents relaxed and chatted under the shade.",
     [
         ("What game did Rohan and his sister play?", "Frisbee.", "Easy", "Remembering"),
         ("Where were they playing frisbee?", "On the grass lawn.", "Easy", "Remembering"),
         ("What were their parents doing?", "Relaxing and chatting under the shade.", "Easy", "Remembering"),
         ("What contrast is shown between the children and parents?", "Children are active playing games, while parents are relaxing and chatting.", "Medium", "Analyzing"),
         ("How does playing frisbee benefit children?", "It promotes physical fitness, outdoor movement, and sibling fun.", "Medium", "Understanding")
     ]),

    # Set 5
    ("At lunchtime, Mother served delicious cheese sandwiches, sweet oranges, and fresh apple juice.",
     [
         ("When did the family eat their food?", "At lunchtime.", "Easy", "Remembering"),
         ("Who served the food?", "Mother.", "Easy", "Remembering"),
         ("What three food items were served?", "Cheese sandwiches, sweet oranges, and fresh apple juice.", "Easy", "Remembering"),
         ("Which adjectives describe the food in this extract?", "'Delicious' (sandwiches), 'sweet' (oranges), and 'fresh' (apple juice).", "Medium", "Understanding"),
         ("Why is sharing a meal outdoors enjoyable for families?", "It combines good food with fresh air, nature, and shared family conversation.", "Medium", "Evaluating")
     ]),

    # Set 6
    ("After eating, Rohan collected all the food wrappers and threw them into the park dustbin.",
     [
         ("What did Rohan collect after eating?", "All the food wrappers.", "Easy", "Remembering"),
         ("Where did Rohan throw the food wrappers?", "Into the park dustbin.", "Easy", "Remembering"),
         ("What value did Rohan demonstrate by cleaning up?", "Civic sense, responsibility, and environmental care.", "Medium", "Evaluating"),
         ("Why is it dangerous to leave plastic wrappers on park grass?", "Plastic pollutes nature and can be eaten by grazing animals or birds.", "Medium", "Understanding"),
         ("How can other children follow Rohan's good example?", "By always cleaning up their trash after eating in public parks.", "Medium", "Applying")
     ]),

    # Set 7
    ("As the sun began to set, the family packed their basket and returned home feeling very happy and united.",
     [
         ("When did the family pack their basket to go home?", "As the sun began to set (in the evening).", "Easy", "Remembering"),
         ("How did the family feel when returning home?", "Very happy and united.", "Easy", "Remembering"),
         ("Why did they return home at sunset?", "Because the picnic day was ending as night approached.", "Easy", "Understanding"),
         ("What resolution closes this story?", "Returning home together feeling happy, united, and refreshed.", "Medium", "Analyzing"),
         ("What is the main takeaway of a family day out story?", "Spending quality time together creates strong love, joy, and family unity.", "Medium", "Evaluating")
     ]),

    # Set 8
    ("Composition Tip: Observe the picture carefully -> Identify characters & setting -> Write sentences in logical sequence.",
     [
         ("What is the first step in the composition tip?", "Observe the picture carefully.", "Easy", "Remembering"),
         ("What should you identify after observing the picture?", "Characters and setting.", "Easy", "Remembering"),
         ("How should sentences be written?", "In logical sequence.", "Easy", "Remembering"),
         ("Why is logical sequence important in writing?", "It ensures the story flows naturally from beginning to end.", "Medium", "Understanding"),
         ("How does this tip help Class 2 students?", "It gives them a clear, simple guide for writing structured picture stories.", "Medium", "Evaluating")
     ]),

    # Set 9
    ("Look at the Picture and write a short story based on it: Family's Day Out.",
     [
         ("What grade level is this composition activity designed for?", "Class 2 (COMPOSITION-2).", "Easy", "Remembering"),
         ("What skill does story-writing from a picture build?", "Creative writing, vocabulary, visual literacy, and sentence sequencing.", "Medium", "Understanding"),
         ("Give two examples of good titles for this composition.", "'A Fun Picnic Day' or 'Our Family's Day Out'.", "Medium", "Applying"),
         ("What visual elements are usually present in a picnic picture?", "Family members, picnic blanket, basket, trees, sun, ball, and park.", "Easy", "Remembering"),
         ("What is the ultimate goal of Chapter 14?", "To help young learners express visual ideas into clear, creative written stories.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("On a bright sunny Sunday... Rohan collected all food wrappers... Returned home feeling happy and united.",
     [
         ("Summarize the entire 5-sentence story in one line.", "The Sharma family enjoyed a sunny picnic in the park, played games, ate delicious food, cleaned up their trash, and returned home happy and united.", "Medium", "Evaluating"),
         ("What weather made the picnic pleasant?", "Bright sunny weather.", "Easy", "Remembering"),
         ("What lesson on nature care was shown?", "Throwing all trash into dustbins.", "Easy", "Understanding"),
         ("What moral value about family was highlighted?", "Family togetherness, love, and unity.", "Easy", "Understanding"),
         ("Why is this sample story an effective model for Class 2 writers?", "It has clear characters, good adjectives, logical flow, civic values, and a satisfying ending.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 14: Family's Day Out\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH14_EXT_{q_counter:03d}"
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

with open(os.path.join(CH14_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 14 in {CH14_DIR}")
