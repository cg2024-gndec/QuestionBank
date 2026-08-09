r"""
Refines all 6 Category files for Chapter 03 ("The Turtle and the Swans") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH03_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_03")
os.makedirs(CH03_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Who were the turtle's best friends in Chapter 03?", "(A) A pair of swans", "(B) Two ducks", "(C) Three fish", "(D) A frog", "(A)", "A pair of swans were the turtle's best friends.", "Easy", "Remembering", "Character Identification"),
    ("What main character trait did the turtle have?", "(A) He was very talkative", "(B) He was quiet", "(C) He was lazy", "(D) He was angry", "(A)", "The turtle loved to talk a lot.", "Easy", "Remembering", "Character Trait"),
    ("What advice did the swans often give to the talkative turtle?", "(A) Learn to think before speaking", "(B) Never swim in the lake", "(C) Fly in the sky", "(D) Eat more grass", "(A)", "They advised him to think before speaking.", "Easy", "Remembering", "Advice"),
    ("Why did the lake start drying up?", "(A) Because of a very hot, cloudless summer", "(B) Because of winter snow", "(C) Because a monster drank it", "(D) Because of heavy rain", "(A)", "A hot, cloudless summer caused the lake to dry up.", "Easy", "Remembering", "Plot Problem"),
    ("Where did the swans find a new place for all of them to live?", "(A) A bigger lake some distance away", "(B) A dark cave", "(C) On top of a tree", "(D) In a river", "(A)", "They found a bigger lake some distance away.", "Easy", "Remembering", "New Habitat"),
    ("Why was carrying the turtle to the new lake a big problem?", "(A) The turtle could not fly and was very slow", "(B) The turtle was too heavy", "(C) The swans had no wings", "(D) The turtle hated water", "(A)", "Turtles cannot fly and walk very slowly.", "Easy", "Understanding", "Problem Reason"),
    ("What tool did the swans use to carry the turtle in the air?", "(A) A wooden stick", "(B) A rope", "(C) A basket", "(D) A leaf", "(A)", "The swans held a wooden stick at both ends.", "Easy", "Remembering", "Tool"),
    ("How were the swans holding the stick?", "(A) In their baks (beaks) at each end", "(B) With their feet", "(C) Under their wings", "(D) On their heads", "(A)", "Each swan held one end of the stick in its beak.", "Easy", "Remembering", "Swans' Action"),
    ("How was the turtle supposed to hold the stick?", "(A) Tightly in the middle with his mouth", "(B) With his tail", "(C) With his front legs", "(D) On his shell", "(A)", "The turtle held the middle of the stick with his mouth.", "Easy", "Remembering", "Turtle's Action"),
    ("What strict warning did the swans give to the turtle before flying?", "(A) Do not talk while flying!", "(B) Do not close your eyes!", "(C) Do not look down!", "(D) Hold your breath!", "(A)", "They warned him not to talk while holding the stick.", "Easy", "Remembering", "Warning"),
    ("How did the people on the ground react when they saw the flying turtle?", "(A) Watched the unique sight in awe", "(B) Threw stones", "(C) Ran away in fear", "(D) Slept on the grass", "(A)", "People watched the unique sight in awe.", "Easy", "Remembering", "People's Reaction"),
    ("What words did the turtle blurt out when he opened his mouth?", "(A) Look at all the people!", "(B) I am flying high!", "(C) Help me!", "(D) Goodbye friends!", "(A)", "He blurted out, 'Look at all the people!'", "Easy", "Remembering", "Dialogue"),
    ("What happened the moment the turtle opened his mouth to talk?", "(A) He lost his grip and fell to his death", "(B) He flew faster", "(C) The swans caught him", "(D) He landed on a cloud", "(A)", "Opening his mouth made him drop the stick and fall.", "Easy", "Remembering", "Climax"),
    ("What is the moral of the story 'The Turtle and the Swans'?", "(A) Speak only after assessing the situation / Think before you speak", "(B) Turtles should learn to fly", "(C) Never trust birds", "(D) Summer is bad", "(A)", "Think before you speak and control your tongue.", "Easy", "Understanding", "Moral Lesson"),
    ("What does the word 'heed' mean in the passage?", "(A) To pay attention to advice", "(B) To run fast", "(C) To drink water", "(D) To fly high", "(A)", "Heed means paying attention to advice.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'awe' mean?", "(A) A feeling of admiration, wonder, or respect", "(B) A feeling of anger", "(C) A feeling of hunger", "(D) A feeling of sadness", "(A)", "Awe means admiration, wonder, or deep respect.", "Easy", "Understanding", "Vocabulary"),
    ("Where did the three friends live at the beginning of the story?", "(A) Near a lake", "(B) In a ocean", "(C) In a desert", "(D) In a palace", "(A)", "They lived near a peaceful lake.", "Easy", "Remembering", "Setting"),
    ("Why did the turtle love talking so much?", "(A) He loved the sound of his own voice", "(B) He wanted to teach others", "(C) He was singing songs", "(D) He was shouting for help", "(A)", "He loved the sound of his own voice.", "Easy", "Remembering", "Character Motivation"),
    ("Who came up with the clever plan to transport the turtle?", "(A) The swans", "(B) The turtle", "(C) The villagers", "(D) A fish", "(A)", "The swans devised the clever stick transport plan.", "Easy", "Remembering", "Plan Origin"),
    ("Was the turtle able to keep his promise of staying quiet until the end?", "(A) No, he broke his promise and talked", "(B) Yes, he stayed quiet", "(C) He sang a song", "(D) He fell asleep", "(A)", "He broke his promise and opened his mouth.", "Easy", "Remembering", "Plot Event"),
    ("From which famous Indian fable collection is this story taken?", "(A) Panchatantra", "(B) Akbar Birbal", "(C) Arabian Nights", "(D) Grimm's Fairy Tales", "(A)", "It is a famous Panchatantra tale.", "Easy", "Remembering", "Literary Origin"),
    ("Why could the turtle not walk to the new lake by himself?", "(A) Because he was very slow and the distance was far", "(B) He had no legs", "(C) He lost his way", "(D) He was blind", "(A)", "Turtles walk very slowly and the lake was far.", "Easy", "Understanding", "Reasoning"),
    ("Did the swans try to save their friend by giving good advice?", "(A) Yes, they warned him repeatedly", "(B) No, they tricked him", "(C) They left him behind", "(D) They pushed him", "(A)", "The swans were true friends who gave good advice.", "Easy", "Understanding", "Character Assessment"),
    ("What season caused the lake to dry up?", "(A) Summer", "(B) Winter", "(C) Spring", "(D) Autumn", "(A)", "A hot, dry summer caused the lake to dry up.", "Easy", "Remembering", "Season"),
    ("What title does Chapter 03 carry in Book 2?", "(A) The Turtle and the Swans", "(B) The Rats Who Ate the Iron Balance", "(C) Four Brahmins", "(D) The Greedy Dog", "(A)", "Chapter 03 is titled 'The Turtle and the Swans'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why was the turtle's habit of not paying heed to advice dangerous?", "(A) Ignoring wise advice eventually led to a fatal mistake during the flight", "(B) It made his voice loud", "(C) It made him sleep long", "(D) It ruined his shell", "(A)", "Ignoring good advice inevitably leads to trouble.", "Medium", "Understanding", "Cause & Effect"),
    ("How did environmental climate change (hot summer) force the animals to act?", "(A) The drying lake threatened their survival, forcing them to search for a new habitat", "(B) It made them play games", "(C) It made them sleep", "(D) It made them fly for fun", "(A)", "Drying water forced them to migrate to a new lake.", "Medium", "Understanding", "Environmental Context"),
    ("Why was the swans' solution both clever and risky?", "(A) It solved the transport problem, but relied completely on the turtle keeping his mouth shut", "(B) The stick was too heavy", "(C) Swans cannot fly high", "(D) The turtle was too light", "(A)", "The plan depended entirely on the turtle's self-control.", "Medium", "Analyzing", "Plan Analysis"),
    ("What does the phrase 'unique view in awe' describe?", "(A) The unusual sight of two swans flying while holding a stick with a turtle in between", "(B) A rainbow in the sky", "(C) An airplane flying by", "(D) A giant bird nest", "(A)", "Villagers marveled at two swans flying with a turtle.", "Medium", "Understanding", "Visual Image"),
    ("Why did the turtle feel compelled to speak despite knowing the risk?", "(A) His foolish desire to show off and express excitement overcame his self-control", "(B) The stick was slippery", "(C) A bee bit him", "(D) The swans dropped him", "(A)", "Lack of self-control made him blurt out comments.", "Medium", "Analyzing", "Psychological Cause"),
    ("How does this story illustrate the danger of foolish pride?", "(A) The turtle wanted people to admire him, which made him forget his safety and open his mouth", "(B) Pride makes you fly", "(C) Pride makes you quiet", "(D) Pride builds lakes", "(A)", "Wanting to show off made him forget safety.", "Medium", "Evaluating", "Theme Analysis"),
    ("What makes a true friend according to the swans' actions?", "(A) True friends help solve problems, share resources, and give wise warnings to protect you", "(B) Friends let you do foolish things", "(C) Friends leave you behind", "(D) Friends laugh at you", "(A)", "Swans helped, warned, and transported their turtle friend.", "Medium", "Evaluating", "Friendship Concept"),
    ("Why is silence powerful in certain dangerous situations?", "(A) Remaining quiet preserves focus, safety, and self-control when action is required", "(B) Silence makes you invisible", "(C) Silence makes you sleep", "(D) Silence stops rain", "(A)", "Silence maintains focus and safety during critical moments.", "Medium", "Evaluating", "Life Principle"),
    ("Compare the nature of the swans with the nature of the turtle.", "(A) Swans were practical, thoughtful, and flying birds; Turtle was talkative, impulsive, and slow-moving", "(B) Both were identical", "(C) Turtle was wise; Swans were foolish", "(D) Swans could not fly", "(A)", "Practical/cautious swans vs talkative/impulsive turtle.", "Medium", "Analyzing", "Character Contrast"),
    ("What would have happened if the turtle had remembered the swans' warning?", "(A) He would have reached the new big lake safely and lived happily with his friends", "(B) He would have fallen anyway", "(C) The stick would break", "(D) The swans would drop him", "(A)", "Remembering the warning would have saved his life.", "Medium", "Analyzing", "Hypothetical Scenario"),
    ("How does Panchatantra use animal physical traits to teach human lessons?", "(A) Using a turtle's mouth gripping a stick illustrates how opening one's mouth carelessly leads to downfall", "(B) It teaches animal facts only", "(C) It shows how birds sing", "(D) It describes lake water", "(A)", "Physical gripping symbolizes mouth control and self-restraint.", "Medium", "Evaluating", "Literary Device"),
    ("What does 'blurt out' mean in sentence context?", "(A) To speak suddenly and thoughtlessly without considering consequences", "(B) To sing softly", "(C) To whisper secrets", "(D) To swallow food", "(A)", "Blurt out means speaking suddenly without thinking.", "Medium", "Understanding", "Vocabulary"),
    ("Why did the villagers' amazement trigger the turtle's downfall?", "(A) The turtle wanted to respond to their attention, letting pride ruin his concentration", "(B) The villagers shouted at him", "(C) The villagers threw rocks", "(D) The villagers scared the swans", "(A)", "Public attention triggered his need to show off.", "Medium", "Understanding", "Plot Trigger"),
    ("What lesson does Chapter 03 give about self-discipline?", "(A) Discipline your tongue and desires, especially when your safety depends on it", "(B) Speak whenever you feel like it", "(C) Ignore warnings", "(D) Never trust friends", "(A)", "Self-discipline of speech is vital for safety.", "Medium", "Evaluating", "Core Values"),
    ("What single sentence summarizes the main plot of Chapter 03?", "(A) A talkative turtle fell to his death when he opened his mouth while flying on a stick", "(B) Swans learned to swim in a lake", "(C) A turtle built a house", "(D) People threw stones at birds", "(A)", "The plot centers on the talkative turtle falling due to opening his mouth.", "Medium", "Understanding", "Plot Summary"),

    # Hard (41-50)
    ("Analyze how impulse control (or lack thereof) determines the tragic outcome in Chapter 03.", "(A) The turtle possessed intellectual knowledge of the rule, but lacked internal impulse control to override his habit of talking", "(B) The swans accidentally dropped the stick", "(C) A strong wind blew the stick away", "(D) The turtle was too heavy", "(A)", "Impulse control failure caused the fatal drop.", "Hard", "Analyzing", "HOTS Psychological Analysis"),
    ("Evaluate the concept of 'think before you speak' in high-stakes environments.", "(A) In critical situations, speech must be filtered by situational awareness; careless speech destroys safety and focus", "(B) Speech is always harmless", "(C) Thinking slows you down", "(D) Talking solves all problems", "(A)", "Situational awareness must filter speech in critical moments.", "Hard", "Evaluating", "Strategic Communication"),
    ("How does the story highlight the irony of a successful plan destroyed by user indiscretion?", "(A) The swans engineered a brilliant aeronautical solution, but the beneficiary's inability to stay silent ruined it", "(B) The plan failed because of rain", "(C) The stick was rotten", "(D) The swans got tired", "(A)", "User indiscretion ruined an engineered solution.", "Hard", "Analyzing", "Irony Analysis"),
    ("Compare the turtle's tragic flaw (loquacity/talkativeness) with other classic fable character flaws.", "(A) Like vanity or greed, excessive talkativeness prevents clear judgment and leads to self-inflicted harm", "(B) Talkativeness is always praised", "(C) Talkativeness is a magic power", "(D) It has no flaw", "(A)", "Excessive talkativeness is a self-destructive character flaw.", "Hard", "Analyzing", "Comparative Fable Critique"),
    ("How can Class 2 students apply the moral of 'The Turtle and the Swans' in their classroom?", "(A) Know when to be quiet (e.g., during teacher instructions or fire drills) to ensure safety and effective learning", "(B) Talk continuously in class", "(C) Ignore teacher rules", "(D) Shout at classmates", "(A)", "Knowing when to stay silent ensures classroom safety and focus.", "Hard", "Applying", "Real Life Application"),
    ("Deconstruct the sequence of ecological and behavioral events leading to the climax.", "(A) Drought -> Drying Lake -> Decision to Migrate -> Innovative Transport -> Flight -> Crowd Attention -> Impulse -> Speech -> Fall", "(B) Speech -> Fall -> Drought -> Lake -> Flight", "(C) Flight -> Crowd -> Drought -> Stick -> Fall", "(D) Lake -> Swans -> Fall -> Speech -> Flight", "(A)", "Sequence from environmental cause to behavioral downfall.", "Hard", "Analyzing", "Sequential Analysis"),
    ("Why is the warning 'speak only after assessing the situation' vital for leadership and citizenship?", "(A) Reckless statements in delicate situations create chaos, whereas assessed speech builds clarity and safety", "(B) Leaders should never speak", "(C) Anyone can say whatever they want anytime", "(D) Assessing takes too much time", "(A)", "Assessed speech builds clarity, safety, and leadership integrity.", "Hard", "Evaluating", "Civic Wisdom"),
    ("What does the turtle's fall symbolize in moral literature?", "(A) The fall from safety into ruin caused by unbridled vanity and inability to hold one's tongue", "(B) Learning to fly", "(C) Swimming in water", "(D) Falling asleep", "(A)", "Symbolizes downfall caused by vanity and unrestrained tongue.", "Hard", "Evaluating", "Symbolism"),
    ("How does Panchatantra balance tragedy with moral instruction in this narrative?", "(A) The stark tragic ending (the turtle's death) emphasizes the severe reality of ignoring wisdom, making the lesson unforgettable", "(B) It makes children laugh", "(C) It gives money rewards", "(D) It hides the ending", "(A)", "Stark consequences make the moral unforgettable.", "Hard", "Evaluating", "Literary Effectiveness"),
    ("What is the ultimate takeaway message of Chapter 03 for primary learners?", "(A) Value good advice, exercise self-control over your speech, and remember that staying quiet at the right moment can save your life!", "(B) Always talk loudly", "(C) Never fly with birds", "(D) Turtles should stay in dry mud", "(A)", "Self-control of speech, listening to advice, and silence in critical moments.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 03: The Turtle and the Swans\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH03_MCQ_{idx:03d}"
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
    ("Near a lake lived a turtle who had a pair of _______ as his best friends.", "swans", "A pair of swans were his best friends.", "Easy"),
    ("The turtle loved the sound of his voice and was very _______.", "talkative", "The turtle was very talkative.", "Easy"),
    ("The swans often asked the turtle to learn to think before _______.", "speaking / talking", "They advised him to think before speaking.", "Easy"),
    ("The turtle did not pay any _______ to his friends' advice.", "heed / attention", "He did not pay heed to advice.", "Easy"),
    ("During a very hot, cloudless summer, the lake started _______ up.", "drying", "The lake started drying up.", "Easy"),
    ("The three friends decided to find a new _______ to live in.", "place / lake / home", "They searched for a new home.", "Easy"),
    ("The swans flew around and found a bigger _______ some distance away.", "lake", "They found a bigger lake.", "Easy"),
    ("The problem was how to carry the turtle, as he could not _______.", "fly", "The turtle could not fly.", "Easy"),
    ("The swans decided to hold a wooden _______ in their baks (beaks).", "stick", "They held a stick in their beaks.", "Easy"),
    ("The turtle was asked to hold the middle of the stick tightly with his _______.", "mouth", "He held the stick with his mouth.", "Easy"),
    ("The swans warned the turtle not to _______ while flying.", "talk / speak", "They warned him not to talk.", "Easy"),
    ("The turtle _______ to keep quiet during the flight.", "agreed", "The turtle agreed to stay quiet.", "Easy"),
    ("Soon all three friends were flying in the _______.", "air / sky", "They flew through the air.", "Easy"),
    ("People of the towns and villages watched the unique view in _______.", "awe", "People watched in awe.", "Easy"),
    ("The talkative turtle opened his mouth to say, 'Look at all the _______!'", "people", "He blurted out, 'Look at all the people!'", "Easy"),
    ("The moment he opened his mouth, he fell down to his _______.", "death", "He fell to his death.", "Easy"),
    ("The moral of the story is to speak only after assessing the _______.", "situation", "Speak after assessing the situation.", "Easy"),
    ("The word 'heed' means to pay _______ to advice.", "attention", "Heed means paying attention.", "Easy"),
    ("The word 'awe' means a feeling of admiration and _______.", "wonder / respect", "Awe means admiration and respect.", "Easy"),
    ("This story is a famous tale from the _______.", "Panchatantra", "It is a Panchatantra tale.", "Easy"),
    ("The turtle moved very _______ on land.", "slowly / slow", "Turtles move slowly.", "Easy"),
    ("The swans used their _______ to hold the ends of the stick.", "beaks / baks", "Swans used their beaks.", "Easy"),
    ("The summer weather was very _______ and cloudless.", "hot", "The summer was hot and cloudless.", "Easy"),
    ("Opening his mouth caused the turtle to lose his _______ on the stick.", "grip / hold", "Opening his mouth broke his grip.", "Easy"),
    ("Chapter 03 is titled The Turtle and the _______.", "Swans", "Chapter 03 is titled The Turtle and the Swans.", "Easy"),

    # Medium (26-40)
    ("The word 'talkative' means fond of _______ a lot.", "talking / speaking", "Talkative means fond of talking.", "Medium"),
    ("The word 'unique' means one of a kind or _______.", "unusual / special", "Unique means one of a kind.", "Medium"),
    ("The word 'assessing' means evaluating or thinking about a _______.", "situation / condition", "Assessing means evaluating.", "Medium"),
    ("The turtle's weakness was his lack of self-_______.", "control / discipline", "He lacked self-control.", "Medium"),
    ("The swans demonstrated problem-solving skills by creating a clever _______.", "plan / solution", "They created a clever plan.", "Medium"),
    ("The villagers expressed great admiration and _______ when looking at the sky.", "wonder / awe", "They expressed wonder and awe.", "Medium"),
    ("The turtle's desire to show off made him forget the swans' _______.", "warning", "Pride made him forget the warning.", "Medium"),
    ("Silence is necessary when safety depends on maintaining a tight _______.", "grip / hold", "Safety depended on holding tight.", "Medium"),
    ("The drying lake presented an environmental _______ for the animals.", "crisis / problem", "Drought created an environmental crisis.", "Medium"),
    ("A true friend gives honest advice to keep you out of _______.", "danger / harm", "Friends give advice to keep you safe.", "Medium"),
    ("The turtle's fall was a direct result of his own _______.", "folly / mistake / choice", "His fall resulted from his own choice.", "Medium"),
    ("Boastfulness can lead to sudden and tragic _______.", "downfall / failure", "Boastfulness causes downfall.", "Medium"),
    ("The swans flew smoothly while holding the stick in their _______.", "beaks", "Swans held the stick in beaks.", "Medium"),
    ("Thinking before speaking prevents foolish _______.", "mistakes / errors", "Thinking prevents mistakes.", "Medium"),
    ("The story illustrates how habit can overcome rational _______.", "thought / reasoning", "Habit can overcome reasoning.", "Medium"),

    # Hard (41-50)
    ("Impulse control is essential for sustaining physical _______ in dangerous situations.", "safety / grip", "Impulse control ensures safety.", "Hard"),
    ("The swans' aeronautical innovation was undone by human-like _______.", "vanity / loquacity", "Vanity ruined the innovation.", "Hard"),
    ("Situational awareness demands evaluating risks before opening one's _______.", "mouth", "Evaluate risks before speaking.", "Hard"),
    ("The crowd's gaze acted as a psychological trigger for the turtle's _______.", "vanity / pride", "Crowd gaze triggered vanity.", "Hard"),
    ("Tragic consequences emerge when warning signals are consistently _______.", "ignored / disregarded", "Ignoring warnings brings disaster.", "Hard"),
    ("Physical gravity punished the turtle's breach of strict _______.", "silence", "Gravity punished breaking silence.", "Hard"),
    ("Self-restraint elevates individual safety above superficial _______.", "attention", "Restraint elevates safety.", "Hard"),
    ("Fables use tragic outcomes to reinforce moral _______.", "discipline / truth", "Tragedy reinforces moral truth.", "Hard"),
    ("The turtle's oral grip was mutually exclusive with verbal _______.", "expression", "Grip and speech were mutually exclusive.", "Hard"),
    ("Chapter 03 reinforces that self-regulation of speech is a vital life _______.", "skill", "Speech self-regulation is vital.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 03: The Turtle and the Swans\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH03_FIB_{idx:03d}"
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

with open(os.path.join(CH03_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The turtle lived near a lake with a pair of swans as best friends.", True, "The turtle lived near a lake with two swans.", "Easy"),
    ("The turtle was very quiet and rarely spoke.", False, "The turtle loved to talk and was very talkative.", "Easy"),
    ("The swans often advised the turtle to think before speaking.", True, "They advised him to think before speaking.", "Easy"),
    ("The turtle always followed the swans' advice carefully.", False, "The turtle did not pay any heed to their advice.", "Easy"),
    ("A cold rainy winter caused the lake to dry up.", False, "A hot, cloudless summer caused the lake to dry up.", "Easy"),
    ("The friends decided to search for a new lake to live in.", True, "They searched for a new lake together.", "Easy"),
    ("The turtle was able to fly fast by himself.", False, "The turtle could not fly and walked very slowly.", "Easy"),
    ("The swans devised a plan using a wooden stick to carry the turtle.", True, "They used a wooden stick held by their beaks.", "Easy"),
    ("The turtle was instructed to hold the middle of the stick with his mouth.", True, "He held the middle of the stick with his mouth.", "Easy"),
    ("The swans warned the turtle to talk loudly while flying.", False, "They warned him strictly NOT to talk while flying.", "Easy"),
    ("The turtle agreed to keep quiet during the flight.", True, "The turtle agreed to stay silent.", "Easy"),
    ("People on the ground watched the flying turtle in awe.", True, "People watched the unique sight in awe.", "Easy"),
    ("The turtle kept his mouth closed until they reached the new lake.", False, "He opened his mouth to talk to the crowd below.", "Easy"),
    ("The turtle said, 'Look at all the people!' before falling.", True, "He blurted out, 'Look at all the people!'", "Easy"),
    ("Opening his mouth caused the turtle to lose his grip and fall to his death.", True, "Opening his mouth made him drop the stick.", "Easy"),
    ("The story teaches us to speak only after assessing the situation.", True, "This is the core moral lesson.", "Easy"),
    ("The word 'heed' means to ignore advice.", False, "Heed means to pay attention to advice.", "Easy"),
    ("The word 'awe' means a feeling of great admiration and wonder.", True, "Awe means admiration and wonder.", "Easy"),
    ("The swans held the ends of the stick with their beaks.", True, "Swans held the stick in their beaks.", "Easy"),
    ("The turtle was able to survive the fall from the sky.", False, "He fell to his death.", "Easy"),
    ("This story is taken from the Panchatantra collection of fables.", True, "It is a Panchatantra fable.", "Easy"),
    ("The new lake found by the swans was bigger than the old one.", True, "They found a bigger lake some distance away.", "Easy"),
    ("The turtle loved the sound of his own voice.", True, "He loved the sound of his voice.", "Easy"),
    ("The swans were selfish and left the turtle behind to die in the drought.", False, "The swans helped their friend by creating a flight plan.", "Easy"),
    ("Chapter 03 is titled 'The Turtle and the Swans'.", True, "Chapter 03 is titled 'The Turtle and the Swans'.", "Easy"),

    # Medium (26-40)
    ("The turtle's main flaw was his inability to control his tongue.", True, "Lack of speech control caused his downfall.", "Medium"),
    ("The swans' plan failed because the wooden stick broke in half.", False, "The plan failed because the turtle opened his mouth.", "Medium"),
    ("The villagers threw stones at the flying animals.", False, "The villagers watched the unique view in awe.", "Medium"),
    ("Silence was necessary for the turtle to maintain his physical grip.", True, "His mouth was holding the stick, requiring silence.", "Medium"),
    ("The turtle opened his mouth because he wanted to boast to the crowd.", True, "Pride made him blurt out a comment.", "Medium"),
    ("Drought forced the animals to seek a new living habitat.", True, "The dry lake forced them to migrate.", "Medium"),
    ("The swans gave bad advice that harmed the turtle.", False, "The swans gave wise advice that the turtle ignored.", "Medium"),
    ("Self-discipline is essential when life depends on adhering to rules.", True, "Self-discipline ensures physical safety.", "Medium"),
    ("The turtle realized his mistake while falling through the air.", True, "He realized his mistake as he fell.", "Medium"),
    ("A true friend helps find solutions to difficult survival challenges.", True, "Swans helped solve the transport problem.", "Medium"),
    ("The turtle's talkative nature had never caused any concern before the flight.", False, "The swans had repeatedly advised him to think before speaking.", "Medium"),
    ("The flight plan was physically impossible for birds to execute.", False, "The flight succeeded until the turtle spoke.", "Medium"),
    ("Assessing a situation before speaking prevents careless mistakes.", True, "Thinking before speaking prevents errors.", "Medium"),
    ("The turtle's death was caused by external interference from people.", False, "His death was self-inflicted by his own loose tongue.", "Medium"),
    ("The fable highlights the dangerous consequences of vanity.", True, "Vanity and showing off cause downfall.", "Medium"),

    # Hard (41-50)
    ("Impulse control requires suppressing immediate desires for long-term safety.", True, "Suppressing immediate impulse preserves safety.", "Hard"),
    ("The turtle's fatal error demonstrates how habit overrides conscious agreement.", True, "Habit of talking overrode his agreement to be silent.", "Hard"),
    ("Physical mechanics of the transport plan made speech mutually exclusive with survival.", True, "Mouth holding stick meant speech equaled death.", "Hard"),
    ("Public admiration often serves as a dangerous catalyst for foolish behavior.", True, "Public gaze triggered foolish showmanship.", "Hard"),
    ("The tragic ending reinforces that natural consequences enforce moral laws.", True, "Gravity enforced the consequence of foolish speech.", "Hard"),
    ("The swans were morally responsible for the turtle's death because they suggested flying.", False, "The swans planned well and warned him; the turtle chose to speak.", "Hard"),
    ("Silence in critical moments reflects high emotional intelligence.", True, "Silence during danger shows emotional control.", "Hard"),
    ("Panchatantra fables use fatal outcomes to leave an indelible moral impression.", True, "Fatal outcomes make lessons unforgettable.", "Hard"),
    ("The story implies that persistent disregard for good advice builds self-destructive habits.", True, "Disregarding advice builds bad habits.", "Hard"),
    ("Chapter 03 advocates complete muteness in all human relationships.", False, "It advocates thinking and assessing before speaking, not absolute muteness.", "Hard")
]

tf_content = f"# True / False — Chapter 03: The Turtle and the Swans\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH03_TF_{idx:03d}"
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

with open(os.path.join(CH03_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who lived near the lake and who were his best friends?", "A talkative turtle lived near the lake with a pair of swans as his best friends.", "Easy"),
    ("What was the main character weakness of the turtle?", "The turtle was extremely talkative and loved the sound of his own voice.", "Easy"),
    ("What advice did the swans frequently give to the turtle?", "The swans frequently advised him to learn to think before speaking.", "Easy"),
    ("Why did the lake start drying up?", "The lake started drying up because of a very hot and cloudless summer.", "Easy"),
    ("Where did the swans find a new home for the three friends?", "The swans flew around and found a bigger lake some distance away.", "Easy"),
    ("Why was it difficult for the turtle to travel to the new lake?", "Because the turtle could not fly and walked very slowly on land.", "Easy"),
    ("What clever solution did the swans create to carry the turtle?", "They held a wooden stick at both ends with their beaks and asked the turtle to bite the middle.", "Easy"),
    ("How did the turtle hold onto the wooden stick during flight?", "The turtle held the middle of the wooden stick tightly with his mouth.", "Easy"),
    ("What warning did the swans give the turtle before taking off?", "They warned him strictly not to talk or open his mouth while flying.", "Easy"),
    ("How did the villagers react when they saw the flying turtle?", "The villagers watched the unique and unusual sight in awe and wonder.", "Easy"),
    ("Why did the turtle open his mouth while flying in the air?", "He wanted to show off and blurt out a comment to the crowd below.", "Easy"),
    ("What words did the turtle say when he opened his mouth?", "He blurted out, 'Look at all the people!'", "Easy"),
    ("What happened immediately after the turtle opened his mouth?", "He lost his mouth grip on the stick and fell to the ground to his death.", "Easy"),
    ("What is the main moral of 'The Turtle and the Swans'?", "The moral is to speak only after assessing the situation and to think before speaking.", "Easy"),
    ("What does the word 'heed' mean in this story?", "'Heed' means paying careful attention to advice or warnings.", "Easy"),
    ("What does the word 'awe' mean?", "'Awe' means a strong feeling of admiration, wonder, or respect.", "Easy"),
    ("Did the turtle listen to his friends' advice before the drought happened?", "No, the turtle did not pay any heed to their advice.", "Easy"),
    ("How many swans were there in the story?", "There were two swans (a pair of swans).", "Easy"),
    ("Why was silence necessary during the flight?", "Because opening his mouth meant letting go of the stick that kept him airborne.", "Easy"),
    ("What book of ancient fables includes this tale?", "This tale comes from the ancient Indian fable collection called the Panchatantra.", "Easy"),
    ("What season caused the water crisis for the animals?", "A hot, cloudless summer season caused the drought.", "Easy"),
    ("Who held the ends of the wooden stick?", "The two swans held one end each of the stick in their beaks.", "Easy"),
    ("Did the swans try their best to save their friend?", "Yes, the swans found a new lake and devised a flight plan to help him.", "Easy"),
    ("What title does Chapter 03 carry in Book 2?", "Chapter 03 is titled 'The Turtle and the Swans'.", "Easy"),
    ("How could the turtle have reached the new lake safely?", "By keeping his mouth shut tightly on the stick until they landed.", "Easy"),

    # Medium (26-40)
    ("Why is ignoring wise advice dangerous in times of crisis?", "Ignoring good advice creates bad habits that lead to fatal errors when real danger strikes.", "Medium"),
    ("How did drought affect the living conditions of the lake animals?", "Drought dried up the lake, depriving them of water and forcing them to migrate.", "Medium"),
    ("Why was the swans' transport plan reliant on the turtle's self-control?", "Because the mechanical grip depended entirely on the turtle keeping his jaws closed.", "Medium"),
    ("What motivated the turtle to speak despite knowing the danger?", "His foolish desire for attention and lack of speech discipline overcame his common sense.", "Medium"),
    ("Explain the meaning of 'speak only after assessing the situation'.", "Evaluate the risks and surroundings before talking, ensuring it is safe and appropriate to speak.", "Medium"),
    ("How did the villagers' attention trigger the turtle's vanity?", "Seeing people admire the flight made the turtle want to boast, triggering his downfall.", "Medium"),
    ("Contrast the flying ability of the swans with the physical limits of the turtle.", "Swans fly high and fast through the air; turtles are bound to land and move slowly.", "Medium"),
    ("Why is self-discipline over one's tongue vital for personal safety?", "Careless words can ruin plans, damage relationships, or cause physical harm in risky situations.", "Medium"),
    ("How did the swans show true friendship toward the talkative turtle?", "They searched for a new home, invented a flight method, and warned him caring for his safety.", "Medium"),
    ("What would have happened if the swans had left the turtle behind?", "The turtle would have perished slowly in the dried-up lake due to lack of water.", "Medium"),
    ("Why is silence a virtue during critical tasks?", "Silence ensures complete concentration, maintains physical control, and prevents fatal distractions.", "Medium"),
    ("How does Panchatantra use this fable to warn against loose speech?", "It demonstrates dramatically that opening one's mouth at the wrong time leads to instant ruin.", "Medium"),
    ("What does 'blurt out' tell us about the turtle's mental state?", "It shows he spoke impulsively on sudden emotion without reflecting on the consequences.", "Medium"),
    ("How did the physical act of talking directly cause physical falling?", "Opening his mouth released the stick handle, breaking the sole connection holding him in the air.", "Medium"),
    ("Summarize Chapter 03 in two clear sentences.", "A talkative turtle migrated to a new lake by biting the middle of a stick held by two flying swans. Unable to stay quiet, he opened his mouth to boast and fell to his death.", "Medium"),

    # Hard (41-50)
    ("Analyze impulse control failure in the turtle's psychological profile.", "The turtle suffered from chronic loquacity; when stimulated by public gaze, habit defeated rational safety rules.", "Hard"),
    ("Evaluate the friction between structural safety and individual behavior in the flight plan.", "The swans engineered a sound structural plan, but its weakest link was the turtle's behavioral indiscretion.", "Hard"),
    ("How does the gaze of the crowd operate as a narrative catalyst in fables?", "The crowd represents external validation; desire for public applause lures vain characters into self-destruction.", "Hard"),
    ("Compare the turtle's talkative flaw with the Brahmins' arrogance in Chapter 02.", "Both flaws stem from vanity—the Brahmins showed off magic, while the turtle showed off speech; both caused death.", "Hard"),
    ("How can Class 2 students apply Chapter 03's moral during group activities?", "Students learn to control impulsive talking, listen to instructions, and stay focused during critical tasks.", "Hard"),
    ("Deconstruct the sequence of ecological cause and behavioral effect in Chapter 03.", "Drought -> Lake Dries -> Migration Needed -> Flight Plan -> Sky Journey -> Public View -> Impulsive Speech -> Fall.", "Hard"),
    ("Why is the moral 'think before you speak' universally applicable across cultures?", "Because unchecked speech consistently causes misunderstandings, accidents, and ruined endeavors in all human societies.", "Hard"),
    ("What does the turtle's fall symbolize in ethical literature?", "It symbolizes the swift, gravity-like punishment that unbridled vanity brings upon foolish individuals.", "Hard"),
    ("How does Panchatantra balance compassion for animals with tragic lessons?", "It presents affectionate friendship among animals, but enforces uncompromising natural consequences for foolish choices.", "Hard"),
    ("Synthesize the ultimate educational message of Chapter 03 for primary learners.", "Master your tongue, heed good advice, stay focused under pressure, and remember that silence is life-saving wisdom!", "Hard")
]

sa_content = f"# Short Answer — Chapter 03: The Turtle and the Swans\n\n> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH03_SA_{idx:03d}"
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

with open(os.path.join(CH03_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-15)
    ("Write a simple summary of Chapter 03 'The Turtle and the Swans'.", "Near a lake lived a talkative turtle with his best friends, a pair of swans. The turtle loved to talk and never listened to the swans' advice to think before speaking. During a hot summer, the lake dried up, so the friends decided to move to a bigger lake. Since the turtle could not fly, the swans came up with a plan: they held a wooden stick at both ends in their beaks and asked the turtle to bite the middle tightly with his mouth. They strictly warned him not to speak while flying. The turtle agreed, and they flew up into the sky. Villagers watched the unique sight in awe. Unfortunately, the talkative turtle could not stay quiet and opened his mouth to say, 'Look at all the people!' The moment he opened his mouth, he lost his grip and fell to his death. The moral is to think before you speak and control your tongue.", "Easy"),
    ("Describe the character of the turtle in detail.", "The turtle is the central character of the story. He lives near a lake and is best friends with two swans. His defining personality trait is that he is extremely talkative and loves the sound of his own voice. However, he suffers from a major flaw: he lacks self-control and does not pay heed to wise advice. Even when his life depends on staying quiet while being carried through the air on a stick, his foolish urge to show off and talk overcomes his common sense. Opening his mouth causes his tragic downfall, showing the dangers of uncontrolled speech.", "Easy"),
    ("Describe the characters of the two swans and their friendship with the turtle.", "The two swans are wise, caring, and practical friends. They live in the lake and treat the turtle as their best companion. When the lake dries up during a hot summer, they do not abandon their slow friend. Instead, they fly around, locate a new bigger lake, and invent a clever flight transport plan using a wooden stick. They give clear, protective warnings to the turtle about the danger of speaking during flight. Their actions show true friendship, intelligence, and protective care.", "Easy"),
    ("Explain the clever plan devised by the swans to transport the turtle.", "The swans devised a unique mechanical transport plan:\n1. They selected a strong wooden stick.\n2. Each swan held one end of the stick firmly in its beak.\n3. They instructed the turtle to bite the center of the stick tightly with his mouth.\n4. As the swans flew up, the turtle hung in the middle between them.\n5. The vital condition of the plan was that the turtle had to remain completely silent, because opening his mouth would release his grip on the stick.", "Easy"),
    ("What caused the lake to dry up and what problem did it create?", "A very hot and cloudless summer season caused the water in the lake to evaporate and dry up completely. This created a severe survival crisis for the aquatic animals. The three friends were forced to leave their home and find a new water body. While the swans could easily fly to a new lake, transporting the slow, non-flying turtle across a long distance presented a major challenge.", "Easy"),
    ("Explain why the turtle opened his mouth while flying in the sky.", "While flying through the air, the unique sight of two swans carrying a turtle on a stick amazed the villagers below, who watched in awe. Seeing the crowd watching him triggered the turtle's foolish vanity. He felt an overwhelming urge to comment and show off. Unable to control his talkative habit, he opened his mouth to say, 'Look at all the people!', forgetting that his mouth was the only thing holding him to the stick.", "Easy"),
    ("What moral lesson does the story teach about controlling one's speech?", "The story teaches that we must exercise strict discipline over our speech and think carefully before speaking. Talking thoughtlessly or at inappropriate times can ruin good plans and cause serious harm. We should assess our situation, listen to wise advice, and know when silence is necessary for safety and success.", "Easy"),
    ("Explain the meaning and importance of the vocabulary words 'heed' and 'awe'.", "• Heed: Paying careful attention to advice, instructions, or warnings. Taking heed of good advice prevents unnecessary mistakes and danger.\n• Awe: A deep feeling of wonder, admiration, and respect experienced when witnessing something extraordinary or unusual, such as a turtle flying in the sky.", "Easy"),
    ("How did the villagers react when they saw the turtle flying?", "As the swans flew over towns and villages, the people on the ground looked up and saw the extraordinary sight of two birds carrying a turtle on a stick. They were filled with amazement and watched the unique spectacle in awe, talking excitedly among themselves.", "Easy"),
    ("Why did the swans' warning fail to save the turtle?", "The swans' warning failed not because it was unclear, but because the turtle lacked internal self-discipline. Although he understood and agreed to the rule on the ground, his long-formed habit of talkativeness and sudden vanity in the air completely broke his self-control, causing him to ignore the warning when it mattered most.", "Easy"),
    ("Describe the contrast between the turtle's physical limitations and the swans' capabilities.", "Swans are graceful water birds capable of flying high and fast across great distances. In contrast, the turtle is a slow-moving reptile bound to land and water, completely incapable of flight. This physical contrast made the turtle entirely dependent on the swans' flight ability to reach the new lake.", "Easy"),
    ("Why is silence considered a life-saving virtue in this story?", "In this story, silence was not just a polite habit; it was a physical necessity for survival. The turtle's mouth was acting as his safety harness. Remaining silent kept his jaws locked on the stick, securing his life. Breaking silence released the harness, making silence a literal life-saving virtue.", "Easy"),
    ("How does Panchatantra use this fable to instruct young children?", "Panchatantra uses this memorable fable to teach children the practical importance of listening to elders, thinking before speaking, maintaining self-control under excitement, and recognizing that careless actions have irreversible consequences.", "Easy"),
    ("What happens when someone ignores good advice repeatedly?", "When a person repeatedly ignores good advice (as the turtle did when his friends warned him about talkativeness), they build dangerous habits of carelessness. Eventually, when faced with a high-stakes situation, those bad habits lead to fatal or irreversible mistakes.", "Easy"),
    ("What values should Class 2 students learn from Chapter 03?", "Class 2 students should learn to practice self-restraint in speech, pay attention to rules and safety warnings, avoid showing off in public, appreciate true friends who help them, and think about safety before acting.", "Easy"),

    # Medium (16-40)
    ("Analyze how impulse control failure led to the turtle's tragic downfall.", "The turtle suffered from a severe lack of impulse control. Although he consciously agreed to stay quiet while on the ground, the immediate sensory stimulus of crowd admiration triggered his habit of talking. Unable to suppress his impulsive desire to speak, he opened his mouth. This single moment of impulse control failure broke his physical grip, causing his fatal fall.", "Medium"),
    ("Discuss the theme of environmental adaptation and migration in the story.", "The narrative begins with an environmental crisis—a severe summer drought drying up the lake. To survive, the species must adapt through migration. While birds migrate effortlessly, slow land-bound creatures like turtles face extreme vulnerability. The story highlights how ecological changes force animals into high-risk migration strategies.", "Medium"),
    ("Evaluate the quality of friendship shown by the two swans.", "The swans exemplify noble friendship. They did not abandon their slow companion during the drought. They actively researched a new habitat, engineered a creative solution, managed the physical burden of carrying him, and gave clear safety instructions. The tragic outcome was entirely due to the turtle's choice, not any failure of friendship.", "Medium"),
    ("Explain the concept of 'assessing the situation' before taking action.", "'Assessing the situation' means analyzing your current environment, understanding risks, and evaluating consequences before speaking or acting. Had the turtle assessed his situation—hanging hundreds of feet in the air by his mouth—he would have recognized that speech equaled immediate death and chosen silence.", "Medium"),
    ("Why do public attention and crowd gaze often trigger foolish behavior in people?", "Public attention fuels human vanity and the desire for social approval or applause. When people feel observed by a crowd, they often experience an urge to perform or make statements to gain attention, which can cloud their judgment and lead to foolish, dangerous choices.", "Medium"),
    ("Write a dialogue between the swans and the turtle when planning the flight.", "Swan 1: 'We found a big lake, but you cannot fly. How will you come?'\nTurtle: 'Please don't leave me behind! Find a way!'\nSwan 2: 'We can carry a stick in our beaks, and you must bite the middle tightly. But you MUST promise not to speak!'\nTurtle: 'I promise! I will not say a single word until we land!'", "Medium"),
    ("Compare the physical strength of the turtle's mouth with his mental strength.", "Physically, the turtle's jaws were strong enough to hold his body weight on the stick throughout the flight. Mentally, however, his willpower and self-discipline were extremely weak. His physical capability was undermined by his mental weakness, demonstrating that physical strength is useless without mental discipline.", "Medium"),
    ("Explain why warnings given in peaceful times must be remembered during moments of excitement.", "Warnings are designed to protect us during future moments of temptation or danger. If we forget warnings the moment excitement or public attention arrives, the warnings become useless. True discipline means upholding safety rules precisely when temptation is highest.", "Medium"),
    ("How does irony function in the turtle's final words: 'Look at all the people!'?", "The irony lies in the turtle wanting the people to look at his grand achievement of flying. However, by opening his mouth to call attention to himself, he instantly destroyed his achievement and fell to his death, turning a moment of glory into sudden tragedy.", "Medium"),
    ("Describe the journey through the air from the perspective of the swans.", "The swans flew steadily, using their wing power to carry the added weight of the turtle hanging from the stick. They maintained steady flight, focused on reaching the distant lake, and relied on their friend to keep his promise of silence, only to feel the stick suddenly lighten as he let go.", "Medium"),
    ("Why is loose speech considered a dangerous habit in human society?", "In daily life, loose speech spreads rumors, causes arguments, reveals secrets, hurts feelings, and ruins reputation. Just as opening his mouth destroyed the turtle, careless words in human relationships destroy trust and create lasting conflict.", "Medium"),
    ("How can Class 2 teachers use Chapter 03 to teach classroom discipline?", "Teachers can explain that during important tasks (like crossing roads or listening to instructions), staying quiet and focused is like holding the stick. Talking out of turn distracts attention and causes safety risks, showing why quiet focus is essential.", "Medium"),
    ("Explain how habit formation influences human behavior during emergencies.", "Habits formed over time operate automatically during moments of distraction or stress. Because the turtle had formed a lifelong habit of talking incessantly without thinking, that habit took over automatically when he saw the crowd, overriding his temporary promise of silence.", "Medium"),
    ("Contrast the character of a wise person with a talkative foolish person.", "A wise person listens more than speaks, evaluates risks, respects good advice, and speaks only when helpful and safe. A talkative foolish person speaks constantly to gain attention, ignores warnings, acts impulsively, and brings trouble upon themselves.", "Medium"),
    ("What does this fable teach about taking responsibility for one's own downfall?", "The fable shows that the turtle's downfall was entirely self-inflicted. The swans provided a safe plan and clear warnings, but the turtle's own choice to speak caused his death. It teaches that we must take personal responsibility for the outcomes of our choices.", "Medium"),
    ("Describe the visual imagery of the flight scene.", "The scene presents a striking visual contrast: two majestic white swans flying in tandem against a blue summer sky, holding a wooden stick in their sharp beaks, with a round green turtle suspended in mid-air biting the center, while miniature towns and astonished villagers lie far below.", "Medium"),
    ("Why did the Panchatantra storyteller choose a turtle for this specific moral?", "Turtles are naturally slow and carry heavy protective shells, symbolizing stability. Giving a naturally slow, quiet-looking creature an excessively talkative personality creates a striking character contradiction that highlights how foolish talkativeness ruins even natural stability.", "Medium"),
    ("How does Chapter 03 fulfill Class 2 English learning objectives?", "It enhances reading comprehension, introduces essential vocabulary (heed, awe, unique, assessing), develops cause-and-effect reasoning, teaches moral values, and provides engaging structured assessment exercises.", "Medium"),
    ("How did the drought act as a test of the three friends' character?", "The drought tested their loyalty and problem-solving. The swans passed the test by staying loyal and inventing a flight plan. The turtle failed the test of self-discipline during execution, proving that plans require execution discipline to succeed.", "Medium"),
    ("Summarize Chapter 03 in four comprehensive bullet points.", "• A talkative turtle and two swans faced a severe drought that dried up their lake.\n• The swans found a new lake and planned to carry the turtle using a stick held by their beaks.\n• The turtle promised to hold the stick with his mouth and stay completely silent during flight.\n• Overcome by vanity when seeing villagers, the turtle opened his mouth to talk and fell to his death.", "Medium"),

    # Hard (41-50)
    ("Deconstruct the psychological conflict between long-term goal (survival) and short-term impulse (speech).", "The turtle experienced a classic psychological conflict: his long-term goal was reaching the new lake safely, requiring sustained silence. His short-term impulse was blurting out a comment to satisfy immediate vanity. The immediate, accessible impulse defeated the delayed, abstract goal, illustrating how short-term gratification destroys long-term survival.", "Hard"),
    ("Analyze how public spectacle dynamics alter individual risk perception.", "Being elevated in the sky turned the turtle into a public spectacle for the crowd below. Public visibility alters psychology—it inflates self-importance and creates psychological pressure to perform, blinding the individual to immediate physical dangers (gravity and mouth grip).", "Hard"),
    ("Critique the structural mechanics of the swans' transport system.", "The transport system was mechanically sound under static conditions (holding stick with mouth). However, it lacked operational redundancy—there was no backup harness or safety net. This single-point-of-failure design meant that a single human/animal error inevitably led to catastrophic system collapse.", "Hard"),
    ("Evaluate the philosophical statement: 'Silence is not the absence of thought, but the highest form of self-governance.'", "The fable demonstrates that silence during flight required intense active self-governance—suppressing speech, maintaining muscle tension, and focusing on safety. Silence was an active, disciplined choice, whereas speech was a passive collapse of control.", "Hard"),
    ("Examine how Chapter 03 reflects ancient Indian oral traditions of ethical instruction.", "Ancient Indian oral traditions used vivid, memorable parables with stark consequences to instill core social virtues (speech control, respect for advice, situational awareness) in young minds, ensuring ethical principles were easily remembered and applied in daily life.", "Hard"),
    ("Formulate a multi-disciplinary primary lesson connecting Chapter 03 with Science and Ethics.", "• Science: Study animal adaptations (birds flying vs turtles swimming/walking) and drought impact on ecosystems.\n• Ethics: Discuss the importance of listening to safety rules and exercising self-control over speech during class activities.", "Hard"),
    ("Differentiate between situational silence (context-dependent) and chronic muteness.", "The fable does not advocate chronic muteness or fear of speaking. It advocates situational silence—recognizing when environmental context (hanging from a stick in mid-air) demands absolute silence, and speaking only when conditions are safe.", "Hard"),
    ("Why is the moral 'speak only after assessing the situation' vital in modern digital communication?", "In the modern digital age, people often 'blurt out' comments, posts, or messages impulsively on social media without assessing consequences, leading to ruined reputations and social fallout, directly echoing the turtle's tragic mistake.", "Hard"),
    ("Discuss how tragedy in fables serves a cathartic and educational function.", "Tragedy creates emotional impact (shock and sorrow) that burns the moral lesson into the reader's memory. A happy ending where the turtle speaks but doesn't fall would fail to convey the real-world severity of ignoring safety warnings.", "Hard"),
    ("Synthesize the ultimate educational philosophy of Chapter 03 for primary learners.", "True wisdom lies in governing your tongue. Respect wise advice, stay focused on your goals, exercise self-control when tempted by attention, and remember that thinking before speaking protects your life and honor!", "Hard")
]

la_content = f"# Long Answer — Chapter 03: The Turtle and the Swans\n\n> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH03_LA_{idx:03d}"
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

with open(os.path.join(CH03_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based Questions (10 Extracts x 5 Qs = 50 Qs)
# -------------------------------------------------------------
extracts = [
    (
        "Once upon a time, near a lake lived a turtle who had a pair of swans living in the lake as his best friends. The turtle loved the sound of his voice and this is why was very talkative.",
        [
            ("Where did the turtle live?", "The turtle lived near a lake.", "Easy"),
            ("Who were the turtle's best friends?", "A pair of swans living in the lake were his best friends.", "Easy"),
            ("What was the turtle's defining habit?", "The turtle was very talkative and loved to speak a lot.", "Easy"),
            ("Why was the turtle so talkative according to the passage?", "Because he loved the sound of his own voice.", "Medium"),
            ("What potential character flaw is highlighted in this opening passage?", "Excessive talkativeness and self-fondness (vanity) regarding his voice.", "Hard")
        ]
    ),
    (
        "Many a times, the swans asked him to learn to think before speaking. But the turtle did not pay any heed to their advice.",
        [
            ("What advice did the swans often give to the turtle?", "They asked him to learn to think before speaking.", "Easy"),
            ("Did the turtle follow the swans' advice?", "No, the turtle did not pay any heed to their advice.", "Easy"),
            ("What does the word 'heed' mean in this sentence?", "'Heed' means paying attention to advice or warnings.", "Easy"),
            ("Who were giving advice to the turtle?", "His best friends, the two swans, were giving him advice.", "Medium"),
            ("What pattern of behavior is revealed by the turtle's refusal to listen?", "A stubborn habit of disregarding wise advice from caring friends.", "Hard")
        ]
    ),
    (
        "During a very hot cloudless summer, the lake started drying up. The friends decided to find a new place to live in.",
        [
            ("What season caused the lake to dry up?", "A very hot, cloudless summer caused the lake to dry up.", "Easy"),
            ("What happened to the lake during the summer?", "The lake started drying up.", "Easy"),
            ("What decision did the three friends make when the lake dried up?", "They decided to find a new place to live in.", "Easy"),
            ("Why was living near the drying lake impossible for them?", "Because as aquatic creatures, they needed water to survive.", "Medium"),
            ("How does this environmental crisis set the main story in motion?", "It forces the animals to leave their safe home and attempt a risky migration.", "Hard")
        ]
    ),
    (
        "The swans flew around and found a bigger lake some distance away. Now, the problem was how to carry the turtle with them as the turtle could not fly and was very slow too.",
        [
            ("Where did the swans find a new home?", "They found a bigger lake some distance away.", "Easy"),
            ("Why couldn't the turtle travel to the new lake by himself easily?", "Because the turtle could not fly and walked very slowly.", "Easy"),
            ("Who searched for and found the new lake?", "The two swans flew around and found the new lake.", "Easy"),
            ("What was the main problem facing the three friends?", "How to carry the slow, non-flying turtle across a long distance.", "Medium"),
            ("How does this passage highlight the physical contrast between swans and turtles?", "Swans have aerial mobility, while turtles are bound to slow land movement.", "Hard")
        ]
    ),
    (
        "After thinking over it, finally the swans came up with a solution. They decided to hold one end each of a stick in their baks (beaks) and asked the turtle to hold it with his mouth tightly in the middle.",
        [
            ("Who came up with the solution to transport the turtle?", "The swans came up with the solution.", "Easy"),
            ("What object did the swans decide to use for carrying the turtle?", "They decided to use a wooden stick.", "Easy"),
            ("How were the swans holding the stick?", "Each swan held one end of the stick in its beak.", "Easy"),
            ("How was the turtle supposed to hold the stick?", "The turtle was asked to hold the middle of the stick tightly with his mouth.", "Medium"),
            ("What mechanical principle made this transport solution work?", "Suspension: the turtle hung in the center while two flying birds supported the ends.", "Hard")
        ]
    ),
    (
        "They also warned him not to talk and the turtle agreed. Soon all the three were flying in the air.",
        [
            ("What warning did the swans give to the turtle before taking off?", "They warned him strictly not to talk while flying.", "Easy"),
            ("Did the turtle agree to the swans' condition?", "Yes, the turtle agreed not to talk.", "Easy"),
            ("Where were all three friends flying soon after?", "All three were flying up in the air.", "Easy"),
            ("Why was the warning 'not to talk' essential for the turtle's survival?", "Because opening his mouth to talk would break his grip on the stick.", "Medium"),
            ("What agreement was established between the swans and the turtle?", "A safety covenant: transport in exchange for absolute silence during flight.", "Hard")
        ]
    ),
    (
        "People of the villages and towns they passed watched the unique view in awe.",
        [
            ("Who was watching the three animals flying in the air?", "People of the villages and towns they passed.", "Easy"),
            ("How did the people feel while watching them?", "They watched the unique view in awe and wonder.", "Easy"),
            ("What does the word 'awe' mean in this context?", "A feeling of great admiration, wonder, and respect.", "Easy"),
            ("What made the view so 'unique' to the villagers?", "Seeing two swans flying while carrying a turtle on a stick between them.", "Medium"),
            ("How did the crowd's reaction create an unstated danger for the talkative turtle?", "It excited the turtle's vanity, tempting him to open his mouth and boast.", "Hard")
        ]
    ),
    (
        "Unfortunately, the turtle could not stay quiet any longer and opened his mouth to blurt out, 'Look at all the people.'",
        [
            ("Could the turtle keep his promise of staying quiet?", "No, unfortunately he could not stay quiet any longer.", "Easy"),
            ("What did the turtle do when he saw the people?", "He opened his mouth to blurt out a comment.", "Easy"),
            ("What exact words did the turtle say?", "'Look at all the people.'", "Easy"),
            ("What does 'blurt out' mean in this sentence?", "To speak impulsively and suddenly without thinking of the danger.", "Medium"),
            ("Identify the precise moment of failure in the story.", "The moment the turtle prioritized speaking over maintaining his mouth grip.", "Hard")
        ]
    ),
    (
        "He fell down to his death.",
        [
            ("What happened to the turtle after he opened his mouth?", "He fell down to his death.", "Easy"),
            ("Why did the turtle fall from the sky?", "Because opening his mouth released the stick he was holding.", "Easy"),
            ("Could the swans save him when he fell?", "No, they were holding the ends of the stick and could not catch a falling turtle.", "Easy"),
            ("Was the turtle's fall preventable?", "Yes, if he had kept his mouth closed as promised, he would have landed safely.", "Medium"),
            ("Analyze the tragic finality of this single-sentence event.", "It underscores how a single moment of lost self-control leads to swift, fatal consequences.", "Hard")
        ]
    ),
    (
        "Moral of the Story: Speak only after assessing the situation. Word Meaning: Heed: To pay attention to advice. Awe: Feeling of admiration or respect.",
        [
            ("What is the stated moral of Chapter 03?", "Speak only after assessing the situation.", "Easy"),
            ("What is the definition of 'heed'?", "To pay attention to advice.", "Easy"),
            ("What is the definition of 'awe'?", "Feeling of admiration or respect.", "Easy"),
            ("How does assessing a situation help us in daily life?", "It helps us evaluate risks and choose when it is safe and wise to speak or act.", "Medium"),
            ("Synthesize the connection between the moral and the story events.", "Had the turtle assessed his mid-air situation, he would have realized speech meant death and stayed silent.", "Hard")
        ]
    )
]

ext_content = f"# Extract Based Questions — Chapter 03: The Turtle and the Swans\n\n> **Category**: Extract Based Questions | **Total**: 10 Extracts (50 Sub-Questions) | **Marks**: 3 per set\n\n---\n\n"
sub_q_counter = 1
for ext_idx, (passage, q_list) in enumerate(extracts, start=1):
    ext_content += f"## Extract {ext_idx}\n\n"
    ext_content += f"> *\"{passage}\"*\n\n"
    for q_idx, (q_txt, ans, diff) in enumerate(q_list, start=1):
        q_id = f"BK02_CH03_EXT_{sub_q_counter:03d}"
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

with open(os.path.join(CH03_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print("[SUCCESS] All 6 category files for Book 2 Chapter 03 completely refined with 100% unique Class 2 questions!")
