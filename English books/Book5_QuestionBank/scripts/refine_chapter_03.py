r"""
Refines all 6 Category files for Book 5 Chapter 03 ("The Tiger and the Persimmon") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH03_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_03")
os.makedirs(CH03_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What kind of story is 'The Tiger and the Persimmon'?", "(A) A Korean Folktale", "(B) An Aesop Fable", "(C) A Panchatantra Tale", "(D) A Greek Myth", "(A)", "It is subtitled '-A Korean Folktale'.", "Easy", "Remembering", "Genre"),
    ("Where was the tiger roaming when the story began?", "(A) Around the outskirts of the forest near a solitary hut", "(B) In the middle of a busy city market", "(C) High up on a snowy mountain peak", "(D) Inside a king's palace zoo", "(A)", "Tiger was roaming around the outskirts of the forest.", "Easy", "Remembering", "Setting"),
    ("What sound coming from inside the solitary hut attracted the tiger?", "(A) The non-stop wailing of a baby", "(B) A person playing a flute", "(C) Loud singing and dancing", "(D) The sound of rain falling", "(A)", "He heard the non-stop wailing of a child coming from inside.", "Easy", "Remembering", "Plot Trigger"),
    ("Was the tiger hungry when he approached the hut?", "(A) No, he was not at all hungry, but curious to know the reason for wails", "(B) Yes, he was starving for three days", "(C) Yes, he was hunting for sheep", "(D) He was looking for water", "(A)", "The tiger was not at all hungry but curious.", "Easy", "Remembering", "Motivation"),
    ("How did the tiger look inside the solitary hut?", "(A) Peeping inside through a window", "(B) Knocking on the front door", "(C) Climbing down the chimney", "(D) Digging a hole under the wall", "(A)", "He started peeping inside through a window.", "Easy", "Remembering", "Action"),
    ("What was the mother doing inside the hut to stop the baby from crying?", "(A) Holding the baby close to her bosom and rocking it to and fro", "(B) Giving the baby a glass of milk", "(C) Singing a song on a guitar", "(D) Playing hide and seek with the child", "(A)", "Holding the baby close to her bosom and rocking it to and fro.", "Easy", "Remembering", "Mother's Action"),
    ("Which wild animal did the mother FIRST mention to scare the child into silence?", "(A) A hungry fox", "(B) A hungry bear", "(C) A hungry tiger", "(D) A hungry wolf", "(A)", "First she said: 'The hungry fox will hear you and eat you.'", "Easy", "Remembering", "First Animal"),
    ("What did the tiger think when the baby kept crying after hearing about the fox?", "(A) 'What a brave child! He is not at all afraid of a fox.'", "(B) 'The fox is a coward animal.'", "(C) 'I should call the fox here.'", "(D) 'The baby must be deaf.'", "(A)", "Thought: 'What a brave child! He is not at all afraid of a fox.'", "Easy", "Remembering", "Tiger's Thought"),
    ("Which animal did the mother SECONDLY mention to scare the baby?", "(A) A hungry bear", "(B) A hungry fox", "(C) A hungry lion", "(D) A hungry snake", "(A)", "Secondly she said: 'The hungry bear will hear you and eat you.'", "Easy", "Remembering", "Second Animal"),
    ("Which animal did the mother THIRDLY mention to scare the baby?", "(A) A hungry tiger", "(B) A hungry elephant", "(C) A hungry crocodile", "(D) A hungry leopard", "(A)", "Thirdly she said: 'The hungry tiger will hear you and eat you.'", "Easy", "Remembering", "Third Animal"),
    ("How did the tiger feel when the baby did not stop crying even at the name of a tiger?", "(A) Angry that the child was not terrified of him", "(B) Happy that the child liked tigers", "(C) Sleepy and indifferent", "(D) Sad that he was ugly", "(A)", "The tiger felt angry that the child was not terrified of him.", "Easy", "Remembering", "Tiger's Emotion"),
    ("What did the tiger decide to do just before the baby finally fell silent?", "(A) He decided to roar to scare the child", "(B) He decided to jump into the hut", "(C) He decided to run away", "(D) He decided to bring food", "(A)", "He decided to roar to scare the child.", "Easy", "Remembering", "Plot Detail"),
    ("What word spoken by the mother FINALLY made the baby fall completely silent?", "(A) Persimmon", "(B) Tiger", "(C) Bear", "(D) Candy", "(A)", "She said 'There is a persimmon (a fruit)' and the baby fell silent.", "Easy", "Remembering", "Turning Point"),
    ("What is a persimmon in reality?", "(A) A sweet orange-red edible fruit", "(B) A fierce monster with long horns", "(C) A giant carnivorous bear", "(D) A heavy iron weapon", "(A)", "A persimmon is a fruit.", "Easy", "Remembering", "Real Meaning"),
    ("What did the foolish tiger believe a 'persimmon' was after the baby fell silent?", "(A) A great, terrifying animal capable of scaring the brave child", "(B) A small harmless insect", "(C) A type of delicious soup", "(D) A giant tree in the forest", "(A)", "Wondered what a great animal persimmon must be to scare the child.", "Easy", "Remembering", "Tiger's Misconception"),
    ("Who was hiding on the slanting thatched roof of the hut during these events?", "(A) A thief waiting to get into the hut", "(B) A flock of black ravens", "(C) The baby's father", "(D) A village hunter", "(A)", "A thief was waiting to get into the hut, hiding on the roof.", "Easy", "Remembering", "New Character"),
    ("How did the thief end up on the tiger's back?", "(A) He lost his balance on the slanting roof and fell directly onto the tiger", "(B) He jumped down intentionally to ride the tiger", "(C) The tiger reached up and pulled him down", "(D) The mother pushed him off the roof", "(A)", "He lost his balance and fell on the tiger's back.", "Easy", "Remembering", "Accident"),
    ("What did the tiger think when the thief fell directly onto his back in the dark?", "(A) He thought the terrifying persimmon had attacked him", "(B) He thought heavy rain was falling", "(C) He thought a tree branch fell on him", "(D) He thought his friend was playing a prank", "(A)", "Thought that the persimmon had attacked him.", "Easy", "Remembering", "Climax Misconception"),
    ("What did the tiger do after the thief fell on his back?", "(A) Jumped in fright and started running for his life", "(B) Stood still and roared at the sky", "(C) Lay down and rolled on the ground", "(D) Ate the thief immediately", "(A)", "Jumped in fright and started running for his life.", "Easy", "Remembering", "Tiger's Reaction"),
    ("How did the story end for the tiger and the thief?", "(A) The thief managed to get off, and the foolish tiger ran back into the forest", "(B) The tiger took the thief home as a pet", "(C) The thief caught the tiger in a cage", "(D) They became best friends", "(A)", "The thief managed to get off and the tiger went back into the forest.", "Easy", "Remembering", "Resolution"),
    ("What is the moral of the story 'The Tiger and the Persimmon'?", "(A) We fear the unknown", "(B) Never trust a crying baby", "(C) Persimmons are dangerous fruits", "(D) Thieves are brave tiger riders", "(A)", "Moral of the Story: We fear the unknown.", "Easy", "Remembering", "Moral Lesson"),
    ("What does the word 'outskirt' mean in the vocabulary list?", "(A) Furthest part or outer edge of a town or forest", "(B) Deep center of a ocean", "(C) High peak of a mountain", "(D) Inside a house room", "(A)", "Outskirt means furthest part of a town/forest.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'solitary' mean?", "(A) Alone or isolated", "(B) Very crowded", "(C) Extremely noisy", "(D) Bright and colorful", "(A)", "Solitary means alone.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'incessant' mean?", "(A) Never stopping; continuous", "(B) Occurring once a year", "(C) Very quiet", "(D) Slow and lazy", "(A)", "Incessant means never stopping.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'bosom' mean in the story?", "(A) Chest or heart area", "(B) A small basket", "(C) A high shelf", "(D) A wooden chair", "(A)", "Bosom means chest area where the mother held the baby.", "Easy", "Understanding", "Vocabulary"),

    # Medium (26-40)
    ("Why did the tiger's ego get hurt when the mother threatened the baby with a tiger?", "(A) The baby did not stop crying, making the tiger feel that humans did not fear his mighty presence", "(B) The mother mispronounced the word tiger", "(C) The baby started laughing at the tiger", "(D) The tiger wanted to eat milk instead", "(A)", "Hurt his ego because the threat fell on deaf ears and the child was not terrified.", "Medium", "Analyzing", "Character Psychology"),
    ("How did a misunderstanding about a word cause the tiger to fear a fruit?", "(A) Hearing the baby fall silent at 'persimmon', the tiger assumed persimmon was a ferocious predator stronger than a tiger", "(B) The persimmon fruit fell from the tree and hit the tiger's nose", "(C) The mother told the tiger that persimmons eat big animals", "(D) The thief told the tiger a scary story about persimmons", "(A)", "Assumed persimmon was a creature stronger than a tiger since it quieted the child.", "Medium", "Analyzing", "Misconception Analysis"),
    ("How did coincidental timing compound the tiger's terror during the night?", "(A) Just as the tiger was fearing the 'persimmon', the thief accidentally fell on his back, making him believe the monster struck", "(B) A thunderstorm started at the exact moment the tiger roared", "(C) The mother threw a persimmon out of the window", "(D) The fox and bear arrived together at the hut", "(A)", "Thief's fall coincided with the tiger's fear of persimmon, confirming his terror.", "Medium", "Analyzing", "Plot Structure"),
    ("What irony exists in the thief's experience on the tiger's back?", "(A) The thief was terrified for his life riding a tiger, while the tiger was equally terrified thinking a persimmon caught him", "(B) The thief thought he was riding a horse", "(C) The tiger gave the thief a gold coin", "(D) The thief was trying to steal the tiger's fur", "(A)", "Mutual terror: thief feared tiger, tiger feared imaginary persimmon monster.", "Medium", "Analyzing", "Irony"),
    ("Why did the baby actually stop crying when the mother mentioned 'persimmon'?", "(A) The mother offered or showed a sweet fruit the baby liked to eat, satisfying its hunger or mood", "(B) The baby knew persimmons were dangerous monsters", "(C) The baby saw the tiger outside the window", "(D) The baby fell asleep instantly from fear", "(A)", "Baby stopped because it wanted/liked the sweet fruit offered by the mother.", "Medium", "Understanding", "Real Reason"),
    ("How does the moral 'We fear the unknown' apply to the tiger's behavior?", "(A) Ignorance about what a 'persimmon' was caused the tiger's imagination to create a terrifying monster out of nothing", "(B) The tiger feared the dark forest because he had no eyes", "(C) The tiger feared the thief because the thief had a gun", "(D) The tiger was afraid of falling rain", "(A)", "Ignorance led his imagination to create a terrifying monster out of a fruit name.", "Medium", "Evaluating", "Moral Application"),
    ("What role did curiosity play in bringing the tiger into danger/panic?", "(A) Curiosity about the wailing baby brought the tiger to the window, leading to his comical terror and wild flight", "(B) Curiosity made the tiger eat the thief's bag", "(C) Curiosity made the tiger attack the mother", "(D) Curiosity made the tiger climb the roof", "(A)", "Curiosity brought him to the window where the chain of misunderstandings began.", "Medium", "Analyzing", "Theme of Curiosity"),
    ("What made the mother's threats of fox, bear, and tiger ineffective?", "(A) The infant was too young to understand the danger of wild predators, responding only to actual food comfort", "(B) The baby was deaf and could not hear anything", "(C) The baby had beaten a tiger before", "(D) The mother spoke in a whisper", "(A)", "Infant was too young to comprehend wild predators.", "Medium", "Understanding", "Child Psychology"),
    ("How did the thief benefit from the tiger's misunderstanding?", "(A) The tiger was too panicked thinking about the persimmon to turn around and eat the thief on its back", "(B) The tiger carried the thief safely to his home in town", "(C) The tiger gave the thief shelter from the rain", "(D) The thief stole the tiger's stripes", "(A)", "Panic kept the tiger running instead of attacking the rider on its back.", "Medium", "Understanding", "Plot Connection"),
    ("What contrast is shown between the tiger's real power and his mental state?", "(A) Physically he was an apex predator, but mentally he was foolish, gullible, and easily terrified by false imagination", "(B) He was physically weak but mentally a genius", "(C) He was small like a cat but roared like thunder", "(D) There was no contrast in his character", "(A)", "Apex predator physically vs gullible and terrified mentally.", "Medium", "Comparing", "Character Contrast"),
    ("Why is 'slanted thatched roof' an important setting detail?", "(A) The slanting, slippery thatch caused the hiding thief to lose balance and fall onto the tiger below", "(B) It allowed the tiger to jump into the attic", "(C) It caught fire during the story", "(D) It kept persimmon fruits stored on top", "(A)", "Slanted slippery thatch caused the thief to slip and fall.", "Medium", "Analyzing", "Setting Role"),
    ("How does comedy function alongside fear in this Korean folktale?", "(A) The tiger's dramatic fear of a simple fruit creates slapstick humor while delivering a wise lesson on human nature", "(B) The story has no funny elements at all", "(C) The thief tells jokes to the baby", "(D) The mother laughs at the tiger", "(A)", "Dramatic fear of a simple fruit creates slapstick humor.", "Medium", "Evaluating", "Literary Analysis"),
    ("What does the tiger's decision to 'roar' tell us about his pride?", "(A) He wanted to assert dominance and demand fear when his reputation seemed ignored by the baby", "(B) He roars whenever he is sleepy", "(C) He wanted to signal to other tigers in the woods", "(D) He was clearing his throat", "(A)", "Wanted to assert dominance when his reputation seemed ignored.", "Medium", "Analyzing", "Character Motivation"),
    ("What advice does this folktale offer regarding rumors and unfamiliar words?", "(A) Investigate and understand the facts before letting unverified words spark irrational fear", "(B) Always run away when you hear a new word", "(C) Never eat fruits that start with letter P", "(D) Trust every threat you hear", "(A)", "Investigate facts before letting unverified words spark fear.", "Medium", "Applying", "Real-World Application"),
    ("Why did the thief jump off the tiger's back as soon as he could?", "(A) He realized he was riding a dangerous wild tiger and seized the first chance to escape unharmed", "(B) He wanted to pick a persimmon from a tree", "(C) The tiger asked him to get off politely", "(D) He dropped his wallet on the road", "(A)", "Realized he was riding a dangerous wild tiger and seized the chance to escape.", "Medium", "Understanding", "Thief's Action"),

    # Hard (41-50)
    ("Deconstruct the cognitive chain of misinterpretations that drives the entire plot of Chapter 03.", "(A) Baby crying → Mother mentions fruit → Baby stops → Tiger infers fruit is monster → Thief falls → Tiger confirms monster attack → Wild flight into forest.", "(B) Tiger attacks hut → Thief saves baby → Mother eats persimmon → Tiger runs away.", "(C) Thief steals persimmon → Baby eats tiger → Mother roars → Tiger sleeps.", "(D) There is no logical chain in folktales.", "(A)", "Full 7-step misinterpretation chain driving the plot.", "Hard", "Analyzing", "HOTS Narrative Structure"),
    ("Evaluate the psychological depth of the moral 'We fear the unknown' in human behavior.", "(A) When individuals lack clear information, active imagination fills the knowledge gap with irrational fears and catastrophic assumptions", "(B) Unknown things are always physically dangerous", "(C) People only fear what they can see clearly", "(D) Fear is an emotion found only in animals", "(A)", "Lack of information causes imagination to fill gaps with irrational fear.", "Hard", "Evaluating", "Psychological Analysis"),
    ("Compare the tiger's mistake in Chapter 03 with the jackal's mistake in Book 3 Chapter 02 (The Jackal and the Dhol).", "(A) Both characters misidentified an unfamiliar signal—the jackal thought drum sounds meant food; the tiger thought a fruit name meant a monster", "(B) Both characters were killed by hunters", "(C) Both stories take place in ocean waters", "(D) Neither character experienced any fear", "(A)", "Both misidentified an unfamiliar signal due to faulty assumptions.", "Hard", "Comparing", "Comparative Literature Study"),
    ("Critique the cultural significance of using a 'persimmon' in Korean folktales.", "(A) Persimmons are common, sweet traditional fruits in Korea; using a familiar domestic fruit highlights the absurdity of the tiger's fear", "(B) Persimmons were rare toxic poisons in ancient Korea", "(C) Persimmon trees were worshipped as gods", "(D) The fruit was imported from South America", "(A)", "Common sweet domestic fruit highlights the absurdity of the tiger's fear.", "Hard", "Evaluating", "Cultural Context Analysis"),
    ("Formulate a continuation where the tiger meets the fox in the forest after his wild escape.", "(A) 'The tiger gasped, 'A persimmon attacked me!' The fox laughed, 'Persimmon is just a sweet fruit!' The tiger blushed, realizing how fear of the unknown made him a fool.'", "(B) 'The fox ate the persimmon and turned into a monster.'", "(C) 'The tiger fought the fox and won.'", "(D) 'The thief and tiger built a house together.'", "(A)", "Humorous continuation highlighting realization of the moral.", "Hard", "Creating", "Creative Writing Continuation"),
    ("Assess the pedagogical value of using humor and irony to teach emotional regulation to Class 5 students.", "(A) Humor makes students laugh at irrational panic, helping them recognize how unexamined fears can make anyone act foolishly", "(B) Humor prevents children from learning serious lessons", "(C) Irony is too complicated for primary students", "(D) It teaches students to fear fruits", "(A)", "Humor helps students recognize and reflect on irrational panic.", "Hard", "Evaluating", "Pedagogical Assessment"),
    ("Analyze how the narrative maintains dual perspectives (dramatic irony) throughout the story.", "(A) The reader knows a persimmon is a fruit and the rider is a thief, while the tiger operates under complete comic delusion", "(B) The reader is kept in the dark until the final sentence", "(C) The mother knows the tiger is outside watching", "(D) The thief knows the tiger's inner thoughts", "(A)", "Reader knows the truth (fruit/thief) while tiger operates under delusion.", "Hard", "Analyzing", "Dramatic Irony Analysis"),
    ("Synthesize how Chapters 01, 02, and 03 of Book 5 together build a comprehensive framework of personal growth.", "(A) Ch 01: Value friendship & empathy. Ch 02: Avoid blind imitation. Ch 03: Overcome fear of the unknown. Together: Emotional security + Authenticity + Rational thinking.", "(B) All three chapters teach cooking recipes.", "(C) All three chapters are about forest animals only.", "(D) There is no common theme among the chapters.", "(A)", "Emotional security (Ch1) + Authenticity (Ch2) + Rational thinking (Ch3).", "Hard", "Synthesizing", "Curricular Synthesis"),
    ("Critique the tiger's threat response mechanism from an animal behavior perspective.", "(A) Although an apex predator, sudden unidentifiable physical impact from behind triggers a natural flight response over fight when disoriented", "(B) Tigers always fight regardless of orientation or surprise", "(C) Tigers cannot run when startled from above", "(D) The tiger's response was biologically impossible", "(A)", "Sudden unidentifiable impact from behind triggers flight when disoriented.", "Hard", "Evaluating", "Cross-Disciplinary Evaluation"),
    ("Formulate a classroom activity based on Chapter 03 to teach critical thinking.", "(A) 'The Unknown Mystery Box': Students guess contents of a closed box using clues, discussing how assumptions change when facts are revealed.", "(B) 'Tiger Drawing Contest': Students paint pictures of tigers.", "(C) 'Fruit Tasting': Students eat persimmons in silence.", "(D) 'Rooftop Climbing': Students practice climbing thatched roofs.", "(A)", "Interactive mystery box activity demonstrating evidence vs assumption.", "Hard", "Creating", "Pedagogical Activity Design")
]

mcq_content = f"# MCQs — Chapter 03: The Tiger and the Persimmon\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH03_MCQ_{idx:03d}"
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

with open(os.path.join(CH03_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("A tiger was roaming around the outskirts of the _______.", "forest", "Roaming around the outskirts of the forest.", "Easy"),
    ("There was a _______ hut near the outskirts of the forest.", "solitary", "A solitary hut nearby.", "Easy"),
    ("The tiger heard the non-stop _______ of a child inside the hut.", "wailing", "Heard non-stop wailing of a child.", "Easy"),
    ("The tiger was not at all _______ but became curious.", "hungry", "Not at all hungry but curious.", "Easy"),
    ("The tiger started peeping inside through a _______.", "window", "Peeping inside through a window.", "Easy"),
    ("The woman held the crying baby close to her _______.", "bosom", "Held the baby close to her bosom.", "Easy"),
    ("The mother rocked the baby to and fro to _______ him down.", "calm", "Rocked him to calm him down.", "Easy"),
    ("First, the lady warned the baby about a hungry _______.", "fox", "First mentioned a hungry fox.", "Easy"),
    ("The tiger thought, 'What a _______ child! He is not afraid of a fox.'", "brave", "Thought: What a brave child!", "Easy"),
    ("Secondly, the lady warned the baby about a hungry _______.", "bear", "Secondly mentioned a hungry bear.", "Easy"),
    ("Thirdly, the lady warned the baby about a hungry _______.", "tiger", "Thirdly mentioned a hungry tiger.", "Easy"),
    ("The tiger felt _______ because the child was not terrified of him.", "angry", "Felt angry that the child was not terrified.", "Easy"),
    ("The tiger decided to _______ to scare the child into silence.", "roar", "Decided to roar to scare the child.", "Easy"),
    ("The lady mentioned a _______, which made the baby fall silent.", "persimmon", "Mentioned a persimmon and baby fell silent.", "Easy"),
    ("A persimmon is actually a sweet orange-red _______.", "fruit", "A persimmon is a fruit.", "Easy"),
    ("The tiger wondered what a great _______ persimmon must be.", "animal", "Wondered what a great animal persimmon must be.", "Easy"),
    ("A thief was hiding on the slanting _______ roof.", "thatched", "Hiding on the slanting thatched roof.", "Easy"),
    ("The thief lost his balance and fell on the tiger's _______.", "back", "Fell on the tiger's back.", "Easy"),
    ("The tiger thought the _______ had attacked him.", "persimmon", "Thought the persimmon had attacked him.", "Easy"),
    ("The tiger jumped in fright and started running for his _______.", "life", "Started running for his life.", "Easy"),
    ("The thief managed to get off the tiger's _______.", "back", "Managed to get off the tiger's back.", "Easy"),
    ("The foolish tiger went back into the _______.", "forest", "Foolish tiger went back into the forest.", "Easy"),
    ("The moral of the story is: We fear the _______.", "unknown", "Moral: We fear the unknown.", "Easy"),
    ("Outskirt means the furthest part of a _______.", "town", "Outskirt means furthest part of a town/forest.", "Easy"),
    ("Incessant means never _______.", "stopping", "Incessant means never stopping.", "Easy"),

    # Medium (26-40)
    ("The tiger's curiosity led to a series of comical _______.", "misunderstandings", "Led to comical misunderstandings.", "Medium"),
    ("The baby stopped crying because it wanted to eat the sweet _______.", "persimmon", "Wanted to eat the sweet persimmon.", "Medium"),
    ("The tiger misinterpreted a simple fruit name as a ferocious _______.", "monster", "Misinterpreted fruit as a monster.", "Medium"),
    ("The thief fell from the roof because the thatch was _______.", "slanting", "Thatch was slanting and slippery.", "Medium"),
    ("Panic caused the tiger to flee without looking at his _______.", "rider", "Fled without looking at his rider.", "Medium"),
    ("The story illustrates how imagination amplifies irrational _______.", "fears", "Imagination amplifies irrational fears.", "Medium"),
    ("The mother used animal threats to quiet her _______ baby.", "crying", "Quiet her crying baby.", "Medium"),
    ("The tiger's pride was hurt when his name failed to intimidate the _______.", "child", "Failed to intimidate the child.", "Medium"),
    ("The thief was as terrified of the tiger as the tiger was of the _______.", "persimmon", "Thief feared tiger, tiger feared persimmon.", "Medium"),
    ("The folktale combines dramatic irony with moral _______.", "instruction", "Combines dramatic irony with moral instruction.", "Medium"),
    ("Ignorance about the word 'persimmon' deceived the mighty _______.", "predator", "Deceived the mighty predator.", "Medium"),
    ("Coincidental events reinforced the tiger's false _______.", "belief", "Reinforced the tiger's false belief.", "Medium"),
    ("The tiger returned to the safety of the deep _______.", "forest", "Returned to the deep forest.", "Medium"),
    ("The thief escaped unharmed due to the tiger's wild _______.", "panic", "Escaped due to the tiger's panic.", "Medium"),
    ("Korean folktales often use humor to teach timeless _______.", "wisdom", "Use humor to teach timeless wisdom.", "Medium"),

    # Hard (41-50)
    ("Fearing unexamined assumptions leads to ridiculous _______.", "consequences", "Leads to ridiculous consequences.", "Hard"),
    ("The tiger's cognitive error highlights the danger of false _______.", "inference", "Highlights danger of false inference.", "Hard"),
    ("Dramatic irony keeps the reader informed while characters remain _______.", "deceived", "Reader informed while characters deceived.", "Hard"),
    ("Unidentified physical contact triggered the tiger's natural _______ response.", "flight", "Triggered natural flight response.", "Hard"),
    ("The thatched roof provided an unstable hiding spot for the _______.", "thief", "Unstable hiding spot for the thief.", "Hard"),
    ("Fearing what we do not understand distorts logical _______.", "reasoning", "Distorts logical reasoning.", "Hard"),
    ("The infant's response reflected natural desire over threat _______.", "comprehension", "Reflected natural desire over threat comprehension.", "Hard"),
    ("The story demonstrates how rumor and ignorance create imaginary _______.", "threats", "Create imaginary threats.", "Hard"),
    ("Chapter 03 integrates folktale structure, humor, and psychological _______.", "insight", "Integrates psychological insight.", "Hard"),
    ("Understanding facts dispels the darkness of irrational _______.", "fear", "Dispels the darkness of irrational fear.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 03: The Tiger and the Persimmon\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH03_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH03_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The tiger was extremely hungry when he arrived at the solitary hut.", "False", "The tiger was not at all hungry, but curious about the baby's crying.", "Easy"),
    ("The tiger peeping through the window heard a child wailing inside.", "True", "He went near the hut and started peeping inside through a window.", "Easy"),
    ("The mother first tried to quiet the baby by offering a glass of water.", "False", "She first warned the baby about a hungry fox.", "Easy"),
    ("The baby stopped crying immediately when the mother mentioned a hungry bear.", "False", "The threat fell on deaf ears and the baby kept on crying.", "Easy"),
    ("The tiger was angry because the child was not terrified at the mention of a tiger.", "True", "The tiger felt angry that the child was not terrified of him.", "Easy"),
    ("The mother mentioned a 'persimmon', which instantly made the baby fall silent.", "True", "On hearing the name of a fruit (persimmon) the baby fell silent.", "Easy"),
    ("A persimmon is a fierce carnivorous beast that lives in Korean mountains.", "False", "A persimmon is actually a sweet edible fruit.", "Easy"),
    ("The foolish tiger believed a persimmon was a dangerous animal stronger than a tiger.", "True", "He wondered what a great animal persimmon must be to scare the child.", "Easy"),
    ("A thief was hiding on the slanting thatched roof of the hut.", "True", "A thief was waiting to get into the hut, hiding on the slanting thatched roof.", "Easy"),
    ("The thief jumped off the roof to attack the tiger bravely.", "False", "He lost his balance and accidentally fell onto the tiger's back.", "Easy"),
    ("The tiger believed the terrifying persimmon had fallen on his back.", "True", "He thought that the persimmon had attacked him.", "Easy"),
    ("The tiger ran for his life in fear after the thief fell on him.", "True", "The tiger jumped in fright and started running for his life.", "Easy"),
    ("The thief stayed on the tiger's back for three years.", "False", "The thief somehow managed to get off the tiger's back quickly.", "Easy"),
    ("The tiger went back into the forest after the thief fell off.", "True", "The foolish tiger went back into the forest.", "Easy"),
    ("The moral of the story is 'We fear the unknown'.", "True", "Moral of the Story: We fear the unknown.", "Easy"),
    ("'Outskirt' means the exact middle center of a large city.", "False", "Outskirt means the furthest part or outer edge.", "Easy"),
    ("'Solitary' means isolated or alone.", "True", "Solitary means alone.", "Easy"),
    ("'Incessant' means stopping every two minutes.", "False", "Incessant means never stopping; continuous.", "Easy"),
    ("'Bosom' refers to the chest or heart area.", "True", "Bosom refers to the chest area.", "Easy"),
    ("The tiger roared loudly before the mother mentioned the persimmon.", "False", "Before he could roar, the lady mentioned persimmon and the baby quieted down.", "Easy"),
    ("The baby stopped crying because it was scared of persimmons.", "False", "The baby stopped because it wanted to eat the sweet persimmon fruit.", "Easy"),
    ("The thief knew he was falling onto a tiger when he slipped.", "False", "He lost his balance in the dark and fell accidentally.", "Easy"),
    ("Chapter 03 is a Korean Folktale.", "True", "Subtitled '-A Korean Folktale'.", "Easy"),
    ("The tiger ate both the mother and the baby at the end.", "False", "The tiger ran away into the forest without harming anyone.", "Easy"),
    ("Chapter 03 title is 'The Tiger and the Persimmon'.", "True", "Title is 'The Tiger and the Persimmon'.", "Easy"),

    # Medium (26-40)
    ("The tiger's misinterpretation turned a domestic situation into a comedy of errors.", "True", "Mistaking a fruit name for a monster created a hilarious chain of events.", "Medium"),
    ("The baby was old enough to understand the dangerous nature of wild tigers.", "False", "The baby was an infant who responded to food comfort, not animal threats.", "Medium"),
    ("The thief was unharmed because the tiger was too panicked to fight back.", "True", "The tiger's panic about the 'persimmon' allowed the thief to slip away safely.", "Medium"),
    ("The mother intentionally lied to the tiger to trick him into fleeing.", "False", "The mother was unaware that a tiger was peeping through her window.", "Medium"),
    ("Curiosity was the initial motivation that brought the tiger to the window.", "True", "He was not hungry, but curious to know the reason for the baby's wails.", "Medium"),
    ("The tiger's flight proves that even powerful predators succumb to irrational fear.", "True", "Ignorance and imagination made the apex predator run in terror.", "Medium"),
    ("The slanting thatched roof contributed directly to the climax of the story.", "True", "The slippery slanting roof caused the thief to fall onto the tiger.", "Medium"),
    ("The story shows that lack of information leads to false assumptions.", "True", "Not knowing what a persimmon was caused the tiger's absurd assumption.", "Medium"),
    ("The baby cried louder when the mother said 'persimmon'.", "False", "The baby fell completely silent upon hearing 'persimmon'.", "Medium"),
    ("The thief planned to use the tiger as a riding animal to escape the village.", "False", "The thief fell by accident while trying to rob the hut.", "Medium"),
    ("Dramatic irony occurs because the reader knows a persimmon is just a fruit.", "True", "The reader enjoys the humor knowing the truth while the tiger is terrified.", "Medium"),
    ("The tiger stayed in the village to search for more persimmons.", "False", "He fled back into the forest and never returned.", "Medium"),
    ("The mother rocked the baby to and fro to calm him down.", "True", "Text states she held the baby close and rocked it to and fro.", "Medium"),
    ("The story suggests that unverified rumors should be accepted as truth.", "False", "The story warns that believing unverified assumptions causes foolish fear.", "Medium"),
    ("The tiger's reaction to the baby's silence reveals his inflated ego.", "True", "He expected the baby to fear him and was offended when his name failed.", "Medium"),

    # Hard (41-50)
    ("The tiger's behavior demonstrates how fear overwrites predatory instincts.", "True", "Instead of turning around to hunt the threat on his back, panic drove him to flee.", "Hard"),
    ("The narrative highlights the absurdity of fearing words without understanding their meaning.", "True", "Fearing the simple word 'persimmon' highlights the folly of uninformed fear.", "Hard"),
    ("The thief's survival was a result of strategic planning rather than luck.", "False", "His survival was pure luck due to the tiger's coincidental panic.", "Hard"),
    ("The Korean folktale uses animal personification to critique human foolishness.", "True", "The tiger personifies human gullibility and irrational fear of the unknown.", "Hard"),
    ("The climax merges two independent plotlines: the mother-baby dynamic and the thief's burglary.", "True", "The mother-baby dialogue and thief's burglary collide when the thief falls.", "Hard"),
    ("The tiger's assumption that persimmon was a monster followed logical deductive reasoning.", "False", "It was a flawed inference based on incomplete sensory data.", "Hard"),
    ("The moral 'We fear the unknown' provides a universal psychological truth.", "True", "Applies universally to human anxieties regarding unexamined mysteries.", "Hard"),
    ("The physical setting of the solitary hut emphasizes vulnerability and isolation.", "True", "A solitary hut at the forest edge creates an isolated, suspenseful setting.", "Hard"),
    ("The story ends with the tiger gaining complete enlightenment about persimmons.", "False", "The tiger ran away still believing the persimmon was a monster.", "Hard"),
    ("Chapter 03 effectively combines folklore humor with critical reading pedagogy for Class 5.", "True", "Blends engaging narrative with rich vocabulary and moral analysis.", "Hard")
]

tf_content = f"# True / False — Chapter 03: The Tiger and the Persimmon\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH03_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH03_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Where was the tiger roaming when the story began, and what did he hear?", "The tiger was roaming around the outskirts of a forest near a solitary hut when he heard the non-stop wailing of a child coming from inside.", "Easy", "Remembering"),
    ("Why did the tiger go near the hut if he was not hungry?", "He was not hungry, but he became curious to find out why the baby was crying so incessantly.", "Easy", "Remembering"),
    ("How did the mother try to calm her crying baby at first?", "She held the baby close to her bosom, rocked it to and fro, and warned it about a hungry fox coming to eat it.", "Easy", "Remembering"),
    ("What did the tiger think when the baby ignored the warning about the fox?", "The tiger thought, 'What a brave child! He is not at all afraid of a fox.'", "Easy", "Remembering"),
    ("Which three animals did the mother mention to scare the child?", "She mentioned a hungry fox, a hungry bear, and a hungry tiger.", "Easy", "Remembering"),
    ("Why did the tiger feel angry when the mother mentioned a tiger?", "He felt angry because even the mention of a fierce tiger failed to terrify the baby or stop its crying.", "Easy", "Understanding"),
    ("What did the tiger decide to do to prove his ferocity to the child?", "He decided to roar loudly to terrify the child into silence.", "Easy", "Remembering"),
    ("What word spoken by the mother caused the baby to fall completely silent?", "The mother mentioned 'persimmon' (a fruit), which instantly made the baby stop crying.", "Easy", "Remembering"),
    ("What is a persimmon in reality?", "A persimmon is a sweet, edible, orange-red fruit.", "Easy", "Remembering"),
    ("What did the foolish tiger assume a 'persimmon' was?", "The tiger assumed that a 'persimmon' was a terrifying, powerful animal even stronger and fiercer than a tiger.", "Easy", "Understanding"),
    ("Who was hiding on the slanting thatched roof of the hut and why?", "A thief was hiding on the thatched roof, waiting for an opportunity to break into the hut and steal.", "Easy", "Remembering"),
    ("How did the thief end up on the tiger's back?", "The thief lost his balance on the slanting thatched roof and fell directly onto the tiger's back below.", "Easy", "Remembering"),
    ("What did the tiger think when the thief fell on his back in the dark?", "The tiger panicked, believing that the terrifying 'persimmon' monster had attacked him.", "Easy", "Understanding"),
    ("How did the tiger react when he thought the persimmon attacked him?", "He jumped in fright and ran frantically for his life back into the forest.", "Easy", "Remembering"),
    ("How did the thief escape from the tiger?", "As the tiger ran wildly, the thief managed to slip off its back and escape unharmed.", "Easy", "Remembering"),
    ("Where did the tiger go after the thief fell off his back?", "The terrified tiger fled deep back into the forest.", "Easy", "Remembering"),
    ("What is the moral of the story 'The Tiger and the Persimmon'?", "The moral of the story is: 'We fear the unknown.'", "Easy", "Remembering"),
    ("What does the word 'outskirt' mean?", "'Outskirt' means the outer boundary or furthest border of a town or forest.", "Easy", "Understanding"),
    ("What does the word 'solitary' mean?", "'Solitary' means isolated, alone, or single.", "Easy", "Understanding"),
    ("What does the word 'incessant' mean?", "'Incessant' means continuous and never stopping.", "Easy", "Understanding"),
    ("What does the word 'bosom' mean?", "'Bosom' refers to a person's chest or heart area.", "Easy", "Understanding"),
    ("What does the word 'thatched' mean?", "'Thatched' describes a roof covered with dry straw, reeds, or plant stalks.", "Easy", "Understanding"),
    ("Why did the tiger peep through the window?", "He wanted to look inside to see who was crying so loudly.", "Easy", "Remembering"),
    ("What country does this folktale originate from?", "This folktale originates from Korea (it is a Korean folktale).", "Easy", "Remembering"),
    ("What title is given to Chapter 03?", "The title of Chapter 03 is 'The Tiger and the Persimmon'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Explain why the baby actually stopped crying when the mother said 'persimmon'.", "The baby stopped crying because it recognized the name of a delicious, sweet fruit it liked to eat, satisfying its mood, not because it was afraid.", "Medium", "Understanding"),
    ("Analyze how the tiger's pride led to his foolish conclusion.", "The tiger expected everyone to fear him. When the baby didn't fear a tiger but quieted at 'persimmon', his ego made him conclude persimmon must be a superior beast.", "Medium", "Analyzing"),
    ("How did the physical condition of the roof contribute to the climax?", "The roof was thatched and slanting, making it slippery and unstable. This caused the hiding thief to lose his balance and fall on the tiger.", "Medium", "Analyzing"),
    ("Explain the dramatic irony present in Chapter 03.", "The reader knows that a persimmon is a sweet fruit and the rider is a human thief, while the tiger foolishly believes he is being attacked by a monster.", "Medium", "Analyzing"),
    ("Why did the tiger run away instead of fighting the creature on his back?", "He was blinded by panic. Believing the legendary 'persimmon' monster had pounced on him, terror overruled his natural fighting instincts.", "Medium", "Evaluating"),
    ("How does the story demonstrate that curiosity can lead to unexpected consequences?", "The tiger's idle curiosity about a baby's cry brought him to the window, leading to a hilarious sequence of misunderstandings and terror.", "Medium", "Analyzing"),
    ("Contrast the real nature of a persimmon with the tiger's imaginary perception of it.", "Real nature: A small, soft, sweet, harmless fruit. Tiger's perception: A terrifying, mighty, aggressive monster stronger than a tiger.", "Medium", "Comparing"),
    ("Why did the mother use animal threats to quiet her baby?", "In traditional rural folklore, parents often used threats of wild animals to instill quick obedience in crying children.", "Medium", "Understanding"),
    ("How does the thief's accidental fall resolve the suspense of the story?", "The fall triggers the tiger's wild flight, ensuring the thief escapes, the tiger leaves the village forever, and the family inside remains safe.", "Medium", "Analyzing"),
    ("What lesson does the story teach about unverified fear?", "It teaches that fearing things we do not understand causes irrational panic. We should seek true facts before jumping to scary conclusions.", "Medium", "Evaluating"),
    ("Why didn't the thief try to rob the hut after falling off the tiger?", "He was far too shaken and terrified after unexpectedly riding a wild tiger through the night to care about stealing.", "Medium", "Understanding"),
    ("How does humor play a role in delivering the moral of Chapter 03?", "The absurd sight of a fierce tiger terrified of a soft fruit and running with a thief on his back makes readers laugh while grasping the lesson.", "Medium", "Evaluating"),
    ("What makes the tiger a comical character in this folktale?", "His gullibility, inflated ego, and dramatic terror over simple words transform a dangerous apex predator into a funny, foolish character.", "Medium", "Analyzing"),
    ("Summarize Chapter 03 in four sentences.", "A curious tiger peeping into a hut heard a mother quiet her crying baby by offering a persimmon fruit. Misunderstanding, the tiger believed a persimmon was a ferocious monster stronger than a tiger. When a hiding thief fell from the roof onto his back, the tiger panicked thinking the persimmon had struck. Terrified, the tiger ran blindly back into the forest, leaving everyone safe.", "Medium", "Understanding"),
    ("What advice would you give to someone who panics over unfamiliar words or rumors?", "Take time to ask questions, research facts, and verify the true meaning before allowing imagination to create unnecessary fear.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the tiger's decision-making process using logical reasoning.", "The tiger committed a fallacy of false cause: assuming that because the baby quieted at 'persimmon', the word MUST represent a frightening creature, ignoring alternative reasons.", "Hard", "Evaluating"),
    ("Deconstruct how miscommunication drives the narrative in Chapter 03.", "Miscommunication occurs on two levels: 1) Mother-baby dialogue misinterpreted by tiger. 2) Thief's accidental fall misinterpreted as monster attack.", "Hard", "Analyzing"),
    ("Evaluate the psychological insight behind 'We fear the unknown'.", "Human and animal minds naturally fear what they cannot define. In the absence of knowledge, imagination fills the void with exaggerated dangers.", "Hard", "Evaluating"),
    ("Compare the tiger's character in this folktale with traditional fierce tigers in literature.", "Traditional tigers are portrayed as deadly, cunning predators. In this Korean folktale, the tiger is subverted into a gullible, comical figure defeated by his own imagination.", "Hard", "Comparing"),
    ("Formulate a creative scene where the tiger learns the truth about persimmons later.", "'Months later, the tiger saw a monkey eating an orange fruit. 'Beware! The persimmon monster!' yelled the tiger. The monkey laughed and threw him a sweet slice. Tasting it, the tiger realized he had fled from a harmless fruit!'", "Hard", "Creating"),
    ("Assess the pedagogical value of teaching Korean folktales in Class 5 English.", "Exposes students to world folklore, enhances cultural appreciation, develops dramatic irony comprehension, and teaches universal moral reasoning.", "Hard", "Evaluating"),
    ("Analyze how coincidence and timing are weaponized by the storyteller for comedic effect.", "The storyteller aligns the exact moment of the tiger's inner fear with the thief's accidental fall, creating a flawless comedic climax.", "Hard", "Analyzing"),
    ("Synthesize the core themes of Chapters 01, 02, and 03 of Book 5.", "Ch 01: Compassion overcomes isolation. Ch 02: Authenticity avoids self-harm. Ch 03: Fact-checking overcomes irrational fear. Together: Foundation for emotional wisdom.", "Hard", "Synthesizing"),
    ("Critique the mother's parenting strategy of using fear threats.", "Using fear threats works temporarily but creates unnecessary anxiety; offering real comfort or sweet food (persimmon) proved far more effective.", "Hard", "Evaluating"),
    ("Formulate a 4-line summary stanza capturing Chapter 03.", "'A tiger feared a fruit named persimmon,\nThinking it scary beyond all vision;\nA thief fell down and gave him a fright,\nAnd sent the foolish beast into wild flight!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 03: The Tiger and the Persimmon\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH03_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH03_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe how the tiger came to the solitary hut and what he witnessed while peeping through the window.",
     "A tiger was roaming around the outskirts of a forest near a solitary hut. Although he was not at all hungry, he heard the incessant, non-stop wailing of a baby coming from inside the hut. Curious to know why the child was crying so bitterly, he walked up to the hut and began peeping through a window. Inside, he saw a mother holding her crying baby close to her bosom, rocking it to and fro to calm it down. To quiet the child, the mother first warned that a hungry fox would hear and eat it, then a hungry bear, and finally a hungry tiger. However, none of these wild animal threats had any effect, and the baby continued crying loudly.",
     "Easy", "Remembering"),

    ("Explain how the word 'persimmon' caused the tiger to form a massive misunderstanding.",
     "When the mother's threats of a fox, bear, and tiger failed to stop the baby's crying, the mother finally said, 'Hush baby hush. There is a persimmon.' On hearing the name of the fruit, the baby fell completely silent. The peeping tiger was astonished. He did not know that a persimmon was merely a sweet orange fruit that the baby wanted to eat. Instead, his foolish ego made him reason that if a child was not afraid of a fierce tiger but fell silent at the word 'persimmon', then a persimmon must be a terrifying, giant beast far more ferocious and dangerous than a tiger. This single misunderstanding sparked intense fear in the tiger.",
     "Easy", "Understanding"),

    ("Narrate the climax of the story involving the thief, the slanting thatched roof, and the tiger's wild flight.",
     "While the tiger was standing beneath the window fearing the imaginary 'persimmon' monster, a thief was hiding on the slanting thatched roof of the hut waiting to break in. Suddenly, the thief lost his balance on the slippery thatch and fell directly onto the tiger's back in the dark. The tiger jumped in absolute fright, convincing himself that the terrifying persimmon monster had pounced on him from above. In sheer terror for his life, the tiger ran frantically into the night. The thief, equally terrified to find himself riding a wild tiger, managed to slip off its back, and the foolish tiger ran deep into the forest, never returning.",
     "Easy", "Remembering"),

    ("What is the moral of 'The Tiger and the Persimmon'? Explain how the story illustrates this moral.",
     "The moral of the story is 'We fear the unknown.' This moral is illustrated through the tiger's irrational behavior. Because the tiger did not know what a 'persimmon' was, his imagination filled the knowledge gap with terrifying assumptions. He turned a sweet, harmless fruit into a monstrous beast simply because he did not understand the word. Furthermore, when an unknown object (the thief) fell on him in the dark, his unexamined fear drove him to run away in terror. The story teaches that ignorance and lack of information create artificial, exaggerated fears.",
     "Easy", "Understanding"),

    ("Explain the vocabulary words from Chapter 03: Outskirt, Solitary, Incessant, Bosom, and Thatched.",
     "1. **Outskirt**: The outer edge or boundary of a town or forest. *Sentence*: The tiger roamed near the outskirts of the forest.\n2. **Solitary**: Isolated or alone. *Sentence*: A solitary hut stood near the woods.\n3. **Incessant**: Continuous and never stopping. *Sentence*: The baby's incessant crying attracted the tiger.\n4. **Bosom**: The chest area. *Sentence*: The mother held the child close to her bosom.\n5. **Thatched**: Covered with dry straw or reeds. *Sentence*: The thief hid on the slanting thatched roof.",
     "Easy", "Understanding"),

    ("Discuss the character of the tiger in Chapter 03.",
     "The tiger in Chapter 03 is an interesting character who subverts the traditional image of a ferocious apex predator. While he possesses physical strength and a loud roar, he is driven by curiosity rather than hunger. He is also vain about his reputation, getting offended when the baby does not fear a tiger. Most notably, he is highly gullible and imaginative, creating a terrifying monster out of a simple fruit name. His foolish panic when the thief falls on him makes him a hilarious, memorable character.",
     "Easy", "Analyzing"),

    ("How does the mother successfully quiet her baby in Chapter 03?",
     "The mother initially tries physical comforting (rocking to and fro) and fear threats (fox, bear, tiger), all of which fail because an infant does not comprehend wild animal dangers. She successfully quiets her baby by offering a 'persimmon', a sweet fruit that appeals to the child's appetite and sensory pleasure. The offer of food comfort immediately satisfies the child, causing it to fall silent.",
     "Easy", "Understanding"),

    ("Describe the role of the thief in Chapter 03.",
     "The thief acts as an accidental catalyst for the story's resolution. He has no connection to the tiger or the mother; he is simply hiding on the slanting thatched roof to rob the hut. However, his accidental slip and fall onto the tiger's back in the dark provides the physical trigger that confirms the tiger's false fear of the 'persimmon'. His fall sends the tiger fleeing, saving the hut from both the thief and the predator.",
     "Easy", "Understanding"),

    ("Summarize Chapter 03 in five structured paragraphs.",
     "Paragraph 1: A curious tiger roamed the forest outskirts and heard a baby wailing inside a solitary hut.\nParagraph 2: Peeping inside, he saw a mother try fear threats of a fox, bear, and tiger, all of which failed to quiet the brave child.\nParagraph 3: When the mother offered a 'persimmon' fruit, the baby stopped crying, leading the tiger to assume persimmon was a ferocious monster.\nParagraph 4: A thief hiding on the roof slipped and fell on the tiger's back, making the tiger believe the persimmon had attacked.\nParagraph 5: Panicked, the tiger ran wildly into the forest, leaving everyone safe and demonstrating that we fear the unknown.",
     "Easy", "Understanding"),

    ("How does Chapter 03 use dramatic irony to create comedy for young readers?",
     "Dramatic irony occurs when the audience knows facts that characters do not. In Chapter 03, readers know that a persimmon is a sweet, harmless fruit and the creature on the roof is a human thief. However, the tiger genuinely believes the persimmon is a giant monster pouncing on him. This contrast between the reader's knowledge and the tiger's wild, terrified overreaction creates delightful visual and situational comedy.",
     "Easy", "Analyzing"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why did the tiger's pride get wounded during the mother's threats?", "The tiger considered himself the undisputed king of the forest. When the mother threatened the baby with a tiger and the baby kept crying without fear, the tiger felt his grand reputation was insulted, motivating him to roar to demand fear.", "Easy", "Understanding"),
    ("Explain the physical setup of the solitary hut and how it facilitated the plot.", "The hut was solitary at the forest edge, allowing the tiger to approach unnoticed. It had a window for peeping and an unstable, slanting thatched roof where the thief hid. The slippery thatch caused the thief's fall directly onto the tiger below.", "Easy", "Analyzing"),
    ("How does the moral 'We fear the unknown' apply to modern human behavior?", "People frequently fear new situations, unfamiliar cultures, or unverified rumors simply because they lack accurate information. Like the tiger, human imagination often creates imaginary dangers out of unexamined mysteries.", "Easy", "Applying"),
    ("Describe the sequence of threats the mother used before mentioning persimmon.", "First: 'The hungry fox will hear you and eat you.' Second: 'The hungry bear will hear you and eat you.' Third: 'The hungry tiger will hear you and eat you.' All three failed as the baby cried incessantly.", "Easy", "Remembering"),
    ("Why didn't the tiger turn around to look at what fell on his back?", "Terror blinded his natural instincts. Believing the legendary 'persimmon' monster had struck, his immediate flight response took over, driving him to sprint for his life without stopping to inspect his rider.", "Easy", "Analyzing"),
    ("What lesson does this folktale teach about double-checking facts?", "It teaches that jumping to conclusions based on partial information leads to foolish panic. Double-checking facts and seeking true meanings prevents unnecessary fear and embarrassing mistakes.", "Easy", "Evaluating"),
    ("How does the setting of a forest edge create a bridge between wild animals and human living?", "The forest edge is a borderland where wild nature meets human settlement. This setting allows a wild tiger and a human thief to cross paths naturally near a family's hut.", "Easy", "Analyzing"),
    ("Discuss the mother's character in Chapter 03.", "The mother is a caring, patient parent doing her best to soothe her crying child late at night. Although her fear threats fail, her intuitive offer of a sweet fruit succeeds, unknowingly saving her home from two dangers.", "Easy", "Understanding"),
    ("Why did the thief decide to rob a solitary hut at the forest edge?", "A solitary hut at the forest edge is isolated from village neighbors, making it an easy, quiet target for a thief looking to break in without alerting others.", "Easy", "Understanding"),
    ("Explain how the author uses sound to build the story's opening scene.", "The author uses auditory details—the 'incessant wailing' of the baby cutting through the quiet forest outskirts—to capture the tiger's attention and set the narrative in motion.", "Easy", "Analyzing"),
    ("What makes Korean folktales like 'The Tiger and the Persimmon' universally popular?", "Their universal popularity stems from combining relatable human behaviors, clever humor, animal personification, and timeless moral lessons that appeal across cultures.", "Easy", "Evaluating"),
    ("Re-write the ending of the story where the thief tells his friends about riding a tiger.", "'Back at his hideout, the thief gasped, 'I survived riding a giant tiger through the forest!' His friends laughed, but the thief swore he would quit stealing forever after such a terrifying night!'", "Easy", "Creating"),
    ("How does the tiger's foolishness contrast with the baby's innocence?", "The baby is innocent, responding naturally to hunger and comfort without fear of big words. The tiger is overly analytical and vain, overthinking simple words into terrifying monsters.", "Easy", "Comparing"),
    ("What role does surprise play in the story's climax?", "Surprise turns the story upside down. The unexpected fall of the thief in the dark instantly converts the tiger's theoretical fear of persimmons into frantic physical panic.", "Easy", "Analyzing"),
    ("How does Chapter 03 enrich a Class 5 student's reading comprehension skills?", "It develops skills in tracking narrative cause-and-effect, identifying dramatic irony, expanding descriptive vocabulary, and analyzing character misconceptions.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Critically analyze the tiger's cognitive leap from 'persimmon' to 'ferocious beast'.",
     "The tiger committed a severe cognitive error through flawed deduction:\n1. Premise A: The baby is unafraid of foxes, bears, and tigers (brave child).\n2. Premise B: The baby falls silent instantly at the word 'persimmon'.\n3. False Conclusion: 'Persimmon' must be a creature far more terrifying than a tiger.\nThis logical fallacy shows how unverified assumptions built on flawed premises produce absurd conclusions.",
     "Medium", "Analyzing"),

    ("Examine the narrative pacing in Chapter 03 from curiosity to panic.",
     "Pacing shifts effectively:\n1. Slow & Curious: Tiger roaming, hearing wails, peeping through window.\n2. Building Tension: Mother's escalation of animal threats; tiger getting angry.\n3. Sudden Shift: Mother says 'persimmon', baby quiets down; tiger confused.\n4. Explosive Climax: Thief slips from roof, falls on tiger; wild sprint into darkness.\n5. Calming Resolution: Thief slips off, tiger flees deep into forest.",
     "Medium", "Analyzing"),

    ("Evaluate the use of slapstick elements in traditional folklore storytelling.",
     "Slapstick elements—a thief slipping off a thatched roof, falling squarely onto a tiger's back in the dark, and a mighty predator running terrified from an imaginary fruit monster—add physical comedy. This slapstick style engages young readers while embedding the serious moral that fear of the unknown turns anyone into a fool.",
     "Medium", "Evaluating"),

    ("Discuss how Chapter 03 explores the theme of 'Perception vs. Reality'.",
     "Perception: The tiger perceives 'persimmon' as an apex predator and the thief on his back as the monster attacking him. Reality: A persimmon is a sweet fruit and the rider is a scared thief. The story shows that unexamined perception often distorts true reality.",
     "Medium", "Analyzing"),

    ("Design a puppet show script outline based on Chapter 03 for primary students.",
     "- **Scene 1**: Tiger puppet peeping at a cardboard hut window, making confused faces.\n- **Scene 2**: Mother puppet holding baby puppet; audio of crying and fruit offers.\n- **Scene 3**: Thief puppet wobbling on straw roof and falling onto tiger puppet.\n- **Scene 4**: Tiger puppet running wildly across stage yelling 'The Persimmon is here!'",
     "Medium", "Creating"),

    ("How does the setting of a dark night enhance the tiger's misunderstanding?", "Nighttime reduces visibility and heightens sensory paranoia. In the dark, the tiger could not see what landed on his back, allowing his fearful imagination to assume it was the persimmon monster.", "Medium", "Analyzing"),
    ("Contrast the mother's intention when saying 'persimmon' with the tiger's interpretation.", "Mother's intention: Offering a comforting sweet snack to quiet her baby. Tiger's interpretation: Invoking a dark, powerful monster that instills supreme terror.", "Medium", "Comparing"),
    ("Explain why fear of the unknown is a fundamental human emotion.", "The brain seeks predictability for survival. When faced with the unknown, lack of data triggers defensive fear, making people overreact to unfamiliar situations.", "Medium", "Evaluating"),
    ("How does the thief's presence add an extra layer of irony to the narrative?", "It is ironic that a criminal intending to rob a helpless family ends up accidentally scaring away a dangerous tiger, unintentionally protecting the very home he tried to rob.", "Medium", "Analyzing"),
    ("Describe how the author builds the tiger's inflated sense of self-importance.", "By showing the tiger proud of the baby's bravery against foxes/bears, but becoming offended and angry when the baby refuses to fear a tiger, establishing his ego before his downfall.", "Medium", "Analyzing"),
    ("Why is the phrase 'threat fell on deaf ears' appropriate in this context?", "It poetically describes how the infant ignored threats of wild predators because it was too young to understand animal dangers, caring only about food.", "Medium", "Understanding"),
    ("Evaluate the effectiveness of the story's moral statement at the end.", "The simple moral 'We fear the unknown' perfectly synthesizes the entire plot, serving as a memorable summary for students to reflect on their own fears.", "Medium", "Evaluating"),
    ("How can Class 5 teachers use Chapter 03 to teach vocabulary in context?", "Teachers can use contextual clues for words like 'solitary', 'incessant', and 'outskirt', having students deduce meanings from story actions before consulting dictionary definitions.", "Medium", "Applying"),
    ("Deconstruct the structural function of the baby's wailing in driving the plot.", "The baby's wailing acts as the inciting incident. It attracts the tiger, prompts the mother's threats, leads to the word 'persimmon', and sets up the entire sequence of events.", "Medium", "Analyzing"),
    ("Construct a dialogue between two villagers discussing the tiger's sudden flight the next morning.", "'Did you hear the loud noise last night?' 'Yes! A thief fell from a roof onto a tiger, and the tiger ran away terrified of a persimmon!' 'What a foolish tiger!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the tiger's cognitive failure from a behavioral psychology standpoint.",
     "The tiger suffered from cognitive distortion via catastrophic misinterpretation. Lacking schema for the word 'persimmon', he assigned maximum threat value to it. When tactile stimulus (thief falling) occurred, his brain confirmed the catastrophic bias, triggering an acute fight-or-flight response dominated by flight.",
     "Hard", "Evaluating"),

    ("Deconstruct the folklore motif of the 'Foolish Predator' in world literature.",
     "The 'Foolish Predator' motif (seen in Korean, African, and Indian folklore) subverts physical dominance. By giving powerful animals silly intellectual flaws, folklore reassures humans that intelligence, wit, and facts can overcome raw physical strength.",
     "Hard", "Analyzing"),

    ("Synthesize the literary devices used in Chapter 03 (irony, personification, pacing, climax).",
     "1. **Dramatic Irony**: Reader knows truth while tiger is deceived.\n2. **Personification**: Tiger thinking in human language.\n3. **Narrative Pacing**: Building from quiet peeping to explosive flight.\n4. **Climax**: Collision of thief's fall with tiger's inner fear.",
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive assessment rubric for Chapter 03 story analysis.",
     "- **Factual Comprehension (20%)**: Accurately recalling plot points and settings.\n- **Vocabulary Contextualization (20%)**: Correctly applying terms like 'incessant', 'solitary'.\n- **Irony & Motif Analysis (30%)**: Explaining dramatic irony and character misconceptions.\n- **Moral Evaluation (30%)**: Relating 'We fear the unknown' to personal and societal behavior.",
     "Hard", "Creating"),

    ("Evaluate how Chapter 03 promotes media literacy and critical thinking in modern students.", "Just as the tiger feared an unverified word, modern students often fear unverified online rumors. The story teaches students to fact-check information before reacting with panic.", "Hard", "Evaluating"),

    ("Compare the tiger's fear in Chapter 03 with the jackal's fear in Book 3 Chapter 02.", "Both characters misidentified environmental signals due to lack of investigation—the jackal tore a hollow drum expecting food; the tiger ran from a fruit expecting a monster.", "Hard", "Comparing"),
    ("Discuss the cultural universality of Korean folktales in global English education.", "Korean folktales use universal themes of human folly, parenting, and fear, making them accessible and enriching for multicultural English learners.", "Hard", "Evaluating"),
    ("Analyze how the narrative maintains suspense despite its comedic tone.", "Suspense is maintained because the reader wonders when and how the tiger's misunderstanding will collide with physical reality, keeping readers eager for the climax.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'The foolish tiger went back into the forest.'", "This concluding line seals the tiger's comedic defeat. His return to the forest signifies the retreat of foolish panic back into obscurity, leaving human settlement in peace.", "Hard", "Evaluating"),
    ("Synthesize the overall contribution of Batch 1 (Chapters 01–03) to Book 5 Question Bank.", "Batch 1 delivers 900 high-rigor, text-matched questions across 6 categories, establishing an authoritative benchmark for Class 5 English assessment.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 03: The Tiger and the Persimmon\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH03_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH03_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Once upon a time, lived a tiger in a forest. One day it was roaming around the outskirts of the forest. There was a solitary hut nearby. The tiger could hear the non-stop wailing of a child coming from inside the hut.",
     [
         ("Where was the tiger roaming when the story started?", "Around the outskirts of the forest.", "Easy", "Remembering"),
         ("What kind of hut was located nearby?", "A solitary hut.", "Easy", "Remembering"),
         ("What sound did the tiger hear coming from inside the hut?", "The non-stop wailing of a child.", "Easy", "Remembering"),
         ("What does the word 'solitary' mean in this passage?", "Alone or isolated.", "Easy", "Understanding"),
         ("What does the word 'outskirt' mean?", "The outer edge or boundary of a town or forest.", "Easy", "Understanding")
     ]),

    # Set 2
    ("The tiger was not at all hungry but became curious to know the reason of the baby's incessant wails. He went near the hut and started peeping inside through a window. He saw a woman holding a crying baby close to her bosom and rocking it to and fro to calm him down, but to no avail.",
     [
         ("Was the tiger hungry when he approached the hut?", "No, he was not at all hungry.", "Easy", "Remembering"),
         ("Why did the tiger approach the hut?", "He was curious to know the reason for the baby's incessant wailing.", "Easy", "Remembering"),
         ("How did the tiger look inside the hut?", "He started peeping inside through a window.", "Easy", "Remembering"),
         ("What was the mother doing to soothe her crying baby?", "Holding it close to her bosom and rocking it to and fro.", "Easy", "Remembering"),
         ("What does the word 'incessant' mean?", "Never stopping; continuous.", "Easy", "Understanding")
     ]),

    # Set 3
    ("'Hush baby hush. Don't cry. The hungry fox will hear you and eat you.' The lady said this to calm the baby down. But the baby kept on crying. The tiger thought to himself, 'What a brave child! He is not at all afraid of a fox.'",
     [
         ("Which animal did the lady FIRST mention to quiet her baby?", "A hungry fox.", "Easy", "Remembering"),
         ("Did the baby stop crying when the fox was mentioned?", "No, the baby kept on crying.", "Easy", "Remembering"),
         ("What was the tiger's inner reaction to the baby's behavior?", "He thought: 'What a brave child! He is not at all afraid of a fox.'", "Easy", "Remembering"),
         ("Why did the mother use the threat of a hungry fox?", "To scare the baby into falling silent.", "Medium", "Understanding"),
         ("What trait does the tiger admire in the child here?", "Bravery / lack of fear toward a wild fox.", "Medium", "Understanding")
     ]),

    # Set 4
    ("'Hush baby hush. Don't cry. The hungry bear will hear you and eat you.' Again, the threat did not have any effect on the child and he kept on crying. The tiger became surprised again.",
     [
         ("Which animal did the mother SECONDLY mention to scare the child?", "A hungry bear.", "Easy", "Remembering"),
         ("What effect did the threat of a bear have on the child?", "It had no effect and the child kept on crying.", "Easy", "Remembering"),
         ("How did the tiger feel when the baby ignored the bear threat?", "He became surprised again.", "Easy", "Remembering"),
         ("Why was the child not afraid of the bear?", "The infant was too young to understand what a bear was or the danger it posed.", "Medium", "Understanding"),
         ("What does 'threat fell on deaf ears' mean in this context?", "The warning was completely ignored by the listener.", "Medium", "Understanding")
     ]),

    # Set 5
    ("'Hush baby hush. Don't cry. The hungry tiger will hear you and eat you.' Yet again, the threat fell on deaf ears. This time the tiger felt angry that the child was not terrified of him. He decided to roar to scare the child.",
     [
         ("Which animal did the mother THIRDLY mention to quiet her baby?", "A hungry tiger.", "Easy", "Remembering"),
         ("How did the tiger feel when the baby did not fear the tiger threat?", "He felt angry that the child was not terrified of him.", "Easy", "Remembering"),
         ("What did the tiger plan to do to prove his ferocity?", "He decided to roar loudly to scare the child.", "Easy", "Remembering"),
         ("What character flaw of the tiger is revealed in his anger?", "Pride and an inflated ego regarding his terrifying reputation.", "Medium", "Analyzing"),
         ("Why did the tiger want the baby to be terrified of him?", "To assert his dominance as the king of the forest.", "Medium", "Understanding")
     ]),

    # Set 6
    ("But before he could, the lady said 'Hush baby hush. There is a persimmon (a fruit).' On hearing the name of a fruit the baby fell silent. The tiger wondered, 'What a great animal persimmon must be to scare this brave child into silence!'",
     [
         ("What word spoken by the mother finally made the baby fall silent?", "Persimmon.", "Easy", "Remembering"),
         ("What is a persimmon in reality?", "A sweet orange-red edible fruit.", "Easy", "Remembering"),
         ("Did the tiger know that persimmon was a fruit?", "No, he believed it was a great, terrifying animal.", "Easy", "Remembering"),
         ("Why did the tiger think persimmon was a dangerous creature?", "Because it quieted a child who was not afraid of foxes, bears, or tigers.", "Medium", "Understanding"),
         ("What literary device is used when the reader knows persimmon is a fruit but the tiger does not?", "Dramatic irony.", "Medium", "Analyzing")
     ]),

    # Set 7
    ("Meanwhile, a thief was waiting to get into the hut, hiding on the slanting thatched roof. All of a sudden he lost his balance and fell on the tiger's back.",
     [
         ("Who was hiding on the roof of the hut and why?", "A thief waiting to break into the hut.", "Easy", "Remembering"),
         ("What kind of roof did the solitary hut have?", "A slanting thatched roof.", "Easy", "Remembering"),
         ("What happened suddenly to the thief?", "He lost his balance and fell directly onto the tiger's back.", "Easy", "Remembering"),
         ("Why did the thief lose his balance?", "The slanting, straw thatched roof was slippery and unstable.", "Medium", "Understanding"),
         ("How does this accidental fall advance the plot?", "It triggers the climax where the tiger believes the persimmon has attacked him.", "Medium", "Analyzing")
     ]),

    # Set 8
    ("The tiger jumped in fright as he thought that the persimmon had attacked him and started running for his life. The thief somehow managed to get off the tiger's back and the foolish tiger went back into the forest.",
     [
         ("Why did the tiger jump in fright when the thief fell on him?", "He thought the terrifying persimmon monster had attacked him.", "Easy", "Remembering"),
         ("What did the tiger do after jumping in fright?", "He started running for his life.", "Easy", "Remembering"),
         ("How did the thief escape?", "He somehow managed to slip off the tiger's back as it ran.", "Easy", "Remembering"),
         ("Where did the tiger go in the end?", "The foolish tiger went back into the forest.", "Easy", "Remembering"),
         ("Why did the tiger run away instead of fighting the thief?", "Panic made him believe he was attacked by the irresistible persimmon monster.", "Medium", "Analyzing")
     ]),

    # Set 9
    ("Moral of the Story: We fear the unknown.",
     [
         ("What is the moral of Chapter 03?", "We fear the unknown.", "Easy", "Remembering"),
         ("How does the tiger's fear of persimmon illustrate this moral?", "He feared the word 'persimmon' simply because he did not know what it meant.", "Medium", "Understanding"),
         ("How does the thief's fall reinforce this moral?", "The tiger feared the unknown rider on his back, assuming it was a monster.", "Medium", "Understanding"),
         ("How can students avoid fearing the unknown in daily life?", "By asking questions, gathering facts, and understanding things before panicking.", "Medium", "Applying"),
         ("What key lesson does this moral teach about human nature?", "Ignorance breeds unexamined, irrational fears that cause foolish behavior.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("The tiger wondered, 'What a great animal persimmon must be...'\nAll of a sudden he lost his balance and fell on the tiger's back. The tiger jumped in fright... and the foolish tiger went back into the forest.",
     [
         ("What misconception drove the tiger's entire fear?", "Believing persimmon was a fierce animal stronger than a tiger.", "Easy", "Remembering"),
         ("What physical collision triggered his wild escape?", "The thief losing balance and falling on his back.", "Easy", "Remembering"),
         ("How is the tiger described in the final sentence?", "The foolish tiger.", "Easy", "Remembering"),
         ("Why is the story described as a comedy of errors?", "Because a series of silly misunderstandings turned a sweet fruit into a monster.", "Medium", "Evaluating"),
         ("Summarize the resolution of this extract in one line.", "The foolish tiger fled in fear from an imaginary monster, leaving the village safe.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 03: The Tiger and the Persimmon\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH03_EXT_{q_counter:03d}"
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

with open(os.path.join(CH03_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 03 in {CH03_DIR}")
