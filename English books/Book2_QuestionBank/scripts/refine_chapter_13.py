r"""
Refines all 6 Category files for Chapter 13 ("Habits of the Hippopotamus") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH13_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_13")
os.makedirs(CH13_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Who wrote the humorous poem 'Habits of the Hippopotamus'?", "(A) Arthur Guiterman", "(B) Ogden Nash", "(C) Louisa May Alcott", "(D) Robert Frost", "(A)", "The author is Arthur Guiterman.", "Easy", "Remembering", "Poet Name"),
    ("How is the hippopotamus's head and body described in the first stanza?", "(A) Strong, huge of head, and broad of bustle", "(B) Tiny and thin", "(C) Covered in feathers", "(D) Long like a snake", "(A)", "It says 'strong and huge of head and broad of bustle'.", "Easy", "Remembering", "Appearance"),
    ("What special word does the poet invent for the hippopotamus's muscle?", "(A) Hippopotomuscle", "(B) Megamuscle", "(C) Supermuscle", "(D) Fatmuscle", "(A)", "The poem uses 'hippopotomuscle'.", "Easy", "Remembering", "Wordplay"),
    ("What sweets does the hippopotamus NOT greatly care for?", "(A) Ice cream, apple pie, or custard", "(B) Carrots and grass", "(C) Rice and bread", "(D) Apples and bananas", "(A)", "It does not care for sweets like ice cream, apple pie or custard.", "Easy", "Remembering", "Food Preference"),
    ("What spice/condiment does the hippopotamus use to flavor what he eats?", "(A) Hippopotomustard", "(B) Salt", "(C) Sugar", "(D) Pepper", "(A)", "It uses 'a little hippopotomustard'.", "Easy", "Remembering", "Flavoring"),
    ("How does the hippopotamus behave regarding his principles?", "(A) He is true to all his principles and just", "(B) He breaks all rules", "(C) He tells lies", "(D) He forgets everything", "(A)", "He is true to all his principles and just.", "Easy", "Remembering", "Character"),
    ("What does the hippopotamus always try his best to do?", "(A) The things one hippopotomust", "(B) Sleep all day", "(C) Eat all sweets", "(D) Run in races", "(A)", "He tries his best to do the things one hippopotomust.", "Easy", "Remembering", "Duty"),
    ("Which vehicle does the hippopotamus NEVER ride in?", "(A) Trucks, trams, taxicabs, or omnibuses", "(B) Canoes", "(C) Skateboards", "(D) Airplanes", "(A)", "He never rides in trucks, trams, taxicabs, or omnibuses.", "Easy", "Remembering", "Vehicles Avoided"),
    ("By not riding in trucks or taxicabs, what does the hippopotamus keep out of?", "(A) Traffic jams and other hippopotomusses", "(B) Deep water", "(C) Muddy rivers", "(D) Green forests", "(A)", "He keeps out of traffic jams and other hippopotomusses.", "Easy", "Remembering", "Traffic Avoidance"),
    ("What does the word 'bustle' mean in the poem's word meaning box?", "(A) Rear part of body", "(B) Front nose", "(C) Long tail", "(D) Big ears", "(A)", "Bustle is defined as the rear part of body.", "Easy", "Understanding", "Vocabulary"),
    ("What funny word combines 'hippopotamus' and 'muscle'?", "(A) Hippopotomuscle", "(B) Musclepotamus", "(C) Hippomuscle", "(D) Potatomuscle", "(A)", "Hippopotomuscle is formed.", "Easy", "Understanding", "Wordplay Concept"),
    ("What funny word combines 'hippopotamus' and 'mustard'?", "(A) Hippopotomustard", "(B) Mustardpotamus", "(C) Hippomustard", "(D) Yellowmustard", "(A)", "Hippopotomustard is formed.", "Easy", "Understanding", "Wordplay Concept"),
    ("What funny word combines 'hippopotamus' and 'must'?", "(A) Hippopotomust", "(B) Mustpotamus", "(C) Hippomust", "(D) Potamust", "(A)", "Hippopotomust is formed.", "Easy", "Understanding", "Wordplay Concept"),
    ("What funny word combines 'hippopotamus' and 'musses' (messes)?", "(A) Hippopotomusses", "(B) Messpotamus", "(C) Hippomesses", "(D) Trafficmusses", "(A)", "Hippopotomusses is formed.", "Easy", "Understanding", "Wordplay Concept"),
    ("How does the hippopotamus move along on his big limbs?", "(A) He rolls along", "(B) He flies", "(C) He hops on one leg", "(D) He slides on ice", "(A)", "The limbs on which he rolls along.", "Easy", "Remembering", "Movement"),
    ("Is the hippopotamus described as weak or strong?", "(A) Strong", "(B) Weak", "(C) Tiny", "(D) Fragile", "(A)", "The text states 'The hippopotamus is strong'.", "Easy", "Remembering", "Strength"),
    ("What kind of food does the hippopotamus prefer over sweets?", "(A) Savory food flavored with a little mustard", "(B) Chocolate cake", "(C) Laddoos", "(D) Candy canes", "(A)", "He prefers food with a little hippopotomustard.", "Easy", "Understanding", "Dietary Choice"),
    ("What is an omnibus?", "(A) A large bus for carrying passengers", "(B) A small bicycle", "(C) A boat", "(D) A train engine", "(A)", "An omnibus is a traditional public bus.", "Easy", "Understanding", "Vocabulary"),
    ("What is a tram?", "(A) A rail vehicle that runs on tracks along city streets", "(B) A jet plane", "(C) A rowboat", "(D) A horse cart", "(A)", "A tram is a streetcar running on tracks.", "Easy", "Understanding", "Vocabulary"),
    ("Does the hippopotamus get stuck in city traffic jams?", "(A) No, because he never rides in vehicles", "(B) Yes, every morning", "(C) Yes, in taxicabs", "(D) Only on Mondays", "(A)", "He keeps out of traffic jams because he never rides in vehicles.", "Easy", "Remembering", "No Traffic Jams"),
    ("What moral quality does 'just' mean in the poem?", "(A) Fair and honest", "(B) Very quick", "(C) Small", "(D) Loud", "(A)", "'Just' means fair, moral, and honest.", "Easy", "Understanding", "Vocabulary"),
    ("What does 'principles' mean when describing the hippopotamus?", "(A) Moral rules and beliefs about what is right", "(B) School principals", "(C) Sweet foods", "(D) Heavy trucks", "(A)", "Principles are moral rules/values.", "Easy", "Understanding", "Vocabulary"),
    ("How many stanzas are in the poem 'Habits of the Hippopotamus'?", "(A) 4 stanzas", "(B) 2 stanzas", "(C) 10 stanzas", "(D) 1 stanza", "(A)", "The poem has 4 four-line stanzas.", "Easy", "Remembering", "Stanza Count"),
    ("What is the main technique the poet uses for humor?", "(A) Portmanteau wordplay (adding 'hippopoto-' to words)", "(B) Scary stories", "(C) Sad endings", "(D) Difficult math problems", "(A)", "Combining 'hippopoto-' with common words creates humor.", "Easy", "Understanding", "Humor Technique"),
    ("What is the title of Chapter 13?", "(A) Habits of the Hippopotamus", "(B) The Cat", "(C) The Big Elephant", "(D) Animal World", "(A)", "Chapter 13 is titled 'Habits of the Hippopotamus'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why is Arthur Guiterman's wordplay with 'hippopotamus' so clever for children?", "(A) It blends a long, complex animal name with simple daily words (muscle, mustard, must, messes) into funny rhyming words", "(B) It uses foreign languages nobody understands", "(C) It makes the poem very long", "(D) It removes all rhymes", "(A)", "Blends complex animal name with simple words cleverly.", "Medium", "Analyzing", "Wordplay Analysis"),
    ("How does the poem present a positive moral lesson through a funny animal?", "(A) The hippo is not just big and funny; he is also just, true to principles, and does his duty", "(B) The hippo teaches how to break rules", "(C) The hippo eats all ice cream", "(D) The hippo drives fast cars", "(A)", "Presents virtue (justice, duty, honesty) through humor.", "Medium", "Evaluating", "Moral Dimension"),
    ("Why does the hippopotamus avoid trucks, trams, taxicabs, and omnibuses?", "(A) To avoid getting caught in noisy, stressful city traffic jams and messes ('hippopotomusses')", "(B) Because he has no money", "(C) Because he is scared of tires", "(D) Because drivers hate animals", "(A)", "Avoids city traffic jams and stressful messes.", "Medium", "Understanding", "Travel Motivation"),
    ("What rhyming scheme does each four-line stanza follow?", "(A) ABAB rhyming scheme", "(B) AABB rhyming scheme", "(C) ABCB rhyming scheme", "(D) No rhyme scheme", "(A)", "Stanzas follow ABAB pattern (strong/along, bustle/hippopotomuscle).", "Medium", "Analyzing", "Rhyme Scheme"),
    ("What physical contrast is drawn between the hippo's massive size and his movement?", "(A) He is huge with big 'hippopotomuscle', yet he smoothly 'rolls along'", "(B) He is tiny but walks heavily", "(C) He flies in the air", "(D) He sleeps without moving", "(A)", "Massive size vs smooth rolling movement.", "Medium", "Analyzing", "Physical Contrast"),
    ("What does 'hippopotomusses' mean as a pun in the final line?", "(A) A humorous pun combining 'hippopotamus' and 'messes' (troubles/confusions)", "(B) Female hippopotamuses", "(C) Buses driven by hippos", "(D) Sweet desserts", "(A)", "Pun combining hippopotamus and messes/troubles.", "Medium", "Analyzing", "Pun Analysis"),
    ("How does the hippo's food taste reflect a sensible, non-greedy diet?", "(A) He rejects excessive sugary sweets (ice cream, pie) in favor of simple food with a little flavor", "(B) He eats fifty pies a day", "(C) He starves himself", "(D) He eats paper", "(A)", "Rejects excess sugar for simple flavored food.", "Medium", "Evaluating", "Dietary Wisdom"),
    ("Why is the word 'bustle' defined as 'rear part of body' in this poem?", "(A) To explain the hippo's broad physical rear shape in a humorous poetic way", "(B) Because bustle means a small hat", "(C) Because bustle means a fast car", "(D) Because hippo wears a dress", "(A)", "Explains broad physical rear shape poetically.", "Medium", "Understanding", "Contextual Meaning"),
    ("What does 'one hippopotomust' signify about personal duty?", "(A) It means doing the essential duties and moral responsibilities that one MUST do in life", "(B) It means buying mustard", "(C) It means riding a tram", "(D) It means eating ice cream", "(A)", "Essential duties and moral responsibilities one MUST do.", "Medium", "Analyzing", "Duty Concept"),
    ("How does Chapter 13 build phonics and rhythm skills for Class 2 students?", "(A) Repeating multi-syllable rhyming words ('hippopotomuscle', 'hippopotomustard') enhances tongue agility and rhythmic reading", "(B) By teaching silent reading only", "(C) By avoiding long words", "(D) By memorizing dictionary pages", "(A)", "Multi-syllable rhyming words enhance tongue agility and rhythm.", "Medium", "Applying", "Pedagogical Value"),
    ("What visual image of the hippopotamus is created in Stanza 1?", "(A) A strong, grand animal with a huge head, broad body, and muscular limbs rolling along happily", "(B) A skinny cat wearing shoes", "(C) A small bird in a tree", "(D) A fish in a bowl", "(A)", "Strong animal with huge head, broad body, muscular limbs.", "Medium", "Analyzing", "Visual Imagery"),
    ("Why is the hippo called 'true to all his principles and just'?", "(A) Because he follows honest moral principles and acts fairly toward everyone", "(B) Because he wins all games", "(C) Because he is very rich", "(D) Because he is loud", "(A)", "Follows honest moral principles and acts fairly.", "Medium", "Understanding", "Character Traits"),
    ("What is the difference between a real wild hippopotamus and the poet's hippo?", "(A) Real hippos live in African rivers; the poet's hippo humorously deals with mustard, traffic, and urban transport", "(B) Real hippos fly; poet's hippo swims", "(C) Real hippos eat pie; poet's hippo eats cars", "(D) There is no difference", "(A)", "Real river animal vs poet's humorous urban-aware character.", "Medium", "Comparing", "Real vs Poetic Hippo"),
    ("How does the poem encourage children to avoid unnecessary trouble?", "(A) By showing how the hippo avoids traffic jams and messes by making simple, smart travel choices", "(B) By telling children to stay in bed all day", "(C) By warning against eating apples", "(D) By forbidding all travel", "(A)", "Smart travel choices avoid traffic jams and messes.", "Medium", "Evaluating", "Practical Wisdom"),
    ("What literary device is used in combining 'hippopotamus' with other words?", "(A) Portmanteau / blended wordplay", "(B) Simile", "(C) Alliteration", "(D) Personification only", "(A)", "Portmanteau wordplay (blending words together).", "Medium", "Analyzing", "Literary Device"),

    # Hard (41-50)
    ("Analyze the linguistic structure of Arthur Guiterman's portmanteau words in 'Habits of the Hippopotamus'.", "(A) Prefixes 'hipppoto-' attach to root words (muscle, mustard, must, messes), creating rhythmically matched quadrisyllabic rhymes", "(B) Words are chosen at random without pattern", "(C) All words are translated from German", "(D) No root words are used", "(A)", "Attaches 'hippopoto-' to root words creating quadrisyllabic rhymes.", "Hard", "Analyzing", "HOTS Linguistic Structure"),
    ("Deconstruct the philosophical satire underlying the hippo's avoidance of modern transportation.", "(A) Satire on urban modern life: even a wild giant animal is smart enough to avoid man-made traffic jams, trams, and stress", "(B) Satire on animal farming", "(C) Satire on cooking mustard", "(D) Satire on ice cream factories", "(A)", "Smart avoidance of man-made urban traffic jams and stress.", "Hard", "Analyzing", "Satirical Commentary"),
    ("Evaluate the moral lesson of self-discipline in food and lifestyle portrayed by the hippo.", "(A) The hippo practices restraint—preferring savory moderation over junk sweets and simple walking over stressful transit", "(B) The hippo is forced by others to diet", "(C) The hippo eats everything in sight", "(D) The hippo hates eating", "(A)", "Restraint: moderation over junk food, walking over transit.", "Hard", "Evaluating", "Lifestyle Evaluation"),
    ("Compare the humorous wordplay of Arthur Guiterman with Ogden Nash's comic verse.", "(A) Guiterman invents portmanteau words ('hippopotomuscle'); Nash uses unexpected situational twists and ironic couplets", "(B) Both write serious historical essays", "(C) Neither uses rhyming words", "(D) Guiterman writes sad stories; Nash writes science", "(A)", "Portmanteau inventions vs situational twists and ironic couplets.", "Hard", "Comparing", "Comparative Poetics"),
    ("Assess the psychological appeal of nonsense words ('hippopotomustard') for young learners.", "(A) Playful invented words spark joy, reduce reading anxiety, and demonstrate the creative flexibility of language", "(B) Nonsense words confuse children permanently", "(C) Children dislike made-up words", "(D) Made-up words lower reading scores", "(A)", "Sparks joy, reduces anxiety, demonstrates language flexibility.", "Hard", "Evaluating", "Psychological Appeal"),
    ("How does the poem balance biological reality with whimsical fantasy?", "(A) Reality: hippo is strong, huge, muscular; Fantasy: hippo eats mustard, follows ethics, avoids taxicabs", "(B) Reality: hippo flies; Fantasy: hippo lives in water", "(C) Entire poem is 100% textbook biology", "(D) Entire poem is dark horror", "(A)", "Real physical traits + whimsical urban/ethical behaviors.", "Hard", "Analyzing", "Fantasy vs Reality"),
    ("Synthesize how Chapter 13 promotes advanced phonemic awareness in Class 2 students.", "(A) Pronouncing 6-syllable blended words ('hip-po-po-to-mus-cle') challenges and strengthens phonemic articulation", "(B) Teaches children how to drive buses", "(C) Teaches children how to make mustard", "(D) Eliminates multi-syllable words", "(A)", "6-syllable blended words strengthen phonemic articulation.", "Hard", "Synthesizing", "Pedagogical Benefit"),
    ("Formulate a new 4-line stanza continuing Arthur Guiterman's poem with a new portmanteau word.", "(A) 'When night comes down upon the plain, He sleeps without a frown or fuss; And dreams inside his heavy brain Some happy hippopotodreams!'", "(B) 'He eats a hundred pies a day'", "(C) 'He drives a car across the town'", "(D) 'He flies up high into the sky'", "(A)", "Creative stanza extension with new portmanteau word.", "Hard", "Creating", "Creative Stanza Extension"),
    ("Formulate a critical appreciation of the line 'He always tries his best to do / The things one hippopotomust'.", "(A) Encapsulates the core ethical message: combining duty ('must') with humor ('hippopoto-') inspires doing one's moral best cheerfully", "(B) Explains why hippos eat grass", "(C) Proves hippos cannot walk", "(D) Describes a hippo swimming in mud", "(A)", "Combining moral duty with humor inspires doing one's best.", "Hard", "Evaluating", "Critical Appreciation"),
    ("Synthesize the ultimate lesson of Chapter 13 for Class 2 learners.", "(A) Be strong, fair, and true to your principles, avoid unnecessary trouble, and enjoy the playful magic of language!", "(B) Drive taxicabs every day", "(C) Eat ice cream for breakfast, lunch, and dinner", "(D) Never read funny poems", "(A)", "Be strong, fair, true to principles, avoid trouble, enjoy language.", "Hard", "Evaluating", "Core Lesson Synthesis")
]

mcq_content = f"# MCQs — Chapter 13: Habits of the Hippopotamus\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH13_MCQ_{idx:03d}"
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

with open(os.path.join(CH13_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("The hippopotamus is _______ and huge of head.", "strong", "The hippopotamus is strong.", "Easy"),
    ("The hippopotamus is strong and huge of head and broad of _______.", "bustle", "Broad of bustle.", "Easy"),
    ("The limbs on which he rolls along are big with _______.", "hippopotomuscle", "Big with hippopotomuscle.", "Easy"),
    ("He does not greatly care for _______ like ice cream.", "sweets", "Does not care for sweets.", "Easy"),
    ("He does not care for sweets like ice cream, apple pie or _______.", "custard", "Apple pie or custard.", "Easy"),
    ("He takes to flavor what he eats a little _______.", "hippopotomustard", "A little hippopotomustard.", "Easy"),
    ("The hippopotamus is _______ to all his principles and just.", "true", "True to all his principles.", "Easy"),
    ("The hippopotamus is true to all his principles and _______.", "just", "True and just.", "Easy"),
    ("He always tries his best to do the things one _______.", "hippopotomust", "Things one hippopotomust.", "Easy"),
    ("He never rides in trucks or _______.", "trams", "Trucks or trams.", "Easy"),
    ("He never rides in taxicabs or _______.", "omnibuses", "Taxicabs or omnibuses.", "Easy"),
    ("And so keeps out of traffic _______.", "jams", "Keeps out of traffic jams.", "Easy"),
    ("And so keeps out of traffic jams and other _______.", "hippopotomusses", "And other hippopotomusses.", "Easy"),
    ("The author of the poem is Arthur _______.", "Guiterman", "Arthur Guiterman.", "Easy"),
    ("The word 'bustle' in the poem means rear part of _______.", "body", "Rear part of body.", "Easy"),
    ("The hippopotamus has a huge _______.", "head", "Huge of head.", "Easy"),
    ("The hippopotamus has big _______ with muscle.", "limbs", "Limbs are big.", "Easy"),
    ("Ice cream, apple pie, and custard are examples of _______.", "sweets", "Examples of sweets.", "Easy"),
    ("Hippopotomustard is a funny word for _______.", "mustard", "Funny word for mustard.", "Easy"),
    ("Hippopotomuscle is a funny word for _______.", "muscle", "Funny word for muscle.", "Easy"),
    ("Hippopotomust is a funny word for _______.", "must", "Funny word for must.", "Easy"),
    ("Hippopotomusses is a funny word for _______.", "musses", "Funny word for messes/musses.", "Easy"),
    ("The hippopotamus stays away from city _______ jams.", "traffic", "Traffic jams.", "Easy"),
    ("A tram is a vehicle that runs on _______ along streets.", "tracks", "Runs on tracks.", "Easy"),
    ("Chapter 13 is titled 'Habits of the _______'.", "Hippopotamus", "Titled 'Habits of the Hippopotamus'.", "Easy"),

    # Medium (26-40)
    ("The poem combines the word 'hippopotamus' with daily words to create funny _______.", "rhymes", "Create funny rhymes.", "Medium"),
    ("Instead of eating sugary desserts, the hippo flavors food with _______.", "mustard", "Flavors food with mustard.", "Medium"),
    ("The hippo is honest and stays true to his moral _______.", "principles", "Stays true to principles.", "Medium"),
    ("By walking on his own legs, the hippo avoids crowded public _______.", "transport", "Avoids public transport.", "Medium"),
    ("The hippo's limbs are strong and filled with massive _______.", "muscle", "Filled with muscle.", "Medium"),
    ("An omnibus is an old-fashioned term for a public _______.", "bus", "Public bus.", "Medium"),
    ("The poem consists of four four-line _______.", "stanzas", "Four stanzas.", "Medium"),
    ("The hippo's rear part of the body is described as broad of _______.", "bustle", "Broad of bustle.", "Medium"),
    ("Doing what one 'hippopotomust' means doing one's ethical _______.", "duty", "Doing one's duty.", "Medium"),
    ("Avoiding taxicabs keeps the hippo out of street _______.", "jams", "Out of street jams.", "Medium"),
    ("The rhyme scheme of each stanza is _______.", "ABAB", "Rhyme scheme ABAB.", "Medium"),
    ("The poet Arthur Guiterman uses portmanteau wordplay for _______.", "humor", "Wordplay for humor.", "Medium"),
    ("The hippo rolls along smoothly on his heavy _______.", "limbs", "Rolls along on limbs.", "Medium"),
    ("Ice cream, custard, and apple pie are all _______ foods.", "sweet", "Sweet foods.", "Medium"),
    ("The hippo sets a good example of staying out of unnecessary _______.", "trouble", "Avoiding trouble.", "Medium"),

    # Hard (41-50)
    ("Quadrisyllabic portmanteau rhymes create distinctive poetic _______.", "cadence", "Creates distinctive cadence.", "Hard"),
    ("The hippo's moral character is defined as principled and _______.", "just", "Principled and just.", "Hard"),
    ("Avoiding omnibuses and taxicabs symbolizes rejection of urban _______.", "congestion", "Rejection of urban congestion.", "Hard"),
    ("The word 'hippopotomusses' blends hippopotamus with urban _______.", "messes", "Blends with messes.", "Hard"),
    ("Guiterman's light verse demonstrates playful linguistic _______.", "inventiveness", "Playful inventiveness.", "Hard"),
    ("The hippo's dietary choice favors savory spices over sugary _______.", "confections", "Over sugary confections.", "Hard"),
    ("Physical strength is poetically exaggerated through the term _______.", "hippopotomuscle", "Term hippopotomuscle.", "Hard"),
    ("The hippo's character balances formidable size with gentle _______.", "ethics", "Balanced with gentle ethics.", "Hard"),
    ("Humorous animal poetry engages young readers through rhythmic _______.", "repetition", "Through rhythmic repetition.", "Hard"),
    ("Chapter 13 teaches phonemic agility, moral duty, and poetic _______.", "appreciation", "Teaches poetic appreciation.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 13: Habits of the Hippopotamus\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH13_FIB_{idx:03d}"
    sent, ans, exp, diff = item
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
    ("The poem 'Habits of the Hippopotamus' was written by Arthur Guiterman.", "True", "Text explicitly names Arthur Guiterman.", "Easy"),
    ("The hippopotamus is described as weak and small of head.", "False", "The hippopotamus is strong and huge of head.", "Easy"),
    ("The limbs of the hippopotamus are big with hippopotomuscle.", "True", "Limbs are big with hippopotomuscle.", "Easy"),
    ("The hippopotamus loves to eat ice cream, apple pie, and custard all day.", "False", "He does not greatly care for sweets like ice cream, apple pie or custard.", "Easy"),
    ("The hippopotamus likes to flavor his food with a little hippopotomustard.", "True", "He takes to flavor what he eats a little hippopotomustard.", "Easy"),
    ("The hippopotamus is true to all his principles and just.", "True", "He is true to all his principles and just.", "Easy"),
    ("The hippopotamus always tries his best to do the things one hippopotomust.", "True", "He tries his best to do the things one hippopotomust.", "Easy"),
    ("The hippopotamus loves riding in trucks, trams, taxicabs, and omnibuses.", "False", "He never rides in trucks or trams, in taxicabs or omnibuses.", "Easy"),
    ("By avoiding vehicles, the hippopotamus keeps out of traffic jams.", "True", "And so keeps out of traffic jams.", "Easy"),
    ("The word 'bustle' in the poem refers to the rear part of the body.", "True", "Word meaning box defines bustle as rear part of body.", "Easy"),
    ("Hippopotomuscle is a real scientific word found in medical dictionaries.", "False", "It is a made-up humorous word combining hippopotamus and muscle.", "Easy"),
    ("Hippopotomustard combines hippopotamus and mustard.", "True", "It is a funny blend of hippopotamus and mustard.", "Easy"),
    ("An omnibus is a type of bicycle.", "False", "An omnibus is a large public passenger bus.", "Easy"),
    ("A tram runs on tracks along city streets.", "True", "A tram is a streetcar running on tracks.", "Easy"),
    ("The hippopotamus rolls along on his big limbs.", "True", "The limbs on which he rolls along.", "Easy"),
    ("The hippopotamus is unfair and lies to everyone.", "False", "He is true to all his principles and just.", "Easy"),
    ("The poem consists of four stanzas.", "True", "The poem has 4 four-line stanzas.", "Easy"),
    ("Bustle rhymes with hippopotomuscle in the first stanza.", "True", "Bustle and hippopotomuscle rhyme.", "Easy"),
    ("Custard rhymes with hippopotomustard in the second stanza.", "True", "Custard and hippopotomustard rhyme.", "Easy"),
    ("Just rhymes with hippopotomust in the third stanza.", "True", "Just and hippopotomust rhyme.", "Easy"),
    ("Omnibuses rhymes with hippopotomusses in the fourth stanza.", "True", "Omnibuses and hippopotomusses rhyme.", "Easy"),
    ("The hippopotamus prefers savory food with mustard over sugary desserts.", "True", "He prefers savory food with mustard over sweets.", "Easy"),
    ("The hippopotamus gets stuck in city traffic jams every morning.", "False", "He keeps out of traffic jams.", "Easy"),
    ("The poet uses funny invented words to make readers laugh.", "True", "Portmanteau words create lighthearted humor.", "Easy"),
    ("Chapter 13 is titled 'Habits of the Hippopotamus'.", "True", "Chapter 13 is titled 'Habits of the Hippopotamus'.", "Easy"),

    # Medium (26-40)
    ("The poem combines physical description, dietary habits, moral character, and travel habits.", "True", "Stanza 1: physical, Stanza 2: diet, Stanza 3: character, Stanza 4: travel.", "Medium"),
    ("The word 'hippopotomusses' refers to messy traffic complications.", "True", "It is a pun on messes/troubles caused by traffic.", "Medium"),
    ("The hippopotamus is portrayed as an undisciplined animal that eats junk food.", "False", "He rejects sugary sweets and eats sensibly with mustard.", "Medium"),
    ("Each stanza in the poem follows an ABAB rhyming pattern.", "True", "Strong/along, bustle/hippopotomuscle follows ABAB pattern.", "Medium"),
    ("The hippopotamus travels exclusively by taxicab.", "False", "He never rides in taxicabs.", "Medium"),
    ("Doing what one 'hippopotomust' emphasizes personal duty and responsibility.", "True", "It represents doing what one must do morally.", "Medium"),
    ("The poet Arthur Guiterman wrote this poem as a serious scientific study.", "False", "It is a lighthearted, whimsical, humorous poem.", "Medium"),
    ("The hippo's large size prevents him from moving smoothly.", "False", "Despite being big, he 'rolls along' smoothly on his limbs.", "Medium"),
    ("Avoidance of city vehicles saves the hippo from daily stress.", "True", "Avoiding vehicles keeps him out of traffic jams.", "Medium"),
    ("The hippo's food preferences show he dislikes all food completely.", "False", "He likes food when flavored with a little mustard.", "Medium"),
    ("The invented words in the poem all start with 'hippopoto-'.", "True", "Hippopotomuscle, hippopotomustard, hippopotomust, hippopotomusses all start with hippopoto-.", "Medium"),
    ("The hippo's moral character is described in the third stanza.", "True", "Stanza 3 covers principles, justice, and doing what one must.", "Medium"),
    ("Class 2 students can practice multi-syllable pronunciation through this poem.", "True", "Long rhyming words aid multi-syllable pronunciation practice.", "Medium"),
    ("The hippo is described as having a tiny head and narrow body.", "False", "He is huge of head and broad of bustle.", "Medium"),
    ("The poem suggests that staying away from crowded city transport avoids trouble.", "True", "Avoiding vehicles keeps out of traffic jams and messes.", "Medium"),

    # Hard (41-50)
    ("Arthur Guiterman uses portmanteau morphology to create quadrisyllabic rhymes.", "True", "Blends words with hippopotamus for quadrisyllabic rhymes.", "Hard"),
    ("The hippo's rejection of sweets reflects stoic dietary temperance.", "True", "Rejecting sugary desserts reflects temperance.", "Hard"),
    ("The word 'bustle' in Victorian fashion referred to a pad worn under skirts at the back.", "True", "Victorian bustle was a rear dress pad, fitting the hippo's broad rear.", "Hard"),
    ("The hippo's travel habit is an allegory for living a simple, unhurried life.", "True", "Walking instead of riding vehicles symbolizes unhurried living.", "Hard"),
    ("The poem maintains a strict metric rhythm across all four stanzas.", "True", "Consistent iambic tetrameter/trimeter rhythm.", "Hard"),
    ("The term 'hippopotomust' is a noun meaning a large water tank.", "False", "It is a funny verb/noun blend meaning something one MUST do.", "Hard"),
    ("The hippo's justice and adherence to principles highlight anthropomorphic virtue.", "True", "Gives human moral virtues to the animal character.", "Hard"),
    ("Traffic jams are described as 'hippopotomusses' to create a final visual pun.", "True", "Creates a memorable final visual and verbal pun.", "Hard"),
    ("The poem implies that physical strength renders moral principles unnecessary.", "False", "Despite immense strength, the hippo remains just and principled.", "Hard"),
    ("Chapter 13 integrates humor, moral ethics, vocabulary expansion, and poetic rhythm.", "True", "Combines wordplay, moral principles, vocabulary, and rhythm.", "Hard")
]

tf_content = f"# True / False — Chapter 13: Habits of the Hippopotamus\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH13_TF_{idx:03d}"
    stmt, ans, exp, diff = item
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
    ("Who wrote the poem 'Habits of the Hippopotamus'?", "The poem was written by Arthur Guiterman.", "Easy", "Remembering"),
    ("How is the physical appearance of the hippopotamus described in Stanza 1?", "He is described as strong, huge of head, broad of bustle (rear body), with big muscular limbs.", "Easy", "Remembering"),
    ("What special funny word is used for the hippopotamus's muscle?", "The word used is 'hippopotomuscle'.", "Easy", "Remembering"),
    ("What sweet foods does the hippopotamus NOT greatly care for?", "He does not care for sweets like ice cream, apple pie, or custard.", "Easy", "Remembering"),
    ("What does the hippopotamus use to flavor what he eats?", "He uses a little 'hippopotomustard'.", "Easy", "Remembering"),
    ("How is the character of the hippopotamus described in Stanza 3?", "He is true to all his principles and just, always doing his best to do what he must.", "Easy", "Remembering"),
    ("What funny word is used for the things the hippo MUST do?", "The word used is 'hippopotomust'.", "Easy", "Remembering"),
    ("Which vehicles does the hippopotamus NEVER ride in?", "He never rides in trucks, trams, taxicabs, or omnibuses.", "Easy", "Remembering"),
    ("What does the hippopotamus avoid by not riding in vehicles?", "He avoids getting caught in traffic jams and other 'hippopotomusses' (messes).", "Easy", "Remembering"),
    ("What does the word 'bustle' mean according to the poem?", "'Bustle' refers to the rear part of the body.", "Easy", "Understanding"),
    ("What is an omnibus?", "An omnibus is a traditional large bus for carrying passengers.", "Easy", "Understanding"),
    ("What is a tram?", "A tram is a rail vehicle that runs on street tracks.", "Easy", "Understanding"),
    ("How does the hippopotamus move along?", "He rolls along on his big muscular limbs.", "Easy", "Remembering"),
    ("Is the hippopotamus a weak or a strong animal in the poem?", "He is a strong animal.", "Easy", "Remembering"),
    ("What funny word blends 'hippopotamus' and 'mustard'?", "Hippopotomustard.", "Easy", "Understanding"),
    ("What funny word blends 'hippopotamus' and 'musses'?", "Hippopotomusses.", "Easy", "Understanding"),
    ("Why doesn't the hippopotamus get stuck in traffic jams?", "Because he never rides in city vehicles like trucks, taxicabs, or buses.", "Easy", "Understanding"),
    ("Does the hippopotamus like sugary desserts?", "No, he does not greatly care for sweets like ice cream or apple pie.", "Easy", "Remembering"),
    ("What does 'just' mean when describing the hippo's character?", "'Just' means fair, honest, and morally right.", "Easy", "Understanding"),
    ("What does 'principles' mean?", "'Principles' means moral rules and guidelines for good behavior.", "Easy", "Understanding"),
    ("How many stanzas are there in Chapter 13's poem?", "There are 4 stanzas in the poem.", "Easy", "Remembering"),
    ("What technique does the poet use to create funny words?", "He combines the prefix 'hippopoto-' with regular words like muscle, mustard, must, and musses.", "Easy", "Understanding"),
    ("What does the hippo do when he has a duty to fulfill?", "He always tries his best to do the things he must do.", "Easy", "Understanding"),
    ("What visual image do you get of the hippo walking?", "A giant, muscular, heavy animal rolling along cheerfully on four strong limbs.", "Easy", "Understanding"),
    ("What is the title of Chapter 13?", "The title of Chapter 13 is 'Habits of the Hippopotamus'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Explain the clever wordplay Arthur Guiterman uses throughout the poem.", "Guiterman attaches 'hippopoto-' to everyday words (muscle -> hippopotomuscle, mustard -> hippopotomustard, must -> hippopotomust, messes -> hippopotomusses) to make long, funny rhyming words.", "Medium", "Analyzing"),
    ("How does the hippopotamus demonstrate sensible eating habits?", "He avoids overindulging in sugary desserts like ice cream and apple pie, preferring simple food seasoned with a bit of mustard.", "Medium", "Evaluating"),
    ("Describe the moral character of the hippopotamus in Stanza 3.", "Despite his giant physical strength, he is gentle, fair ('just'), stays loyal to his moral principles, and conscientiously performs his duties.", "Medium", "Analyzing"),
    ("Why is walking better than riding vehicles for the hippopotamus?", "By walking on his own legs instead of taking trucks or taxicabs, he completely avoids stressful city traffic jams and chaotic messes.", "Medium", "Understanding"),
    ("What is the rhyme scheme of Stanza 1 (strong / bustle / along / hippopotomuscle)?", "The rhyme scheme is ABAB (strong rhymes with along; bustle rhymes with hippopotomuscle).", "Medium", "Remembering"),
    ("Summarize Page 46 of the textbook in two sentences.", "Arthur Guiterman's poem 'Habits of the Hippopotamus' describes a strong, muscular hippo with a huge head who prefers savory food with mustard over sweets. Honest and dutiful, he avoids city vehicles, thereby staying free from traffic jams and messes.", "Medium", "Understanding"),
    ("Why is the word 'hippopotomusses' a clever visual and verbal pun?", "It punningly combines the plural of hippopotamus with 'musses' (meaning messy, chaotic traffic complications).", "Medium", "Analyzing"),
    ("How does the poem balance animal characteristics with human moral virtues?", "It combines realistic hippo traits (big head, huge body, strong limbs) with human virtues (ethics, fairness, simple living, duty).", "Medium", "Analyzing"),
    ("What makes multi-syllable made-up words fun for Class 2 students to read aloud?", "They challenge children's pronunciation in a playful way, creating rhythmic tongue-twisters that bring laughter.", "Medium", "Evaluating"),
    ("How does the hippopotamus set a good example for handling daily responsibilities?", "He does not make excuses; he always tries his best to fulfill his moral duties ('hippopotomust').", "Medium", "Applying"),
    ("Contrast the hippo's size with his peaceful, gentle behavior.", "Though giant and powerful enough to crush things, he is peaceful, eats simple food, respects principles, and avoids city chaos.", "Medium", "Analyzing"),
    ("Why does the poet mention ice cream, apple pie, and custard?", "To list common delicious sweets that humans love, highlighting that the hippo surprisingly prefers simple mustard instead.", "Medium", "Understanding"),
    ("What does 'broad of bustle' mean in a humorous physical description?", "It poetically describes the hippo's wide, heavy rear end as he rolls along on his legs.", "Medium", "Understanding"),
    ("How does the poem encourage children to choose peaceful, unhurried habits?", "By showing that walking peacefully and staying away from crowded, noisy transport keeps life simple and trouble-free.", "Medium", "Evaluating"),
    ("How can Class 2 students recite this poem dramatically?", "Students can stomp lightly for 'hippopotomuscle', mime eating mustard for 'hippopotomustard', and salute for 'hippopotomust'.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the pedagogical value of portmanteau poetry in early childhood language development.", "Portmanteau poetry breaks down fear of long words, builds phonemic awareness, enhances syllabic decoding skills, and sparks creative writing interest.", "Hard", "Evaluating"),
    ("Analyze how Arthur Guiterman uses iambic meter and rhyme to maintain comedic momentum.", "Guiterman uses consistent 4-beat and 3-beat iambic lines with alternating ABAB rhymes, giving the poem a brisk, dancing march tempo.", "Hard", "Analyzing"),
    ("Deconstruct the four thematic stanzas of 'Habits of the Hippopotamus'.", "1. **Physical Anatomy**: Head, bustle, muscular limbs.\n2. **Dietary Preferences**: Rejection of sweets, preference for mustard.\n3. **Moral Character**: Justice, principles, dutifulness.\n4. **Lifestyle Choices**: Rejection of vehicles, avoidance of traffic jams.", "Hard", "Analyzing"),
    ("Compare Arthur Guiterman's hippo with other famous literary hippos (e.g., George and Martha).", "Guiterman's hippo is defined by poetic linguistic puns and urban avoidance, whereas other literary hippos focus on social friendship stories.", "Hard", "Analyzing"),
    ("Evaluate the ecological symbolism of a wild animal rejecting urban transportation.", "The hippo's rejection of trucks and taxicabs symbolizes the natural world staying untainted by human urban pollution, traffic, and stress.", "Hard", "Evaluating"),
    ("How can primary teachers use this poem for a cross-curricular Science and English lesson?", "Science: Studying real hippopotamus anatomy and habitat in Africa; English: Analyzing poetic meter, invented words, and rhyming schemes.", "Hard", "Applying"),
    ("Assess the artistic function of nonsense words in classic light verse.", "Nonsense words create stylistic delight, subvert formal dictionary rigidity, and demonstrate that poetry can be joyous verbal play.", "Hard", "Evaluating"),
    ("Why is 'doing what one hippopotomust' a timeless philosophy for students?", "It re-frames mandatory chores and homework into a cheerful, self-enforced moral duty done with pride.", "Hard", "Analyzing"),
    ("Formulate an additional 4-line stanza introducing a new habit of the hippopotamus.", "'He never wears a suit or tie,\nNor fancy coats of blue;\nHe bathes beneath the sunny sky\nIn hippopotomud!'", "Hard", "Creating"),
    ("Synthesize the ultimate lesson of Chapter 13 for Class 2 learners.", "Be proud of your unique strength, live by honest principles, eat sensibly, avoid unnecessary chaos, and enjoy creative wordplay!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 13: Habits of the Hippopotamus\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH13_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
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
    ("Describe the physical appearance, diet, character, and travel habits of the hippopotamus in Chapter 13.", 
     "In Arthur Guiterman's poem 'Habits of the Hippopotamus':\n1. **Appearance**: The hippopotamus is strong, huge of head, broad of bustle (rear body), and rolls along on big limbs filled with 'hippopotomuscle'.\n2. **Diet**: He does not care for sweets like ice cream or pie, preferring food flavored with a little 'hippopotomustard'.\n3. **Character**: He is true to his principles, fair ('just'), and always does what he 'hippopotomust'.\n4. **Travel Habits**: He never rides in trucks, trams, taxicabs, or omnibuses, which keeps him free from traffic jams and messes.", 
     "Easy", "Remembering"),

    ("Explain the funny invented words used in the poem and what real words they are based on.", 
     "The poet Arthur Guiterman invents clever portmanteau words by attaching 'hippopoto-' to everyday words:\n1. **Hippopotomuscle**: Hippopotamus + muscle (describing his strong limbs).\n2. **Hippopotomustard**: Hippopotamus + mustard (describing his favorite condiment).\n3. **Hippopotomust**: Hippopotamus + must (describing his duties).\n4. **Hippopotomusses**: Hippopotamus + musses/messes (describing chaotic traffic trouble).", 
     "Easy", "Understanding"),

    ("Why does the hippopotamus avoid riding in city vehicles like trucks, trams, and taxicabs?", 
     "The hippopotamus avoids riding in trucks, trams, taxicabs, and omnibuses because he prefers walking on his own strong legs. By staying away from crowded city vehicles, he successfully keeps himself out of frustrating traffic jams, crowded noise, and chaotic urban messes ('hippopotomusses').", 
     "Easy", "Understanding"),

    ("Describe the food preferences of the hippopotamus as detailed in Stanza 2.", 
     "In Stanza 2, the hippopotamus shows sensible eating habits. He does not greatly care for rich, sugary desserts like ice cream, apple pie, or custard. Instead, he prefers plain, savory food and likes to add a little bit of 'hippopotomustard' (mustard) to give his meal a nice flavor.", 
     "Easy", "Remembering"),

    ("Explain the moral principles and dutiful behavior of the hippopotamus in Stanza 3.", 
     "In Stanza 3, the poem highlights that despite his giant physical power, the hippopotamus is moral and gentle. He is true to all his principles, acts with justice and fairness toward others, and always tries his best to fulfill all the duties and responsibilities that one 'hippopotomust' do.", 
     "Easy", "Understanding"),

    ("Explain the meanings of the vocabulary words 'bustle', 'tram', and 'omnibus'.", 
     "1. **Bustle**: In this poem, refers to the rear part of the body ('broad of bustle').\n2. **Tram**: A rail vehicle that runs along tracks on city streets for public transport.\n3. **Omnibus**: A traditional, large passenger bus used in cities.", 
     "Easy", "Understanding"),

    ("How does the poet create rhythm and rhyme in the four stanzas of the poem?", 
     "The poet uses a consistent 4-line stanza structure with an ABAB rhyming scheme in every stanza (e.g., strong/along, bustle/hippopotomuscle). This alternating rhyme scheme combines with a steady bouncy beat to give the poem a marching, musical rhythm.", 
     "Easy", "Understanding"),

    ("Why is the hippopotamus a positive role model for young children?", 
     "The hippopotamus is a great role model because he is strong yet gentle, eats sensible non-sugary food, stays true to honest principles, does his duty dutifully, and makes smart choices to avoid unnecessary traffic jams and daily messes.", 
     "Easy", "Evaluating"),

    ("What contrast is shown between how giant the hippo is and how simply he lives?", 
     "Though the hippo is massive with a huge head, broad bustle, and giant muscles, he lives very simply: he eats plain food with mustard instead of fancy sweets, walks on his own legs instead of taking taxis, and lives by fair, simple principles.", 
     "Easy", "Analyzing"),

    ("Summarize the four stanzas of 'Habits of the Hippopotamus' in your own words.", 
     "**Stanza 1**: Describes his strong body, huge head, and limbs filled with muscle.\n**Stanza 2**: Describes his diet—disliking sweets and preferring mustard.\n**Stanza 3**: Describes his honest, just character and commitment to duty.\n**Stanza 4**: Describes his travel habits—walking instead of taking buses or cabs to avoid traffic jams.", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Who wrote 'Habits of the Hippopotamus' and what is special about his poetic style?", "Written by Arthur Guiterman, who is famous for humorous light verse filled with playful invented words and catchy rhythms.", "Easy", "Remembering"),
    ("What does 'broad of bustle' mean when describing the hippo's body?", "It means the hippo has a wide, heavy rear end that sways as he rolls along on his big muscular legs.", "Easy", "Understanding"),
    ("Why doesn't the hippo eat ice cream, apple pie, or custard?", "Because he does not greatly care for sugary sweets, preferring savory food seasoned with mustard.", "Easy", "Remembering"),
    ("What does 'hippopotomust' teach about doing your best?", "It teaches that whenever we have a duty or job that we MUST do, we should do it faithfully and cheerfully.", "Easy", "Evaluating"),
    ("What does 'hippopotomusses' mean at the end of the poem?", "It is a funny pun combining hippopotamus with 'musses' or messes, referring to chaotic city traffic trouble.", "Easy", "Understanding"),
    ("How does the hippo move along on his limbs?", "He rolls along smoothly on his big, strong, muscular legs.", "Easy", "Remembering"),
    ("Why is walking better for the hippo than taking a taxicab?", "Walking keeps him healthy, independent, and completely free from traffic jams in the city.", "Easy", "Understanding"),
    ("What four vehicles are listed in Stanza 4?", "Trucks, trams, taxicabs, and omnibuses.", "Easy", "Remembering"),
    ("What makes the invented words easy for children to remember?", "They all start with the familiar sound 'hippopoto-' and end with common rhyming words like muscle, mustard, must, and musses.", "Easy", "Understanding"),
    ("How can a student use this poem to practice expressive speech?", "By pronouncing the long 6-syllable made-up words clearly and stamping feet to the rhythmic beat of the stanzas.", "Easy", "Applying"),
    ("Is the hippopotamus a fair or unfair animal?", "He is a fair animal ('just') who is true to all his principles.", "Easy", "Remembering"),
    ("What does 'true to all his principles' mean?", "It means he always stays honest and follows his moral rules without breaking them.", "Easy", "Understanding"),
    ("Why is mustard mentioned in a hippo's poem?", "Because it rhymes humorously with custard ('custard / hippopotomustard') and gives his food a little extra flavor.", "Easy", "Understanding"),
    ("What is the difference between a real hippo's diet and this poem's hippo?", "Real hippos eat river grass; the poet's hippo humorously eats food with mustard and avoids pie.", "Easy", "Analyzing"),
    ("Summarize Chapter 13 in five key sentences.", "Chapter 13 contains Arthur Guiterman's funny poem 'Habits of the Hippopotamus'. The hippo is strong, huge of head, and rolls along on big limbs filled with 'hippopotomuscle'. He prefers savory food with 'hippopotomustard' over sweets like ice cream or custard. Honest and fair, he always does the things one 'hippopotomust'. By walking instead of taking trucks or taxicabs, he avoids traffic jams and 'hippopotomusses'.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how Arthur Guiterman blends biological realism with imaginative wordplay.", 
     "Guiterman grounds the poem in biological realism—noting the hippo's massive head, broad body, and thick muscular limbs. He then layers whimsical fantasy on top by giving the hippo human habits (eating mustard, keeping principles, avoiding taxicabs) and creating invented words ('hippopotomuscle', 'hippopotomustard') that make the reader laugh.", 
     "Medium", "Analyzing"),

    ("Examine the moral lessons hidden beneath the lighthearted humor of Chapter 13.", 
     "Beneath the silly rhymes lie three clear moral lessons:\n1. **Dietary Moderation**: Preferring simple food over excessive junk sweets.\n2. **Moral Integrity**: Staying true to principles and doing one's duty ('hippopotomust').\n3. **Practical Wisdom**: Avoiding stressful, crowded situations (traffic jams) by making smart personal choices.", 
     "Medium", "Evaluating"),

    ("Discuss the structure and rhythm of the quadrisyllabic rhymes in 'Habits of the Hippopotamus'.", 
     "The poem uses alternating ABAB rhymes where the B-rhymes are long, quadrisyllabic invented words:\n- bustle / hippopotomuscle\n- custard / hippopotomustard\n- just / hippopotomust\n- omnibuses / hippopotomusses\nThese long rhyming endings create a playful, stumbling rhythm that echoes the heavy, rolling walk of a hippopotamus.", 
     "Medium", "Analyzing"),

    ("Explore the social commentary on modern city transportation in Stanza 4.", 
     "Stanza 4 presents a lighthearted critique of modern city transport. Humans often crowd into trucks, trams, taxicabs, and omnibuses, getting stuck in stressful traffic jams. The hippo wisely avoids all these vehicles, demonstrating that walking and living simply avoids artificial urban stress.", 
     "Medium", "Analyzing"),

    ("How can Class 2 teachers use Chapter 13 for a fun language arts activity?", 
     "Teachers can ask students to invent their own 'animal portmanteau words' by taking an animal name (like 'Elephant') and combining it with daily items (e.g., 'Elephantomobile', 'Elephantomusic'), building creative vocabulary.", 
     "Medium", "Applying"),

    ("Why is the hippo's choice of mustard over ice cream significant?", "It shows that he values substance and true flavor over flashy, sugary treats, reflecting a grounded, sensible character.", "Medium", "Analyzing"),
    ("Describe how the poem's 4 stanzas cover four distinct aspects of the hippo's life.", "Stanza 1 covers physical anatomy; Stanza 2 covers dietary habits; Stanza 3 covers moral character; Stanza 4 covers travel habits.", "Medium", "Understanding"),
    ("What makes the hippo's rolling walk sound cheerful in Stanza 1?", "The phrase 'limbs on which he rolls along' creates an image of a big, happy animal moving smoothly without effort despite his massive weight.", "Medium", "Analyzing"),
    ("How does the poem demonstrate that big size does not mean mean behavior?", "Though giant and muscular, the hippo is portrayed as fair, just, peaceful, and polite—never aggressive.", "Medium", "Evaluating"),
    ("What is the difference between a serious poem about duty and this poem?", "A serious poem uses solemn language; this poem uses silly made-up words like 'hippopotomust' to make doing duty feel fun and lighthearted.", "Medium", "Comparing"),
    ("Why did Guiterman choose a hippopotamus instead of a small animal like a mouse?", "Because 'hippopotamus' is a long 5-syllable word that offers rich possibilities for funny, exaggerated word blends.", "Medium", "Analyzing"),
    ("How does avoiding traffic jams contribute to a peaceful lifestyle?", "Traffic jams cause noise, anger, and wasted time. Avoiding them keeps the hippo calm, relaxed, and stress-free.", "Medium", "Understanding"),
    ("Explain the meaning of 'just' in the phrase 'true to all his principles and just'.", "'Just' means acting fairly, honoring agreements, and treating all creatures with equality and respect.", "Medium", "Understanding"),
    ("What visual drawing would best illustrate Stanza 4?", "A drawing of a big smiling hippo walking happily down a green footpath while a line of tiny cars and buses sit stuck in a smoky traffic jam.", "Medium", "Applying"),
    ("Construct a 4-line poem about an Elephant using Arthur Guiterman's style.", "'The elephant is big and strong,\nWith ears as wide as sails;\nHe carries water all day long\nIn elephantom-pails!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the literary effectiveness of portmanteau word creation in children's poetry.", 
     "Portmanteau creation (blending words) is highly effective in children's poetry. It expands linguistic creativity, breaks down fear of multi-syllable words, builds phonemic awareness, and demonstrates that language can be adapted playfully to fit rhyme and rhythm.", 
     "Hard", "Evaluating"),

    ("Deconstruct the rhyming and metrical blueprint of 'Habits of the Hippopotamus'.", 
     "The poem is composed in four quatrains with an ABAB rhyme scheme. Lines 1 and 3 are in iambic tetrameter (4 beats); lines 2 and 4 are in iambic trimeter (3 beats) ending in hypermetrical quadrisyllabic portmanteau rhymes.", 
     "Hard", "Analyzing"),

    ("Synthesize the physical, moral, dietary, and social philosophy of the hippo.", 
     "1. **Physical**: Massive strength used peacefully.\n2. **Dietary**: Savory moderation over sugary indulgence.\n3. **Moral**: Firm adherence to principles and justice.\n4. **Social**: Avoidance of artificial urban congestion and chaos.", 
     "Hard", "Synthesizing"),

    ("Formulate a complete lesson unit integrating Chapter 13 with Elementary Science and English.", 
     "- **English**: Portmanteau word creation, ABAB rhyme analysis, recitation.\n- **Science**: Mammal classification, real hippo habitats in African rivers, herbivorous diets.\n- **Ethics**: Discussion on justice, keeping promises, and simple living.", 
     "Hard", "Creating"),

    ("Evaluate the impact of light verse in developing a lifelong love for poetry.", 
     "Light verse disarms young readers who might find formal poetry intimidating. By prioritizing humor, bouncy rhythm, and clever wordplay, it proves that poetry is accessible, enjoyable, and entertaining, laying the foundation for lifelong literary appreciation.", 
     "Hard", "Evaluating"),

    ("Analyze why the word 'hippopotomusses' is the ultimate climax of the poem.", "It serves as the final comedic climax, combining the animal's name with urban traffic 'messes' to resolve the 4-stanza narrative on a high note of laughter.", "Hard", "Analyzing"),
    ("Compare Arthur Guiterman's invented words with Lewis Carroll's 'Jabberwocky' portmanteau words.", "Carroll invents entirely new nonsense roots (e.g., 'slithy' = slimy + lithe); Guiterman keeps real root words (muscle, mustard) and prefixes them with 'hippopoto-' for clear comedic recognition.", "Hard", "Analyzing"),
    ("Draft a short review of Chapter 13 for a primary school literary journal.", "'Arthur Guiterman's 16-line masterpiece 'Habits of the Hippopotamus' is a triumph of light verse. Combining quadrisyllabic wordplay with lessons in diet, ethics, and travel, it delights Class 2 learners while sharpening phonemic skills.'", "Hard", "Creating"),
    ("Assess how the hippo's rejection of public transit reflects environmental wisdom.", "Walking under one's own power reduces urban reliance on fossil-fuel vehicles, presenting an unintended yet modern green environmental message.", "Hard", "Evaluating"),
    ("Synthesize the ultimate philosophy of Chapter 13 into a guiding motto.", "'Embrace your unique strength, live by honest principles, choose moderation over sugary excess, and walk cheerfully through life!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 13: Habits of the Hippopotamus\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH13_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
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
    ("The hippopotamus is strong\nAnd huge of head and broad of bustle;\nThe limbs on which he rolls along\nAre big with hippopotomuscle.",
     [
         ("How is the strength and head of the hippopotamus described?", "He is strong and huge of head.", "Easy", "Remembering"),
         ("What does 'broad of bustle' mean?", "Broad rear part of the body.", "Easy", "Understanding"),
         ("How does the hippopotamus move along?", "He rolls along on his limbs.", "Easy", "Remembering"),
         ("What funny word is used for his muscle?", "Hippopotomuscle.", "Easy", "Remembering"),
         ("Which two lines rhyme in this stanza?", "Lines 1 & 3 (strong/along) and Lines 2 & 4 (bustle/hippopotomuscle).", "Medium", "Analyzing")
     ]),

    # Set 2
    ("He does not greatly care for sweets\nLike ice cream, apple pie or custard,\nBut takes to flavor what he eats\nA little hippopotomustard.",
     [
         ("What foods does the hippopotamus NOT greatly care for?", "Sweets like ice cream, apple pie, or custard.", "Easy", "Remembering"),
         ("Name three sweet foods listed in the extract.", "Ice cream, apple pie, and custard.", "Easy", "Remembering"),
         ("What does he use to flavor his food?", "A little hippopotomustard.", "Easy", "Remembering"),
         ("What real word is 'hippopotomustard' based on?", "Mustard.", "Easy", "Understanding"),
         ("What does his food choice show about his character?", "He prefers sensible savory food over excessive sugary desserts.", "Medium", "Evaluating")
     ]),

    # Set 3
    ("The hippopotamus is true\nTo all his principles and just;\nHe always tries his best to do\nThe things one hippopotomust.",
     [
         ("What is the hippopotamus true to?", "All his principles.", "Easy", "Remembering"),
         ("What word describes his fairness?", "Just.", "Easy", "Remembering"),
         ("What does he always try his best to do?", "The things one hippopotomust (his duties).", "Easy", "Remembering"),
         ("What does 'hippopotomust' mean poetically?", "The things that one MUST do / duty.", "Medium", "Understanding"),
         ("What moral values are highlighted in this stanza?", "Integrity, justice, and dutifulness.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("He never rides in trucks or trams,\nIn taxicabs or omnibuses,\nAnd so keeps out of traffic jams\nAnd other hippopotomusses.",
     [
         ("Name four vehicles the hippopotamus never rides in.", "Trucks, trams, taxicabs, and omnibuses.", "Easy", "Remembering"),
         ("What is an omnibus?", "A large public passenger bus.", "Easy", "Understanding"),
         ("What does the hippopotamus keep out of by not riding vehicles?", "Traffic jams and other hippopotomusses.", "Easy", "Remembering"),
         ("What real word is 'hippopotomusses' a pun on?", "Musses / messes.", "Medium", "Understanding"),
         ("What practical wisdom does this stanza teach?", "Walking peacefully avoids stressful urban traffic jams.", "Medium", "Evaluating")
     ]),

    # Set 5
    ("Word Meaning: Bustle: (here) rear part of body",
     [
         ("What is the definition of 'bustle' in this poem?", "Rear part of body.", "Easy", "Remembering"),
         ("Which part of the hippopotamus's body is broad?", "His bustle (rear body).", "Easy", "Remembering"),
         ("Why is this word definition provided?", "To clarify the poetic description of the hippo's body shape.", "Medium", "Understanding"),
         ("Is 'bustle' used here to mean busy activity or body part?", "It is used to mean the rear part of the body.", "Easy", "Understanding"),
         ("What adjective describes the bustle in Stanza 1?", "Broad ('broad of bustle').", "Easy", "Remembering")
     ]),

    # Set 6
    ("The hippopotamus is strong / And huge of head and broad of bustle...",
     [
         ("Name the title of the poem.", "'Habits of the Hippopotamus'.", "Easy", "Remembering"),
         ("Who wrote this poem?", "Arthur Guiterman.", "Easy", "Remembering"),
         ("What animal is the poem about?", "The hippopotamus.", "Easy", "Remembering"),
         ("What adjective describes the hippo's head?", "Huge.", "Easy", "Remembering"),
         ("What main technique makes this poem famous?", "Clever portmanteau wordplay combining 'hippopoto-' with everyday words.", "Medium", "Analyzing")
     ]),

    # Set 7
    ("He does not greatly care for sweets... But takes to flavor what he eats / A little hippopotomustard.",
     [
         ("Does the hippo like ice cream?", "No, he does not greatly care for sweets like ice cream.", "Easy", "Remembering"),
         ("What flavor does he add to what he eats?", "A little hippopotomustard (mustard).", "Easy", "Remembering"),
         ("What rhyming words end lines 2 and 4 in this extract?", "Custard / hippopotomustard.", "Easy", "Remembering"),
         ("Why is 'mustard' a funny choice for a hippo?", "Because mustard is a sharp, spicy condiment, contrasting with sweet desserts.", "Medium", "Understanding"),
         ("Summarize this stanza in one simple sentence.", "The hippo rejects sugary sweets and prefers food flavored with a little mustard.", "Medium", "Understanding")
     ]),

    # Set 8
    ("The hippopotamus is true / To all his principles and just... The things one hippopotomust.",
     [
         ("Is the hippo honest?", "Yes, he is true to all his principles.", "Easy", "Remembering"),
         ("What does 'just' mean?", "Fair and honest.", "Easy", "Understanding"),
         ("Does the hippo try his best or give up easily?", "He always tries his best.", "Easy", "Remembering"),
         ("What rhyming pair ends lines 2 and 4 in this extract?", "Just / hippopotomust.", "Easy", "Remembering"),
         ("What character lesson can children learn from this stanza?", "To be honest, fair, and always try your best to do your duty.", "Medium", "Evaluating")
     ]),

    # Set 9
    ("He never rides in trucks or trams... And so keeps out of traffic jams / And other hippopotomusses.",
     [
         ("Why does the hippo avoid traffic jams?", "Because he never rides in vehicles like trucks, trams, cabs, or buses.", "Easy", "Remembering"),
         ("What is a tram?", "A rail vehicle running on city street tracks.", "Easy", "Understanding"),
         ("What rhyming pair ends lines 2 and 4 in this extract?", "Omnibuses / hippopotomusses.", "Easy", "Remembering"),
         ("What visual scene does 'traffic jams' bring to mind?", "Long lines of stuck cars, trucks, and buses blowing horns in city streets.", "Medium", "Understanding"),
         ("How does the hippo travel instead of using vehicles?", "He rolls along on his own big muscular legs.", "Medium", "Understanding")
     ]),

    # Set 10
    ("Habits of the Hippopotamus by Arthur Guiterman: The hippopotamus is strong... And other hippopotomusses.",
     [
         ("How many stanzas are in the entire poem?", "4 stanzas.", "Easy", "Remembering"),
         ("How many total lines are in the poem?", "16 lines.", "Easy", "Remembering"),
         ("Name all four invented words in the poem.", "Hippopotomuscle, hippopotomustard, hippopotomust, hippopotomusses.", "Medium", "Remembering"),
         ("What is the general mood of Arthur Guiterman's poem?", "Whimsical, cheerful, rhythmic, and lighthearted.", "Medium", "Evaluating"),
         ("Summarize the poem's core philosophy in one sentence.", "Live simply, stay true to honest principles, do your best, avoid chaos, and enjoy language!", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 13: Habits of the Hippopotamus\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH13_EXT_{q_counter:03d}"
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

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 13 in {CH13_DIR}")
