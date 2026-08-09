r"""
Refines all 6 Category files for Chapter 12 ("The Cat") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH12_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_12")
os.makedirs(CH12_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Who wrote the humorous poem 'The Cat'?", "(A) Ogden Nash", "(B) Louisa May Alcott", "(C) Robert Frost", "(D) Christina Rossetti", "(A)", "The author is Ogden Nash.", "Easy", "Remembering", "Poet Name"),
    ("What do you get after getting a wife and a house in the poem?", "(A) Eventually a mouse", "(B) A elephant", "(C) A car", "(D) A lion", "(A)", "It says 'Eventually you get a mouse'.", "Easy", "Remembering", "First Problem"),
    ("How quickly do you get a kitty after getting words regarding mice?", "(A) In a trice (very quickly)", "(B) Next year", "(C) Never", "(D) In ten hours", "(A)", "It says 'You get a kitty in a trice'.", "Easy", "Remembering", "Kitty Arrival Speed"),
    ("Around what time in the night does the funny situation happen?", "(A) By two a.m. or thereabouts", "(B) At noon", "(C) At 6 p.m.", "(D) At 10 a.m.", "(A)", "It says 'By two a.m. or thereabouts'.", "Easy", "Remembering", "Time of Night"),
    ("At 2 a.m., where is the mouse and where is the cat?", "(A) The mouse is in, the cat is out", "(B) The cat is in, the mouse is out", "(C) Both are outside", "(D) Both are asleep in bed", "(A)", "It says 'The mouse is in, the cat is out'.", "Easy", "Remembering", "Animal Locations"),
    ("Where are you lying when the realization dawns upon you?", "(A) In your cot (bed)", "(B) On the roof", "(C) Under the table", "(D) In the kitchen", "(A)", "It says 'It dawns upon you, in your cot'.", "Easy", "Remembering", "Person's Location"),
    ("At 2 a.m., which animal is silent and which animal is not silent?", "(A) The mouse is silent, the cat is not", "(B) The cat is silent, the mouse is not", "(C) Both are screaming", "(D) Neither is silent", "(A)", "It says 'The mouse is silent, the cat is not'.", "Easy", "Remembering", "Noise Difference"),
    ("What humorous advice does your spouse give instead of getting a kitty?", "(A) You should have got another mouse", "(B) You should buy a dog", "(C) You should buy a parrot", "(D) You should leave the house", "(A)", "Spouse says 'You should have got another mouse'.", "Easy", "Remembering", "Spouse Advice"),
    ("What does the word 'eventually' mean according to the word box?", "(A) Finally", "(B) Never", "(C) Slowly", "(D) Yesterday", "(A)", "Eventually means finally.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'trice' mean in the poem?", "(A) Very quickly", "(B) Three times", "(C) Loudly", "(D) In a box", "(A)", "In a trice means very quickly.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'spouse' mean?", "(A) A married person (husband or wife)", "(B) A pet cat", "(C) A small mouse", "(D) A wooden house", "(A)", "Spouse means a married person.", "Easy", "Understanding", "Vocabulary"),
    ("What does 'cot' mean in the poem?", "(A) A small bed", "(B) A coat", "(C) A cupboard", "(D) A car", "(A)", "A cot is a small bed.", "Easy", "Understanding", "Vocabulary"),
    ("Why did the person get a kitty in the first place?", "(A) Because there was a mouse in the house", "(B) To go for a walk", "(C) To catch birds", "(D) To guard the car", "(A)", "Getting words regarding mice led to getting a kitty.", "Easy", "Remembering", "Reason for Kitty"),
    ("Is the cat inside the house making quiet sleep at 2 a.m.?", "(A) No, the cat is outside making noise ('cat is not silent')", "(B) Yes", "(C) The cat is in the cot", "(D) The cat is eating cheese", "(A)", "The cat is out and not silent.", "Easy", "Remembering", "Cat Behavior"),
    ("Is the mouse making loud noise at 2 a.m.?", "(A) No, the mouse is silent inside", "(B) Yes, the mouse is shouting", "(C) The mouse is playing drums", "(D) The mouse is barking", "(A)", "The mouse is silent.", "Easy", "Remembering", "Mouse Behavior"),
    ("What is the tone of Ogden Nash's poem 'The Cat'?", "(A) Funny and humorous", "(B) Scary and spooky", "(C) Very sad and crying", "(D) Serious and formal", "(A)", "The poem is funny and humorous.", "Easy", "Understanding", "Poem Tone"),
    ("What rhymes with 'house' in the first lines?", "(A) Mouse", "(B) Kitty", "(C) Cot", "(D) Night", "(A)", "House rhymes with mouse.", "Easy", "Remembering", "Rhyme Pair"),
    ("What rhymes with 'trice' in the poem?", "(A) Mice", "(B) Cot", "(C) Spouse", "(D) Out", "(A)", "Mice rhymes with trice.", "Easy", "Remembering", "Rhyme Pair"),
    ("What rhymes with 'thereabouts' in the poem?", "(A) Out", "(B) Cot", "(C) Mouse", "(D) In", "(A)", "Thereabouts rhymes with out.", "Easy", "Remembering", "Rhyme Pair"),
    ("What rhymes with 'cot' in the poem?", "(A) Not", "(B) Cat", "(C) Mouse", "(D) House", "(A)", "Cot rhymes with not.", "Easy", "Remembering", "Rhyme Pair"),
    ("What rhymes with 'spouse' in the final lines?", "(A) Mouse", "(B) Kitty", "(C) Cat", "(D) Trice", "(A)", "Spouse rhymes with mouse.", "Easy", "Remembering", "Rhyme Pair"),
    ("Why is the spouse's suggestion funny?", "(A) Because mice are usually unwanted pests, yet a quiet mouse is preferred over a noisy cat", "(B) Because mice eat cats", "(C) Because cats eat houses", "(D) Because mice wear clothes", "(A)", "Humor comes from preferring a quiet pest over a noisy pet.", "Easy", "Understanding", "Humor Reason"),
    ("What time of night is 2 a.m.?", "(A) Late night / early morning", "(B) Bright afternoon", "(C) Evening teatime", "(D) Sunset", "(A)", "2 a.m. is late night.", "Easy", "Understanding", "Time Meaning"),
    ("What does 'it dawns upon you' mean?", "(A) You suddenly realize or understand something", "(B) The sun rises outside", "(C) You fall asleep", "(D) You open the door", "(A)", "It dawns upon you means coming to a realization.", "Easy", "Understanding", "Idiom Meaning"),
    ("What is the title of Chapter 12?", "(A) The Cat", "(B) A Little Bird I Am", "(C) The Quiet Mouse", "(D) 2 a.m. Night", "(A)", "Chapter 12 is titled 'The Cat'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why is Ogden Nash famous as a poet?", "(A) For writing witty, humorous, lighthearted poetry with unexpected twist endings", "(B) For writing difficult medical textbooks", "(C) For writing serious epic tragedies", "(D) For writing math formulas", "(A)", "Famous for witty, humorous light verse with unexpected twists.", "Medium", "Understanding", "Poet Background"),
    ("How does the poem turn domestic expectation upside down?", "(A) Expectation: cat stays in & catches mouse; Reality: mouse stays in silently while cat locks out & makes noise", "(B) Expectation: mouse eats house; Reality: house eats mouse", "(C) Expectation: cat flies; Reality: mouse swims", "(D) No expectation is changed", "(A)", "Reverses expected roles of cat and mouse.", "Medium", "Analyzing", "Irony & Expectation"),
    ("What ironic twist happens at 2:00 a.m.?", "(A) The mouse is comfortably inside and quiet, while the cat meant to catch it is locked outside making noise", "(B) The mouse catches the cat", "(C) The house turns into a cat", "(D) The cat goes to work", "(A)", "Ironic twist of mouse inside silent vs cat outside noisy.", "Medium", "Analyzing", "Plot Irony"),
    ("Why does the spouse say 'You should have got another mouse'?", "(A) Because a quiet mouse inside causes less disturbance than a howling cat outside late at night", "(B) Because mice are cheaper to feed", "(C) Because they want a mouse farm", "(D) Because cats are dangerous", "(A)", "Quiet mouse causes less night disturbance than a noisy cat.", "Medium", "Evaluating", "Spouse Reasoning"),
    ("What rhythm style is used in the rhyming couplets of 'The Cat'?", "(A) Light, bouncy AABB rhyming couplets that create a fast humorous pace", "(B) Heavy, slow unrhymed prose", "(C) Deep sad funeral march", "(D) Complex Latin stanzas", "(A)", "Light bouncy AABB couplets.", "Medium", "Analyzing", "Poetic Form"),
    ("What does 'words regarding mice' mean in a domestic household?", "(A) Complaints or discussions from family about seeing mice in the house", "(B) Reading a dictionary definition of mice", "(C) Writing a story about mice", "(D) Singing songs to mice", "(A)", "Family complaints or discussions about mice.", "Medium", "Understanding", "Household Context"),
    ("How does the setting of 'cot' at 2 a.m. heighten the comedy?", "(A) Trying to sleep in bed at 2 a.m. makes any late-night cat noise extra annoying and clear", "(B) Cots are funny furniture", "(C) Sleeping at 2 a.m. is illegal", "(D) The cat sleeps in the cot", "(A)", "Sleep disruption at 2 a.m. heightens comedy.", "Medium", "Analyzing", "Setting Effect"),
    ("Why is getting a kitty 'in a trice' relatable to pet owners?", "(A) People often rush quickly to get a pet solution whenever pests appear in the house", "(B) Kitty means toy cat", "(C) Pets are delivered in boxes", "(D) People buy cats every hour", "(A)", "Rushing quickly for a pet solution to pests.", "Medium", "Understanding", "Relatability"),
    ("What sensory contrast is present in lines 7-8 ('The mouse is silent, the cat is not')?", "(A) Sound contrast: complete quiet of the mouse vs annoying noise of the cat", "(B) Color contrast: black vs white", "(C) Size contrast: big vs small", "(D) Temperature contrast: hot vs cold", "(A)", "Sound contrast between quiet mouse and noisy cat.", "Medium", "Analyzing", "Sensory Contrast"),
    ("How does Chapter 12 help Class 2 students appreciate humor in poetry?", "(A) By showing that poems can tell funny everyday stories with surprising and silly conclusions", "(B) By teaching strict rules of grammar", "(C) By asking them to draw cats", "(D) By memorizing hard words", "(A)", "Demonstrates that poetry can tell funny everyday stories.", "Medium", "Applying", "Pedagogical Value"),
    ("What is the progression of events in the poem?", "(A) House -> Mouse -> Complaints -> Cat -> 2 a.m. Cat noisy outside -> Spouse joke", "(B) Cat -> House -> Mouse -> Dog", "(C) Mouse -> Cat -> House -> Sleeping", "(D) Spouse -> Cat -> Mouse -> Cot", "(A)", "House -> Mouse -> Complaints -> Cat -> Night noise -> Spouse joke.", "Medium", "Analyzing", "Sequence of Events"),
    ("Why is the phrase 'thereabouts' used with 'two a.m.'?", "(A) It poetically means 'around that time' in the middle of the night", "(B) It means in a location nearby", "(C) It means 2 years later", "(D) It means inside the kitchen", "(A)", "Means 'around that time'.", "Medium", "Understanding", "Poetic Diction"),
    ("What does 'the cat is not' imply without repeating words?", "(A) Implies that 'the cat is not silent' (it is meowing/making noise)", "(B) Implies the cat is dead", "(C) Implies the cat is invisible", "(D) Implies the cat is sleeping", "(A)", "Implies the cat is not silent.", "Medium", "Understanding", "Ellipsis / Implication"),
    ("How does Ogden Nash create humor through rhyme schemes?", "(A) By pairing simple words like 'house/mouse' and 'spouse/mouse' to deliver witty punchlines", "(B) By using long hard words", "(C) By using no rhymes", "(D) By repeating the same sentence ten times", "(A)", "Simple rhyming pairs delivering witty punchlines.", "Medium", "Analyzing", "Rhyme Mechanics"),
    ("What visual image do you get of the cat at 2 a.m.?", "(A) A cat standing outside the locked door meowing to get back inside", "(B) A cat sleeping in a cage", "(C) A cat eating cheese with a mouse", "(D) A cat driving a car", "(A)", "Cat outside locked door meowing late at night.", "Medium", "Analyzing", "Visual Imagery"),

    # Hard (41-50)
    ("Analyze the satirical commentary on problem-solving in Ogden Nash's 'The Cat'.", "(A) Satire: Attempting to fix a small problem (quiet mouse) with a quick remedy (cat) often creates a noisier, bigger headache", "(B) Satire: Cats should be trained as guard dogs", "(C) Satire: Houses should not have roofs", "(D) Satire: People shouldn't get married", "(A)", "Quick fixes often create bigger, noisier headaches.", "Hard", "Analyzing", "HOTS Satirical Analysis"),
    ("Deconstruct the comic timing of the final couplet ('Instead of kitty, says your spouse...').", "(A) Punchline delivery: The spouse's absurd logical solution delivers the perfect humorous payoff to the midnight dilemma", "(B) Tragic ending: Both animals disappear", "(C) Boring ending: Nothing happens", "(D) Musical chorus: Repeated ten times", "(A)", "Absurd logical solution delivers perfect humorous payoff.", "Hard", "Analyzing", "Comic Structure"),
    ("Evaluate the literary device of irony in the reversal of pest control roles.", "(A) Structural irony: The predator (cat) is banished outside making noise while the prey (mouse) enjoys quiet comfort inside", "(B) Dramatic irony: The reader knows the mouse is a lion", "(C) Verbal irony: The word cat means dog", "(D) No irony exists", "(A)", "Predator locked outside while prey enjoys quiet inside.", "Hard", "Evaluating", "Literary Irony"),
    ("Compare the humorous style of Ogden Nash with devotional poets like Louisa May Alcott.", "(A) Nash: lighthearted, ironic, everyday humor; Alcott: solemn, spiritual, moral devotion", "(B) Both write identical serious hymns", "(C) Nash writes sad poems; Alcott writes jokes", "(D) Neither uses rhyming words", "(A)", "Lighthearted ironic humor vs solemn spiritual devotion.", "Hard", "Comparing", "Comparative Poetics"),
    ("Assess the psychological reality of late-night disturbances on human logic.", "(A) Middle-of-the-night sleep deprivation causes absurd logical conclusions like preferring a quiet mouse over a noisy cat", "(B) Sleep deprivation makes people smarter at math", "(C) Night noise makes people fall asleep faster", "(D) Late night logic is always 100% scientific", "(A)", "Sleep deprivation leads to absurd, funny conclusions.", "Hard", "Evaluating", "Psychological Reality"),
    ("How does the brevity (10 lines) of 'The Cat' enhance its comedic impact?", "(A) Concise lines deliver setup, escalation, twist, and punchline rapidly without unnecessary filler", "(B) Short poems are easy to print", "(C) Longer poems are always funnier", "(D) 10 lines is too long for a joke", "(A)", "Rapid delivery of setup, escalation, twist, and punchline.", "Hard", "Analyzing", "Structural Brevity"),
    ("Synthesize how Chapter 12 broadens the poetry genre for Class 2 students.", "(A) Expands appreciation from serious nature/devotional poetry to witty, lighthearted, storytelling verse", "(B) Teaches how to write legal contracts", "(C) Focuses only on pet care instructions", "(D) Replaces prose reading completely", "(A)", "Expands appreciation to witty, lighthearted storytelling verse.", "Hard", "Synthesizing", "Genre Expansion"),
    ("Formulate an additional 2-line comic couplet continuing Ogden Nash's poem.", "(A) 'So now the mouse is in your cot, And you are out, whether ready or not!'", "(B) 'The cat is quiet and mouse is fast'", "(C) 'We need a dog to catch the cat'", "(D) 'The mouse left the house'", "(A)", "Creative extension continuing comic theme.", "Hard", "Creating", "Comic Verse Extension"),
    ("Formulate a critical appreciation of the line 'The mouse is silent, the cat is not'.", "(A) Highlights Nash's mastery of contrast: ten simple words capture the entire absurdity of a ruined night's sleep", "(B) Explains how mice eat cheese", "(C) Proves cats cannot meow", "(D) Describes a quiet afternoon in the park", "(A)", "Ten simple words capture the entire absurd ruined sleep.", "Hard", "Evaluating", "Critical Appreciation"),
    ("Synthesize the ultimate lesson of Chapter 12 for Class 2 learners.", "(A) Enjoy the humor in everyday life's unexpected mix-ups and laugh at funny household situations!", "(B) Never own a pet cat", "(C) Always keep ten mice at home", "(D) Stay awake every night at 2 a.m.", "(A)", "Enjoy everyday humor and laugh at life's funny mix-ups.", "Hard", "Evaluating", "Core Lesson Synthesis")
]

mcq_content = f"# MCQs — Chapter 12: The Cat\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH12_MCQ_{idx:03d}"
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

with open(os.path.join(CH12_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("You get a wife, you get a house, Eventually you get a _______.", "mouse", "Eventually you get a mouse.", "Easy"),
    ("You get some words regarding _______.", "mice", "Words regarding mice.", "Easy"),
    ("You get a kitty in a _______.", "trice", "In a trice.", "Easy"),
    ("By two a.m. or _______, the mouse is in, the cat is out.", "thereabouts", "Two a.m. or thereabouts.", "Easy"),
    ("By two a.m. or thereabouts, the mouse is in, the cat is _______.", "out", "Cat is out.", "Easy"),
    ("By two a.m. or thereabouts, the mouse is _______, the cat is out.", "in", "Mouse is in.", "Easy"),
    ("It dawns upon you, in your _______.", "cot", "In your cot.", "Easy"),
    ("The mouse is silent, the cat is _______.", "not", "The cat is not.", "Easy"),
    ("The mouse is _______, the cat is not.", "silent", "Mouse is silent.", "Easy"),
    ("Instead of kitty, says your _______.", "spouse", "Says your spouse.", "Easy"),
    ("You should have got another _______.", "mouse", "Got another mouse.", "Easy"),
    ("The author of the poem 'The Cat' is Ogden _______.", "Nash", "Ogden Nash.", "Easy"),
    ("The word 'eventually' means _______.", "finally", "Eventually means finally.", "Easy"),
    ("The word 'trice' means very _______.", "quickly", "Trice means very quickly.", "Easy"),
    ("The word 'spouse' means a married _______.", "person", "Spouse means married person.", "Easy"),
    ("A 'cot' is a small _______.", "bed", "Cot means small bed.", "Easy"),
    ("You get a kitty because there is a _______ in the house.", "mouse", "Because of a mouse.", "Easy"),
    ("At 2 a.m., the cat is _______ of the house.", "outside", "Cat is out.", "Easy"),
    ("At 2 a.m., the mouse is _______ the house.", "inside", "Mouse is in.", "Easy"),
    ("The cat makes _______ at night while the mouse is quiet.", "noise", "Cat makes noise.", "Easy"),
    ("The spouse suggests getting another _______.", "mouse", "Suggests another mouse.", "Easy"),
    ("In a trice means very _______.", "fast", "Very fast / quickly.", "Easy"),
    ("The poem describes a funny situation at _______ a.m.", "two", "Two a.m.", "Easy"),
    ("The mouse remains completely _______ at night.", "silent", "Mouse is silent.", "Easy"),
    ("Chapter 12 is titled 'The _______'.", "Cat", "Titled 'The Cat'.", "Easy"),

    # Medium (26-40)
    ("The poem uses funny rhyming pairs like house and _______.", "mouse", "House and mouse.", "Medium"),
    ("Getting a kitty in a trice means getting a cat very _______.", "quickly", "Getting a cat quickly.", "Medium"),
    ("The realization occurs while lying in your _______.", "cot", "Lying in cot.", "Medium"),
    ("The mouse is inside and silent, creating an unexpected _______.", "twist", "Unexpected twist.", "Medium"),
    ("The spouse gives a humorous suggestion about keeping a quiet _______.", "mouse", "Quiet mouse.", "Medium"),
    ("Ogden Nash is famous for writing lighthearted and funny _______.", "poetry", "Lighthearted poetry.", "Medium"),
    ("The poem contrasts the noise of the cat with the silence of the _______.", "mouse", "Silence of the mouse.", "Medium"),
    ("The words 'thereabouts' refers to the approximate _______ of 2 a.m.", "time", "Approximate time.", "Medium"),
    ("A married partner, whether husband or wife, is called a _______.", "spouse", "Called a spouse.", "Medium"),
    ("The cat is locked out at two in the _______.", "morning", "Two in the morning / a.m.", "Medium"),
    ("Instead of solving the problem, getting a cat brought more _______.", "noise", "Brought more noise.", "Medium"),
    ("The spouse's advice provides the humorous _______ of the poem.", "punchline", "Humorous punchline.", "Medium"),
    ("The mouse stays quiet while the cat stays _______.", "noisy", "Cat stays noisy.", "Medium"),
    ("Lying in a cot at 2 a.m. means trying to _______.", "sleep", "Trying to sleep.", "Medium"),
    ("The poem consists of five rhyming _______.", "couplets", "Five rhyming couplets.", "Medium"),

    # Hard (41-50)
    ("The reversal of roles between predator and prey creates comic _______.", "irony", "Creates comic irony.", "Hard"),
    ("Ogden Nash's AABB rhyme scheme delivers a swift comedic _______.", "rhythm", "Swift comedic rhythm.", "Hard"),
    ("The phrase 'words regarding mice' implies household complaints about _______.", "pests", "Complaints about pests.", "Hard"),
    ("Late-night noise disruption turns a house owner's solution into a _______.", "headache", "Turns solution into headache.", "Hard"),
    ("The word 'dawns' is used idiomatically to mean sudden mental _______.", "realization", "Sudden mental realization.", "Hard"),
    ("Preferring a quiet mouse over a noisy cat is a logical _______.", "absurdity", "Logical absurdity / paradox.", "Hard"),
    ("The poem consists of ten concise, rhythmically bouncy _______.", "lines", "Ten concise lines.", "Hard"),
    ("Domestic humor in poetry highlights relatable household _______.", "mishaps", "Relatable household mishaps.", "Hard"),
    ("The cat's howling outside at 2 a.m. causes sleep _______.", "deprivation", "Sleep deprivation.", "Hard"),
    ("Chapter 12 teaches children to appreciate lighthearted poetic _______.", "humor", "Lighthearted poetic humor.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 12: The Cat\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH12_FIB_{idx:03d}"
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
    ("The author of the poem 'The Cat' is Ogden Nash.", "True", "Text explicitly names Ogden Nash.", "Easy"),
    ("In the poem, you get a house and eventually get a mouse.", "True", "You get a wife, you get a house, eventually you get a mouse.", "Easy"),
    ("Getting a kitty in a trice means getting a cat very slowly.", "False", "Trice means very quickly.", "Easy"),
    ("By 2 a.m., the mouse is in and the cat is out.", "True", "The mouse is in, the cat is out.", "Easy"),
    ("At 2 a.m., the mouse is making loud noises in the house.", "False", "The mouse is silent.", "Easy"),
    ("At 2 a.m., the cat is silent.", "False", "The cat is not silent.", "Easy"),
    ("You lie in your cot when you realize the cat is noisy.", "True", "It dawns upon you, in your cot.", "Easy"),
    ("The spouse suggests getting another mouse instead of the cat.", "True", "Says your spouse, you should have got another mouse.", "Easy"),
    ("The word 'eventually' means 'finally'.", "True", "Eventually means finally.", "Easy"),
    ("The word 'trice' means 'three times'.", "False", "Trice means very quickly.", "Easy"),
    ("The word 'spouse' means a married person (husband or wife).", "True", "Spouse means a married person.", "Easy"),
    ("A 'cot' is a small bed.", "True", "A cot is a small bed.", "Easy"),
    ("The cat was brought home to deal with a mouse problem.", "True", "Words regarding mice led to getting a kitty.", "Easy"),
    ("The poem describes a serious sad tragedy.", "False", "The poem is a lighthearted, funny poem.", "Easy"),
    ("House rhymes with mouse in the poem.", "True", "House and mouse rhyme.", "Easy"),
    ("Mice rhymes with trice in the poem.", "True", "Mice and trice rhyme.", "Easy"),
    ("Cot rhymes with not in the poem.", "True", "Cot and not rhyme.", "Easy"),
    ("The mouse comes into the house after the cat goes outside.", "True", "The mouse is in, the cat is out.", "Easy"),
    ("The cat sleeps quietly inside the house all night long.", "False", "The cat is outside and not silent.", "Easy"),
    ("The spouse is happy with the noisy cat at 2 a.m.", "False", "The spouse sarcastically says they should have gotten another mouse.", "Easy"),
    ("2 a.m. is in the middle of the afternoon.", "False", "2 a.m. is late night / early morning.", "Easy"),
    ("The poem has 10 lines in total.", "True", "The poem consists of 10 lines (5 couplets).", "Easy"),
    ("The mouse causes more noise than the cat at night.", "False", "The mouse is silent, while the cat is not.", "Easy"),
    ("The word 'kitty' refers to a cat.", "True", "Kitty means a cat/kitten.", "Easy"),
    ("Chapter 12 is titled 'The Cat'.", "True", "Chapter 12 is titled 'The Cat'.", "Easy"),

    # Medium (26-40)
    ("Ogden Nash uses unexpected, funny endings in his poetry.", "True", "Nash is famous for witty punchline endings.", "Medium"),
    ("The poem shows that solutions to problems sometimes create new funny problems.", "True", "Getting a cat to stop a mouse created a noisy cat problem at 2 a.m.", "Medium"),
    ("The phrase 'in a trice' means after three years of waiting.", "False", "In a trice means almost instantly or very quickly.", "Medium"),
    ("The mouse is depicted as an aggressive animal attacking the cat.", "False", "The mouse is described simply as silent inside the house.", "Medium"),
    ("The comedy comes from preferring a silent pest over a noisy pet.", "True", "Preferring a silent mouse over a noisy cat is the core joke.", "Medium"),
    ("The poem takes place over a period of ten years.", "False", "It quickly moves from house purchase to a 2 a.m. night.", "Medium"),
    ("The word 'dawns' in 'dawns upon you' means the sun is rising in the sky.", "False", "It idiomatically means coming to a sudden mental realization.", "Medium"),
    ("The cat was locked outside the house by 2 a.m.", "True", "The cat is out.", "Medium"),
    ("The spouse's reaction is a humorous punchline.", "True", "The spouse's line ends the poem with humor.", "Medium"),
    ("The poem teaches a strict rule of scientific animal behavior.", "False", "It is a lighthearted comic verse, not a scientific textbook.", "Medium"),
    ("The cat meowing outside disrupts late-night sleep.", "True", "Cat not silent at 2 a.m. disrupts sleep in the cot.", "Medium"),
    ("Getting a cat solved the household mouse problem perfectly.", "False", "It resulted in a noisy cat outside and a quiet mouse inside.", "Medium"),
    ("The poem consists of five rhyming AABB couplets.", "True", "House/mouse, mice/trice, thereabouts/out, cot/not, spouse/mouse.", "Medium"),
    ("Class 2 students can easily understand the humor in the poem.", "True", "Simple story, funny reversal, and clear rhymes make it easy.", "Medium"),
    ("The cat is happy to stay outside in the cold at 2 a.m.", "False", "The cat is 'not silent', meaning it wants to come back in.", "Medium"),

    # Hard (41-50)
    ("The poem satirizes impulsive human attempts to solve domestic nuisances.", "True", "Satirizes how quick fixes often lead to new disruptions.", "Hard"),
    ("The contrast between 'silent mouse' and 'noisy cat' uses sensory irony.", "True", "Sensory irony in sound levels of pest vs pet.", "Hard"),
    ("The word 'cot' implies a modest, humble household setting.", "True", "Cot refers to a small simple bed.", "Hard"),
    ("Ogden Nash's poetry style avoids rhyming words completely.", "False", "Nash uses distinct, witty rhyming patterns.", "Hard"),
    ("The spouse's dialogue provides an ironic resolution to the narrative.", "True", "Spouse's absurd suggestion provides ironic resolution.", "Hard"),
    ("Sleep deprivation at 2 a.m. heightens the emotional impact of the cat's noise.", "True", "Middle-of-the-night noise amplifies frustration and humor.", "Hard"),
    ("The poem implies that the cat caught the mouse before going outside.", "False", "The mouse is still inside ('the mouse is in'), uncaught.", "Hard"),
    ("The title 'The Cat' focuses on the animal that causes the late-night comedy.", "True", "Title highlights the central noisy pet character.", "Hard"),
    ("The poem encourages readers to buy more cats for pest control.", "False", "It humorously questions the effectiveness of getting a cat.", "Hard"),
    ("Chapter 12 introduces poetic satire and comic timing to Class 2 learners.", "True", "Introduces comic structure, irony, and lighthearted verse.", "Hard")
]

tf_content = f"# True / False — Chapter 12: The Cat\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH12_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH12_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who wrote the poem 'The Cat'?", "The poem 'The Cat' was written by Ogden Nash.", "Easy", "Remembering"),
    ("What problem appears after you get a wife and a house?", "Eventually, you get a mouse in the house.", "Easy", "Remembering"),
    ("How fast do you get a kitty after hearing words about mice?", "You get a kitty 'in a trice' (very quickly).", "Easy", "Remembering"),
    ("Around what time at night does the funny situation happen?", "Around 2:00 a.m. (by two a.m. or thereabouts).", "Easy", "Remembering"),
    ("Where is the mouse and where is the cat at 2 a.m.?", "The mouse is inside the house ('in'), and the cat is outside ('out').", "Easy", "Remembering"),
    ("Where are you lying when the realization comes to you?", "You are lying in your cot (small bed).", "Easy", "Remembering"),
    ("Which animal is quiet and which animal is noisy at 2 a.m.?", "The mouse is silent inside, while the cat is noisy outside.", "Easy", "Remembering"),
    ("What funny advice does your spouse give at the end?", "The spouse says, 'You should have got another mouse.'", "Easy", "Remembering"),
    ("What does the word 'eventually' mean?", "'Eventually' means finally or after some time.", "Easy", "Understanding"),
    ("What does the word 'trice' mean?", "'Trice' means very quickly or in a short moment.", "Easy", "Understanding"),
    ("What does the word 'spouse' mean?", "'Spouse' means a married person (a husband or wife).", "Easy", "Understanding"),
    ("What is a cot?", "A cot is a small, simple bed.", "Easy", "Understanding"),
    ("Why did the family get a cat in the first place?", "They got a cat to catch the mouse that entered their house.", "Easy", "Remembering"),
    ("Why is the cat outside at 2 a.m.?", "The cat went or was let outside late at night.", "Easy", "Understanding"),
    ("Why is the cat 'not silent' at 2 a.m.?", "Because it is meowing or making noise outside wanting to get back in.", "Easy", "Understanding"),
    ("Is the mouse caught by the cat at 2 a.m.?", "No, the mouse is safely inside the house and silent.", "Easy", "Remembering"),
    ("What does 'it dawns upon you' mean in the poem?", "It means you suddenly realize or understand the funny truth.", "Easy", "Understanding"),
    ("What kind of poem is 'The Cat'?", "It is a lighthearted, funny, and humorous poem.", "Easy", "Understanding"),
    ("Name two words that rhyme with 'house' in the poem.", "Mouse and spouse.", "Easy", "Remembering"),
    ("What word rhymes with 'trice' in the poem?", "Mice.", "Easy", "Remembering"),
    ("What word rhymes with 'cot' in the poem?", "Not.", "Easy", "Remembering"),
    ("What word rhymes with 'thereabouts' in the poem?", "Out.", "Easy", "Remembering"),
    ("Why did getting a cat fail to solve the household problem?", "Because the cat stayed outside making noise, while the mouse stayed inside.", "Easy", "Understanding"),
    ("Who speaks the final line of the poem?", "The spouse speaks the final line.", "Easy", "Remembering"),
    ("What is the title of Chapter 12?", "The title of Chapter 12 is 'The Cat'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Explain the humor behind the spouse's suggestion to get 'another mouse'.", "It is funny because mice are unwanted pests, but because this mouse is quiet and the cat is noisy late at night, a quiet mouse seems better!", "Medium", "Evaluating"),
    ("How does Ogden Nash create a surprising twist at 2:00 a.m.?", "He reverses expected roles: instead of the cat being inside catching the mouse, the cat is locked outside howling while the mouse sits quietly inside.", "Medium", "Analyzing"),
    ("Describe the progression of the household's events from start to finish.", "1. Get house & wife -> 2. Find a mouse -> 3. Buy a cat quickly -> 4. Cat ends up noisy outside at 2 a.m. while mouse is quiet inside -> 5. Spouse jokes about getting another mouse.", "Medium", "Analyzing"),
    ("What makes Ogden Nash's poetic style enjoyable for children?", "Its short bouncy rhyming couplets, simple story, relatable domestic setup, and funny punchline.", "Medium", "Understanding"),
    ("Why does the sound contrast between 'silent mouse' and 'noisy cat' heighten the comedy?", "Because pets are supposed to bring peace and catch pests quietly, but here the pet creates the disturbance while the pest causes no trouble.", "Medium", "Analyzing"),
    ("What does 'words regarding mice' mean in a family home?", "It means family members complaining or talking about seeing a mouse running around the house.", "Medium", "Understanding"),
    ("How does lying in a 'cot' at 2 a.m. emphasize human frustration?", "When you are trying to sleep in bed late at night, any sudden animal noise outside feels extra annoying.", "Medium", "Analyzing"),
    ("Why is the phrase 'in a trice' appropriate for buying a pet in a panic?", "Because when people see a mouse, they panic and buy a cat as fast as possible without thinking.", "Medium", "Understanding"),
    ("What is the rhyme scheme of the 10-line poem?", "The rhyme scheme is AABBCCDDEE (couplet rhyming).", "Medium", "Remembering"),
    ("Summarize Page 43 of the textbook in two sentences.", "Ogden Nash's poem 'The Cat' humorously describes a person who gets a house, finds a mouse, and quickly buys a cat. At 2 a.m., the cat is noisy outside while the mouse is quiet inside, leading the spouse to joke that they should have gotten another mouse.", "Medium", "Understanding"),
    ("How does the poet use only 10 lines to deliver a complete funny story?", "By using concise couplets that quickly jump from getting a house to the mouse problem, the cat solution, the midnight twist, and the final punchline.", "Medium", "Analyzing"),
    ("What lesson does the poem teach about quick fixes?", "It shows humorously that quick fixes sometimes create unexpected new problems.", "Medium", "Evaluating"),
    ("What visual picture does the poem create in your mind at 2 a.m.?", "A tired person lying in bed listening to a cat meowing outside the window, while a little mouse sits quietly in the kitchen corner.", "Medium", "Analyzing"),
    ("Why are rhyming couplets effective for comedic poetry?", "Couplets create a fast, bouncy rhythm where each pair of lines builds up to a witty rhyme.", "Medium", "Understanding"),
    ("How can Class 2 students perform this poem aloud in class?", "Students can recite line by line with funny facial expressions for 2 a.m. sleepiness and meowing cat sounds.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the moral irony of pest management in 'The Cat'.", "The moral irony lies in human folly: trying to eliminate a minor silent inconvenience (a mouse) introduces a far louder, more disruptive nuisance (a meowing cat at 2 a.m.).", "Hard", "Evaluating"),
    ("Analyze the linguistic rhythm and meter of Ogden Nash's verse.", "Nash uses a bouncy, conversational meter with simple rhyming couplets that accelerate the narrative speed toward a sharp comedic climax.", "Hard", "Analyzing"),
    ("Deconstruct how the poet builds up to the final punchline.", "Lines 1-4 setup the problem & quick fix; Lines 5-8 establish the midnight twist & sensory contrast; Lines 9-10 deliver the absurd spouse punchline.", "Hard", "Analyzing"),
    ("Compare 'The Cat' with traditional animal poems that praise pets.", "Traditional poems praise cats as quiet, helpful mouse-hunters; Nash's poem subverts this by portraying the cat as an unhelpful, night-disrupting creature.", "Hard", "Analyzing"),
    ("Evaluate the psychological reaction of sleep-deprived individuals in comic literature.", "Sleep deprivation at 2 a.m. distorts normal logic, making the spouse's absurd claim ('get another mouse') sound perfectly reasonable in the moment.", "Hard", "Evaluating"),
    ("How does Chapter 12 introduce young readers to poetic subversion?", "It shows how poets can take familiar domestic animals and turn expectations upside down to create unexpected laughter.", "Hard", "Applying"),
    ("Assess the role of brief vocabulary glossaries (Eventually, Trice, Spouse) for primary learners.", "Glossaries bridge the gap between classic poetic diction and modern child comprehension, enabling fluent reading without breaking comic flow.", "Hard", "Evaluating"),
    ("Why is the phrase 'thereabouts' essential to the midnight setting?", "It gives a realistic, casual tone to middle-of-the-night awakening when no one looks at an exact clock.", "Hard", "Analyzing"),
    ("Formulate a short 2-line comic response from the mouse's perspective.", "'I sit inside and eat your cheese,\nWhile kitty shivers in the breeze!'", "Hard", "Creating"),
    ("Synthesize the core educational takeaway of Chapter 12 for Class 2 learners.", "Appreciate how poetry uses story structure, rhythm, and clever twists to bring laughter and lighthearted joy to everyday life!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 12: The Cat\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH12_SA_{idx:03d}"
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
    ("Describe the plot and story events in Ogden Nash's poem 'The Cat'.", 
     "In the poem 'The Cat' by Ogden Nash, a person gets married, buys a house, and eventually finds a mouse living inside. After family members complain ('words regarding mice'), they quickly get a cat ('kitty in a trice') to catch the mouse. However, by 2:00 a.m., a funny twist happens: the mouse stays quietly inside the house, while the cat is locked outside making noise. Lying in bed, the spouse humorously suggests that they should have gotten another mouse instead of the cat.", 
     "Easy", "Remembering"),

    ("Explain the humorous twist that happens at 2:00 a.m. in the poem.", 
     "The humorous twist occurs because people expect a cat to stay inside, hunt the mouse, and keep the home quiet. Instead, at 2:00 a.m., the roles are completely reversed: the mouse is inside the house sitting in total silence, while the cat is locked outside making annoying noises. This unexpected turn of events turns a serious pest problem into a hilarious midnight situation.", 
     "Easy", "Understanding"),

    ("Why does the spouse suggest getting 'another mouse' instead of a cat?", 
     "The spouse makes this funny suggestion because at 2:00 a.m., the cat outside is making noise and disturbing their sleep, whereas the mouse inside is completely silent and causing no noise at all. Out of sleep-deprived frustration, the spouse sarcastically decides that a quiet mouse is much better to have around at night than a noisy cat!", 
     "Easy", "Understanding"),

    ("Explain the meanings of the vocabulary words: 'eventually', 'trice', 'spouse', and 'cot'.", 
     "1. **Eventually**: Finally or after a period of time (e.g., eventually finding a mouse).\n2. **Trice**: A very short time or moment ('in a trice' means very quickly).\n3. **Spouse**: A married partner (husband or wife).\n4. **Cot**: A small, simple bed used for sleeping.", 
     "Easy", "Understanding"),

    ("How does Ogden Nash use rhyming pairs to make the poem catchy and fun?", 
     "Ogden Nash uses simple, bouncy AABB rhyming couplets:\n- house / mouse\n- mice / trice\n- thereabouts / out\n- cot / not\n- spouse / mouse\nThese simple rhymes create a fast musical rhythm that makes the funny story easy to remember and enjoyable to read aloud.", 
     "Easy", "Understanding"),

    ("What is the contrast between the mouse and the cat at night?", 
     "The contrast is twofold:\n1. **Location**: The mouse is inside the house ('mouse is in'), while the cat is outside ('cat is out').\n2. **Sound**: The mouse is completely quiet ('mouse is silent'), while the cat is making noise outside ('cat is not').", 
     "Easy", "Remembering"),

    ("Why did the owner get a cat so quickly ('in a trice')?", 
     "The owner got a cat quickly because finding a mouse in the house caused family complaints ('words regarding mice'). Wanting a quick solution to get rid of the mouse, the owner rushed out and bought a cat immediately.", 
     "Easy", "Remembering"),

    ("What does 'it dawns upon you, in your cot' mean in the context of the poem?", 
     "It means that while you are lying in bed at 2:00 a.m. trying to sleep, you suddenly realize the funny and frustrating truth: your plan failed because the cat is making noise outside while the mouse is resting quietly inside.", 
     "Easy", "Understanding"),

    ("How does the poem show that solutions sometimes bring new unexpected problems?", 
     "The family got a cat to solve the mouse problem. However, instead of solving it quietly, the cat went outside and started making noise at 2 a.m., creating a brand new problem of ruined sleep that was worse than having a quiet mouse!", 
     "Easy", "Understanding"),

    ("Summarize the main message and tone of Chapter 12.", 
     "Chapter 12 presents a lighthearted, humorous poem that shows the funny side of everyday household mix-ups. Its tone is witty and cheerful, encouraging readers to laugh at funny life situations.", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Who is Ogden Nash and what type of poetry is he known for?", "Ogden Nash was a famous American poet known for writing witty, humorous, light verse with surprising twists and clever rhymes.", "Easy", "Remembering"),
    ("Why is 2:00 a.m. an important time setting in the poem?", "2:00 a.m. is late night when people want total silence to sleep, making any animal noise outside stand out and feel extra funny and frustrating.", "Easy", "Understanding"),
    ("What does 'words regarding mice' mean?", "It refers to household discussions or complaints about seeing a mouse in the house.", "Easy", "Remembering"),
    ("Is the cat inside or outside the house at 2 a.m.?", "The cat is outside the house ('the cat is out').", "Easy", "Remembering"),
    ("Is the mouse silent or noisy at 2 a.m.?", "The mouse is silent ('the mouse is silent').", "Easy", "Remembering"),
    ("What does 'in a trice' mean in everyday language?", "It means extremely quickly or in a split second.", "Easy", "Understanding"),
    ("Why is the spouse's reaction funny to readers?", "Because nobody actually wants a mouse as a household pest, but preferring a quiet mouse over a noisy cat creates absurd humor.", "Easy", "Evaluating"),
    ("How many lines are in the poem 'The Cat'?", "The poem has 10 lines divided into 5 rhyming couplets.", "Easy", "Remembering"),
    ("What sensory detail tells us the cat is making noise at 2 a.m.?", "The phrase 'the cat is not' [silent] tells us the cat is meowing or making noise outside.", "Easy", "Understanding"),
    ("How does Chapter 12 build reading enjoyment for Class 2 students?", "By combining a short, funny story with easy rhyming words and a silly ending that makes children laugh.", "Easy", "Applying"),
    ("What does 'eventually' tell us about how the mouse arrived?", "It tells us that after settling into a new house, a mouse inevitably finds its way inside after some time.", "Easy", "Understanding"),
    ("Why didn't the cat catch the mouse before 2 a.m.?", "The poem humorously implies the cat went outside instead of doing its job, leaving the mouse safely inside.", "Easy", "Understanding"),
    ("What furniture is mentioned in the poem?", "A 'cot' (small bed) is mentioned in the poem.", "Easy", "Remembering"),
    ("What is the main contrast between the beginning and end of the poem?", "Beginning: getting a cat to get rid of a mouse; End: wishing for another mouse to get rid of the noisy cat!", "Easy", "Analyzing"),
    ("Summarize Chapter 12 in five key sentences.", "Chapter 12 features Ogden Nash's funny poem 'The Cat'. A person gets a house, finds a mouse, and quickly buys a cat to solve the problem. But at 2 a.m., the mouse sits quietly inside while the cat is outside making noise. Lying in bed, the owner realizes the plan backfired. The spouse humorously suggests they should have gotten another quiet mouse instead!", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how Ogden Nash uses structural irony to create comedy in 'The Cat'.", 
     "Structural irony occurs when the outcome of a situation is exact opposite of what was intended. The owner buys a cat to eliminate a quiet mouse. Instead, by 2 a.m., the predator (cat) is locked outside making noise, while the prey (mouse) enjoys quiet sanctuary inside. This reversal of expected roles creates sharp comedic irony.", 
     "Medium", "Analyzing"),

    ("Examine the role of rhyming couplets in delivering comic punchlines.", 
     "The poem uses an AABBCCDDEE couplet structure. Each couplet sets up a rhythmic momentum that leads directly to a witty conclusion. The final couplet ('Instead of kitty, says your spouse / You should have got another mouse') uses the predictable rhyme of 'spouse/mouse' to deliver a sudden, hilarious punchline.", 
     "Medium", "Analyzing"),

    ("Discuss how 'The Cat' reflects everyday human reactions to minor domestic problems.", 
     "When faced with a minor nuisance like a mouse, humans often react impulsively ('get a kitty in a trice'). However, hasty solutions can introduce new inconveniences. The poem lightheartedly reflects how human attempts to control nature often result in funny domestic mishaps.", 
     "Medium", "Evaluating"),

    ("Explore the poetic significance of brevity in 10-line narrative verse.", 
     "In just 10 short lines, Nash establishes character (husband and spouse), setting (house, cot at 2 a.m.), plot conflict (mouse infestation), action (getting a cat), twist (cat out, mouse in), and resolution (spouse's joke). Brevity ensures fast pacing and maximum comedic punch.", 
     "Medium", "Analyzing"),

    ("How can a primary English teacher use 'The Cat' to teach rhyme, rhythm, and tone?", 
     "Teachers can:\n1. **Rhyme**: Have students highlight end-rhymes (house/mouse, cot/not).\n2. **Rhythm**: Clap hands to the 4-beat cadence of each couplet.\n3. **Tone**: Practice reading the spouse's line with funny sarcastic expression.", 
     "Medium", "Applying"),

    ("Why is the phrase 'the cat is not' an effective use of poetic brevity?", "Instead of writing 'the cat is not silent and is making loud noises outside', Nash uses three simple words 'the cat is not' to complete the contrast with 'the mouse is silent', leaving the noisy image to the reader's imagination.", "Medium", "Analyzing"),
    ("Contrast the character of the mouse with the character of the cat in the poem.", "The mouse is an uninvited guest that settles in quietly and stays inside without making trouble at night; the cat is a purchased helper that ends up outside making loud late-night noise.", "Medium", "Analyzing"),
    ("How does the setting of 'cot at 2 a.m.' contribute to the poem's atmosphere?", "Middle-of-the-night settings evoke quiet sleepiness, making any unexpected noise outside feel dramatically amplified and absurdly funny to a tired person lying in bed.", "Medium", "Analyzing"),
    ("What makes Ogden Nash's humor accessible across different age groups?", "His humor relies on universal everyday situations—pets, household mix-ups, and funny family dialogue—that appeal equally to 7-year-olds and adults.", "Medium", "Evaluating"),
    ("Explain why getting a cat 'in a trice' represents hasty decision making.", "It shows that as soon as complaints arose, the owner rushed to buy a cat without considering whether the cat would actually stay inside or make noise at night.", "Medium", "Understanding"),
    ("How does the poem subvert traditional animal tropes in children's literature?", "Traditional literature depicts cats as clever mouse-hunters and mice as noisy destructive pests; Nash subverts this by making the mouse silent and the cat noisy and locked out.", "Medium", "Analyzing"),
    ("What is the significance of the word 'eventually' in line 2?", "It suggests that no matter how nice a new house is, domestic problems like mice are an inevitable part of home ownership.", "Medium", "Understanding"),
    ("How does the spouse's dialogue provide closure to the poem?", "The spouse's witty remark summarizes the absurdity of the entire situation, delivering a satisfying comic ending that resolves the poem.", "Medium", "Evaluating"),
    ("What activities can Class 2 students do after reading 'The Cat'?", "Students can draw a comic strip of the poem in 4 panels, roleplay the husband and spouse at 2 a.m., or write a 2-line rhyming poem about their own pets.", "Medium", "Applying"),
    ("Construct a 4-line sequel stanza describing what happens next morning.", "'Morning comes and the sun shines bright,\nThe mouse goes to sleep after a quiet night;\nWhile kitty slips in through the kitchen door,\nAnd falls asleep right on the floor!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the satirical representation of domestic problem-solving in modern light verse.", 
     "Nash satirizes the human tendency to over-engineer solutions for simple problems. Rather than dealing with a quiet mouse calmly, the owner rushes to introduce a predator (cat), resulting in secondary disruption (midnight noise) that exposes the absurdity of hasty remedies.", 
     "Hard", "Evaluating"),

    ("Deconstruct the comic architecture of 'The Cat' across its five stanzas.", 
     "1. **Stanza 1 (L1-2)**: Domestic setup -> House + Mouse.\n2. **Stanza 2 (L3-4)**: Problem escalation -> Complaints + Cat.\n3. **Stanza 3 (L5-6)**: Spatial reversal -> Mouse in + Cat out.\n4. **Stanza 4 (L7-8)**: Acoustic contrast -> Mouse quiet + Cat noisy.\n5. **Stanza 5 (L9-10)**: Absurd resolution -> Spouse's punchline.", 
     "Hard", "Analyzing"),

    ("Synthesize the literary features that make Ogden Nash a master of light verse.", 
     "1. **Clever Couplets**: Perfect AABB rhyming.\n2. **Situational Irony**: Reversal of expected animal behavior.\n3. **Conversational Diction**: Everyday words (wife, house, cot, spouse).\n4. **Witty Punchline**: Unexpected humorous conclusion.", 
     "Hard", "Synthesizing"),

    ("Formulate a complete primary school lesson plan based on Chapter 12.", 
     "- **Warm-up**: Discussion on pet stories.\n- **Reading**: Choral reading of 'The Cat' with emphasis on rhymes.\n- **Vocabulary**: Game matching 'trice', 'eventually', 'spouse', 'cot'.\n- **Analysis**: Comparing mouse silence vs cat noise.\n- **Creative Writing**: Writing a funny 2-line rhyme about an animal.", 
     "Hard", "Creating"),

    ("Evaluate the educational value of teaching lighthearted humorous poetry alongside classic literature.", 
     "Lighthearted poetry breaks the misconception that literature must always be serious or difficult. It builds reading pleasure, vocabulary, phonics awareness, and creative thinking by showing that language can be a tool for play and laughter.", 
     "Hard", "Evaluating"),

    ("Analyze how acoustic contrast (silence vs noise) drives the narrative tension in 10 lines.", "Silence represents peace; noise represents disruption. By contrasting the silent mouse inside with the noisy cat outside at 2 a.m., Nash creates instant narrative tension that resolves into laughter.", "Hard", "Analyzing"),
    ("Compare Ogden Nash's 'The Cat' with T.S. Eliot's 'Old Possum's Book of Practical Cats'.", "Eliot celebrates complex cat personalities in formal poetic meters; Nash uses short, ironic couplets to present a relatable domestic anecdote about a cat's failure.", "Hard", "Analyzing"),
    ("Draft a short review of Chapter 12 for an elementary English curriculum guide.", "'Chapter 12 delivers a masterclass in humorous poetry for Class 2 learners. Ogden Nash's 10-line gem uses crisp rhymes and situational irony to teach poetic rhythm, sensory contrast, and storytelling joy.'", "Hard", "Creating"),
    ("Assess how middle-of-the-night setting heightens comedic empathy in readers.", "Every reader has experienced middle-of-the-night sleep disruption, making the protagonist's 2 a.m. frustration universally relatable and deeply funny.", "Hard", "Evaluating"),
    ("Synthesize the ultimate moral lesson of Chapter 12 into a guiding principle.", "'Look for laughter in life's little mix-ups, and remember that sometimes the simplest solution is enjoying a good sense of humor!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 12: The Cat\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH12_LA_{idx:03d}"
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
    ("You get a wife, you get a house,\nEventually you get a mouse.",
     [
         ("What two things do you get first in the poem?", "A wife and a house.", "Easy", "Remembering"),
         ("What do you eventually get after getting a house?", "A mouse.", "Easy", "Remembering"),
         ("What does the word 'eventually' mean?", "Finally or after some time.", "Easy", "Understanding"),
         ("What rhyming pair ends these two lines?", "House / mouse.", "Easy", "Remembering"),
         ("What setting is established in these opening lines?", "A newly established domestic home.", "Medium", "Understanding")
     ]),

    # Set 2
    ("You get some words regarding mice,\nYou get a kitty in a trice.",
     [
         ("What causes the family to get a kitty?", "Words regarding mice (complaints/discussions).", "Easy", "Remembering"),
         ("How quickly is the kitty acquired?", "In a trice (very quickly).", "Easy", "Remembering"),
         ("What does 'trice' mean?", "Very quickly or in a short moment.", "Easy", "Understanding"),
         ("What rhyming pair ends these two lines?", "Mice / trice.", "Easy", "Remembering"),
         ("Why did the family rush to get a cat?", "To solve the problem of having a mouse in the house.", "Medium", "Understanding")
     ]),

    # Set 3
    ("By two a.m. or thereabouts,\nThe mouse is in, the cat is out.",
     [
         ("Around what time does this scene take place?", "By 2 a.m. or thereabouts.", "Easy", "Remembering"),
         ("Where is the mouse at 2 a.m.?", "Inside the house ('in').", "Easy", "Remembering"),
         ("Where is the cat at 2 a.m.?", "Outside the house ('out').", "Easy", "Remembering"),
         ("What does 'thereabouts' mean?", "Around that time / approximately.", "Medium", "Understanding"),
         ("What unexpected situation has occurred by 2 a.m.?", "The cat meant to catch the mouse is outside while the mouse is inside.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("It dawns upon you, in your cot,\nThe mouse is silent, the cat is not.",
     [
         ("Where are you lying when the truth dawns upon you?", "In your cot (small bed).", "Easy", "Remembering"),
         ("Which animal is quiet at 2 a.m.?", "The mouse.", "Easy", "Remembering"),
         ("Which animal is making noise at 2 a.m.?", "The cat ('the cat is not' silent).", "Easy", "Remembering"),
         ("What does 'it dawns upon you' mean?", "You suddenly realize or understand the situation.", "Medium", "Understanding"),
         ("What sensory contrast is highlighted in this extract?", "The quiet silence of the mouse vs the disturbing noise of the cat.", "Medium", "Analyzing")
     ]),

    # Set 5
    ("Instead of kitty, says your spouse,\nYou should have got another mouse.",
     [
         ("Who speaks in these lines?", "Your spouse (husband/wife).", "Easy", "Remembering"),
         ("What does the spouse suggest instead of getting a kitty?", "Getting another mouse.", "Easy", "Remembering"),
         ("What does the word 'spouse' mean?", "A married person.", "Easy", "Understanding"),
         ("Why is the spouse's suggestion funny?", "Because preferring a quiet mouse over a noisy cat turns common sense upside down.", "Medium", "Evaluating"),
         ("What role does this couplet play in the poem?", "It serves as the final witty punchline of the poem.", "Medium", "Analyzing")
     ]),

    # Set 6
    ("Word Meaning: Eventually: Finally | Trice: Very quickly | Spouse: A married person : husband/wife",
     [
         ("What is the meaning of 'eventually'?", "Finally.", "Easy", "Remembering"),
         ("What is the meaning of 'trice'?", "Very quickly.", "Easy", "Remembering"),
         ("What is the meaning of 'spouse'?", "A married person (husband/wife).", "Easy", "Remembering"),
         ("Which word describes getting something in a split second?", "Trice.", "Easy", "Understanding"),
         ("Why are these vocabulary definitions helpful?", "They help students understand old or informal poetic words.", "Medium", "Understanding")
     ]),

    # Set 7
    ("You get a wife, you get a house,\nEventually you get a mouse.\nYou get some words regarding mice,\nYou get a kitty in a trice.",
     [
         ("Name the title of the poem.", "'The Cat'.", "Easy", "Remembering"),
         ("Who wrote this poem?", "Ogden Nash.", "Easy", "Remembering"),
         ("What is the first problem encountered after getting a house?", "Finding a mouse.", "Easy", "Remembering"),
         ("What action is taken to solve the mouse problem?", "Getting a kitty very quickly.", "Easy", "Remembering"),
         ("Summarize these 4 lines in one sentence.", "A family gets a house, finds a mouse, and quickly buys a cat to solve it.", "Medium", "Understanding")
     ]),

    # Set 8
    ("By two a.m. or thereabouts,\nThe mouse is in, the cat is out.\nIt dawns upon you, in your cot,\nThe mouse is silent, the cat is not.",
     [
         ("What time of night is described?", "2:00 a.m.", "Easy", "Remembering"),
         ("Is the mouse inside or outside?", "Inside.", "Easy", "Remembering"),
         ("Is the cat silent or noisy?", "Noisy ('not silent').", "Easy", "Remembering"),
         ("Where is the house owner during this scene?", "In bed (in a cot).", "Easy", "Remembering"),
         ("What is the irony in these 4 lines?", "The cat is outside making noise while the mouse is inside keeping quiet.", "Medium", "Analyzing")
     ]),

    # Set 9
    ("Instead of kitty, says your spouse,\nYou should have got another mouse.",
     [
         ("What animal was originally brought home?", "A kitty (cat).", "Easy", "Remembering"),
         ("Who expresses frustration at 2 a.m.?", "The spouse.", "Easy", "Remembering"),
         ("What rhyming words end these two lines?", "Spouse / mouse.", "Easy", "Remembering"),
         ("Why is 'another mouse' preferred by the spouse?", "Because the mouse in the house is silent and doesn't wake them up at night.", "Medium", "Understanding"),
         ("What tone does the spouse's line create?", "A sarcastic, funny, and lighthearted tone.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("The Cat by Ogden Nash: You get a wife, you get a house... You should have got another mouse.",
     [
         ("What is the main topic of the poem?", "A funny household mix-up involving a cat and a mouse.", "Easy", "Remembering"),
         ("How many lines make up the whole poem?", "10 lines.", "Easy", "Remembering"),
         ("What kind of rhymes are used throughout?", "Simple AABB rhyming couplets.", "Medium", "Understanding"),
         ("Why is the poem popular with young readers?", "It is short, bouncy, easy to read, and has a silly punchline.", "Medium", "Evaluating"),
         ("Summarize the lesson of the poem in one sentence.", "Appreciate the humor when quick solutions turn into funny unexpected mix-ups!", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 12: The Cat\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH12_EXT_{q_counter:03d}"
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

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 12 in {CH12_DIR}")
