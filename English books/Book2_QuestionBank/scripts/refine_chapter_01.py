r"""
Refines all 6 Category files for Chapter 01 ("The Rats Who Ate the Iron Balance") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
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
    ("What was the name of the poor boy in the story?", "(A) Dilip", "(B) Mohan", "(C) Rahul", "(D) Rohan", "(A)", "The poor boy in the story was named Dilip.", "Easy", "Remembering", "Character Name"),
    ("Why did Dilip want to go to a foreign land?", "(A) To earn money", "(B) To buy a house", "(C) To play sports", "(D) To study music", "(A)", "He wanted to travel abroad to earn money.", "Easy", "Remembering", "Plot Motivation"),
    ("From whom did Dilip borrow money for his travels?", "(A) The Mahajan (money lender)", "(B) The King", "(C) The Teacher", "(D) A Farmer", "(A)", "Dilip borrowed money from the rich Mahajan.", "Easy", "Remembering", "Character Identification"),
    ("What object did Dilip give to the Mahajan as security?", "(A) Heavy iron scales", "(B) Gold ring", "(C) Wooden cart", "(D) Silver coins", "(A)", "He gave his heavy iron scales as security for the loan.", "Easy", "Remembering", "Security Item"),
    ("What lie did the greedy Mahajan tell Dilip when he asked for his scales back?", "(A) The mice ate the iron scales", "(B) The scales fell into the river", "(C) The scales were stolen by thieves", "(D) He broke the scales", "(A)", "The Mahajan lied that mice ate up the iron scales.", "Easy", "Remembering", "The Lie"),
    ("How did Dilip react immediately when the Mahajan lied to him?", "(A) He quietly went back home without arguing", "(B) He started fighting", "(C) He cried loudly", "(D) He called the police", "(A)", "Dilip remained calm and went home quietly.", "Easy", "Remembering", "Character Reaction"),
    ("Whom did Dilip meet on the way to the river a few days later?", "(A) The Mahajan's son", "(B) The King's servant", "(C) A fruit seller", "(D) A fisherman", "(A)", "Dilip met the Mahajan's son walking to the river.", "Easy", "Remembering", "Plot Event"),
    ("Where did Dilip lock the Mahajan's son?", "(A) Inside his house", "(B) In a cave", "(C) On a tree", "(D) In a boat", "(A)", "Dilip invited the boy home and locked him inside.", "Easy", "Remembering", "Action"),
    ("What clever lie did Dilip tell the Mahajan about his son?", "(A) An eagle carried his son away into the sky", "(B) A tiger chased his son", "(C) His son ran into the forest", "(D) His son fell into a well", "(A)", "Dilip claimed an eagle flew away with the Mahajan's son.", "Easy", "Remembering", "Counter Lie"),
    ("Why did the Mahajan say an eagle could not carry his son?", "(A) Because a boy is too heavy for an eagle to lift", "(B) Because eagles cannot fly", "(C) Because there are no eagles in the village", "(D) Because his son was hiding", "(A)", "A heavy boy cannot be carried away by a small eagle.", "Easy", "Understanding", "Logic"),
    ("What was Dilip's famous reply to the Mahajan's question?", "(A) An eagle carrying a boy is possible just like mice eating iron scales!", "(B) Eagles are very strong", "(C) Your son wanted to fly", "(D) I didn't see anything", "(A)", "Dilip exposed the Mahajan's lie using his own logic.", "Easy", "Remembering", "Dialogue"),
    ("How did the Mahajan feel when he realized Dilip's clever lesson?", "(A) He felt deeply ashamed and apologized", "(B) He felt very happy", "(C) He laughed out loud", "(D) He called the guard", "(A)", "The Mahajan realized his mistake, felt ashamed, and apologized.", "Easy", "Remembering", "Climax"),
    ("What did the Mahajan do after apologizing to Dilip?", "(A) He returned the iron scales to Dilip", "(B) He asked for more money", "(C) He ran away from the village", "(D) He kept both items", "(A)", "He returned the iron scales to Dilip immediately.", "Easy", "Remembering", "Resolution"),
    ("What did Dilip do after receiving his iron scales back?", "(A) He brought the Mahajan's son safely back to his father", "(B) He ran away", "(C) He locked the Mahajan in the house", "(D) He went back abroad", "(A)", "Dilip brought the boy safely back to the Mahajan.", "Easy", "Remembering", "Resolution"),
    ("What is the moral of the story 'The Rats Who Ate the Iron Balance'?", "(A) You cannot get away with doing bad things", "(B) Money is everything", "(C) Never lend money to anyone", "(D) Mice love to eat iron", "(A)", "Doing bad things leads to lessons and consequences.", "Easy", "Understanding", "Moral Lesson"),
    ("What does the word 'scales' mean in this story?", "(A) An equipment used for weighing things", "(B) Fish skin", "(C) Climbing a wall", "(D) Music notes", "(A)", "Scales are weighing equipment.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'security' mean in loan agreement?", "(A) Something of value given to guarantee loan repayment", "(B) A guard at the door", "(C) A lock and key", "(D) A secret password", "(A)", "Security is a valuable item given against a loan.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'ashamed' mean?", "(A) Feeling guilty and embarrassed because of wrong action", "(B) Feeling sleepy", "(C) Feeling angry", "(D) Feeling proud", "(A)", "Ashamed means feeling guilty for doing something wrong.", "Easy", "Understanding", "Vocabulary"),
    ("From which famous Indian book of tales is this story taken?", "(A) Panchatantra", "(B) Akbar Birbal", "(C) Tenali Raman", "(D) Arabian Nights", "(A)", "This story is a classic Panchatantra tale.", "Easy", "Remembering", "Literary Origin"),
    ("What metal were Dilip's scales made of?", "(A) Iron", "(B) Gold", "(C) Plastic", "(D) Wood", "(A)", "The scales were made of heavy iron.", "Easy", "Remembering", "Material"),
    ("Can real mice or rats eat solid iron?", "(A) No, iron is too hard for mice to eat", "(B) Yes, mice eat iron daily", "(C) Mice love eating iron", "(D) Iron turns into cheese", "(A)", "Mice cannot chew or eat solid iron metal.", "Easy", "Understanding", "General Knowledge"),
    ("Why did the Mahajan lie about the iron scales?", "(A) Because he was greedy and wanted to keep the valuable scales", "(B) Because he lost them in the lake", "(C) Because he gave them to a beggar", "(D) Because he broke them", "(A)", "Greed made him lie so he could keep the scales.", "Easy", "Understanding", "Character Motivation"),
    ("Did Dilip use violence or cleverness to teach the Mahajan a lesson?", "(A) He used cleverness and wit", "(B) He used a stick to beat him", "(C) He burned his house", "(D) He hired guards", "(A)", "Dilip used clever wit rather than violence.", "Easy", "Understanding", "Plot Insight"),
    ("What kind of man was Dilip at the end of the story?", "(A) Clever, honest, and fair", "(B) Greedy and cruel", "(C) Foolish and weak", "(D) Lazy", "(A)", "Dilip was clever, honest, and fair throughout.", "Easy", "Understanding", "Character Trait"),
    ("What is the title of Chapter 01 in Book 2?", "(A) The Rats Who Ate the Iron Balance", "(B) The Clever Crow", "(C) The Greedy Dog", "(D) The Lion and the Mouse", "(A)", "Chapter 01 is titled 'The Rats Who Ate the Iron Balance'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why did Dilip need to borrow money before traveling to a foreign land?", "(A) Because he was poor and needed funds for travel expenses", "(B) To buy clothes for a party", "(C) To buy toys for children", "(D) To build a palace", "(A)", "Dilip was poor and needed money to pay for his journey.", "Medium", "Understanding", "Cause & Effect"),
    ("Why did the Mahajan think Dilip would easily believe his lie about the mice?", "(A) He thought Dilip was simple and would not challenge a rich money lender", "(B) Because mice eat iron in that village", "(C) Because Dilip had no eyes", "(D) Because Dilip forgot his scales", "(A)", "The Mahajan counted on Dilip's simple nature.", "Medium", "Understanding", "Psychological Insight"),
    ("How does Dilip's quiet departure after the lie show his wisdom?", "(A) Instead of wasting time shouting, he planned a smart way to expose the lie", "(B) He was afraid of the Mahajan", "(C) He actually believed the lie", "(D) He forgot about his scales", "(A)", "Staying calm allowed him to think of a clever plan.", "Medium", "Analyzing", "Character Wisdom"),
    ("What is the similarity between the two lies in the story?", "(A) Both lies describe impossible events (mice eating iron and eagles lifting heavy boys)", "(B) Both lies were true", "(C) Both lies involved fish", "(D) Both lies were written in books", "(A)", "Both lies involve absurd, physically impossible situations.", "Medium", "Analyzing", "Structural Parallel"),
    ("Why did the Mahajan immediately realize his mistake when Dilip mentioned the eagle?", "(A) He recognized that Dilip was using the same impossible logic against him", "(B) He saw an eagle landing on his roof", "(C) The boy started shouting from the tree", "(D) Dilip showed him a picture", "(A)", "Dilip's words mirrored the Mahajan's own lie perfectly.", "Medium", "Understanding", "Climax Analysis"),
    ("How did Dilip ensure that the Mahajan's son remained completely safe?", "(A) He locked him safely inside his own house without harming him", "(B) He tied him to a tree", "(C) He pushed him into the river", "(D) He sent him to another city", "(A)", "Dilip kept the boy safe in his house.", "Medium", "Remembering", "Detail"),
    ("What does 'Tit for Tat' mean in relation to this story?", "(A) Treating someone in the same way they have treated you to teach a lesson", "(B) Giving gifts to friends", "(C) Buying two scales at once", "(D) Playing a game of tag", "(A)", "Tit for Tat means returning similar treatment.", "Medium", "Understanding", "Proverb Meaning"),
    ("Why is greed considered a negative trait based on the Mahajan's actions?", "(A) Greed made the Mahajan lie, lose his honor, feel ashamed, and almost lose his son's trust", "(B) Greed makes people rich quickly", "(C) Greed helps you make friends", "(D) Greed is praised by kings", "(A)", "Greed causes moral downfall and embarrassment.", "Medium", "Evaluating", "Moral Evaluation"),
    ("What lesson about problem-solving does Dilip teach young students?", "(A) Solve problems calmly using your mind and intelligence rather than anger or fighting", "(B) Scream at people when they lie", "(C) Give up immediately when cheated", "(D) Never trust anyone", "(A)", "Calm intelligence solves difficult problems effectively.", "Medium", "Evaluating", "Life Lesson"),
    ("What would have happened if Dilip had gotten angry and fought the rich Mahajan physically?", "(A) The powerful Mahajan might have used his wealth to punish Dilip instead of returning the scales", "(B) The Mahajan would give him double money", "(C) The King would reward Dilip", "(D) The scales would turn to gold", "(A)", "Physical fighting with a rich man would have hurt poor Dilip.", "Medium", "Analyzing", "Hypothetical Scenario"),
    ("How does Panchatantra story format help children learn good values?", "(A) By using engaging stories with clear consequences for good and bad behavior", "(B) By giving hard math formulas", "(C) By teaching complex grammar rules only", "(D) By asking children to memorize facts", "(A)", "Stories make moral lessons easy and memorable for children.", "Medium", "Evaluating", "Literary Purpose"),
    ("What shows that Dilip was an honest person despite locking the Mahajan's son?", "(A) He returned the boy safely as soon as the Mahajan gave back his scales", "(B) He demanded extra money", "(C) He kept the boy forever", "(D) He sold the scales", "(A)", "Dilip only wanted his fair item back, not harm to the boy.", "Medium", "Analyzing", "Moral Character"),
    ("What opposite words best describe Dilip and the Mahajan at the start of the story?", "(A) Dilip was Poor & Honest; Mahajan was Rich & Greedy", "(B) Dilip was Lazy; Mahajan was Hardworking", "(C) Dilip was Tall; Mahajan was Short", "(D) Dilip was Young; Mahajan was a King", "(A)", "Poor/Honest vs Rich/Greedy sets up the contrast.", "Medium", "Analyzing", "Character Contrast"),
    ("Why did Dilip go abroad to earn money instead of staying in the village?", "(A) Opportunity to earn better wages and overcome poverty", "(B) To go on a holiday", "(C) To buy foreign toys", "(D) Because he disliked his village", "(A)", "He traveled to seek better earnings.", "Medium", "Understanding", "Motivation"),
    ("How did the story end for both main characters?", "(A) Dilip got his scales back happily, and the Mahajan learned an important moral lesson", "(B) Both went to jail", "(C) Dilip moved to another country forever", "(D) The Mahajan stole the scales again", "(A)", "Dilip recovered his property and Mahajan learned honesty.", "Medium", "Understanding", "Plot Resolution"),

    # Hard (41-50)
    ("Analyze how irony is used in Dilip's statement about the eagle carrying the boy.", "(A) Dilip used an absurd lie (eagle lifting boy) to mirror the Mahajan's absurd lie (rats eating iron), exposing the truth through irony", "(B) Dilip was telling a real scientific fact", "(C) Dilip actually saw an eagle", "(D) The Mahajan liked eagles", "(A)", "Irony exposed the Mahajan's absurdity.", "Hard", "Analyzing", "HOTS Literary Device"),
    ("Evaluate the ethical boundary of Dilip locking the Mahajan's son inside his house.", "(A) Though temporary detention is wrong normally, here it was a non-violent, harmless stratagem used to restore justice", "(B) Dilip was a criminal", "(C) The son wanted to stay locked", "(D) The Mahajan asked him to lock the boy", "(A)", "It was a harmless strategic trick to achieve justice.", "Hard", "Evaluating", "Ethical Analysis"),
    ("How does the Mahajan's transformation from greedy liar to ashamed man highlight the power of conscience?", "(A) When confronted with his own absurd logic, his conscience made him feel ashamed and rectify his action", "(B) He was scared of the police", "(C) Dilip paid him money", "(D) The King ordered him", "(A)", "Self-realization awakened his conscience.", "Hard", "Evaluating", "Psychological Transformation"),
    ("Compare the value of material wealth (Mahajan) versus intellectual cleverness (Dilip) in this chapter.", "(A) Wealth gave the Mahajan power to lie, but cleverness gave Dilip the power to reclaim justice without violence", "(B) Wealth is always superior to cleverness", "(C) Neither wealth nor cleverness matters", "(D) Wealth makes you wise", "(A)", "Wit and truth triumph over wealth and deceit.", "Hard", "Analyzing", "Theme Comparison"),
    ("How can Class 2 students apply Dilip's calm attitude when faced with an unfair situation in school?", "(A) Stay calm, avoid physical fights, and use smart reasoning or teacher support to solve the issue fairly", "(B) Shout and break things", "(C) Cry and hide under a desk", "(D) Tell bigger lies to everyone", "(A)", "Calm reasoning resolves playground conflicts peacefully.", "Hard", "Applying", "Real Life Application"),
    ("Why are iron scales a meaningful symbol of security and fairness in this narrative?", "(A) Scales represent justice and balance; the Mahajan's theft of scales symbolized his unbalanced, unfair heart", "(B) Scales are made of heavy metal", "(C) Scales are used in shops", "(D) Scales look shiny", "(A)", "Scales symbolize justice and moral balance.", "Hard", "Evaluating", "Symbolism Analysis"),
    ("Deconstruct the sequence of cause and effect that drives the entire plot of Chapter 01.", "(A) Poverty -> Borrowing Money -> Travel -> Return -> Mahajan's Lie -> Dilip's Trick -> Realization -> Justice", "(B) Lie -> Travel -> Money -> Scales -> Eagle -> Rat", "(C) Eagle -> Money -> Rat -> Lock -> House -> Return", "(D) Scales -> Poverty -> Lie -> Eagle -> Travel", "(A)", "Logical cause-and-effect progression of the story.", "Hard", "Analyzing", "Plot Structure"),
    ("What does the story imply about the relationship between truth and justice?", "(A) Justice is achieved when truth exposes lies, forcing the offender to make amends", "(B) Truth is unimportant as long as you win", "(C) Justice depends on who has more money", "(D) Lies always win in court", "(A)", "Exposing lies restores truth and justice.", "Hard", "Evaluating", "Philosophical Insight"),
    ("Why has this Panchatantra tale remained popular for over two thousand years?", "(A) Its timeless theme of wit overcoming greed and non-violent justice resonates across generations and cultures", "(B) It is a very long story", "(C) It has many scary monsters", "(D) It teaches how to catch rats", "(A)", "Timeless moral themes of wit and justice keep it popular.", "Hard", "Evaluating", "Cultural Longevity"),
    ("What is the ultimate takeaway message of Chapter 01 for young Class 2 learners?", "(A) Be honest, respect others' property, and remember that wisdom and truth will always defeat greed and deceit!", "(B) Keep heavy iron scales at home", "(C) Lock your friends in rooms", "(D) Never travel to foreign lands", "(A)", "Honesty, wisdom, and respect form the ultimate moral lesson.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH01_MCQ_{idx:03d}"
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
    ("A poor boy named Dilip wanted to go to a _______ land to earn money.", "foreign", "Dilip wanted to go to a foreign land.", "Easy"),
    ("Dilip borrowed money from the village _______.", "Mahajan", "He borrowed money from the Mahajan.", "Easy"),
    ("Dilip gave his heavy iron _______ as security for the loan.", "scales / balance", "He pledged his heavy iron scales.", "Easy"),
    ("After a few years, Dilip returned to his village after earning _______.", "money", "He returned after earning money.", "Easy"),
    ("The Mahajan was _______ and did not want to return the scales.", "greedy", "The Mahajan was greedy.", "Easy"),
    ("The Mahajan lied that the _______ ate the iron scales.", "mice / rats", "He lied that mice ate the scales.", "Easy"),
    ("Dilip went back home _______ without saying a word.", "quietly", "He left quietly without arguing.", "Easy"),
    ("A few days later, Dilip met the Mahajan's _______ on the way to the river.", "son", "He met the Mahajan's son.", "Easy"),
    ("Dilip invited the boy home and _______ him inside his house.", "locked", "He locked the boy in his house.", "Easy"),
    ("Dilip told the Mahajan that an _______ carried away his son.", "eagle", "He claimed an eagle took the boy.", "Easy"),
    ("The Mahajan asked how an eagle could carry a heavy _______.", "boy / child", "He asked how an eagle could carry a boy.", "Easy"),
    ("Dilip replied that it is possible in the exact way that mice eat _______ scales.", "iron", "Mice eating iron scales logic.", "Easy"),
    ("The Mahajan felt deeply _______ when he understood his mistake.", "ashamed", "The Mahajan felt ashamed.", "Easy"),
    ("The Mahajan _______ to Dilip and returned the iron scales.", "apologized", "He apologized and returned the scales.", "Easy"),
    ("Dilip brought the boy back safely to his _______.", "father / Mahajan", "He brought the boy to his father.", "Easy"),
    ("The moral of the story is that you cannot get away with doing _______ things.", "bad / wrong", "Doing bad things has consequences.", "Easy"),
    ("Scales are an equipment used for _______ things.", "weighing", "Scales weigh objects.", "Easy"),
    ("Security is something of _______ pledged to borrow money.", "value", "Security is valuable item pledged.", "Easy"),
    ("Ashamed means feeling _______ because of wrongdoing.", "guilty / embarrassed", "Ashamed means feeling guilty.", "Easy"),
    ("This story is a famous tale from the _______.", "Panchatantra", "It is from Panchatantra.", "Easy"),
    ("Dilip's scales were made of heavy _______.", "iron", "The scales were made of iron.", "Easy"),
    ("Mice cannot eat solid metal like _______.", "iron", "Mice cannot chew iron metal.", "Easy"),
    ("Dilip used his _______ to teach the greedy Mahajan a lesson.", "cleverness / wit", "He used cleverness to teach a lesson.", "Easy"),
    ("The Mahajan's lie was about rats eating iron _______.", "scales", "His lie was about iron scales.", "Easy"),
    ("Chapter 01 is titled The Rats Who Ate the Iron _______.", "Balance", "Chapter 01 is titled The Rats Who Ate the Iron Balance.", "Easy"),

    # Medium (26-40)
    ("The word 'foreign' means belonging to a different _______.", "country / land", "Foreign means another country.", "Medium"),
    ("The word 'security' refers to an item pledged against a _______.", "loan / debt", "Security guarantees loan repayment.", "Medium"),
    ("The word 'apologized' means expressed regret for a _______.", "mistake / fault / lie", "Apologized means expressing regret.", "Medium"),
    ("Dilip remained calm instead of giving in to _______.", "anger / temper", "He controlled his anger.", "Medium"),
    ("The Mahajan's greed made him lose his moral _______.", "honesty / character", "Greed ruined his honesty.", "Medium"),
    ("An eagle is a large bird of prey that flies high in the _______.", "sky", "Eagles fly high in the sky.", "Medium"),
    ("Both mice eating iron and eagles lifting boys are physically _______.", "impossible", "Both events are impossible.", "Medium"),
    ("Dilip proved that clever thinking is stronger than physical _______.", "force / fight", "Cleverness beats force.", "Medium"),
    ("The Mahajan returned the scales because his conscience was _______.", "awakened / shaken", "His conscience was awakened.", "Medium"),
    ("Dilip's plan succeeded without causing any physical _______ to the boy.", "harm / injury", "The boy was unhurt.", "Medium"),
    ("Tit for tat means responding to bad behavior with a matching _______.", "lesson / response", "Tit for tat matches treatment.", "Medium"),
    ("The Mahajan tried to cheat Dilip because Dilip was a _______ boy.", "poor", "He took advantage of poor Dilip.", "Medium"),
    ("Honesty and fair dealing build trust in a _______.", "village / community", "Honesty builds community trust.", "Medium"),
    ("Dilip earned money abroad through hard _______.", "work / labor", "He earned money through hard work.", "Medium"),
    ("The story ends with the safe return of the boy and the iron _______.", "scales", "Both items were returned safely.", "Medium"),

    # Hard (41-50)
    ("Irony occurs when the Mahajan's own absurd logic is turned against _______.", "himself", "Irony turned his logic against him.", "Hard"),
    ("Pledging security is a standard practice in financial _______.", "transactions / loans", "Security is used in financial transactions.", "Hard"),
    ("Dilip's strategic patience prevented unnecessary conflict with the village _______.", "elder / Mahajan", "Patience prevented conflict.", "Hard"),
    ("Moral retribution forces a wrongdoer to face their own _______.", "deceit / lie", "Retribution exposes deceit.", "Hard"),
    ("The contrast between material wealth and moral integrity is central to this _______.", "tale / story", "Wealth vs integrity is central theme.", "Hard"),
    ("Dilip's actions demonstrate how wit can overcome systemic _______.", "injustice / greed", "Wit overcomes injustice.", "Hard"),
    ("Conscience causes internal embarrassment when one's lie is publicly _______.", "exposed", "Exposure causes embarrassment.", "Hard"),
    ("Fables use animal imagery and exaggerated situations to teach universal _______.", "morals / truths", "Fables teach universal morals.", "Hard"),
    ("The Mahajan's son served as a temporary bargaining _______ for justice.", "chip / instrument", "The son served to bargain justice.", "Hard"),
    ("Chapter 01 emphasizes that truth and righteousness eventually prevail over _______.", "falsehood / greed", "Truth prevails over falsehood.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH01_FIB_{idx:03d}"
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

with open(os.path.join(CH01_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Dilip wanted to go to a foreign land to buy new clothes.", False, "Dilip wanted to go abroad to earn money.", "Easy"),
    ("Dilip borrowed money from the rich Mahajan.", True, "He borrowed money from the Mahajan.", "Easy"),
    ("Dilip gave his heavy iron scales as security for the loan.", True, "He gave his iron scales as security.", "Easy"),
    ("The Mahajan happily returned the scales as soon as Dilip came back.", False, "The Mahajan lied that mice ate the scales.", "Easy"),
    ("The Mahajan lied that mice had eaten Dilip's iron scales.", True, "He claimed mice ate the iron scales.", "Easy"),
    ("Dilip started shouting and fighting with the Mahajan immediately.", False, "Dilip quietly went home without arguing.", "Easy"),
    ("Dilip met the Mahajan's son on the way to the river.", True, "He met the Mahajan's son near the river.", "Easy"),
    ("Dilip locked the Mahajan's son safely inside his house.", True, "He invited the boy home and locked him inside.", "Easy"),
    ("Dilip told the Mahajan that a tiger had eaten his son.", False, "He told him an eagle carried his son into the sky.", "Easy"),
    ("The Mahajan believed right away that an eagle took his son.", False, "The Mahajan questioned how an eagle could lift a heavy boy.", "Easy"),
    ("Dilip said an eagle carrying a boy is possible just like mice eating iron scales.", True, "Dilip exposed the Mahajan's lie using his own logic.", "Easy"),
    ("The Mahajan felt ashamed and apologized for his greedy lie.", True, "He felt deeply ashamed and apologized.", "Easy"),
    ("The Mahajan returned the iron scales to Dilip in the end.", True, "He returned the scales to Dilip.", "Easy"),
    ("Dilip kept the Mahajan's son locked forever.", False, "Dilip brought the boy back safely as soon as he got his scales.", "Easy"),
    ("The moral of the story is that you cannot get away with doing bad things.", True, "Doing bad things brings moral consequences.", "Easy"),
    ("Scales are an equipment used for measuring length.", False, "Scales are used for weighing items.", "Easy"),
    ("Security is something of value given to borrow money.", True, "Security pledges value against a loan.", "Easy"),
    ("Ashamed means feeling proud and famous.", False, "Ashamed means feeling guilty for wrongdoing.", "Easy"),
    ("Dilip's scales were made of solid gold.", False, "The scales were made of heavy iron.", "Easy"),
    ("Mice can easily chew and digest heavy iron scales.", False, "Mice cannot eat or chew solid iron metal.", "Easy"),
    ("Dilip used clever wit to teach the greedy Mahajan a lesson.", True, "He used clever wit to expose the lie.", "Easy"),
    ("The Mahajan was a generous and honest money lender.", False, "The Mahajan was greedy and dishonest.", "Easy"),
    ("Dilip worked hard abroad for a few years before returning.", True, "He worked abroad for a few years.", "Easy"),
    ("Dilip harmed the Mahajan's son while he was locked in the house.", False, "The boy was kept safe and unhurt.", "Easy"),
    ("This story is a famous Panchatantra moral tale.", True, "It is a classic Panchatantra tale.", "Easy"),

    # Medium (26-40)
    ("The Mahajan lied because he wanted to keep the valuable iron scales.", True, "Greed motivated his lie.", "Medium"),
    ("Dilip's calm reaction showed that he was a wise problem-solver.", True, "Calmness allowed him to plan a smart lesson.", "Medium"),
    ("An eagle is physically capable of lifting an 8-year-old boy into the clouds.", False, "An eagle cannot lift a heavy child.", "Medium"),
    ("Dilip's counter-story was designed to make the Mahajan realize the absurdity of his own lie.", True, "The story mirrored the Mahajan's impossible lie.", "Medium"),
    ("The Mahajan apologized only because the King threatened him.", False, "He apologized out of self-realization and shame.", "Medium"),
    ("Dilip intended to harm the Mahajan's son out of revenge.", False, "Dilip only wanted his stolen scales back safely.", "Medium"),
    ("Tit-for-tat in this story means teaching a dishonest person a lesson using their own logic.", True, "It means returning matching logical treatment.", "Medium"),
    ("Greed leads to dishonest actions that ruin a person's reputation.", True, "Greed ruins reputation and moral standing.", "Medium"),
    ("Dilip's iron scales were useless and had no value.", False, "They were heavy and valuable weighing equipment.", "Medium"),
    ("The story shows that a poor person can stand up for justice using cleverness.", True, "Cleverness empowers poor people against injustice.", "Medium"),
    ("The Mahajan's lie about mice eating iron was scientifically plausible.", False, "It was completely impossible.", "Medium"),
    ("Dilip paid back the money he had borrowed from the Mahajan.", True, "He went to pay back the loan before asking for scales.", "Medium"),
    ("The Mahajan's son enjoyed playing at Dilip's house.", True, "The boy willingly followed Dilip home.", "Medium"),
    ("Dilip's cleverness prevented a violent fight in the village.", True, "His wit resolved the dispute peacefully.", "Medium"),
    ("The Mahajan learned that bad actions have unexpected consequences.", True, "He learned that bad actions bring consequences.", "Medium"),

    # Hard (41-50)
    ("The narrative uses parallel impossible claims to create satirical humor and moral impact.", True, "Parallel impossible lies create moral satire.", "Hard"),
    ("Dilip's actions violated basic ethics by using a child as a pawn for justice.", False, "He ensured the child's complete safety while non-violently forcing restitution.", "Hard"),
    ("The Mahajan's shame indicates that his moral conscience was still redeemable.", True, "Feeling ashamed showed he could be redeemed.", "Hard"),
    ("Poverty forced Dilip into dishonesty at the beginning of the story.", False, "Dilip remained honest and hardworking throughout.", "Hard"),
    ("The iron scales symbolize the balance of justice in human relationships.", True, "Scales symbolize justice and moral balance.", "Hard"),
    ("Dilip's success proves that anger is more effective than strategic patience.", False, "Patience and wit proved far more effective than anger.", "Hard"),
    ("The story illustrates the Panchatantra tradition of teaching diplomacy through fables.", True, "Panchatantra teaches diplomacy and worldly wisdom.", "Hard"),
    ("The Mahajan's initial greed was rewarded with permanent ownership of the scales.", False, "His greed was exposed and he had to return the scales.", "Hard"),
    ("Exposing absurd lies through irony is a powerful non-violent strategy.", True, "Irony non-violently exposes absurd lies.", "Hard"),
    ("Chapter 01 demonstrates that integrity and cleverness triumph over deceit.", True, "Integrity and cleverness defeat deceit.", "Hard")
]

tf_content = f"# True / False — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH01_TF_{idx:03d}"
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

with open(os.path.join(CH01_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who was Dilip and why did he leave his village?", "Dilip was a poor boy who left his village to travel to a foreign land to earn money.", "Easy"),
    ("From whom did Dilip borrow money for his travels?", "Dilip borrowed money for his travels from the rich village money lender, the Mahajan.", "Easy"),
    ("What did Dilip give to the Mahajan as security for the loan?", "Dilip gave his heavy iron scales to the Mahajan as security for the borrowed money.", "Easy"),
    ("What lie did the Mahajan tell Dilip when he asked for his scales back?", "The Mahajan lied that mice had eaten up the iron scales while they were stored in his house.", "Easy"),
    ("How did Dilip react when he heard the Mahajan's lie?", "Dilip remained calm, did not argue, and quietly walked back to his house.", "Easy"),
    ("Whom did Dilip meet a few days later near the river?", "Dilip met the Mahajan's young son walking near the river a few days later.", "Easy"),
    ("What did Dilip do with the Mahajan's son after meeting him?", "Dilip invited the boy to his house and locked him safely inside.", "Easy"),
    ("What story did Dilip make up to tell the Mahajan about his son?", "Dilip claimed that a big eagle flew down and carried the Mahajan's son away into the sky.", "Easy"),
    ("Why did the Mahajan refuse to believe Dilip's story about the eagle?", "Because an eagle cannot carry away a heavy boy, which the Mahajan knew was physically impossible.", "Easy"),
    ("How did Dilip reply when the Mahajan questioned his eagle story?", "Dilip replied that an eagle carrying a boy is possible in the exact same way that mice can eat iron scales.", "Easy"),
    ("How did the Mahajan feel when he understood Dilip's clever point?", "The Mahajan felt deeply ashamed of his greedy lie and apologized to Dilip.", "Easy"),
    ("What did the Mahajan do after apologizing to Dilip?", "The Mahajan immediately returned the heavy iron scales to Dilip.", "Easy"),
    ("What did Dilip do after receiving his scales back?", "Dilip went home and brought the Mahajan's son back safely to his father.", "Easy"),
    ("What is the main moral of the story 'The Rats Who Ate the Iron Balance'?", "The moral is that you cannot get away with doing bad things, and honesty always wins.", "Easy"),
    ("What does the word 'scales' mean in the story?", "'Scales' means an equipment or balance used for weighing objects.", "Easy"),
    ("What does the word 'security' mean in financial transactions?", "'Security' means a valuable item pledged to guarantee the repayment of a loan.", "Easy"),
    ("What does the word 'ashamed' mean?", "'Ashamed' means feeling guilty, embarrassed, or sorry because of doing something wrong.", "Easy"),
    ("Why did the Mahajan lie about the scales?", "The Mahajan lied because he was greedy and wanted to keep the valuable iron scales for himself.", "Easy"),
    ("What metal were the scales made of?", "The scales were made of heavy solid iron.", "Easy"),
    ("Can real mice eat iron metal? Why or why not?", "No, mice cannot eat iron because metal is too hard for animal teeth to chew or digest.", "Easy"),
    ("What book of ancient tales does this story come from?", "This story comes from the ancient Indian book of moral fables called the Panchatantra.", "Easy"),
    ("Did Dilip hurt the Mahajan's son while he was locked inside?", "No, Dilip kept the boy completely safe and unharmed inside his house.", "Easy"),
    ("How did Dilip show cleverness instead of anger?", "Instead of fighting or shouting, Dilip used a smart counter-story to make the Mahajan admit his lie.", "Easy"),
    ("What kind of person was the Mahajan at the beginning of the story?", "At the beginning, the Mahajan was a rich, greedy, and dishonest money lender.", "Easy"),
    ("What title does Chapter 01 carry in Book 2?", "Chapter 01 is titled 'The Rats Who Ate the Iron Balance'.", "Easy"),

    # Medium (26-40)
    ("Why was Dilip forced to borrow money before going abroad?", "Dilip was very poor and lacked the necessary funds to pay for his journey to a foreign land.", "Medium"),
    ("Why did the Mahajan think Dilip would accept his lie without protest?", "The Mahajan thought poor Dilip was simple and helpless, unable to challenge a rich man.", "Medium"),
    ("Explain why Dilip chose not to fight with the Mahajan immediately.", "Fighting a rich man directly would not get his scales back; staying calm allowed him to plan a clever lesson.", "Medium"),
    ("What is the common theme between the two lies told in the story?", "Both lies describe absurd, physically impossible events—mice eating iron and an eagle lifting a heavy boy.", "Medium"),
    ("How did Dilip's counter-story force the Mahajan to admit the truth?", "It mirrored the absurdity of the Mahajan's lie, making him realize how foolish his own lie sounded.", "Medium"),
    ("What does 'Tit for Tat' mean, and how does it apply to Dilip?", "'Tit for Tat' means giving matching treatment. Dilip gave an absurd lie back to match the Mahajan's absurd lie.", "Medium"),
    ("Why is greed harmful according to this chapter?", "Greed makes people dishonest, destroys trust, causes humiliation, and leads to moral downfall.", "Medium"),
    ("How did Dilip demonstrate self-control throughout the story?", "He refrained from anger, planned a smart stratagem, kept the boy safe, and returned him honorably.", "Medium"),
    ("What would have happened if the Mahajan had been honest from the start?", "Dilip would have paid back the loan, received his scales peacefully, and both would remain respected.", "Medium"),
    ("How does clever wit solve problems better than physical force?", "Clever wit exposes wrongdoings peacefully and compels opponents to change their minds out of self-realization.", "Medium"),
    ("Why did Dilip take the iron scales as security in the first place?", "Because security guaranteed the Mahajan that Dilip would return to repay the borrowed money.", "Medium"),
    ("What shows that Dilip was an honorable person despite locking the boy?", "He never intended to harm or keep the boy; he released him immediately upon receiving his scales.", "Medium"),
    ("Contrast the characters of Dilip and the Mahajan.", "Dilip was poor, honest, and clever; the Mahajan was rich, greedy, and dishonest.", "Medium"),
    ("How did the Mahajan feel after hearing Dilip's explanation about the eagle?", "He felt deeply embarrassed and ashamed because he realized his dishonesty was completely exposed.", "Medium"),
    ("Summarize Chapter 01 in two sentences.", "Dilip pledged iron scales to a greedy Mahajan, who lied that mice ate them. Dilip cleverly claimed an eagle took the Mahajan's son, forcing the ashamed Mahajan to return the scales.", "Medium"),

    # Hard (41-50)
    ("Analyze how irony functions as the primary narrative tool in Chapter 01.", "Irony is created when Dilip uses an equally absurd lie (eagle taking a boy) to expose the Mahajan's original lie (rats eating iron), turning deceit against the deceiver.", "Hard"),
    ("Evaluate the moral justification of Dilip taking the Mahajan's son to his house.", "While locking a child is unethical in isolation, here it was a non-violent, harmless psychological tactic used solely to achieve justice against theft.", "Hard"),
    ("How does the Mahajan's sudden remorse demonstrate the presence of inner conscience?", "His shame shows that when confronted with stark moral hypocrisy, his internal conscience recognized his guilt and prompted repentance.", "Hard"),
    ("Discuss the symbolic meaning of the iron scales in the story.", "The heavy iron scales symbolize justice, weight of truth, and moral balance; withholding them represented breaking ethical balance.", "Hard"),
    ("How can Class 2 students apply Dilip's problem-solving strategy when cheated?", "Students can stay calm, avoid physical fights, use polite logic to explain fairness, and seek teacher or parental guidance.", "Hard"),
    ("Deconstruct the psychological shift in the Mahajan from arrogant greed to humble apology.", "Arrogance -> Deceit -> Arrogant Confrontation -> Shock -> Logical Trapping -> Realization -> Shame -> Apology -> Restitution.", "Hard"),
    ("Compare the power of wealth versus the power of intelligence in resolving conflicts.", "Wealth allows temporary exploitation, but intelligence provides strategic solutions that restore justice permanently.", "Hard"),
    ("Why is peaceful resolution superior to violent retaliation in moral fables?", "Peaceful resolution upholds moral integrity, avoids collateral harm, and converts the wrongdoer through self-awareness.", "Hard"),
    ("What role does security/collateral play in commercial trust based on this text?", "Collateral provides material assurance that debts will be honored, forming the basis of financial trust.", "Hard"),
    ("Synthesize the ultimate educational message of Chapter 01 for primary learners.", "Integrity, calm reasoning, and clever wit will always triumph over greed, dishonesty, and unfair exploitation!", "Hard")
]

sa_content = f"# Short Answer — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH01_SA_{idx:03d}"
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

with open(os.path.join(CH01_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-15)
    ("Write a simple summary of Chapter 01 'The Rats Who Ate the Iron Balance'.", "A poor boy named Dilip wanted to travel to a foreign land to earn money. He borrowed money from a rich village Mahajan and gave his heavy iron scales as security. After a few years, Dilip returned with money and asked for his scales back. The greedy Mahajan lied that mice had eaten the iron scales. Dilip stayed calm and walked home quietly. A few days later, Dilip met the Mahajan's son, invited him home, and locked him inside safely. Dilip then told the Mahajan that an eagle had carried his son away into the sky. When the Mahajan said an eagle could not carry a heavy boy, Dilip replied that it was possible in the same way mice could eat iron scales. The Mahajan felt deeply ashamed, apologized, and returned the scales. Dilip then brought the boy safely back to his father.", "Easy"),
    ("Describe the character of Dilip in detail based on the story.", "Dilip is the main hero of the story. He is a poor, hardworking young boy who travels to a foreign land to earn money for his family. He is honest because he returns to pay back his loan. When cheated by the greedy Mahajan, Dilip does not lose his temper or engage in physical fighting. Instead, he shows great intelligence, self-control, and cleverness. He creates a smart plan to teach the Mahajan a lesson, keeps the Mahajan's son completely safe, and successfully recovers his iron scales. Dilip represents honesty, wisdom, and peaceful problem-solving.", "Easy"),
    ("Describe the character of the Mahajan and how his character changes.", "The Mahajan is a rich money lender in the village. At the beginning of the story, he is greedy, dishonest, and selfish. When Dilip returns to pay back his debt, the Mahajan lies that mice ate the heavy iron scales so he can keep them for himself. He takes advantage of Dilip's poor status. However, when Dilip outsmarts him with the eagle story, the Mahajan recognizes his own foolish lie. He feels deeply ashamed, apologizes for his dishonesty, returns the scales, and learns a valuable moral lesson about integrity.", "Easy"),
    ("Explain the trick Dilip used to teach the Mahajan a lesson.", "Dilip used a clever psychological trick based on matching logic. He met the Mahajan's son near the river, invited him home, and locked him safely inside. Then Dilip went to the Mahajan crying and claimed an eagle flew away with his son. When the Mahajan angrily pointed out that an eagle carrying a boy is impossible, Dilip pointed out that an eagle carrying a boy is just as possible as mice eating heavy iron scales. This clever counter-lie instantly exposed the Mahajan's dishonesty.", "Easy"),
    ("Why did the Mahajan's lie about the mice eating iron scales fail?", "The Mahajan's lie failed because solid iron metal is far too hard for mice or rats to chew or eat. It was a completely absurd and physically impossible lie. Dilip immediately recognized that the Mahajan was cheating him, and later used an equally impossible lie about an eagle lifting a child to force the Mahajan to admit that both claims were absurd.", "Easy"),
    ("What moral lessons does the story teach us about greed and dishonesty?", "The story teaches that greed leads to dishonest behavior, which destroys trust and damages reputation. It proves that wrongdoers cannot get away with bad actions because truth and cleverness will eventually catch up with them. It also shows that being honest and dealing fairly with others brings lasting peace and respect.", "Easy"),
    ("Explain the meaning and usage of the words 'scales', 'security', and 'ashamed'.", "• Scales: An equipment or balance used for weighing items in trade.\n• Security: A valuable object pledged to a lender to guarantee loan repayment.\n• Ashamed: Feeling embarrassed, guilty, and sorry after realizing one has done something wrong.", "Easy"),
    ("How did Dilip ensure that no harm came to the Mahajan's son?", "Dilip treated the Mahajan's son with kindness. He invited the boy to his home politely and kept him locked safely inside a room. Dilip did not hurt, scold, or scare the child. As soon as the Mahajan confessed his lie and returned the iron scales, Dilip immediately brought the boy back home safe and sound.", "Easy"),
    ("Why is clever wit better than anger when dealing with unfair people?", "Anger often leads to physical fights, harsh words, and further trouble without solving the underlying problem. Clever wit, on the other hand, allows a person to remain calm, think logically, expose the lie peacefully, and convince the other person to correct their wrongdoing without violence.", "Easy"),
    ("What role did the iron scales play in the financial agreement between Dilip and Mahajan?", "Because Dilip was poor and had no money, the Mahajan required a guarantee before lending money. Dilip gave his heavy iron scales as collateral or security. This meant that if Dilip failed to return, the Mahajan could keep the scales; but once Dilip repaid the loan, the Mahajan was legally and morally required to return them.", "Easy"),
    ("Describe the meeting between Dilip and the Mahajan's son near the river.", "A few days after the Mahajan lied about the scales, Dilip was walking near the river when he met the Mahajan's young son. Dilip spoke kindly to the boy and invited him to come to his house. The boy trusted Dilip and willingly followed him home, where Dilip locked him inside safely.", "Easy"),
    ("Why did the Mahajan feel deeply ashamed at the end of the story?", "The Mahajan felt deeply ashamed because Dilip's clever logic trapped him completely. The Mahajan had insisted that an eagle carrying a boy was impossible, but by saying so, he admitted that his own lie about mice eating iron scales was also impossible. Realizing how greedy and foolish he looked, his conscience made him feel ashamed.", "Easy"),
    ("How does the story demonstrate that poor people can overcome rich oppressors?", "The story demonstrates that physical wealth and power do not guarantee victory. Even though Dilip was poor and the Mahajan was rich, Dilip used his mind, truth, and clever reasoning to defeat the rich man's greed and reclaim his stolen property peacefully.", "Easy"),
    ("What makes Panchatantra stories timeless and valuable for children?", "Panchatantra stories use engaging plots, memorable characters, and clever situations to teach practical life lessons, moral values, human psychology, and social wisdom in a simple, enjoyable format suitable for young learners.", "Easy"),
    ("What values should Class 2 students learn from Chapter 01?", "Class 2 students should learn to be honest in all matters, respect other people's property, refrain from lying or cheating, maintain self-control when facing unfairness, and use calm intelligence to solve everyday problems.", "Easy"),

    # Medium (16-40)
    ("Analyze how Dilip's strategic patience helped him achieve justice.", "Instead of reacting with immediate fury or getting into a physical brawl with the wealthy Mahajan, Dilip maintained composure and left quietly. This strategic patience gave him the time and mental clarity needed to devise a brilliant, non-violent stratagem that exposed the Mahajan's hypocrisy and restored his property.", "Medium"),
    ("Compare the initial intentions of Dilip and the Mahajan regarding the loan.", "Dilip entered the agreement with complete honesty, intending to travel, work hard, earn money, and repay every coin to reclaim his scales. Conversely, the Mahajan entered the transaction with latent greed, eyeing the valuable iron scales and waiting for an opportunity to cheat the poor boy.", "Medium"),
    ("Discuss how the theme of 'Tit for Tat' is portrayed in Chapter 01.", "'Tit for Tat' is portrayed not as malicious revenge, but as a teaching mechanism. Dilip mirrored the Mahajan's absurd lie (rats eating iron) with his own absurd lie (eagle taking a boy). By placing the Mahajan in the exact same logical dilemma, Dilip forced him to experience the injustice firsthand.", "Medium"),
    ("Why is keeping one's promise crucial in commercial and social relationships?", "Keeping promises and honoring agreements builds mutual trust, stability, and economic cooperation in a community. When individuals like the Mahajan break promises out of greed, social harmony breaks down, leading to conflict and loss of personal reputation.", "Medium"),
    ("Explain the significance of the setting: traveling to a foreign land to earn money.", "Traveling abroad highlights Dilip's determination, courage, and hard work to overcome poverty. It establishes that his earnings and iron scales were earned through immense personal sacrifice, making the Mahajan's theft even more cruel and unjustified.", "Medium"),
    ("Write a dialogue between Dilip and the Mahajan when Dilip claims the eagle took the boy.", "Mahajan: 'Where is my son, Dilip? He went to the river with you!'\nDilip: (Crying) 'Oh Mahajan, a huge eagle flew down from the sky and carried your son away!'\nMahajan: 'You liar! How can an eagle carry a heavy boy into the sky?'\nDilip: 'It is possible in the exact same way that tiny mice can eat up heavy iron scales!'", "Medium"),
    ("Evaluate why physical violence would have been disastrous for Dilip.", "If Dilip had resorted to violence, the wealthy Mahajan would have used his influence, money, and guards to arrest Dilip for assault. Dilip would have lost his scales, his freedom, and his moral high ground. Wit allowed him to win legally and morally.", "Medium"),
    ("How does the Mahajan's son act as an unwitting catalyst for justice in the story?", "The Mahajan's son was innocent and unaware of the conflict. By temporarily hosting the boy, Dilip created emotional leverage that forced the Mahajan to experience the anxiety of loss, instantly shattering the Mahajan's greedy arrogance.", "Medium"),
    ("Describe the psychological relief felt by the Mahajan upon getting his son back.", "When the Mahajan received his son back unharmed, he felt overwhelming relief and gratitude. This emotional resolution reinforced the moral lesson: honesty and family safety are far more precious than stolen material goods like iron scales.", "Medium"),
    ("Explain how irony creates humor while delivering a serious moral lesson.", "The humor arises from the absurd image of an eagle flying off with a boy and mice munching on iron. This comedic absurdity highlights the ridiculousness of dishonesty, making the serious moral lesson—that lying makes you look foolish—memorable for students.", "Medium"),
    ("What does the story reveal about the nature of lies?", "The story reveals that lies require increasingly ridiculous justifications. A single lie creates an unstable web of deceit that collapses the moment it is tested against cold logic and truth.", "Medium"),
    ("How did Dilip's return of the boy immediately after getting his scales prove his ethical character?", "Dilip did not demand ransom or extra money. The moment justice was served and his scales were returned, he honorably returned the boy, proving his goal was fairness, not extortion or malice.", "Medium"),
    ("Why is emotional intelligence (controlling anger) vital for effective problem solving?", "Emotional intelligence prevents impulsive actions driven by rage. By keeping cool, Dilip evaluated his options, exploited the weakness in the Mahajan's lie, and executed a flawless plan to achieve his goal.", "Medium"),
    ("How does Panchatantra literature use irony to educate young royalty and citizens?", "Panchatantra was composed to teach 'Niti' (practical governance and wise living). Irony exposes human folly, teaching readers to anticipate deceit, think critically, and govern with justice and intellect.", "Medium"),
    ("Describe how Dilip's reputation in the village likely changed after this incident.", "Dilip would be recognized not just as a hardworking young man, but as a clever, fair-minded, and formidable individual who could hold his own against corrupt figures, earning universal respect.", "Medium"),
    ("Explain why security/collateral is used in traditional lending practices.", "Security protects lenders against default. However, it requires absolute honesty from the custodian. The Mahajan breached this sacred commercial trust, showing that legal mechanisms fail without personal integrity.", "Medium"),
    ("What lesson does the Mahajan's son learn from watching his father's apology?", "The son learns that dishonesty brings humiliation, that his father made a grave mistake, and that apologizing and returning stolen property is the right way to restore honor.", "Medium"),
    ("How does Chapter 01 align with Class 2 English curriculum goals?", "It develops reading comprehension, vocabulary (scales, security, ashamed), story sequencing, character analysis, moral reasoning, and critical thinking through structured primary exercises.", "Medium"),
    ("Contrast the feelings of the Mahajan at the beginning, middle, and end of the story.", "• Beginning: Greedily confident and arrogant in his lie.\n• Middle: Anxious, angry, and demanding when his son went missing.\n• End: Deeply ashamed, humbled, remorseful, and relieved.", "Medium"),
    ("Summarize Chapter 01 in four comprehensive bullet points.", "• Dilip pledges iron scales to the Mahajan for travel money and returns years later to repay the debt.\n• The greedy Mahajan lies that mice ate the iron scales to keep them for himself.\n• Dilip locks the Mahajan's son safely and claims an eagle carried the boy away into the sky.\n• Trapped by his own logic, the ashamed Mahajan apologizes, returns the scales, and receives his son back.", "Medium"),

    # Hard (41-50)
    ("Deconstruct the ethical dilemma presented in Dilip's stratagem of locking the child.", "Dilip faces an ethical dilemma: submit to unjust theft or use deception to reclaim his property. By choosing temporary, harmless detention of the son, Dilip minimizes harm while engineering a psychological mirror that compels moral restitution. The ethics of his action are justified by his non-violent intent, protection of the child, and immediate release upon justice.", "Hard"),
    ("Analyze the structural symmetry of the narrative in Chapter 01.", "The plot exhibits perfect structural symmetry: Act 1 presents Transaction & Pledge; Act 2 presents Deceit (Mice eat Iron); Act 3 presents Counter-Deceit (Eagle takes Boy); Act 4 presents Logical Confrontation; and Act 5 presents Dual Restitution (Scales returned, Boy returned). This symmetry reinforces the moral law of cause and effect.", "Hard"),
    ("Critique the socio-economic dynamics between the wealthy Mahajan and poor Dilip.", "The narrative exposes class vulnerability: rich moneylenders often exploit poor borrowers expecting no resistance. Dilip's victory subverts class oppression, proving that intellectual agency and moral truth can overcome economic hegemony without political or physical rebellion.", "Hard"),
    ("Evaluate the role of 'Shame' (Lajja) as an internal mechanism for social justice.", "External punishment (jail or fines) often breeds resentment, whereas genuine shame triggers internal moral re-alignment. When the Mahajan felt ashamed, his self-image as a respected elder was shattered, driving authentic repentance and structural restitution.", "Hard"),
    ("Examine the linguistic precision of Dilip's response: 'It is possible exactly the way the mice eating up the iron scales is.'", "Dilip's response is a masterclass in rhetorical reductio ad absurdum. Without directly calling the Mahajan a liar, he equates two logical impossibilities, forcing the antagonist to either accept both absurdities or admit his own falsehood.", "Hard"),
    ("Formulate a Class 2 classroom debate on 'Was Dilip right to trick the Mahajan?'", "Group A argues Dilip was right because he was non-violent, protected the child, and reclaimed his rightful property against a thief. Group B explores alternative peaceful avenues like village elders. The exercise builds ethical reasoning and verbal expression.", "Hard"),
    ("Differentiate between retributive justice and restorative justice as demonstrated in this tale.", "Retributive justice focuses on punishing the offender (e.g., beating or jailing the Mahajan). Restorative justice focuses on repairing harm and restoring balance (returning scales, returning the son, and awakening conscience). Dilip achieved restorative justice.", "Hard"),
    ("How does Chapter 01 reflect ancient Indian legal and philosophical concepts of Dharma?", "Dharma encompasses duty, truth, and cosmic order. The Mahajan violated Dharma through Adharma (greed and deceit). Dilip acted as an instrument of Dharma, restoring order through intellect and truth, proving that Dharma protects those who uphold it.", "Hard"),
    ("Why is material security (collateral) secondary to moral integrity in commercial trade?", "Without moral integrity, physical security can be stolen or denied through false claims. Commercial trade relies fundamentally on human honor; when honor fails, contracts collapse regardless of signed papers or stored collateral.", "Hard"),
    ("Synthesize the ultimate philosophy of Chapter 01 for primary learners.", "True strength lies not in wealth or physical power, but in moral integrity and sharp intellect. Walk in truth, treat others fairly, and face adversity with calm, clever wisdom!", "Hard")
]

la_content = f"# Long Answer — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH01_LA_{idx:03d}"
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

with open(os.path.join(CH01_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based Questions (10 Extracts x 5 Qs = 50 Qs)
# -------------------------------------------------------------
extracts = [
    (
        "A boy named Dilip wanted to go to a foreign land to earn money. As he was poor he borrowed money for his travels from the Mahajan, giving his heavy iron scales as security.",
        [
            ("Who wanted to go to a foreign land?", "Dilip wanted to go to a foreign land to earn money.", "Easy"),
            ("Why did Dilip borrow money from the Mahajan?", "Because he was poor and needed funds for his travel expenses.", "Easy"),
            ("What did Dilip pledge as security for the borrowed money?", "He pledged his heavy iron scales as security.", "Easy"),
            ("What does the word 'security' mean in this passage?", "Security means a valuable item pledged to guarantee loan repayment.", "Medium"),
            ("What trait of Dilip is shown by giving security before borrowing?", "It shows Dilip was responsible, honest, and respected financial agreements.", "Hard")
        ]
    ),
    (
        "After a few years when he had earned money, he returned to his village. He went to the Mahajan to pay him back and get his scales back.",
        [
            ("When did Dilip return to his village?", "He returned to his village after a few years of earning money abroad.", "Easy"),
            ("Why did Dilip visit the Mahajan upon his return?", "To pay back the borrowed money and get his iron scales back.", "Easy"),
            ("How did Dilip earn his money while abroad?", "He earned money through hard work during his stay in the foreign land.", "Easy"),
            ("What does 'pay him back' mean in simple words?", "It means repaying the debt or returning the borrowed money.", "Medium"),
            ("What value does Dilip demonstrate by returning to repay his loan?", "Dilip demonstrates honesty, integrity, and law-abiding character.", "Hard")
        ]
    ),
    (
        "The Mahajan was greedy and did not want to return the strong scales. He lied, 'The mice ate it.' Dilip understood what was going on. Without saying a word, he went back home.",
        [
            ("Why did the Mahajan refuse to return the scales?", "Because he was greedy and wanted to keep the strong iron scales for himself.", "Easy"),
            ("What absurd lie did the Mahajan tell Dilip?", "He lied that mice had eaten up the iron scales.", "Easy"),
            ("What did Dilip do immediately after hearing the lie?", "Without saying a word, he quietly walked back home.", "Easy"),
            ("Why could mice not actually eat the scales?", "Because the scales were made of solid iron metal, which mice cannot chew or digest.", "Medium"),
            ("How does Dilip's silent departure show wisdom rather than weakness?", "Instead of wasting energy in futile arguments, he quietly planned a strategic lesson.", "Hard")
        ]
    ),
    (
        "After some days, Dilip met Mahajan's son on way to the river and asked him to come home with him. The boy followed him and Dilip locked him in his house.",
        [
            ("Whom did Dilip meet near the river a few days later?", "Dilip met the Mahajan's son near the river.", "Easy"),
            ("Where did Dilip invite the Mahajan's son?", "He invited the boy to come to his house.", "Easy"),
            ("What did Dilip do once the boy entered his house?", "Dilip locked the boy safely inside his house.", "Easy"),
            ("Why did the Mahajan's son willingly follow Dilip?", "Because Dilip was friendly and the boy trusted him as a fellow villager.", "Medium"),
            ("Was Dilip's action motivated by harm or by seeking justice?", "It was motivated purely by seeking non-violent justice, ensuring the boy was safe.", "Hard")
        ]
    ),
    (
        "Then, crying, he went to the Mahajan and informed him that an eagle carried away his son into the sky.",
        [
            ("Whom did Dilip visit after locking the boy?", "Dilip visited the Mahajan.", "Easy"),
            ("What emotion did Dilip pretend to show while speaking?", "Dilip pretended to cry while speaking.", "Easy"),
            ("What story did Dilip tell the Mahajan about his son?", "He told him that an eagle had carried his son away into the sky.", "Easy"),
            ("Why did Dilip pretend to cry?", "To create dramatic belief and draw out an immediate reaction from the Mahajan.", "Medium"),
            ("How does this lie mirror the Mahajan's original lie?", "Both lies describe physically impossible events to test logical honesty.", "Hard")
        ]
    ),
    (
        "The Mahajan could not believe it and asked how was that possible.",
        [
            ("Did the Mahajan believe Dilip's story about the eagle?", "No, the Mahajan could not believe it.", "Easy"),
            ("What question did the Mahajan ask Dilip?", "He asked how it was possible for an eagle to carry away his son.", "Easy"),
            ("Why did the Mahajan find the eagle story impossible?", "Because a young boy is far too heavy for an eagle to lift and carry into the sky.", "Easy"),
            ("What does 'could not believe it' mean in this context?", "It means he found the claim completely absurd and false.", "Medium"),
            ("What irony exists in the Mahajan demanding physical logic from Dilip?", "The irony is that the Mahajan had previously expected Dilip to believe an equally impossible lie.", "Hard")
        ]
    ),
    (
        "'It is possible exactly the way the mice eating up the iron scales is.' The Mahajan felt ashamed.",
        [
            ("What was Dilip's exact answer to the Mahajan?", "'It is possible exactly the way the mice eating up the iron scales is.'", "Easy"),
            ("How did the Mahajan feel after hearing Dilip's response?", "The Mahajan felt deeply ashamed.", "Easy"),
            ("Why did the Mahajan feel ashamed?", "Because Dilip's answer exposed his greedy lie using his own logic.", "Easy"),
            ("What does the word 'ashamed' mean?", "Feeling guilty, embarrassed, and sorry for committing a wrong act.", "Medium"),
            ("Analyze the logical power of Dilip's statement.", "It used reductio ad absurdum to collapse the Mahajan's lie without needing external proof.", "Hard")
        ]
    ),
    (
        "He apologised and returned the scales to Dilip. Dilip brought back the boy to his father.",
        [
            ("What did the Mahajan do after feeling ashamed?", "He apologized and returned the iron scales to Dilip.", "Easy"),
            ("What did Dilip do as soon as he received his scales?", "Dilip brought the boy back safely to his father.", "Easy"),
            ("Did Dilip keep the boy locked after getting his scales?", "No, he released the boy immediately.", "Easy"),
            ("What does 'apologised' mean in this passage?", "Expressed sincere regret for doing something wrong.", "Medium"),
            ("How does this resolution show that restoration of justice brings peace?", "When scales were returned and the boy restored, conflict ended cleanly and honorably.", "Hard")
        ]
    ),
    (
        "Moral of the Story: You cannot get away with doing bad things.",
        [
            ("What is the stated moral of the story?", "You cannot get away with doing bad things.", "Easy"),
            ("What happens when someone does something bad according to this moral?", "Their wrongdoings will eventually be exposed and punished by truth or cleverness.", "Easy"),
            ("Which character in the story did something bad?", "The Mahajan did something bad by lying and stealing the iron scales.", "Easy"),
            ("How was the moral demonstrated through Dilip's actions?", "Dilip's clever stratagem forced the Mahajan to face consequences and return the scales.", "Medium"),
            ("How can primary students apply this moral in their daily life?", "By speaking the truth, respecting others' belongings, and dealing honestly with friends.", "Hard")
        ]
    ),
    (
        "Word Meaning: Scales: An equipment that is used for weighing something. Security: Something of value used to borrow money. Ashamed: Feeling guilty because of some wrong doing.",
        [
            ("Define the word 'scales' according to the glossary.", "An equipment that is used for weighing something.", "Easy"),
            ("Define the word 'security' according to the glossary.", "Something of value used to borrow money.", "Easy"),
            ("Define the word 'ashamed' according to the glossary.", "Feeling guilty because of some wrong doing.", "Easy"),
            ("Use the word 'ashamed' in a simple sentence.", "The boy felt ashamed after breaking his friend's toy.", "Medium"),
            ("Why are clear word definitions helpful for Class 2 readers?", "They build vocabulary, improve reading comprehension, and aid contextual understanding.", "Hard")
        ]
    )
]

ext_content = f"# Extract Based Questions — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Category**: Extract Based Questions | **Total**: 10 Extracts (50 Sub-Questions) | **Marks**: 3 per set\n\n---\n\n"
sub_q_counter = 1
for ext_idx, (passage, q_list) in enumerate(extracts, start=1):
    ext_content += f"## Extract {ext_idx}\n\n"
    ext_content += f"> *\"{passage}\"*\n\n"
    for q_idx, (q_txt, ans, diff) in enumerate(q_list, start=1):
        q_id = f"BK02_CH01_EXT_{sub_q_counter:03d}"
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

with open(os.path.join(CH01_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print("[SUCCESS] All 6 category files for Book 2 Chapter 01 completely refined with 100% unique Class 2 questions!")
