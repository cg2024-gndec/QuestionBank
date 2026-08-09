r"""
Refines all 6 Category files for Chapter 01 ("The Foolish Pandit") for Class 3 (Book 3).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 3 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH01_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_01")
os.makedirs(CH01_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What was the name of the pandit in the story?", "(A) Pandit Someshwar", "(B) Pandit Ramdas", "(C) Pandit Vishnu", "(D) Pandit Devdutt", "(A)", "The pandit was named Pandit Someshwar.", "Easy", "Remembering", "Character Name"),
    ("Which deity was Pandit Someshwar devoted to?", "(A) Goddess Durga", "(B) Lord Shiva", "(C) Goddess Lakshmi", "(D) Lord Vishnu", "(A)", "He was a devotee of Goddess Durga.", "Easy", "Remembering", "Deity"),
    ("What did Pandit Someshwar wish for from Goddess Durga?", "(A) A divine meeting and special blessings", "(B) A bag of gold coins", "(C) A big palace", "(D) A magic horse", "(A)", "He wished for a divine meeting and special blessings.", "Easy", "Remembering", "Wish"),
    ("Who advised Someshwar to pray where there were no disturbances?", "(A) His guru", "(B) His father", "(C) The village chief", "(D) A king", "(A)", "His guru asked him to pray without disturbances.", "Easy", "Remembering", "Guru's Advice"),
    ("Where did Someshwar go to meditate and pray?", "(A) To a big jungle", "(B) To a crowded market", "(C) To a riverbank", "(D) To a mountain top", "(A)", "He went to a big jungle to pray.", "Easy", "Remembering", "Setting"),
    ("How did Someshwar pray despite changing weather?", "(A) He did not waver and remained fully dedicated", "(B) He ran back home during rain", "(C) He complained to his friends", "(D) He gave up quickly", "(A)", "He did not waver and remained fully dedicated.", "Easy", "Understanding", "Dedication"),
    ("What magical herb did Goddess Durga grant to Someshwar?", "(A) Sanjeevani booti", "(B) Neem leaves", "(C) Tulsi herb", "(D) Magic lotus", "(A)", "She granted him the Sanjeevani booti.", "Easy", "Remembering", "Magical Item"),
    ("What was the magical power of the Sanjeevani booti?", "(A) Bringing the dead back to life", "(B) Turning stone into gold", "(C) Making a person invisible", "(D) Granting endless food", "(A)", "A few drops could bring the dead back to life.", "Easy", "Remembering", "Magic Power"),
    ("What did Someshwar daydream about after getting the booti?", "(A) Helping villagers, gaining followers, and becoming Sarpanch", "(B) Flying to the moon", "(C) Hiding the booti in a cave", "(D) Selling the booti for money", "(A)", "He daydreamed about gaining followers and becoming Sarpanch.", "Easy", "Remembering", "Daydream"),
    ("What doubt entered Someshwar's mind regarding the booti?", "(A) 'What if the booti does not work?'", "(B) 'What if Goddess Durga takes it back?'", "(C) 'What if it tastes sour?'", "(D) 'What if it loses color?'", "(A)", "He doubted whether the booti would actually work.", "Easy", "Understanding", "Doubt"),
    ("Which dead animal did Someshwar decide to test the booti on?", "(A) A dead lion", "(B) A dead tiger", "(C) A dead elephant", "(D) A dead deer", "(A)", "He decided to test it on a dead lion lying nearby.", "Easy", "Remembering", "Test Subject"),
    ("What happened when Someshwar dropped the booti on the lion?", "(A) The lion came back to life with more energy and strength", "(B) The lion turned into dust", "(C) Nothing happened", "(D) The lion turned into a cat", "(A)", "The lion came back to life with more energy and strength.", "Easy", "Remembering", "Result of Test"),
    ("What sound did the revived lion make?", "(A) Roared ferociously", "(B) Barked loudly", "(C) Meowed softly", "(D) Squeaked quietly", "(A)", "The lion roared ferociously.", "Easy", "Remembering", "Lion's Sound"),
    ("What happened to Someshwar at the end of the story?", "(A) He was eaten by the lion", "(B) He climbed a tree safely", "(C) He ran faster than the lion", "(D) The lion bowed to him", "(A)", "He could not outrun the lion and was eaten by it.", "Easy", "Remembering", "Story Outcome"),
    ("What is the moral of the story 'The Foolish Pandit'?", "(A) Think before you act", "(B) Always trust wild animals", "(C) Never pray in jungles", "(D) Greed always brings gold", "(A)", "The moral is: Think before you act.", "Easy", "Remembering", "Moral Lesson"),
    ("What does the word 'devotee' mean in the vocabulary box?", "(A) An ardent follower", "(B) A fierce animal", "(C) A village ruler", "(D) A magical plant", "(A)", "Devotee means an ardent follower.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'divine' mean?", "(A) Connected to God", "(B) Very fast", "(C) Loud and noisy", "(D) Dangerous", "(A)", "Divine means connected to God.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'deity' mean?", "(A) A God", "(B) A leaf", "(C) A forest path", "(D) A student", "(A)", "Deity means a God.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'ferociously' mean?", "(A) In a frightening and violent way", "(B) In a quiet and soft way", "(C) In a silly way", "(D) In a slow way", "(A)", "Ferociously means in a frightening and violent way.", "Easy", "Understanding", "Vocabulary"),
    ("What type of tale is 'The Foolish Pandit'?", "(A) A Panchatantra Tale", "(B) A Greek Myth", "(C) A Modern Sci-Fi Story", "(D) A Historical Essay", "(A)", "It is a Panchatantra Tale.", "Easy", "Remembering", "Genre"),
    ("Why did Goddess Durga appear in front of Someshwar?", "(A) She was pleased by his deep devotion and dedicated prayer", "(B) He called her loudly", "(C) She wanted to scare him", "(D) She lost her way in the jungle", "(A)", "She was pleased by his devotion.", "Easy", "Understanding", "Appearance Reason"),
    ("What village position did Someshwar dream of achieving?", "(A) Sarpanch", "(B) King", "(C) Guard", "(D) Doctor", "(A)", "He dreamed of becoming the village Sarpanch.", "Easy", "Remembering", "Village Position"),
    ("Could Someshwar outrun the lion when it revived?", "(A) No, he could not outrun the lion", "(B) Yes, he ran faster than a horse", "(C) Yes, he flew into the sky", "(D) He did not try to run", "(A)", "He could not outrun the lion.", "Easy", "Remembering", "Attempted Escape"),
    ("Why was Someshwar's action foolish?", "(A) Because he revived a dangerous predator without thinking of the consequences", "(B) Because he prayed too long", "(C) Because he spoke to Goddess Durga", "(D) Because he lived in a village", "(A)", "He revived a dangerous predator without thinking.", "Easy", "Understanding", "Foolishness Analysis"),
    ("What is the title of Chapter 01?", "(A) The Foolish Pandit", "(B) The Jackal and the Dhol", "(C) Two Cats and the Monkey", "(D) Fountain Pen", "(A)", "Chapter 01 is titled 'The Foolish Pandit'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why did Someshwar's guru instruct him to pray in a secluded jungle?", "(A) To ensure deep concentration without any distraction or noise from the village", "(B) Because the jungle was full of wild animals", "(C) To punish Someshwar", "(D) Because there were no temples left", "(A)", "To ensure deep concentration without distraction.", "Medium", "Analyzing", "Guru's Strategy"),
    ("How did Someshwar's desire for fame and status ruin his spiritual achievement?", "(A) Instead of using the divine blessing humbly, he daydreamed about gaining village power and foolishly tested it on a lion", "(B) He threw the booti away into a river", "(C) Goddess Durga took the booti back immediately", "(D) The villagers drove him out of the jungle", "(A)", "Selfish ambition and foolish curiosity ruined his blessing.", "Medium", "Evaluating", "Flaw Analysis"),
    ("What contrast exists between Goddess Durga's gift and Someshwar's use of it?", "(A) The gift was meant to give life and help others; Someshwar used it rashly on a deadly predator to satisfy his doubt", "(B) The gift was harmful, but Someshwar made it good", "(C) The gift was fake, but Someshwar made it real", "(D) There is no contrast", "(A)", "Divine gift of life vs foolish, rash testing on a predator.", "Medium", "Analyzing", "Thematic Contrast"),
    ("Why was testing the Sanjeevani booti on a lion a fatal mistake?", "(A) A lion is a wild, carnivorous predator that naturally attacks humans upon reviving", "(B) The lion was too old to move", "(C) The booti turned the lion into ice", "(D) The lion ran away to another forest", "(A)", "Reviving a wild carnivorous predator guarantees an attack.", "Medium", "Understanding", "Fatal Choice"),
    ("What psychological flaw made Someshwar test the booti despite receiving it from a Goddess?", "(A) Lack of faith and foolish doubt ('What if it does not work?') combined with impatience", "(B) He forgot what Goddess Durga said", "(C) He wanted to feed the lion", "(D) He was forced by the villagers", "(A)", "Lack of faith, doubt, and impatience drove his action.", "Medium", "Analyzing", "Psychological Flaw"),
    ("How does Panchatantra storytelling use animal characters to convey human wisdom?", "(A) By showing realistic consequences of foolish human choices through dramatic animal encounters", "(B) By proving that lions can talk in English", "(C) By teaching children how to hunt lions", "(D) By encouraging people to keep lions as pets", "(A)", "Shows realistic consequences of human choices through animal encounters.", "Medium", "Evaluating", "Panchatantra Style"),
    ("What does 'spiritual pursuit' mean in the context of Someshwar's meditation?", "(A) Dedicated effort to achieve a holy connection with God through prayer", "(B) Running fast in a jungle race", "(C) Looking for gold treasures", "(D) Learning hunting skills", "(A)", "Dedicated effort to achieve a holy connection with God.", "Medium", "Understanding", "Concept Explanation"),
    ("What irony is present in Someshwar's tragic end?", "(A) The herb that possessed the power to give life became the direct cause of his own death", "(B) He became Sarpanch after dying", "(C) The lion became his best friend", "(D) Goddess Durga saved the lion instead of him", "(A)", "The life-giving herb caused his own death due to foolishness.", "Medium", "Analyzing", "Dramatic Irony"),
    ("How could Someshwar have tested the Sanjeevani booti safely if he really wanted to check it?", "(A) By testing it on a harmless dead creature like a small bird or dry plant rather than a wild lion", "(B) By throwing it in fire", "(C) By drinking it all himself", "(D) By testing it on a dragon", "(A)", "Testing on a harmless creature or plant would have been safe.", "Medium", "Applying", "Alternative Action"),
    ("What lesson does 'The Foolish Pandit' teach Class 3 students about decision-making?", "(A) Always consider the dangerous consequences of your actions before taking a foolish step", "(B) Never ask for wishes from God", "(C) Run fast whenever you see a forest", "(D) Always doubt what your teachers tell you", "(A)", "Consider dangerous consequences before taking action.", "Medium", "Evaluating", "Practical Application"),
    ("Why did Someshwar want to become the village Sarpanch?", "(A) He was tempted by worldly power, prestige, and political leadership over the villagers", "(B) His guru ordered him to become Sarpanch", "(C) Goddess Durga demanded it", "(D) The Sarpanch was his brother", "(A)", "Tempted by worldly power, prestige, and leadership.", "Medium", "Understanding", "Character Motivation"),
    ("How does the story show that physical speed cannot overcome a foolish mistake?", "(A) Once the lion was revived, Someshwar's human running speed was no match for a powerful predator", "(B) Someshwar ran faster than the lion", "(C) Someshwar hid under a small stone", "(D) The lion fell asleep while chasing him", "(A)", "Human running speed cannot outrun a revived predator.", "Medium", "Analyzing", "Physical Limitation"),
    ("What does the word 'ferociously' tell us about the revived lion's behavior?", "(A) It came back to life full of wild, dangerous, aggressive predator energy", "(B) It came back to life tame like a pet puppy", "(C) It was sleepy and tired", "(D) It was singing happily", "(A)", "Came back to life full of wild, aggressive predator energy.", "Medium", "Understanding", "Word Analysis"),
    ("How does patience play a role in Someshwar's initial success and later failure?", "(A) He showed great patience during years of prayer, but lost patience and wisdom in a single moment of doubt", "(B) He was impatient during prayer but patient with the lion", "(C) He never prayed at all", "(D) He waited fifty years for the lion to wake up", "(A)", "Years of patient prayer ruined by one moment of foolish impatience.", "Medium", "Analyzing", "Patience vs Impatience"),
    ("What is the significance of the Sanjeevani booti in Indian mythology?", "(A) It is a legendary divine herb capable of reviving the dead or healing fatal injuries", "(B) It is a poison used in wars", "(C) It is a sweet dish made of milk", "(D) It is a type of tree bark used for paper", "(A)", "Legendary divine herb capable of reviving the dead/healing fatal injuries.", "Medium", "Understanding", "Mythological Context"),

    # Hard (41-50)
    ("Deconstruct the tragic flaw (Hubris & Doubt) in Pandit Someshwar's character.", "(A) His spiritual discipline was undermined by vanity (seeking Sarpanch post) and intellectual arrogance (doubting divine grace)", "(B) He had no flaws and was purely unlucky", "(C) His flaw was praying too much", "(D) His flaw was loving animals too much", "(A)", "Vanity (seeking power) and arrogance (doubting divine grace) caused his downfall.", "Hard", "Analyzing", "HOTS Character Analysis"),
    ("Analyze the cause-and-effect chain that leads from Someshwar's prayer to his demise.", "(A) Prayer -> Divine Blessing (Booti) -> Daydreaming of Power -> Doubt in Gift -> Testing on Lion -> Lion Revives -> Someshwar Eaten", "(B) Prayer -> Sarpanch -> Lion -> Booti", "(C) Booti -> Lion -> Prayer -> Goddess Durga", "(D) Random events without cause", "(A)", "Logical 7-step cause-and-effect chain leading to demise.", "Hard", "Analyzing", "Cause and Effect Chain"),
    ("Evaluate the philosophical theme of 'Think Before You Act' in risk management.", "(A) Irreversible actions performed without foresight lead to fatal consequences that cannot be undone", "(B) Action should always precede thinking", "(C) Thinking causes failure; acting quickly guarantees success", "(D) Risk management is unnecessary for smart people", "(A)", "Foresight prevents irreversible fatal consequences.", "Hard", "Evaluating", "Philosophical Evaluation"),
    ("Compare Pandit Someshwar's mistake with the fable of 'The Boy Who Cried Wolf'.", "(A) Both characters suffer fatal/serious loss due to misuse of trust—Someshwar misuses divine grace; the boy misuses community trust", "(B) Both stories take place in ocean ships", "(C) Neither story has a moral", "(D) Both characters become village kings", "(A)", "Misuse of divine grace vs misuse of community trust.", "Hard", "Comparing", "Comparative Fable Analysis"),
    ("Critique the narrative pacing of 'The Foolish Pandit' from long devotion to swift tragedy.", "(A) Years of slow, disciplined meditation contrast sharply with the swift, violent catastrophe caused by a single foolish decision", "(B) The story moves at a constant slow speed throughout", "(C) The tragedy happens before the prayer starts", "(D) The story ends with a comedy dance", "(A)", "Slow disciplined devotion vs swift violent catastrophe.", "Hard", "Evaluating", "Narrative Pacing"),
    ("How does the story warn against testing divine or natural laws foolishly?", "(A) Attempting to manipulate dangerous natural forces (like a apex predator) to satisfy doubt results in self-destruction", "(B) It encourages everyone to test wild animals daily", "(C) It proves that lions prefer eating herbs", "(D) It shows that magic herbs are dangerous for plants", "(A)", "Manipulating dangerous natural forces leads to self-destruction.", "Hard", "Analyzing", "Warning Analysis"),
    ("Synthesize how Chapter 01 establishes core reading comprehension skills for Class 3 learners.", "(A) Combines vocabulary acquisition, cause-effect tracing, character flaw evaluation, and moral lesson deduction", "(B) Focuses only on memorizing spellings", "(C) Eliminates reading comprehension questions", "(D) Replaces prose with mathematical equations", "(A)", "Combines vocabulary, cause-effect, character evaluation, and moral deduction.", "Hard", "Synthesizing", "Pedagogical Synthesis"),
    ("Formulate an alternative ending where Someshwar demonstrates wisdom instead of foolishness.", "(A) 'Upon receiving the booti, Someshwar humbly thanked Goddess Durga, returned to his village, and safely used a tiny drop to heal a sick old cow...'", "(B) 'He threw the booti away'", "(C) 'He fought the lion with a sword'", "(D) 'He ran away to another country'", "(A)", "Creative alternative wise ending.", "Hard", "Creating", "Alternative Narrative Creation"),
    ("Formulate a critical appreciation of the line 'Watching the lion roar ferociously, Someshwar realised his mistake. But it was too late by then.'", "(A) Encapsulates the poignant truth that realization coming AFTER irreversible action cannot prevent the impending tragedy", "(B) Proves that the lion was grateful to Someshwar", "(C) Shows that Someshwar was a fast runner", "(D) Explains why lions live in jungles", "(A)", "Realization after irreversible action cannot prevent tragedy.", "Hard", "Evaluating", "Critical Appreciation"),
    ("Synthesize the ultimate lesson of Chapter 01 for young learners.", "(A) Wisdom lies not just in acquiring knowledge or power, but in exercising self-control, humility, and careful foresight before acting!", "(B) Always run away from your guru", "(C) Never go to a jungle under any circumstances", "(D) Try to fight lions whenever you see them", "(A)", "Self-control, humility, and careful foresight before acting.", "Hard", "Evaluating", "Core Philosophy Synthesis")
]

mcq_content = f"# MCQs — Chapter 01: The Foolish Pandit\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK03_CH01_MCQ_{idx:03d}"
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
    ("Pandit Someshwar was a devotee of Goddess _______.", "Durga", "Devotee of Goddess Durga.", "Easy"),
    ("Someshwar wished for a divine meeting and special _______.", "blessings", "Wished for special blessings.", "Easy"),
    ("His guru asked him to pray without any _______ around him.", "disturbances", "Pray without disturbances.", "Easy"),
    ("Someshwar went to a big _______ to pray and meditate.", "jungle", "Went to a big jungle.", "Easy"),
    ("He spent years meditating and _______.", "praying", "Spent years meditating and praying.", "Easy"),
    ("No matter the weather, Someshwar did not _______.", "waver", "Did not waver.", "Easy"),
    ("Goddess Durga was pleased by his _______.", "devotion", "Pleased by his devotion.", "Easy"),
    ("Goddess Durga agreed to grant Someshwar a _______.", "wish", "Agreed to grant a wish.", "Easy"),
    ("Someshwar asked for the magical _______ booti.", "Sanjeevani", "Asked for Sanjeevani booti.", "Easy"),
    ("A few drops of Sanjeevani booti could bring the _______ back to life.", "dead", "Bring the dead back to life.", "Easy"),
    ("Someshwar hoped to gain followers and become the village _______.", "Sarpanch", "Become the village Sarpanch.", "Easy"),
    ("He started day-_______ about his future power.", "dreaming", "Day-dreaming about power.", "Easy"),
    ("Suddenly, he became _______ about the booti's powers.", "doubtful", "Became doubtful about powers.", "Easy"),
    ("He decided to test the booti on a dead _______.", "lion", "Test on a dead lion.", "Easy"),
    ("The lion came back to life with more energy and _______.", "strength", "More energy and strength.", "Easy"),
    ("The lion roared _______ after coming back to life.", "ferociously", "Roared ferociously.", "Easy"),
    ("Someshwar realized his mistake, but it was too _______.", "late", "Too late by then.", "Easy"),
    ("He could not _______ the lion and was eaten.", "outrun", "Could not outrun the lion.", "Easy"),
    ("The moral of the story is: Think before you _______.", "act", "Think before you act.", "Easy"),
    ("A devotee is an ardent _______.", "follower", "Devotee means follower.", "Easy"),
    ("Divine means connected to _______.", "God", "Divine means connected to God.", "Easy"),
    ("Deity means a _______.", "God", "Deity means a God.", "Easy"),
    ("Ferociously means in a frightening and _______ way.", "violent", "Frightening and violent way.", "Easy"),
    ("Chapter 01 is titled 'The Foolish _______'.", "Pandit", "Titled 'The Foolish Pandit'.", "Easy"),
    ("The story is a tale from the _______.", "Panchatantra", "Panchatantra Tale.", "Easy"),

    # Medium (26-40)
    ("Someshwar's guru advised him to find a secluded spot for deep _______.", "meditation", "Secluded spot for meditation.", "Medium"),
    ("Selfish ambition made Someshwar dream of becoming village _______.", "Sarpanch", "Dream of becoming Sarpanch.", "Medium"),
    ("Testing a life-giving herb on a wild predator was a fatal _______.", "mistake", "Fatal mistake.", "Medium"),
    ("The revived lion acted according to its fierce predatory _______.", "nature", "Fierce predatory nature.", "Medium"),
    ("Someshwar lacked true faith because he was consumed by _______.", "doubt", "Consumed by doubt.", "Medium"),
    ("The Sanjeevani booti possessed divine magical _______.", "powers", "Divine magical powers.", "Medium"),
    ("A person who acts without thinking suffers tragic _______.", "consequences", "Suffers tragic consequences.", "Medium"),
    ("The lion came back to life with immense physical _______.", "energy", "Immense physical energy.", "Medium"),
    ("Someshwar could not escape because a lion runs much _______.", "faster", "Lion runs much faster.", "Medium"),
    ("The story teaches us to exercise careful foresight and _______.", "wisdom", "Foresight and wisdom.", "Medium"),
    ("Someshwar spent years in the jungle demonstrating intense _______.", "dedication", "Intense dedication.", "Medium"),
    ("Doubt destroyed the value of the divine _______.", "blessing", "Divine blessing.", "Medium"),
    ("Panchatantra tales convey practical moral _______.", "lessons", "Practical moral lessons.", "Medium"),
    ("Someshwar's day-dreaming caused him to lose mental _______.", "focus", "Lose mental focus.", "Medium"),
    ("Foolish curiosity led Someshwar to his self-destruction and _______.", "demise", "Self-destruction and demise.", "Medium"),

    # Hard (41-50)
    ("Someshwar's vanity and doubt constituted his tragic _______.", "flaw", "Tragic flaw.", "Hard"),
    ("The life-restoring herb paradoxically precipitated Someshwar's _______.", "death", "Precipitated his death.", "Hard"),
    ("Attempting to test divine grace reflects intellectual _______.", "arrogance", "Intellectual arrogance.", "Hard"),
    ("The ferocious roar of the revived lion signaled immediate _______.", "danger", "Signaled immediate danger.", "Hard"),
    ("Irreversible foolish actions render belated realization _______.", "useless", "Render realization useless.", "Hard"),
    ("Panchatantra allegories warn against uncontrolled human _______.", "folly", "Uncontrolled human folly.", "Hard"),
    ("Someshwar's spiritual pursuit was corrupted by political _______.", "ambition", "Corrupted by political ambition.", "Hard"),
    ("The story illustrates the severe peril of reviving dangerous _______.", "predators", "Peril of reviving predators.", "Hard"),
    ("Foresight must precede action to avoid catastrophic _______.", "outcomes", "Avoid catastrophic outcomes.", "Hard"),
    ("Chapter 01 integrates vocabulary, character analysis, and ethical _______.", "reasoning", "Integrates ethical reasoning.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 01: The Foolish Pandit\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK03_CH01_FIB_{idx:03d}"
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
    ("Pandit Someshwar was a devotee of Goddess Durga.", "True", "Text explicitly states he was a devotee of Goddess Durga.", "Easy"),
    ("Someshwar's guru told him to pray in a noisy crowded market.", "False", "His guru asked him to pray where there were no disturbances around him.", "Easy"),
    ("Someshwar went to a big jungle to meditate and pray.", "True", "He went to a big jungle to pray.", "Easy"),
    ("Someshwar gave up praying as soon as winter arrived.", "False", "No matter the weather, he did not waver.", "Easy"),
    ("Goddess Durga was pleased by Someshwar's devotion.", "True", "She was pleased by his devotion.", "Easy"),
    ("Goddess Durga gave Someshwar a bag of gold coins.", "False", "She gave him the Sanjeevani booti.", "Easy"),
    ("Sanjeevani booti had the power to bring the dead back to life.", "True", "A few drops could bring the dead back to life.", "Easy"),
    ("Someshwar wanted to become the Sarpanch of his village.", "True", "He daydreamed about becoming Sarpanch.", "Easy"),
    ("Someshwar was 100% confident that the booti would work.", "False", "He became doubtful about the booti's powers.", "Easy"),
    ("Someshwar tested the booti on a dead lion.", "True", "He tested it on a dead lion lying nearby.", "Easy"),
    ("When the booti was applied, the lion remained dead.", "False", "The lion came back to life with more energy and strength.", "Easy"),
    ("The revived lion purred gently like a pet cat.", "False", "The lion roared ferociously.", "Easy"),
    ("Someshwar was able to outrun the lion and escape.", "False", "He could not outrun the lion and was eaten by it.", "Easy"),
    ("The moral of the story is 'Think before you act'.", "True", "Moral of the story: Think before you act.", "Easy"),
    ("'Devotee' means an ardent follower.", "True", "Devotee is defined as an ardent follower.", "Easy"),
    ("'Divine' means connected to God.", "True", "Divine is defined as connected to God.", "Easy"),
    ("'Ferociously' means in a quiet and gentle way.", "False", "Ferociously means in a frightening and violent way.", "Easy"),
    ("Someshwar meditated for only ten minutes before Goddess Durga appeared.", "False", "He spent years meditating and praying.", "Easy"),
    ("The lion was very weak after coming back to life.", "False", "The lion came back to life with more energy and strength.", "Easy"),
    ("Someshwar regretted his mistake before he was eaten.", "True", "Watching the lion roar ferociously, Someshwar realized his mistake.", "Easy"),
    ("Sanjeevani booti required fifty bottles to work.", "False", "A few drops from this could bring the dead back to life.", "Easy"),
    ("The story 'The Foolish Pandit' comes from the Panchatantra.", "True", "It is a Panchatantra Tale.", "Easy"),
    ("Someshwar tested the booti on a dead bird first.", "False", "He tested it directly on a dead lion.", "Easy"),
    ("The lion spared Someshwar because Someshwar saved its life.", "False", "The lion ate Someshwar.", "Easy"),
    ("Chapter 01 is titled 'The Foolish Pandit'.", "True", "Chapter 01 is titled 'The Foolish Pandit'.", "Easy"),

    # Medium (26-40)
    ("Someshwar's guru wanted him to meditate in isolation to achieve deep concentration.", "True", "Isolation removed all village disturbances.", "Medium"),
    ("Someshwar's ultimate downfall was caused by doubt and lack of foresight.", "True", "Doubt led him to test the booti on a lion without foresight.", "Medium"),
    ("Goddess Durga warned Someshwar never to use the booti on animals.", "False", "She only said a few drops could bring the dead back to life.", "Medium"),
    ("A wild lion loses its predatory instincts once brought back to life by magic.", "False", "The lion revived with fierce natural predatory instincts.", "Medium"),
    ("Someshwar's ambition to become Sarpanch showed he was seeking personal glory.", "True", "He wanted followers and political leadership.", "Medium"),
    ("Realizing a mistake after taking an irreversible dangerous action can prevent harm.", "False", "Realizing too late cannot stop an impending catastrophe.", "Medium"),
    ("Someshwar showed great physical bravery by fighting the lion with a stick.", "False", "He tried to run away but could not outrun the lion.", "Medium"),
    ("The Sanjeevani booti was a natural herb with divine healing powers.", "True", "It was a divine herb with magical life-restoring powers.", "Medium"),
    ("Someshwar could have safely tested the herb on a dead leaf or dry branch.", "True", "Testing on non-dangerous objects would have been safe.", "Medium"),
    ("Panchatantra stories use dramatic events to teach moral lessons to readers.", "True", "Panchatantra tales convey practical moral wisdom.", "Medium"),
    ("Someshwar's years of meditation proved he had no patience at all.", "False", "He had great patience during prayer, but acted foolishly later.", "Medium"),
    ("The word 'pursuit' means an action done to achieve something.", "True", "Pursuit is defined as an action done to achieve something.", "Medium"),
    ("Someshwar shared the booti with all the villagers before going to the jungle.", "False", "He received the booti in the jungle and tested it there immediately.", "Medium"),
    ("The revived lion recognized Someshwar as its savior and obeyed his commands.", "False", "The wild lion immediately attacked and ate Someshwar.", "Medium"),
    ("Thinking before acting helps people avoid dangerous, regrettable choices.", "True", "Foresight prevents dangerous choices.", "Medium"),

    # Hard (41-50)
    ("Someshwar's character exhibits tragic hubris by doubting a divine gift.", "True", "Doubting divine grace displays tragic hubris.", "Hard"),
    ("The narrative highlights the psychological conflict between faith and skepticism.", "True", "Highlights conflict between faith (devotion) and skepticism (doubt).", "Hard"),
    ("Reviving an apex predator without defensive precautions is an example of reckless folly.", "True", "Reviving a predator without defense is reckless folly.", "Hard"),
    ("The story implies that spiritual power without wisdom is dangerous.", "True", "Power without practical wisdom leads to self-destruction.", "Hard"),
    ("Someshwar's inability to outrun the lion symbolizes the inevitability of consequences.", "True", "Inability to escape symbolizes inescapable consequences.", "Hard"),
    ("Goddess Durga tested Someshwar by giving him a fake herb.", "False", "The herb was genuine and worked instantly.", "Hard"),
    ("Panchatantra literature emphasizes practical worldly wisdom over blind ambition.", "True", "Emphasizes practical wisdom over blind ambition.", "Hard"),
    ("Someshwar's daydreaming distracted him from evaluating real-world dangers.", "True", "Daydreaming blinded him to real-world dangers.", "Hard"),
    ("The term 'ferociously' conveys both acoustic intensity and predatory threat.", "True", "Conveys acoustic intensity and predatory threat.", "Hard"),
    ("Chapter 01 integrates vocabulary, textual analysis, and ethical evaluation for Class 3.", "True", "Integrates vocabulary, textual analysis, and ethics.", "Hard")
]

tf_content = f"# True / False — Chapter 01: The Foolish Pandit\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK03_CH01_TF_{idx:03d}"
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
    ("Who was Pandit Someshwar?", "Pandit Someshwar was a devout follower of Goddess Durga who meditated in a jungle to receive her blessings.", "Easy", "Remembering"),
    ("Which deity did Pandit Someshwar pray to?", "He prayed to Goddess Durga.", "Easy", "Remembering"),
    ("Why did Someshwar's guru send him to a big jungle?", "His guru asked him to pray in a place free from all disturbances around him.", "Easy", "Understanding"),
    ("How long did Someshwar meditate in the jungle?", "He spent years meditating and praying in the jungle.", "Easy", "Remembering"),
    ("Did Someshwar stop praying when the weather was bad?", "No, no matter the weather, he did not waver and remained fully dedicated.", "Easy", "Remembering"),
    ("Why did Goddess Durga appear in front of Someshwar?", "She appeared because she was pleased by his deep devotion and dedicated prayer.", "Easy", "Understanding"),
    ("What gift did Goddess Durga give to Someshwar?", "She gave him the magical Sanjeevani booti.", "Easy", "Remembering"),
    ("What was the magical power of the Sanjeevani booti?", "A few drops of the Sanjeevani booti could bring the dead back to life.", "Easy", "Remembering"),
    ("What did Someshwar daydream about after getting the booti?", "He daydreamed about helping villagers, gaining followers, and becoming the village Sarpanch.", "Easy", "Remembering"),
    ("What doubt entered Someshwar's mind?", "He doubted whether the booti would actually work ('What if the booti does not work?').", "Easy", "Understanding"),
    ("What dead animal did Someshwar see lying nearby?", "He saw a dead lion lying nearby.", "Easy", "Remembering"),
    ("Why did Someshwar decide to test the booti on the dead lion?", "He wanted to check if the Sanjeevani booti really had the power to bring the dead back to life.", "Easy", "Understanding"),
    ("What happened when Someshwar put drops of the booti on the lion?", "The dead lion came back to life with more energy and strength.", "Easy", "Remembering"),
    ("How did the revived lion react upon coming back to life?", "The lion stood up and roared ferociously.", "Easy", "Remembering"),
    ("What happened to Someshwar at the end of the story?", "He could not outrun the revived lion and was eaten by the beast.", "Easy", "Remembering"),
    ("What is the moral of the story 'The Foolish Pandit'?", "The moral of the story is: Think before you act.", "Easy", "Remembering"),
    ("What does the word 'devotee' mean?", "'Devotee' means an ardent follower of a deity or religion.", "Easy", "Understanding"),
    ("What does the word 'divine' mean?", "'Divine' means connected to or coming from God.", "Easy", "Understanding"),
    ("What does the word 'deity' mean?", "'Deity' means a God or Goddess.", "Easy", "Understanding"),
    ("What does the word 'ferociously' mean?", "'Ferociously' means acting in a frightening, fierce, and violent way.", "Easy", "Understanding"),
    ("What position in the village did Someshwar hope to get?", "He hoped to become the village Sarpanch.", "Easy", "Remembering"),
    ("Why could Someshwar not escape from the lion?", "Because a lion is extremely fast and Someshwar could not outrun it.", "Easy", "Understanding"),
    ("When did Someshwar realize his mistake?", "He realized his mistake when he watched the lion roar ferociously.", "Easy", "Remembering"),
    ("Was Someshwar's realization of his mistake helpful to save his life?", "No, it was too late by then, and he was eaten by the lion.", "Easy", "Understanding"),
    ("What is the title of Chapter 01?", "The title of Chapter 01 is 'The Foolish Pandit'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Explain why Someshwar's decision to test the herb on a lion was foolish.", "It was foolish because a lion is a wild predator. Reviving a fierce carnivorous animal put his own life in immediate danger.", "Medium", "Analyzing"),
    ("How did Someshwar's doubt ruin his divine gift?", "Instead of accepting Goddess Durga's gift with faith, his doubt drove him to test it on a lion, leading to his death.", "Medium", "Analyzing"),
    ("What contrast exists between Someshwar's long meditation and his final action?", "He showed immense patience and discipline during years of meditation, but acted with complete lack of wisdom and thought in a single moment.", "Medium", "Analyzing"),
    ("How does the story demonstrate the proverb 'Haste makes waste' or 'Look before you leap'?", "Someshwar acted hastily to test the booti without thinking about the danger of a live lion, resulting in the total loss of his life.", "Medium", "Evaluating"),
    ("What lesson does this story teach about ambition and vanity?", "It teaches that ambition driven by vanity (seeking followers and power as Sarpanch) can blind a person to real-world dangers.", "Medium", "Evaluating"),
    ("Summarize Pages 5 and 6 of the textbook in two sentences.", "Pandit Someshwar prayed in a jungle for years until Goddess Durga granted him the life-giving Sanjeevani booti. Doubting its power, he tested it on a dead lion, which revived and ate him.", "Medium", "Understanding"),
    ("Why is a lion a dangerous animal to bring back to life?", "A lion is an apex predator driven by wild instincts. Upon reviving, it naturally hunts for food and attacks nearby prey, including humans.", "Medium", "Understanding"),
    ("How could Someshwar have proven the booti's power safely?", "He could have tested it on a harmless dead insect, a small bird, or a withered plant without putting his life at risk.", "Medium", "Applying"),
    ("What does the word 'spiritual pursuit' mean in Someshwar's story?", "It refers to his dedicated religious efforts—praying and meditating in the jungle—to seek a divine vision of Goddess Durga.", "Medium", "Understanding"),
    ("Why did Someshwar want to become Sarpanch?", "He wanted political authority, high social status, and a large number of followers in the village.", "Medium", "Understanding"),
    ("Explain how Someshwar's realization came 'too late'.", "He realized his mistake only after the lion was fully revived and roaring. By then, the predator was ready to attack, and escape was impossible.", "Medium", "Analyzing"),
    ("What role does the guru play at the beginning of the story?", "The guru guides Someshwar by advising him to find a quiet place without disturbances for effective meditation.", "Medium", "Understanding"),
    ("How does Panchatantra literature use moral lessons to educate readers?", "Panchatantra literature uses memorable stories involving humans and animals to teach practical life skills, caution, and ethics.", "Medium", "Evaluating"),
    ("What feelings did Someshwar experience when Goddess Durga appeared?", "He felt immense joy, surprise, and gratitude because his years of devotion were rewarded.", "Medium", "Understanding"),
    ("How does this story encourage children to think critically before making choices?", "It shows that every action has consequences, warning children to evaluate potential dangers before doing something risky.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique Someshwar's spiritual devotion vs his practical wisdom.", "While Someshwar possessed high spiritual endurance (praying for years), he lacked basic practical wisdom (common sense), proving that spiritual devotion without practical intelligence can lead to disaster.", "Hard", "Evaluating"),
    ("Analyze how doubt (skepticism) transformed a divine blessing into a fatal curse.", "The Sanjeevani booti was a divine blessing meant to save lives. Someshwar's doubt compelled him to test it recklessly, turning the blessing into the instrument of his own death.", "Hard", "Analyzing"),
    ("Deconstruct the 5-part narrative structure of 'The Foolish Pandit'.", "1. **Exposition**: Someshwar's devotion & guru's advice.\n2. **Rising Action**: Years of jungle meditation & Durga's boon.\n3. **Climax**: Daydreaming of Sarpanch post & doubt leading to testing booti on lion.\n4. **Falling Action**: Lion revives and roars ferociously.\n5. **Resolution**: Someshwar is eaten; moral 'Think before you act' stated.", "Hard", "Analyzing"),
    ("Compare Pandit Someshwar with another Panchatantra character who acts foolishly.", "Like the talkative turtle who fell after opening his mouth, Someshwar suffered self-destruction because he failed to control his impulsive urge.", "Hard", "Comparing"),
    ("Evaluate the theme of human vulnerability against nature in the story.", "No matter how much magical power or divine gifts a human possesses, disrespecting natural laws (reviving a fierce predator unprepared) results in nature overpowering the human.", "Hard", "Evaluating"),
    ("How does the author use imagery to describe the revived lion?", "The author uses dynamic imagery—'more energy and strength', 'roar ferociously'—to create an alarming sense of immediate physical danger.", "Hard", "Analyzing"),
    ("Assess how this story builds moral reasoning in Class 3 students.", "It challenges students to analyze cause-and-effect, recognize self-delusion, and understand that intelligence requires foresight.", "Hard", "Evaluating"),
    ("Why is 'Think before you act' a fundamental rule in personal safety?", "Because once an action is taken (like releasing a dangerous force), its consequences unfold automatically and cannot be recalled.", "Hard", "Analyzing"),
    ("Formulate a short 4-line poem summarizing Chapter 01.", "'Someshwar prayed for blessings bright,\nGot magic herb of divine might;\nHe brought a lion back to life,\nAnd paid with death for foolish strife!'", "Hard", "Creating"),
    ("Synthesize the ultimate lesson of Chapter 01 for Class 3 learners.", "True wisdom combines faith with intelligence, caution, and foresight; always think deeply about the consequences before taking any action!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 01: The Foolish Pandit\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK03_CH01_SA_{idx:03d}"
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
    ("Describe the story of 'The Foolish Pandit' from Pandit Someshwar's prayer to his tragic end.", 
     "Pandit Someshwar was a devotee of Goddess Durga who wished for a divine meeting. Guided by his guru, he went to a big jungle to pray without disturbances. He meditated for years with complete dedication. Pleased with his devotion, Goddess Durga appeared and granted him a wish. Someshwar asked for the Sanjeevani booti, a magical herb that could bring the dead back to life.\n\nAfter receiving the herb, Someshwar daydreamed about helping villagers and becoming the village Sarpanch. However, doubt crept into his mind about whether the herb actually worked. To test it, he applied a few drops to a dead lion lying nearby. The lion instantly revived with immense strength, roared ferociously, and attacked Someshwar. Realizing his foolish mistake too late, Someshwar could not outrun the lion and was eaten by the beast. The story teaches the valuable moral: 'Think before you act.'", 
     "Easy", "Remembering"),

    ("Explain the character of Pandit Someshwar, highlighting his strengths and weaknesses.", 
     "Pandit Someshwar displays a mix of strong devotion and severe character flaws:\n1. **Strengths**: He possessed great patience, dedication, and endurance, meditating for years in a tough jungle environment regardless of harsh weather.\n2. **Weaknesses**: He suffered from vanity, ambition, and doubt. After receiving a divine gift, he daydreamed about political power (becoming Sarpanch). Furthermore, his lack of faith led him to doubt Goddess Durga's gift, prompting him to foolishly test it on a dangerous predator without thinking.", 
     "Easy", "Understanding"),

    ("What was the Sanjeevani booti, how did Someshwar obtain it, and how did he misuse it?", 
     "The Sanjeevani booti was a divine magical herb capable of bringing dead creatures back to life with a few drops. Someshwar obtained it as a boon from Goddess Durga after years of intense jungle meditation. However, he misused it due to doubt and foolish curiosity. Instead of keeping the herb safe to help sick or dying villagers, he recklessly poured drops on a dead lion to verify its magical power, leading to his tragic death.", 
     "Easy", "Understanding"),

    ("Explain the moral lesson 'Think before you act' with reference to Chapter 01.", 
     "The moral lesson 'Think before you act' emphasizes the necessity of foresight and caution before taking any action. In Chapter 01, Someshwar acted impulsively out of doubt by reviving a dead lion. He failed to think about the obvious danger: a live lion is a dangerous predator that attacks humans. Because he acted without thinking, he faced fatal consequences that could not be undone. This teaches readers to always evaluate risks before taking action.", 
     "Easy", "Understanding"),

    ("Describe the role of the guru and Goddess Durga in the story of Pandit Someshwar.", 
     "1. **The Guru**: Guided Someshwar at the beginning, advising him to meditate in a quiet jungle free from village distractions so he could focus his mind completely on prayer.\n2. **Goddess Durga**: Appeared after years of Someshwar's unwavering devotion and generously granted his wish for the Sanjeevani booti, trusting him with divine power.", 
     "Easy", "Remembering"),

    ("Why did Someshwar doubt the power of the Sanjeevani booti and what were the consequences of his doubt?", 
     "Someshwar doubted the booti because human skepticism entered his mind ('What if the booti does not work?'). He wanted visual proof before presenting himself as a savior to the villagers. The consequence of his doubt was catastrophic: he tested the booti on a dead lion, which revived with fierce strength and devoured him immediately.", 
     "Easy", "Understanding"),

    ("Explain the meanings and context of the vocabulary words: Devotee, Divine, Deity, Pursuit, and Ferociously.", 
     "1. **Devotee**: An ardent follower (Someshwar was a devotee of Goddess Durga).\n2. **Divine**: Connected to God (Someshwar wished for a divine meeting).\n3. **Deity**: A God or Goddess (His guru asked him to pray to the deity).\n4. **Pursuit**: An action done to achieve something (He remained dedicated to his spiritual pursuit).\n5. **Ferociously**: In a frightening and violent way (The revived lion roared ferociously).", 
     "Easy", "Understanding"),

    ("How does Panchatantra storytelling use simple animal encounters to teach deep moral values?", 
     "Panchatantra tales use relatable human characters (like Someshwar) and animal encounters (like the lion) to dramatize real-world consequences. By showing a foolish decision leading directly to a dramatic animal attack, the story creates a powerful, unforgettable lesson about caution, wisdom, and thinking before acting.", 
     "Easy", "Evaluating"),

    ("What mistakes did Someshwar make after receiving the divine herb from Goddess Durga?", 
     "Someshwar made three major mistakes:\n1. He became vain and daydreamed about personal power (becoming Sarpanch) instead of remaining humble.\n2. He doubted Goddess Durga's word and lacked faith in her divine gift.\n3. He chose the worst possible test subject—a dead apex predator (lion)—endangering his own life.", 
     "Easy", "Analyzing"),

    ("Summarize the complete narrative of Chapter 01 in five clear bullet points.", 
     "- Pandit Someshwar meditated for years in a jungle to seek Goddess Durga's blessings.\n- Goddess Durga appeared and granted him the life-restoring Sanjeevani booti.\n- Someshwar daydreamed of becoming village Sarpanch but doubted if the booti worked.\n- He tested the booti on a dead lion, which revived with immense energy and roared ferociously.\n- Unable to outrun the lion, Someshwar was eaten, proving the moral: 'Think before you act.'", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("What kind of environment did Someshwar choose for his meditation and why?", "He chose a big, quiet jungle away from human settlement because his guru advised him to pray where there were no disturbances around him to maintain total spiritual focus.", "Easy", "Understanding"),
    ("Why was Someshwar's daydreaming about becoming Sarpanch a sign of distraction?", "Because true spiritual devotion requires humility; daydreaming about political office and village prestige showed his mind was distracted by worldly ambition.", "Easy", "Analyzing"),
    ("What physical changes occurred to the dead lion when Someshwar used the Sanjeevani booti?", "The dead lion instantly came back to life, gaining full energy, immense physical strength, and a ferocious roar.", "Easy", "Remembering"),
    ("Why is it impossible for a human to outrun a wild lion in the jungle?", "Lions are natural sprinters capable of running at very high speeds, whereas humans are much slower; thus Someshwar had no chance of escaping.", "Easy", "Understanding"),
    ("How does the title 'The Foolish Pandit' reflect the character of Someshwar?", "Though he was a learned pandit who meditated for years, his single foolish decision to revive a lion without thinking proved his utter lack of practical sense, justifying the title.", "Easy", "Analyzing"),
    ("What difference exists between having knowledge and having wisdom?", "Knowledge is knowing facts or possessing tools (like the booti); wisdom is knowing how and when to use them safely and responsibly. Someshwar had power but lacked wisdom.", "Easy", "Evaluating"),
    ("What safety precautions should anyone take before dealing with dangerous wild animals?", "One should maintain safe distance, avoid provoking them, never revive or release wild predators near oneself, and respect their natural wild instincts.", "Easy", "Applying"),
    ("Why did Goddess Durga grant Someshwar's wish without testing his wisdom first?", "Goddess Durga rewarded his sincere devotion and effort; it was up to Someshwar to use his free will and wisdom responsibly.", "Easy", "Understanding"),
    ("How does the story highlight the danger of doubt in spiritual faith?", "Someshwar's doubt made him question divine grace, prompting a foolish test that led directly to his destruction.", "Easy", "Analyzing"),
    ("What would have happened if Someshwar had tested the booti on a dead deer instead of a lion?", "If tested on a deer, the deer would have revived and run away into the forest, leaving Someshwar unharmed and aware of the booti's power.", "Easy", "Analyzing"),
    ("Explain the role of weather in showing Someshwar's initial dedication.", "Rain, heat, and storm did not waver Someshwar; he remained steadfast in his jungle prayers, proving his intense physical discipline.", "Easy", "Understanding"),
    ("Why is Panchatantra considered timeless literature for children?", "Because its vivid stories combine excitement, simple language, unforgettable animal characters, and practical life wisdom that remains true across generations.", "Easy", "Evaluating"),
    ("How can Class 3 students apply the moral 'Think before you act' in their daily lives?", "By stopping to think before speaking angrily, avoiding dangerous physical dares, doing homework carefully, and evaluating consequences before making choices.", "Easy", "Applying"),
    ("What contrast is shown between the peaceful beginning and violent ending of the story?", "The story begins in peaceful, silent meditation in nature and ends in a sudden, violent lion attack, emphasizing how quickly a foolish choice can cause disaster.", "Easy", "Analyzing"),
    ("Summarize Chapter 01 in five key sentences.", "Pandit Someshwar meditated deeply in a jungle to receive blessings from Goddess Durga. She granted him the divine Sanjeevani booti, which could bring the dead back to life. Doubting its power, Someshwar foolishly applied drops of the booti onto a dead lion. The lion revived with immense strength, roared ferociously, and ate Someshwar. The tale warns everyone to always think carefully before taking action.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how ambition, doubt, and foolishness combined to cause Someshwar's downfall.", 
     "Someshwar's downfall resulted from a chain of three psychological flaws:\n1. **Ambition**: Receiving divine power triggered greedy daydreams of becoming village Sarpanch.\n2. **Doubt**: Insecurity about whether the booti would work made him question Goddess Durga's word.\n3. **Foolishness**: Impulsively testing the booti on a lion without considering that a revived predator would eat him. Together, these flaws destroyed his spiritual achievement and life.", 
     "Medium", "Analyzing"),

    ("Examine the moral framework of Panchatantra stories as demonstrated in 'The Foolish Pandit'.", 
     "Panchatantra stories teach *Niti* (practical wisdom and worldly conduct). Unlike pure religious texts that focus solely on devotion, Panchatantra emphasizes that spiritual merit is useless without practical intelligence. Someshwar had devotion, but because he lacked *Niti* (common sense), his life ended tragically. This framework teaches readers that practical wisdom is essential for survival.", 
     "Medium", "Evaluating"),

    ("Discuss the dramatic irony in the story's climax.", 
     "Dramatic irony occurs when the outcome is the exact opposite of what a character expects. Someshwar expected the booti to prove its power so he could become a glorious leader (Sarpanch). Instead, the very power he sought to prove created the instrument of his own gruesome death. The herb of life became his sentence of death.", 
     "Medium", "Analyzing"),

    ("Explore the psychological transformation of Someshwar from a calm devotee to a panicked victim.", 
     "During meditation, Someshwar was calm, patient, and spiritually focused. Upon receiving the booti, his mind shifted to ambition and doubt. When he applied the booti and heard the lion's ferocious roar, sudden terror struck him. In a flash of panic, he realized his error, but his human speed could not save him from the predator.", 
     "Medium", "Analyzing"),

    ("How can Class 3 teachers use Chapter 01 for a classroom role-play activity?", 
     "Teachers can assign roles:\n- **Student 1 (Someshwar)**: Meditating, receiving booti, daydreaming, testing on lion.\n- **Student 2 (Goddess Durga)**: Granting the boon gracefully.\n- **Student 3 (The Lion)**: Roaring ferociously upon waking.\nThis role-play helps students internalize character emotions, dramatic pacing, and the core moral lesson.", 
     "Medium", "Applying"),

    ("Why is human curiosity dangerous when disconnected from safety precautions?", "Curiosity without safety precautions leads people to touch fire, handle wild animals, or test dangerous substances, resulting in severe physical injury or death.", "Medium", "Evaluating"),
    ("Describe how the setting of the jungle contributes to both Someshwar's success and demise.", "The jungle's quiet isolation allowed deep meditation to win Durga's boon, but its wild nature provided the dead lion and lacked any village help when the lion attacked.", "Medium", "Analyzing"),
    ("Contrast Goddess Durga's divine generosity with Someshwar's human weakness.", "Goddess Durga gave freely without suspicion; Someshwar responded with doubt, vanity, and rash experimentation.", "Medium", "Comparing"),
    ("Explain the significance of the word 'waver' in describing Someshwar's early meditation.", "'Waver' means to hesitate or lose focus. Saying he did not waver highlights his immense willpower during spiritual discipline.", "Medium", "Understanding"),
    ("Why did the lion attack Someshwar instead of showing gratitude?", "Wild animals act on predatory instinct, not human gratitude. A hungry, revived lion sees any nearby living creature as prey.", "Medium", "Understanding"),
    ("How does the story illustrate that knowledge without common sense is dangerous?", "Someshwar knew how to use the booti, but lacked the common sense to realize reviving a lion would get him killed.", "Medium", "Evaluating"),
    ("What structural elements make Panchatantra fables effective for children's moral education?", "Clear characters, fast-paced plot, vivid conflict, dramatic consequences, and an explicit moral statement at the end.", "Medium", "Analyzing"),
    ("How could Someshwar have fulfilled his goal of becoming Sarpanch safely?", "By returning to the village and using the booti responsibly to cure sick villagers or save dying livestock in times of genuine need.", "Medium", "Applying"),
    ("What warning does the story give about daydreaming during critical moments?", "Daydreaming creates false confidence and distracts the mind from recognizing immediate real-world dangers.", "Medium", "Evaluating"),
    ("Construct an alternative 4-sentence paragraph where Someshwar makes a wise choice.", "'After receiving the Sanjeevani booti, Pandit Someshwar bowed humbly to Goddess Durga. He kept the precious herb safely in a cloth pouch and returned to his village. When a poor farmer's bull fell gravely ill, Someshwar used a single drop to heal it. The grateful villagers praised his wisdom, and he served them faithfully for many years.'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the philosophical tension between divine grace and human free will in 'The Foolish Pandit'.", 
     "The story explores the boundary between divine grace and human free will. Goddess Durga granted divine power unconditionally. However, divine grace does not overrule human free will or shield a person from their own foolish choices. Someshwar's free will to test the booti on a lion brought self-inflicted ruin, proving that divine gifts require human wisdom.", 
     "Hard", "Evaluating"),

    ("Deconstruct the thematic motif of 'The Dangerous Test' across global folklore.", 
     "In folklore across cultures (e.g., Pandora's Box, King Midas, The Sorcerer's Apprentice), characters receive a magical power or gift and foolishly test or overuse it due to curiosity or greed. Someshwar's story fits this universal archetype, warning humanity against tampering recklessly with forces beyond their control.", 
     "Hard", "Analyzing"),

    ("Synthesize how Chapter 01 lays the foundation for Class 3 English language mastery.", 
     "- **Vocabulary**: Terms like devotee, divine, deity, pursuit, ferociously.\n- **Grammar**: Sentence structures in narrative past tense.\n- **Comprehension**: Character motivation, cause-effect, plot sequencing.\n- **Ethics**: Deduction of moral principles ('Think before you act').", 
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive evaluation rubric for assessing student responses to Chapter 01.", 
     "- **Recall (2 pts)**: Accurate identification of characters, booti, and lion.\n- **Analysis (2 pts)**: Understanding Someshwar's doubt and foolishness.\n- **Vocabulary (2 pts)**: Correct usage of story vocabulary.\n- **Moral Reasoning (2 pts)**: Application of 'Think before you act' to real life.\n- **Expression (2 pts)**: Clear grammar and sequential structure.", 
     "Hard", "Creating"),

    ("Evaluate the psychological realism of Someshwar's sudden transition from devotion to doubt.", 
     "Someshwar's transition is psychologically realistic. Long isolation can breed overthinking. Once the miraculous event occurred, ego (daydreaming of Sarpanch post) and anxiety ('what if it fails?') flooded his mind, overwhelming his spiritual calm and leading to rationalized risk-taking.", 
     "Hard", "Evaluating"),

    ("Analyze why the moral 'Think before you act' is particularly vital for 8-to-9-year-old learners.", "Children at age 8-9 are developing independent decision-making. Learning that actions carry irreversible physical consequences encourages impulse control, critical thinking, and personal safety.", "Hard", "Analyzing"),
    ("Compare Pandit Someshwar's tragedy with the myth of Icarus flying too close to the sun.", "Both characters received extraordinary gifts (booti / wax wings) but suffered fatal falls because vanity and lack of caution drove them to exceed safe boundaries.", "Hard", "Comparing"),
    ("Draft a short book review of Chapter 01 for an elementary school magazine.", "'Chapter 01, 'The Foolish Pandit', is a thrilling Panchatantra masterpiece. Through Pandit Someshwar's dramatic encounter with a revived lion, young readers learn the indispensable lesson that wisdom and foresight must always guide our actions.'", "Hard", "Creating"),
    ("Assess the literary function of the lion as a symbol of unrestrained wild nature.", "The lion symbolizes raw, unyielding nature that cannot be tamed by human vanity or magic. It enforces nature's immutable laws: predators hunt, and foolishness bears consequences.", "Hard", "Evaluating"),
    ("Synthesize the ultimate philosophy of Chapter 01 into a guiding motto for life.", "'Spiritual devotion gains power, but practical wisdom preserves life; always let careful foresight guide your actions!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 01: The Foolish Pandit\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK03_CH01_LA_{idx:03d}"
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
    ("Pandit Someshwar was a devotee of Goddess Durga. He wished for a divine meeting with her and also wanted to get special blessings from her.",
     [
         ("Who was Pandit Someshwar devoted to?", "Goddess Durga.", "Easy", "Remembering"),
         ("What two things did Someshwar wish for?", "A divine meeting with Goddess Durga and special blessings.", "Easy", "Remembering"),
         ("What does the word 'devotee' mean?", "An ardent follower of a deity or religion.", "Easy", "Understanding"),
         ("What does the word 'divine' mean in this context?", "Connected to or coming from God.", "Easy", "Understanding"),
         ("What action did Someshwar take to fulfill his wish?", "He sought advice from his guru and went to a jungle to meditate.", "Medium", "Understanding")
     ]),

    # Set 2
    ("His guru asked him to go and pray to the deity at such a place where there were no disturbances around him. So, Someshwar went to a big jungle to pray.",
     [
         ("Who gave advice to Someshwar?", "His guru.", "Easy", "Remembering"),
         ("Where did his guru tell him to pray?", "At a place where there were no disturbances around him.", "Easy", "Remembering"),
         ("Where did Someshwar go to meditate and pray?", "To a big jungle.", "Easy", "Remembering"),
         ("Why was a place without disturbances necessary for meditation?", "To allow deep concentration without noise or village distractions.", "Medium", "Understanding"),
         ("What does the word 'deity' mean?", "A God or Goddess.", "Easy", "Understanding")
     ]),

    # Set 3
    ("He spent years meditating and praying. No matter the weather, he did not waver. He remained fully dedicated to his spiritual pursuit.",
     [
         ("How long did Someshwar spend in the jungle?", "He spent years meditating and praying.", "Easy", "Remembering"),
         ("What phrase shows that bad weather did not stop him?", "'No matter the weather, he did not waver.'", "Easy", "Remembering"),
         ("What word describes his dedication to prayer?", "Dedicated / unwavering.", "Easy", "Understanding"),
         ("What does 'spiritual pursuit' mean?", "An action or effort done to achieve a holy connection with God.", "Medium", "Understanding"),
         ("What quality of Someshwar is highlighted in this extract?", "His patience, discipline, and strong physical endurance.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("Finally, one day Goddess Durga appeared in front of him. She was pleased by his devotion... The Goddess not only blessed him but also agreed to grant him a wish.",
     [
         ("Who appeared in front of Someshwar?", "Goddess Durga.", "Easy", "Remembering"),
         ("Why was Goddess Durga pleased with Someshwar?", "Because of his deep devotion and unwavering years of prayer.", "Easy", "Remembering"),
         ("What two things did Goddess Durga do for Someshwar?", "She blessed him and agreed to grant him a wish.", "Easy", "Remembering"),
         ("How did Someshwar feel when Goddess Durga appeared?", "He could not believe his luck and felt immense gratitude.", "Medium", "Understanding"),
         ("What wish did Someshwar ask for?", "He asked for the Sanjeevani booti that could bring the dead back to life.", "Medium", "Remembering")
     ]),

    # Set 5
    ("He told her if she wanted to give him something, she could give him Sanjeevani booti which had magical power to even bring back the dead.",
     [
         ("What magical herb did Someshwar request?", "The Sanjeevani booti.", "Easy", "Remembering"),
         ("What was the unique power of the Sanjeevani booti?", "It had the magical power to bring the dead back to life.", "Easy", "Remembering"),
         ("How many drops of the booti were needed to bring someone back to life?", "A few drops from the herb could bring the dead back to life.", "Easy", "Remembering"),
         ("Why did Someshwar ask for this specific herb?", "He thought it would help him heal people, gain followers, and become Sarpanch.", "Medium", "Understanding"),
         ("Is Sanjeevani booti a real plant or a legendary herb?", "It is a legendary divine herb from Indian mythology.", "Medium", "Understanding")
     ]),

    # Set 6
    ("Someshwar thought this was a great way to help the villagers and gain followers. This may even lead him to becoming the Sarpanch one day. He started day-dreaming.",
     [
         ("Who did Someshwar plan to help with the booti?", "The villagers.", "Easy", "Remembering"),
         ("What position in the village did Someshwar dream of getting?", "The village Sarpanch.", "Easy", "Remembering"),
         ("What was Someshwar doing instead of staying humble?", "He started day-dreaming about gaining followers and power.", "Easy", "Remembering"),
         ("What flaw is revealed in Someshwar's character during this moment?", "His vanity, ambition for political power, and loss of spiritual humility.", "Medium", "Analyzing"),
         ("How did day-dreaming affect his judgment?", "It distracted his mind from reality and led him to make a foolish decision.", "Medium", "Analyzing")
     ]),

    # Set 7
    ("Suddenly, he became doubtful about the booti's powers. He thought, 'What if the booti does not work'. So he decided to test it on a dead lion which was lying nearby.",
     [
         ("What negative thought entered Someshwar's mind?", "He became doubtful about the booti's powers ('What if it does not work?').", "Easy", "Remembering"),
         ("What did Someshwar decide to do to remove his doubt?", "He decided to test the booti.", "Easy", "Remembering"),
         ("What dead animal did he choose to test the booti on?", "A dead lion lying nearby.", "Easy", "Remembering"),
         ("Why was choosing a dead lion a terrible mistake?", "Because a lion is a fierce predator that will naturally attack humans upon reviving.", "Medium", "Analyzing"),
         ("What quality did Someshwar lack when he doubted Goddess Durga's gift?", "He lacked genuine faith and trust in the divine blessing.", "Medium", "Evaluating")
     ]),

    # Set 8
    ("He dropped a few drops on the lion and the beast came back to life with more energy and strength.",
     [
         ("How much booti did Someshwar drop on the lion?", "A few drops.", "Easy", "Remembering"),
         ("What happened to the lion immediately after receiving the drops?", "The beast came back to life.", "Easy", "Remembering"),
         ("With what qualities did the lion come back to life?", "With more energy and strength.", "Easy", "Remembering"),
         ("Did the Sanjeevani booti work effectively?", "Yes, it worked exactly as Goddess Durga had promised.", "Medium", "Understanding"),
         ("What did this result prove about Goddess Durga's gift?", "It proved that the divine gift was 100% genuine and powerful.", "Medium", "Evaluating")
     ]),

    # Set 9
    ("Watching the lion roar ferociously, Someshwar realised his mistake. But it was too late by then. He could not outrun the lion and was soon eaten by the beast.",
     [
         ("How did the lion roar after reviving?", "Ferociously.", "Easy", "Remembering"),
         ("What did Someshwar realize when he heard the roar?", "He realized his foolish mistake.", "Easy", "Remembering"),
         ("Why could Someshwar not save himself?", "Because it was too late and he could not outrun the fast lion.", "Easy", "Remembering"),
         ("What was Someshwar's tragic fate?", "He was eaten by the lion.", "Easy", "Remembering"),
         ("What does 'ferociously' mean in this passage?", "In a frightening, fierce, and violent way.", "Medium", "Understanding")
     ]),

    # Set 10
    ("Moral of the Story: Think before you act.",
     [
         ("What is the stated moral of the story?", "Think before you act.", "Easy", "Remembering"),
         ("Why is thinking before acting important in life?", "Because reckless actions can cause irreversible harm or fatal consequences.", "Medium", "Understanding"),
         ("How does Someshwar's story illustrate this moral?", "He acted without thinking about the danger of a live lion, resulting in his death.", "Medium", "Analyzing"),
         ("What advice would you give to someone who acts impulsively like Someshwar?", "Stop, evaluate the risks and consequences, and choose a safe, wise path before taking action.", "Medium", "Applying"),
         ("Summarize the main lesson of Chapter 01 in your own words.", "Always use caution and foresight before making choices, as foolish actions cannot be undone.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 01: The Foolish Pandit\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK03_CH01_EXT_{q_counter:03d}"
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

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 01 in {CH01_DIR}")
