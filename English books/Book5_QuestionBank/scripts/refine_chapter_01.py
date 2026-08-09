r"""
Refines all 6 Category files for Book 5 Chapter 01 ("Sankalp and his Friend") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH01_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_01")
os.makedirs(CH01_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Why was Sankalp very unhappy in the new town?", "(A) He missed his old school, teachers, and friends", "(B) He did not like the food in the new town", "(C) He failed his final examinations", "(D) He lost his school bag on the first day", "(A)", "Sankalp missed his old school, teachers, and friends.", "Easy", "Remembering", "Character Feelings"),
    ("Why did Sankalp dread going to school every day?", "(A) Classmates bullied him and he failed to make friends", "(B) The school was too far from his home", "(C) His teachers gave him too much homework", "(D) He was afraid of strict examinations", "(A)", "He had failed to make friends and classmates bullied him.", "Easy", "Remembering", "Conflict"),
    ("What threat did the bullies make to Sankalp today?", "(A) If they caught up with him, they would beat him", "(B) They would tell his parents a lie", "(C) They would steal his lunchbox", "(D) They would hide his bicycle", "(A)", "They threatened to beat him if they caught up with him.", "Easy", "Remembering", "Plot Details"),
    ("What did Sankalp do as soon as the school bell rang?", "(A) Picked up his bag and ran out of the school premises", "(B) Went to the principal's office to report bullies", "(C) Waited inside the classroom for his parents", "(D) Hid under a desk in the library", "(A)", "He picked up his bag and ran out of the premises to avoid confrontation.", "Easy", "Remembering", "Action"),
    ("Why did Sankalp run out of the school so quickly?", "(A) To avoid any confrontation with the bullies", "(B) To catch the school bus", "(C) To play football in the park", "(D) To buy ice cream from a vendor", "(A)", "He ran out to avoid confrontation.", "Easy", "Understanding", "Motivation"),
    ("Where did Sankalp find himself after running for a long time without looking back?", "(A) At the edge of the woods", "(B) Near the town railway station", "(C) In front of his old house", "(D) In the town market area", "(A)", "He realized he was at the edge of the woods.", "Easy", "Remembering", "Setting"),
    ("What warning had Sankalp's parents given him regarding the woods?", "(A) They had asked him to avoid the woods", "(B) They told him never to walk on paved roads", "(C) They asked him to bring firewood", "(D) They told him to play inside the woods", "(A)", "His parents had asked him to avoid the woods.", "Easy", "Remembering", "Parental Advice"),
    ("Why did Sankalp suddenly enter the woods?", "(A) He felt that some boys were following him", "(B) He wanted to pick wild berries", "(C) He saw a beautiful bird inside", "(D) He was looking for his lost ball", "(A)", "He felt some boys were following him and entered the woods in a jiffy.", "Easy", "Remembering", "Plot Action"),
    ("How quickly did Sankalp enter the woods when he thought he was followed?", "(A) In a jiffy", "(B) After one hour", "(C) Very slowly", "(D) At midnight", "(A)", "He entered the woods in a jiffy.", "Easy", "Remembering", "Vocabulary Usage"),
    ("What did Sankalp do once he thought he was safe inside the woods?", "(A) Sat down to catch his breath and fell asleep", "(B) Built a small wooden hut", "(C) Climbed to the top of a tall tree", "(D) Started singing loudly", "(A)", "He sat down to catch his breath and fell asleep.", "Easy", "Remembering", "Plot Details"),
    ("What did Sankalp notice when he woke up in the woods?", "(A) It was getting dark", "(B) It was bright morning", "(C) Heavy snow was falling", "(D) He was back in his bedroom", "(A)", "When he woke up, he saw it was getting dark.", "Easy", "Remembering", "Setting"),
    ("Why did tears start falling from Sankalp's eyes in the dark woods?", "(A) He was lost, worried for his parents, and worried for himself", "(B) Smoke from a camp fire went into his eyes", "(C) He scraped his knee on a thorn bush", "(D) He lost his gold watch", "(A)", "Tears fell because he was lost and worried for his family and himself.", "Easy", "Understanding", "Emotions"),
    ("What sound did Sankalp hear behind him in the dark woods?", "(A) Dry leaves rustling and very light footsteps", "(B) A fierce tiger roaring loudly", "(C) Thunder cracking in the sky", "(D) A car horn blowing", "(A)", "He heard dry leaves rustling and very light footsteps.", "Easy", "Remembering", "Sensory Details"),
    ("What animal was standing behind Sankalp when he turned around?", "(A) A lost and forlorn pup", "(B) A big wild wolf", "(C) A stray cat", "(D) A small monkey", "(A)", "He found a pup standing behind him.", "Easy", "Remembering", "Character"),
    ("How did the pup look when Sankalp first saw it?", "(A) Lost and forlorn", "(B) Fierce and angry", "(C) Well-fed and wearing a gold collar", "(D) Sleepy and lazy", "(A)", "It looked lost and forlorn.", "Easy", "Remembering", "Character Description"),
    ("What question did Sankalp ask the pup when he first met it?", "(A) 'Are you also lonely and lost, just like me?'", "(B) 'Where is your house owner?'", "(C) 'Why are you barking at me?'", "(D) 'Can you run faster than a horse?'", "(A)", "He asked: 'Are you also lonely and lost, just like me?'", "Easy", "Remembering", "Dialogue"),
    ("How did the pup respond when Sankalp asked, 'Will you be my friend?'", "(A) Nuzzled against Sankalp's leg and started sniffing the ground", "(B) Ran away into the deep forest", "(C) Barked fiercely and bit his shoe", "(D) Lay down and fell asleep", "(A)", "It nuzzled against his leg and started sniffing the ground.", "Easy", "Remembering", "Action"),
    ("How was Sankalp guided out of the dark woods?", "(A) The pup sniffed the ground and led him out", "(B) A forest ranger carried him on a horse", "(C) He followed a river stream", "(D) He used a compass in his bag", "(A)", "He was led out of the woods by the pup.", "Easy", "Remembering", "Resolution"),
    ("Who was in the search party heading toward Sankalp?", "(A) His anxious parents, a few people, and the school watchman", "(B) The police chief and ten soldiers", "(C) The school principal and his bullies", "(D) Only his grandmother", "(A)", "His anxious parents, a few people, and the school watchman.", "Easy", "Remembering", "Characters"),
    ("What was the school watchman holding in his hand during the search?", "(A) A flashlight", "(B) A wooden stick", "(C) A lantern", "(D) A bell", "(A)", "The watchman was holding a flashlight.", "Easy", "Remembering", "Detail"),
    ("Why was the watchman part of the search party?", "(A) He had seen Sankalp running toward the woods and shouted after him", "(B) He was Sankalp's uncle", "(C) He lived inside the woods", "(D) He was tracking a lost dog", "(A)", "He had seen Sankalp running in that direction.", "Easy", "Understanding", "Plot Connection"),
    ("What name did Sankalp give to his new friend and savior pup?", "(A) Pepper", "(B) Bruno", "(C) Rocky", "(D) Buddy", "(A)", "He named the pup Pepper.", "Easy", "Remembering", "Character Name"),
    ("What was Pepper doing when everyone saw it standing behind Sankalp?", "(A) Standing quietly and wagging its tail", "(B) Barking at Sankalp's father", "(C) Chewing a bone", "(D) Running back into the woods", "(A)", "Pepper was standing quietly wagging its tail.", "Easy", "Remembering", "Visual Detail"),
    ("What is the moral of the story 'Sankalp and his Friend'?", "(A) Love does not need a language", "(B) Never make new friends", "(C) Always explore dark forests", "(D) Bullies always win", "(A)", "Moral: Love does not need a language.", "Easy", "Remembering", "Moral Lesson"),
    ("What does the word 'forlorn' mean in the vocabulary box?", "(A) Lonely and unhappy", "(B) Very loud", "(C) Extremely fast", "(D) Full of energy", "(A)", "Forlorn means lonely and unhappy.", "Easy", "Understanding", "Vocabulary"),

    # Medium (26-40)
    ("Why did Sankalp call the evening 'the best day so far in this town' despite getting lost?", "(A) Because he had finally found a genuine, loyal friend in Pepper", "(B) Because he skipped his evening homework", "(C) Because the bullies apologized to him", "(D) Because his parents bought him a new bike", "(A)", "Finding Pepper gave him true friendship, making it his best day.", "Medium", "Analyzing", "Theme & Motivation"),
    ("How did Pepper demonstrate loyalty and helpfulness without speaking human words?", "(A) By nuzzling Sankalp for comfort and sniffing the trail to guide him out of the woods", "(B) By barking loudly at the watchman", "(C) By bringing a torch in its mouth", "(D) By performing trick jumps", "(A)", "Showed loyalty through comfort and guiding him out.", "Medium", "Analyzing", "Non-verbal Communication"),
    ("What contrast exists between Sankalp's human classmates and the stray pup Pepper?", "(A) Classmates bullied and threatened him, while Pepper offered unconditional friendship and help", "(B) Classmates were friendly, but Pepper was aggressive", "(C) Classmates helped him home, but Pepper got him lost", "(D) There is no contrast between them", "(A)", "Human bullies vs. compassionate animal companion.", "Medium", "Comparing", "Character Comparison"),
    ("Why did the watchman's clue prove crucial to finding Sankalp?", "(A) He had observed Sankalp running toward the woods and pointed the search party in the right direction", "(B) He found Sankalp's lost bag in the hallway", "(C) He called the police on his radio", "(D) He guessed Sankalp was at the cinema", "(A)", "His observation directed the search party to the woods.", "Medium", "Understanding", "Plot Structure"),
    ("What psychological change occurred in Sankalp from the beginning of the story to the end?", "(A) From feeling fearful, isolated, and hopeless to feeling hopeful, supported, and happy with a friend", "(B) From being angry to being greedy", "(C) From being cheerful to becoming a bully himself", "(D) No change occurred in his feelings", "(A)", "Shift from fear and isolation to hope and friendship.", "Medium", "Analyzing", "Character Arc"),
    ("What does the word 'confrontation' mean as used when Sankalp avoided the bullies?", "(A) A fight or hostile disagreement", "(B) A peaceful conversation", "(C) A school assembly", "(D) A sports competition", "(A)", "Confrontation means a fight or hostile disagreement.", "Medium", "Understanding", "Vocabulary"),
    ("Why did Sankalp's parents feel anxious when he did not return home on time?", "(A) He was new to town, timid, and the woods nearby were known to be unsafe for a lost child", "(B) He had taken all their money", "(C) He was supposed to cook dinner", "(D) He missed a doctor's appointment", "(A)", "New to town, timid, lost near woods in the dark.", "Medium", "Understanding", "Parental Concern"),
    ("How does the phrase 'Love does not need a language' apply to Sankalp and Pepper's bond?", "(A) They understood each other's feelings and offered mutual comfort through care, not words", "(B) Dogs can speak English if trained well", "(C) Sankalp taught Pepper how to read", "(D) Language is useless in schools", "(A)", "Emotional bond built on care and actions without words.", "Medium", "Evaluating", "Moral Interpretation"),
    ("Why did Sankalp ignore the watchman when he ran out of the school?", "(A) Panic and fear of being caught by bullies blinded him to his surroundings", "(B) He was listening to loud music on headphones", "(C) He hated the watchman", "(D) He wanted to play a trick on the watchman", "(A)", "Panic and fear of bullies blinded him.", "Medium", "Understanding", "Behavioral Analysis"),
    ("What role did nature/environment play in escalating Sankalp's distress?", "(A) The dark, unfamiliar woods surrounded him, making him lose direction and feel helpless", "(B) Heavy rain washed away his clothes", "(C) A thunderstorm destroyed the trees", "(D) Wild bears chased him deeper into the forest", "(A)", "Dark, unfamiliar woods caused loss of direction.", "Medium", "Analyzing", "Setting Impact"),
    ("How did the pup's own situation mirror Sankalp's situation?", "(A) Both were lost, lonely, forlorn, and in need of affection in an unfamiliar environment", "(B) Both were injured by bullies", "(C) Both were looking for food in a restaurant", "(D) Both had run away from home on purpose", "(A)", "Both were lost, lonely, and in need of affection.", "Medium", "Comparing", "Parallel Character Situation"),
    ("What does the word 'nuzzled' tell us about the pup's temperament?", "(A) It was gentle, affectionate, and seeking warmth and friendship", "(B) It was fierce and preparing to bite", "(C) It was trained as a guard dog", "(D) It was terrified of humans", "(A)", "Gentle, affectionate, and seeking warmth.", "Medium", "Understanding", "Word Analysis"),
    ("How did Sankalp's perspective about his future in the new town change at the end?", "(A) He gained confidence that better days were ahead now that he had Pepper as his friend", "(B) He decided to leave the town the next morning", "(C) He resolved never to go back to school", "(D) He planned to fight the bullies himself", "(A)", "He gained confidence that better days lay ahead.", "Medium", "Analyzing", "Resolution Analysis"),
    ("What lesson does Sankalp's story teach Class 5 students about coping with bullying?", "(A) Seek safety, communicate with parents, and find comfort in supportive relationships rather than suffering alone", "(B) Always fight bullies with physical violence", "(C) Hide in forests forever", "(D) Never tell parents about school problems", "(A)", "Seek safety, inform parents, find positive support.", "Medium", "Applying", "Real-World Application"),
    ("What literary genre best describes 'Sankalp and his Friend'?", "(A) Realistic Fiction focusing on emotional growth and human-animal bond", "(B) Historical Fantasy about medieval knights", "(C) Science Fiction involving space travel", "(D) Mystery Detective Novel", "(A)", "Realistic Fiction about emotional growth and human-animal bond.", "Medium", "Understanding", "Genre Identification"),

    # Hard (41-50)
    ("Critique Sankalp's decision to enter the woods despite his parents' explicit warning.", "(A) Driven by acute panic and fear of physical violence from bullies, his rational judgment was compromised", "(B) He disobeyed his parents out of spite and anger", "(C) He wanted to prove he was brave", "(D) He planned to live in the woods permanently", "(A)", "Panic and fear compromised rational decision-making.", "Hard", "Evaluating", "HOTS Character Critique"),
    ("Deconstruct the emotional climax of the story when Sankalp meets his search party.", "(A) Fear and relief converge as Sankalp embraces his parents, transforms his trauma into hope, and introduces Pepper", "(B) Sankalp gets scolded and punished by his parents", "(C) The watchman arrests the bullies", "(D) Pepper runs away back into the forest", "(A)", "Fear and relief converge; trauma turns into hope.", "Hard", "Analyzing", "Narrative Climax Analysis"),
    ("Evaluate the effectiveness of Shaivalini Sinha's narrative pacing from isolation to resolution.", "(A) The pacing builds tension through panic and darkness, then releases it gently through Pepper's arrival and parental reunion", "(B) The story moves at a uniform, dull pace without tension", "(C) The resolution happens in the first paragraph", "(D) The story ends abruptly without resolving the plot", "(A)", "Tension builds through panic/darkness and releases through reunion.", "Hard", "Evaluating", "Literary Analysis"),
    ("Formulate a continuation of the story showing how Pepper helps Sankalp face his school bullies.", "(A) 'The next day, walking with Pepper by his side, Sankalp felt confident. Seeing his gentle dog and calm demeanor, the bullies realized Sankalp was no longer an easy target.'", "(B) 'Pepper bit all the bullies and got sent away.'", "(C) 'Sankalp never went to school again.'", "(D) 'The bullies stole Pepper from Sankalp.'", "(A)", "Creative, positive continuation showing newfound confidence.", "Hard", "Creating", "Creative Continuation"),
    ("Compare the human capacity for empathy shown by Pepper versus the school watchman.", "(A) Pepper responded instinctively to emotional vulnerability, while the watchman acted out of duty and vigilance", "(B) Neither showed any care for Sankalp", "(C) The watchman was cruel, but Pepper was lazy", "(D) Both spoke to Sankalp in English", "(A)", "Instinctive emotional empathy vs duty-bound vigilance.", "Hard", "Comparing", "Comparative Character Study"),
    ("Assess the psychological impact of relocation on primary school children as depicted through Sankalp.", "(A) Relocation induces vulnerability, loneliness, and anxiety, which can be exacerbated by hostile school environments", "(B) Children adapt instantly without any emotional stress", "(C) Relocation only makes children happier", "(D) School environment has no impact on children", "(A)", "Relocation induces vulnerability and anxiety, amplified by hostility.", "Hard", "Evaluating", "Psychological Theme Assessment"),
    ("Analyze the symbolic significance of the 'flashlight' held by the school watchman in the dark woods.", "(A) Symbolizes hope, guidance, and the return of adult protection penetrating the dark isolation of fear", "(B) Represents the watchman's desire to scare wild animals", "(C) Symbolizes Sankalp's lost school bag", "(D) Has no symbolic meaning in the story", "(A)", "Symbolizes hope, guidance, and adult protection.", "Hard", "Analyzing", "Symbolism Analysis"),
    ("Synthesize how Chapter 01 addresses core SEL (Social-Emotional Learning) competencies for Class 5.", "(A) Teaches self-awareness (identifying fear), relationship skills (building friendship), and seeking help when lost", "(B) Teaches financial management and mathematics", "(C) Focuses solely on physical endurance", "(D) Promotes isolation from society", "(A)", "Teaches self-awareness, relationship building, and seeking help.", "Hard", "Synthesizing", "Pedagogical SEL Synthesis"),
    ("Critique the moral 'Love does not need a language' in the context of modern human-animal interactions.", "(A) Validates that non-verbal empathy, care, and mutual trust form deep emotional connections across species boundaries", "(B) Proves that animals should be trained to speak human words", "(C) Suggests that spoken language is useless between humans", "(D) Claims that animals do not feel emotions", "(A)", "Validates non-verbal empathy and mutual trust across species.", "Hard", "Evaluating", "Moral Philosophy Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 01 for a Class 5 assessment.", "(A) 'Describe a time when an unexpected friend helped you overcome a difficult situation. How did this experience change your outlook?'", "(B) 'Write ten sentences about forest trees.'", "(C) 'List the names of five dog breeds.'", "(D) 'Explain how flashlights work.'", "(A)", "Thought-provoking essay prompt connecting theme to personal experience.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 01: Sankalp and his Friend\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH01_MCQ_{idx:03d}"
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

with open(os.path.join(CH01_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Sankalp was very unhappy because he missed his old school, teachers, and _______.", "friends", "Missed his old school, teachers, and friends.", "Easy"),
    ("Some classmates used to _______ Sankalp while returning from school.", "bully", "Classmates used to bully him.", "Easy"),
    ("The bullies threatened that if they caught up with Sankalp, they would _______ him.", "beat", "Threatened to beat him.", "Easy"),
    ("Sankalp ran out of the school premises to avoid any _______.", "confrontation", "Avoid any confrontation.", "Easy"),
    ("He went on running until he reached the edge of the _______.", "woods", "Reached the edge of the woods.", "Easy"),
    ("Sankalp's parents had asked him to _______ the woods.", "avoid", "Parents asked him to avoid the woods.", "Easy"),
    ("Sankalp entered the woods in a _______ when he felt followed.", "jiffy", "Entered the woods in a jiffy.", "Easy"),
    ("Once he thought he was safe, Sankalp sat down to catch his _______.", "breath", "Sat down to catch his breath.", "Easy"),
    ("Sankalp fell asleep and woke up when it was getting _______.", "dark", "Woke up when it was getting dark.", "Easy"),
    ("Tears started falling from Sankalp's eyes because he was _______.", "lost", "Cried because he was lost.", "Easy"),
    ("He heard dry leaves _______ and light footsteps behind him.", "rustling", "Heard dry leaves rustling.", "Easy"),
    ("A lost and _______ pup was standing behind Sankalp.", "forlorn", "A lost and forlorn pup.", "Easy"),
    ("Sankalp asked the pup, 'Will you be my _______?'", "friend", "Asked the pup to be his friend.", "Easy"),
    ("The pup _______ against Sankalp's leg affectionately.", "nuzzled", "The pup nuzzled against his leg.", "Easy"),
    ("The pup started _______ the ground as if on cue to find the path.", "sniffing", "Started sniffing the ground.", "Easy"),
    ("Sankalp was led out of the woods by the _______.", "pup", "Led out by the pup.", "Easy"),
    ("Sankalp saw his anxious _______ heading his way in a search party.", "parents", "Saw his anxious parents.", "Easy"),
    ("The school _______ was holding a flashlight in the search party.", "watchman", "School watchman held a flashlight.", "Easy"),
    ("The watchman had seen Sankalp running away and _______ after him.", "shouted", "Shouted after Sankalp.", "Easy"),
    ("Sankalp ran ahead and _______ his parents tightly.", "hugged", "Hugged his parents tightly.", "Easy"),
    ("Sankalp declared this was the _______ day so far in the new town.", "best", "Declared it the best day so far.", "Easy"),
    ("Sankalp named his new friend and savior _______.", "Pepper", "Named the pup Pepper.", "Easy"),
    ("Pepper was standing quietly behind Sankalp wagging its _______.", "tail", "Wagging its tail.", "Easy"),
    ("The moral of the story is: Love does not need a _______.", "language", "Love does not need a language.", "Easy"),
    ("A confrontation is defined as a _______ or fight.", "disagreement", "Confrontation means a disagreement or fight.", "Easy"),

    # Medium (26-40)
    ("Sankalp felt isolated because he failed to make new _______ in the town.", "friends", "Failed to make new friends.", "Medium"),
    ("The bullies' hostility caused Sankalp to _______ going to school every day.", "dread", "Dread going to school.", "Medium"),
    ("Running without looking back caused Sankalp to lose his _______.", "way", "Lost his way.", "Medium"),
    ("The dark woods created a sense of fear and _______ in Sankalp.", "loneliness", "Fear and loneliness.", "Medium"),
    ("The pup's presence provided immediate emotional _______ to Sankalp.", "comfort", "Provided emotional comfort.", "Medium"),
    ("Pepper guided Sankalp out of the forest using its strong sense of _______.", "smell", "Guided using sense of smell.", "Medium"),
    ("The search party was organized because Sankalp did not return home by _______.", "nightfall", "Did not return by nightfall.", "Medium"),
    ("Sankalp realized that genuine friendship brings hope and _______.", "confidence", "Brings hope and confidence.", "Medium"),
    ("The watchman provided valuable _______ to the searching parents.", "information", "Provided valuable information.", "Medium"),
    ("Pepper's silent actions proved that true bond needs no _______ words.", "spoken", "Needs no spoken words.", "Medium"),
    ("Sankalp's parents experienced great relief when they found their _______ son.", "missing", "Found their missing son.", "Medium"),
    ("The word 'jiffy' signifies doing an action extremely _______.", "quickly", "Jiffy means extremely quickly.", "Medium"),
    ("Bullying in school can severely affect a student's mental _______.", "well-being", "Affects mental well-being.", "Medium"),
    ("Pepper was a stray animal that also needed a caring _______.", "home", "Needed a caring home.", "Medium"),
    ("Sankalp's story illustrates the profound strength of human-animal _______.", "companionship", "Strength of human-animal companionship.", "Medium"),

    # Hard (41-50)
    ("Panic-driven decisions often lead individuals into unexpected _______.", "peril", "Lead into unexpected peril.", "Hard"),
    ("Pepper's guidance symbolizes nature providing a path through _______.", "adversity", "Providing a path through adversity.", "Hard"),
    ("Sankalp's emotional catharsis occurred when he embraced his _______.", "parents", "Embraced his parents.", "Hard"),
    ("The narrative highlights how non-verbal empathy bridges emotional _______.", "barriers", "Bridges emotional barriers.", "Hard"),
    ("Vigilance by adults like the watchman plays a vital role in child _______.", "safety", "Vital role in child safety.", "Hard"),
    ("Overcoming trauma requires supportive relationships and emotional _______.", "resilience", "Requires emotional resilience.", "Hard"),
    ("Pepper's tail-wagging reflected complete trust and mutual _______.", "affection", "Reflected mutual affection.", "Hard"),
    ("Sankalp's experience transformed his initial despair into optimistic _______.", "expectation", "Transformed despair into expectation.", "Hard"),
    ("The woods represent a physical manifestation of Sankalp's internal _______.", "confusion", "Manifestation of internal confusion.", "Hard"),
    ("Chapter 01 integrates character development, thematic depth, and moral _______.", "insight", "Integrates moral insight.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 01: Sankalp and his Friend\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH01_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH01_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Sankalp enjoyed his new school and made many friends on his first day.", "False", "Sankalp was very unhappy, missed his old school, and failed to make friends.", "Easy"),
    ("Some of Sankalp's classmates bullied him while returning from school.", "True", "A few classmates behaved badly and bullied him on his way home.", "Easy"),
    ("The bullies threatened to beat Sankalp if they caught up with him.", "True", "They had threatened to beat him if they caught up with him.", "Easy"),
    ("Sankalp stayed back in the classroom to fight the bullies.", "False", "He picked up his bag and ran out of the school premises as soon as the bell rang.", "Easy"),
    ("Sankalp ran continuously without looking back to avoid confrontation.", "True", "Without looking back he went on running for a long time.", "Easy"),
    ("Sankalp's parents had encouraged him to explore the woods near the town.", "False", "His parents had explicitly asked him to avoid the woods.", "Easy"),
    ("Sankalp entered the woods because he thought some boys were following him.", "True", "He felt some boys were following him and entered the woods in a jiffy.", "Easy"),
    ("Sankalp stayed awake all night playing inside the woods.", "False", "He sat down to catch his breath and fell asleep.", "Easy"),
    ("When Sankalp woke up in the woods, it was getting dark.", "True", "When he woke up, he saw it was getting dark.", "Easy"),
    ("Sankalp cried in the woods because he lost his school shoes.", "False", "He cried because he was lost and worried for his parents and himself.", "Easy"),
    ("Sankalp heard heavy footsteps and a wolf growling behind him.", "False", "He heard dry leaves rustling and very light footsteps.", "Easy"),
    ("A lost and forlorn pup was standing behind Sankalp in the woods.", "True", "He turned to find a pup standing behind him.", "Easy"),
    ("Sankalp asked the pup to be his friend and help him find his way home.", "True", "He asked the pup to be his friend and help him find his way home.", "Easy"),
    ("The pup barked angrily and ran away from Sankalp.", "False", "The pup nuzzled against his leg and started sniffing the ground.", "Easy"),
    ("The pup guided Sankalp out of the woods safely.", "True", "Very soon Sankalp was out of the woods, being led on by the pup.", "Easy"),
    ("Sankalp's parents were relaxing at home while Sankalp was in the woods.", "False", "His parents were anxious and part of a search party looking for him.", "Easy"),
    ("The school watchman held a flashlight in the search party.", "True", "The watchman was holding a flashlight in the search party.", "Easy"),
    ("The watchman had seen Sankalp running away and tried to shout after him.", "True", "The watchman had seen him running and shouted after him.", "Easy"),
    ("Sankalp refused to talk to his parents when he saw them.", "False", "He ran ahead and hugged his parents tightly.", "Easy"),
    ("Sankalp named the pup 'Pepper'.", "True", "He introduced the pup as 'Pepper'.", "Easy"),
    ("The moral of the story is 'Love does not need a language'.", "True", "Moral stated at the end: Love does not need a language.", "Easy"),
    ("'Confrontation' means a peaceful picnic with friends.", "False", "Confrontation means a fight or hostile disagreement.", "Easy"),
    ("'Forlorn' means feeling happy and excited.", "False", "Forlorn means lonely and unhappy.", "Easy"),
    ("'Jiffy' means a period of ten days.", "False", "Jiffy means a very short moment.", "Easy"),
    ("Pepper wagged its tail quietly while standing behind Sankalp.", "True", "Pepper stood quietly behind Sankalp wagging its tail.", "Easy"),

    # Medium (26-40)
    ("Sankalp's panic caused him to ignore the watchman's shouts at school.", "True", "In his rush to escape bullies, Sankalp ignored the watchman shouting after him.", "Medium"),
    ("Pepper was a trained rescue dog owned by the forest department.", "False", "Pepper was a stray, lost pup that befriended Sankalp in the woods.", "Medium"),
    ("Sankalp called the day 'the best day so far' because he gained a loyal friend.", "True", "Finding Pepper transformed his lonely day into his best day in the new town.", "Medium"),
    ("Bullying is portrayed as a harmless activity in this story.", "False", "Bullying caused severe emotional distress and dangerous panic in Sankalp.", "Medium"),
    ("The watchman's clue was helpful in locating Sankalp's direction.", "True", "He informed the parents that Sankalp had run toward the woods.", "Medium"),
    ("Pepper required complex verbal commands to lead Sankalp home.", "False", "Pepper acted on non-verbal cues and natural tracking instincts.", "Medium"),
    ("Sankalp's parents were angry and punished him as soon as they found him.", "False", "They were anxious and hugged him tightly with relief.", "Medium"),
    ("Sankalp's story shows that animal companionship can alleviate human loneliness.", "True", "Pepper's friendship instantly ended Sankalp's feelings of isolation.", "Medium"),
    ("Sankalp fell asleep in the woods because he was calm and relaxed.", "False", "He fell asleep from exhaustion after running continuously in panic.", "Medium"),
    ("The story takes place over the course of a single afternoon and evening.", "True", "Events unfold from the school bell ringing in the afternoon to evening nightfall.", "Medium"),
    ("Pepper's name was given to it by the school watchman.", "False", "Sankalp named the pup Pepper himself.", "Medium"),
    ("Sankalp's experience helped him develop a more positive outlook on his future.", "True", "He expressed confidence that better days lay ahead in the new town.", "Medium"),
    ("The bullies followed Sankalp all the way into the search party.", "False", "The bullies did not follow him into the woods; Sankalp only thought he was followed.", "Medium"),
    ("Sankalp's tearful moment in the woods showed his emotional vulnerability.", "True", "Being lost in the dark made him cry out of fear for himself and his parents.", "Medium"),
    ("Non-verbal affection between Sankalp and Pepper is a key theme of the story.", "True", "Demonstrated by nuzzling, tail-wagging, and the moral 'Love does not need a language'.", "Medium"),

    # Hard (41-50)
    ("Sankalp's entry into the prohibited woods represents an intentional act of rebellion.", "False", "It was a panic-induced decision to escape perceived threats from bullies.", "Hard"),
    ("Pepper's character serves as an emotional foil to the hostile classmates.", "True", "Pepper offers unconditional affection, contrasting with the classmates' cruelty.", "Hard"),
    ("The narrative implies that spoken language is indispensable for establishing deep trust.", "False", "It proves love and trust transcend spoken language.", "Hard"),
    ("Sankalp's willingness to accept a stray pup reflects his deep need for connection.", "True", "His isolation made him instantly open to befriending the lost pup.", "Hard"),
    ("The school watchman acted irresponsibly by not following Sankalp into the woods immediately.", "False", "He alerted the parents and joined the search party with a flashlight.", "Hard"),
    ("Sankalp's initial unhappiness stemmed solely from academic pressure.", "False", "It stemmed from missing his old home and experiencing bullying.", "Hard"),
    ("The resolution of the story highlights the importance of parental support in crisis recovery.", "True", "The loving embrace of his parents provided safety after his ordeal.", "Hard"),
    ("Pepper's ability to navigate out of the woods highlights canine sensory superiority.", "True", "The pup used its acute sense of smell to trace a path out.", "Hard"),
    ("The story suggests that challenging experiences can sometimes yield positive outcomes.", "True", "Getting lost led Sankalp to find his beloved pet Pepper.", "Hard"),
    ("Chapter 01 integrates realistic social conflict with uplifting emotional resolution.", "True", "Transitions from school bullying to warm family and pet reunion.", "Hard")
]

tf_content = f"# True / False — Chapter 01: Sankalp and his Friend\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH01_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH01_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who was Sankalp and why was he unhappy in the new town?", "Sankalp was a simple-hearted young boy who was unhappy because he missed his old school, teachers, and friends, and had failed to make new friends.", "Easy", "Remembering"),
    ("How did Sankalp's new classmates treat him?", "A few classmates behaved very badly, bullied him on his way home from school, and threatened to beat him if they caught him.", "Easy", "Remembering"),
    ("What did Sankalp do to avoid confrontation with the bullies?", "As soon as the school bell rang, Sankalp picked up his bag and ran out of the school premises without looking back.", "Easy", "Remembering"),
    ("Where did Sankalp find himself after running for a long time?", "He realized he had lost his way and was standing at the edge of the woods near the town.", "Easy", "Remembering"),
    ("What warning had Sankalp's parents given him about the woods?", "His parents had explicitly asked him to avoid going into the woods.", "Easy", "Remembering"),
    ("Why did Sankalp enter the prohibited woods?", "He thought some boys were following him, so he entered the woods in a jiffy to hide and stay safe.", "Easy", "Understanding"),
    ("What happened to Sankalp after he sat down inside the woods?", "Thinking he was safe and invisible, he sat down to catch his breath and fell asleep from exhaustion.", "Easy", "Remembering"),
    ("What time of day was it when Sankalp woke up in the woods?", "When he woke up, he saw that it was getting dark.", "Easy", "Remembering"),
    ("Why did tears fall from Sankalp's eyes when he woke up?", "He cried because he was lost in the dark woods and felt deeply worried for his parents and himself.", "Easy", "Understanding"),
    ("What sounds alerted Sankalp to a presence behind him?", "He heard dry leaves rustling and very light footsteps approaching behind him.", "Easy", "Remembering"),
    ("What animal did Sankalp discover standing behind him in the woods?", "He discovered a lost, forlorn little pup standing quietly behind him.", "Easy", "Remembering"),
    ("What did Sankalp say when he first spoke to the pup?", "He asked, 'Are you also lonely and lost, just like me? Will you help me find my way home? Will you be my friend?'", "Easy", "Remembering"),
    ("How did the pup respond to Sankalp's friendly words?", "The pup nuzzled against Sankalp's leg affectionately and started sniffing the ground as if on cue to find a way out.", "Easy", "Remembering"),
    ("How did Sankalp manage to get out of the dark woods?", "The pup sniffed the trail and guided Sankalp safely out of the woods.", "Easy", "Remembering"),
    ("Who was in the search party that met Sankalp outside the woods?", "The search party included his anxious parents, a few townspeople, and the school watchman holding a flashlight.", "Easy", "Remembering"),
    ("What role did the school watchman play in finding Sankalp?", "The watchman had seen Sankalp running toward the woods and alerted the search party to look in that direction.", "Easy", "Understanding"),
    ("How did Sankalp greet his parents when he saw them?", "He ran ahead and hugged his anxious parents tightly, narrating everything that had happened.", "Easy", "Remembering"),
    ("What name did Sankalp give to his new pup friend?", "He named the pup 'Pepper'.", "Easy", "Remembering"),
    ("Why did Sankalp call the evening 'the best day so far in this town'?", "Because despite getting lost, he had finally found a true and loyal friend in Pepper.", "Easy", "Understanding"),
    ("What was Pepper doing while standing behind Sankalp in front of the search party?", "Pepper was standing quietly behind Sankalp, wagging its tail warmly.", "Easy", "Remembering"),
    ("What is the stated moral of the story 'Sankalp and his Friend'?", "The moral of the story is: 'Love does not need a language.'", "Easy", "Remembering"),
    ("What does the word 'confrontation' mean?", "'Confrontation' means a hostile argument or physical fight between people.", "Easy", "Understanding"),
    ("What does the word 'forlorn' mean?", "'Forlorn' means feeling lonely, abandoned, and unhappy.", "Easy", "Understanding"),
    ("What does the word 'jiffy' mean?", "'Jiffy' means an extremely short period of time or a moment.", "Easy", "Understanding"),
    ("What does the word 'nuzzled' mean?", "'Nuzzled' means rubbing or pushing one's nose or face gently against someone to show affection.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Explain why Sankalp felt so isolated at his new school.", "Sankalp struggled to adapt to the new town. He missed his old environment and failed to make friends, while hostile classmates bullied him, deepening his isolation.", "Medium", "Analyzing"),
    ("How did fear dictate Sankalp's actions after school?", "Fear of physical violence from bullies made Sankalp run frantically out of school, ignore the watchman, and enter the dangerous woods without thinking.", "Medium", "Analyzing"),
    ("Describe the turning point in Sankalp's emotional state inside the woods.", "The turning point occurred when the pup Pepper appeared. Instead of feeling helpless and terrified, Sankalp found comfort, companionship, and hope.", "Medium", "Analyzing"),
    ("How does Pepper illustrate the moral 'Love does not need a language'?", "Pepper could not speak human words, yet conveyed comfort, affection, and guidance through nuzzling, sniffing trails, and tail-wagging.", "Medium", "Evaluating"),
    ("Why was the watchman's presence with a flashlight significant?", "The watchman's flashlight symbolised safety and adult protection, cutting through the dark fear of the woods to reunite Sankalp with his family.", "Medium", "Analyzing"),
    ("Contrast Sankalp's feelings at the start of the day with his feelings at night.", "At the start, he felt dread, lonely despair, and fear. By night, having found Pepper and reunited with his parents, he felt hopeful and happy.", "Medium", "Comparing"),
    ("How did Sankalp's parents react when they saw him safe?", "They were filled with overwhelming anxiety and relief, hugging him tightly without scolding him, listening attentively to his experience.", "Medium", "Understanding"),
    ("Why did Sankalp consider Pepper his 'saviour'?", "Pepper provided emotional solace when Sankalp was weeping in the dark and physically guided him out of the confusing woods.", "Medium", "Understanding"),
    ("What lesson does this story convey about dealing with difficult life changes?", "It shows that while new environments and challenges can be daunting, staying hopeful and open to unexpected bonds can bring positive outcomes.", "Medium", "Evaluating"),
    ("How does the author create suspense when Sankalp wakes up in the woods?", "The author uses sensory details—darkness setting in, total isolation, dry leaves rustling, and quiet footsteps—to build tension before revealing the harmless pup.", "Medium", "Analyzing"),
    ("Why did Sankalp's bullies act the way they did towards him?", "As a new and timid student, Sankalp was perceived as vulnerable, making him an easy target for hostile classmates seeking to assert dominance.", "Medium", "Understanding"),
    ("What reveals that Sankalp was a sensitive and affectionate boy?", "His tears when lost, his tender words to the lost pup, his immediate embrace of his parents, and his gratitude toward Pepper reveal his sensitive nature.", "Medium", "Analyzing"),
    ("How did Pepper's guidance demonstrate animal intelligence?", "Pepper picked up human emotional cues, used its sharp sense of smell to trace a path, and purposefully led Sankalp toward safety.", "Medium", "Evaluating"),
    ("Summarize the main events of Chapter 01 in four sentences.", "Sankalp ran into the woods to escape school bullies and fell asleep. Waking up lost in the dark, he cried until a lost pup named Pepper comforted him. Pepper guided Sankalp out of the woods to his searching parents. Sankalp happily welcomed Pepper as his new best friend.", "Medium", "Understanding"),
    ("What advice would you give to someone experiencing school bullying like Sankalp?", "I would advise them to report the bullying immediately to parents and teachers, stay calm, avoid isolated areas, and seek supportive friends.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique Sankalp's impulsive behavior when escaping the bullies.", "While running away protected him from immediate confrontation, entering forbidden woods without checking direction created a life-threatening risk. Panic clouded his judgment.", "Hard", "Evaluating"),
    ("Analyze the theme of mutual salvation between Sankalp and Pepper.", "Both were lost and forlorn. Sankalp gave Pepper a loving home, while Pepper gave Sankalp direction and emotional healing, saving each other from solitude.", "Hard", "Analyzing"),
    ("Deconstruct the narrative arc of Chapter 01 from conflict to resolution.", "Exposition (bullying/loneliness) → Rising Action (flight into woods, getting lost in dark) → Climax (encounter with pup) → Falling Action (guided escape & search party) → Resolution (reunion & adopting Pepper).", "Hard", "Analyzing"),
    ("Evaluate the role of non-verbal communication in building trust in this story.", "Non-verbal gestures—sniffing, nuzzling, tight hugs, and tail-wagging—communicated empathy and security far more effectively than words during a crisis.", "Hard", "Evaluating"),
    ("Compare the atmosphere inside the woods before and after Pepper's appearance.", "Before: Threatening, dark, cold, and terrifying. After: Reassuring, cooperative, hopeful, and warm as friendship transformed the environment.", "Hard", "Comparing"),
    ("Discuss how Chapter 01 addresses childhood resilience.", "It shows how a child copes with fear and trauma by maintaining compassion, seeking connection, and reframing adversity into a positive milestone.", "Hard", "Evaluating"),
    ("How does Shaivalini Sinha use sensory details to enhance the story?", "Visual details (darkness, flashlight), auditory cues (rustling leaves, footsteps), and tactile sensations (nuzzling, tight hugs) immerse the reader deeply.", "Hard", "Analyzing"),
    ("Assess the importance of community vigilance as portrayed by the school watchman.", "The watchman's alertness in noticing Sankalp running and joining the search party demonstrates how attentive community members protect children.", "Hard", "Evaluating"),
    ("Formulate an alternative resolution where Sankalp confronts his bullies with Pepper.", "Empowered by Pepper's loyal presence, Sankalp stands firm the next day. Seeing his confidence and pet, the bullies realize he can no longer be intimidated.", "Hard", "Creating"),
    ("Synthesize the key pedagogical takeaways of Chapter 01 for Class 5 learners.", "Encourages empathy toward animals, promotes open communication with parents regarding bullying, and teaches resilience in new environments.", "Hard", "Synthesizing")
]

sa_content = f"# Short Answer Questions — Chapter 01: Sankalp and his Friend\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH01_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH01_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe Sankalp's life in the new town, detailing why he was unhappy and how his classmates treated him.",
     "Sankalp was a simple-hearted young boy who moved to a new town with his parents. He was deeply unhappy because he missed his old school, teachers, and childhood friends. He found it difficult to adapt and failed to make new friends in the new environment. To make matters worse, a few hostile classmates began bullying him while he returned home from school. On the day of the story, these bullies threatened to beat him if they caught up with him. This constant intimidation made Sankalp dread going to school every day, causing him immense emotional stress and loneliness.",
     "Easy", "Remembering"),

    ("Narrate the events that led to Sankalp getting lost in the dark woods.",
     "To avoid a violent confrontation with his bullies, Sankalp picked up his bag and ran out of the school premises the moment the final bell rang. He ran frantically without looking back for a long time. Suddenly, feeling that some boys were pursuing him, he entered the nearby woods in a jiffy to hide, disobeying his parents' explicit warning to avoid the area. Thinking he was safe and invisible, he sat down to catch his breath and fell asleep from sheer exhaustion. When he woke up, evening had set in and it was getting dark. Realizing he had completely lost his way and could not find his path out, Sankalp began weeping in fear and worry for his parents and himself.",
     "Easy", "Remembering"),

    ("Explain how Sankalp met the stray pup in the woods and how their friendship developed.",
     "While crying in the dark woods, Sankalp heard dry leaves rustling and light footsteps behind him. Turning around, he discovered a small, lost, and forlorn pup standing quietly. Recognizing that the pup was as lonely and lost as himself, Sankalp spoke to it with warmth, asking if it would be his friend and help him find his way home. The pup responded immediately by nuzzling against Sankalp's leg affectionately and sniffing the ground. This simple, tender interaction established a deep bond of mutual trust and friendship between the lonely boy and the stray pup.",
     "Easy", "Understanding"),

    ("Describe how the pup guided Sankalp out of the woods and how they met the search party.",
     "After bonding with Sankalp, the pup began sniffing the ground as if on cue to trace a path through the dark forest. Demonstrating natural tracking instincts, the pup walked ahead and guided Sankalp safely out of the woods. As they emerged, they encountered an anxious search party consisting of Sankalp's parents, townspeople, and the school watchman holding a flashlight. Sankalp ran ahead and hugged his relieved parents tightly, narrating his terrifying ordeal and introducing his savior pup, whom he officially named 'Pepper'.",
     "Easy", "Remembering"),

    ("What is the moral of the story 'Sankalp and his Friend'? Explain how the story illustrates this moral.",
     "The moral of the story is 'Love does not need a language.' This moral is beautifully illustrated through the relationship between Sankalp and the stray pup Pepper. Although Pepper could not speak human words, it understood Sankalp's distress and loneliness. Through non-verbal actions such as gentle nuzzling, trail-sniffing, and tail-wagging, Pepper offered affection, comfort, and physical guidance. The story proves that genuine love, empathy, and friendship transcend spoken words and can be communicated purely through caring actions.",
     "Easy", "Understanding"),

    ("Explain the vocabulary words from Chapter 01: Confrontation, Rustle, Forlorn, and Jiffy with meanings and example sentences.",
     "1. **Confrontation**: A hostile fight or disagreement. *Sentence*: Sankalp ran out of school to avoid a confrontation with the bullies.\n2. **Rustle**: A soft sound made by dry leaves or paper moving. *Sentence*: Sankalp heard dry leaves rustle behind him in the dark woods.\n3. **Forlorn**: Feeling lonely, abandoned, and unhappy. *Sentence*: The lost pup looked forlorn standing alone in the forest.\n4. **Jiffy**: A very short moment. *Sentence*: Hearing footsteps, Sankalp ran into the woods in a jiffy.",
     "Easy", "Understanding"),

    ("How did Sankalp's mood transform from the beginning of the story to the end?",
     "Sankalp experienced a dramatic emotional transformation. At the beginning, he was miserable, dreading school, and terrified of bullies. Inside the dark woods, his fear peaked as he wept in isolation. However, meeting Pepper brought immediate emotional solace. Guided safely back to his loving parents, Sankalp felt immense relief and happiness. By the end of the evening, he declared it the 'best day so far' in the new town because he had gained a loyal companion, filling his heart with optimism for the future.",
     "Easy", "Analyzing"),

    ("Describe the role of the school watchman in resolving the crisis in Chapter 01.",
     "The school watchman played a critical role in finding lost Sankalp. When Sankalp panicked and ran out of school toward the woods, the watchman noticed him and shouted after him. Although Sankalp ignored his calls, the watchman remembered the direction Sankalp had taken. When Sankalp's parents realized he was missing, the watchman alerted them and joined the search party, guiding them toward the woods with a flashlight. His alertness ensured the search party searched the right location promptly.",
     "Easy", "Understanding"),

    ("Discuss the importance of animal companionship in helping children overcome trauma and loneliness.",
     "Animal companionship offers unconditional affection and non-judgmental comfort, which is deeply therapeutic for children experiencing trauma or social isolation. In Sankalp's case, facing bullying and relocation created deep loneliness. Pepper's gentle presence provided an immediate sense of security and belonging. Taking care of Pepper shifted Sankalp's focus away from fear toward love, restoring his self-confidence and emotional well-being.",
     "Easy", "Evaluating"),

    ("Summarize Chapter 01 in five structured paragraphs.",
     "Paragraph 1: Sankalp was an unhappy boy who recently moved to a new town, missing his old friends and facing severe bullying at school.\nParagraph 2: Threatening bullies made Sankalp flee school in panic, leading him to run into forbidden woods where he fell asleep.\nParagraph 3: Woking up lost in the dark, Sankalp wept until he met a forlorn stray pup that comforted him affectionately.\nParagraph 4: The pup sniffed out a path, guiding Sankalp out of the woods to his searching parents and watchman.\nParagraph 5: Reunited happily, Sankalp adopted the pup, named it Pepper, and realized love needs no language.",
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why did Sankalp's parents warn him against going into the woods?", "His parents warned him because unfamiliar woods pose serious physical hazards for a child, especially after dark. Dangers include getting disoriented, harsh weather, falling into ravines, or encountering wild creatures. Sankalp's parents wanted to ensure his safety in a new, unfamiliar town.", "Easy", "Understanding"),
    ("Analyze how panic leads to poor decision-making as seen in Sankalp's actions.", "When individuals experience intense panic, rational thinking is overwritten by fear. Sankalp's panic over bullies caused him to run blindly, ignore the watchman's warnings, disobey his parents by entering dangerous woods, and lose his way completely, turning a school problem into a survival crisis.", "Easy", "Analyzing"),
    ("Explain how the author uses setting to mirror Sankalp's internal emotions.", "The author mirrors Sankalp's inner state through the setting. The bright, chaotic school reflects his anxiety and conflict. The dark, vast, and silent woods mirror his deep isolation, confusion, and fear. Finally, the flashlight beam and parental embrace symbolize returning hope and safety.", "Easy", "Analyzing"),
    ("What makes Pepper an ideal friend for Sankalp?", "Pepper is an ideal friend because it offers non-judgmental, unconditional companionship. Having experienced abandonment itself, Pepper empathizes with Sankalp's vulnerability, providing warmth, physical guidance, and emotional security without demanding anything in return.", "Easy", "Evaluating"),
    ("How does the story highlight the responsibilities of parents when a child faces bullying?", "The story highlights that parents must create a safe haven for children. When Sankalp was missing, his parents organized an immediate search party. Upon finding him, they offered immediate physical comfort and attentive listening instead of anger, validating his emotional experience.", "Easy", "Evaluating"),
    ("Describe the significance of the dialogue between Sankalp and Pepper in the woods.", "Sankalp's dialogue—asking Pepper if it was also lonely and if it would be his friend—represents a crucial moment of emotional vulnerability. Expressing his feelings aloud helped Sankalp process his fear and establish a meaningful emotional connection with the pup.", "Easy", "Analyzing"),
    ("What steps could Sankalp's school take to prevent bullying after this incident?", "The school could implement anti-bullying policies, counsel the aggressive students, foster inclusive classroom activities, train watchmen and staff to intervene in hallway conflicts, and establish a peer buddy system for new students.", "Easy", "Applying"),
    ("How does the story explore the theme of hope in times of adversity?", "The story demonstrates that even in dark and frightening circumstances, unexpected sources of help and friendship can emerge. Sankalp's terrifying ordeal in the woods led directly to finding Pepper, transforming his despair into lasting joy.", "Easy", "Evaluating"),
    ("Detail the sensory details used in Chapter 01 to build atmosphere.", "The author uses visual details (darkness, flashing light, tail-wagging), auditory details (bell ringing, rustling dry leaves, light footsteps, crying), and tactile details (nuzzling nose, tight parental hug) to create a vivid, immersive atmosphere.", "Easy", "Analyzing"),
    ("Why did Sankalp feel confident about his future in the new town at the end of the story?", "Finding Pepper gave Sankalp a sense of belonging and unconditional support. Knowing he had a loyal friend waiting for him at home gave him the emotional strength to face school challenges and feel optimistic about his life in the new town.", "Easy", "Understanding"),
    ("Compare Sankalp's relationship with his old friends versus his new bond with Pepper.", "While his old friends were missed memories from his former home, Pepper provided immediate, active emotional support during a real crisis. Both represent connection, but Pepper's bond was forged through shared vulnerability and rescue.", "Easy", "Comparing"),
    ("Explain the significance of Sankalp naming the pup 'Pepper'.", "Naming the pup 'Pepper' signifies ownership, acceptance, and formal inclusion into Sankalp's family. It transformed a nameless stray into a cherished individual and permanent companion.", "Easy", "Understanding"),
    ("How does Chapter 01 promote empathy toward stray animals?", "By depicting Pepper as a gentle, intelligent, and protective creature in need of love, the story encourages young readers to treat stray animals with kindness, respect, and care.", "Easy", "Evaluating"),
    ("What role does self-reflection play in Sankalp's character development?", "While waiting in the woods, Sankalp reflected on his worry for his parents, recognizing how much he loved them. Meeting Pepper made him reflect on his need for friendship, helping him grow emotionally mature.", "Easy", "Analyzing"),
    ("Re-write the ending of the story from Pepper's perspective.", "'I was cold and lost in the dark woods when I saw a human boy crying. I walked up to him gently. He spoke kindly to me and asked to be my friend. I nuzzled his leg and sniffed the ground to lead him to safety. When his family embraced him, I wagged my tail happily, knowing I had found my forever home.'", "Easy", "Creating"),

    # Medium (26-40)
    ("Critically analyze the impact of school bullying on a child's psychological well-being as shown in Chapter 01.",
     "Bullying creates severe emotional trauma, inducing feelings of dread, inadequacy, and intense isolation. In Chapter 01, hostility from classmates caused Sankalp to hate his new school environment, feel alienated, and experience extreme panic. It forced him to flee blindly into physical danger to escape harassment. The story accurately depicts how bullying compromises a child's sense of safety, self-esteem, and rational decision-making.",
     "Medium", "Analyzing"),

    ("Examine the narrative function of the woods in 'Sankalp and his Friend'.",
     "The woods serve a dual narrative function: as a physical obstacle and a symbolic space of transition. Physically, it presents darkness, confusion, and disorientation that tests Sankalp's endurance. Symbolically, entering the dark woods represents Sankalp's deep emotional isolation and fear. Leaving the woods led by Pepper symbolizes passing through emotional darkness into safety, connection, and newfound maturity.",
     "Medium", "Analyzing"),

    ("Evaluate the effectiveness of non-verbal communication in resolving human conflict and loneliness.",
     "Non-verbal communication is exceptionally powerful in conveying genuine empathy when words fail. Pepper's gentle nuzzling, attentive eye contact, and trail-sniffing communicated trust and comfort far more effectively than spoken language to a traumatized boy. Similarly, Sankalp's tight embrace with his parents expressed profound relief beyond words, validating the moral that love transcends language.",
     "Medium", "Evaluating"),

    ("Discuss how the author constructs tension and relief throughout the story.",
     "Tension is constructed incrementally: school harassment → threats of violence → panic-driven flight into forbidden woods → getting lost → darkness setting in → crying in isolation. The tension reaches its peak with mysterious rustling sounds. Relief is introduced gradually: the appearance of a gentle pup → mutual bonding → guided path out → flashlight beam of the search party → warm family embrace.",
     "Medium", "Analyzing"),

    ("Design a comprehensive lesson plan around Chapter 01 focusing on Social-Emotional Learning (SEL).",
     "1. **Objective**: Develop empathy, conflict management, and emotional awareness.\n2. **Discussion**: Analyze Sankalp's feelings of loneliness and how bullying affects students.\n3. **Activity**: Role-play positive ways to welcome new classmates and resolve conflicts.\n4. **Writing Task**: Write a paragraph on 'How I can be a loyal friend to someone in need.'\n5. **Reflection**: Discuss the moral 'Love does not need a language' regarding pet care.",
     "Medium", "Creating"),

    ("How does the watchman's character highlight the concept of community safety?", "The watchman represents vigilant community protection. By paying attention to students, noticing Sankalp's flight, and joining the search party, he demonstrates that adult alertness is vital for safeguarding children.", "Medium", "Evaluating"),
    ("Contrast the behavior of the school bullies with the behavior of Pepper.", "The bullies exhibited cruelty, hostility, and physical intimidation toward a vulnerable new student. Pepper exhibited warmth, gentle affection, and protective guidance toward the same vulnerable boy, highlighting true friendship.", "Medium", "Comparing"),
    ("Explain how parental empathy aids in healing childhood trauma.", "When Sankalp returned, his parents offered immediate physical affection and attentive listening instead of anger or blame. This supportive response restored his sense of security and enabled him to process his fear healthily.", "Medium", "Evaluating"),
    ("Analyze why Sankalp ignored the watchman's calls when running away.", "Sankalp's mind was consumed by acute flight-or-fight panic. His single-minded urge to escape perceived violence made him deaf to external calls, demonstrating how terror narrows focus.", "Medium", "Analyzing"),
    ("Discuss the symbolic meaning of darkness and light in Chapter 01.", "Darkness symbolizes confusion, fear, isolation, and lost direction inside the woods. Light (flashlight beam and dawn of friendship) symbolizes guidance, safety, adult protection, and emotional hope.", "Medium", "Analyzing"),
    ("How does Pepper's arrival alter Sankalp's perception of his predicament?", "Before Pepper arrived, Sankalp viewed himself as a helpless victim trapped in darkness. After Pepper arrived, he felt needed as a protector and friend, shifting his mindset from despair to active cooperation.", "Medium", "Analyzing"),
    ("Evaluate the role of intuition in animal tracking as shown by Pepper.", "Pepper relied on instinctive olfactory senses to trace human footsteps and scent trails, demonstrating how animals utilize natural capabilities to navigate environments that confuse humans.", "Medium", "Evaluating"),
    ("How can schools create an inclusive environment for newly relocated students?", "Schools can pair new students with peer mentors, conduct welcome orientations, enforce strict anti-bullying policies, and encourage cooperative group activities to build belonging.", "Medium", "Applying"),
    ("Describe the structure of Chapter 01 from problem identification to resolution.", "Problem: Relocation loneliness & school bullying. Complication: Flight into forbidden woods & getting lost in dark. Climax: Encounter with stray pup. Resolution: Guided escape, parental reunion, & adopting Pepper.", "Medium", "Analyzing"),
    ("Construct an alternative scene where Sankalp introduces Pepper to his teacher the next day.", "'Sankalp walked into school confidently with Pepper waiting at the gate. He introduced Pepper to his teacher, explaining how the pup saved him. Impressed, the teacher praised Sankalp and used his story to teach the class about empathy and kindness.'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the moral framework of Chapter 01 in addressing systemic school bullying.",
     "While Chapter 01 provides an uplifting personal resolution through pet companionship and family support, it leaves the systemic issue of school bullying unresolved. The bullies face no immediate accountability within the narrative text. From a critical standpoint, while emotional resilience and external support are vital, schools must also enforce structural consequences for bullying to ensure long-term student safety.",
     "Hard", "Evaluating"),

    ("Deconstruct the psychological concept of 'attachment' as depicted through Sankalp and Pepper.",
     "Sankalp's sudden attachment to Pepper reflects secure base seeking under stress. Experiencing rejection from peers, Sankalp projected his need for safety onto Pepper. Pepper's non-threatening, responsive behavior fulfilled the criteria of an attachment figure, providing proximity, comfort, and emotional stabilization during severe distress.",
     "Hard", "Analyzing"),

    ("Synthesize the literary craftsmanship of Shaivalini Sinha in 'Sankalp and his Friend'.",
     "Sinha weaves realistic childhood anxieties with emotional warmth. She employs tight narrative focus, relatable character motives, effective environmental symbolism, and realistic dialogue. By resolving emotional conflict through human-animal bonding, Sinha delivers a poignant, age-appropriate story that resonates deeply with Class 5 readers.",
     "Hard", "Synthesizing"),

    ("Formulate a rubrics-based assessment task for evaluating student comprehension of Chapter 01.",
     "- **Textual Recall (20%)**: Accurately identifying plot events, characters, and settings.\n- **Vocabulary Mastery (20%)**: Correct definition and contextual application of key terms.\n- **Character Analysis (30%)**: Explaining Sankalp's emotional arc and motivations.\n- **Thematic Evaluation (30%)**: Critiquing the moral 'Love does not need a language' with real-world examples.",
     "Hard", "Creating"),

    ("Evaluate how Chapter 01 fosters emotional intelligence (EQ) in young readers.", "The story develops EQ by encouraging readers to identify complex emotions (dread, loneliness, relief), understand non-verbal cues, practice empathy toward vulnerable beings, and recognize the value of supportive relationships in managing fear.", "Hard", "Evaluating"),

    ("Compare Sankalp's survival experience in the woods with traditional wilderness survival narratives.", "Unlike classic survival tales where protagonists rely on physical tools or bushcraft, Sankalp's survival relies entirely on emotional connection and natural animal instincts, emphasizing relational survival over physical mastery.", "Hard", "Comparing"),
    ("Discuss the socio-emotional challenges faced by primary school children during family relocation.", "Relocation disrupts established peer networks, creates academic adjustment stress, and forces children to rebuild social identity. Without immediate support, children may experience acute anxiety and vulnerability to peer marginalization.", "Hard", "Evaluating"),
    ("Analyze the character function of Pepper as an archetype of the 'Loyal Companion'.", "Pepper embodies the timeless literary archetype of the Loyal Companion—an unpretentious, intuitive guide who appears during adversity to assist the protagonist on their emotional and physical journey.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'This has been the best day so far in this town... I have finally made a friend.'", "This poignant line encapsulates Sankalp's profound psychological shift. It reframes a harrowing ordeal into a milestone of hope, proving that true companionship outweighs physical hardship and restores faith in the future.", "Hard", "Evaluating"),
    ("Synthesize the ultimate pedagogical lesson of Chapter 01 for Class 5 English curriculum.", "Chapter 01 seamlessly integrates linguistic skill development with character education, demonstrating that empathy, resilience, family support, and genuine companionship are fundamental to overcoming life's challenges.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 01: Sankalp and his Friend\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH01_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH01_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Sankalp was very unhappy. He missed his old school, teachers and friends in this new town. He dreaded coming to school every day as not only he had failed to make friends but a few classmates behaved very badly with him.",
     [
         ("Why was Sankalp unhappy in his new town?", "He missed his old school, teachers, and friends.", "Easy", "Remembering"),
         ("What two main reasons made Sankalp dread going to school every day?", "He failed to make new friends and a few classmates bullied him.", "Easy", "Remembering"),
         ("Find a word in the extract that means 'feared greatly'.", "Dreaded.", "Easy", "Understanding"),
         ("How did Sankalp feel emotionally in his new school environment?", "Isolated, lonely, anxious, and deeply unhappy.", "Medium", "Understanding"),
         ("What advice would you give to a student facing a similar situation as Sankalp?", "Report the bullying to parents and teachers, stay calm, and seek positive peer groups.", "Medium", "Applying")
     ]),

    # Set 2
    ("They used to bully him while returning from school and today they had threatened him that if they caught up with him, they would beat him. Sankalp, who was a simple-hearted boy, picked up his bag and ran out of the school premises once the bell rang to avoid any confrontation.",
     [
         ("When did the classmates usually bully Sankalp?", "While returning home from school.", "Easy", "Remembering"),
         ("What threat did the bullies make to Sankalp on that day?", "They threatened to beat him if they caught up with him.", "Easy", "Remembering"),
         ("What kind of boy was Sankalp described as?", "A simple-hearted boy.", "Easy", "Remembering"),
         ("Why did Sankalp run out of the school premises immediately after the bell rang?", "To avoid any confrontation or physical fight with the bullies.", "Medium", "Understanding"),
         ("What does the word 'confrontation' mean in this passage?", "A fight or hostile disagreement.", "Easy", "Understanding")
     ]),

    # Set 3
    ("Without looking back he went on running for a long time. Then, he realised that he had lost his way and was now at the edge of the woods which his parents had asked him to avoid.",
     [
         ("How did Sankalp run when escaping the school?", "He ran continuously for a long time without looking back.", "Easy", "Remembering"),
         ("What did Sankalp realize after running for a long time?", "He realized he had lost his way.", "Easy", "Remembering"),
         ("Where did Sankalp find himself standing?", "At the edge of the woods.", "Easy", "Remembering"),
         ("What instruction had Sankalp's parents given him about the woods?", "They had explicitly asked him to avoid the woods.", "Easy", "Remembering"),
         ("Why did Sankalp ignore his parents' warning in that moment?", "He was in acute panic and fleeing from perceived physical harm from bullies.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("Suddenly he felt that some boys were following him and he entered the woods in a jiffy. Once he thought he was invisible and safe, he sat down to catch his breath. But before he could realise he fell asleep.",
     [
         ("Why did Sankalp decide to enter the woods?", "He felt that some boys were following him.", "Easy", "Remembering"),
         ("How quickly did Sankalp enter the woods?", "In a jiffy (very quickly).", "Easy", "Remembering"),
         ("What did Sankalp do once he thought he was safe?", "He sat down to catch his breath.", "Easy", "Remembering"),
         ("What happened to Sankalp shortly after he sat down?", "He fell asleep from exhaustion.", "Easy", "Remembering"),
         ("What does the phrase 'catch his breath' mean?", "To rest briefly until normal breathing resumes after heavy running.", "Medium", "Understanding")
     ]),

    # Set 5
    ("When Sankalp woke up, he saw it was getting dark. Then he worried. He worried for his father, his mother and for himself. He could not even make his way out of the woods. Tears started falling down from his eyes.",
     [
         ("What was the light condition when Sankalp woke up?", "It was getting dark.", "Easy", "Remembering"),
         ("Who did Sankalp worry about when he woke up?", "His father, his mother, and himself.", "Easy", "Remembering"),
         ("Why could Sankalp not leave the woods?", "He had lost his path and could not find his way out.", "Easy", "Remembering"),
         ("Why did tears fall from Sankalp's eyes?", "Because he was lost, frightened, and overwhelmed by concern for his family and safety.", "Medium", "Understanding"),
         ("What emotion dominates this extract?", "Fear, disorientation, and vulnerability.", "Medium", "Analyzing")
     ]),

    # Set 6
    ("After a few moments, he heard dry leaves rustling behind him and very light footsteps. He turned to find a pup standing behind him. It also looked lost and forlorn.",
     [
         ("What sounds did Sankalp hear in the dark woods?", "Dry leaves rustling and very light footsteps.", "Easy", "Remembering"),
         ("What did Sankalp see when he turned around?", "A pup standing behind him.", "Easy", "Remembering"),
         ("How is the pup described in this extract?", "Lost and forlorn.", "Easy", "Remembering"),
         ("What does the word 'forlorn' mean?", "Lonely and unhappy.", "Easy", "Understanding"),
         ("How did the pup's presence change the mood of the story?", "It shifted the tone from terrifying isolation to potential comfort and companionship.", "Medium", "Analyzing")
     ]),

    # Set 7
    ("Sankalp sat down and said, 'Are you also lonely and lost, just like me?' The pup kept on looking at him. 'Will you help me find my way home? Will you be my friend?' The pup nuzzled against Sankalp's leg and started sniffing the ground as if on cue.",
     [
         ("What questions did Sankalp ask the pup?", "He asked if it was lonely and lost, if it would help him find home, and if it would be his friend.", "Easy", "Remembering"),
         ("How did the pup react when Sankalp asked for friendship?", "It nuzzled against his leg and started sniffing the ground.", "Easy", "Remembering"),
         ("What does the word 'nuzzled' mean?", "Rubbed its nose gently against his leg affectionately.", "Easy", "Understanding"),
         ("Why did the pup start sniffing the ground?", "To trace a scent trail and guide Sankalp out of the woods.", "Medium", "Understanding"),
         ("What connection is established between Sankalp and the pup here?", "A mutual bond of trust, companionship, and non-verbal understanding.", "Medium", "Analyzing")
     ]),

    # Set 8
    ("Very soon Sankalp was out of woods being led on by the pup. Both of them had gone ahead a little when they saw a search party heading their way. Sankalp could see his anxious parents, a few more people and the school watchman holding a flashlight.",
     [
         ("Who led Sankalp out of the woods?", "The pup.", "Easy", "Remembering"),
         ("What did Sankalp see after emerging from the woods?", "A search party heading their way.", "Easy", "Remembering"),
         ("Who was present in the search party?", "His anxious parents, a few townspeople, and the school watchman.", "Easy", "Remembering"),
         ("What object was the school watchman holding?", "A flashlight.", "Easy", "Remembering"),
         ("What did the flashlight symbolise in this dark scene?", "Hope, guidance, safety, and adult protection.", "Medium", "Analyzing")
     ]),

    # Set 9
    ("The watchman had seen Sankalp running away in this direction and shouted after him but Sankalp had ignored him. He ran ahead and hugged his parents tightly. He narrated all that had happened earlier in the day.",
     [
         ("Why was the watchman looking in the woods?", "He had seen Sankalp running toward the woods and shouted after him.", "Easy", "Remembering"),
         ("Why had Sankalp ignored the watchman earlier?", "Because he was in extreme panic escaping the bullies.", "Medium", "Understanding"),
         ("What did Sankalp do when he reached his parents?", "He ran ahead, hugged his parents tightly, and narrated everything.", "Easy", "Remembering"),
         ("What emotion did the tight hug express?", "Profound relief, safety, and love.", "Medium", "Understanding"),
         ("What role did adult alertness play in Sankalp's rescue?", "The watchman's observation provided the vital clue for the search party.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("Then he said, 'This has been the best day so far in this town but I am sure I have better days ahead. As you can see Mom, Dad, I have finally made a friend.' He turned back and everybody saw a pup standing quietly behind Sankalp wagging its tail. 'Meet my friend and saviour Pepper.' Moral of the Story: Love does not need a language.",
     [
         ("Why did Sankalp call it 'the best day so far in this town'?", "Because he had finally found a true, loyal friend in Pepper.", "Easy", "Remembering"),
         ("What was the pup doing when introduced to Sankalp's parents?", "Standing quietly behind Sankalp wagging its tail.", "Easy", "Remembering"),
         ("What name did Sankalp give to the pup?", "Pepper.", "Easy", "Remembering"),
         ("What is the moral of the story stated at the end?", "Love does not need a language.", "Easy", "Remembering"),
         ("How does Pepper prove that 'Love does not need a language'?", "Pepper offered affection, comfort, and rescue purely through non-verbal actions.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 01: Sankalp and his Friend\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH01_EXT_{q_counter:03d}"
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

with open(os.path.join(CH01_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 01 in {CH01_DIR}")
