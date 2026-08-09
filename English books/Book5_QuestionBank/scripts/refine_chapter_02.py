r"""
Refines all 6 Category files for Book 5 Chapter 02 ("The Raven that Wanted to be an Eagle") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH02_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_02")
os.makedirs(CH02_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Where did the raven live in the fable?", "(A) In a valley", "(B) High up in the mountains", "(C) In a deep ocean cave", "(D) On a desert dune", "(A)", "The raven lived in a valley.", "Easy", "Remembering", "Setting"),
    ("Where did the eagle live?", "(A) High up in the mountains", "(B) In a valley", "(C) In a dense forest swamp", "(D) Near a farmer's barn", "(A)", "The eagle lived high up in the mountains.", "Easy", "Remembering", "Setting"),
    ("Why was the raven unhappy with himself?", "(A) He envied the eagle's precise hunting skills and wished to be like him", "(B) He had no feathers on his wings", "(C) He could not find any food in the valley", "(D) Other birds bullied him every day", "(A)", "He admired the eagle and wished to be as precise and strong as him.", "Easy", "Understanding", "Motivation"),
    ("How did the eagle catch its prey from the valley?", "(A) Swooped down from great heights with great precision", "(B) Walked slowly on the ground", "(C) Trapped animals in a net", "(D) Waited for animals to die naturally", "(A)", "The eagle swooped down with great precision.", "Easy", "Remembering", "Action"),
    ("What animal did the eagle carry away from the flock in front of the raven?", "(A) A sheep", "(B) A cow", "(C) A rabbit", "(D) A goat", "(A)", "The eagle carried away a sheep from the flock.", "Easy", "Remembering", "Plot Detail"),
    ("How did everyone react when the eagle carried away the sheep?", "(A) They were shocked by the sudden attack", "(B) They clapped and cheered", "(C) They laughed loudly", "(D) Nobody noticed the eagle", "(A)", "Carried away a sheep much to everyone's shock.", "Easy", "Remembering", "Reaction"),
    ("How long did the raven practice flying and swooping like an eagle?", "(A) A fortnight (two weeks)", "(B) Only ten minutes", "(C) Three full years", "(D) One single morning", "(A)", "He practiced for a fortnight.", "Easy", "Remembering", "Time Detail"),
    ("Who was the raven waiting for before carrying out his attack?", "(A) The shepherd to arrive with the flock of sheep", "(B) The eagle to return to the valley", "(C) The rain to stop", "(D) The night to set in", "(A)", "He waited for the shepherd to arrive with the flock.", "Easy", "Remembering", "Plot Detail"),
    ("Which sheep did the foolish raven choose as his prey?", "(A) The fattest sheep of the flock", "(B) The smallest newborn lamb", "(C) The weakest sick sheep", "(D) The black sheep at the back", "(A)", "The raven chose the fattest sheep of the flock.", "Easy", "Remembering", "Choice"),
    ("Why did the raven choose the fattest sheep instead of a smaller one?", "(A) He thought tales of his grand feat would travel in all directions", "(B) He wanted to feed twenty other ravens", "(C) The fattest sheep was sleeping", "(D) The shepherd asked him to catch it", "(A)", "He thought tales of his feat would travel in all directions.", "Easy", "Understanding", "Vanity"),
    ("What happened when the raven swooped down on the chosen sheep?", "(A) His talons got stuck in the thick hair of the sheep", "(B) He carried the sheep high into the clouds", "(C) The sheep bit the raven's wing", "(D) The sheep ran into a river", "(A)", "His talons got stuck in the thick hair on the sheep.", "Easy", "Remembering", "Complication"),
    ("Could the raven fly away with the fattest sheep?", "(A) No, he tried in vain and was stuck", "(B) Yes, he flew straight to his nest", "(C) Yes, but he dropped it halfway", "(D) He did not try to lift it", "(A)", "He tried to fly away with it but in vain.", "Easy", "Remembering", "Outcome"),
    ("Who came and pulled the raven away from the sheep?", "(A) The shepherd", "(B) The eagle", "(C) The farmer's dog", "(D) Another raven", "(A)", "The shepherd pulled away the raven from the sheep.", "Easy", "Remembering", "Character Action"),
    ("What did the shepherd do to the raven after pulling it off the sheep?", "(A) Threw it roughly on the ground", "(B) Kept it in a cage as a pet", "(C) Gave it fresh grains to eat", "(D) Set it free gently in the air", "(A)", "The shepherd threw it roughly on the ground.", "Easy", "Remembering", "Consequence"),
    ("What happened to the raven after being thrown to the ground?", "(A) He got injured and could not fly for many days", "(B) He immediately flew up into the clouds", "(C) He turned into an eagle", "(D) He ran away into the woods", "(A)", "The raven got injured and could not fly for many days.", "Easy", "Remembering", "Physical Condition"),
    ("What is the moral of the fable 'The Raven that Wanted to be an Eagle'?", "(A) Do not imitate others blindly", "(B) Always fight with eagles", "(C) Fat sheep are easy to catch", "(D) Practice makes a raven an eagle", "(A)", "Moral: Do not imitate others blindly.", "Easy", "Remembering", "Moral Lesson"),
    ("What does the word 'swoop' mean?", "(A) To fly down suddenly and swiftly", "(B) To sing a high song", "(C) To swim under water", "(D) To sleep on a tree branch", "(A)", "Swoop means to fly down suddenly.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'precise' mean?", "(A) Clear, exact, and accurate", "(B) Very large", "(C) Extremely noisy", "(D) Dark and gloomy", "(A)", "Precise means clear and accurate.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'feat' mean?", "(A) Something that shows great skill or strength", "(B) The bottom part of a bird's leg", "(C) A small stone", "(D) A musical concert", "(A)", "Feat means an action showing great skill.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'opportune' mean?", "(A) Suitable or favorable moment", "(B) Very dangerous", "(C) Late at night", "(D) Difficult to understand", "(A)", "Opportune means suitable.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'fortnight' mean?", "(A) A period of two weeks (14 days)", "(B) A period of forty days", "(C) Four hours", "(D) One full year", "(A)", "Fortnight means a period of two weeks.", "Easy", "Understanding", "Vocabulary"),
    ("What body part of the raven got tangled in the sheep's wool?", "(A) Talons (claws)", "(B) Beak", "(C) Tail feathers", "(D) Eyes", "(A)", "His talons got stuck in the thick hair.", "Easy", "Remembering", "Anatomy Detail"),
    ("Why did the raven consider himself 'simple' compared to the eagle?", "(A) He lacked the physical size, strength, and talon structure of an eagle", "(B) He had black feathers instead of white", "(C) He could not make any sounds", "(D) He lived in a house", "(A)", "He lacked the size, strength, and power of a predatory eagle.", "Easy", "Understanding", "Self-Perception"),
    ("What literary collection does this fable belong to?", "(A) Aesop's Fables", "(B) Panchatantra", "(C) Jataka Tales", "(D) Arabian Nights", "(A)", "It is an Aesop Fable.", "Easy", "Remembering", "Genre"),
    ("What is the title of Chapter 02?", "(A) The Raven that Wanted to be an Eagle", "(B) The Foolish Pandit", "(C) The Tiger and the Persimmon", "(D) Sankalp and his Friend", "(A)", "Chapter 02 is titled 'The Raven that Wanted to be an Eagle'.", "Easy", "Remembering", "Title"),

    # Medium (26-40)
    ("Why was the raven's ambition to hunt like an eagle fundamentally flawed?", "(A) He ignored his biological limitations as a raven and blindly imitated a larger predator", "(B) He did not practice flying enough days", "(C) He chose a goat instead of a sheep", "(D) The eagle gave him bad advice", "(A)", "He ignored his biological limitations and natural capabilities.", "Medium", "Analyzing", "Character Flaw"),
    ("How did vanity influence the raven's choice of prey?", "(A) He chose the fattest sheep to win glory and fame, overestimating his strength", "(B) He chose a small lamb to be safe", "(C) He let the shepherd choose for him", "(D) He wanted to share the fat sheep with the eagle", "(A)", "Vanity made him choose the fattest sheep for glory.", "Medium", "Analyzing", "Vanity"),
    ("What physical difference prevented the raven from lifting the sheep?", "(A) A raven lacks the muscle mass, wing span, and powerful talons required to lift heavy livestock", "(B) The sheep was tied to a tree with a rope", "(C) The eagle pushed the raven down", "(D) The raven's wings were broken before swooping", "(A)", "Ravens lack muscle mass and wing power to lift heavy sheep.", "Medium", "Understanding", "Physical Reality"),
    ("What does the shepherd's rough treatment of the raven signify?", "(A) Consequences of rash interference with livestock and foolish arrogance", "(B) The shepherd's hatred for all birds", "(C) A reward for entertaining the sheep", "(D) The shepherd training the raven to hunt", "(A)", "Consequences of foolish arrogance and livestock interference.", "Medium", "Analyzing", "Consequence"),
    ("How does practicing for a fortnight fail to make the raven an eagle?", "(A) Practice cannot alter species capabilities or physical anatomy; desire without capability leads to failure", "(B) He practiced at night instead of day", "(C) A fortnight was too long to practice", "(D) The eagle stole his practice time", "(A)", "Practice cannot change physical anatomy or natural limits.", "Medium", "Evaluating", "Thematic Evaluation"),
    ("What contrast is drawn between the eagle's swoop and the raven's swoop?", "(A) The eagle's swoop was powerful, precise, and successful; the raven's was weak, clumsy, and disastrous", "(B) The raven flew higher than the eagle", "(C) The eagle failed but the raven succeeded", "(D) Both swoops were identical in strength", "(A)", "Eagle: powerful and precise. Raven: weak and disastrous.", "Medium", "Comparing", "Contrast"),
    ("Why did the raven's talons get tangled in the sheep's wool?", "(A) His small claws could not grasp the heavy skin and got trapped in thick, dense fleece", "(B) The sheep was wearing sticky glue", "(C) The shepherd tied the claws with string", "(D) The raven intentionally dug into the wool", "(A)", "Small claws trapped in dense wool fleece.", "Medium", "Understanding", "Physical Mechanism"),
    ("What lesson does the raven's injury teach about self-acceptance?", "(A) Value your unique abilities rather than causing self-harm by foolishly trying to be someone else", "(B) Always try to fly higher than eagles", "(C) Never look at sheep in a valley", "(D) Injuries make you stronger next time", "(A)", "Value unique abilities instead of imitating others.", "Medium", "Evaluating", "Moral Interpretation"),
    ("How did the raven's environment (valley vs mountains) reflect his status?", "(A) Living in the valley symbolized lower status and modest ability compared to the majestic mountain-dwelling eagle", "(B) The valley was dangerous, but mountains were safe", "(C) The valley had no food at all", "(D) The mountain was smaller than the valley", "(A)", "Valley = modest status. Mountain = majestic power.", "Medium", "Analyzing", "Setting Symbolism"),
    ("What cognitive mistake did the raven make when observing the eagle?", "(A) He focused only on the eagle's glorious result (carrying sheep) and ignored the immense strength required", "(B) He thought the eagle was a small insect", "(C) He believed the sheep gave up willingly", "(D) He thought the eagle flew backwards", "(A)", "Focused on glorious result, ignored physical strength required.", "Medium", "Analyzing", "Cognitive Error"),
    ("Why did the raven's plan fail despite waiting for an 'opportune time'?", "(A) Perfect timing cannot compensate for a total lack of physical capability", "(B) The shepherd saw him from ten miles away", "(C) The sheep ran away before he landed", "(D) Rain started falling suddenly", "(A)", "Timing cannot compensate for lack of capability.", "Medium", "Evaluating", "Logical Analysis"),
    ("What emotion did the raven experience while lying injured on the ground?", "(A) Humiliation, pain, and regret over his foolish ambition", "(B) Pride in his grand attempt", "(C) Happiness that he touched a sheep", "(D) Anger at the eagle for not helping", "(A)", "Humiliation, pain, and regret.", "Medium", "Analyzing", "Character Emotion"),
    ("How does Aesop use animal fables to deliver moral instruction?", "(A) By using animal behaviors to personify human flaws like envy, vanity, and blind imitation", "(B) By teaching biology and zoology facts", "(C) By encouraging children to hunt wild animals", "(D) By explaining how birds build nests", "(A)", "Uses animal behaviors to personify human flaws.", "Medium", "Evaluating", "Fable Mechanics"),
    ("What advice would you give to someone who envies others like the raven did?", "(A) Focus on developing your own strengths and talents instead of copying others recklessly", "(B) Try harder to copy them until you succeed", "(C) Hide away and never work", "(D) Blame others for your weakness", "(A)", "Develop your own strengths instead of copying others.", "Medium", "Applying", "Real-World Application"),
    ("What literary device is present when the raven imagines becoming famous from catching a fat sheep?", "(A) Hubris / Overconfidence preceding a fall", "(B) Onomatopoeia", "(C) Alliteration", "(D) Personification of the mountain", "(A)", "Hubris / Overconfidence preceding a fall.", "Medium", "Analyzing", "Literary Device"),

    # Hard (41-50)
    ("Critique the raven's failure from an evolutionary adaptation perspective.", "(A) The raven's anatomy evolved for scavenging and small feeding, making predatory lifting mechanically impossible", "(B) The raven simply needed a better diet to grow larger claws", "(C) The sheep evolved armor to defeat ravens", "(D) Evolutionary traits change within two weeks of practice", "(A)", "Anatomy evolved for scavenging, not heavy predatory lifting.", "Hard", "Evaluating", "HOTS Cross-Disciplinary Critique"),
    ("Deconstruct the tragicomic tone of the fable during the raven's attack.", "(A) The grand contrast between the raven's noble expectations of glory and the ridiculous reality of getting stuck in wool", "(B) The story is purely tragic with no lesson", "(C) The story is a slapstick comedy about farming", "(D) The tone is terrifying and horror-filled", "(A)", "Grand expectation of glory vs ridiculous reality of tangled claws.", "Hard", "Analyzing", "Tone Analysis"),
    ("Evaluate the psychological motivation of envy in driving self-destructive actions.", "(A) Envy blinds individuals to personal limitations, causing reckless endeavors that result in self-inflicted harm", "(B) Envy always leads to success if practiced for a fortnight", "(C) Envy is a positive trait in all fables", "(D) Envy only affects birds, not humans", "(A)", "Envy blinds to limitations, causing self-destructive actions.", "Hard", "Evaluating", "Psychological Evaluation"),
    ("Compare the raven's foolishness in Chapter 02 with Someshwar's foolishness in Book 3 Chapter 01.", "(A) Both characters let doubt/vanity blind them to physical danger — Someshwar revived a lion, the raven attacked a heavy sheep", "(B) Both characters were successful leaders", "(C) Neither character made any mistake", "(D) Both stories take place in ocean waters", "(A)", "Both let vanity/impulse blind them to physical danger.", "Hard", "Comparing", "Comparative Fable Analysis"),
    ("Formulate an alternative outcome where the raven demonstrates wisdom.", "(A) 'Observing the eagle, the raven appreciated the majestic sight but recognized his own gifts of agility and cleverness, flying happily across the valley.'", "(B) 'The raven called ten eagles to lift the sheep together.'", "(C) 'The raven stole the shepherd's hat instead.'", "(D) 'The raven became the ruler of the mountains.'", "(A)", "Demonstrates self-awareness and appreciation of unique gifts.", "Hard", "Creating", "Alternative Narrative Creation"),
    ("Assess the pedagogical value of teaching 'Do not imitate others blindly' to 10-year-olds.", "(A) Promotes self-worth, discourages negative peer pressure, and encourages authentic personal growth", "(B) Teaches children never to learn new skills", "(C) Encourages children to ignore teachers", "(D) Prevents students from participating in sports", "(A)", "Promotes self-worth, discourages peer pressure, encourages authentic growth.", "Hard", "Evaluating", "Pedagogical Assessment"),
    ("Analyze the structural function of the fortnight practice period in the plot.", "(A) Highlights deliberate hubris; his failure was not due to lack of effort, but fundamental impossibility", "(B) Shows that the raven was lazy", "(C) Proves that two weeks is equal to one year", "(D) Serves no purpose in the narrative", "(A)", "Highlights deliberate hubris — failure despite effort proves impossibility.", "Hard", "Analyzing", "Structural Plot Function"),
    ("Synthesize how Chapter 02 develops critical reading comprehension skills in Class 5.", "(A) Combines fable analysis, vocabulary in context, character flaw evaluation, and moral deduction", "(B) Teaches only spelling memorization", "(C) Replaces prose with mathematical equations", "(D) Focuses exclusively on drawing pictures", "(A)", "Combines fable analysis, vocabulary, character evaluation, and moral deduction.", "Hard", "Synthesizing", "Curricular Synthesis"),
    ("Critique the shepherd's reaction from a moral standpoint.", "(A) Throwing the raven roughly reflects a farmer protecting livestock from perceived pests, delivering harsh natural justice", "(B) The shepherd should have crowned the raven king", "(C) The shepherd acted out of pure malice toward all wild life", "(D) The shepherd was wrong to save his own sheep", "(A)", "Protecting livestock, delivering harsh natural justice to an intruder.", "Hard", "Evaluating", "Moral Critique"),
    ("Formulate a high-level discussion prompt based on Chapter 02 for a Class 5 classroom.", "(A) 'Can practice overcome any limitation, or are there boundaries where wisdom means accepting who we are? Discuss with examples.'", "(B) 'How many feathers does a raven have?'", "(C) 'What is the weight of an average sheep?'", "(D) 'Spell the word raven ten times.'", "(A)", "High-level philosophical prompt balancing effort vs realistic capability.", "Hard", "Creating", "Discussion Prompt Design")
]

mcq_content = f"# MCQs — Chapter 02: The Raven that Wanted to be an Eagle\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH02_MCQ_{idx:03d}"
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

with open(os.path.join(CH02_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("There lived an unhappy raven in a _______.", "valley", "Lived a raven in a valley.", "Easy"),
    ("High up in the mountains there lived an _______.", "eagle", "Eagle lived in the mountains.", "Easy"),
    ("The eagle swooped down from great heights with great _______.", "precision", "Swooped down with great precision.", "Easy"),
    ("The raven admired the eagle and wanted to be exactly like _______.", "him", "Wanted to be like him.", "Easy"),
    ("The raven found himself to be very _______ compared to the eagle.", "simple", "Found himself to be very simple.", "Easy"),
    ("One day, the eagle swooped down and carried away a _______ from the flock.", "sheep", "Carried away a sheep.", "Easy"),
    ("The raven became impatient to become like the _______.", "eagle", "Impatient to become like the eagle.", "Easy"),
    ("The raven practiced flying and swooping for a _______.", "fortnight", "Practiced for a fortnight.", "Easy"),
    ("He waited for the _______ to arrive with the flock of sheep.", "shepherd", "Waited for the shepherd.", "Easy"),
    ("The raven chose the _______ sheep of the flock as his prey.", "fattest", "Chose the fattest sheep.", "Easy"),
    ("The raven thought tales of his _______ would travel in all directions.", "feat", "Tales of his feat.", "Easy"),
    ("At the opportune time, the raven swooped down on the chosen _______.", "sheep", "Swooped down on the chosen sheep.", "Easy"),
    ("The raven clutched on the sheep's body and tried to fly away in _______.", "vain", "Tried to fly away in vain.", "Easy"),
    ("His _______ got stuck in the thick hair on the sheep.", "talons", "Talons got stuck in thick hair.", "Easy"),
    ("The shepherd pulled away the raven from the _______.", "sheep", "Pulled away from the sheep.", "Easy"),
    ("The shepherd threw the raven roughly on the _______.", "ground", "Threw it roughly on the ground.", "Easy"),
    ("The raven got _______ and could not fly for many days.", "injured", "Got injured and could not fly.", "Easy"),
    ("The moral of the story is: Do not _______ others blindly.", "imitate", "Do not imitate others blindly.", "Easy"),
    ("To swoop means to fly down _______.", "suddenly", "Swoop means fly down suddenly.", "Easy"),
    ("Precise means clear and _______.", "accurate", "Precise means clear and accurate.", "Easy"),
    ("A feat is an action showing great _______.", "skill", "Feat shows great skill.", "Easy"),
    ("Opportune means a _______ moment.", "suitable", "Opportune means a suitable moment.", "Easy"),
    ("A fortnight is a period of _______ weeks.", "two", "Fortnight means two weeks.", "Easy"),
    ("Talons are the _______ of a bird of prey.", "claws", "Talons are claws.", "Easy"),
    ("Chapter 02 is an Aesop _______.", "Fable", "Chapter 02 is an Aesop Fable.", "Easy"),

    # Medium (26-40)
    ("The raven's envy clouded his practical _______.", "judgment", "Envy clouded judgment.", "Medium"),
    ("Blind imitation without strength leads to severe _______.", "failure", "Leads to severe failure.", "Medium"),
    ("The sheep's dense _______ trapped the raven's claws.", "wool", "Dense wool trapped claws.", "Medium"),
    ("The raven sought personal _______ by attacking the fattest sheep.", "glory", "Sought personal glory.", "Medium"),
    ("Two weeks of practice could not change the raven's physical _______.", "anatomy", "Could not change physical anatomy.", "Medium"),
    ("The eagle operated with natural predatory _______.", "instinct", "Operated with predatory instinct.", "Medium"),
    ("The shepherd intervened to protect his livestock from _______.", "harm", "Protected livestock from harm.", "Medium"),
    ("The raven learned a painful lesson about overestimating his _______.", "abilities", "Overestimating abilities.", "Medium"),
    ("Vanity blinded the raven to the obvious _______ of his plan.", "danger", "Blinded to obvious danger.", "Medium"),
    ("Each bird species possesses distinct physical _______.", "adaptations", "Possesses distinct physical adaptations.", "Medium"),
    ("The eagle's aerial maneuver inspired deep _______ in the raven.", "envy", "Inspired deep envy.", "Medium"),
    ("Attempts to perform impossible tasks result in wasted _______.", "effort", "Result in wasted effort.", "Medium"),
    ("Fables use animal stories to deliver practical moral _______.", "lessons", "Deliver practical moral lessons.", "Medium"),
    ("The raven's grounded condition symbolized his lost _______.", "pride", "Symbolized lost pride.", "Medium"),
    ("True wisdom lies in understanding one's own natural _______.", "limits", "Understanding natural limits.", "Medium"),

    # Hard (41-50)
    ("Overconfidence before a tragic fall exemplifies literary _______.", "hubris", "Exemplifies literary hubris.", "Hard"),
    ("Physical limitations render grand ambitions completely _______.", "futile", "Render ambitions futile.", "Hard"),
    ("The narrative contrasts majestic mountain power with valley _______.", "modesty", "Contrasts with valley modesty.", "Hard"),
    ("Blindly copying others exposes an individual to public _______.", "humiliation", "Exposes to public humiliation.", "Hard"),
    ("Biological realities cannot be overcome by sheer _______.", "desire", "Cannot be overcome by desire.", "Hard"),
    ("The shepherd's action delivered swift natural _______.", "justice", "Delivered natural justice.", "Hard"),
    ("Self-acceptance protects individuals from self-inflicted _______.", "injury", "Protects from self-inflicted injury.", "Hard"),
    ("The raven's entangled talons represent the trap of foolish _______.", "vanity", "Trap of foolish vanity.", "Hard"),
    ("Aesop's fables caution society against unchecked _______.", "arrogance", "Caution against unchecked arrogance.", "Hard"),
    ("Chapter 02 integrates fable analysis, vocabulary, and moral _______.", "reasoning", "Integrates moral reasoning.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 02: The Raven that Wanted to be an Eagle\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH02_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH02_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The raven lived high up in the mountains with the eagle.", "False", "The raven lived in the valley, while the eagle lived high up in the mountains.", "Easy"),
    ("The eagle swooped down from great heights with great precision.", "True", "Text states the eagle swooped down from great heights with great precision.", "Easy"),
    ("The raven was completely satisfied with his simple life.", "False", "The raven was an unhappy raven because he envied the eagle.", "Easy"),
    ("The eagle carried away a sheep from the flock in front of everyone.", "True", "The eagle swooped down and carried away a sheep from the flock.", "Easy"),
    ("The raven practiced swooping like an eagle for a fortnight.", "True", "He practiced flying and swooping for a fortnight (14 days).", "Easy"),
    ("The raven chose the smallest, thinnest sheep as his prey.", "False", "The raven chose the fattest sheep of the flock as his prey.", "Easy"),
    ("The raven wanted to catch a fat sheep so tales of his feat would travel in all directions.", "True", "He thought tales of his feat would travel in all directions.", "Easy"),
    ("The raven successfully flew away to his nest with the fat sheep.", "False", "He could not lift the sheep and his talons got stuck in its thick hair.", "Easy"),
    ("The raven's talons got stuck in the thick hair on the sheep.", "True", "His talons got stuck in the thick hair on the sheep.", "Easy"),
    ("The eagle came to help the raven get unstuck from the sheep.", "False", "The shepherd came and pulled the raven away.", "Easy"),
    ("The shepherd threw the raven roughly on the ground.", "True", "The shepherd pulled him off and threw him roughly on the ground.", "Easy"),
    ("The raven got injured and could not fly for many days.", "True", "The raven got injured and could not fly for many days.", "Easy"),
    ("The moral of the story is 'Do not imitate others blindly'.", "True", "Moral stated at the end: Do not imitate others blindly.", "Easy"),
    ("'Swoop' means to fly down slowly and land gently.", "False", "Swoop means to fly down suddenly and swiftly.", "Easy"),
    ("'Precise' means clear, exact, and accurate.", "True", "Precise means clear and accurate.", "Easy"),
    ("'Feat' means an action showing great skill or strength.", "True", "Feat means an action showing great skill.", "Easy"),
    ("'Opportune' means a very bad time to do something.", "False", "Opportune means a suitable or favorable moment.", "Easy"),
    ("'Fortnight' means a period of two full months.", "False", "Fortnight means a period of two weeks (14 days).", "Easy"),
    ("The raven was able to outrun the shepherd on foot.", "False", "He was pulled off the sheep by the shepherd and thrown down.", "Easy"),
    ("The raven's ambition was driven by vanity and envy.", "True", "He envied the eagle and wanted glory for catching a fat sheep.", "Easy"),
    ("The sheep was severely injured by the raven.", "False", "The raven could not hurt the sheep; its claws just got stuck in wool.", "Easy"),
    ("Chapter 02 is a fable written by Aesop.", "True", "It is subtitled '-An Aesop Fable'.", "Easy"),
    ("The raven changed his color to white after practicing for a fortnight.", "False", "Practicing did not change his physical appearance or power.", "Easy"),
    ("The raven enjoyed being thrown on the ground by the shepherd.", "False", "He was injured and suffered pain and humiliation.", "Easy"),
    ("Chapter 02 is titled 'The Raven that Wanted to be an Eagle'.", "True", "Chapter 02 title is 'The Raven that Wanted to be an Eagle'.", "Easy"),

    # Medium (26-40)
    ("The raven failed because he did not practice swooping enough times.", "False", "He failed because a raven physically lacks the strength and claw structure to lift a sheep.", "Medium"),
    ("The eagle's successful hunt looked effortless to the observing raven.", "True", "The eagle's precision made the difficult feat look attractive to the raven.", "Medium"),
    ("The shepherd attacked the raven to protect his valuable livestock.", "True", "The shepherd pulled the raven away to save his sheep from harm.", "Medium"),
    ("A fortnight of practice can transform a small bird into a bird of prey.", "False", "Practice cannot change an animal's species, anatomy, or natural limitations.", "Medium"),
    ("The raven's desire for fame made him pick the most difficult prey possible.", "True", "Choosing the fattest sheep was driven by his desire for widespread fame.", "Medium"),
    ("The fable warns against overestimating one's physical capabilities.", "True", "It demonstrates the painful consequences of overestimating strength.", "Medium"),
    ("The raven's talons were naturally suited for lifting heavy mammals.", "False", "Raven talons are small and weak, suited for perching and scavenging, not carrying sheep.", "Medium"),
    ("The story illustrates that envy often leads to self-inflicted harm.", "True", "Envy motivated the raven's foolish attack, resulting in his injury.", "Medium"),
    ("The shepherd gave the raven a prize for trying to fly like an eagle.", "False", "The shepherd threw him roughly onto the ground, injuring him.", "Medium"),
    ("The eagle helped the raven select the fattest sheep.", "False", "The eagle had no interaction with the raven in the story.", "Medium"),
    ("The raven's grounded state after injury symbolizes his brought-down ego.", "True", "Being unable to fly for days humbled his arrogant ambition.", "Medium"),
    ("The fable suggests that everyone should try to copy successful people blindly.", "False", "The explicit moral warns: Do not imitate others blindly.", "Medium"),
    ("The raven's attack took place during the daytime in front of the flock.", "True", "He waited for the shepherd and flock to arrive during the day.", "Medium"),
    ("The fable emphasizes that self-awareness is essential for safety.", "True", "Knowing your own limits prevents dangerous mistakes.", "Medium"),
    ("The raven's inability to fly away was caused by the sheep's heavy weight and thick wool.", "True", "The heavy weight prevented lifting, and dense wool trapped his claws.", "Medium"),

    # Hard (41-50)
    ("The raven's mistake was a failure of self-evaluation rather than effort.", "True", "He put in two weeks of effort, but his underlying self-evaluation was completely wrong.", "Hard"),
    ("The narrative highlights the distinction between admiration and foolish imitation.", "True", "Admiring the eagle was fine, but blindly trying to copy it was disastrous.", "Hard"),
    ("The fable implies that glory sought through reckless vanity ends in humiliation.", "True", "Seeking fame with the fat sheep ended in being thrown to the ground.", "Hard"),
    ("The raven's physical structure adapted during the fortnight of training.", "False", "Anatomical adaptations do not occur through short-term practice.", "Hard"),
    ("The shepherd's response represents the unyielding reality of external consequences.", "True", "External reality (shepherd/ground) crushed the raven's false fantasy.", "Hard"),
    ("The eagle's absence during the raven's attack emphasizes individual responsibility.", "True", "The raven acted entirely on his own foolish choice.", "Hard"),
    ("Chapter 02 uses dramatic irony to show the contrast between fantasy and reality.", "True", "The raven envisioned glory while the reader foresees his obvious failure.", "Hard"),
    ("The moral applies equally to personal abilities, career choices, and peer pressure.", "True", "Blindly copying others in any domain without capability leads to failure.", "Hard"),
    ("The raven's injury was a temporary setback that taught a permanent lesson.", "True", "His inability to fly for days instilled a lasting moral truth.", "Hard"),
    ("Chapter 02 combines literary fable structure with practical life wisdom for Class 5.", "True", "Combines engaging narrative with essential moral development.", "Hard")
]

tf_content = f"# True / False — Chapter 02: The Raven that Wanted to be an Eagle\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH02_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH02_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Where did the raven and the eagle live respectively?", "The raven lived down in a valley, while the eagle lived high up in the mountains.", "Easy", "Remembering"),
    ("Why was the raven unhappy with his own life?", "He was unhappy because he envied the eagle's precision and strength and wished to hunt just like him.", "Easy", "Remembering"),
    ("How did the eagle hunt its prey in the valley?", "The eagle swooped down from great heights with great precision and carried away its prey effortlessly.", "Easy", "Remembering"),
    ("What dramatic event did the raven witness in the valley one day?", "He saw the eagle swoop down out of nowhere and carry away a live sheep from the grazing flock.", "Easy", "Remembering"),
    ("What did the raven do for a fortnight after watching the eagle?", "He practiced flying and swooping repeatedly to master the skills needed to hunt like an eagle.", "Easy", "Remembering"),
    ("Which sheep did the raven choose to attack and why?", "He chose the fattest sheep in the flock because he thought tales of his great feat would spread everywhere.", "Easy", "Understanding"),
    ("What happened when the raven swooped down on the fattest sheep?", "His claws (talons) got tangled and stuck in the sheep's thick wool, and he could not fly away.", "Easy", "Remembering"),
    ("Did the raven succeed in carrying away the sheep?", "No, he tried in vain to fly away with the heavy sheep but was completely stuck.", "Easy", "Remembering"),
    ("What did the shepherd do when he saw the raven on the sheep?", "The shepherd came, pulled the raven off the sheep, and threw him roughly onto the ground.", "Easy", "Remembering"),
    ("What was the raven's physical condition after the incident?", "The raven was severely injured from the fall and could not fly for many days.", "Easy", "Remembering"),
    ("What is the main moral of the fable 'The Raven that Wanted to be an Eagle'?", "The moral of the story is: 'Do not imitate others blindly.'", "Easy", "Remembering"),
    ("What does the word 'swoop' mean?", "'Swoop' means to fly down suddenly and rapidly through the air to catch something.", "Easy", "Understanding"),
    ("What does the word 'precise' mean?", "'Precise' means exact, clear, and accurate in performance or measurement.", "Easy", "Understanding"),
    ("What does the word 'feat' mean?", "'Feat' means an impressive act or achievement that demonstrates great skill or strength.", "Easy", "Understanding"),
    ("What does the word 'opportune' mean?", "'Opportune' means particularly suitable, convenient, or favorable for a specific action.", "Easy", "Understanding"),
    ("What does the word 'fortnight' mean?", "'Fortnight' means a period of fourteen consecutive days (two weeks).", "Easy", "Understanding"),
    ("What body part of the raven proved useless for lifting a sheep?", "His small, weak talons (claws), which were meant for perching rather than carrying heavy prey.", "Easy", "Understanding"),
    ("Why could the raven not outrun or escape from the shepherd?", "His claws were tangled deep in the sheep's wool, holding him trapped on the animal's back.", "Easy", "Understanding"),
    ("How long was the raven unable to fly after his injury?", "He was unable to fly for many days.", "Easy", "Remembering"),
    ("Who wrote or collected this fable?", "This fable comes from the ancient collection known as Aesop's Fables.", "Easy", "Remembering"),
    ("Why did the flock of sheep get shocked when the eagle struck?", "Because the eagle swooped down suddenly from great heights with incredible speed and power.", "Easy", "Remembering"),
    ("What impulse drove the raven to attack right after his practice fortnight?", "Impatience and vanity drove him to execute his attack as soon as the shepherd arrived.", "Easy", "Understanding"),
    ("Was the raven's practice effective in changing his physical nature?", "No, practicing swooping could not change his small body size or weak claw structure.", "Easy", "Understanding"),
    ("What title is given to Chapter 02?", "The title of Chapter 02 is 'The Raven that Wanted to be an Eagle'.", "Easy", "Remembering"),
    ("What lesson did the raven learn at the end of his ordeal?", "He learned that foolishly copying a stronger creature leads only to pain, injury, and humiliation.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze why the raven's ambition was foolish from the start.", "It was foolish because he ignored basic physical differences. A raven is built for scavenging, not for lifting heavy animals like sheep.", "Medium", "Analyzing"),
    ("How did vanity cloud the raven's judgment when choosing his target?", "Instead of testing his strength on a tiny lamb, vanity made him target the fattest sheep so he could boast about a grand feat.", "Medium", "Analyzing"),
    ("Contrast the natural abilities of the eagle with those of the raven.", "The eagle has massive wings, great muscular power, and sharp, strong talons for hunting. The raven is smaller, weaker, and lacks predatory lifting power.", "Medium", "Comparing"),
    ("Why did the shepherd react roughly toward the raven?", "The shepherd saw the raven as a threat to his flock. Throwing it roughly was his way of punishing the intruder and protecting his sheep.", "Medium", "Understanding"),
    ("Explain why two weeks of practice could not make the raven hunt like an eagle.", "Practice improves skill, but it cannot alter physical anatomy. No amount of practice can give a raven the physical strength of an eagle.", "Medium", "Evaluating"),
    ("What role does the setting (mountains vs. valley) play in highlighting character status?", "The high mountains symbolize the eagle's elevated, powerful status, while the lower valley represents the raven's modest, ordinary position.", "Medium", "Analyzing"),
    ("How does the phrase 'tried in vain' describe the raven's struggle?", "It emphasizes total helplessness—despite flapping his wings frantically, his physical weakness made escape impossible.", "Medium", "Understanding"),
    ("What does the raven's physical injury represent symbolically?", "His injury symbolizes his crushed pride and humbled ego, showing that foolish arrogance brings painful downfall.", "Medium", "Analyzing"),
    ("How can Class 5 students apply the moral 'Do not imitate others blindly' in school?", "Students should focus on developing their own unique talents rather than copying peers recklessly in studies, sports, or behavior.", "Medium", "Applying"),
    ("What cognitive error did the raven make when observing the eagle?", "He focused only on the rewarding result (catching food easily) while ignoring the immense physical strength and training required.", "Medium", "Analyzing"),
    ("Why was the sheep unaffected by the raven's attack?", "The raven was too small and weak to harm the sheep; its claws merely got tangled in the sheep's thick wool layer.", "Medium", "Understanding"),
    ("How does Aesop use contrast to build the fable's lesson?", "He contrasts the eagle's smooth success with the raven's embarrassing failure to highlight the folly of blind imitation.", "Medium", "Analyzing"),
    ("What would a wise raven have done after watching the eagle?", "A wise raven would have admired the eagle's skill while continuing to hunt small food suitable for a raven's size.", "Medium", "Evaluating"),
    ("Summarize Chapter 02 in four sentences.", "An envious raven in a valley wanted to hunt like a powerful eagle. After practicing for two weeks, he swooped down to carry away the fattest sheep in a flock. His claws got tangled in the sheep's wool, and he could not fly. The shepherd caught him and threw him roughly, leaving the foolish raven injured.", "Medium", "Understanding"),
    ("What is the difference between healthy inspiration and blind imitation?", "Healthy inspiration encourages developing one's own gifts, whereas blind imitation foolishly copies others without considering personal capability.", "Medium", "Evaluating"),

    # Hard (41-50)
    ("Critique the raven's failure using principles of animal anatomy.", "Ravens possess perching feet (anisodactyl) designed for gripping branches, whereas eagles have strong raptorial feet with powerful muscles built for carrying heavy prey.", "Hard", "Evaluating"),
    ("Deconstruct the tragicomic tone during the raven's failed attack.", "The scene is tragicomic because the raven's high expectations of glory contrast absurdly with the silly reality of him getting stuck helpless in sheep wool.", "Hard", "Analyzing"),
    ("Evaluate how envy distorts self-awareness in individuals.", "Envy makes individuals focus on what others possess, blinding them to their own limitations and driving them to dangerous, unrealistic choices.", "Hard", "Evaluating"),
    ("Compare the raven's ambition with human peer pressure in modern society.", "Like people who buy things or attempt dangerous stunts just to copy popular influencers, the raven suffered harm by imitating someone out of vanity.", "Hard", "Comparing"),
    ("Formulate a continuation where the raven reflects on his mistake while recovering.", "'As he lay resting his sore wings, the raven watched smaller birds catch seeds skillfully. He realized that every bird has its own purpose, and resolved to be proud of being a clever raven.'", "Hard", "Creating"),
    ("Assess the psychological impact of public failure on character growth.", "Public failure humbles arrogance. The raven's painful landing forced him to abandon his false pretenses and accept his true nature.", "Hard", "Evaluating"),
    ("Analyze how the narrative structure builds hubris before the climax.", "The narrative builds hubris by showing the raven's detailed preparations and proud thoughts ('tales of my feat will travel'), making his sudden failure more impactful.", "Hard", "Analyzing"),
    ("Synthesize the core educational values embedded in Aesop's fables for primary students.", "Fables combine engaging animal stories with clear moral lessons, teaching critical thinking, self-awareness, modesty, and practical wisdom.", "Hard", "Synthesizing"),
    ("Critique the shepherd's action from an animal welfare vs. farm protection perspective.", "From a farm protection view, the shepherd acted reasonably to protect his flock; from an animal welfare view, throwing the bird roughly caused preventable harm.", "Hard", "Evaluating"),
    ("Formulate a 4-line poem capturing the essence of Chapter 02.", "'The raven wished to soar and slay,\nAnd steal a heavy sheep away;\nHis tangled claws brought injury,\nFor copying blindly brings misery.'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 02: The Raven that Wanted to be an Eagle\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH02_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH02_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the raven's envy of the eagle and his decision to imitate him.",
     "The raven lived down in a peaceful valley, but he was deeply unhappy with his simple life. High above in the mountains lived a majestic eagle. The raven watched with intense envy as the eagle swooped down from great heights with speed and precision, catching prey and carrying it away effortlessly. Desiring to be admired just like the eagle, the raven thought to himself that if only he could fly, hunt, and be as precise as the eagle, he would be great. Driven by this envy, he decided to imitate the eagle. He spent a full fortnight practicing flying and swooping skills in preparation for his planned attack.",
     "Easy", "Remembering"),

    ("Narrate the story of the raven's attack on the sheep and its disastrous outcome.",
     "After practicing swooping for a fortnight, the raven waited for the shepherd to bring his flock of sheep into the valley. Driven by vanity, the raven chose the fattest sheep of the flock as his target, believing that carrying away such a large prize would make tales of his skill travel in all directions. At what he thought was an opportune moment, he swooped down and clutched the sheep's back. However, his small talons got tangled in the sheep's dense, thick wool. He flapped his wings frantically, trying in vain to fly away, but he was completely stuck. The shepherd walked over, pulled the raven off the sheep, and threw him roughly onto the ground, injuring him severely.",
     "Easy", "Remembering"),

    ("Explain the moral lesson 'Do not imitate others blindly' as demonstrated in Chapter 02.",
     "The moral lesson 'Do not imitate others blindly' warns against copying the actions or lifestyles of others without considering one's own limitations. In Chapter 02, the raven admired the eagle's hunting ability and tried to copy him without realizing that he lacked the eagle's physical size, strength, and talon structure. His foolish attempt to carry off a fat sheep ended in failure, physical injury, and humiliation. The story teaches that everyone has unique capabilities, and trying to blindly copy someone else can lead to self-harm.",
     "Easy", "Understanding"),

    ("Explain the vocabulary words from Chapter 02: Swoop, Precise, Feat, Opportune, and Fortnight.",
     "1. **Swoop**: To fly down suddenly and rapidly through the air. *Sentence*: The eagle swooped down to catch its prey.\n2. **Precise**: Exact, clear, and accurate. *Sentence*: The eagle caught the sheep with precise timing.\n3. **Feat**: An action showing extraordinary skill or strength. *Sentence*: The raven thought catching a fat sheep would be a great feat.\n4. **Opportune**: A suitable or favorable moment. *Sentence*: The raven waited for an opportune time to attack.\n5. **Fortnight**: A period of two weeks (14 days). *Sentence*: The raven practiced swooping for a fortnight.",
     "Easy", "Understanding"),

    ("How did the raven's vanity lead directly to his downfall?",
     "Vanity corrupted the raven's practical judgment. Had he attempted to catch a tiny insect or a small crumb, he might not have suffered physical harm. However, vanity convinced him that catching a small target would not win him fame. He deliberately selected the fattest, heaviest sheep in the flock because he wanted everyone to praise his impressive achievement. This extreme overconfidence blinded him to his physical weakness, resulting in his claws getting trapped and leading directly to his painful injury.",
     "Easy", "Analyzing"),

    ("Describe the role of the shepherd in Chapter 02.",
     "The shepherd represents the owner and protector of the flock. He observed the raven's foolish attempt to steal his fattest sheep. When he saw the raven struggling and stuck in the wool, he intervened immediately. He pulled the bird off the sheep to protect his animal and threw the raven roughly to the ground to punish the intruder. His action brought the raven's foolish fantasy to an abrupt, painful end.",
     "Easy", "Understanding"),

    ("What contrast does the fable draw between physical reality and foolish desire?",
     "The fable contrasts the reality of biological limits with the foolishness of unchecked desire. Desire made the raven believe that two weeks of swooping practice could make him as strong as an eagle. However, physical reality proved that a raven's small body, weak wing muscles, and slender claws cannot lift a heavy mammal. Reality defeated desire the moment his claws got tangled in the wool.",
     "Easy", "Analyzing"),

    ("Discuss how Chapter 02 teaches children about self-worth and self-acceptance.",
     "Chapter 02 teaches children that every individual has unique strengths and limitations. The raven was unhappy simply because he compared himself to the eagle instead of appreciating his own gifts as a raven. The story encourages young readers to embrace self-acceptance, build upon their personal talents, and avoid damaging their self-worth through negative comparisons with peers.",
     "Easy", "Evaluating"),

    ("Summarize the entire fable of 'The Raven that Wanted to be an Eagle' in five bullet points.",
     "- An envious raven living in a valley admired a mountain eagle's impressive hunting skills.\n- The raven practiced swooping for a fortnight, wishing to hunt just like the eagle.\n- He foolishly chose the fattest sheep in a grazing flock to gain widespread fame.\n- Upon swooping down, his claws got tangled in the sheep's thick wool, leaving him trapped.\n- The shepherd pulled him off and threw him down, leaving the raven injured and teaching him not to imitate others blindly.",
     "Easy", "Understanding"),

    ("How does the setting of the story enhance the contrast between the raven and the eagle?",
     "The setting places the eagle high up in the majestic mountains and the raven down in the low valley. The lofty mountains represent high achievement, strength, and dominance, while the valley represents modest, ground-level living. This geographical separation visually reinforces the vast gap in strength and status between the two birds.",
     "Easy", "Analyzing"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why did the raven think two weeks of practice would make him as strong as an eagle?", "The raven suffered from naive overconfidence. He believed that flying technique was the only secret to the eagle's success. He failed to understand that the eagle's power came from millions of years of anatomical evolution, wing muscle density, and specialized talon structure, which practice alone cannot create.", "Easy", "Understanding"),
    ("Explain the physical mechanism that caused the raven to get stuck on the sheep.", "The raven's talons are adapted for perching on branches, with slender, curved claws. When he slammed into the sheep's dense, curly wool fleece, his claws penetrated deep into the thick fibers. Lacking the muscular strength to tear through or pull out, the wool wrapped around his claws like a net, locking him in place.", "Easy", "Understanding"),
    ("How does Aesop's use of animal characters make moral lessons easier for children to digest?", "Animals simplify complex human flaws. By embodying envy and vanity in a raven, children can objectively observe the folly of bad choices without feeling personally attacked. The clear cause-and-effect structure makes the moral lesson memorable and easy to apply.", "Easy", "Evaluating"),
    ("Describe the emotional arc of the raven from envy to practice, attack, and injury.", "The raven begins in envious discontent, moves into enthusiastic determination during his fortnight of practice, reaches a peak of vain excitement during his attack, plunges into panic when stuck, and ends in physical pain and humbled regret on the ground.", "Easy", "Analyzing"),
    ("Why did the shepherd throw the raven roughly on the ground instead of keeping it?", "The shepherd viewed the raven as a predatory nuisance attempting to harm his livestock. He threw it down roughly to punish the bird and deter any future attacks on his flock, acting out of protective duty as a livestock owner.", "Easy", "Understanding"),
    ("What advice would you give to a classmate who constantly tries to copy others?", "I would advise them to identify their own unique interests and talents. Copying others prevents personal growth and can lead to embarrassing failures. Developing one's authentic abilities brings true satisfaction and respect.", "Easy", "Applying"),
    ("How does the story demonstrate that overestimating one's ability leads to humiliation?", "The raven boasted in his mind that catching a fat sheep would make his name famous across all directions. Instead of fame, his overestimation resulted in him getting tangled helplessly and being tossed aside by a shepherd, replacing expected glory with public humiliation.", "Easy", "Analyzing"),
    ("Explain how the fable highlights the difference between appearance and reality.", "Appearance: Swooping looked simple and easy when performed by the majestic eagle. Reality: Swooping onto heavy prey required immense muscular strength and specialized claws that the raven completely lacked.", "Easy", "Analyzing"),
    ("What role does the sheep play in the fable's conflict?", "The sheep acts as a passive physical barrier. Its thick wool and heavy weight naturally defeat the raven without the sheep even needing to fight back, proving that the raven was defeated by his own choice rather than a battle.", "Easy", "Understanding"),
    ("How does Chapter 02 build vocabulary skills in Class 5 students?", "It introduces rich, descriptive vocabulary such as 'swoop', 'precise', 'feat', 'opportune', and 'fortnight', teaching students how precise word choice enhances narrative storytelling.", "Easy", "Understanding"),
    ("Re-write Chapter 02 from the perspective of the eagle watching from the mountain.", "'From my mountain perch, I saw the little black raven trying to copy my swoop. I watched him plunge toward a massive sheep. When his tiny claws got tangled in the fleece, I shook my head. He forgot that to hunt like an eagle, one must have the heart and claws of an eagle.'", "Easy", "Creating"),
    ("Discuss how envy ruins personal peace of mind as illustrated by the raven.", "The raven lived in a pleasant valley with plenty of food, yet he was perpetually unhappy because he spent his time staring up at the eagle. Envy prevented him from enjoying his own life, driving him into unnecessary danger.", "Easy", "Evaluating"),
    ("What does the phrase 'tales of my feat would travel in all directions' reveal about the raven?", "It reveals his intense desire for public validation and fame. He was not hunting out of hunger, but out of vanity to impress others and elevate his social standing.", "Easy", "Analyzing"),
    ("How does Chapter 02 fit into the overall Class 5 English literature curriculum?", "It provides classical fable literature that balances realistic fiction, developing students' ability to analyze character flaws, comprehend figurative language, and extract universal ethical morals.", "Easy", "Understanding"),
    ("What is the significance of the raven being unable to fly for many days after the fall?", "His temporary flightlessness serves as a physical reminder of his moral error. Being forced to stay grounded compelled him to reflect on his foolishness and accept his true identity as a valley bird.", "Easy", "Analyzing"),

    # Medium (26-40)
    ("Critically analyze the concept of 'blind imitation' as portrayed in Aesop's fable.",
     "Blind imitation occurs when an individual copies the superficial actions of another without understanding the underlying requirements, capabilities, or consequences. In Chapter 02, the raven saw the eagle's successful outcome but failed to comprehend the anatomical power required. He copied the flight motion blindly. The fable illustrates that blind imitation stems from superficial observation and envy, inevitably leading to failure because it ignores fundamental individual differences.",
     "Medium", "Analyzing"),

    ("Examine how the author uses cause-and-effect relationships to structure the plot.",
     "The plot is built on a tight cause-and-effect chain:\n1. Cause: Envy of eagle → Effect: Fortnight of swooping practice.\n2. Cause: Vanity for fame → Effect: Target chosen is the fattest sheep.\n3. Cause: Small claws vs thick wool → Effect: Talons trapped in fleece.\n4. Cause: Inability to lift heavy weight → Effect: Shepherd catches and throws raven.\n5. Cause: Rough landing → Effect: Injury and inability to fly for days.",
     "Medium", "Analyzing"),

    ("Evaluate the psychological difference between healthy ambition and reckless hubris.",
     "Healthy ambition involves setting challenging goals while recognizing personal starting points and working methodically within realistic boundaries. Reckless hubris involves arrogant overconfidence that ignores reality and safety for quick glory. The raven demonstrated hubris—he assumed two weeks of practice entitled him to conquer a heavy sheep, mistaking reckless arrogance for genuine capability.",
     "Medium", "Evaluating"),

    ("Discuss the symbolic meaning of the raven's injured wings in the story's resolution.",
     "The injured wings carry strong symbolic weight. Wings represent freedom, mobility, and bird identity. By attempting to fly beyond his natural station out of vanity, the raven temporarily lost the very thing that made him a bird—his ability to fly. His grounded state symbolizes how foolish arrogance strips away existing gifts and humbles the ego.",
     "Medium", "Analyzing"),

    ("Design a creative writing prompt for Class 5 students based on the fable's moral.",
     "Prompt: 'Imagine a animal that tried to copy another animal's special talent (like a monkey trying to swim like a fish, or a frog trying to roar like a lion). Write a short fable describing their attempt, the outcome, and the lesson they learned.'",
     "Medium", "Creating"),

    ("How does the shepherd's role reflect the enforcement of natural boundaries?", "The shepherd represents external reality enforcing natural boundaries. When the raven breached physical limits by attacking farm livestock, the shepherd's swift intervention restored the natural order, demonstrating that foolish actions encounter firm real-world resistance.", "Medium", "Evaluating"),
    ("Compare the raven's mistake with a real-life situation involving peer pressure.", "A student might see an expert athlete perform an advanced stunt and try to copy it without training, resulting in severe physical injury. Both situations stem from copying outcomes without possessing requisite preparation.", "Medium", "Applying"),
    ("Analyze how the word 'opportune' is used ironically in the story.", "The raven thought the timing was 'opportune' (perfect) for his triumph. Ironically, it was actually the worst possible moment because attacking a sheep guaranteed his claws would get trapped, turning an 'opportune' moment into a disaster.", "Medium", "Analyzing"),
    ("Explain why self-awareness is considered a core life skill in primary education.", "Self-awareness allows children to recognize their personal strengths, accept limitations, set realistic goals, and resist harmful peer pressure, ensuring healthy emotional development and physical safety.", "Medium", "Evaluating"),
    ("How does the narrative convey the passivity of the sheep during the attack?", "The sheep remains entirely passive, unaware of the raven's grand scheme. Its thick wool naturally traps the bird without any effort, emphasizing that the raven was defeated by his own foolish choice rather than a battle.", "Medium", "Analyzing"),
    ("Describe how Aesop establishes character motivation in the first paragraph.", "Aesop immediately establishes motivation by contrasting the raven's valley life with the eagle's mountain heights, explicitly describing the raven's inner thoughts of envy and desire to be admired.", "Medium", "Analyzing"),
    ("Evaluate the effectiveness of using a 'fortnight' as the practice duration.", "A fortnight (14 days) is long enough to show deliberate effort, proving the raven was committed, yet short enough to emphasize that practice cannot alter biological reality.", "Medium", "Evaluating"),
    ("How can educators use Chapter 02 to foster self-esteem in students?", "Educators can guide students to identify their individual talents (art, writing, empathy) and celebrate unique traits rather than measuring self-worth against others' achievements.", "Medium", "Applying"),
    ("Deconstruct the title 'The Raven that Wanted to be an Eagle'.", "The title succinctly summarizes the core conflict: identity dissonance. 'The Raven' states who he is; 'Wanted to be an Eagle' states his impossible, envious desire that drives the entire tragedy.", "Medium", "Analyzing"),
    ("Construct an alternative scene where the raven asks the eagle for advice.", "'The raven flew to the mountain peak and asked, 'Eagle, teach me to hunt sheep!' The eagle replied kindly, 'Little raven, my heavy claws were made for sheep, but your nimble beak is made for seeds and insects. Master your own nature, for that is true wisdom.''", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the philosophical dilemma between striving for self-improvement and accepting limits.",
     "The fable presents a subtle philosophical boundary. Striving for self-improvement is positive when aligned with personal potential. However, when ambition ignores fundamental biological or physical limits and is driven by vanity, it becomes destructive hubris. True wisdom lies in discerning the difference between achievable growth and impossible fantasy.",
     "Hard", "Evaluating"),

    ("Deconstruct the literary archetype of the 'Icarus Fall' in Chapter 02.",
     "Like the Greek myth of Icarus who flew too close to the sun on artificial wings, the raven attempts an elevated flight beyond his nature. Both characters experience temporary exhilaration followed by an inevitable, catastrophic fall to the ground, serving as universal archetypes warning against overreaching pride.",
     "Hard", "Analyzing"),

    ("Synthesize the stylistic features of Aesop's fables present in Chapter 02.",
     "1. **Brevity**: Concise, fast-paced storytelling without unnecessary description.\n2. **Anthropomorphism**: Animal characters exhibiting human emotions (envy, vanity).\n3. **Binary Contrast**: High mountain eagle vs low valley raven.\n4. **Explicit Moral**: Concluding sentence summarizing the ethical takeaway.",
     "Hard", "Synthesizing"),

    ("Formulate a assessment rubric for evaluating Class 5 student essays on Chapter 02.",
     "- **Fable Comprehension (25%)**: Accurate detail recall and plot sequencing.\n- **Character Analysis (25%)**: Explaining the raven's envy, vanity, and cognitive errors.\n- **Vocabulary Usage (25%)**: Correct application of terms like 'swoop', 'precise', 'feat'.\n- **Moral Application (25%)**: Relating 'Do not imitate blindly' to real-life personal choices.",
     "Hard", "Creating"),

    ("Evaluate how Chapter 02 addresses cognitive dissonance in character behavior.", "The raven experienced cognitive dissonance between his modest reality and his grand fantasy. To resolve it, he convinced himself that two weeks of swooping practice made him an eagle's equal, rationalizing a fatal choice.", "Hard", "Evaluating"),

    ("Compare the raven's motivation with the jackal's motivation in Chapter 02 of Book 3.", "Both characters suffered from faulty reasoning: the jackal assumed drum noise was food due to greed; the raven assumed he could lift a sheep due to vanity. Both failed to verify reality before committing effort.", "Hard", "Comparing"),
    ("Discuss the ethical implications of livestock management as depicted by the shepherd.", "The shepherd acted out of protective duty toward his domestic flock. His decisive intervention underscores the human responsibility to safeguard vulnerable animals from predatory threats.", "Hard", "Evaluating"),
    ("Analyze how the narrative uses irony in the raven's expectation of 'tales of my feat'.", "The raven expected tales of his glory to travel everywhere. Ironically, tales of his embarrassing failure and tangled claws became the famous fable passed down for centuries as a warning against folly.", "Hard", "Analyzing"),
    ("Draft an analytical critique of the line: 'His talons got stuck in the thick hair on the sheep.'", "This sentence marks the tragicomic climax. The word 'stuck' strips away all majestic pretenses of the attack, reducing the raven's grand ambition to a helpless, comical entanglement in sheep fleece.", "Hard", "Evaluating"),
    ("Synthesize the ultimate pedagogical value of Chapter 02 for primary school literature.", "Chapter 02 seamlessly merges language development with character education, teaching children that authentic self-worth comes from accepting who we are rather than blindly imitating others.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 02: The Raven that Wanted to be an Eagle\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH02_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH02_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Once upon a time, there lived a raven in a valley. He was an unhappy raven. This is because high up in the mountains there lived an eagle. The eagle swooped down from great heights and with great precision, caught the prey and carried it away.",
     [
         ("Where did the raven live?", "In a valley.", "Easy", "Remembering"),
         ("Where did the eagle live?", "High up in the mountains.", "Easy", "Remembering"),
         ("Why was the raven unhappy?", "He envied the eagle's precision and strength in catching prey.", "Easy", "Remembering"),
         ("How did the eagle catch its prey?", "Swooped down from great heights with great precision.", "Easy", "Remembering"),
         ("What does the word 'precision' mean in this passage?", "Clear, exact, and accurate performance.", "Easy", "Understanding")
     ]),

    # Set 2
    ("The raven admired the eagle and wanted to be exactly like him but found himself to be very simple. 'Only if I could fly like the eagle, only if I could hunt like the eagle, only if I could be as precise as the eagle', he kept on thinking and wishing.",
     [
         ("Who did the raven admire?", "The eagle.", "Easy", "Remembering"),
         ("How did the raven view himself compared to the eagle?", "He found himself to be very simple.", "Easy", "Remembering"),
         ("What three things did the raven wish he could do like the eagle?", "Fly like the eagle, hunt like the eagle, and be as precise as the eagle.", "Easy", "Remembering"),
         ("What emotion drove the raven's repeated wishing?", "Envy and dissatisfaction with his own modest life.", "Medium", "Understanding"),
         ("What does this extract reveal about the raven's character flaw?", "He was obsessed with imitating someone else instead of appreciating himself.", "Medium", "Analyzing")
     ]),

    # Set 3
    ("One day, the raven was eagerly waiting for the eagle to come. He could see a lot of sheep grazing in the valley. Suddenly, out of nowhere, the eagle swooped down and carried away a sheep from the flock much to everyone's shock.",
     [
         ("What was the raven waiting for?", "He was eagerly waiting for the eagle to come.", "Easy", "Remembering"),
         ("What were the sheep doing in the valley?", "They were grazing in the valley.", "Easy", "Remembering"),
         ("What did the eagle do suddenly?", "Swooped down out of nowhere and carried away a sheep.", "Easy", "Remembering"),
         ("How did everyone react to the eagle's attack?", "Much to everyone's shock.", "Easy", "Remembering"),
         ("Find a word in the extract that means 'eating grass in a field'.", "Grazing.", "Easy", "Understanding")
     ]),

    # Set 4
    ("Now the raven became impatient to become like the eagle. He started flying and swooping like the eagle. After a fortnight when he thought that he had mastered all needed skills, he decided to carry out the attack.",
     [
         ("How did the raven feel after watching the eagle's hunt?", "He became impatient to become like the eagle.", "Easy", "Remembering"),
         ("What skills did the raven start practicing?", "Flying and swooping like an eagle.", "Easy", "Remembering"),
         ("How long did the raven practice before planning his attack?", "A fortnight (two weeks).", "Easy", "Remembering"),
         ("What did the raven foolishly believe after a fortnight?", "That he had mastered all the needed skills to hunt heavy prey.", "Medium", "Understanding"),
         ("What does the word 'fortnight' mean?", "A period of two weeks (14 days).", "Easy", "Understanding")
     ]),

    # Set 5
    ("He waited for the shepherd to arrive with the flock. Once all sheep had arrived, the raven chose the fattest sheep of the flock as his prey. 'If I fly away with fattest sheep, tales of my feat would travel in all directions', thought the foolish raven.",
     [
         ("Who was the raven waiting for?", "The shepherd to arrive with the flock of sheep.", "Easy", "Remembering"),
         ("Which sheep did the raven choose as his prey?", "The fattest sheep of the flock.", "Easy", "Remembering"),
         ("Why did the raven choose the fattest sheep?", "He thought tales of his feat would travel in all directions.", "Easy", "Remembering"),
         ("What flaw in the raven's thinking is highlighted in this quote?", "Vanity and desire for public fame blinded him to physical realities.", "Medium", "Analyzing"),
         ("What does the word 'feat' mean in this context?", "An impressive action showing great skill or strength.", "Easy", "Understanding")
     ]),

    # Set 6
    ("At the opportune time, the raven flew down into the valley and swooped down on the chosen sheep. He clutched on the sheep's body and tried to fly away with it but in vain.",
     [
         ("When did the raven attack the sheep?", "At the opportune time.", "Easy", "Remembering"),
         ("What action did the raven take when he reached the sheep?", "He clutched on the sheep's body and tried to fly away with it.", "Easy", "Remembering"),
         ("Was the raven successful in flying away with the sheep?", "No, he tried in vain.", "Easy", "Remembering"),
         ("What does the phrase 'in vain' mean?", "Without success; producing no useful result.", "Medium", "Understanding"),
         ("What does the word 'opportune' mean?", "Suitable or favorable moment.", "Easy", "Understanding")
     ]),

    # Set 7
    ("Its talons got stuck in the thick hair on the sheep. The shepherd came and pulled away the raven from the sheep and threw it roughly on the ground. The raven got injured and could not fly for many days.",
     [
         ("What body part of the raven got stuck in the sheep?", "His talons (claws).", "Easy", "Remembering"),
         ("Where exactly did the talons get stuck?", "In the thick hair (wool) on the sheep.", "Easy", "Remembering"),
         ("What did the shepherd do to the raven?", "Pulled him away from the sheep and threw him roughly on the ground.", "Easy", "Remembering"),
         ("What happened to the raven as a result of being thrown down?", "He got injured and could not fly for many days.", "Easy", "Remembering"),
         ("What does the word 'talons' mean?", "The sharp claws of a bird of prey.", "Easy", "Understanding")
     ]),

    # Set 8
    ("Moral of the Story: Do not imitate others blindly.",
     [
         ("What is the moral of the fable stated here?", "Do not imitate others blindly.", "Easy", "Remembering"),
         ("Why was the raven's imitation described as 'blind'?", "Because he copied the eagle without considering his own small size and weak claws.", "Medium", "Understanding"),
         ("How does this moral apply to students at school?", "Students should not copy others recklessly, but focus on their own talents.", "Medium", "Applying"),
         ("What consequence did the raven suffer for his blind imitation?", "He suffered physical injury, pain, and being unable to fly for days.", "Medium", "Understanding"),
         ("How does this fable encourage self-acceptance?", "It teaches that accepting one's natural gifts prevents dangerous mistakes.", "Medium", "Evaluating")
     ]),

    # Set 9
    ("The eagle swooped down from great heights... The raven admired the eagle and wanted to be exactly like him... After a fortnight... his talons got stuck in the thick hair on the sheep.",
     [
         ("What contrast is shown between the eagle's flight and the raven's flight?", "The eagle swooped with effortless power; the raven got stuck helplessly in wool.", "Easy", "Remembering"),
         ("How long did the raven prepare for his flight?", "A fortnight.", "Easy", "Remembering"),
         ("Why did his talons get stuck?", "His small claws were not built for heavy lifting and got tangled in dense wool.", "Medium", "Understanding"),
         ("What does this passage teach about preparation versus physical reality?", "No amount of preparation can overcome a fundamental physical impossibility.", "Medium", "Analyzing"),
         ("What emotion did the raven feel before the attack versus after getting stuck?", "Before: Vain excitement. After: Panic and helplessness.", "Medium", "Analyzing")
     ]),

    # Set 10
    ("The shepherd came and pulled away the raven from the sheep and threw it roughly on the ground. The raven got injured and could not fly for many days. Moral of the Story: Do not imitate others blindly.",
     [
         ("Who saved the sheep from the raven?", "The shepherd.", "Easy", "Remembering"),
         ("How did the shepherd treat the raven?", "Roughly, throwing him onto the ground.", "Easy", "Remembering"),
         ("What physical punishment did the raven receive for his foolishness?", "He got injured and lost his ability to fly for many days.", "Easy", "Remembering"),
         ("Why did the shepherd handle the raven roughly?", "To protect his sheep and punish the invading bird.", "Medium", "Understanding"),
         ("Summarize the lesson of this final extract in one sentence.", "Foolish vanity and blind imitation lead to painful downfall and loss of freedom.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 02: The Raven that Wanted to be an Eagle\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH02_EXT_{q_counter:03d}"
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

with open(os.path.join(CH02_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 02 in {CH02_DIR}")
