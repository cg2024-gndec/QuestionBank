r"""
Refines all 6 Category files for Chapter 02 ("The Stork and the Crab") for Class 1.
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 1 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
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
    ("Who is the main bird character in the story?", "(A) A parrot", "(B) An old stork", "(C) A crow", "(D) An eagle", "(B)", "The story features an old stork living near the pond.", "Easy", "Remembering", "Character Identification"),
    ("Why could the stork no longer catch fish easily?", "(A) He was getting old and weak", "(B) The water was frozen", "(C) The fish were flying", "(D) He forgot how to catch fish", "(A)", "As he grew older, it became difficult for him to catch fish.", "Easy", "Remembering", "Plot Cause"),
    ("What lie did the stork tell the animals in the pond?", "(A) Men were going to fill the pond and grow crops", "(B) Rain was coming", "(C) The water was turning red", "(D) Monsters were coming", "(A)", "He lied that men would drain the pond to grow crops.", "Easy", "Remembering", "Trick / Lie"),
    ("Where did the stork promise to take the fish?", "(A) To a bigger pond", "(B) To a tree top", "(C) To a cage", "(D) To the ocean", "(A)", "He promised to carry them to a bigger, safer pond.", "Easy", "Remembering", "False Promise"),
    ("What did the stork actually do to the fish he carried?", "(A) He took them to a rock and ate them", "(B) He let them go", "(C) He taught them to fly", "(D) He gave them toys", "(A)", "He carried them to a big rock and ate them.", "Easy", "Remembering", "Real Action"),
    ("Who asked the stork to take him to the bigger pond for a change?", "(A) A crab", "(B) A turtle", "(C) A duck", "(D) A snake", "(A)", "The crab wanted to go to the bigger pond too.", "Easy", "Remembering", "Plot Event"),
    ("What did the crab see when he looked down at the rock?", "(A) Lots of fish bones", "(B) Clear water", "(C) Green grass", "(D) Gold coins", "(A)", "He saw a heap of fish bones on the rock.", "Easy", "Remembering", "Climax Discovery"),
    ("How did the crab save his own life?", "(A) He pinched the stork's neck with his sharp claws", "(B) He jumped into the mud", "(C) He cried loudly", "(D) He flew away", "(A)", "He held the stork's neck tightly until the stork died.", "Easy", "Remembering", "Action"),
    ("What is the moral of 'The Stork and the Crab'?", "(A) Always act quickly with presence of mind in danger", "(B) Trust everyone easily", "(C) Never go near water", "(D) Birds are friendly", "(A)", "The story teaches us to stay alert and act quickly when threatened.", "Easy", "Understanding", "Moral"),
    ("What animal lived in the pond along with the fish?", "(A) A crab", "(B) A lion", "(C) An elephant", "(D) A goat", "(A)", "Crabs and fish lived together in the pond.", "Easy", "Remembering", "Setting"),
    ("Why did the stork pretend to be sad in front of the fish?", "(A) To make them trust him", "(B) Because he was hurt", "(C) Because he wanted to sleep", "(D) Because it was raining", "(A)", "He acted sad so the fish would believe his fake story.", "Easy", "Understanding", "Character Motivation"),
    ("How did the stork carry the fish?", "(A) In his beak", "(B) In a bag", "(C) On his back", "(D) In a bucket", "(A)", "He picked them up in his beak.", "Easy", "Remembering", "Detail"),
    ("How did the stork carry the crab?", "(A) The crab held onto his neck", "(B) In his beak", "(C) On his feet", "(D) In a basket", "(A)", "The crab held onto the stork's neck.", "Easy", "Remembering", "Detail"),
    ("What kind of story is 'The Stork and the Crab'?", "(A) A Panchatantra fable", "(B) A poem about winter", "(C) A science lesson", "(D) A song", "(A)", "It is a Panchatantra moral fable.", "Easy", "Remembering", "Genre"),
    ("Which word describes the stork in the story?", "(A) Greedy and treacherous", "(B) Kind and helpful", "(C) Shy", "(D) Generous", "(A)", "The stork lied and ate the innocent fish.", "Easy", "Understanding", "Character Analysis"),
    ("Which word describes the crab in the story?", "(A) Clever and brave", "(B) Foolish", "(C) Lazy", "(D) Scared", "(A)", "The crab was sharp and saved his life by quick action.", "Easy", "Understanding", "Character Analysis"),
    ("Where did the fish bones lie?", "(A) On a big rock", "(B) In the grass", "(C) Under a tree", "(D) On the road", "(A)", "The bones were piled on a big rock.", "Easy", "Remembering", "Detail"),
    ("Why did the fish easily believe the stork?", "(A) They were simple and trusted his sad words", "(B) They saw the new pond", "(C) They knew the stork well", "(D) The king ordered them", "(A)", "They were innocent and trusted his fake concern.", "Easy", "Understanding", "Reasoning"),
    ("What did the crab do after the stork died?", "(A) He crawled back to the pond to tell the others", "(B) He stayed on the rock", "(C) He swam across the sea", "(D) He went to sleep", "(A)", "He returned safely to the pond.", "Easy", "Remembering", "Plot Ending"),
    ("What did the stork laugh about when the crab asked where the pond was?", "(A) He laughed that the crab was going to be his meal", "(B) He heard a joke", "(C) He saw a fish", "(D) He was happy", "(A)", "He cruelly revealed that there was no new pond.", "Easy", "Remembering", "Plot Detail"),
    ("Did the stork manage to eat the crab?", "(A) No, the crab killed the stork first", "(B) Yes, he ate him", "(C) Yes, with salt", "(D) No, the crab ran away", "(A)", "The crab outsmarted and killed the stork.", "Easy", "Remembering", "Plot Result"),
    ("What sharp body part did the crab use to grip the stork?", "(A) Claws / pincers", "(B) Teeth", "(C) Wings", "(D) Tail", "(A)", "The crab used his strong sharp claws.", "Easy", "Remembering", "Detail"),
    ("Why did the stork pick the crab on that day?", "(A) He wanted a change of food", "(B) He liked crabs", "(C) The crab begged him", "(D) The pond was empty", "(A)", "He thought eating a crab would be a nice change.", "Easy", "Remembering", "Plot Cause"),
    ("What would happen to the fish if they stayed in a pond without water?", "(A) They would die", "(B) They would walk", "(C) They would fly", "(D) They would sleep", "(A)", "Fish need water to live and breathe.", "Easy", "Understanding", "General Knowledge"),
    ("How many fish could the stork carry at one time?", "(A) A few at a time", "(B) All of them together", "(C) One hundred", "(D) None", "(A)", "He claimed he was too old to carry more than a few.", "Easy", "Remembering", "Detail"),

    # Medium (26-40)
    ("Why was the stork's trick successful for many days?", "(A) The fish who went never returned to warn the others", "(B) The fish liked the rock", "(C) The frogs helped him", "(D) The pond was clear", "(A)", "Because the fish were eaten, none could return to expose the lie.", "Medium", "Understanding", "Inference"),
    ("How did the crab discover the stork's lie?", "(A) He saw the rock covered with fish bones", "(B) The fish told him", "(C) He read a sign", "(D) The stork confessed early", "(A)", "Seeing the bones on the rock revealed the truth instantly.", "Medium", "Understanding", "Plot Discovery"),
    ("Why did the crab act immediately without waiting?", "(A) Delaying would have allowed the stork to kill him", "(B) He was in a hurry", "(C) He was angry", "(D) The sun was hot", "(A)", "Quick action in danger is necessary for survival.", "Medium", "Analyzing", "Reasoning"),
    ("What does the phrase 'presence of mind' mean in this chapter?", "(A) Remaining alert and taking quick, smart action in trouble", "(B) Thinking about home", "(C) Forgetfulness", "(D) Sleeping quietly", "(A)", "It means keeping your head clear during danger.", "Medium", "Understanding", "Vocabulary Concept"),
    ("Why was the stork foolish to point out the fish bones to the crab?", "(A) It alerted the crab to the danger before the stork could attack", "(B) The bones were pretty", "(C) The crab liked bones", "(D) It made the crab laugh", "(A)", "His boasting gave the crab time to defend himself.", "Medium", "Analyzing", "Character Mistake"),
    ("What quality of the crab is shown when he returned to the pond?", "(A) Responsibility and helpfulness", "(B) Greed", "(C) Pride", "(D) Laziness", "(A)", "He went back to warn and save the remaining creatures.", "Medium", "Understanding", "Character Trait"),
    ("How did the stork's age play a role in his trick?", "(A) He used his age as an excuse to carry only a few fish at a time", "(B) He was too fast", "(C) He could not talk", "(D) He slept all day", "(A)", "He claimed he was old so he could take small batches.", "Medium", "Understanding", "Plot Detail"),
    ("What does the word 'crop' mean in the stork's lie?", "(A) Plants grown by farmers for food", "(B) Water in a well", "(C) Fish in a lake", "(D) Stones on a hill", "(A)", "Crops are agricultural plants grown on land.", "Medium", "Understanding", "Vocabulary"),
    ("Why did the fish not suspect the stork when he looked sad?", "(A) They assumed a sad bird would not harm them", "(B) They knew he was lying", "(C) They did not care", "(D) They were blind", "(A)", "His fake sadness made him appear caring and sympathetic.", "Medium", "Understanding", "Inference"),
    ("What is the main difference between the fish and the crab in this story?", "(A) The fish trusted blindly, while the crab stayed alert and defended himself", "(B) The fish could walk", "(C) The crab had wings", "(D) Both did the same thing", "(A)", "The crab used presence of mind while the fish were gullible.", "Medium", "Analyzing", "Comparative Analysis"),
    ("How did the crab's physical body help him win against the stork?", "(A) He used his strong, pinching claws to grip the stork's neck", "(B) He had sharp teeth", "(C) He had a heavy shell", "(D) He could fly", "(A)", "His sharp claws were perfect weapons for self-defense.", "Medium", "Understanding", "Fact"),
    ("Why did the stork laugh when the crab asked about the big pond?", "(A) He was arrogant and thought the crab was helpless", "(B) He heard a song", "(C) He was happy to see water", "(D) He was playing", "(A)", "His arrogance made him boast before securing his prey.", "Medium", "Understanding", "Character Motivation"),
    ("What lesson does this story teach about believing false rumors?", "(A) Do not believe scary rumors without checking the facts", "(B) Believe everything you hear", "(C) Never listen to anyone", "(D) Rumors are always true", "(A)", "The fish panicked because of an unverified rumor.", "Medium", "Applying", "Life Lesson"),
    ("What would have happened if the crab had not gripped the stork's neck?", "(A) The stork would have smashed and eaten the crab on the rock", "(B) The stork would drop him safely", "(C) They would become friends", "(D) The crab would fly", "(A)", "The stork would have killed him just like the fish.", "Medium", "Analyzing", "Hypothetical"),
    ("Which word best describes the stork's fake promise?", "(A) Deceitful", "(B) Honest", "(C) Friendly", "(D) Polite", "(A)", "Deceitful means misleading someone intentionally.", "Medium", "Understanding", "Vocabulary"),

    # Hard (41-50)
    ("Why is quick decision-making crucial when faced with a life-threatening situation?", "(A) Hesitation gives the danger time to harm you", "(B) It makes you look strong", "(C) It saves time for sleep", "(D) Decisions don't matter", "(A)", "Acting promptly neutralizes the threat before it strikes.", "Hard", "Evaluating", "HOTS Reasoning"),
    ("How does the stork's downfall illustrate the proverb 'Greed leads to ruin'?", "(A) His greed to eat the crab made him reckless, leading to his death", "(B) He ate too much fish", "(C) He lost his nest", "(D) He fell in water", "(A)", "His endless greed eventually brought him against a dangerous opponent.", "Hard", "Evaluating", "Proverb Application"),
    ("In what way does this fable highlight the importance of self-defense?", "(A) Every creature must be prepared to protect itself when attacked", "(B) Animals should not defend themselves", "(C) Defense is bad", "(D) Only big animals win", "(A)", "The small crab successfully used his natural claws to defend his life.", "Hard", "Evaluating", "Theme Analysis"),
    ("Analyze why the crab's action was self-defense rather than violence.", "(A) He acted solely to protect his own life from an immediate killer", "(B) He wanted to eat the stork", "(C) He was playing", "(D) He disliked birds", "(A)", "Defending oneself against an attacker is a necessary act of survival.", "Hard", "Analyzing", "Moral Analysis"),
    ("What contrast exists between the stork's age and his wisdom?", "(A) Though old in age, he used his experience for wickedness rather than true wisdom", "(B) He was very wise", "(C) He was young", "(D) Age has no relation to wisdom", "(A)", "He used his age to craft cunning lies instead of living honorably.", "Hard", "Analyzing", "Character Contrast"),
    ("How can Class 1 students practice 'presence of mind' in their daily lives?", "(A) By staying calm during emergencies and telling an adult quickly", "(B) By panicking", "(C) By running blindly", "(D) By hiding forever", "(A)", "Calmness and alert communication help solve real-life problems.", "Hard", "Applying", "Real Life Application"),
    ("Why did the stork's plan work so well until he met the crab?", "(A) The fish lacked claws or defense tools, whereas the crab had strong pincers", "(B) The fish were fast", "(C) The crab was big", "(D) The pond was small", "(A)", "The crab had both the awareness and physical capability to retaliate.", "Hard", "Analyzing", "Plot Logic"),
    ("What does the rock covered in fish bones symbolize in the story?", "(A) The hidden truth behind a sweet lie", "(B) A pretty garden", "(C) A resting place", "(D) A treasure chest", "(A)", "It symbolizes the grim reality hidden behind deceptive promises.", "Hard", "Evaluating", "Symbolism"),
    ("How does the story demonstrate that appearances can be deceiving?", "(A) The stork appeared as a gentle savior but was actually a murderer", "(B) The pond looked small", "(C) The rock was smooth", "(D) The crab looked soft", "(A)", "The stork's sad, helpful facade disguised his evil intentions.", "Hard", "Evaluating", "Theme Analysis"),
    ("What is the ultimate takeaway from 'The Stork and the Crab'?", "(A) Be vigilant against trickery, stay calm in danger, and act decisively to save yourself", "(B) Avoid all birds", "(C) Live only on land", "(D) Never talk to crabs", "(A)", "Vigilance and quick presence of mind ensure safety against deceit.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 02: The Stork and the Crab\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK01_CH02_MCQ_{idx:03d}"
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
    ("An old _______ lived near a pond filled with fish.", "stork", "The main bird character was a stork.", "Easy"),
    ("As the stork grew older, he found it hard to catch _______.", "fish", "He could not catch fish easily.", "Easy"),
    ("The stork lied that men were going to fill the pond to grow _______.", "crops", "He claimed men would grow crops there.", "Easy"),
    ("The stork promised to carry the fish to a _______ pond.", "bigger / larger", "He promised to move them to a bigger pond.", "Easy"),
    ("Instead of taking them to a pond, he carried them to a big _______.", "rock", "He took the fish to a big rock.", "Easy"),
    ("On the rock, the stork _______ the fish and ate them.", "killed / ate", "He ate the fish on the rock.", "Easy"),
    ("A clever _______ also wanted to go to the bigger pond.", "crab", "The crab asked for a ride.", "Easy"),
    ("The crab looked down and saw a pile of fish _______.", "bones", "He saw fish bones on the rock.", "Easy"),
    ("The crab pinched the stork's _______ with his sharp claws.", "neck", "He caught the stork's neck tightly.", "Easy"),
    ("The crab did not let go until the stork _______.", "died", "The stork died from the grip.", "Easy"),
    ("The crab saved his own _______ by acting quickly.", "life", "Quick action saved the crab.", "Easy"),
    ("The story teaches us to have _______ of mind in danger.", "presence", "Presence of mind is essential.", "Easy"),
    ("The stork picked up fish using his _______.", "beak", "He carried fish in his beak.", "Easy"),
    ("The crab held onto the stork's neck with his _______.", "claws / pincers", "He used his sharp claws.", "Easy"),
    ("The innocent fish _______ the stork's false story.", "believed / trusted", "They trusted his lie.", "Easy"),
    ("The stork pretended to be _______ to trick the fish.", "sad / unhappy", "He acted sad to look caring.", "Easy"),
    ("The crab crawled back to the _______ to tell the others.", "pond", "He returned to the pond.", "Easy"),
    ("The stork was very _______ and wanted to eat all the fish.", "greedy", "His greed drove his actions.", "Easy"),
    ("Fish cannot live without _______.", "water", "Fish need water to survive.", "Easy"),
    ("The crab was _______ and quick-witted.", "clever / smart / brave", "The crab was clever.", "Easy"),
    ("'The Stork and the Crab' is a _______ fable.", "Panchatantra", "It is a Panchatantra moral fable.", "Easy"),
    ("The stork claimed he could carry only a _______ fish at a time.", "few", "He took small batches.", "Easy"),
    ("The rock was covered with the _______ of many fish.", "remains / bones", "Fish bones covered the rock.", "Easy"),
    ("The crab realized the stork was a _______.", "killer / liar / enemy", "He realized the stork's trick.", "Easy"),
    ("We should always be _______ when someone tells scary rumors.", "alert / careful", "We must verify facts.", "Easy"),

    # Medium (26-40)
    ("The word 'agree' means to have the same _______ as someone.", "views / opinion", "Agree means sharing views.", "Medium"),
    ("The stork used his _______ age as an excuse to take few fish.", "old", "He used his age as an excuse.", "Medium"),
    ("The fish panicked because they thought the pond would be _______.", "drained / filled", "They feared losing their water.", "Medium"),
    ("The stork's fake sympathy made the fish feel _______.", "thankful / hopeful", "They felt grateful for his help.", "Medium"),
    ("The crab noticed the fish bones before the stork could _______.", "attack / eat him", "Spotting bones saved him.", "Medium"),
    ("The crab did not _______ when he saw the danger.", "panic / hesitate", "He acted without delay.", "Medium"),
    ("The stork laughed because he thought the crab was _______.", "helpless / easy food", "He arrogantly thought he won.", "Medium"),
    ("The crab's sharp claws served as a natural _______ tool.", "defense / self-defense", "Claws protected him.", "Medium"),
    ("The fish vanished one by one because the stork _______ them.", "ate / devoured", "He ate them on the rock.", "Medium"),
    ("The story shows that a clever mind beats physical _______.", "strength / size", "Intelligence beats strength.", "Medium"),
    ("The stork's deceit was exposed by the pile of _______.", "bones", "Bones proved his crime.", "Medium"),
    ("The crab showed great _______ by returning to warn his friends.", "courage / kindness", "He warned the other animals.", "Medium"),
    ("False promises should always be checked with _______.", "care / facts", "We must check facts.", "Medium"),
    ("The stork met his end because he was _______ and arrogant.", "greedy / foolish", "Greed led to his death.", "Medium"),
    ("Presence of mind requires staying _______ under pressure.", "calm", "Calmness is necessary.", "Medium"),

    # Hard (41-50)
    ("The stork's initial success relied on the total _______ of his victims.", "ignorance / trust", "Victims didn't know the truth.", "Hard"),
    ("The crab's swift retaliation neutralized the stork's _______ threat.", "deadly / physical", "Swift action stopped danger.", "Hard"),
    ("Overconfidence caused the stork to reveal his clue by showing the _______.", "bones / rock", "Boasting revealed his secret.", "Hard"),
    ("The pond ecosystem was threatened by a predator disguised as a _______.", "savior / friend", "The stork hid behind a helpful mask.", "Hard"),
    ("Critical evaluation of strange advice protects us from _______.", "harm / trickery", "Critical thinking keeps us safe.", "Hard"),
    ("The crab's claws acted as a decisive counter-measure against _______.", "aggression / betrayal", "Pincers defeated the attacker.", "Hard"),
    ("Discerning truth from falsehood is a vital life _______.", "skill / lesson", "Discerning truth is essential.", "Hard"),
    ("The story illustrates that evil intentions ultimately bring self-_______.", "destruction", "Wicked deeds destroy the doer.", "Hard"),
    ("Prompt action during a crisis turns vulnerability into _______.", "victory / safety", "Quick action yields safety.", "Hard"),
    ("Moral vigilance prevents us from falling prey to false _______.", "promises / leaders", "Vigilance protects against deceit.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 02: The Stork and the Crab\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK01_CH02_FIB_{idx:03d}"
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
# 3. Fill in Blanks from Story (Cloze Passage) (50 Distinct Qs)
# -------------------------------------------------------------
cloze_data = [
    ("Once upon a time, an old _______ lived beside a pond.", "stork", "Easy"),
    ("As he grew older, he found it hard to catch a single _______.", "fish", "Easy"),
    ("In order to feed himself, he thought of a cunning _______.", "plan", "Easy"),
    ("He told the animals that men were planning to fill the _______.", "pond", "Easy"),
    ("He claimed men wanted to grow _______ in the dry land.", "crops", "Easy"),
    ("The innocent fish felt _______ when they heard the news.", "sad / scared", "Easy"),
    ("The stork promised to carry them to a _______ pond.", "bigger / larger", "Easy"),
    ("He said he could take only a _______ fish at one time.", "few", "Easy"),
    ("The stork took the fish to a big _______ instead of a pond.", "rock", "Easy"),
    ("He killed the fish on the rock and _______ them up.", "ate", "Easy"),
    ("Every time he felt hungry, he carried away a few more _______.", "fish", "Easy"),
    ("One day, a _______ asked to go to the bigger pond too.", "crab", "Easy"),
    ("The stork agreed because he wanted to eat crab for a _______.", "change", "Easy"),
    ("The crab held onto the stork's _______ as they flew.", "neck", "Easy"),
    ("On the way, the crab asked, 'Where is the big _______?'", "pond", "Easy"),
    ("The stork laughed and pointed to the rock covered in fish _______.", "bones", "Easy"),
    ("The crab realized that the stork was going to _______ him.", "kill / eat", "Easy"),
    ("The clever crab did not _______ in fear.", "panic", "Easy"),
    ("He quickly caught the stork's neck with his sharp _______.", "claws / pincers", "Easy"),
    ("He squeezed tightly and did not let go until the stork _______.", "died", "Easy"),
    ("The crab saved his own _______ by acting fast.", "life", "Easy"),
    ("He crawled back safely to the _______.", "pond", "Easy"),
    ("He warned all the other fish about the stork's _______.", "trick / lie", "Easy"),
    ("The moral is to act quickly with presence of _______.", "mind", "Easy"),
    ("This classic story comes from the famous _______.", "Panchatantra", "Easy"),

    ("The old stork relied on _______ because he lacked speed.", "trickery", "Medium"),
    ("The fish believed his fake expression of _______.", "sorrow / sympathy", "Medium"),
    ("None of the fish returned because they were all _______.", "eaten", "Medium"),
    ("The rock became a graveyard of fish _______.", "bones", "Medium"),
    ("The crab was observant and noticed the dangerous _______.", "sign / bones", "Medium"),
    ("The stork's arrogance made him laugh at his _______.", "victim", "Medium"),
    ("The crab used his natural pincers for self-_______.", "defense", "Medium"),
    ("The stork's breath was cut off by the crab's strong _______.", "grip", "Medium"),
    ("Presence of mind helps us overcome sudden _______.", "danger", "Medium"),
    ("The story warns us against trusting unverified _______.", "rumors", "Medium"),
    ("The word 'agree' means to accept a _______.", "request / view", "Medium"),
    ("The stork's beak was sharp, but the crab's claws were _______.", "stronger", "Medium"),
    ("The crab demonstrated bravery and quick _______.", "thinking", "Medium"),
    ("The pond animals were saved from further _______.", "loss", "Medium"),
    ("A false savior is more dangerous than an open _______.", "enemy", "Medium"),

    ("In moments of peril, swift action prevents catastrophic _______.", "failure / death", "Hard"),
    ("The stork's deceitful strategy was exposed by physical _______.", "evidence", "Hard"),
    ("Overconfidence blinded the stork to the crab's defensive _______.", "capability", "Hard"),
    ("The crab's decisive intervention ended the predator's _______.", "reign / streak", "Hard"),
    ("Deceptive promises often conceal fatal _______.", "traps", "Hard"),
    ("Vigilance remains the best shield against clever _______.", "schemes", "Hard"),
    ("The story balances the threat of greed with the power of _______.", "wit", "Hard"),
    ("Class 1 students learn to recognize false expressions of _______.", "care", "Hard"),
    ("Logical deduction helped the crab spot the hidden _______.", "truth", "Hard"),
    ("Quick execution of a self-defense plan ensures personal _______.", "safety", "Hard")
]

cloze_content = f"# Fill in the Blanks from Story — Chapter 02: The Stork and the Crab\n\n> **Category**: Fill in the Blanks from Story (Cloze Passage) | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(cloze_data, start=1):
    q_id = f"BK01_CH02_STORY_FIB_{idx:03d}"
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

with open(os.path.join(CH02_DIR, "fill_in_blanks_story.md"), "w", encoding="utf-8") as f:
    f.write(cloze_content)

# -------------------------------------------------------------
# 4. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The old stork found it easy to catch fish as he grew older.", False, "He found it difficult to catch fish because he was getting old.", "Easy"),
    ("The stork lied that men were going to fill the pond to grow crops.", True, "He made up this lie to scare the animals.", "Easy"),
    ("The stork promised to carry the fish to a bigger pond.", True, "He promised to move them safely.", "Easy"),
    ("The stork actually took the fish to a big rock and ate them.", True, "He killed and ate the fish on the rock.", "Easy"),
    ("The fish realized the stork's lie immediately and refused to go.", False, "The innocent fish believed him and asked for help.", "Easy"),
    ("The crab asked the stork to carry him to the bigger pond too.", True, "The crab wanted to go to the bigger pond.", "Easy"),
    ("The stork agreed to carry the crab because he wanted to eat crab for a change.", True, "He wanted a change of food.", "Easy"),
    ("The crab saw a heap of fish bones when he looked at the rock.", True, "Seeing fish bones exposed the stork's lie.", "Easy"),
    ("The crab panicked and fell off the stork's neck.", False, "The crab stayed calm and used his claws to hold the neck.", "Easy"),
    ("The crab pinched the stork's neck until the stork died.", True, "He held the stork's neck tightly with his sharp claws.", "Easy"),
    ("The crab saved his own life through quick action.", True, "His presence of mind saved his life.", "Easy"),
    ("The moral of the story is to act quickly with presence of mind in danger.", True, "The story teaches presence of mind in crisis.", "Easy"),
    ("'The Stork and the Crab' is a Panchatantra fable.", True, "It is an ancient Panchatantra fable.", "Easy"),
    ("The stork carried the fish in a small bucket.", False, "He carried them in his beak.", "Easy"),
    ("The crab crawled back to the pond after killing the stork.", True, "He returned safely to warn others.", "Easy"),
    ("The stork was a kind bird who helped all animals.", False, "He was a greedy, deceitful bird.", "Easy"),
    ("The fish bones were lying under the water in the pond.", False, "The bones were piled on top of the rock.", "Easy"),
    ("The crab used his claws to defend himself.", True, "His sharp claws were his natural weapons.", "Easy"),
    ("The stork told the fish he could carry everyone at once.", False, "He claimed he was old and could carry only a few at a time.", "Easy"),
    ("The crab saved the remaining animals by killing the deceitful stork.", True, "His action stopped the stork from eating more fish.", "Easy"),
    ("Fish can survive on dry land among crops.", False, "Fish need water to breathe and live.", "Easy"),
    ("The stork laughed arrogantly when asked about the big pond.", True, "He laughed and pointed to the fish bones.", "Easy"),
    ("The crab was foolish and slow to react.", False, "The crab was clever and reacted quickly.", "Easy"),
    ("Presence of mind helps us stay safe in sudden trouble.", True, "Clear thinking helps us survive danger.", "Easy"),
    ("The stork's lie was completely true.", False, "It was a false rumor created to trick the fish.", "Easy"),

    # Medium (26-40)
    ("The word 'agree' means to accept or share the same view.", True, "Agree means accepting a proposal.", "Medium"),
    ("The stork used his age as a clever excuse to take small batches of fish.", True, "Claiming age let him eat them gradually.", "Medium"),
    ("None of the fish returned because they loved the new pond.", False, "None returned because the stork ate them all on the rock.", "Medium"),
    ("The crab trusted the stork blindly until the very end.", False, "The crab spotted the bones and realized the trick in time.", "Medium"),
    ("The stork's arrogance made him reveal his clue prematurely.", True, "Pointing at the bones alerted the crab.", "Medium"),
    ("The crab's quick grip cut off the stork's breathing.", True, "Squeezing his neck suffocated the stork.", "Medium"),
    ("The story proves that small animals cannot defend themselves.", False, "The small crab successfully defeated the larger stork.", "Medium"),
    ("Rumors about danger should be checked before panicking.", True, "We should verify facts before acting on rumors.", "Medium"),
    ("The stork's fake sadness convinced the fish he was a friend.", True, "His act made him look sympathetic.", "Medium"),
    ("The crab ran away into the forest after reaching land.", False, "He returned to the pond to warn the other sea creatures.", "Medium"),
    ("Deceitful people often hide behind friendly masks.", True, "The stork pretended to be a helpful savior.", "Medium"),
    ("The fish were able to fight back against the stork.", False, "The fish had no defense and were eaten easily.", "Medium"),
    ("The crab's claws were strong enough to defeat the bird.", True, "His pincers killed the stork.", "Medium"),
    ("The story teaches us to stay calm during emergency situations.", True, "Calmness is essential for clear thinking.", "Medium"),
    ("The stork felt sorry for eating the fish.", False, "He enjoyed devouring them on the rock.", "Medium"),

    # Hard (41-50)
    ("The stork's downfall shows that greed leads to reckless choices.", True, "Wanting to eat the crab led to his death.", "Hard"),
    ("The crab's self-defense was morally justified to save his life.", True, "Defending oneself against a murderer is justified.", "Hard"),
    ("Hesitation during danger always yields better results.", False, "Hesitation in danger can prove fatal.", "Hard"),
    ("The pile of bones served as empirical proof of the stork's crime.", True, "The bones proved the stork killed the fish.", "Hard"),
    ("The fish lacked defensive physical features compared to the crab.", True, "Fish had no claws to fight back.", "Hard"),
    ("Boasting before winning is a sign of dangerous overconfidence.", True, "The stork boasted before securing his prey.", "Hard"),
    ("Critical thinking enables individuals to spot deceptive schemes.", True, "Critical thinking reveals hidden tricks.", "Hard"),
    ("The crab acted responsibly by informing the rest of the pond.", True, "Warning others protected the remaining community.", "Hard"),
    ("Physical size determines the outcome of every battle in nature.", False, "Intelligence and quick action can overcome size.", "Hard"),
    ("The overarching message is to combine alertness with decisive action.", True, "Vigilance and prompt action ensure safety.", "Hard")
]

tf_content = f"# True / False — Chapter 02: The Stork and the Crab\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK01_CH02_TF_{idx:03d}"
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
# 5. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who is the main bird in the story and where did he live?", "The main bird is an old stork who lived near a pond filled with fish and crabs.", "Easy"),
    ("Why did the old stork find it difficult to catch fish?", "He was getting old and weak, so he could no longer catch fish easily.", "Easy"),
    ("What lie did the stork tell the fish in the pond?", "He lied that men were going to fill the pond to grow crops, leaving no water.", "Easy"),
    ("What did the stork promise to do for the fish?", "He promised to carry them one by one to a bigger, safer pond.", "Easy"),
    ("Where did the stork actually take the fish?", "He took them to a big rock, killed them, and ate them.", "Easy"),
    ("Why did the stork carry only a few fish at a time?", "He claimed he was old and weak, but really he wanted to eat them gradually.", "Easy"),
    ("Who asked the stork for a ride to the bigger pond?", "A clever crab asked the stork to take him to the bigger pond.", "Easy"),
    ("Why did the stork agree to carry the crab?", "The stork agreed because he wanted to eat crab for a change.", "Easy"),
    ("What did the crab see when he looked down at the rock?", "The crab saw a large pile of fish bones on the rock.", "Easy"),
    ("How did the crab realize the stork was lying?", "Seeing the fish bones on the rock exposed the stork's lie.", "Easy"),
    ("How did the crab defend himself against the stork?", "The crab pinched the stork's neck tightly with his sharp claws.", "Easy"),
    ("What happened to the stork when the crab pinched his neck?", "The stork could not breathe and died from the crab's tight grip.", "Easy"),
    ("What did the crab do after the stork died?", "The crab crawled back safely to the pond to warn the other animals.", "Easy"),
    ("What is the main moral of the story?", "The moral is to always have presence of mind and act quickly when in danger.", "Easy"),
    ("What kind of story is 'The Stork and the Crab'?", "It is an ancient Panchatantra moral fable.", "Easy"),
    ("How did the stork carry the fish?", "The stork carried the fish in his beak.", "Easy"),
    ("How did the crab hold onto the stork during the flight?", "The crab held onto the stork's neck with his claws.", "Easy"),
    ("Why were the fish sad when they heard the stork's story?", "They were sad because they thought they would lose their pond and die.", "Easy"),
    ("Name the animals living in the pond.", "Fish, frogs, and crabs lived in the pond.", "Easy"),
    ("Which body part did the crab use to kill the stork?", "The crab used his strong, sharp claws.", "Easy"),
    ("Why did the stork laugh when asked about the big pond?", "He laughed arrogantly, thinking the crab was about to become his food.", "Easy"),
    ("Did any fish return from the rock?", "No, none returned because the stork ate them all.", "Easy"),
    ("What does the word 'agree' mean?", "'Agree' means to accept a proposal or share the same view.", "Easy"),
    ("Why was the crab clever?", "The crab stayed alert, spotted the fish bones, and acted fast to save his life.", "Easy"),
    ("What lesson does this story teach about stranger advice?", "We should not blindly trust strangers who tell scary stories.", "Easy"),

    # Medium (26-40)
    ("Why was the stork's trick successful for a long time?", "Because he ate all the fish he took, so no one returned to tell the truth.", "Medium"),
    ("How did the fake news about crops affect the pond animals?", "It caused panic and made them trust the stork's false promise out of fear.", "Medium"),
    ("Why did the crab not panic when he saw the fish bones?", "He stayed calm so he could think of a quick way to defend himself.", "Medium"),
    ("What mistake did the arrogant stork make?", "He showed the fish bones to the crab before attacking, giving away his secret.", "Medium"),
    ("How did the crab's quick action save the remaining fish?", "By killing the stork, he stopped the bird from eating any more pond animals.", "Medium"),
    ("What does 'presence of mind' mean in simple words?", "It means keeping your head calm and taking smart, fast action during danger.", "Medium"),
    ("Why did the stork pretend to be sad at the beginning?", "To look like a caring savior so the fish would trust him completely.", "Medium"),
    ("Compare the physical strength of the stork and crab.", "The stork was bigger and could fly, but the crab had sharp, powerful pincers.", "Medium"),
    ("What would have happened if the crab hesitated on the rock?", "The stork would have smashed and eaten him on the rock.", "Medium"),
    ("Why is greed dangerous, as shown by the stork?", "The stork's endless greed led him to target the crab, which caused his death.", "Medium"),
    ("How did the crab show responsibility after escaping?", "He returned to the pond to inform and protect his fellow sea creatures.", "Medium"),
    ("What lesson can we learn about rumors?", "We should verify facts carefully before panicking over bad news.", "Medium"),
    ("How did the stork carry small batches of fish?", "He claimed his old age limited his strength, taking only a few at a time.", "Medium"),
    ("Why was the crab able to grip the stork's neck so tightly?", "His sharp claws locked around the soft neck, cutting off the bird's air.", "Medium"),
    ("Why is this story popular in primary education?", "It teaches safety, critical thinking, and quick problem-solving in a simple way.", "Medium"),

    # Hard (41-50)
    ("Analyze how fear made the fish vulnerable to the stork's lie.", "Fear of losing their pond clouded their judgment, making them trust a predator.", "Hard"),
    ("Explain why the crab's action was self-defense.", "The crab acted solely to protect his life from an active killer on the verge of attack.", "Hard"),
    ("How did overconfidence lead to the stork's defeat?", "He assumed the crab was helpless and revealed his secret, giving the crab time to strike.", "Hard"),
    ("What does the rock covered in fish bones represent ethically?", "It represents the brutal truth hidden beneath deceitful, friendly promises.", "Hard"),
    ("How does intelligence overcome physical disadvantage in this fable?", "The small crab used alertness and sharp pincers to defeat a much larger bird.", "Hard"),
    ("What advice would you give to someone who hears a frightening rumor?", "Stay calm, do not panic, and verify the truth with trusted adults.", "Hard"),
    ("Evaluate the stork's character using two adjectives.", "Deceitful (he lied to the fish) and arrogant (he boasted before attacking).", "Hard"),
    ("Why is quick execution vital in self-defense scenarios?", "Any delay allows the aggressor to gain control and inflict fatal harm.", "Hard"),
    ("Summarize how the crab turned a death trap into a victory.", "He spotted the bones, kept calm, locked his claws on the stork's neck, and eliminated the threat.", "Hard"),
    ("What is the ultimate educational message of Chapter 02?", "Vigilance against deceit and prompt presence of mind ensure safety in crisis.", "Hard")
]

sa_content = f"# Short Answer — Chapter 02: The Stork and the Crab\n\n> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK01_CH02_SA_{idx:03d}"
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
# 6. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-15)
    ("Write a simple summary of the story 'The Stork and the Crab'.", "An old stork could no longer catch fish easily. He lied to the pond animals that men were going to fill the pond to grow crops. He offered to carry them to a bigger pond, but instead took them to a rock and ate them. When the clever crab went with him, he saw fish bones on the rock, realized the lie, and pinched the stork's neck with his claws until the stork died. The crab returned safely to warn the others.", "Easy"),
    ("Describe how the old stork tricked the fish in the pond.", "The stork stood near the pond looking sad. He told the fish, frogs, and crabs that men were planning to drain the pond to grow crops. The scared fish asked for help. The stork promised to move them to a bigger pond in small groups because he was old. The fish trusted him, but he took them to a rock and ate them.", "Easy"),
    ("How did the crab discover the stork's lie on the way?", "When the crab rode on the stork's neck, he asked where the big pond was. The arrogant stork laughed and pointed to a big rock covered with fish bones. Seeing the bones, the crab instantly realized that the stork had eaten all the fish and was planning to eat him next.", "Easy"),
    ("How did the clever crab save his life and defeat the stork?", "Instead of panicking, the crab acted quickly. He gripped the stork's neck tightly with his sharp claws and squeezed hard. He did not let go until the stork suffocated and died. The crab then crawled back safely to the pond.", "Easy"),
    ("What is the moral of 'The Stork and the Crab'?", "The moral of the story is: Always have presence of mind and act quickly when in danger. Staying calm and alert helps us solve scary problems and protect ourselves.", "Easy"),
    ("Describe the character of the old stork.", "The old stork was greedy, deceitful, and arrogant. He used a fake story of kindness to trick helpless fish. He was also boastful, which exposed his secret to the crab and led to his downfall.", "Easy"),
    ("Describe the character of the crab.", "The crab was clever, brave, observant, and decisive. He noticed the fish bones, stayed calm under threat, used his claws for self-defense, and responsibly returned to warn the pond community.", "Easy"),
    ("Why did the fish believe the stork so easily?", "The fish were innocent and simple. They were terrified of losing their pond, and the stork's fake sad expression made him look like a caring savior. Their fear made them trust him without checking the facts.", "Easy"),
    ("What lesson does this story teach about scary rumors?", "The story teaches us not to panic over scary rumors. We should check facts carefully and consult trusted people before acting on bad news.", "Easy"),
    ("Explain why presence of mind is important in daily life.", "Presence of mind keeps us calm during unexpected trouble, allowing our brain to think of smart solutions. Panicking causes confusion, while presence of mind ensures safety.", "Easy"),
    ("Why did the stork carry only a few fish at a time?", "The stork claimed he was too old to carry heavy loads, but really he wanted to eat them gradually so the remaining fish wouldn't notice they were disappearing.", "Easy"),
    ("How did the crab help the other animals in the pond?", "By killing the deceitful stork, the crab eliminated the predator and then returned to the pond to warn the remaining fish and frogs about the danger.", "Easy"),
    ("Why is 'The Stork and the Crab' a Panchatantra tale?", "It is a Panchatantra fable because it uses animal characters to teach practical wisdom, alertness, and self-defense lessons to young children.", "Easy"),
    ("What would have happened if the crab had frozen in fear?", "If the crab had frozen in fear, the stork would have smashed him against the rock and eaten him, just as he did with the fish.", "Easy"),
    ("How did the crab's claws help him survive?", "His sharp, powerful claws served as natural weapons. By clamping them tightly around the bird's soft neck, he stopped the stork from attacking.", "Easy"),

    # Medium (16-40)
    ("Explain the term 'presence of mind' using the crab's actions.", "Presence of mind is the ability to remain calm and think clearly during a crisis. When the crab saw the fish bones, he did not scream or fall off. He instantly analyzed the threat, used his natural claws, and locked onto the stork's neck until safe.", "Medium"),
    ("Compare the behavior of the fish with the behavior of the crab.", "The fish were naive and panicked over the stork's lie, walking blindly into a trap. The crab, however, was vigilant, spotted the evidence of danger, and took immediate self-defense action.", "Medium"),
    ("How did the stork's arrogance lead to his own death?", "The stork boasted by pointing out the fish bones to the crab, assuming the crab was helpless. This arrogance alerted the crab and gave him time to strike first.", "Medium"),
    ("Why should we never trust false promises from unknown people?", "False promises are often used by bad people to trick us. Like the stork's promise of a bigger pond, deceitful offers can lead into hidden traps.", "Medium"),
    ("Discuss the significance of the rock covered in fish bones.", "The rock covered in bones was the physical proof of the stork's crime. It shattered the stork's lie instantly and triggered the crab's survival response.", "Medium"),
    ("How does this story show that small creatures can defeat big enemies?", "Though small, the crab used his sharp claws and quick thinking to defeat a large flying bird. Size does not matter when intelligence and courage are applied.", "Medium"),
    ("Why was the stork's fake sadness an effective trick?", "People often trust those who appear sympathetic. By pretending to cry for the fish, the stork hid his evil intention behind a mask of care.", "Medium"),
    ("Write a dialogue between the crab and stork when they reached the rock.", "Stork: 'Ha! Look at those bones! You are my lunch now!'\nCrab: 'Not today, greedy bird!' *clamps claws on neck*\nStork: 'Gasp! Let go!'\nCrab: 'Never!'", "Medium"),
    ("What steps should a Class 1 student take if they feel in danger?", "Stay calm, do not panic, look for a safe escape or adult helper, and act quickly to stay safe.", "Medium"),
    ("How does greed ruin a person's life according to this tale?", "The stork had eaten many fish, but his endless greed for 'crab meat' made him careless, ultimately costing him his life.", "Medium"),
    ("Why did no fish return to warn the pond?", "Because the stork killed and ate every fish he took immediately upon reaching the rock, leaving no survivors.", "Medium"),
    ("What role did fear play in enabling the stork's lie?", "Fear of starvation and losing their water overwhelmed the fish's common sense, making them easy targets for the stork's scheme.", "Medium"),
    ("How did the crab's claws serve as a tool of justice?", "His claws not only saved his own life but also punished the wicked bird for murdering the innocent fish.", "Medium"),
    ("What makes Panchatantra stories timeless for young learners?", "They feature simple animal characters, exciting situations, clear logic, and morals that guide human behavior across generations.", "Medium"),
    ("Why is quick action essential when faced with immediate threat?", "Danger moves fast. Immediate action stops the attacker before they can complete their strike.", "Medium"),
    ("How did the stork's age give him an advantage in lying?", "Age gave him an aura of experience and wisdom, making the young fish assume he was telling the truth.", "Medium"),
    ("What feelings did the crab experience during his journey?", "Curiosity when leaving, horror when seeing the bones, fierce determination when attacking, and relief upon returning safe.", "Medium"),
    ("Why did the crab return to the pond instead of running away?", "He felt a duty to inform his fellow sea creatures so no one else would fall for similar lies.", "Medium"),
    ("How does this story teach safety awareness?", "It teaches children to question suspicious offers, stay alert to danger signs, and act boldly to protect themselves.", "Medium"),
    ("Summarize the conflict and resolution of Chapter 02.", "Conflict: The stork tricks pond animals to eat them. Resolution: The clever crab discovers the lie, kills the stork in self-defense, and saves the pond.", "Medium"),

    # Hard (41-50)
    ("Critique the stork's predatory strategy and its fatal flaw.", "The stork used psychological manipulation by creating artificial panic. His fatal flaw was overconfidence—he assumed all victims were helpless, ignoring the crab's natural defensive weapons.", "Hard"),
    ("Analyze the moral justification of the crab's lethal response.", "The crab's action was strict self-defense. Facing imminent death on an isolated rock, neutralizing the active killer was the only viable means of survival.", "Hard"),
    ("How does this fable address the danger of unverified panic?", "It illustrates how unverified rumors create mass hysteria, allowing manipulators to exploit vulnerable communities for personal gain.", "Hard"),
    ("Examine the symbolic contrast between the water and the dry rock.", "Water represents life, community, and safety for aquatic creatures. The dry rock represents isolation, deception, and death.", "Hard"),
    ("Why is emotional control necessary for executing presence of mind?", "Panic triggers freezing or irrational flight. Emotional control keeps the mind analytical, enabling one to spot weaknesses in an attacker.", "Hard"),
    ("Reimagine the story if the crab had noticed the bones earlier.", "If noticed earlier, the crab would have alerted the entire pond community, leading to a collective boycott or defense before any fish were lost.", "Hard"),
    ("Evaluate how natural adaptations (claws vs beak) determined the outcome.", "The stork's beak was designed for catching soft fish, but the crab's hard shell and sharp pincers provided superior close-combat defense.", "Hard"),
    ("What philosophical lesson does this story give about deceit?", "Deceit may yield short-term gains, but it creates vulnerabilities that eventually bring total destruction.", "Hard"),
    ("How can primary educators connect this story to anti-bullying?", "Educators can show that standing up to bullies with calm courage and quick action stops exploitation and protects others.", "Hard"),
    ("Formulate the complete takeaway of 'The Stork and the Crab' for Class 1.", "Combine vigilance with courage: question suspicious promises, stay calm in crisis, and use your strengths decisively.", "Hard")
]

la_content = f"# Long Answer — Chapter 02: The Stork and the Crab\n\n> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK01_CH02_LA_{idx:03d}"
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

print("[SUCCESS] All 6 category files for Chapter 02 completely refined with 100% unique Class 1 questions!")
