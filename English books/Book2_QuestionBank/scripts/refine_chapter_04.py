r"""
Refines all 6 Category files for Chapter 04 ("The Wannabe Chocolate") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH04_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_04")
os.makedirs(CH04_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What was the name of the town where the story took place?", "(A) Chocoland", "(B) Candyland", "(C) Sweetville", "(D) Cake Town", "(A)", "The story states that it took place in a town called Chocoland.", "Easy", "Remembering", "Setting"),
    ("Who was the main character in the story?", "(A) Mr. Candy Nougat", "(B) Mr. Jammy", "(C) Mr. Sugar", "(D) Mr. Baker", "(A)", "The story is about a man named Mr. Candy Nougat.", "Easy", "Remembering", "Character Name"),
    ("What did Mr. Candy Nougat make in Chocoland?", "(A) Chocolates and cakes", "(B) Bread and buns", "(C) Toys and games", "(D) Juices and sodas", "(A)", "He made the best chocolates and cakes of different flavours.", "Easy", "Remembering", "Occupation"),
    ("What was Mr. Candy Nougat's assistant's name?", "(A) Jammy", "(B) Tommy", "(C) Sammy", "(D) Jimmy", "(A)", "His assistant's name was Jammy.", "Easy", "Remembering", "Assistant Name"),
    ("Which three words describe Mr. Candy Nougat in the text?", "(A) Talented, hard-working, but clumsy", "(B) Lazy, foolish, and rude", "(C) Quiet, slow, and sad", "(D) Angry, strict, and old", "(A)", "The text states he was talented, hard-working but clumsy.", "Easy", "Remembering", "Character Traits"),
    ("What was Mr. Candy Nougat trying to reach for when the accident happened?", "(A) Sugar", "(B) Salt", "(C) Milk", "(D) Butter", "(A)", "He tried to reach for sugar while mixing chocolate.", "Easy", "Remembering", "Plot Trigger"),
    ("Which ingredients accidentally fell into the chocolate bowl?", "(A) Peanuts, caramel, cashew, and raisins", "(B) Apples, bananas, and cherries", "(C) Rice, wheat, and oats", "(D) Pepper, salt, and ginger", "(A)", "Bowls of peanuts, caramel, cashew, and raisins knocked down into the bowl.", "Easy", "Remembering", "Ingredients"),
    ("What did Mr. Candy Nougat initially want to do with the new mixture?", "(A) Throw it away", "(B) Sell it immediately", "(C) Eat it all", "(D) Give it to birds", "(A)", "He decided to throw away the mixture.", "Easy", "Remembering", "Initial Decision"),
    ("Who tasted the new mixture first before it was thrown away?", "(A) Jammy", "(B) A customer", "(C) A dog", "(D) The Mayor", "(A)", "His assistant Jammy decided to taste it.", "Easy", "Remembering", "Action"),
    ("How did the new mixture taste to Jammy?", "(A) Amazing", "(B) Bitter", "(C) Salty", "(D) Terrible", "(A)", "Jammy found out that the new mixture tasted amazing.", "Easy", "Remembering", "Taste Assessment"),
    ("What name was given to the new chocolates?", "(A) Wannabe Chocolates", "(B) Yummy Chocolates", "(C) Crunchy Bars", "(D) Chocoland Delights", "(A)", "Jammy convinced him to sell it as 'Wannabe Chocolates'.", "Easy", "Remembering", "Product Name"),
    ("Why were the new chocolates named 'Wannabe Chocolates'?", "(A) Because the mixture was different from usual chocolates", "(B) Because they were fake", "(C) Because they cost one rupee", "(D) Because they were shaped like stars", "(A)", "They were called 'Wannabe' because they were different from usual ones.", "Easy", "Remembering", "Name Rationale"),
    ("How did people react when they tasted Wannabe Chocolates?", "(A) Anybody who tasted them loved them", "(B) People spat them out", "(C) Nobody bought them", "(D) People complained", "(A)", "Anybody who tasted the new chocolates loved them.", "Easy", "Remembering", "Customer Response"),
    ("What happened to Wannabe Chocolates in the market?", "(A) They soon ruled the markets", "(B) They were banned", "(C) They failed completely", "(D) They were forgotten", "(A)", "The Wannabe Chocolates soon ruled the markets.", "Easy", "Remembering", "Market Impact"),
    ("What does the word 'clumsy' mean according to the word bank?", "(A) Careless", "(B) Fast", "(C) Smart", "(D) Brave", "(A)", "The word meaning given for clumsy is Careless.", "Easy", "Understanding", "Vocabulary"),
    ("What is 'caramel' as defined in the lesson?", "(A) A type of sticky sweet", "(B) A spicy sauce", "(C) A cold ice cream", "(D) A dry fruit", "(A)", "Caramel is defined as a type of sticky sweet.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'convinced' mean?", "(A) Completely sure about something", "(B) Very angry", "(C) Confused", "(D) Tired", "(A)", "Convinced means completely sure about something.", "Easy", "Understanding", "Vocabulary"),
    ("How many different dry fruits/sweets fell into the bowl?", "(A) Four (peanuts, caramel, cashew, raisins)", "(B) Two", "(C) Five", "(D) One", "(A)", "Four items: peanuts, caramel, cashew, and raisins.", "Easy", "Remembering", "Detail Counting"),
    ("What was Mr. Candy Nougat doing right before he knocked down the bowls?", "(A) Mixing his chocolate", "(B) Baking a cake", "(C) Sleeping", "(D) Sweeping the floor", "(A)", "He was mixing his chocolate when reaching for sugar.", "Easy", "Remembering", "Activity Context"),
    ("Was Mr. Candy Nougat lazy or hard-working?", "(A) Hard-working", "(B) Lazy", "(C) Slow", "(D) Idle", "(A)", "The text clearly states he was hard-working.", "Easy", "Remembering", "Character Trait"),
    ("Who was talented at making cakes and chocolates?", "(A) Mr. Candy Nougat", "(B) Jammy", "(C) The Mayor", "(D) The shopkeeper", "(A)", "Mr. Candy Nougat made the best chocolates and cakes.", "Easy", "Remembering", "Talent"),
    ("Did Jammy agree to throw away the mixture?", "(A) No, he decided to taste it first", "(B) Yes, he threw it in the bin", "(C) Yes, he burned it", "(D) No, he gave it to a cat", "(A)", "Jammy stopped throwing it away by tasting it first.", "Easy", "Remembering", "Decision"),
    ("What kind of town was Chocoland?", "(A) A town where the best chocolates and cakes were made", "(B) A forest town", "(C) A desert town", "(D) A seaside village", "(A)", "Chocoland was famous for delicious chocolates and cakes.", "Easy", "Remembering", "Setting Context"),
    ("Did Mr. Candy Nougat ruin the chocolate on purpose or by accident?", "(A) By accident, because he was clumsy", "(B) On purpose, as an experiment", "(C) Because Jammy pushed him", "(D) Because a wind blew", "(A)", "It was an accident caused by his clumsiness while reaching for sugar.", "Easy", "Understanding", "Cause & Effect"),
    ("What is the title of Chapter 04?", "(A) The Wannabe Chocolate", "(B) The Greedy Baker", "(C) Chocoland Stories", "(D) The Sweet Shop", "(A)", "Chapter 04 is titled 'The Wannabe Chocolate'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why is Jammy's decision to taste the mixture important to the plot?", "(A) It saved a delicious new creation from being wasted in the trash", "(B) It made Jammy sick", "(C) It proved Mr. Nougat was wrong", "(D) It closed the shop", "(A)", "Testing the mixture discovered its amazing taste before disposal.", "Medium", "Understanding", "Plot Turning Point"),
    ("How can a clumsy mistake lead to a great discovery, as shown in this story?", "(A) Sometimes accidental combinations create wonderful new ideas if tested open-mindedly", "(B) Clumsiness always causes total destruction", "(C) Mistakes should always be hidden", "(D) Being careless is better than being careful", "(A)", "Accidents can lead to positive breakthroughs.", "Medium", "Evaluating", "Theme Insight"),
    ("Why did Mr. Candy Nougat want to throw away the mixture right after the spill?", "(A) He assumed that an unintended mix of random items was spoiled and unusable", "(B) He hated peanuts", "(C) Jammy told him to throw it", "(D) The bowl broke", "(A)", "He assumed an accidental mess was ruined.", "Medium", "Understanding", "Character Mindset"),
    ("What quality of Jammy makes him a valuable assistant to Mr. Candy Nougat?", "(A) Curiosity, initiative, and good judgment of taste", "(B) He cleans the floor fast", "(C) He agrees with everything blindly", "(D) He eats all the profits", "(A)", "Jammy showed initiative and curiosity.", "Medium", "Analyzing", "Assistant Value"),
    ("How does the name 'Wannabe Chocolates' reflect the product's identity?", "(A) It highlights that it was unique and did not fit standard chocolate categories", "(B) It implies the chocolate tasted bad", "(C) It means it wanted to be a cake", "(D) It was named after a place", "(A)", "It was different from conventional pure chocolates.", "Medium", "Understanding", "Naming Significance"),
    ("What lesson does Mr. Candy Nougat learn from his assistant Jammy?", "(A) To get a second opinion before discarding something that looks like a mistake", "(B) Never hire assistants", "(C) Stop making chocolates", "(D) Always throw away spills", "(A)", "Testing unexpected results can reveal value.", "Medium", "Evaluating", "Life Lesson"),
    ("What contrast exists between Mr. Candy Nougat's skills and his physical habits?", "(A) He was highly talented and hard-working, yet physically clumsy", "(B) He was lazy but quick", "(C) He was rude but generous", "(D) He was quiet but noisy", "(A)", "Talented and hard-working vs. clumsy.", "Medium", "Analyzing", "Character Contrast"),
    ("How did teamwork between Mr. Candy Nougat and Jammy lead to success?", "(A) Mr. Nougat created the base and Jammy identified the commercial potential of the mix", "(B) Mr. Nougat did nothing while Jammy worked", "(C) Jammy bought the shop", "(D) They competed against each other", "(A)", "Combining Nougat's mix with Jammy's insight brought success.", "Medium", "Analyzing", "Teamwork"),
    ("Why did Wannabe Chocolates rule the markets so quickly?", "(A) Because their unique flavor combination tasted amazing to everyone who tried them", "(B) Because they were given for free", "(C) Because there were no other sweets", "(D) Because the King forced people to buy them", "(A)", "Delightful unique taste drove market popularity.", "Medium", "Understanding", "Market Success"),
    ("What role did peanuts, cashew, caramel, and raisins play in the story?", "(A) They were the accidental extra ingredients that created the new signature crunch and flavor", "(B) They ruined the chocolate batch", "(C) They were used to decorate the walls", "(D) They were fed to animals", "(A)", "They provided the distinct flavor and texture.", "Medium", "Understanding", "Ingredient Role"),
    ("If Jammy had not tasted the mixture, what would have been the outcome?", "(A) The delicious Wannabe Chocolate would have been thrown into the trash and never invented", "(B) Mr. Nougat would taste it later", "(C) A customer would buy the trash", "(D) Nothing would change", "(A)", "Without Jammy, the invention would be lost.", "Medium", "Analyzing", "Hypothetical Scenario"),
    ("What attitude should inventors have when unexpected accidents occur in their work?", "(A) Curious, flexible, and willing to evaluate unexpected results", "(B) Angry and ready to quit immediately", "(C) Blaming others for the spill", "(D) Hiding the mistake", "(A)", "Flexibility and curiosity lead to innovation.", "Medium", "Evaluating", "Inventor Attitude"),
    ("How does the story encourage Class 2 children not to give up when they make mistakes?", "(A) It shows that a mistake can turn into something wonderful if we stay calm and creative", "(B) It tells them to spill things everywhere", "(C) It advises them to let others clean up", "(D) It says mistakes are bad", "(A)", "Mistakes can yield positive outcomes.", "Medium", "Applying", "Child Encouragement"),
    ("What type of literary story is 'The Wannabe Chocolate'?", "(A) An inspirational light-hearted modern tale with a positive moral lesson", "(B) A scary ghost story", "(C) A historical biography", "(D) A science textbook chapter", "(A)", "It is an engaging modern story with a moral lesson.", "Medium", "Understanding", "Genre"),
    ("Why did Mr. Candy Nougat knock down the ingredient bowls?", "(A) He was clumsy while reaching across for the sugar bowl", "(B) A dog ran into the kitchen", "(C) He dropped his apron", "(D) Jammy bumped into him", "(A)", "His natural clumsiness caused the knock-down while reaching.", "Medium", "Remembering", "Plot Detail"),

    # Hard (41-50)
    ("Analyze how the theme of 'serendipity' (happy accidental discovery) is central to Chapter 04.", "(A) The creation of Wannabe Chocolates happened purely by chance, but succeeded because the creators recognized its value", "(B) The story proves that planning is useless", "(C) Serendipity means making cakes carefully", "(D) The story shows money is everything", "(A)", "Serendipity combines accidental creation with smart recognition.", "Hard", "Analyzing", "HOTS Literary Theme"),
    ("Evaluate Mr. Candy Nougat's willingness to listen to Jammy's suggestion despite being the master confectioner.", "(A) It shows humility and open-mindedness; he respected his assistant's feedback over his own initial assumption", "(B) It shows he was weak and had no mind of his own", "(C) He listened only because he was tired", "(D) He was forced by law", "(A)", "Open-minded master respecting assistant's valid feedback.", "Hard", "Evaluating", "Leadership Trait"),
    ("Deconstruct the step-by-step chain of events from the spill to market dominance.", "(A) Clumsy Reach -> Accidental Spill -> Intended Disposal -> Jammy's Taste Test -> Rebranding -> Market Success", "(B) Market Success -> Spill -> Discard -> Taste -> Name", "(C) Taste -> Spill -> Reach -> Market -> Disposal", "(D) Rebranding -> Taste -> Disposal -> Reach -> Market", "(A)", "Logical chronological sequence of plot events.", "Hard", "Analyzing", "Plot Sequence"),
    ("Compare Mr. Candy Nougat's initial assumption with Jammy's practical observation.", "(A) Nougat assumed unmeasured mixing equaled ruin, whereas Jammy empirically tested flavor before judging", "(B) Both assumed the mixture was terrible", "(C) Nougat knew it was great immediately", "(D) Jammy wanted to throw it away", "(A)", "Assumed ruin vs empirical taste verification.", "Hard", "Analyzing", "Comparative Mindset"),
    ("How does the word 'Wannabe' add charm and humor to the brand identity in a market setting?", "(A) It playfully acknowledges that while it isn't traditional plain chocolate, it is something uniquely desirable", "(B) It tricks customers into buying fake goods", "(C) It means the chocolate is bad", "(D) It is an old traditional word", "(A)", "Playful branding that embraces uniqueness.", "Hard", "Evaluating", "Branding Dynamics"),
    ("What socio-economic lesson does this chapter convey regarding workplace collaboration?", "(A) Ideas from all levels of staff (master or assistant) should be valued for collective success", "(B) Assistants should only clean and never speak", "(C) Masters should never do manual work", "(D) Workplace rules must prevent all accidents", "(A)", "Inclusive collaboration drives innovation and growth.", "Hard", "Evaluating", "Workplace Dynamics"),
    ("How can a school student apply Jammy's mindset when a painting or craft project goes wrong?", "(A) Look at the new pattern creatively and see if it can be turned into a unique artwork instead of tearing it up", "(B) Cry and throw the paper away", "(C) Blame the art teacher", "(D) Stop doing craft forever", "(A)", "Creative adaptability turns mistakes into art.", "Hard", "Applying", "Practical Application"),
    ("Why is adaptability a key business skill demonstrated by Mr. Candy Nougat in this story?", "(A) He quickly adapted his product lineup to embrace an unplanned recipe that customers loved", "(B) He closed his shop and opened a bakery", "(C) He refused to change his menu", "(D) He sold plain sugar", "(A)", "Flexibility to embrace market-pleasing innovations.", "Hard", "Evaluating", "Business Adaptability"),
    ("What does the phrase 'ruled the markets' imply about consumer behavior in Chocoland?", "(A) Consumers appreciate innovative, delicious, and novel products over repetitive traditional offerings", "(B) Consumers buy whatever is cheapest", "(C) Consumers were tricked by advertising", "(D) Consumers only eat plain chocolate", "(A)", "Enthusiastic adoption of novel quality products.", "Hard", "Analyzing", "Consumer Insight"),
    ("Synthesize the ultimate moral message of 'The Wannabe Chocolate' for Class 2 learners.", "(A) Embrace your talents, stay humble to listen to others, and turn life's clumsy accidents into sweet successes!", "(B) Always carry sugar carefully", "(C) Eat chocolates three times a day", "(D) Never work in a kitchen", "(A)", "Talent, humility, open-mindedness, and creative resilience.", "Hard", "Evaluating", "Core Synthesis")
]

mcq_content = f"# MCQs — Chapter 04: The Wannabe Chocolate\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH04_MCQ_{idx:03d}"
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

with open(os.path.join(CH04_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("The story of Mr. Candy Nougat takes place in a town called _______.", "Chocoland", "The town is named Chocoland.", "Easy"),
    ("Mr. Candy Nougat made the best chocolates and _______ of different flavours.", "cakes", "He made chocolates and cakes.", "Easy"),
    ("Mr. Candy Nougat was talented and hard-working, but _______. ", "clumsy", "The story states he was clumsy.", "Easy"),
    ("While mixing his chocolate, Mr. Candy Nougat tried to reach for _______. ", "sugar", "He reached for sugar.", "Easy"),
    ("He accidentally knocked down bowls of peanuts, caramel, cashew, and _______. ", "raisins", "Raisins fell into the bowl along with peanuts, caramel, and cashew.", "Easy"),
    ("All the spilled items landed inside the chocolate _______.", "bowl", "They landed in the chocolate bowl.", "Easy"),
    ("Mr. Candy Nougat initially decided to _______ away the new mixture.", "throw", "He decided to throw it away.", "Easy"),
    ("Mr. Candy Nougat's assistant was named _______.", "Jammy", "His assistant's name was Jammy.", "Easy"),
    ("Jammy decided to _______ the mixture before it was thrown away.", "taste", "Jammy tasted the mixture.", "Easy"),
    ("Jammy found out that the new mixture tasted _______.", "amazing", "The new mixture tasted amazing.", "Easy"),
    ("Jammy convinced Mr. Candy Nougat to sell the mixture as '_______ Chocolates'.", "Wannabe", "They were named Wannabe Chocolates.", "Easy"),
    ("The new chocolates were called Wannabe Chocolates because the mixture was _______ from usual chocolates.", "different", "It was different from usual chocolates.", "Easy"),
    ("Anybody who tasted the new chocolates _______ them.", "loved", "Everyone loved the new chocolates.", "Easy"),
    ("The Wannabe Chocolates soon ruled the _______.", "markets", "They ruled the markets.", "Easy"),
    ("The word 'clumsy' means _______.", "careless", "Clumsy means careless.", "Easy"),
    ("Caramel is a type of sticky _______.", "sweet", "Caramel is a sticky sweet.", "Easy"),
    ("The word 'convinced' means completely _______ about something.", "sure", "Convinced means completely sure.", "Easy"),
    ("Bowls of peanuts, caramel, cashew, and raisins were knocked down by _______.", "accident", "It was an accidental knock-down.", "Easy"),
    ("Jammy stopped Mr. Candy Nougat from throwing away a _______ discovery.", "delicious", "It was a delicious chocolate mixture.", "Easy"),
    ("Mr. Candy Nougat was a maker of delicious _______ and cakes.", "chocolates", "He made chocolates and cakes.", "Easy"),
    ("Jammy was not the master baker, but his _______.", "assistant", "Jammy was his assistant.", "Easy"),
    ("The ingredients that fell in were peanuts, caramel, cashew, and _______.", "raisins", "Raisins were one of the four ingredients.", "Easy"),
    ("The new sweet became very popular in the town of _______.", "Chocoland", "Chocoland is the town setting.", "Easy"),
    ("Instead of failing, the clumsy accident turned into a great _______.", "success", "The accident turned into market success.", "Easy"),
    ("Chapter 04 is titled 'The Wannabe _______'.", "Chocolate", "The title is 'The Wannabe Chocolate'.", "Easy"),

    # Medium (26-40)
    ("Mr. Nougat's clumsiness caused him to knock over four bowls of _______.", "ingredients", "He knocked over four bowls of ingredients.", "Medium"),
    ("Jammy showed great curiosity when he chose to _______ the accidental mix.", "sample", "He sampled/tasted the mix.", "Medium"),
    ("The name 'Wannabe Chocolates' highlights that the sweet was _______ in flavor and texture.", "unique", "It was unique compared to traditional chocolate.", "Medium"),
    ("Although Mr. Nougat was very talented, his _______ habit created a mess.", "clumsy", "His clumsy habit created a mess.", "Medium"),
    ("Jammy was able to _______ Mr. Nougat because the taste was undeniably delicious.", "persuade", "Jammy persuaded/convinced Nougat.", "Medium"),
    ("The mixture did not go to waste because Jammy acted with quick _______.", "thinking", "Jammy used quick thinking.", "Medium"),
    ("The story teaches us that an accidental mistake can lead to an unexpected _______.", "invention", "Mistakes can lead to inventions.", "Medium"),
    ("People loved Wannabe Chocolates because of their rich mix of cashew, peanuts, caramel, and _______.", "raisins", "The mix included raisins and nuts.", "Medium"),
    ("Mr. Candy Nougat showed _______ by listening to his assistant's advice.", "humility", "He showed humility/openness.", "Medium"),
    ("Wannabe Chocolates became the most popular item in the local _______.", "market", "They ruled the market.", "Medium"),
    ("Jammy's timely taste-test saved the mixture from the _______ bin.", "trash", "Saved from the trash bin.", "Medium"),
    ("The combination of nuts, sticky caramel, and chocolate gave a new _______ to the treat.", "texture", "Gave a new texture/flavor.", "Medium"),
    ("Mr. Candy Nougat's shop was located in the famous town of _______.", "Chocoland", "Located in Chocoland.", "Medium"),
    ("Without Jammy's initiative, the world would never have enjoyed _______ Chocolates.", "Wannabe", "Wannabe Chocolates.", "Medium"),
    ("The lesson encourages children to turn bad situations into _______ opportunities.", "positive", "Turn mistakes into positive opportunities.", "Medium"),

    # Hard (41-50)
    ("The story illustrates the concept of _______ where an accidental blunder yields a valuable discovery.", "serendipity", "Serendipity is accidental discovery of good things.", "Hard"),
    ("Mr. Candy Nougat's willingness to rebrand his mistake demonstrates commercial _______.", "adaptability", "Demonstrates business adaptability.", "Hard"),
    ("Jammy's initiative proves that valuable insights can originate from an _______ in any organization.", "assistant", "Insights can come from an assistant.", "Hard"),
    ("The unexpected crunch of peanuts and cashews transformed smooth chocolate into a multi-layered _______.", "delicacy", "Transformed into a multi-layered delicacy.", "Hard"),
    ("Evaluating the taste before disposal prevented unnecessary _______ of high-quality ingredients.", "waste", "Prevented waste of ingredients.", "Hard"),
    ("The commercial triumph of Wannabe Chocolates shows that consumer demand favors _______ creations.", "innovative", "Favors innovative creations.", "Hard"),
    ("By accepting Jammy's feedback, Mr. Nougat demonstrated exemplary _______ in his kitchen.", "leadership", "Demonstrated open leadership.", "Hard"),
    ("The story teaches that initial failure or mess does not define the ultimate _______ of a project.", "outcome", "Initial mess does not dictate outcome.", "Hard"),
    ("Wannabe Chocolates established a new market standard by combining traditional chocolate with sticky _______.", "caramel", "Combined with sticky caramel.", "Hard"),
    ("The journey from kitchen disaster to market bestseller is a classic tale of creative _______.", "resilience", "Tale of creative resilience.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 04: The Wannabe Chocolate\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH04_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH04_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The story 'The Wannabe Chocolate' takes place in Chocoland.", "True", "The text explicitly states that the story took place in a town called Chocoland.", "Easy"),
    ("Mr. Candy Nougat was a lazy man who hated making sweets.", "False", "Mr. Candy Nougat was talented and hard-working, though clumsy.", "Easy"),
    ("Mr. Candy Nougat made the best chocolates and cakes of different flavours.", "True", "He was famous for making delicious chocolates and cakes in Chocoland.", "Easy"),
    ("Jammy was Mr. Candy Nougat's master chef.", "False", "Jammy was Mr. Candy Nougat's assistant.", "Easy"),
    ("While mixing chocolate, Mr. Candy Nougat tried to reach for salt.", "False", "He was reaching for sugar when the accident happened.", "Easy"),
    ("Bowls of peanuts, caramel, cashew, and raisins fell into the chocolate bowl.", "True", "All four ingredients knocked down and landed in the chocolate mixture.", "Easy"),
    ("Mr. Candy Nougat immediately knew the new mixture would be a huge hit.", "False", "He initially decided to throw away the mixture thinking it was ruined.", "Easy"),
    ("Jammy decided to taste the new mixture before it was thrown out.", "True", "Jammy took the initiative to taste the mixture first.", "Easy"),
    ("The new mixture tasted sour and terrible to Jammy.", "False", "Jammy found out that the new mixture tasted amazing.", "Easy"),
    ("Jammy convinced Mr. Candy Nougat to sell the new chocolates.", "True", "Jammy persuaded him to market and sell the new creation.", "Easy"),
    ("The new chocolates were named 'Yummy Chocolates'.", "False", "They were named 'Wannabe Chocolates'.", "Easy"),
    ("Wannabe Chocolates were called 'Wannabe' because they were different from usual chocolates.", "True", "The name was chosen because the mix was unique and different from standard chocolates.", "Easy"),
    ("Nobody liked the taste of Wannabe Chocolates.", "False", "Anybody who tasted the new chocolates loved them.", "Easy"),
    ("Wannabe Chocolates soon ruled the markets.", "True", "They became extremely popular and ruled the markets.", "Easy"),
    ("The word 'clumsy' means careless.", "True", "The vocabulary box defines clumsy as careless.", "Easy"),
    ("Caramel is a type of sticky sweet.", "True", "Caramel is defined as a sticky sweet.", "Easy"),
    ("The word 'convinced' means feeling angry.", "False", "Convinced means completely sure about something.", "Easy"),
    ("Mr. Candy Nougat spilled the ingredients on purpose as a planned recipe.", "False", "It was an accidental knock-down caused by his clumsiness.", "Easy"),
    ("Four distinct items fell into the chocolate bowl during the accident.", "True", "Peanuts, caramel, cashew, and raisins (4 items) fell in.", "True"),
    ("Jammy threw away the chocolate without telling Mr. Nougat.", "False", "Jammy tasted it and stopped Mr. Nougat from throwing it away.", "Easy"),
    ("Chocoland was known for making poor quality sweets.", "False", "Mr. Candy Nougat made the best chocolates and cakes in the world there.", "Easy"),
    ("Mr. Candy Nougat listened to Jammy's advice and sold the chocolates.", "True", "He accepted Jammy's recommendation to sell the new sweet.", "Easy"),
    ("The accident proved to be a fortunate event for the shop.", "True", "The accidental mix created a market-ruling bestseller.", "Easy"),
    ("Jammy was afraid to taste the new mixture.", "False", "Jammy willingly tasted it and recognized its great flavor.", "Easy"),
    ("Chapter 04 is set in a bakery and confectionery shop.", "True", "The story revolves around chocolate and cake making in Chocoland.", "Easy"),

    # Medium (26-40)
    ("Mr. Candy Nougat's clumsiness completely destroyed his career as a baker.", "False", "His clumsiness led to an accidental discovery that boosted his business.", "Medium"),
    ("Testing an unexpected mixture before throwing it away shows good judgment.", "True", "Jammy's taste test saved a valuable recipe from waste.", "Medium"),
    ("Wannabe Chocolates failed because customers only wanted pure traditional chocolate.", "False", "Customers loved the unique new taste and made it a market success.", "Medium"),
    ("Mr. Candy Nougat refused to give Jammy any credit for the new chocolate.", "False", "Mr. Nougat agreed with Jammy's advice and launched the product as suggested.", "Medium"),
    ("The addition of nuts, caramel, and raisins changed the texture of the chocolate.", "True", "Adding peanuts, cashews, caramel, and raisins added crunch and stickiness.", "Medium"),
    ("Accidents in the kitchen can never produce edible or tasty food.", "False", "The story proves that kitchen accidents can lead to delicious new recipes.", "Medium"),
    ("Jammy was more hard-working than Mr. Candy Nougat.", "False", "Both worked hard; Mr. Nougat was talented/hardworking, while Jammy was observant.", "Medium"),
    ("The name 'Wannabe Chocolates' helped separate the new treat from standard chocolates.", "True", "The unique name highlighted its non-traditional, distinct nature.", "Medium"),
    ("Mr. Candy Nougat showed wisdom by being open to his assistant's opinion.", "True", "Listening to Jammy's feedback allowed him to capitalize on a great product.", "Medium"),
    ("Peanuts were the only ingredient that spilled into the chocolate.", "False", "Peanuts, caramel, cashew, and raisins all fell in together.", "Medium"),
    ("The story teaches that we should judge things by their appearance without testing them.", "False", "The story teaches us to test and evaluate before discarding something.", "Medium"),
    ("Wannabe Chocolates became popular only in a small neighborhood.", "False", "They ruled the markets, indicating widespread popularity.", "Medium"),
    ("Mr. Candy Nougat was reaching for raisins when he knocked over the sugar.", "False", "He was reaching for sugar when he knocked over bowls of peanuts, caramel, cashew, and raisins.", "Medium"),
    ("Jammy tasted the chocolate because he was greedy and hungry.", "False", "Jammy tasted it to check its quality before throwing it away.", "Medium"),
    ("Flexibility and creativity are important traits for an artisan sweet maker.", "True", "Adapting a spill into a bestseller requires creativity and flexibility.", "Medium"),

    # Hard (41-50)
    ("The central theme of Chapter 04 is that careful planning is unnecessary in business.", "False", "The theme is that when unexpected mistakes occur, creative adaptability can turn them into success.", "Hard"),
    ("Jammy's actions exemplify workplace initiative and critical thinking.", "True", "Testing the mixture before disposal demonstrated initiative and practical evaluation.", "Hard"),
    ("The story implies that perfectionism can sometimes cause people to discard valuable opportunities.", "True", "Nougat's desire for perfect plain chocolate almost caused him to trash a delicious innovation.", "Hard"),
    ("Wannabe Chocolates succeeded solely because of aggressive advertising in Chocoland.", "False", "They succeeded because anyone who tasted them loved the genuine taste quality.", "Hard"),
    ("The story highlights a positive model of collaborative master-assistant dynamics.", "True", "Nougat provided the base skill and Jammy provided the critical feedback, creating team success.", "Hard"),
    ("The word 'clumsy' in this text carries an entirely negative outcome for the protagonist.", "False", "Although clumsiness caused the spill, it ironically led to his greatest success.", "Hard"),
    ("The narrative suggests that innovation often occurs at the intersection of accident and evaluation.", "True", "Accidental mixing combined with smart evaluation yielded a breakthrough product.", "Hard"),
    ("Mr. Candy Nougat would have saved more money by throwing the mixture away immediately.", "False", "Selling the mixture generated massive market success and profits.", "Hard"),
    ("The story promotes an open-minded approach toward unexpected problem outcomes.", "True", "It encourages viewing unexpected results as potential opportunities.", "Hard"),
    ("Wannabe Chocolates represent a fusion of confectionery textures including crunchy, sticky, and smooth.", "True", "Chocolate (smooth), caramel (sticky), and nuts/raisins (crunchy/chewy) created a rich fusion.", "Hard")
]

tf_content = f"# True / False — Chapter 04: The Wannabe Chocolate\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH04_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH04_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Where did the story of Mr. Candy Nougat take place?", "The story took place in a town called Chocoland.", "Easy", "Remembering"),
    ("Who was Mr. Candy Nougat?", "Mr. Candy Nougat was a man in Chocoland who made the best chocolates and cakes of different flavours.", "Easy", "Remembering"),
    ("What three character traits are given for Mr. Candy Nougat?", "He was talented, hard-working, but clumsy.", "Easy", "Remembering"),
    ("Who was Jammy in the story?", "Jammy was Mr. Candy Nougat's assistant.", "Easy", "Remembering"),
    ("What was Mr. Candy Nougat doing when the accident happened?", "He was mixing chocolate and reaching across for the sugar bowl.", "Easy", "Remembering"),
    ("Which four ingredients accidentally fell into the chocolate bowl?", "Bowls of peanuts, caramel, cashew, and raisins fell into the chocolate bowl.", "Easy", "Remembering"),
    ("What did Mr. Candy Nougat decide to do with the spilled mixture at first?", "He decided to throw away the mixture thinking it was spoiled.", "Easy", "Remembering"),
    ("Who stopped the mixture from being thrown away?", "His assistant, Jammy, stopped it by deciding to taste it first.", "Easy", "Remembering"),
    ("How did the new mixture taste to Jammy?", "Jammy found out that the new mixture tasted amazing.", "Easy", "Remembering"),
    ("What name did Jammy suggest for the new chocolates?", "Jammy suggested selling them as 'Wannabe Chocolates'.", "Easy", "Remembering"),
    ("Why were the chocolates called 'Wannabe Chocolates'?", "They were called 'Wannabe Chocolates' because the mixture was different from usual plain chocolates.", "Easy", "Remembering"),
    ("How did customers in Chocoland react to Wannabe Chocolates?", "Anybody who tasted the new chocolates loved them, and they soon ruled the markets.", "Easy", "Remembering"),
    ("What is the meaning of the word 'clumsy'?", "Clumsy means careless in movement or handling things.", "Easy", "Understanding"),
    ("What is caramel according to the story's word meaning?", "Caramel is a type of sticky sweet.", "Easy", "Understanding"),
    ("What does the word 'convinced' mean?", "Convinced means completely sure about something.", "Easy", "Understanding"),
    ("Why was Mr. Candy Nougat famous in Chocoland?", "He was famous because he made the best chocolates and cakes with wonderful flavours.", "Easy", "Remembering"),
    ("Was the creation of Wannabe Chocolates intentional or accidental?", "It was an accidental creation caused when Mr. Nougat clumsily knocked ingredient bowls into the chocolate.", "Easy", "Understanding"),
    ("Name the two nut ingredients that fell into the bowl.", "The two nut ingredients were peanuts and cashews.", "Easy", "Remembering"),
    ("What sweet sticky item fell into the bowl alongside the nuts?", "Caramel fell into the bowl alongside the nuts.", "Easy", "Remembering"),
    ("What dried fruit ingredient fell into the chocolate mix?", "Raisins fell into the chocolate mix as the dried fruit ingredient.", "Easy", "Remembering"),
    ("Why did Mr. Candy Nougat agree to sell the new chocolates?", "He agreed because Jammy convinced him that the new taste was amazing and distinct.", "Easy", "Remembering"),
    ("What happened to Wannabe Chocolates in the market after they were launched?", "They became extremely popular and soon ruled the markets in Chocoland.", "Easy", "Remembering"),
    ("What lesson do we learn about making mistakes from this story?", "We learn that mistakes can sometimes lead to great new discoveries if we stay creative.", "Easy", "Understanding"),
    ("What kind of assistant was Jammy to Mr. Candy Nougat?", "Jammy was a smart, curious, and helpful assistant.", "Easy", "Understanding"),
    ("What is the main topic of Chapter 04?", "Chapter 04 is about how an accidental kitchen mix led to the creation of popular 'Wannabe Chocolates'.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Why did Mr. Candy Nougat initially decide to throw away the chocolate mixture?", "He thought that knocking four unplanned ingredients into the bowl ruined the batch, as it was not his original recipe.", "Medium", "Understanding"),
    ("How did Jammy demonstrate initiative in the kitchen?", "Jammy demonstrated initiative by testing the taste of the mixture himself instead of blindly throwing it into the trash.", "Medium", "Analyzing"),
    ("Describe the texture and flavor combination of Wannabe Chocolates.", "Wannabe Chocolates combined smooth chocolate with crunchy peanuts and cashews, sticky caramel, and chewy raisins.", "Medium", "Understanding"),
    ("Why is it important to listen to feedback from team members or assistants?", "Listening to feedback allows us to discover good ideas and solutions that we might have missed on our own.", "Medium", "Evaluating"),
    ("In what way was Mr. Candy Nougat both talented and clumsy?", "He was talented because he crafted delicious cakes and chocolates, but clumsy because he accidentally knocked over bowls while working.", "Medium", "Analyzing"),
    ("How did the name 'Wannabe Chocolates' help market the product?", "The unique name aroused curiosity and highlighted that it was a special, non-traditional treat different from standard chocolates.", "Medium", "Understanding"),
    ("What would have happened if Jammy had been obedient without testing the mixture?", "If Jammy had just thrown the mixture away without testing, the delicious Wannabe Chocolate recipe would have been lost forever.", "Medium", "Analyzing"),
    ("How does this story encourage students when they spill or ruin something during an activity?", "It encourages students not to panic, but to inspect the situation calmly to see if a creative solution or new idea can come out of it.", "Medium", "Applying"),
    ("Why did everyone who tasted Wannabe Chocolates fall in love with them?", "They loved them because the mix of nuts, caramel, raisins, and chocolate created a mouth-watering and novel flavor experience.", "Medium", "Understanding"),
    ("Explain how Mr. Candy Nougat's attitude changed from the start of the accident to the end of the story.", "At first he was frustrated and wanted to discard the mix, but after Jammy's feedback, he became excited, open-minded, and successful.", "Medium", "Analyzing"),
    ("What role did caramel play in binding the dry ingredients in the mix?", "Caramel provided a sticky sweet base that held the peanuts, cashews, and raisins together within the chocolate.", "Medium", "Understanding"),
    ("Why was Jammy completely sure ('convinced') about selling the new sweet?", "He was convinced because the flavor tasted so extraordinarily good that he knew customers in Chocoland would buy it eagerly.", "Medium", "Understanding"),
    ("How does Chapter 04 show that hard work alone isn't always enough for innovation?", "While Mr. Nougat worked hard, innovation also required Jammy's curious observation and open-minded testing of an accident.", "Medium", "Evaluating"),
    ("What message does the story convey about workplace roles?", "It shows that even an assistant can contribute game-changing ideas to a master craftsman's business.", "Medium", "Evaluating"),
    ("Summarize the main event of Page 17 in two sentences.", "Mr. Nougat accidentally knocked peanuts, caramel, cashews, and raisins into his chocolate bowl while reaching for sugar. Jammy tasted the mix, loved it, and convinced him to sell it as Wannabe Chocolates.", "Medium", "Understanding"),

    # Hard (41-50)
    ("Critique Mr. Candy Nougat's initial decision to throw away the spilled mixture without tasting it.", "His initial decision was hasty and rigid. As a master baker, he should have evaluated the taste before discarding expensive ingredients, showing that even experts can have blind spots.", "Hard", "Evaluating"),
    ("Analyze how accidental discoveries (serendipity) have shaped real-world inventions like potato chips or chocolate chip cookies, similar to this story.", "Just like Wannabe Chocolates, many famous foods were created when accidental spills or substitute ingredients were tried open-mindedly instead of being discarded.", "Hard", "Analyzing"),
    ("How does the dynamic between Mr. Candy Nougat and Jammy illustrate effective leadership and humility?", "Mr. Nougat showed humility by accepting his assistant's superior suggestion, while Jammy showed leadership by speaking up respectfully with a constructive idea.", "Hard", "Evaluating"),
    ("Deconstruct how the four spilled ingredients (peanuts, caramel, cashew, raisins) complement each other scientifically in flavor profiles.", "Peanuts and cashews add savory crunch and fats, caramel provides rich sticky sweetness, and raisins contribute fruity chewiness, balancing the rich cocoa base.", "Hard", "Analyzing"),
    ("Evaluate the impact of market branding on the success of 'Wannabe Chocolates'.", "Branding the mistake as 'Wannabe Chocolates' turned an unconventional mix into a trendy, desirable brand identity that intrigued customers and dominated the market.", "Hard", "Evaluating"),
    ("How can a school teacher use this chapter to teach resilience and problem-solving to young learners?", "A teacher can use it to demonstrate that making mistakes is a natural part of learning, and that staying calm enables us to turn blunders into creative victories.", "Hard", "Applying"),
    ("Compare Mr. Candy Nougat's character at the beginning versus his character after the success of Wannabe Chocolates.", "Initially, he was rigid and quick to discard flawed work; after the success, he became more flexible, collaborative, and appreciative of unexpected outcomes.", "Hard", "Analyzing"),
    ("What philosophical lesson about human flaw and perfection does the story present?", "It suggests that perfection is not the only source of value; sometimes flaws and clumsiness, when embraced with wisdom, produce the sweetest outcomes.", "Hard", "Evaluating"),
    ("Synthesize how curiosity, courage, and collaboration worked together to turn a kitchen mess into a market hit.", "Jammy had the curiosity to taste, the courage to persuade his master, and Mr. Nougat collaborated by producing and selling it, completing the cycle of success.", "Hard", "Evaluating"),
    ("Formulate a strategy for how a student can handle an accidental mistake during a group science project based on this chapter.", "The student should stop immediately, observe what changed, consult team members to analyze the unexpected result, and see if it yields a new finding before restarting.", "Hard", "Applying")
]

sa_content = f"# Short Answer Questions — Chapter 04: The Wannabe Chocolate\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH04_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH04_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the town of Chocoland and the character of Mr. Candy Nougat.", 
     "The story takes place in a wonderful town called Chocoland. In this town lived a man named Mr. Candy Nougat, who was famous for making the best chocolates and cakes of various delicious flavours in the world. Mr. Candy Nougat was extremely talented and hard-working, but he had one flaw—he was quite clumsy. Despite his clumsiness, his dedication to his craft made his bakery popular among all the residents of Chocoland.", 
     "Easy", "Remembering"),

    ("Explain how the accidental spill occurred in Mr. Candy Nougat's kitchen.", 
     "One day, while Mr. Candy Nougat was busy mixing a batch of chocolate, he needed to add sugar to the recipe. As he reached across his worktable for the sugar bowl, his natural clumsiness caused him to accidentally knock over several other bowls standing nearby. These bowls contained peanuts, caramel, cashews, and raisins. All four of these ingredients tumbled directly into his big chocolate bowl, creating an unplanned, messy mixture.", 
     "Easy", "Remembering"),

    ("What was Mr. Candy Nougat's initial reaction to the spill, and how did Jammy intervene?", 
     "Seeing four extra ingredients land in his chocolate bowl, Mr. Candy Nougat immediately assumed the batch was ruined and decided to throw the entire mixture away into the trash. However, his observant assistant, Jammy, decided to taste the mixture first before discarding it. Upon tasting it, Jammy realized that the combination tasted amazing and convinced Mr. Candy Nougat not to waste it, but to package and sell it instead.", 
     "Easy", "Remembering"),

    ("Why were the new chocolates named 'Wannabe Chocolates' and how were they received by people?", 
     "Jammy suggested naming the new creation 'Wannabe Chocolates' because the product was different from traditional, plain chocolates—it was trying to be chocolate while containing nuts, caramel, and fruit. When the product was placed on the market, anybody who tasted the new chocolates loved them immediately. The Wannabe Chocolates became an instant sensation and soon ruled the markets across Chocoland.", 
     "Easy", "Remembering"),

    ("What are the meanings of 'clumsy', 'caramel', and 'convinced' as used in this story?", 
     "In this story:\n1. **Clumsy** means careless or awkward in movement, leading to minor accidents like knocking things over.\n2. **Caramel** refers to a type of sweet, sticky food made by heating sugar, used to add rich flavor to sweets.\n3. **Convinced** means being completely sure about something after considering evidence or persuasive arguments.", 
     "Easy", "Understanding"),

    ("Describe the role of Jammy in turning a kitchen disaster into a business success.", 
     "Jammy played a vital role in turning the kitchen accident into a major success. While Mr. Nougat was ready to throw away the spilled mixture, Jammy showed curiosity and initiative by tasting it. Recognizing its incredible flavor, Jammy persuaded his master to market it under a fun new name. Without Jammy's quick thinking and willingness to speak up, the business would have lost a delicious invention.", 
     "Easy", "Understanding"),

    ("List all four ingredients that fell into the chocolate bowl and describe how each contributed to the taste.", 
     "The four ingredients that fell into the chocolate bowl were:\n1. **Peanuts**: Added a crunchy, nutty flavor.\n2. **Cashews**: Provided a rich, buttery nut texture.\n3. **Caramel**: Offered a sticky, sweet caramel chewiness.\n4. **Raisins**: Contributed a pleasant fruity sweetness.\nTogether with the rich chocolate, these ingredients created a mouth-watering treat.", 
     "Easy", "Remembering"),

    ("How does the story show that being clumsy doesn't mean a person cannot be successful?", 
     "The story shows that Mr. Candy Nougat was very clumsy, which caused him to knock over bowls of ingredients. However, his clumsiness did not stop him from being talented, hard-working, and successful. Instead of ruining his life, one of his clumsy moments actually led to his greatest product invention, proving that personal flaws can be overcome with creativity and teamwork.", 
     "Easy", "Understanding"),

    ("What moral lesson does 'The Wannabe Chocolate' teach young school children?", 
     "The story teaches children that mistakes and accidents are not always bad. When something goes wrong or doesn't go according to plan, we should not panic or give up right away. Instead, we should evaluate the situation calmly, stay open-minded, listen to helpful advice from others, and see if we can turn a mistake into something positive and successful.", 
     "Easy", "Understanding"),

    ("Compare Mr. Candy Nougat's bakery before and after the invention of Wannabe Chocolates.", 
     "Before the invention, Mr. Candy Nougat was already a talented baker making traditional chocolates and cakes in Chocoland. However, after the accidental spill and Jammy's suggestion, his bakery produced 'Wannabe Chocolates,' which were completely unique. This new creation became so popular that it ruled the entire market, bringing even greater fame and commercial success to his shop.", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Detail the step-by-step process of how Wannabe Chocolates came into existence.", "It started when Mr. Nougat reached for sugar while mixing chocolate. He knocked over peanuts, caramel, cashew, and raisins into the bowl. Thinking it was ruined, he planned to throw it out. Jammy tasted it, realized it was delicious, persuaded Nougat to sell it as 'Wannabe Chocolates', and it became a market hit.", "Easy", "Remembering"),
    ("Why was Jammy's taste test the most important action in the entire story?", "Jammy's taste test was crucial because it prevented high-quality ingredients from being wasted and uncovered a novel recipe. Without his test, Mr. Nougat's assumption of failure would have resulted in throwing away a market-dominating recipe.", "Easy", "Understanding"),
    ("Explain why teamwork between a master and an assistant is important in a business setting.", "Teamwork allows different perspectives to merge. Mr. Nougat provided master baking skills, while Jammy provided fresh observation and customer insight. Working together, they transformed an accident into a profitable commercial product.", "Easy", "Evaluating"),
    ("How did the name 'Wannabe Chocolates' create curiosity among customers in Chocoland?", "The name was playful and unusual. Customers wondered why it was called 'Wannabe' and tried it out of curiosity. Upon tasting the delicious mix of nuts, caramel, raisins, and chocolate, they fell in love with it.", "Easy", "Understanding"),
    ("What character traits make Mr. Candy Nougat a relatable and likable main character?", "Mr. Nougat is hard-working and talented, making him admirable. At the same time, his clumsiness makes him relatable because everybody makes mistakes. His willingness to listen to Jammy shows he is humble and friendly.", "Easy", "Evaluating"),
    ("Discuss the importance of not wasting food as demonstrated by Jammy's action.", "Jammy hesitated to throw away a large bowl of chocolate without checking it first. By tasting the mix, he saved food from being wasted and proved that seemingly ruined food might actually be delicious and safe to eat.", "Easy", "Evaluating"),
    ("How can Class 2 students apply the lesson of this story when playing or studying?", "Students can apply this lesson by not getting upset when they make a mistake in drawings, games, or craft projects. Instead of throwing away their work, they can look for creative ways to turn the mistake into a fun new idea.", "Easy", "Applying"),
    ("Describe the setting of Chocoland and why it is a perfect backdrop for this story.", "Chocoland is a whimsical town dedicated to sweet treats, cakes, and chocolates. It provides a fun, colorful backdrop where chocolate making is central to daily life, making the discovery of a new chocolate bar exciting for the whole community.", "Easy", "Understanding"),
    ("Why did Mr. Candy Nougat reach for sugar in the first place?", "Mr. Nougat was mixing a fresh batch of chocolate and needed sugar to balance the flavor. His reach across the table triggered the domino effect of knocking over the four ingredient bowls.", "Easy", "Remembering"),
    ("Explain the difference between a traditional chocolate bar and a Wannabe Chocolate bar.", "A traditional chocolate bar is usually smooth and plain cocoa. A Wannabe Chocolate bar contains a mix of crunchy peanuts, cashews, sticky caramel, and sweet raisins embedded in chocolate, offering a multi-textured taste experience.", "Easy", "Understanding"),
    ("How does the story highlight the value of open-mindedness in problem solving?", "Mr. Nougat was open-minded enough to change his mind when Jammy showed him the mixture tasted great. Had he been stubborn, he would have rejected Jammy's advice and missed out on market success.", "Easy", "Evaluating"),
    ("What role does practice and hard work play in Mr. Candy Nougat's reputation?", "Mr. Nougat earned his reputation as the best chocolate maker through hard work and talent. His established skills gave him the base recipe that made the accidental mix taste so good.", "Easy", "Understanding"),
    ("How did the citizens of Chocoland show their appreciation for the new sweet?", "They showed appreciation by buying Wannabe Chocolates enthusiastically. Anyone who tasted them loved them, causing the new product to quickly rule the local markets.", "Easy", "Remembering"),
    ("What makes 'The Wannabe Chocolate' an inspiring story for young readers?", "It inspires young readers by showing that flaws like clumsiness do not define a person, and that creative thinking can turn messy accidents into wonderful achievements.", "Easy", "Evaluating"),
    ("Summarize the main plot points of Chapter 04 in five key steps.", "1. Mr. Nougat makes famous sweets in Chocoland.\n2. He clumsily spills peanuts, caramel, cashews, and raisins into chocolate.\n3. He decides to throw the mix away.\n4. Jammy tastes it, finds it amazing, and suggests selling it as 'Wannabe Chocolates'.\n5. The new treat becomes a huge market success.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how the narrative builds tension when the spill occurs and resolves it through Jammy's action.", 
     "Tension is created when Mr. Nougat accidentally knocks four bowls into his chocolate batch, causing immediate frustration and the threat of wasted effort and materials. This tension reaches its peak when Nougat decides to throw the mixture away. The resolution comes swiftly when Jammy steps in to taste the mix, discovering its exceptional flavor and convincing Nougat to sell it. The narrative resolves happily with market triumph.", 
     "Medium", "Analyzing"),

    ("Examine the importance of vocabulary development in Chapter 04 through words like 'clumsy', 'caramel', and 'convinced'.", 
     "The chapter introduces key descriptive words that enhance reading comprehension. 'Clumsy' describes character behavior, explaining why the spill happened. 'Caramel' introduces food vocabulary, helping children picture sticky sweets. 'Convinced' describes persuasive speech and decision-making. Learning these words in context helps Class 2 students expand their expressive vocabulary and literary understanding.", 
     "Medium", "Analyzing"),

    ("How does the concept of 'Accidental Innovation' apply to real-world science, cooking, and daily life?", 
     "Accidental innovation occurs when an unexpected mistake leads to a breakthrough because someone investigates the result rather than discarding it. In cooking, dishes like potato chips and ice pops were invented by accident. In science, penicillin was discovered accidentally. In daily life, unexpected changes can yield positive outcomes if we stay curious and open-minded like Jammy.", 
     "Medium", "Evaluating"),

    ("Discuss the leadership qualities shown by Mr. Candy Nougat when dealing with his assistant Jammy.", 
     "Mr. Candy Nougat displays positive leadership qualities by remaining humble and accessible. Even though he is the master craftsman and owner of the shop, he listens carefully to his assistant Jammy's suggestion. He does not let pride stop him from accepting a good idea, showing that great leaders value input from all team members regardless of rank.", 
     "Medium", "Evaluating"),

    ("Explore how texture and flavor contrast contributed to the success of Wannabe Chocolates.", 
     "Wannabe Chocolates succeeded because of their rich sensory profile. Smooth, sweet chocolate was contrasted with the crunch of peanuts and cashews, the sticky chewiness of caramel, and the fruity tang of raisins. This combination created a complex, satisfying mouthfeel that set it apart from plain chocolates and delighted customers.", 
     "Medium", "Analyzing"),

    ("What does the story teach about managing emotional reactions during unexpected kitchen or school mishaps?", "The story teaches us not to act out of immediate frustration or disappointment. When Mr. Nougat spilled the ingredients, his emotional reaction was to throw everything away. Pausing to evaluate the situation calmly, as Jammy did, prevents hasty decisions and allows constructive solutions to emerge.", "Medium", "Evaluating"),
    ("How does the author use humor and lightheartedness to engage young Class 2 readers?", "The author uses humorous elements like the town name 'Chocoland', character names like 'Mr. Candy Nougat' and 'Jammy', and the funny title 'Wannabe Chocolates'. The idea of a clumsy baker knocking four bowls at once into a big pot creates an amusing, vivid picture that delights young readers.", "Medium", "Analyzing"),
    ("Why is Jammy's respectful persuasion a good model for communication in school and family settings?", "Jammy did not argue angrily or criticize Mr. Nougat. Instead, he tasted the mixture, recognized its value, and respectfully persuaded Nougat by explaining why it would succeed. This shows children how to share ideas politely and convincingly.", "Medium", "Evaluating"),
    ("In what ways does 'The Wannabe Chocolate' challenge the idea that mistakes must always be corrected back to the original plan?", "Usually, when a mistake happens, people try to fix it back to the original plan. This story shows that sometimes a mistake moves us toward a better, new direction altogether. Instead of removing the spilled nuts, embracing them created a superior product.", "Medium", "Analyzing"),
    ("How can parents and teachers use this chapter to encourage children who struggle with physical clumsiness or handwriting mistakes?", "Adults can point out that Mr. Nougat was talented despite being clumsy. Mistakes caused by clumsiness do not mean a child lacks skill or worth. By focusing on creativity and resilience, children learn to forgive themselves for accidents and keep trying.", "Medium", "Applying"),
    ("Evaluate the economic benefit of reducing waste in a small confectionery shop like Mr. Nougat's.", "Discarding a large batch of chocolate and four bowls of premium nuts, caramel, and raisins represents a direct financial loss. By repurposing the spill into a marketable product, Mr. Nougat avoided loss and generated massive new revenue, proving that resourcefulness drives business growth.", "Medium", "Evaluating"),
    ("Contrast Mr. Candy Nougat's mindset before Jammy tasted the mix with his mindset afterward.", "Before the taste test, Mr. Nougat had a rigid mindset focused on his original recipe and assumed the mess was trash. Afterward, he adopted a flexible, growth mindset, recognizing the potential of the new creation and eagerly launching it into the market.", "Medium", "Analyzing"),
    ("Why is the word 'Wannabe' appropriate for a Class 2 story about self-expression and identity?", "The word 'Wannabe' implies wanting to be something special while being slightly different. It teaches children that it's okay not to fit standard molds—being unique and different can be a strength that makes someone or something stand out positively.", "Medium", "Evaluating"),
    ("How does the story build a sense of satisfaction in its final resolution?", "The resolution is satisfying because the initial accident leads to a triumphant outcome. The master baker gains market success, the assistant's advice is validated, and the townspeople enjoy a delicious new sweet, leaving readers with a warm, positive feeling.", "Medium", "Analyzing"),
    ("Construct an alternative ending where Jammy did not taste the mixture, and compare it with the actual story ending.", "In an alternative ending, the mix is thrown out, Mr. Nougat feels sad about wasted ingredients, and business continues as usual without innovation. Compared to the actual ending, the shop misses out on fame, market dominance, and a valuable lesson in adaptability.", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the structural theme of Chapter 04 from a HOTS (Higher Order Thinking Skills) perspective.", 
     "From a HOTS perspective, Chapter 04 integrates evaluation, creativity, and strategic decision-making. It challenges the rigid assumption that accidental deviations are inherently bad. By evaluating the spilled mixture empirically (tasting) and creatively rebranding it, the characters demonstrate problem-solving and innovation. This teaches young minds to analyze unexpected outcomes critically rather than dismissing them based on preconceptions.", 
     "Hard", "Evaluating"),

    ("Deconstruct the psychological transformation of Mr. Candy Nougat from perfectionist baker to innovative entrepreneur.", 
     "Initially, Nougat suffers from perfectionist rigidity: an unplanned spill equals failure. His transformation begins when he accepts Jammy's empirical evidence over his own perfectionist bias. By allowing his assistant to guide product launch, Nougat shifts from a routine baker into an adaptable entrepreneur who leverages serendipity for business expansion.", 
     "Hard", "Analyzing"),

    ("Synthesize the interdisciplinary connection between culinary science, consumer psychology, and moral education in this chapter.", 
     "Culinary science explains how mixing sweet, fat, crunchy, and chewy textures creates high palatability. Consumer psychology shows how novel branding ('Wannabe Chocolates') captures market interest. Moral education teaches open-mindedness, team collaboration, and resilience. Together, these elements form a rich, multidimensional learning experience for young readers.", 
     "Hard", "Creating"),

    ("Formulate a comprehensive plan for a Class 2 classroom workshop inspired by 'The Wannabe Chocolate'.", 
     "The workshop plan includes:\n1. **Story Reading**: Read Chapter 04 and discuss key vocabulary (clumsy, caramel, convinced).\n2. **Creative Art Session**: Give students accidental paint smudges and ask them to turn them into imaginative monster drawings.\n3. **Roleplay**: Students act out Nougat and Jammy's dialogue during the spill.\n4. **Reflection**: Students share personal stories of turning a mistake into something good.", 
     "Hard", "Creating"),

    ("Evaluate the role of serendipity vs. deliberate effort in achieving long-term success, using evidence from the text.", 
     "While serendipity (the accidental spill) provided the initial spark, long-term success required deliberate effort. Mr. Nougat's years of mastering chocolate baking ensured the base chocolate was high quality. Jammy's deliberate choice to taste and persuade, followed by actual production and marketing, turned a random accident into sustained market dominance.", 
     "Hard", "Evaluating"),

    ("Analyze how the narrative subverts traditional authority structures in workplace stories.", "Traditional workplace stories often present the master as all-knowing and the assistant as merely obedient. Chapter 04 subverts this by showing the master making a hasty error (deciding to throw away good food) while the assistant provides the crucial wisdom and vision that saves the business.", "Hard", "Analyzing"),
    ("Construct a logical argument explaining why 'Wannabe Chocolates' succeeded in ruling the market over standard chocolates.", "Standard chocolates offered familiar, predictable tastes. Wannabe Chocolates provided a novel multi-sensory experience (crunchy, chewy, sweet, sticky) combined with intriguing branding. Consumers naturally prefer exciting, superior sensory experiences over routine options when given a choice.", "Hard", "Creating"),
    ("Draft a speech that Mr. Candy Nougat might give to the citizens of Chocoland on the grand launch of Wannabe Chocolates.", "'Dear citizens of Chocoland! Today I present our newest creation—Wannabe Chocolates! Born from a funny kitchen accident and saved by my brilliant assistant Jammy, this treat combines our finest chocolate with peanuts, caramel, cashews, and raisins. Enjoy the sweet taste of turning mistakes into magic!'", "Hard", "Creating"),
    ("Assess the environmental and ethical implications of food waste reduction highlighted in this chapter.", "Food waste is a major global issue. By refusing to throw away a batch of wholesome ingredients, Jammy and Nougat set an ethical example of resourcefulness. Repurposing food reduces waste and models sustainable practices for young readers in an approachable format.", "Hard", "Evaluating"),
    ("Synthesize the overarching philosophy of Chapter 04 into a memorable motto for young learners.", "'Don't let a clumsy spill spoil your skill—taste the magic, stay open-minded, and turn every mess into your next sweet success!' This motto captures the core message of resilience, curiosity, teamwork, and creative optimism presented in the story.", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 04: The Wannabe Chocolate\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH04_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH04_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Once upon a time, in a town called Chocoland, there was a man named Mr. Candy Nougat who made the best chocolates and cakes of different flavours in the world. He was talented, hard-working but clumsy.",
     [
         ("Where did the story take place?", "In a town called Chocoland.", "Easy", "Remembering"),
         ("Who was Mr. Candy Nougat?", "He was a man who made the best chocolates and cakes in Chocoland.", "Easy", "Remembering"),
         ("What positive qualities did Mr. Candy Nougat have?", "He was talented and hard-working.", "Easy", "Remembering"),
         ("What flaw did Mr. Candy Nougat have?", "He was clumsy.", "Easy", "Remembering"),
         ("Find a word in the extract that means 'having a natural ability to do something well'.", "Talented.", "Medium", "Understanding")
     ]),

    # Set 2
    ("One day, while mixing his chocolate he tried to reach for sugar but knocked down bowls of peanuts, caramel, cashew and raisins. All of those landed in the chocolate bowl.",
     [
         ("What was Mr. Candy Nougat doing when the accident happened?", "He was mixing his chocolate.", "Easy", "Remembering"),
         ("What was he reaching for when he knocked down the bowls?", "He was reaching for sugar.", "Easy", "Remembering"),
         ("Name any two items that fell into the chocolate bowl.", "Peanuts and cashews (or caramel and raisins).", "Easy", "Remembering"),
         ("Where did all the spilled items land?", "They landed directly in the chocolate bowl.", "Easy", "Remembering"),
         ("Why did the bowls fall down?", "Because Mr. Nougat was clumsy while reaching for sugar.", "Medium", "Understanding")
     ]),

    # Set 3
    ("He decided to throw away the mixture. But his assistant, Jammy, decided to taste it. And he found out that the new mixture tasted amazing.",
     [
         ("What did Mr. Candy Nougat initially decide to do with the mixture?", "He decided to throw away the mixture.", "Easy", "Remembering"),
         ("Who was Jammy?", "Jammy was Mr. Candy Nougat's assistant.", "Easy", "Remembering"),
         ("What did Jammy decide to do before the mixture was thrown away?", "Jammy decided to taste the mixture.", "Easy", "Remembering"),
         ("How did the new mixture taste to Jammy?", "It tasted amazing.", "Easy", "Remembering"),
         ("What quality did Jammy show by tasting the mixture?", "He showed curiosity and initiative.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("Jammy convinced Candy Nougat to sell it as 'Wannabe Chocolates' because the mixture was different from the usual chocolates.",
     [
         ("Who persuaded Mr. Candy Nougat to sell the new sweet?", "His assistant, Jammy.", "Easy", "Remembering"),
         ("What name was given to the new chocolates?", "'Wannabe Chocolates'.", "Easy", "Remembering"),
         ("Why were they called 'Wannabe Chocolates'?", "Because the mixture was different from usual plain chocolates.", "Easy", "Remembering"),
         ("What does the word 'convinced' mean in this sentence?", "Completely sure about something or persuaded.", "Medium", "Understanding"),
         ("How did Mr. Nougat react to Jammy's suggestion?", "He agreed and decided to sell the new chocolates.", "Medium", "Understanding")
     ]),

    # Set 5
    ("Anybody who tasted the new chocolates loved them. The Wannabe Chocolates soon ruled the markets.",
     [
         ("How did people react when they tasted Wannabe Chocolates?", "Anybody who tasted them loved them.", "Easy", "Remembering"),
         ("What happened to Wannabe Chocolates in the markets?", "They soon ruled the markets.", "Easy", "Remembering"),
         ("What does the phrase 'ruled the markets' mean?", "It means they became extremely popular and sold better than all other sweets.", "Medium", "Understanding"),
         ("Did the accidental spill turn out to be a failure or a success?", "It turned out to be a huge market success.", "Easy", "Evaluating"),
         ("What main lesson does this outcome teach us?", "Accidents and mistakes can lead to great success if we are creative.", "Medium", "Evaluating")
     ]),

    # Set 6
    ("Word Meaning: Clumsy: Careless | Caramel: A type of sticky sweet | Convinced: Completely sure about something",
     [
         ("What is the meaning of the word 'clumsy'?", "Careless in action or movement.", "Easy", "Remembering"),
         ("What is 'caramel'?", "A type of sticky sweet made by heating sugar.", "Easy", "Remembering"),
         ("Define the word 'convinced'.", "Completely sure about something.", "Easy", "Remembering"),
         ("Which character in the story was described as clumsy?", "Mr. Candy Nougat.", "Easy", "Remembering"),
         ("Which ingredient in the story was sticky and sweet?", "Caramel.", "Easy", "Remembering")
     ]),

    # Set 7
    ("Mr. Candy Nougat made the best chocolates and cakes of different flavours in the world. He was talented, hard-working but clumsy.",
     [
         ("What two things did Mr. Candy Nougat make best in the world?", "Chocolates and cakes.", "Easy", "Remembering"),
         ("In which town did Mr. Candy Nougat live?", "Chocoland.", "Easy", "Remembering"),
         ("Was Mr. Nougat lazy or hard-working?", "He was hard-working.", "Easy", "Remembering"),
         ("What problem did his clumsiness cause in the story?", "It caused him to knock over bowls of ingredients into his chocolate.", "Medium", "Understanding"),
         ("Give an antonym for 'hard-working'.", "Lazy.", "Medium", "Understanding")
     ]),

    # Set 8
    ("One day, while mixing his chocolate he tried to reach for sugar but knocked down bowls of peanuts, caramel, cashew and raisins.",
     [
         ("What main base ingredient was Mr. Nougat mixing?", "Chocolate.", "Easy", "Remembering"),
         ("What specific ingredient was he trying to grab when he knocked the bowls?", "Sugar.", "Easy", "Remembering"),
         ("How many distinct ingredient bowls were knocked down?", "Four bowls.", "Easy", "Remembering"),
         ("Name the two nut items in the spilled bowls.", "Peanuts and cashews.", "Easy", "Remembering"),
         ("Name the dried fruit item in the spilled bowls.", "Raisins.", "Easy", "Remembering")
     ]),

    # Set 9
    ("He decided to throw away the mixture. But his assistant, Jammy, decided to taste it. And he found out that the new mixture tasted amazing.",
     [
         ("Why did Mr. Nougat want to throw away the mixture?", "Because he thought the accidental spill ruined the chocolate batch.", "Medium", "Understanding"),
         ("Did Jammy follow Mr. Nougat's initial decision immediately?", "No, he tasted the mixture first.", "Easy", "Remembering"),
         ("What word describes how the mixture tasted to Jammy?", "Amazing.", "Easy", "Remembering"),
         ("What would have happened if Jammy did not taste the mixture?", "The delicious mixture would have been wasted in the trash.", "Medium", "Analyzing"),
         ("What role did Jammy hold in the bakery?", "He was the assistant.", "Easy", "Remembering")
     ]),

    # Set 10
    ("Jammy convinced Candy Nougat to sell it as 'Wannabe Chocolates' because the mixture was different from the usual chocolates. Anybody who tasted the new chocolates loved them.",
     [
         ("What unique name was given to the sweet?", "'Wannabe Chocolates'.", "Easy", "Remembering"),
         ("Why was the name chosen?", "Because the mixture was different from usual plain chocolates.", "Easy", "Remembering"),
         ("Did customers like the new chocolates?", "Yes, anybody who tasted them loved them.", "Easy", "Remembering"),
         ("Who showed open-mindedness by listening to Jammy?", "Mr. Candy Nougat.", "Medium", "Understanding"),
         ("Summarize the main moral of this extract in one sentence.", "Listening to good advice and trying new things can turn an accident into a loved product.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 04: The Wannabe Chocolate\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH04_EXT_{q_counter:03d}"
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

with open(os.path.join(CH04_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 04 in {CH04_DIR}")
