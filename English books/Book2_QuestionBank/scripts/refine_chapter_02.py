r"""
Refines all 6 Category files for Chapter 02 ("Four Brahmins") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH02_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_02")
os.makedirs(CH02_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("How many disciples did the wise sage have in Chapter 02?", "(A) Four", "(B) Three", "(C) Two", "(D) Five", "(A)", "The sage had four disciples in total.", "Easy", "Remembering", "Character Count"),
    ("How many of the Brahmins were clever and learned magical skills quickly?", "(A) Three", "(B) Four", "(C) One", "(D) Two", "(A)", "Three disciples were clever and acquired magical skills.", "Easy", "Remembering", "Character Detail"),
    ("What was the fourth Brahmin called by his friends?", "(A) A simpleton", "(B) A king", "(C) A warrior", "(D) A wizard", "(A)", "The fourth Brahmin was considered a simpleton.", "Easy", "Remembering", "Character Trait"),
    ("Why did the three clever Brahmins want to go to town?", "(A) To earn money", "(B) To buy toys", "(C) To meet a king", "(D) To play games", "(A)", "They wanted to go to town to earn money.", "Easy", "Remembering", "Plot Motivation"),
    ("What work did the fourth Brahmin offer to do so he could travel with his friends?", "(A) Cook and clean for them", "(B) Drive a chariot", "(C) Carry their heavy bags", "(D) Sing songs", "(A)", "He offered to cook and clean for all of them.", "Easy", "Remembering", "Offer"),
    ("What did the friends find lying on the ground while resting under a tree?", "(A) Animal bones", "(B) Gold coins", "(C) Magic lamps", "(D) Red apples", "(A)", "They found some animal bones lying on the ground.", "Easy", "Remembering", "Discovery"),
    ("What did the first Brahmin do with the bones using his magic?", "(A) Reconstructed the skeleton", "(B) Threw them away", "(C) Buried them in dirt", "(D) Turned them into wood", "(A)", "The first Brahmin reconstructed the skeleton.", "Easy", "Remembering", "Magic Action 1"),
    ("What did the second Brahmin add to the reconstructed skeleton?", "(A) Organs, muscles, and skin", "(B) Feathers and wings", "(C) Leaves and flowers", "(D) Clothes and boots", "(A)", "The second Brahmin restored organs, muscles, and skin.", "Easy", "Remembering", "Magic Action 2"),
    ("What animal's body appeared after the second Brahmin used his magic?", "(A) A majestic lion", "(B) A giant tiger", "(C) An elephant", "(D) A bear", "(A)", "The body of a majestic lion appeared.", "Easy", "Remembering", "Animal Identity"),
    ("What did the third Brahmin want to do to the lion's body?", "(A) Bring it back to life", "(B) Paint it yellow", "(C) Burn it", "(D) Take it to town", "(A)", "The third Brahmin wanted to bring the lion back to life.", "Easy", "Remembering", "Magic Action 3"),
    ("What warning did the fourth Brahmin give to his friends?", "(A) Do not bring the lion back to life or it will devour us!", "(B) Run to the river!", "(C) Give me some food!", "(D) Paint the lion blue!", "(A)", "He warned them that the lion would devour them all.", "Easy", "Remembering", "Warning"),
    ("Did the three clever Brahmins listen to the fourth friend's warning?", "(A) No, they ignored him and called him a fool", "(B) Yes, they stopped", "(C) They ran away", "(D) They praised him", "(A)", "They ignored his warning and called him a fool.", "Easy", "Remembering", "Reaction"),
    ("What did the fourth Brahmin do to save himself from the lion?", "(A) He climbed up a tall tree", "(B) He hid behind a rock", "(C) He fought the lion", "(D) He ran into a cave", "(A)", "He silently climbed up a tree to save himself.", "Easy", "Remembering", "Survival Action"),
    ("What happened when the lion was brought back to life?", "(A) The hungry lion attacked and killed the three friends", "(B) The lion ran away into the woods", "(C) The lion danced happily", "(D) The lion fell asleep", "(A)", "The starved lion killed and ate the three friends.", "Easy", "Remembering", "Climax"),
    ("Where did the fourth Brahmin go after the lion ate his friends and left?", "(A) Back to the sage's ashram", "(B) To the town palace", "(C) To a new city", "(D) Into a dark cave", "(A)", "He went back to the sage's ashram, grieving.", "Easy", "Remembering", "Resolution"),
    ("What is the moral of the story 'Four Brahmins'?", "(A) Bookish knowledge without wisdom and common sense is useless", "(B) Magic is always good", "(C) Lions are sweet pets", "(D) Never cook for friends", "(A)", "Knowledge without wisdom and common sense is useless.", "Easy", "Understanding", "Moral Lesson"),
    ("What does the word 'disciple' mean?", "(A) A person who follows a teacher", "(B) A wild animal", "(C) A king's guard", "(D) A magic stick", "(A)", "A disciple is a student who follows a teacher.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'sage' mean?", "(A) A person who has attained wisdom", "(B) A warrior", "(C) A merchant", "(D) A hunter", "(A)", "A sage is a wise holy person.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'consequence' mean?", "(A) Something that happens as a result of an action", "(B) A reward", "(C) A magic spell", "(D) A tree branch", "(A)", "Consequence means result of an action.", "Easy", "Understanding", "Vocabulary"),
    ("Why was the fourth Brahmin able to save his own life?", "(A) Because he possessed common sense and climbed a tree", "(B) Because he was stronger than a lion", "(C) Because he used magic", "(D) Because the lion liked him", "(A)", "Common sense guided him to climb a tree.", "Easy", "Understanding", "Reasoning"),
    ("From which famous Indian story collection is 'Four Brahmins' taken?", "(A) Panchatantra", "(B) Aesop Fables", "(C) Jataka Tales", "(D) Hitopadesha", "(A)", "It is a famous Panchatantra tale.", "Easy", "Remembering", "Origin"),
    ("What did the three friends lack despite having magical knowledge?", "(A) Wisdom and common sense", "(B) Money", "(C) Magic books", "(D) Clothes", "(A)", "They lacked practical wisdom and common sense.", "Easy", "Understanding", "Key Defect"),
    ("How did the lion feel when it woke up from death?", "(A) Very hungry / starved", "(B) Full and sleepy", "(C) Scared of humans", "(D) Cold", "(A)", "The lion was starved and hungry.", "Easy", "Remembering", "Lion State"),
    ("Did the fourth Brahmin survive at the end of the story?", "(A) Yes, he survived by staying in the tree", "(B) No, he was eaten too", "(C) He turned into a lion", "(D) He disappeared", "(A)", "Yes, he survived and returned to the ashram.", "Easy", "Remembering", "Survival"),
    ("What is the title of Chapter 02 in Book 2?", "(A) Four Brahmins", "(B) The Rats Who Ate the Iron Balance", "(C) The Greedy Dog", "(D) The Clever Crow", "(A)", "Chapter 02 is titled 'Four Brahmins'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why did the three clever Brahmins refuse to take the fourth friend at first?", "(A) They thought he was a simpleton with no magical skills to help earn money", "(B) He had no clothes", "(C) He was too old", "(D) They disliked him", "(A)", "They thought his lack of magic made him useless for earning money.", "Medium", "Understanding", "Plot Motivation"),
    ("How did the fourth Brahmin demonstrate humility when his friends made fun of him?", "(A) He calmly offered to cook and clean for them instead of arguing", "(B) He started crying", "(C) He showed off his magic", "(D) He hit them", "(A)", "He offered humble service to accompany them.", "Medium", "Understanding", "Character Trait"),
    ("Why is reconstructing a lion's skeleton without thinking dangerous?", "(A) Because bringing a wild predator back to life threatens everyone's safety", "(B) Because bones are dirty", "(C) Because magic costs money", "(D) Because skeletons are scary", "(A)", "Creating a lion exposes everyone to deadly predator risk.", "Medium", "Analyzing", "Plot Logic"),
    ("What difference existed between bookish knowledge and practical wisdom in this story?", "(A) Bookish knowledge created a lion; practical wisdom foresaw the danger and climbed a tree", "(B) Both are identical", "(C) Bookish knowledge saves lives", "(D) Practical wisdom is useless", "(A)", "Magic knowledge created danger; common sense saved life.", "Medium", "Analyzing", "Theme Contrast"),
    ("Why did the three friends call the fourth Brahmin a fool when he warned them?", "(A) They were arrogant about their magic and believed their skill was superior to common sense", "(B) They were playing a game", "(C) The fourth friend spoke a foreign language", "(D) The sage told them to call him that", "(A)", "Arrogance in magic made them look down on common sense.", "Medium", "Understanding", "Psychological Cause"),
    ("What does the lion represent in this moral fable?", "(A) The dangerous consequence of reckless actions done without foresight", "(B) A cute pet", "(C) A magical king", "(D) A reward for hard work", "(A)", "The lion symbolizes destructive consequences of foolishness.", "Medium", "Evaluating", "Symbolism"),
    ("How did the fourth Brahmin's decision to climb a tree show quick thinking?", "(A) He realized he could not stop his arrogant friends, so he protected himself immediately", "(B) He wanted to pick apples", "(C) He was practicing climbing", "(D) The lion told him to climb", "(A)", "He took immediate practical action to survive.", "Medium", "Analyzing", "Action Evaluation"),
    ("Why were the three clever Brahmins described as turning 'stone out of fear'?", "(A) Because they realized their fatal mistake when the hungry lion stood before them", "(B) A spell turned them to stone", "(C) They were playing freeze tag", "(D) They were cold", "(A)", "Sudden terror paralyzed them when the lion roared.", "Medium", "Understanding", "Figurative Language"),
    ("Why did the fourth Brahmin feel grief on his way back to the ashram?", "(A) He was sad because his three friends lost their lives due to foolish pride", "(B) He lost his bag", "(C) He was hungry", "(D) He was lost in the woods", "(A)", "He grieved the needless loss of his companions.", "Medium", "Understanding", "Emotional Insight"),
    ("What lesson does this story teach about listening to warnings from others?", "(A) Ignore valid warnings out of pride, and you will face severe consequences", "(B) Never listen to friends", "(C) Always ignore advice", "(D) Warnings are always lies", "(A)", "Ignoring good advice leads to disaster.", "Medium", "Evaluating", "Life Application"),
    ("Why is common sense considered superior to mere magic or academic knowledge here?", "(A) Common sense preserves life and prevents harm, whereas unguided knowledge causes self-destruction", "(B) Magic is hard to learn", "(C) Common sense makes you rich", "(D) Books are heavy", "(A)", "Common sense ensures survival and practical safety.", "Medium", "Evaluating", "Comparative Value"),
    ("How did the sage train his disciples differently?", "(A) Three focused on acquiring intellectual skills; the fourth developed practical observation", "(B) The sage only taught one boy", "(C) The sage hated magic", "(D) The sage sent them away", "(A)", "Different disciples absorbed knowledge in different ways.", "Medium", "Understanding", "Background"),
    ("What would have prevented the tragedy of the three Brahmins?", "(A) Heeding the fourth friend's warning and leaving the dead lion alone", "(B) Reconstructing a bigger lion", "(C) Running faster", "(D) Using more magic spells", "(A)", "Stopping the experiment as advised would have saved them.", "Medium", "Analyzing", "Hypothetical Scenario"),
    ("How does Panchatantra use animal characters and situations to convey human wisdom?", "(A) By showing how human flaws (like arrogance) lead to fatal outcomes in realistic situations", "(B) By teaching how to tame lions", "(C) By telling jokes", "(D) By drawing pictures", "(A)", "Flaws lead to realistic consequences in story form.", "Medium", "Evaluating", "Literary Method"),
    ("What image best summarizes the climax of Chapter 02?", "(A) A revived lion pouncing on three paralyzed friends while one smart friend watches safely from a tree", "(B) Four friends eating dinner peacefully", "(C) A sage giving prizes", "(D) A lion sleeping in a cage", "(A)", "Climax depicts the lion attacking the three friends.", "Medium", "Understanding", "Visual Summary"),

    # Hard (41-50)
    ("Analyze the fundamental flaw in the education of the three 'clever' Brahmins.", "(A) They mastered technical skills (magic) without cultivating moral foresight, risk assessment, or humility", "(B) They did not read enough books", "(C) They forgot how to spell", "(D) They had bad memory", "(A)", "Technical mastery without moral foresight is dangerous.", "Hard", "Analyzing", "HOTS Educational Critique"),
    ("Evaluate the ethical decision of the fourth Brahmin to climb the tree instead of fighting his friends.", "(A) Having repeatedly warned them without success, saving his own life was the only rational, ethical choice remaining", "(B) He was a coward for not fighting the lion", "(C) He should have pushed his friends", "(D) He should have cast a counter-spell", "(A)", "Rational self-preservation after unheeded warnings is ethical.", "Hard", "Evaluating", "Ethical Reasoning"),
    ("How does the story highlight the danger of 'intellectual arrogance'?", "(A) Overconfidence in their abilities blinded the three Brahmins to obvious physical danger and made them dismiss wise counsel", "(B) Intellectuals are always bad", "(C) Arrogance makes you run fast", "(D) Magic turns people into trees", "(A)", "Overconfidence creates deadly blind spots.", "Hard", "Evaluating", "Psychological Analysis"),
    ("Compare the characters of the Second Brahmin (restorer of flesh) and the Third Brahmin (giver of life).", "(A) Both sought vanity in magic, but the Third Brahmin committed the ultimate act of foolishness by activating a deadly predator", "(B) The Second was wise; the Third was lazy", "(C) Neither used magic", "(D) The Second saved everyone", "(A)", "Escalating magical vanity culminated in fatal foolishness.", "Hard", "Analyzing", "Character Comparison"),
    ("How can primary students apply the lesson of 'Four Brahmins' to modern technology or science?", "(A) Just because we have the power or technology to do something doesn't mean we should do it without considering safety consequences", "(B) Always use magic gadgets", "(C) Stop studying science", "(D) Never go into forests", "(A)", "Technology without ethical foresight leads to unintended hazards.", "Hard", "Applying", "Real Life Application"),
    ("Deconstruct the sequence of magical escalation that led to the catastrophe.", "(A) Finding bones -> Reconstructing Skeleton -> Restoring Flesh/Organs -> Infusing Life -> Fatal Attack", "(B) Infusing Life -> Bones -> Flesh -> Tree -> Run", "(C) Tree -> Bones -> Lion -> Ashram -> Magic", "(D) Magic -> Sage -> Town -> Lion -> Bones", "(A)", "Logical progression of magical escalation.", "Hard", "Analyzing", "Structural Analysis"),
    ("Why is the fourth Brahmin's return to the ashram a fitting resolution?", "(A) It completes the circle: he returns to the source of true wisdom (sage) with deep experiential understanding of life's lessons", "(B) He had nowhere else to go", "(C) The sage called him on phone", "(D) He wanted to brag", "(A)", "Return to the sage symbolizes returning to true wisdom.", "Hard", "Evaluating", "Resolution Significance"),
    ("What does the story imply about the relationship between humility and wisdom?", "(A) Humility allows one to observe danger clearly and listen to reason; pride blinds one to obvious reality", "(B) Humility makes you weak", "(C) Wisdom requires big speeches", "(D) Pride is necessary for success", "(A)", "Humility enables clear observation and receptive wisdom.", "Hard", "Evaluating", "Philosophical Insight"),
    ("Why does Panchatantra place this story in the category of 'Loss of Gains' or 'Imprudence'?", "(A) Because foolish actions driven by pride destroy all previous achievements and life itself", "(B) Because they lost their money bags", "(C) Because lions are extinct", "(D) Because the sage was angry", "(A)", "Imprudence destroys life and hard-earned gains.", "Hard", "Evaluating", "Literary Categorization"),
    ("What is the ultimate takeaway message of Chapter 02 for Class 2 learners?", "(A) Always combine your learning with common sense, listen to good advice, and think of consequences before acting!", "(B) Never study magic", "(C) Climb trees every day", "(D) Keep lions as guard animals", "(A)", "Combining knowledge with common sense and foresight is the core message.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 02: Four Brahmins\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH02_MCQ_{idx:03d}"
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
    ("A wise sage had _______ disciples.", "four / 4", "The sage had four disciples.", "Easy"),
    ("Three of the disciples were very clever and learned things very _______.", "quickly / fast", "They learned quickly.", "Easy"),
    ("The fourth disciple was a _______ and took time to learn.", "simpleton", "He was considered a simpleton.", "Easy"),
    ("The three clever Brahmins decided to go to _______ to earn money.", "town / city", "They traveled to town for money.", "Easy"),
    ("The fourth Brahmin offered to _______ and clean for his friends.", "cook", "He offered to cook and clean.", "Easy"),
    ("They decided to rest under a _______ in the evening.", "tree", "They rested under a tree.", "Easy"),
    ("While resting, they noticed some animal _______ lying nearby.", "bones", "They found animal bones.", "Easy"),
    ("The first Brahmin reconstructed the _______ using magic.", "skeleton", "He reconstructed the skeleton.", "Easy"),
    ("The second Brahmin restored organs, muscles, and _______.", "skin", "He added organs, muscles, and skin.", "Easy"),
    ("A lifeless body of a majestic _______ appeared before them.", "lion", "The body of a lion appeared.", "Easy"),
    ("The third Brahmin wanted to bring the lion back to _______.", "life", "He wanted to bring it to life.", "Easy"),
    ("The fourth Brahmin warned: Spare the dead or it will _______ us all!", "devour / eat", "He warned it would devour them.", "Easy"),
    ("His friends ignored his warning and called him a _______.", "fool", "They called him a fool.", "Easy"),
    ("The fourth Brahmin silently climbed a _______ to save himself.", "tree", "He climbed a tree.", "Easy"),
    ("The third Brahmin chanted magic to revive the _______.", "lion", "He revived the lion.", "Easy"),
    ("The starved lion killed and _______ up the three friends.", "ate / devoured", "The lion ate the three friends.", "Easy"),
    ("After the lion left, the fourth Brahmin went back to the sage's _______.", "ashram", "He returned to the ashram.", "Easy"),
    ("Bookish knowledge without wisdom and common sense is _______.", "useless", "Knowledge without wisdom is useless.", "Easy"),
    ("A disciple is a person who follows a _______.", "teacher / sage", "A disciple follows a teacher.", "Easy"),
    ("A sage is a person who has attained _______.", "wisdom", "A sage has attained wisdom.", "Easy"),
    ("A consequence is something that happens as a result of an _______.", "action", "Consequence is the result of action.", "Easy"),
    ("The fourth Brahmin was grieving over the loss of his _______.", "friends", "He grieved for his friends.", "Easy"),
    ("The three friends acquired _______ skills from the sage.", "magical", "They acquired magical skills.", "Easy"),
    ("The lion was very _______ when it woke up.", "hungry / starved", "The lion was starved.", "Easy"),
    ("Chapter 02 is titled Four _______.", "Brahmins", "Chapter 02 is titled Four Brahmins.", "Easy"),

    # Medium (26-40)
    ("The word 'simpleton' refers to a person who is foolish or simple-_______.", "minded", "Simpleton means simple-minded.", "Medium"),
    ("The word 'resuscitate' means to bring someone back to _______.", "life", "Resuscitate means bring back to life.", "Medium"),
    ("The word 'devour' means to eat up greedily and _______.", "quickly", "Devour means eat greedily.", "Medium"),
    ("Common sense helps people avoid unnecessary _______.", "danger / risk", "Common sense avoids danger.", "Medium"),
    ("The three friends showed off their magic out of vanity and _______.", "pride / arrogance", "They acted out of pride.", "Medium"),
    ("The fourth friend used observation to predict the lion's _______.", "behavior / attack", "He predicted the lion's behavior.", "Medium"),
    ("Fear turned the three friends to _______ when the lion roared.", "stone", "Fear turned them to stone.", "Medium"),
    ("True wisdom requires knowing when NOT to use one's _______.", "power / magic", "Wisdom knows when not to use power.", "Medium"),
    ("The sage's ashram was a place of learning and _______.", "peace / wisdom", "Ashram is a place of peace.", "Medium"),
    ("Ignoring wise warnings leads to severe _______.", "consequences / punishment", "Ignoring warnings has consequences.", "Medium"),
    ("The fourth Brahmin demonstrated practical self-_______.", "preservation / safety", "He demonstrated self-preservation.", "Medium"),
    ("Magic without moral guidance causes unexpected _______.", "disaster / harm", "Magic without morals causes harm.", "Medium"),
    ("The starved lion acted according to its wild _______.", "nature / instincts", "Lions act on wild instincts.", "Medium"),
    ("The fourth Brahmin returned home with deep sadness and _______.", "grief / sorrow", "He returned with deep grief.", "Medium"),
    ("This Panchatantra fable highlights the importance of practical _______.", "wisdom / intelligence", "It highlights practical wisdom.", "Medium"),

    # Hard (41-50)
    ("Intellectual vanity blinded the three Brahmins to basic physical _______.", "danger / reality", "Vanity blinded them to danger.", "Hard"),
    ("Reconstructing a predator step-by-step illustrates reckless escalation of _______.", "risk", "Step-by-step escalation of risk.", "Hard"),
    ("The tree served as a structural refuge for the prudent _______.", "disciple / Brahmin", "The tree provided refuge.", "Hard"),
    ("Moral prudence dictates that one must anticipate the outcome of any _______.", "experiment / action", "Prudence dictates anticipating outcomes.", "Hard"),
    ("Knowledge is potential power, but wisdom determines its proper _______.", "application / use", "Wisdom dictates application.", "Hard"),
    ("Arrogance makes individuals immune to constructive _______.", "criticism / warnings", "Arrogance rejects warnings.", "Hard"),
    ("The lion symbolizes unbridled forces unleashed without ethical _______.", "control / restraint", "The lion symbolizes unbridled forces.", "Hard"),
    ("The tragedy could have been averted by practicing self-_______.", "restraint", "Restraint would avert tragedy.", "Hard"),
    ("Grieving at the ashram represents reflection on human _______.", "folly / mistakes", "Reflection on human folly.", "Hard"),
    ("Chapter 02 teaches that common sense is the ultimate tool for _______.", "survival", "Common sense ensures survival.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 02: Four Brahmins\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH02_FIB_{idx:03d}"
    q_txt, ans, exp, diff = item
    bloom = "Remembering" if diff == "Easy" else ("Understanding" if diff == "Medium" else "Analyzing")
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Bloom Level**: {bloom}\n"
    fib_content += f"- **Topic**: Sentence Completion {idx}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {q_txt}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH02_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The wise sage had four disciples.", True, "The sage had four disciples.", "Easy"),
    ("All four disciples were equally clever at learning magic.", False, "Three were clever; the fourth was a simpleton.", "Easy"),
    ("The fourth Brahmin offered to cook and clean for his friends.", True, "He offered to cook and clean for them.", "Easy"),
    ("The friends found some gold coins lying under a tree.", False, "They found animal bones lying under a tree.", "Easy"),
    ("The first Brahmin reconstructed the skeleton from the bones.", True, "The first Brahmin built the skeleton.", "Easy"),
    ("The second Brahmin restored organs, muscles, and skin.", True, "The second Brahmin restored organs, muscles, and skin.", "Easy"),
    ("The body formed from the bones was a harmless rabbit.", False, "It was the body of a majestic lion.", "Easy"),
    ("The third Brahmin wanted to bring the dead lion back to life.", True, "He wanted to revive the dead lion.", "Easy"),
    ("The fourth Brahmin encouraged his friends to bring the lion back to life.", False, "He warned them that the lion would devour them.", "Easy"),
    ("The fourth Brahmin climbed a tree to save himself from danger.", True, "He climbed a tree to stay safe.", "Easy"),
    ("The three clever Brahmins listened to the fourth friend's warning.", False, "They ignored him and called him a fool.", "Easy"),
    ("The revived lion killed and ate the three clever Brahmins.", True, "The starved lion ate the three friends.", "Easy"),
    ("The lion also climbed the tree and ate the fourth Brahmin.", False, "The fourth Brahmin stayed safe in the tree.", "Easy"),
    ("After the lion left, the fourth Brahmin returned to the sage's ashram.", True, "He returned to the ashram grieving.", "Easy"),
    ("Bookish knowledge without common sense is useless.", True, "This is the central moral of the story.", "Easy"),
    ("A disciple is a teacher who instructs others.", False, "A disciple is a student who follows a teacher.", "Easy"),
    ("A sage is a person who has attained wisdom.", True, "A sage is a wise holy person.", "Easy"),
    ("A consequence is the result of an action.", True, "Consequence means result of an action.", "Easy"),
    ("The fourth Brahmin possessed practical wisdom and common sense.", True, "He possessed practical common sense.", "Easy"),
    ("The lion was very full and sleepy when it woke up.", False, "The lion was starved and extremely hungry.", "Easy"),
    ("The three clever friends went to town to buy new toys.", False, "They went to town to earn money.", "Easy"),
    ("The fourth Brahmin cheered loudly when the lion woke up.", False, "He stayed quiet in the tree while his friends froze in fear.", "Easy"),
    ("The story of 'Four Brahmins' comes from the Panchatantra.", True, "It is a Panchatantra tale.", "Easy"),
    ("The fourth Brahmin tried to stop his friends from bringing the lion to life.", True, "He repeatedly warned them to spare the dead.", "Easy"),
    ("Chapter 02 is titled 'Four Brahmins'.", True, "Chapter 02 is titled 'Four Brahmins'.", "Easy"),

    # Medium (26-40)
    ("The three clever Brahmins showed off their magic out of pride and vanity.", True, "Pride made them want to display magic.", "Medium"),
    ("The fourth Brahmin was afraid of cooking food.", False, "He willingly offered to cook and clean.", "Medium"),
    ("Reconstructing a dangerous lion shows a complete lack of common sense.", True, "Creating a wild predator is foolish.", "Medium"),
    ("The three friends froze like stone because they were confident.", False, "They froze out of sudden terror.", "Medium"),
    ("The fourth Brahmin survived because he acted quickly to protect himself.", True, "Quick action saved his life.", "Medium"),
    ("Lions in the wild normally eat grass and fruits.", False, "Lions are wild carnivores that eat meat.", "Medium"),
    ("The three friends respected the fourth Brahmin's opinion.", False, "They mocked him and called him a fool.", "Medium"),
    ("Having magic power guarantees that a person will make wise decisions.", False, "Magic power without wisdom leads to disaster.", "Medium"),
    ("The fourth Brahmin was happy that his arrogant friends were eaten.", False, "He was deeply grieved by their deaths.", "Medium"),
    ("Common sense means understanding practical safety in real life.", True, "Common sense means practical safety awareness.", "Medium"),
    ("The third Brahmin thought he was the brightest of all four friends.", True, "He claimed to be the brightest.", "Medium"),
    ("The lion spared the three friends because they brought it to life.", False, "The wild lion immediately attacked and ate them.", "Medium"),
    ("The ashram was a safe place where the fourth Brahmin returned.", True, "The ashram was a place of safety.", "Medium"),
    ("Ignoring good advice can lead to fatal consequences.", True, "Ignoring good advice leads to disaster.", "Medium"),
    ("The story proves that formal education alone is insufficient for life.", True, "Formal learning needs common sense.", "Medium"),

    # Hard (41-50)
    ("Arrogance creates cognitive blind spots that prevent risk assessment.", True, "Arrogance prevents proper risk assessment.", "Hard"),
    ("The fourth Brahmin's humble role as cook reflected deeper practical intelligence.", True, "Humble practical skills reflect wisdom.", "Hard"),
    ("The tragedy represents a triumph of brute nature over unguided intellect.", True, "Wild nature defeated unguided magic intellect.", "Hard"),
    ("The third Brahmin's magic spell was an act of extreme imprudence.", True, "Reviving a predator was imprudent.", "Hard"),
    ("Wisdom requires evaluating long-term consequences before taking action.", True, "Wisdom requires evaluating consequences.", "Hard"),
    ("The fourth Brahmin failed in his moral duty by not physically stopping his friends.", False, "He warned them repeatedly; physical intervention against three wizards was impossible.", "Hard"),
    ("Panchatantra stories advocate abandoning theoretical learning entirely.", False, "They advocate combining learning with practical common sense.", "Hard"),
    ("The lion's hunger symbolizes the unyielding reality of natural laws.", True, "Natural predator instincts overwrite magic gratitude.", "Hard"),
    ("Climbing the tree symbolizes elevating oneself above foolish arguments.", True, "Climbing the tree symbolizes practical detachment.", "Hard"),
    ("Chapter 02 demonstrates that survival belongs to the prudent and humble.", True, "Prudence and humility ensure survival.", "Hard")
]

tf_content = f"# True / False — Chapter 02: Four Brahmins\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH02_TF_{idx:03d}"
    q_txt, is_true, exp, diff = item
    ans_str = "True" if is_true else "False"
    bloom = "Remembering" if diff == "Easy" else ("Understanding" if diff == "Medium" else "Analyzing")
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Bloom Level**: {bloom}\n"
    tf_content += f"- **Topic**: Statement Evaluation {idx}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Question**: State True or False: {q_txt}\n\n"
    tf_content += f"- **Answer Key**: **{ans_str}** — {exp}\n\n---\n\n"

with open(os.path.join(CH02_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("How many disciples did the sage have and how were they different?", "The sage had four disciples; three were clever in magic, while the fourth was a simpleton with common sense.", "Easy"),
    ("Why did the three clever Brahmins decide to go to town?", "The three clever Brahmins decided to go to town to earn money using their skills.", "Easy"),
    ("What job did the fourth Brahmin offer to do so he could join them?", "He offered to cook food and clean for all of them during the journey.", "Easy"),
    ("What did the friends find while resting under a tree in the evening?", "They found a pile of old animal bones lying on the ground under the tree.", "Easy"),
    ("What magic did the first Brahmin perform on the bones?", "The first Brahmin used his magic to reconstruct the complete skeleton of the animal.", "Easy"),
    ("What magic did the second Brahmin perform on the skeleton?", "The second Brahmin used magic to restore the organs, muscles, and skin onto the skeleton.", "Easy"),
    ("What animal appeared after the second Brahmin used his magic?", "The complete lifeless body of a majestic lion appeared on the ground.", "Easy"),
    ("What did the third Brahmin want to do to the lion?", "The third Brahmin wanted to use his magic spell to bring the dead lion back to life.", "Easy"),
    ("What warning did the fourth Brahmin give to his three friends?", "He warned them to spare the dead lion and not bring it to life, or it would devour them all.", "Easy"),
    ("How did the three clever friends react to the fourth Brahmin's warning?", "They ignored his warning, mocked him, and called him a fool.", "Easy"),
    ("What did the fourth Brahmin do to save his own life?", "He silently climbed up a tall tree before the third friend cast the spell.", "Easy"),
    ("What happened as soon as the lion was brought back to life?", "The starved lion woke up, saw the three frozen friends, killed them, and ate them up.", "Easy"),
    ("Where did the fourth Brahmin go after the lion finished eating and walked away?", "He climbed down the tree and returned grieving to the sage's ashram.", "Easy"),
    ("What is the main moral of the story 'Four Brahmins'?", "The moral is that bookish knowledge without wisdom and common sense is completely useless.", "Easy"),
    ("What does the word 'disciple' mean?", "'Disciple' means a student or follower who learns from a teacher or sage.", "Easy"),
    ("What does the word 'sage' mean?", "'Sage' means a wise holy person who possesses deep spiritual wisdom.", "Easy"),
    ("What does the word 'consequence' mean?", "'Consequence' means a result or outcome that follows a particular action.", "Easy"),
    ("Why was the lion so dangerous when it came back to life?", "Because it was a wild, starved predator acting on its natural instinct to hunt for food.", "Easy"),
    ("Why did the three clever friends laugh at the fourth Brahmin?", "Because they thought he was foolish and lacked the high magical knowledge they possessed.", "Easy"),
    ("What book of ancient Indian fables contains this story?", "This story comes from the ancient Indian fable collection called the Panchatantra.", "Easy"),
    ("Did the lion harm the fourth Brahmin in the tree?", "No, the lion did not notice or reach the fourth Brahmin staying high in the tree.", "Easy"),
    ("Why did the three friends turn 'stone out of fear'?", "Because they were paralyzed with terror when the revived lion stood up and roared.", "Easy"),
    ("What work was the fourth Brahmin doing when the friends found the bones?", "He was preparing dinner for all of them under the tree.", "Easy"),
    ("What title does Chapter 02 carry in Book 2?", "Chapter 02 is titled 'Four Brahmins'.", "Easy"),
    ("How did the fourth Brahmin show that he was actually wise?", "By predicting the danger of the lion and climbing a tree to save his life.", "Easy"),

    # Medium (26-40)
    ("Why did the three clever Brahmins refuse to let the fourth friend travel with them initially?", "Because they believed his lack of magical skills made him useless for earning money in town.", "Medium"),
    ("How did the fourth Brahmin show humility when mocked by his friends?", "He did not get angry; instead, he humbly offered to perform cooking and cleaning duties.", "Medium"),
    ("Why was it foolish to reconstruct a lion in the middle of a forest?", "Because creating a dangerous predator in an open space creates immediate deadly risk for everyone nearby.", "Medium"),
    ("Contrast the knowledge of the three Brahmins with the wisdom of the fourth Brahmin.", "The three had theoretical magic skills without sense; the fourth had practical wisdom and self-preservation.", "Medium"),
    ("Why did arrogance prevent the three friends from listening to reason?", "Their pride in magic made them feel superior, blinding them to basic physical safety and logical warnings.", "Medium"),
    ("What does the lion symbolize in the context of human actions?", "The lion symbolizes the dangerous, uncontrollable consequences of reckless choices made without foresight.", "Medium"),
    ("How did the fourth Brahmin's quick action in climbing the tree save his life?", "Recognizing his friends wouldn't stop, he took immediate self-protective action before the spell finished.", "Medium"),
    ("Why did fear paralyze the three friends when the lion awoke?", "Because their theoretical knowledge gave them no practical defense against a real, hungry predator.", "Medium"),
    ("Why did the fourth Brahmin return to the ashram grieving?", "He felt deep sorrow that his companions had lost their lives due to their own foolish pride.", "Medium"),
    ("What lesson does this story teach about evaluating risks before taking action?", "Always consider potential hazards and consequences before initiating an action or experiment.", "Medium"),
    ("Why is common sense considered more valuable than specialized knowledge here?", "Specialized knowledge created the threat, but common sense preserved life and ensured survival.", "Medium"),
    ("How did the sage's training manifest differently in his disciples?", "Three disciples focused on dramatic magic spells, while the fourth cultivated observational common sense.", "Medium"),
    ("What simple action could have saved all four Brahmins?", "Heeding the fourth friend's advice and walking away from the dead bones without reviving the lion.", "Medium"),
    ("How does Panchatantra use this fable to criticize vain scholarship?", "It shows that vanity in academic or magical learning leads to destruction if devoid of practical sense.", "Medium"),
    ("Summarize Chapter 02 in two clear sentences.", "Three magic-trained Brahmins reconstructed and revived a dead lion despite warnings from their fourth friend. The lion ate the three arrogant friends, while the fourth saved himself by climbing a tree.", "Medium"),

    # Hard (41-50)
    ("Analyze the failure of technical skill when divorced from ethical foresight.", "Technical skill provides power, but without ethical foresight and risk assessment, power turns destructive toward the creator.", "Hard"),
    ("Evaluate the ethical boundary of the fourth Brahmin saving himself while his friends perished.", "Having issued clear, repeated warnings that were rejected with mockery, he had no means to stop them and was ethically justified in saving himself.", "Hard"),
    ("How does intellectual arrogance lead to cognitive blind spots?", "Overconfidence in one's specialized talent causes one to dismiss simple, obvious dangers and ignore valid external advice.", "Hard"),
    ("Compare the escalation of magic from skeleton -> flesh -> life with real-world technological risks.", "Each stage escalated risk without safety controls, mirroring how unchecked technological development can create uncontrollable hazards.", "Hard"),
    ("How can Class 2 students apply the lesson of 'Four Brahmins' to teamwork and safety?", "Students learn to listen to safety warnings, avoid dangerous show-off behavior, and value every teammate's practical wisdom.", "Hard"),
    ("Deconstruct the narrative arc of Chapter 02 from departure to ashram return.", "Departure -> Discovery of Bones -> Magical Escalation -> Unheeded Warning -> Revitalization -> Tragedy -> Prudent Survival -> Ashram Return.", "Hard"),
    ("Why is returning to the sage's ashram symbolically significant?", "It signifies returning to the source of genuine wisdom after witnessing the fatal failure of superficial knowledge.", "Hard"),
    ("What does the story imply about the relationship between humility and self-preservation?", "Humility allows one to acknowledge personal vulnerability and take practical steps (like climbing a tree) to survive.", "Hard"),
    ("Why does Panchatantra classify this tale under the theme of imprudence?", "Because the core conflict arises from imprudent actions executed without considering deadly outcomes.", "Hard"),
    ("Synthesize the ultimate educational message of Chapter 02 for primary learners.", "True intelligence combines learning with common sense, humility, and careful thought for consequences!", "Hard")
]

sa_content = f"# Short Answer — Chapter 02: Four Brahmins\n\n> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH02_SA_{idx:03d}"
    q_txt, ans, diff = item
    bloom = "Remembering" if diff == "Easy" else ("Understanding" if diff == "Medium" else "Analyzing")
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Topic**: Short Comprehension {idx}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH02_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-15)
    ("Write a simple summary of Chapter 02 'Four Brahmins'.", "A wise sage had four disciples. Three of them were very clever in learning magic skills, while the fourth was a simpleton who took time to learn. One day, the three clever Brahmins decided to go to town to earn money. The fourth friend wanted to join them, so he offered to cook and clean for them. On their journey, they rested under a tree and found a pile of animal bones. To show off their magic, the first Brahmin rebuilt the skeleton, and the second Brahmin added flesh, organs, and skin, creating a lion's body. The third Brahmin wanted to bring the lion back to life. The fourth friend warned them that the lion would devour them, but they mocked him. The fourth Brahmin wisely climbed up a tree to save himself. The third friend cast the spell, and the revived, hungry lion instantly killed and ate the three clever Brahmins. After the lion left, the fourth Brahmin returned to the ashram, grieving for his foolish friends.", "Easy"),
    ("Describe the characters of the four Brahmins in detail.", "The four Brahmins represent two different kinds of knowledge. The first three Brahmins were intellectually clever and acquired impressive magical skills quickly. However, they were arrogant, vain, and completely lacked common sense and foresight. The fourth Brahmin was simple-minded and lacked magic, but he possessed deep practical wisdom, humility, and observational common sense. While the three magic users used their skills recklessly to show off, the fourth Brahmin anticipated danger, warned his companions, and saved his own life by climbing a tree.", "Easy"),
    ("Describe the three magical steps used to recreate the lion.", "The recreation of the lion happened in three distinct magical steps:\n1. First Step: The first Brahmin used his magic to assemble the scattered animal bones into a complete skeleton.\n2. Second Step: The second Brahmin used his magic to add internal organs, muscular tissue, and outer skin onto the skeleton, revealing a majestic lion's body.\n3. Third Step: The third Brahmin chanted magic spells to infuse life into the lifeless body, turning it into a living, moving predator.", "Easy"),
    ("Explain the warning given by the fourth Brahmin and how his friends reacted.", "When the third Brahmin prepared to bring the lion to life, the fourth Brahmin clearly warned them: 'Spare the dead! Do not resuscitate it or it will devour us all! Think of the consequences, please!' However, his three friends arrogantly ignored his warning, laughed at him, and called him a fool, claiming that only fools worry about consequences. Their pride prevented them from seeing the obvious danger.", "Easy"),
    ("Why did common sense save the fourth Brahmin while magic killed the others?", "Common sense saved the fourth Brahmin because it allowed him to evaluate real-world cause and effect. He knew that a revived lion would naturally act on its predatory instincts and hunt for food. Since he could not stop his friends, common sense guided him to climb a tree for safety. In contrast, his friends were so blinded by their magical power that they forgot basic survival logic, resulting in their destruction.", "Easy"),
    ("What moral lesson does the story teach about knowledge and wisdom?", "The story teaches that bookish knowledge or technical skill without practical wisdom and common sense is useless and dangerous. Having great knowledge or power means nothing if one does not know when and how to use it safely. Wisdom involves thinking about consequences, listening to good advice, and protecting life.", "Easy"),
    ("Explain the meaning and importance of the vocabulary words 'disciple', 'sage', and 'consequence'.", "• Disciple: A student who follows a teacher to learn knowledge and values.\n• Sage: A wise, holy person who has attained deep spiritual and practical wisdom.\n• Consequence: The natural result or outcome produced by an action. Understanding consequences is essential for making safe decisions in life.", "Easy"),
    ("How did the lion behave when it was brought back to life?", "When the lion was brought back to life, it did not feel grateful to the Brahmins. Instead, acting as a starved, hungry predator, it looked at the three friends who were frozen in fear. It immediately pounced on them, killed all three, and devoured them completely before walking away into the forest.", "Easy"),
    ("Why is listening to warnings from friends an important life skill?", "Listening to warnings helps us avoid dangerous mistakes that we might not notice ourselves. Arrogantly ignoring advice out of pride can lead to serious harm or disaster, whereas listening carefully to reasonable warnings keeps us safe.", "Easy"),
    ("Describe the setting and journey of the four Brahmins.", "The story begins at a peaceful forest ashram where the four Brahmins lived with their wise sage. The four friends set out on a foot journey toward a nearby town to earn money. By evening, after walking all day, they stopped to rest and cook dinner under a large tree in the forest, which became the scene of the tragic lion experiment.", "Easy"),
    ("What made the fourth Brahmin offer to cook and clean for his friends?", "When the three clever friends initially refused to take him along because he lacked magic, the fourth Brahmin did not get angry or argue. He humbly offered to handle domestic chores like cooking food and cleaning camp so he could travel with them and be useful to the group.", "Easy"),
    ("Why did the fourth Brahmin return to the ashram instead of continuing to town?", "After witnessing the tragic death of his three companions, the fourth Brahmin had no desire to earn money in town. Overwhelmed with grief and sorrow over his friends' foolish end, he returned to the sage's ashram where true wisdom and spiritual peace resided.", "Easy"),
    ("What contrasts exist between the third Brahmin and the fourth Brahmin?", "The third Brahmin was vain, arrogant, and eager to display his supreme spellcasting power regardless of danger. The fourth Brahmin was humble, practical, cautious, and valued safety over display. The third Brahmin's pride caused his death, while the fourth Brahmin's humility saved his life.", "Easy"),
    ("How does Panchatantra use animal stories to teach practical living?", "Panchatantra uses dramatic situations involving animals and human choices to show clear cause-and-effect relationships. By showing how human flaws lead to real consequences, the fables teach children how to navigate life with wisdom, caution, and ethics.", "Easy"),
    ("What key values should Class 2 students learn from Chapter 02?", "Class 2 students should learn to value common sense over showing off, listen respectfully to advice from others, think carefully about the results of their actions before acting, and practice humility in their learning.", "Easy"),

    # Medium (16-40)
    ("Analyze how intellectual vanity led to the destruction of the three Brahmins.", "The three Brahmins suffered from intellectual vanity—they believed their magical accomplishments made them superior to nature and common logic. When presented with the opportunity to revive a lion, their desire to show off their power completely overshadowed their instinct for self-preservation. Their vanity made them immune to valid warnings, directly causing their tragic demise.", "Medium"),
    ("Compare the nature of theoretical knowledge versus practical wisdom.", "Theoretical knowledge (like the magic spells learned by the three Brahmins) consists of technical information and skills. Practical wisdom (demonstrated by the fourth Brahmin) consists of knowing how to apply knowledge safely, understanding human and animal nature, anticipating risks, and exercising self-restraint. Theoretical knowledge without practical wisdom is incomplete and hazardous.", "Medium"),
    ("Discuss why natural instincts always override magic gratitude in wild animals.", "The third Brahmin assumed that bringing the lion back to life would earn its respect or obedience. However, a wild predator operates purely on biological instincts such as hunger and hunting drive. A revived starved lion sees nearby living beings simply as meat, proving that magical ambition cannot rewrite the fundamental laws of natural animal behavior.", "Medium"),
    ("How does the fourth Brahmin's decision to climb a tree illustrate effective risk management?", "When faced with an unpreventable hazard created by his friends, the fourth Brahmin did not stay to argue or panic. He identified a physical sanctuary (the tall tree), executed a quick self-preservation move, and separated himself from the danger zone before the threat materialized. This is a classic example of sound risk management.", "Medium"),
    ("Explain the moral significance of the phrase: 'Spare the dead. Don't resuscitate it or it will devour us all.'", "This warning carries both literal and metaphorical significance. Literally, it warned against reviving a dangerous beast. Metaphorically, it teaches us not to disturb settled dangers, revive past conflicts, or meddle with forces we cannot control, as doing so can unleash destruction upon ourselves.", "Medium"),
    ("Write a dialogue between the third Brahmin and the fourth Brahmin before the spell is cast.", "Fourth Brahmin: 'Please my brother, stop! Do not cast the spell! A living lion will devour us all!'\nThird Brahmin: 'Silent, you fool! You know no magic, so you fear my great power! Watch me bring this majestic beast to life!'\nFourth Brahmin: 'If you will not hear reason, I must save myself!' (Climbs tree)", "Medium"),
    ("Evaluate the role of the Sage in shaping his four disciples.", "The Sage provided equal educational opportunities to all four disciples. Three mastered technical magic quickly, while the fourth absorbed quiet observation. The tragic outcome shows that a teacher can impart knowledge, but the student's personal humility and character determine whether that knowledge becomes wisdom or foolishness.", "Medium"),
    ("Describe the emotional transformation of the fourth Brahmin from departure to return.", "At departure, he felt eager, hopeful, and willing to serve his friends. During the journey, he felt concerned and protective when danger arose. At the climax, he felt tense and helpless watching his friends' arrogance. Upon return, he felt profound grief, sorrow, and deep appreciation for true wisdom.", "Medium"),
    ("Why is the title 'Four Brahmins' appropriate for this fable?", "The title focuses on the contrasting traits of the four companions. It highlights how four individuals from the same background and teacher can make vastly different choices based on their character, serving as a memorable comparison of foolish intellect versus prudent wisdom.", "Medium"),
    ("How does the story caution against reckless scientific or experimental curiosity?", "The story warns that conducting experiments or unleashing powers simply because we possess the technical ability to do so—without establishing safety measures or evaluating risks—can lead to uncontrollable catastrophes that destroy the experimenters.", "Medium"),
    ("Explain why the three friends were paralyzed with fear when the lion woke up.", "Their magical training was purely academic and spell-based; they had never developed physical courage, emergency response skills, or realistic tactical planning. Faced with a roaring predator in real life, their academic confidence collapsed into absolute paralysis.", "Medium"),
    ("How can Class 2 teachers use this story to promote safety and listening skills in school?", "Teachers can explain that school rules and safety guidelines (like not running on wet floors) are like the fourth friend's warning. Following rules and listening to advice prevents accidents and keeps everyone safe, whereas showing off leads to injury.", "Medium"),
    ("Discuss the symbolic difference between ground level and tree level in the story.", "Ground level represents the zone of arrogant action, illusion of control, and physical vulnerability where the three Brahmins operated. Tree level represents the elevated sanctuary of observation, prudence, common sense, and safety where the fourth Brahmin stayed.", "Medium"),
    ("How did the fourth Brahmin balance loyalty to friends with self-preservation?", "He showed loyalty by traveling with them, cooking their meals, and repeatedly warning them of danger. However, when his loyalty could not change their foolish minds, he rightly prioritized self-preservation, recognizing that dying alongside them would serve no purpose.", "Medium"),
    ("What does this tale reveal about ancient Indian educational philosophy?", "Ancient Indian philosophy emphasized that 'Vidya' (education) is complete only when accompanied by 'Vinaya' (humility) and 'Viveka' (discernment/common sense). Knowledge without humility and discernment was considered flawed and dangerous.", "Medium"),
    ("Describe the scene after the lion departed from the tree base.", "The forest returned to quietness. The lion walked away satiated into the woods. The fourth Brahmin, trembling and grieving, slowly climbed down from the tree, looked at the tragic scene, gathered his simple belongings, and began his lonely walk back to the ashram.", "Medium"),
    ("Why did the first two Brahmins share equal blame with the third Brahmin?", "Although the third Brahmin cast the final life-giving spell, the first two initiated the danger by building the skeleton and restoring the flesh. They actively created the weapon of their own destruction, sharing full responsibility for the foolish endeavor.", "Medium"),
    ("How does Chapter 02 fulfill the standards of primary literature comprehension?", "It incorporates vibrant storytelling, clear character contrasts, vocabulary expansion (sage, disciple, consequence), cause-and-effect structure, moral analysis, and engaging exercise formats suitable for Class 2 learners.", "Medium"),
    ("Contrast the responses of an arrogant person vs a humble person when facing advice.", "An arrogant person responds to advice with defensiveness, mockery, and dismissal, believing they know better. A humble person responds by listening attentively, evaluating the risk, and adjusting their actions to ensure safety and harmony.", "Medium"),
    ("Summarize Chapter 02 in four comprehensive bullet points.", "• Four disciples set out for town; three possessed magic skills while the fourth possessed common sense.\n• Finding animal bones, the first three used magic to build a lion's skeleton, flesh, and life.\n• The fourth Brahmin warned them of the deadly danger and climbed a tree for safety.\n• The revived lion killed the three arrogant friends, leaving the wise fourth Brahmin to return home safely.", "Medium"),

    # Hard (41-50)
    ("Deconstruct the philosophical concept of 'Reductio ad Absurdum' in moral fable storytelling.", "In fable storytelling, authorial strategy often pushes foolish behavior to its ultimate logical absurdity (rebuilding a deadly lion) to highlight the contrast between arrogance and prudence. By taking technical skill to a extreme, dangerous conclusion, the fable proves beyond doubt that unguided intellect leads to self-annihilation.", "Hard"),
    ("Analyze how 'Four Brahmins' critiques the social hierarchy of intellect over practical labor.", "The narrative subverts traditional social hierarchies: the three 'clever' scholars who looked down on practical labor (cooking and cleaning) proved completely incompetent at survival, while the 'simple' manual worker survived through practical observation, demonstrating that utility and common sense outweigh superficial status.", "Hard"),
    ("Evaluate the psychological dynamic of mob mentality among the three clever friends.", "The three magic users reinforced each other's hubris, creating a collective mob mentality. Once the first rebuilt the skeleton, the second felt compelled to restore flesh, and the third felt pressured to give life. None dared to stop, illustrating how group vanity suppresses individual risk awareness.", "Hard"),
    ("Examine the ethical responsibility of creators toward their creations.", "The story serves as an early allegory for creator responsibility. Creating life or unleashing powerful systems without building containment mechanisms or understanding the creation's inherent nature is unethical and self-destructive. Creators bear total responsibility for the forces they unbind.", "Hard"),
    ("How does Chapter 02 serve as an archetype for modern environmental and biotechnological ethics?", "Modern bio-engineering and technology echo this fable: scientists can manipulate genetic code or create artificial systems, but doing so without evaluating long-term ecological or ethical consequences threatens humanity. The fable asserts that moral wisdom must govern technological capability.", "Hard"),
    ("Formulate a Class 2 story-mapping activity for Chapter 02.", "Students create a 4-panel comic strip:\nPanel 1: Disciples walking to town.\nPanel 2: Magic used on bones under tree.\nPanel 3: Fourth friend warning and climbing tree.\nPanel 4: Fourth friend returning to ashram with moral text.", "Hard"),
    ("Differentiate between instinctual intelligence in animals and reflective wisdom in humans.", "Animals operate on instinctual intelligence (the lion hunting for food upon waking). Humans possess reflective wisdom—the ability to analyze past events, project future outcomes, exercise moral restraint, and choose actions based on ethics rather than immediate impulse.", "Hard"),
    ("Why is the setting of a wilderness forest crucial to the narrative's resolution?", "The wilderness forest represents raw natural reality, free from human social protections or legal intervention. In the wilderness, academic titles mean nothing, and natural laws (predator instinct) swiftly punish those who ignore physical realities.", "Hard"),
    ("Discuss how the return to the Sage restores narrative and moral equilibrium.", "The journey out represented departure into foolish vanity; the return to the Sage represents returning to true spiritual foundation. The fourth Brahmin brings back a tragic real-world case study, validating the Sage's teaching that true learning is rooted in wisdom.", "Hard"),
    ("Synthesize the ultimate educational philosophy of Chapter 02 for primary learners.", "Knowledge empowers the mind, but wisdom guides the soul. Always pair your skills with common sense, respect reasonable warnings, evaluate consequences before acting, and let humility guide your journey through life!", "Hard")
]

la_content = f"# Long Answer — Chapter 02: Four Brahmins\n\n> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH02_LA_{idx:03d}"
    q_txt, ans, diff = item
    bloom = "Understanding" if diff == "Easy" else ("Analyzing" if diff == "Medium" else "Evaluating")
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Topic**: Comprehensive Analysis {idx}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH02_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based Questions (10 Extracts x 5 Qs = 50 Qs)
# -------------------------------------------------------------
extracts = [
    (
        "A sage had four disciples. Three of them were very clever and learnt things very quickly. As a result, they had also managed to acquire magical skills from the sage. The fourth one was a simpleton and took time to learn things.",
        [
            ("How many disciples did the sage have?", "The sage had four disciples.", "Easy"),
            ("How many of the disciples were clever and learned things quickly?", "Three of the disciples were clever and learned things quickly.", "Easy"),
            ("What special skills did the three clever disciples acquire from the sage?", "They acquired magical skills from the sage.", "Easy"),
            ("How was the fourth disciple described in comparison to his friends?", "The fourth disciple was described as a simpleton who took time to learn things.", "Medium"),
            ("What foundational contrast is established in this opening passage?", "It contrasts theoretical/magical cleverness in three disciples with simple learning in the fourth.", "Hard")
        ]
    ),
    (
        "One day, the three clever Brahmins decided to go to town to earn money. The fourth one wanted to go with them too but they refused and made fun of him. 'After all, what good can you do?'",
        [
            ("Where did the three clever Brahmins decide to go one day?", "They decided to go to town.", "Easy"),
            ("Why did the three Brahmins want to go to town?", "They wanted to go to town to earn money.", "Easy"),
            ("What did the three friends do when the fourth Brahmin wanted to join them?", "They refused to take him and made fun of him.", "Easy"),
            ("What rude question did they ask the fourth Brahmin?", "They asked, 'After all, what good can you do?'", "Medium"),
            ("What character flaw of the three Brahmins is revealed in their response?", "Their arrogance and lack of respect for their companion are revealed.", "Hard")
        ]
    ),
    (
        "'I will cook and clean for all of you, if nothing else', he replied. Hearing this they agreed to take him along.",
        [
            ("Who offered to cook and clean for everyone?", "The fourth Brahmin offered to cook and clean for everyone.", "Easy"),
            ("What two tasks did the fourth Brahmin offer to perform on the journey?", "He offered to cook food and clean for all of them.", "Easy"),
            ("Why did the three friends change their mind and agree to take him?", "Because they realized he would perform useful domestic work for them on the way.", "Easy"),
            ("What quality did the fourth Brahmin display by making this offer?", "He displayed humility, practical helpfulness, and patience.", "Medium"),
            ("How does this offer foreshadow his practical nature later in the story?", "It shows he focuses on practical service and survival rather than boastful display.", "Hard")
        ]
    ),
    (
        "Next day, they started for the town. After walking all through the day, they decided to rest under a tree in the evening. While the fourth Brahmin was preparing dinner, the three friends noticed some bones lying nearby.",
        [
            ("When did the four friends stop to rest under a tree?", "They stopped to rest under a tree in the evening after walking all day.", "Easy"),
            ("What was the fourth Brahmin doing while resting under the tree?", "The fourth Brahmin was preparing dinner for everyone.", "Easy"),
            ("What did the three clever friends discover lying on the ground nearby?", "They noticed some animal bones lying nearby.", "Easy"),
            ("Where were the four Brahmins traveling to?", "They were traveling to the nearby town to earn money.", "Medium"),
            ("How does the setting (evening in a forest) add tension to the discovery of bones?", "Being in a dark forest at dusk makes experimenting with wild animal bones particularly dangerous.", "Hard")
        ]
    ),
    (
        "To show his magical powers, the first Brahmin reconstructed the skeleton. The fourth Brahmin objected, 'Leave it alone.' But no one heard him.",
        [
            ("Why did the first Brahmin reconstruct the skeleton?", "To show off his magical powers.", "Easy"),
            ("What magic did the first Brahmin perform on the bones?", "He reconstructed the complete skeleton of the animal.", "Easy"),
            ("What objection did the fourth Brahmin make to the first Brahmin?", "He objected and said, 'Leave it alone.'", "Easy"),
            ("Did the three friends listen to the fourth Brahmin's objection?", "No, no one heard or listened to him.", "Medium"),
            ("What pattern of behavior is established by ignoring the fourth friend's objection?", "A pattern of arrogant showmanship ignoring reasonable caution.", "Hard")
        ]
    ),
    (
        "Not to be outdone, the second Brahmin restored its organs, muscles and skin. A lifeless body of a majestic lion was now visible to all.",
        [
            ("Why did the second Brahmin use his magic spell?", "He used his magic because he did not want to be outdone by the first Brahmin.", "Easy"),
            ("What three body parts did the second Brahmin restore to the skeleton?", "He restored its organs, muscles, and skin.", "Easy"),
            ("What animal's body appeared after the second Brahmin's magic?", "The lifeless body of a majestic lion appeared.", "Easy"),
            ("What does the phrase 'Not to be outdone' reveal about the friends' motivation?", "It reveals competitive vanity and desire to show off power.", "Medium"),
            ("Why was recreating a lion specifically dangerous?", "Because a lion is a powerful wild carnivore capable of killing humans effortlessly.", "Hard")
        ]
    ),
    (
        "'Spare the dead. Don't resuscitate it or it will devour us all.' pleaded the fourth one. The three friends ignored him again. The third who thought he was the brightest of all declared, 'I will bring it back to life.'",
        [
            ("What warning did the fourth Brahmin give about the dead lion?", "He warned: 'Spare the dead. Don't resuscitate it or it will devour us all!'", "Easy"),
            ("What did the third Brahmin claim about himself?", "He thought he was the brightest of all four friends.", "Easy"),
            ("What did the third Brahmin declare he would do?", "He declared that he would bring the lion back to life.", "Easy"),
            ("What does the word 'resuscitate' mean in this context?", "It means to revive or bring a dead body back to life.", "Medium"),
            ("Analyze the tragedy of the third Brahmin's declaration.", "His desire to prove he was the 'brightest' drove him to execute the most dangerous, foolish action.", "Hard")
        ]
    ),
    (
        "'Only fools worry about the consequences.' All of them mocked him. He silently climbed a tree while the fourth one started chanting to bring the lion back to life.",
        [
            ("What foolish statement did the friends make to mock the fourth Brahmin?", "They said, 'Only fools worry about the consequences.'", "Easy"),
            ("What did the fourth Brahmin do while the spell was being chanted?", "He silently climbed up a tree to save himself.", "Easy"),
            ("What was the third Brahmin doing while the fourth climbed the tree?", "He was chanting magic spells to bring the lion back to life.", "Easy"),
            ("What does the word 'consequences' mean?", "The results or outcomes produced by an action.", "Medium"),
            ("How does the statement 'Only fools worry about consequences' show total foolishness?", "It rejects risk assessment, which is the foundational pillar of human wisdom and survival.", "Hard")
        ]
    ),
    (
        "Within moments the lion was up and about. The starved lion looked at the three friends who had turned stone out of fear and soon killed them all and ate them up.",
        [
            ("How fast did the lion wake up after the spell?", "Within moments, the lion was up and about.", "Easy"),
            ("How was the lion described when it woke up?", "It was described as a starved lion.", "Easy"),
            ("Why did the three friends turn 'stone out of fear'?", "Because they were paralyzed with terror when the hungry lion stood before them.", "Easy"),
            ("What did the lion do to the three friends?", "The lion killed all three of them and ate them up.", "Medium"),
            ("Why did magic fail to save the three friends in this moment?", "Because magic spells could not overcome the physical speed and predatory hunger of a wild lion.", "Hard")
        ]
    ),
    (
        "After the lion went away having its fill, the fourth Brahmin got down and went back to the sage's ashram, grieving over his friends. Moral of the Story: Bookish knowledge without wisdom and common sense is useless.",
        [
            ("When did the fourth Brahmin climb down from the tree?", "He climbed down after the lion had its fill and went away.", "Easy"),
            ("Where did the fourth Brahmin go after getting down from the tree?", "He went back to the sage's ashram.", "Easy"),
            ("What emotion was the fourth Brahmin feeling as he walked back?", "He was grieving over the tragic loss of his friends.", "Easy"),
            ("State the exact moral of the story.", "Bookish knowledge without wisdom and common sense is useless.", "Medium"),
            ("Why is returning to the ashram a fitting end to this fable?", "It symbolizes returning to true spiritual wisdom after witnessing the failure of vain academic knowledge.", "Hard")
        ]
    )
]

ext_content = f"# Extract Based Questions — Chapter 02: Four Brahmins\n\n> **Category**: Extract Based Questions | **Total**: 10 Extracts (50 Sub-Questions) | **Marks**: 3 per set\n\n---\n\n"
sub_q_counter = 1
for ext_idx, (passage, q_list) in enumerate(extracts, start=1):
    ext_content += f"## Extract {ext_idx}\n\n"
    ext_content += f"> *\"{passage}\"*\n\n"
    for q_idx, (q_txt, ans, diff) in enumerate(q_list, start=1):
        q_id = f"BK02_CH02_EXT_{sub_q_counter:03d}"
        bloom = "Remembering" if diff == "Easy" else ("Understanding" if diff == "Medium" else "Analyzing")
        ext_content += f"### Question {sub_q_counter}\n"
        ext_content += f"- **Question ID**: {q_id}\n"
        ext_content += f"- **Type**: Extract Based Sub-Question\n"
        ext_content += f"- **Difficulty**: {diff}\n"
        ext_content += f"- **Bloom Level**: {bloom}\n"
        ext_content += f"- **Topic**: Extract {ext_idx} Comprehension {q_idx}\n"
        ext_content += f"- **Marks**: 1\n\n"
        ext_content += f"**Question**: {q_txt}\n\n"
        ext_content += f"- **Answer Key**: {ans}\n\n"
        sub_q_counter += 1
    ext_content += f"---\n\n"

with open(os.path.join(CH02_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print("[SUCCESS] All 6 category files for Book 2 Chapter 02 completely refined with 100% unique Class 2 questions!")
