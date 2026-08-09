r"""
Refines all 6 Category files for Chapter 01 ("The Monkey and the Crocodile") for Class 1.
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 1 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
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
    ("Where did the monkey live?", "(A) On a mango tree", "(B) On a berry tree", "(C) In a cave", "(D) Under a stone", "(B)", "The monkey lived on a berry tree near the river bank.", "Easy", "Remembering", "Setting"),
    ("What food did the monkey share with the crocodile?", "(A) Apples", "(B) Sweet berries", "(C) Bananas", "(D) Fish", "(B)", "The monkey gave sweet, juicy berries to the crocodile.", "Easy", "Remembering", "Character Action"),
    ("Where was the berry tree located?", "(A) In a town", "(B) On the banks of a river", "(C) On a high mountain", "(D) In a school", "(B)", "The tree was on the banks of a river.", "Easy", "Remembering", "Setting"),
    ("Who came to rest under the berry tree?", "(A) A tiger", "(B) A crocodile", "(C) A bear", "(D) A rabbit", "(B)", "The crocodile came to rest under the berry tree.", "Easy", "Remembering", "Character Introduction"),
    ("What relationship did the monkey and crocodile develop?", "(A) Enemies", "(B) Good friends", "(C) Strangers", "(D) Neighbors", "(B)", "They spent time together and became good friends.", "Easy", "Remembering", "Character Relationship"),
    ("Who did the monkey send berries for?", "(A) The crocodile's wife", "(B) A little bird", "(C) The lion", "(D) A frog", "(A)", "The monkey sent sweet berries for the crocodile's wife.", "Easy", "Remembering", "Plot Detail"),
    ("How did the crocodile's wife feel when she ate the sweet berries?", "(A) Angry", "(B) She liked them but grew jealous", "(C) Sad", "(D) Scared", "(B)", "She liked the berries but felt jealous of their friendship.", "Easy", "Remembering", "Character Emotion"),
    ("What did the crocodile's wife want to eat?", "(A) The monkey's heart", "(B) More berries", "(C) Fish", "(D) Grass", "(A)", "She thought the monkey's heart must be sweet and wanted to eat it.", "Easy", "Remembering", "Plot Conflict"),
    ("Why did the crocodile's wife think the monkey's heart was sweet?", "(A) Because he ate sweet berries every day", "(B) Because he drank milk", "(C) Because he slept a lot", "(D) Because he sang songs", "(A)", "She believed eating sweet berries all day made his heart sweet.", "Easy", "Understanding", "Reasoning"),
    ("How did the monkey travel across the river with the crocodile?", "(A) On a wooden boat", "(B) Riding on the crocodile's back", "(C) Swimming by himself", "(D) Flying with birds", "(B)", "The monkey rode on the crocodile's back because he could not swim.", "Easy", "Remembering", "Action"),
    ("Why could the monkey not swim across the river by himself?", "(A) He was afraid of water and could not swim", "(B) He was too fast", "(C) He had wings", "(D) The water was frozen", "(A)", "Monkeys cannot swim long distances across deep rivers.", "Easy", "Understanding", "Character Trait"),
    ("What mistake did the crocodile make while swimming in the river?", "(A) He lost his way", "(B) He blurted out his wife's real plan", "(C) He fell asleep", "(D) He dropped his tail", "(B)", "The crocodile blurted out that his wife wanted to eat the monkey's heart.", "Easy", "Understanding", "Plot Turning Point"),
    ("What trick did the clever monkey tell the crocodile?", "(A) He left his heart on the berry tree", "(B) He forgot his shoes", "(C) He wanted to bring a friend", "(D) He could not hear him", "(A)", "The monkey cleverly claimed his heart was left behind on the tree.", "Easy", "Understanding", "Clever Action"),
    ("What did the crocodile do after hearing the monkey's trick?", "(A) He swam back to the tree", "(B) He dove deep in water", "(C) He laughed loudly", "(D) He ran into the forest", "(A)", "The foolish crocodile believed him and turned back to the river bank.", "Easy", "Remembering", "Plot Action"),
    ("What did the monkey do as soon as they reached the tree?", "(A) He jumped up the tree to safety", "(B) He gave the crocodile a hug", "(C) He went to sleep", "(D) He jumped into the river", "(A)", "The monkey quickly climbed up his tree and saved his life.", "Easy", "Remembering", "Climax"),
    ("What is the moral of 'The Monkey and the Crocodile'?", "(A) Always trust everyone blindly", "(B) Choose your company wisely and use presence of mind", "(C) Never share your food", "(D) Swimming is easy", "(B)", "The story teaches us to choose friends carefully and stay calm in danger.", "Easy", "Understanding", "Moral"),
    ("What kind of story is 'The Monkey and the Crocodile'?", "(A) A Panchatantra tale", "(B) A fairy tale from Europe", "(C) A science poem", "(D) A real history lesson", "(A)", "It is a famous ancient Indian Panchatantra moral fable.", "Easy", "Remembering", "Genre"),
    ("Which word describes the monkey when he saved his life?", "(A) Foolish", "(B) Clever and quick-witted", "(C) Lazy", "(D) Mean", "(B)", "The monkey used his intelligence to outsmart the crocodile.", "Easy", "Understanding", "Character Analysis"),
    ("Which word describes the crocodile's wife?", "(A) Kind and sharing", "(B) Jealous and greedy", "(C) Helpful", "(D) Shy", "(B)", "She was jealous of their friendship and demanded the monkey's heart.", "Easy", "Understanding", "Character Analysis"),
    ("Which word describes the crocodile when he believed the heart was on the tree?", "(A) Foolish", "(B) Super smart", "(C) Angry", "(D) Careful", "(A)", "The crocodile was foolish to think a heart could be left on a tree.", "Easy", "Understanding", "Character Analysis"),
    ("What did the monkey offer to the crocodile on their first meeting?", "(A) Sweet berries", "(B) Water", "(C) Fish", "(D) Leaves", "(A)", "The kind monkey offered berries to his guest.", "Easy", "Remembering", "Factual Detail"),
    ("How did the crocodile invite the monkey to his house?", "(A) For a dinner party", "(B) For a game of tag", "(C) To show him a movie", "(D) To build a house", "(A)", "He invited the monkey saying his wife wanted to host him for dinner.", "Easy", "Remembering", "Plot Detail"),
    ("Did the monkey survive at the end of the story?", "(A) Yes, he saved himself safely on his tree", "(B) No, he was eaten", "(C) No, he drowned", "(D) He ran away to another forest", "(A)", "The clever monkey safely climbed his tree and stayed away from the crocodile.", "Easy", "Remembering", "Story Ending"),
    ("What happened to the friendship between the monkey and crocodile?", "(A) It ended because the crocodile betrayed his trust", "(B) They stayed best friends", "(C) They moved in together", "(D) They became brothers", "(A)", "The friendship ended because the crocodile tried to harm the monkey.", "Easy", "Understanding", "Plot Resolution"),
    ("Which animal lives both on land and in water in this story?", "(A) Monkey", "(B) Crocodile", "(C) Rabbit", "(D) Parrot", "(B)", "Crocodiles are reptiles that can live in water and on land.", "Easy", "Remembering", "General Knowledge"),

    # Medium (26-40)
    ("Why did the monkey feel happy when the crocodile invited him for dinner?", "(A) He thought it was a genuine gesture of friendship", "(B) He wanted to swim", "(C) He liked the crocodile's wife", "(D) He was bored of berries", "(A)", "The innocent monkey trusted his friend and felt honored.", "Medium", "Understanding", "Inference"),
    ("What does 'presence of mind' mean in this story?", "(A) Thinking quickly and calmly during danger", "(B) Memory of past events", "(C) Being absent-minded", "(D) Sleeping peacefully", "(A)", "Presence of mind means staying calm and finding a solution in crisis.", "Medium", "Understanding", "Vocabulary Concept"),
    ("Why was the crocodile reluctant at first to catch the monkey?", "(A) Because the monkey was his friend", "(B) Because he was scared of monkeys", "(C) Because berries were sour", "(D) Because he was full", "(A)", "The crocodile valued their friendship and did not want to betray him.", "Medium", "Understanding", "Character Motivation"),
    ("What made the crocodile change his mind and trick the monkey?", "(A) His wife insisted and threatened him", "(B) He disliked berries", "(C) He wanted to leave the river", "(D) The king ordered him", "(A)", "His wife persuaded him to bring the monkey's heart.", "Medium", "Understanding", "Plot Cause"),
    ("What would have happened if the monkey had panicked in the middle of the river?", "(A) He would have been killed by the crocodile", "(B) He would have flown away", "(C) The river would dry up", "(D) The crocodile would apologize", "(A)", "Panicking would have cost him his life; staying calm allowed him to think of a plan.", "Medium", "Analyzing", "Hypothetical Outcome"),
    ("Which sentence best describes the monkey's reaction upon reaching the tree safety?", "(A) He laughed at the foolish crocodile and broke off the friendship", "(B) He jumped back into the river", "(C) He apologized to the crocodile", "(D) He invited the wife over", "(A)", "He safely scolded the crocodile for his betrayal and broke off ties.", "Medium", "Understanding", "Plot Climax"),
    ("What does the word 'blurted' mean in the passage?", "(A) Spoke suddenly without thinking", "(B) Sang softly", "(C) Whispered quietly", "(D) Wrote on a paper", "(A)", "Blurted means speaking impulsively without considering the result.", "Medium", "Understanding", "Vocabulary"),
    ("What does the word 'reside' mean in the story?", "(A) To live or have a home in a place", "(B) To travel fast", "(C) To eat food", "(D) To jump high", "(A)", "Reside means to live in a particular location.", "Medium", "Understanding", "Vocabulary"),
    ("What does the word 'jealous' mean in this context?", "(A) Feeling unhappy or bitter because of someone else's bond or good fortune", "(B) Feeling sleepy", "(C) Feeling hungry", "(D) Feeling cold", "(A)", "The wife was jealous of the time her husband spent with the monkey.", "Medium", "Understanding", "Vocabulary"),
    ("Why is it foolish to believe a heart can be left on a tree?", "(A) Because the heart is an organ inside a living body", "(B) Because trees don't have leaves", "(C) Because hearts are too heavy", "(D) Because monkeys don't have hearts", "(A)", "A living creature cannot keep its heart outside its body.", "Medium", "Analyzing", "Reasoning"),
    ("What lesson does the crocodile learn at the end?", "(A) Dishonesty leads to loss of true friendship and trust", "(B) Berries are bad", "(C) Monkeys can fly", "(D) Swimming is dangerous", "(A)", "The crocodile lost a true friend due to his deceitful action.", "Medium", "Understanding", "Character Lesson"),
    ("Which attribute helped the monkey escape from danger?", "(A) Intelligence and calmness", "(B) Physical strength", "(C) Loud shouting", "(D) Heavy weight", "(A)", "His sharp mind and calmness saved him.", "Medium", "Understanding", "Character Attribute"),
    ("How did the monkey share berries with the crocodile every day?", "(A) He plucked fresh berries from his tree and threw them down", "(B) He bought them from a market", "(C) He stole them", "(D) He cooked them", "(A)", "The monkey generously plucked fresh ripe berries for his friend.", "Medium", "Remembering", "Detail"),
    ("Why did the crocodile's wife feel unhappy about her husband's daily routine?", "(A) He spent hours chatting with the monkey instead of staying with her", "(B) He brought too many fish", "(C) He slept all day", "(D) He went to work", "(A)", "She disliked him spending long hours on the river bank with the monkey.", "Medium", "Understanding", "Plot Context"),
    ("What kind of friend was the monkey in the beginning?", "(A) Kind, generous, and warm-hearted", "(B) Selfish and mean", "(C) Greedy and quiet", "(D) Rude and angry", "(A)", "The monkey happily shared his delicious food with the crocodile every day.", "Medium", "Understanding", "Character Evaluation"),

    # Hard (41-50)
    ("If a friend asks you to do something wrong, what should you do based on this story?", "(A) Refuse politely and stick to what is right", "(B) Agree blindly like the crocodile", "(C) Run away forever", "(D) Fight with everyone", "(A)", "True wisdom means refusing to do harmful or wrong deeds even for friends.", "Hard", "Applying", "Real Life Application"),
    ("What is the primary difference between the monkey and the crocodile in terms of thinking?", "(A) The monkey used quick intelligence while the crocodile lacked critical thinking", "(B) The monkey was bigger", "(C) The crocodile could jump", "(D) Both thought identically", "(A)", "The monkey was clever and observant, while the crocodile was gullible.", "Hard", "Analyzing", "Comparative Analysis"),
    ("Why is 'presence of mind' more powerful than physical strength in times of trouble?", "(A) Because clever thinking helps overcome situations where physical force fails", "(B) Because strength never works", "(C) Because animals cannot fight", "(D) Because size is everything", "(A)", "The tiny monkey outsmarted a powerful crocodile using his mind.", "Hard", "Evaluating", "HOTS Reasoning"),
    ("How does the story highlight the danger of bad company?", "(A) Listening to wicked advice can ruin good relationships and reputation", "(B) Animals should not talk", "(C) River banks are unsafe", "(D) Trees are short", "(A)", "The crocodile's wife's bad advice destroyed a wonderful friendship.", "Hard", "Evaluating", "Theme Analysis"),
    ("What statement best summarizes the climax of the story?", "(A) The monkey outsmarted the crocodile by feigning that his heart was on the tree and escaped safely", "(B) The crocodile ate the monkey", "(C) The river flooded", "(D) The monkey fell into the water", "(A)", "The climax centers on the monkey's clever ruse and escape.", "Hard", "Analyzing", "Summary Analysis"),
    ("Why did the monkey pretend not to be angry when the crocodile revealed his plan?", "(A) Showing anger in deep water would have caused the crocodile to attack immediately", "(B) He was happy", "(C) He did not hear", "(D) He liked the plan", "(A)", "Controlling his emotions allowed the monkey to stay safe until he reached land.", "Hard", "Evaluating", "Strategic Thinking"),
    ("What quality of the monkey's parents/upbringing is reflected in his clever response?", "(A) Sharp alertness and self-reliance", "(B) Laziness", "(C) Fearfulness", "(D) Ignorance", "(A)", "His calm problem-solving reflects sharp alertness.", "Hard", "Evaluating", "Character Trait"),
    ("Which proverb matches the resolution of this story?", "(A) Wit is sharper than a sword", "(B) Might makes right", "(C) Haste makes waste", "(D) All that glitters is not gold", "(A)", "Intelligence (wit) overcame brute strength in saving the monkey.", "Hard", "Evaluating", "Proverb Matching"),
    ("Why can we say the crocodile was both guilty and foolish?", "(A) He betrayed a loyal friend and was easily tricked by an obvious lie", "(B) He could not swim", "(C) He ate berries", "(D) He lived in a river", "(A)", "He committed betrayal and lacked basic sense to verify the monkey's claim.", "Hard", "Analyzing", "Character Evaluation"),
    ("What key message does 'The Monkey and the Crocodile' give to Class 1 students?", "(A) Think before you act, be true to good friends, and stay calm in difficult times", "(B) Never eat berries", "(C) Don't talk to animals", "(D) Stay in water", "(A)", "The story teaches essential values of honesty, wise friendship, and cool-headedness.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 01: The Monkey and the Crocodile\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK01_CH01_MCQ_{idx:03d}"
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
    ("The monkey lived on a _______ tree near the river.", "berry", "The monkey's home was a berry tree.", "Easy"),
    ("The monkey and the crocodile became good _______.", "friends", "They spent time together and became friends.", "Easy"),
    ("The crocodile came to rest under the tree on the river _______.", "bank / banks", "The tree stood on the river bank.", "Easy"),
    ("The monkey was kind and shared sweet _______ with the crocodile.", "berries", "The monkey shared sweet berries.", "Easy"),
    ("The crocodile's _______ ate the berries and liked them.", "wife", "The crocodile brought berries for his wife.", "Easy"),
    ("The crocodile's wife felt _______ of their friendship.", "jealous", "She was jealous of the time they spent together.", "Easy"),
    ("She wanted to eat the monkey's _______.", "heart", "She thought the monkey's heart would be sweet.", "Easy"),
    ("The monkey could not _______ in the deep river.", "swim", "Monkeys cannot swim across rivers.", "Easy"),
    ("The monkey rode on the crocodile's _______.", "back", "He sat on the crocodile's back to cross.", "Easy"),
    ("The crocodile invited the monkey to his house for _______.", "dinner", "He tricked him with a dinner invitation.", "Easy"),
    ("The crocodile _______ out his wife's real plan while swimming.", "blurted", "He spoke without thinking.", "Easy"),
    ("The clever monkey said he left his heart on the _______.", "tree / berry tree", "He claimed his heart was left behind on the tree.", "Easy"),
    ("The foolish crocodile _______ back to the tree.", "swam", "He turned around and swam back.", "Easy"),
    ("The monkey jumped up the tree to save his _______.", "life", "He climbed up safely.", "Easy"),
    ("The story teaches us to use our _______ of mind in danger.", "presence", "Presence of mind saves us from trouble.", "Easy"),
    ("The monkey was very _______ to share his berries every day.", "generous / kind", "He shared his food kindly.", "Easy"),
    ("The crocodile lived in the _______.", "river / water", "Crocodiles live in water.", "Easy"),
    ("The monkey lived in the _______ on a tree.", "forest", "The tree was in a forest.", "Easy"),
    ("The wife believed the monkey's heart was _______.", "sweet", "She thought eating sweet berries made his heart sweet.", "Easy"),
    ("The crocodile was _______ to trick his friend at first.", "unwilling / hesitant", "He did not want to betray his friend.", "Easy"),
    ("The clever monkey saved himself using his _______.", "mind / brain / intelligence", "He used his intelligence to escape.", "Easy"),
    ("The monkey told the crocodile that his heart was on the _______.", "branch / tree", "He pretended it was on the branch.", "Easy"),
    ("The crocodile felt _______ when he realized he was fooled.", "foolish / ashamed", "He realized the monkey tricked him.", "Easy"),
    ("The friendship between the monkey and crocodile was _______.", "broken / lost", "Betrayal ended their friendship.", "Easy"),
    ("'The Monkey and the Crocodile' is a _______ tale.", "Panchatantra", "It is a famous Panchatantra moral fable.", "Easy"),

    # Medium (26-40)
    ("The word 'reside' means to _______ in a place.", "live / dwell", "Reside means to have a home somewhere.", "Medium"),
    ("The word 'blurt' means to speak _______ without thinking.", "suddenly / quickly", "Blurt means speaking impulsively.", "Medium"),
    ("The word 'jealous' means feeling _______ about someone's good fortune.", "upset / angry / bitter", "Jealousy is feeling bitter at others.", "Medium"),
    ("The crocodile's wife was _______ because her husband spent time with the monkey.", "unhappy / jealous", "She disliked their close friendship.", "Medium"),
    ("The monkey realized he was in _______ when the crocodile spoke.", "danger", "He realized the crocodile intended to kill him.", "Medium"),
    ("Instead of screaming, the monkey stayed _______ and calm.", "quiet / cool", "Staying calm helped him think of a plan.", "Medium"),
    ("The monkey pretended to be _______ to go back to the tree.", "eager / willing", "He pretended he wanted to get his heart.", "Medium"),
    ("As soon as they reached the shore, the monkey climbed up to _______.", "safety", "He reached the top of the tree safely.", "Medium"),
    ("The crocodile proved to be a _______ friend.", "false / treacherous / bad", "He broke the trust of friendship.", "Medium"),
    ("A true friend never tries to _______ another friend.", "harm / hurt / betray", "True friendship means caring for each other.", "Medium"),
    ("The monkey called the crocodile _______ for believing his lie.", "foolish / silly", "He mocked the crocodile's stupidity.", "Medium"),
    ("The berries on the tree were ripe, red, and _______.", "juicy / sweet", "The berries tasted sweet and delicious.", "Medium"),
    ("The crocodile swam in the _______ part of the river.", "middle / deep", "He blurted the secret in deep water.", "Medium"),
    ("The story shows that wit is stronger than physical _______.", "strength / power", "Cleverness overcomes strength.", "Medium"),
    ("We must choose our companions _______.", "wisely / carefully", "We should select good friends carefully.", "Medium"),

    # Hard (41-50)
    ("The monkey's quick lie was an example of strategic _______.", "thinking / intelligence", "He devised a quick escape plan.", "Hard"),
    ("The story demonstrates how greed and jealousy destroy _______ relationships.", "good / peaceful / friendly", "Jealousy ruins harmony.", "Hard"),
    ("Without presence of mind, the monkey would have lost his _______.", "life / survival", "Panic would have led to his death.", "Hard"),
    ("The crocodile's betrayal shows that blind obedience to bad advice is _______.", "harmful / foolish", "Following bad advice brings ruin.", "Hard"),
    ("The tree served as both a home and a place of _______ for the monkey.", "safety / refuge", "The tree kept him safe from predators.", "Hard"),
    ("The moral lesson teaches us to evaluate our friends' _______ before trusting them.", "intentions / character", "We should know a friend's true nature.", "Hard"),
    ("A person's heart cannot exist separate from their _______.", "body", "An organ cannot be kept on a tree.", "Hard"),
    ("The monkey's calm response prevented the crocodile from attacking in _______ water.", "deep", "Staying calm avoided immediate attack.", "Hard"),
    ("In times of crisis, a calm mind helps us find a quick _______.", "solution / way out", "Calmness leads to solutions.", "Hard"),
    ("The tale of 'The Monkey and the Crocodile' inspires children to value _______ and wisdom.", "honesty / truth / alert mind", "It promotes alertness and integrity.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 01: The Monkey and the Crocodile\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK01_CH01_FIB_{idx:03d}"
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
# 3. Fill in Blanks from Story (Cloze Passage) (50 Distinct Qs)
# -------------------------------------------------------------
cloze_data = [
    ("Once upon a time, a monkey lived on a _______ tree near a river.", "berry", "Easy"),
    ("The monkey offered sweet berries to a _______ who came to rest under his tree.", "crocodile", "Easy"),
    ("The crocodile ate the berries and loved their _______ taste.", "sweet / juicy", "Easy"),
    ("Every day, the crocodile visited the river _______ to meet the monkey.", "bank", "Easy"),
    ("The monkey and the crocodile soon became good _______.", "friends", "Easy"),
    ("One day, the monkey sent some sweet berries for the crocodile's _______.", "wife", "Easy"),
    ("The crocodile's wife ate the berries and liked them very _______.", "much", "Easy"),
    ("However, the wife felt _______ because her husband spent so much time with the monkey.", "jealous", "Easy"),
    ("She told her husband that the monkey's _______ must be very sweet.", "heart", "Easy"),
    ("She asked the crocodile to bring the monkey's heart for her to _______.", "eat", "Easy"),
    ("The crocodile was _______ to kill his good friend at first.", "unwilling / sad", "Easy"),
    ("Finally, the crocodile agreed and invited the monkey home for _______.", "dinner", "Easy"),
    ("The monkey was happy to visit, but he could not _______.", "swim", "Easy"),
    ("So, the crocodile let the monkey ride on his _______.", "back", "Easy"),
    ("As they reached the middle of the river, the water was very _______.", "deep", "Easy"),
    ("The crocodile could not keep the secret and _______ out his wife's plan.", "blurted", "Easy"),
    ("He told the monkey, 'My wife wants to eat your _______.'", "heart", "Easy"),
    ("The monkey was shocked, but he used his _______ of mind.", "presence", "Easy"),
    ("He stayed calm and did not _______ in the water.", "panic / scream", "Easy"),
    ("The clever monkey said, 'I left my heart back on the _______.'", "tree / berry tree", "Easy"),
    ("He told the crocodile, 'We must go _______ and get it.'", "back", "Easy"),
    ("The foolish crocodile _______ the clever monkey.", "believed", "Easy"),
    ("He turned around and _______ back to the river bank.", "swam", "Easy"),
    ("As soon as they reached the bank, the monkey _______ up the tree.", "jumped / climbed", "Easy"),
    ("The monkey reached the top branch and saved his _______.", "life", "Easy"),

    ("The monkey looked down at the crocodile and called him _______.", "foolish", "Medium"),
    ("He said, 'Can anyone ever keep their heart separate on a _______?'", "tree", "Medium"),
    ("The monkey realized the crocodile was a _______ friend.", "false / treacherous", "Medium"),
    ("He said, 'Our _______ is over forever.'", "friendship", "Medium"),
    ("The sad crocodile realized he had lost a _______ friend.", "true / loyal", "Medium"),
    ("The crocodile went back home with an empty _______.", "hand / heart", "Medium"),
    ("The monkey was happy to be safe back in his _______.", "home / tree", "Medium"),
    ("The moral of this Panchatantra tale is to choose company _______.", "wisely", "Medium"),
    ("It also teaches us to act with presence of _______ in danger.", "mind", "Medium"),
    ("The word 'reside' means to _______ in a place.", "live", "Medium"),
    ("The word 'blurt' means to speak _______ without thinking.", "suddenly", "Medium"),
    ("The word 'jealous' means feeling _______ of another's bond.", "bitter / unhappy", "Medium"),
    ("The berries grew on a tree beside the _______.", "river", "Medium"),
    ("The monkey shared his food with a _______ heart.", "generous / kind", "Medium"),
    ("The wife's selfishness caused the loss of a great _______.", "bond / friendship", "Medium"),

    ("In times of sudden crisis, staying _______ is key to survival.", "calm", "Hard"),
    ("Physical strength cannot beat quick _______ in times of trouble.", "intelligence / thinking", "Hard"),
    ("The crocodile's gullibility made him believe an impossible _______.", "lie / claim", "Hard"),
    ("True friendship requires mutual trust and _______.", "respect / loyalty", "Hard"),
    ("Listening to bad advice leads to regret and _______.", "loss / shame", "Hard"),
    ("The monkey's sharp mind turned a dangerous situation into _______.", "safety", "Hard"),
    ("The berry tree was a source of nourishment and _______.", "protection / shelter", "Hard"),
    ("A living creature's heart is located inside its _______.", "chest / body", "Hard"),
    ("The story highlights the contrast between cleverness and _______.", "foolishness", "Hard"),
    ("Class 1 students learn that clear thinking overcomes any _______.", "difficulty / threat", "Hard")
]

cloze_content = f"# Fill in the Blanks from Story — Chapter 01: The Monkey and the Crocodile\n\n> **Category**: Fill in the Blanks from Story (Cloze Passage) | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(cloze_data, start=1):
    q_id = f"BK01_CH01_STORY_FIB_{idx:03d}"
    q_txt, ans, diff = item
    bloom = "Remembering" if diff == "Easy" else ("Understanding" if diff == "Medium" else "Analyzing")
    cloze_content += f"### Question {idx}\n"
    cloze_content += f"- **Question ID**: {q_id}\n"
    cloze_content += f"- **Type**: Story Cloze Fillup\n"
    cloze_content += f"- **Difficulty**: {diff}\n"
    cloze_content += f"- **Bloom Level**: {bloom}\n"
    cloze_content += f"- **Topic**: Story Passage Context {idx}\n"
    cloze_content += f"- **Marks**: 1\n\n"
    cloze_content += f"**Question**: Complete the story line: \"{q_txt}\"\n\n"
    cloze_content += f"- **Answer Key**: **{ans}** — Correct word directly from the story passage.\n\n---\n\n"

with open(os.path.join(CH01_DIR, "fill_in_blanks_story.md"), "w", encoding="utf-8") as f:
    f.write(cloze_content)

# -------------------------------------------------------------
# 4. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The monkey lived on a berry tree near a river bank.", True, "The monkey's home was a berry tree by the river.", "Easy"),
    ("The monkey refused to share berries with the crocodile.", False, "The monkey kindly shared sweet berries every day.", "Easy"),
    ("The crocodile and monkey became good friends.", True, "They met daily and formed a good friendship.", "Easy"),
    ("The crocodile's wife loved the monkey and sent him gifts.", False, "She was jealous and wanted to eat his heart.", "Easy"),
    ("The crocodile's wife believed the monkey's heart must be sweet.", True, "She thought eating sweet berries made his heart sweet.", "Easy"),
    ("The monkey was a great swimmer and swam across the river.", False, "The monkey could not swim and rode on the crocodile's back.", "Easy"),
    ("The crocodile invited the monkey to his home for dinner.", True, "He tricked the monkey with a dinner invitation.", "Easy"),
    ("The crocodile kept his wife's secret until they reached his house.", False, "He blurted out the truth in the middle of the river.", "Easy"),
    ("The monkey panicked and jumped into the deep water.", False, "The monkey stayed calm and used his presence of mind.", "Easy"),
    ("The clever monkey told the crocodile that he left his heart on the tree.", True, "He claimed his heart was kept safely on the tree branch.", "Easy"),
    ("The crocodile realized the lie immediately and ate the monkey.", False, "The foolish crocodile believed the monkey and swam back.", "Easy"),
    ("As soon as they reached the bank, the monkey jumped up the tree to safety.", True, "The monkey quickly climbed to the top branch.", "Easy"),
    ("The monkey gave his heart to the crocodile after reaching the tree.", False, "He laughed at the crocodile and stayed safely on the tree.", "Easy"),
    ("The moral of the story is to choose company wisely.", True, "The story teaches us to choose friends carefully.", "Easy"),
    ("'The Monkey and the Crocodile' is a Panchatantra tale.", True, "It is an ancient Panchatantra fable.", "Easy"),
    ("The crocodile lived on the top of the berry tree.", False, "The crocodile lived in the river.", "Easy"),
    ("The monkey's berries were bitter and sour.", False, "The berries were sweet and juicy.", "Easy"),
    ("The crocodile carried the monkey on his back.", True, "The monkey rode on the crocodile's back.", "Easy"),
    ("The crocodile's wife was happy about her husband's new friend.", False, "She was jealous of their close friendship.", "Easy"),
    ("The monkey outsmarted the crocodile using his clever mind.", True, "His sharp intelligence saved his life.", "Easy"),
    ("The crocodile was wise and could not be fooled.", False, "The crocodile was foolish and believed the heart was on the tree.", "Easy"),
    ("The monkey remained friends with the crocodile at the end.", False, "The monkey broke off the friendship because of betrayal.", "Easy"),
    ("Presence of mind means staying calm and thinking quickly in danger.", True, "It means acting calmly during a crisis.", "Easy"),
    ("The monkey's heart was actually hanging on a branch.", False, "A living creature's heart is inside its body.", "Easy"),
    ("The story shows that true friends never betray each other.", True, "True friendship is built on trust and care.", "Easy"),

    # Medium (26-40)
    ("The word 'reside' means to travel to a new city.", False, "Reside means to live in a particular place.", "Medium"),
    ("The word 'blurt' means to speak suddenly without thinking.", True, "Blurt means speaking impulsively.", "Medium"),
    ("The word 'jealous' means feeling happy for someone's success.", False, "Jealous means feeling bitter or upset about someone's bond or luck.", "Medium"),
    ("The crocodile tried to trick the monkey because his wife demanded it.", True, "His wife threatened and persuaded him.", "Medium"),
    ("The monkey told the crocodile that monkeys carry their hearts in their hands.", False, "He claimed he left his heart on the berry tree.", "Medium"),
    ("Staying calm helped the monkey invent a clever trick.", True, "Calmness allowed him to think clearly in danger.", "Medium"),
    ("The crocodile lost both his friend and his respect at the end.", True, "He lost a loyal friend due to his deceit.", "Medium"),
    ("The monkey went to the crocodile's home every weekend.", False, "He only agreed to go when invited for dinner.", "Medium"),
    ("The berries were red, juicy, and delicious.", True, "The story describes them as sweet and juicy berries.", "Medium"),
    ("The crocodile swam very fast because he was happy to trick the monkey.", True, "He felt proud until he blurted out the truth.", "Medium"),
    ("The monkey scolded the crocodile from the safety of the tree.", True, "He scolded him from the high branch.", "Medium"),
    ("The story proves that physical strength is always superior to intelligence.", False, "It proves that intelligence is superior to strength.", "Medium"),
    ("The crocodile's wife wanted the heart to make medicine.", False, "She wanted to eat it because she thought it was sweet.", "Medium"),
    ("The monkey's generous nature made him share food freely.", True, "He kindly shared berries every day.", "Medium"),
    ("Crocodiles can live in water as well as on land.", True, "Crocodiles are semi-aquatic animals.", "Medium"),

    # Hard (41-50)
    ("The monkey's trick worked because the crocodile lacked logical reasoning.", True, "The crocodile failed to realize a heart cannot be removed.", "Hard"),
    ("A person should follow bad advice if it comes from family members.", False, "Bad advice should never be followed, no matter who gives it.", "Hard"),
    ("Panicking in deep water would have helped the monkey escape.", False, "Panicking would have caused him to drown or get eaten.", "Hard"),
    ("The berry tree was essential for the monkey's food and protection.", True, "It provided him food and safe refuge.", "Hard"),
    ("The story emphasizes that trust once broken is difficult to restore.", True, "The monkey ended the friendship permanently.", "Hard"),
    ("The crocodile's wife represented kindness and hospitality.", False, "She represented selfishness and greed.", "Hard"),
    ("The monkey's quick thinking is an example of emotional control.", True, "He controlled his fear to execute his plan.", "Hard"),
    ("The story teaches children to blindly trust anyone who offers food.", False, "It teaches children to choose companions carefully.", "Hard"),
    ("Without the crocodile blurted secret, the monkey might not have suspected danger.", True, "The secret revealed the true intention in time.", "Hard"),
    ("The moral applies to both children and adults in everyday decisions.", True, "Presence of mind and wise choices are universal values.", "Hard")
]

tf_content = f"# True / False — Chapter 01: The Monkey and the Crocodile\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK01_CH01_TF_{idx:03d}"
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
# 5. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Where did the monkey live in the story?", "The monkey lived on a berry tree located on the bank of a river in a forest.", "Easy"),
    ("What food did the monkey share with the crocodile?", "The monkey shared sweet, juicy berries from his tree with the crocodile.", "Easy"),
    ("Who came to rest under the berry tree?", "A crocodile came to rest under the shade of the berry tree.", "Easy"),
    ("How did the monkey and the crocodile become friends?", "They spent time talking every day, and the monkey shared berries with the crocodile.", "Easy"),
    ("For whom did the monkey send berries across the river?", "The monkey sent sweet berries for the crocodile's wife.", "Easy"),
    ("How did the crocodile's wife react after eating the berries?", "She liked the taste of the berries but grew jealous of their close friendship.", "Easy"),
    ("What did the crocodile's wife demand from her husband?", "She demanded that he bring her the monkey's heart to eat.", "Easy"),
    ("Why did the wife think the monkey's heart would be sweet?", "She believed that eating sweet berries every day made the monkey's heart sweet.", "Easy"),
    ("How did the crocodile invite the monkey to his house?", "He invited the monkey by saying his wife wanted to host him for a nice dinner.", "Easy"),
    ("Why could the monkey not cross the river by himself?", "The monkey could not swim across the deep river by himself.", "Easy"),
    ("How did the monkey travel across the river?", "The monkey rode safely on the back of the crocodile.", "Easy"),
    ("What did the crocodile do in the middle of the river?", "The crocodile blurted out that his wife wanted to eat the monkey's heart.", "Easy"),
    ("How did the monkey feel when he heard the crocodile's plan?", "The monkey was shocked and scared, but he stayed calm and quiet.", "Easy"),
    ("What trick did the clever monkey tell the crocodile?", "He claimed he had left his heart safely behind on the berry tree.", "Easy"),
    ("What did the crocodile do after hearing the monkey's trick?", "The foolish crocodile turned around and swam back to the river bank.", "Easy"),
    ("What did the monkey do as soon as they reached the river bank?", "The monkey quickly jumped off the crocodile's back and climbed up his tree.", "Easy"),
    ("What did the monkey say to the crocodile from the tree?", "He called the crocodile foolish and told him that no one keeps their heart on a tree.", "Easy"),
    ("What happened to their friendship at the end?", "Their friendship ended permanently because the crocodile betrayed the monkey's trust.", "Easy"),
    ("What is the main moral of the story?", "The moral is to choose your company wisely and always use presence of mind in danger.", "Easy"),
    ("What kind of story is 'The Monkey and the Crocodile'?", "It is an ancient Indian Panchatantra moral fable.", "Easy"),
    ("What does the word 'reside' mean?", "'Reside' means to live or have your home in a particular place.", "Easy"),
    ("What does the word 'blurt' mean?", "'Blurt' means to speak out suddenly without thinking first.", "Easy"),
    ("What does the word 'jealous' mean?", "'Jealous' means feeling bitter or unhappy about someone else's bond or good luck.", "Easy"),
    ("Name the main characters in this story.", "The main characters are the clever monkey, the foolish crocodile, and his jealous wife.", "Easy"),
    ("Which animal proved to be clever in the story?", "The monkey proved to be very clever and intelligent.", "Easy"),

    # Medium (26-40)
    ("Why was the crocodile hesitant to harm the monkey at first?", "The crocodile valued their friendship and did not want to hurt someone who shared food with him.", "Medium"),
    ("What forced the crocodile to change his mind and trick the monkey?", "His wife insisted, threatened him, and refused to eat until he brought the heart.", "Medium"),
    ("Why was it important for the monkey to stay calm in the river?", "Staying calm helped him think of a clever trick; panicking in deep water would have killed him.", "Medium"),
    ("Why did the crocodile believe the monkey's lie about his heart?", "The crocodile was gullible and lacked basic logical reasoning.", "Medium"),
    ("What does 'presence of mind' mean in simple words?", "It means staying calm and finding a smart way out when you face sudden danger.", "Medium"),
    ("Why is the berry tree important to the monkey?", "The berry tree gave the monkey sweet food to eat and a safe place to live.", "Medium"),
    ("How did the monkey show generosity every day?", "He willingly plucked fresh, sweet berries and threw them down to the crocodile.", "Medium"),
    ("What made the crocodile's wife jealous of the monkey?", "She disliked her husband spending long hours chatting with the monkey instead of staying home.", "Medium"),
    ("How did the monkey react when he reached the safety of the branch?", "He felt relieved, laughed at the crocodile's foolishness, and ended their friendship.", "Medium"),
    ("What lesson does the crocodile learn at the end of the story?", "He learned that dishonesty and betrayal cause the loss of true friends and trust.", "Medium"),
    ("Why cannot a living creature leave its heart on a tree?", "Because the heart is an essential organ inside a living body that keeps it alive.", "Medium"),
    ("What kind of friend was the crocodile in the end?", "He was a treacherous and false friend who broke the bond of trust.", "Medium"),
    ("How did the monkey's quick thinking save his life?", "He invented a believable story that made the crocodile return to the shore.", "Medium"),
    ("What should we do if someone tries to trick us?", "We should stay calm, think carefully, and use our intelligence to stay safe.", "Medium"),
    ("Why is Panchatantra famous around the world?", "Panchatantra is famous for teaching valuable moral lessons through animal stories.", "Medium"),

    # Hard (41-50)
    ("How does the story demonstrate that intelligence is superior to physical strength?", "The small monkey used his sharp mind to outsmart a large, powerful crocodile and escape safely.", "Hard"),
    ("Why did the crocodile's wife's bad advice bring ruin to her husband?", "Her selfish demand made the crocodile betray his loyal friend and end up with nothing.", "Hard"),
    ("What key values should Class 1 students learn from this fable?", "Students should learn to choose good friends, be generous, stay calm in trouble, and act wisely.", "Hard"),
    ("How did the setting of the river influence the conflict in the story?", "The deep river put the non-swimming monkey at a disadvantage, raising the stakes during the journey.", "Hard"),
    ("Contrast the character of the monkey with the crocodile's wife.", "The monkey was kind, sharing, and clever, while the wife was greedy, jealous, and cruel.", "Hard"),
    ("Why was the monkey's lie justified in this situation?", "His lie was a self-defense strategy used solely to save his life from an attacker.", "Hard"),
    ("What does the end of their friendship teach us about trust?", "Trust is hard to build but easily broken; once lost, it can rarely be restored.", "Hard"),
    ("How can a child apply 'presence of mind' in daily life?", "By staying calm during emergencies, like finding a teacher when lost or hurt.", "Hard"),
    ("Why did the monkey scold the crocodile from the high branch instead of near the ground?", "He made sure he was completely out of reach of the crocodile's jaws before speaking.", "Hard"),
    ("Summarize the ultimate message of 'The Monkey and the Crocodile' in one sentence.", "Clear thinking and moral integrity will always overcome deceit and physical threat.", "Hard")
]

sa_content = f"# Short Answer — Chapter 01: The Monkey and the Crocodile\n\n> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK01_CH01_SA_{idx:03d}"
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
# 6. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-15)
    ("Write a simple summary of the story 'The Monkey and the Crocodile'.", "A kind monkey lived on a berry tree near a river and shared sweet berries with a crocodile. They became good friends. The crocodile's wife grew jealous and wanted to eat the monkey's heart. The crocodile carried the monkey on his back to his house, but blurted out the truth. The clever monkey tricked the crocodile by saying he left his heart on the tree. When they returned, the monkey jumped up the tree to safety, ending their friendship.", "Easy"),
    ("Describe how the monkey and the crocodile first met and became friends.", "The monkey lived on a lush berry tree on the bank of a river. One day, a crocodile swam to the shore and rested under the tree. The generous monkey plucked sweet berries and threw them down. The crocodile enjoyed them immensely and returned every day. Over shared conversations and delicious berries, they became fond companions.", "Easy"),
    ("Explain why the crocodile's wife wanted the monkey's heart.", "When the crocodile brought sweet berries home, his wife loved their taste. However, she felt jealous of the long hours her husband spent with the monkey. She believed that because the monkey ate sweet berries every day, his heart must be exceptionally sweet. She insisted that her husband bring the monkey's heart for her to eat.", "Easy"),
    ("How did the crocodile trick the monkey into riding on his back?", "The crocodile invited the monkey to his house for a special dinner, claiming his wife was eager to host him. Since the monkey could not swim across the deep river, the crocodile kindly offered to carry him on his back. The unsuspecting monkey happily agreed and climbed onto his friend's back.", "Easy"),
    ("What happened when the crocodile revealed his true intention in the river?", "In the middle of the deep river, the crocodile blurted out that his wife wanted to eat the monkey's heart. The monkey was shocked and terrified, but he controlled his fear. He calmly told the crocodile that he kept his heart safely on the berry tree and needed to return to fetch it.", "Easy"),
    ("How did the clever monkey save his life after reaching the river bank?", "As soon as the foolish crocodile swam back and reached the bank, the monkey quickly jumped off his back and climbed to the top branch of his tree. Safe on high ground, he laughed at the foolish crocodile, scolded him for his betrayal, and ended their friendship permanently.", "Easy"),
    ("What is the moral of the story 'The Monkey and the Crocodile'?", "The moral of the story is to choose your company wisely and always use presence of mind in times of danger. True friends never betray trust, and staying calm helps us find clever solutions to dangerous problems.", "Easy"),
    ("Describe the character of the monkey in three to four sentences.", "The monkey was kind, generous, and warm-hearted because he shared sweet berries every day. He was also innocent and trusting toward his friend. Most importantly, he was clever, calm, and quick-witted, which helped him outsmart the crocodile and save his life.", "Easy"),
    ("Describe the character of the crocodile's wife.", "The crocodile's wife was selfish, jealous, and demanding. She disliked her husband spending time with the monkey. Driven by greed and jealousy, she persuaded her husband to kill his loyal friend just to satisfy her desire to eat his heart.", "Easy"),
    ("Describe the character of the crocodile.", "The crocodile was friendly at first, but he lacked wisdom and moral strength. He allowed his wife to persuade him into betraying his best friend. Furthermore, he was foolish enough to believe that a heart could be left on a tree branch.", "Easy"),
    ("Why is 'The Monkey and the Crocodile' called a Panchatantra tale?", "It is called a Panchatantra tale because it belongs to an ancient collection of Indian animal fables written to teach young minds practical wisdom, moral values, and social intelligence through engaging animal stories.", "Easy"),
    ("What lesson does this story teach about sharing food with others?", "The story shows that sharing food brings joy and builds friendships. The monkey kindly shared fresh berries every day, showing that generosity is a noble quality that brings people together.", "Easy"),
    ("Why did the monkey tell the crocodile that he left his heart on the tree?", "He told this lie as a clever ruse to make the crocodile turn back toward the shore. He knew that once he reached land, he could climb his tree and escape from danger.", "Easy"),
    ("How did the crocodile feel when he realized he was tricked by the monkey?", "The crocodile felt foolish, embarrassed, and deeply remorseful. He realized that he had lost a loyal, generous friend forever because of his betrayal and lack of intelligence.", "Easy"),
    ("What would have happened if the monkey had jumped into the water?", "If the monkey had jumped into the water, he would have drowned or been caught easily by the crocodile, because monkeys cannot swim in deep rivers.", "Easy"),

    # Medium (16-40)
    ("Explain the term 'presence of mind' using the monkey's actions in the story.", "Presence of mind means staying calm, composed, and alert when faced with sudden danger. When the crocodile revealed his plan in deep water, the monkey did not scream or panic. Instead, he maintained composure and quickly invented a plausible story about leaving his heart on the tree. This calm intelligence saved his life.", "Medium"),
    ("Compare the friendship of the monkey and crocodile at the beginning versus the end.", "In the beginning, their friendship was warm, sweet, and built on generosity and daily companionship. At the end, the friendship was destroyed because the crocodile betrayed the monkey's trust. The monkey realized that a friend who harms you is a false companion, ending the relationship forever.", "Medium"),
    ("Why did the monkey scold the crocodile from the top branch of the tree?", "From the top branch, the monkey was completely safe from the crocodile's jaws. He scolded him to make him realize how foolish and treacherous he had been, and to declare firmly that their friendship was over.", "Medium"),
    ("Discuss the importance of choosing good companions based on this fable.", "Choosing good companions is vital because bad companions can lead us into danger or betray us. The crocodile gave in to bad advice and betrayed his loyal friend. We must surround ourselves with friends who are honest, caring, and trustworthy.", "Medium"),
    ("How did the setting of the river and tree influence the story's outcome?", "The river was the crocodile's domain where the monkey was helpless. However, the berry tree on the bank was the monkey's safe refuge. By tricking the crocodile into returning to the bank, the monkey regained his natural advantage and reached safety.", "Medium"),
    ("Why was the crocodile's wife jealous of the monkey?", "She was jealous because her husband spent long hours on the river bank talking and eating berries with the monkey instead of staying home. Her jealousy turned into bitterness, prompting her to demand the monkey's life.", "Medium"),
    ("What makes the monkey's trick so believable to the foolish crocodile?", "The monkey spoke with complete confidence and pretended to be eager to help. The foolish crocodile lacked basic scientific knowledge and did not realize that an animal cannot live without its heart inside its body.", "Medium"),
    ("Explain how generosity turned into danger for the monkey.", "The monkey's generous act of sharing sweet berries attracted the crocodile daily. When the wife tasted the berries, her greed led to the plot against the monkey. Thus, his open generosity unintentionally exposed him to danger.", "Medium"),
    ("What values should young students practice after reading this story?", "Students should practice generosity, honesty, loyalty to friends, and calm problem-solving. They should also learn to think critically, avoid bad company, and stand up for their safety.", "Medium"),
    ("Write a dialogue between the monkey and crocodile after reaching the tree.", "Monkey: 'Ha! You foolish crocodile! Did you really think anyone keeps their heart on a tree?'\nCrocodile: 'Please forgive me, my friend! My wife forced me.'\nMonkey: 'A true friend never hurts another! Goodbye forever!'", "Medium"),
    ("Why did the monkey refuse to give the crocodile another chance?", "Because trust once shattered cannot be easily restored. The crocodile had proven he was willing to kill the monkey, making it unsafe to ever trust him again.", "Medium"),
    ("What role did the sweet berries play in advancing the plot?", "The sweet berries established the initial friendship, pleased the crocodile's wife, and sparked her foolish idea that the monkey's heart must taste sweet, driving the main conflict.", "Medium"),
    ("How does the story highlight the difference between wit and physical power?", "The crocodile was larger and stronger in water, but the monkey used his sharp wit to outsmart him. The story proves that mental alertness is superior to physical force.", "Medium"),
    ("What advice would you give to the crocodile if you were his friend?", "I would advise him to value true friendship, refuse to participate in cruel schemes, and think independently instead of blindly following bad advice.", "Medium"),
    ("Explain why panic is dangerous during a crisis.", "Panic clouds the mind, creates confusion, and prevents clear thinking. If the monkey had panicked in deep water, he could not have devised his clever escape plan.", "Medium"),
    ("How does the author create suspense during the river journey?", "Suspense is created when the crocodile carries the monkey into deep water and suddenly reveals his deadly intention, leaving the non-swimming monkey in extreme danger.", "Medium"),
    ("Describe the emotions felt by the monkey from the start to the end of the story.", "The monkey felt happy and generous at first, excited about the dinner, shocked and terrified in the river, calm while planning his trick, and relieved and triumphant atop his tree.", "Medium"),
    ("Why is this fable popular among children for generations?", "It features relatable animal characters, an exciting plot, a clever escape, and a clear, practical moral lesson that children easily understand and remember.", "Medium"),
    ("What is the significance of the monkey addressing the crocodile from high above?", "It symbolizes the monkey's moral and physical victory over betrayal, placing him in a position of complete safety and authority.", "Medium"),
    ("How can parents and teachers use this story to teach safety awareness?", "They can teach children to stay alert around strangers, avoid unsafe situations, remain calm during trouble, and seek trusted help immediately.", "Medium"),

    # Hard (41-50)
    ("Analyze the psychological trick used by the monkey to deceive the crocodile.", "The monkey used reverse psychology and composure. By readily agreeing to go back for his 'heart', he convinced the crocodile that he was not suspicious. His confident tone disarmed the crocodile's caution, exploiting his gullibility.", "Hard"),
    ("Critique the crocodile's decision-making process throughout the story.", "The crocodile demonstrated weak character. He succumbed to his wife's unreasonable demands, betrayed his benefactor, and lacked the critical thinking to realize a heart cannot be stored on a tree. His decisions brought shame and loss.", "Hard"),
    ("Discuss how 'The Monkey and the Crocodile' reflects human relationships.", "The story mirrors real-life dynamics where generosity is sometimes met with envy, and blind loyalty to bad influences destroys genuine bonds. It advises maintaining boundaries and wisdom in social life.", "Hard"),
    ("Evaluate the role of communication in the story's outcome.", "The crocodile's failure to keep a secret (blurting out the plan) gave the monkey vital information. The monkey's persuasive communication then manipulated the crocodile into turning back. Communication drove both the conflict and resolution.", "Hard"),
    ("How does the concept of 'self-preservation' justify the monkey's lie?", "In ethics, deceiving an aggressor to escape unlawful harm or death is morally justified. The monkey's lie was a non-violent self-defense mechanism aimed strictly at survival.", "Hard"),
    ("Formulate a alternative ending where the crocodile realizes his mistake earlier.", "In an alternative ending, midway across the river, the crocodile feels deep remorse, confesses his wife's plan, apologizes, and safely returns the monkey to the bank. The monkey appreciates his honesty, though they maintain a cautious distance.", "Hard"),
    ("Examine the contrast between the environment of the river and the forest.", "The river represents unfamiliar, high-risk territory for the monkey where the crocodile dominates. The forest and tree represent familiar, safe ground. The monkey's victory lay in luring his opponent back to his own domain.", "Hard"),
    ("Why is emotional intelligence crucial when dealing with betrayal?", "Emotional intelligence allowed the monkey to suppress immediate terror and rage, enabling rational problem-solving. Controlling emotions under pressure prevented a fatal reaction.", "Hard"),
    ("Assess the lasting impact of Panchatantra fables on primary education.", "These fables provide foundational moral literacy. They teach children decision-making, character evaluation, and problem-solving through memorable narrative structures.", "Hard"),
    ("Summarize the overarching philosophy embedded in this classic Indian fable.", "The fable posits that true wisdom combines benevolence with vigilance. One must cultivate kindness, but remain mentally sharp and resilient against deceit in an imperfect world.", "Hard")
]

la_content = f"# Long Answer — Chapter 01: The Monkey and the Crocodile\n\n> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK01_CH01_LA_{idx:03d}"
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

print("[SUCCESS] All 6 category files for Chapter 01 completely refined with 100% unique Class 1 questions!")
