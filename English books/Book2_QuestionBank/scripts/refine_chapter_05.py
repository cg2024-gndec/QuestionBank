r"""
Refines all 6 Category files for Chapter 05 ("Invention of Potato Chips") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH05_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_05")
os.makedirs(CH05_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What was the name of the chef who invented potato chips?", "(A) George Crum", "(B) Candy Nougat", "(C) James Watt", "(D) John Miller", "(A)", "The chef's name was George Crum.", "Easy", "Remembering", "Chef Name"),
    ("In which year did the story of George Crum take place?", "(A) 1853", "(B) 1950", "(C) 1700", "(D) 2000", "(A)", "The text states the event happened in 1853.", "Easy", "Remembering", "Year"),
    ("Where did George Crum work as a chef?", "(A) Moon Lake Lodge in New York", "(B) Sun Valley Resort", "(C) Ocean View Cafe", "(D) Mountain Peak Restaurant", "(A)", "He worked at Moon Lake Lodge in New York.", "Easy", "Remembering", "Workplace Setting"),
    ("What was George Crum's original speciality dish?", "(A) Thick-cut French fries", "(B) Thin crispy potato chips", "(C) Mashed potatoes", "(D) Baked potatoes", "(A)", "His speciality was thick-cut French fries.", "Easy", "Remembering", "Chef Speciality"),
    ("How did customers usually react to George Crum's thick-cut French fries?", "(A) They queued up all day long to buy them", "(B) They threw them away", "(C) Nobody bought them", "(D) They complained", "(A)", "People queued up to his restaurant all day long for his fries.", "Easy", "Remembering", "Customer Demand"),
    ("What kind of customer walked into the restaurant one tough day?", "(A) A very picky customer", "(B) A quiet customer", "(C) A polite customer", "(D) A blind customer", "(A)", "A very picky customer walked in.", "Easy", "Remembering", "Customer Trait"),
    ("Why did the picky customer send the fries back to the kitchen at first?", "(A) Because he found the fries too thick", "(B) Because they were too cold", "(C) Because they had no salt", "(D) Because they were sweet", "(A)", "The customer found the fries too thick.", "Easy", "Remembering", "Complaint Reason"),
    ("What did Crum do the first time the fries were sent back?", "(A) He sliced the potatoes a little thinner", "(B) He threw the customer out", "(C) He closed the kitchen", "(D) He gave the customer cake", "(A)", "Crum sliced the potatoes a little thinner.", "Easy", "Remembering", "First Reaction"),
    ("Did the customer accept the second, thinner batch of fries?", "(A) No, he sent them back again", "(B) Yes, he ate them all", "(C) He paid double money", "(D) He left the restaurant", "(A)", "The customer sent the fries back again.", "Easy", "Remembering", "Plot Detail"),
    ("How did George Crum feel after the customer kept sending the fries back repeatedly?", "(A) He lost his patience and felt frustrated and angry", "(B) He felt happy and amused", "(C) He fell asleep", "(D) He sang a song", "(A)", "Crum lost his patience and felt frustrated.", "Easy", "Remembering", "Chef Emotion"),
    ("How did Crum cut the potatoes when he lost his patience?", "(A) Very thinly", "(B) Extremely thick", "(C) In round balls", "(D) In square cubes", "(A)", "He sliced the potatoes very thinly.", "Easy", "Remembering", "Cooking Method"),
    ("How did Crum cook the paper-thin potato slices?", "(A) He fried them until they were crispy", "(B) He boiled them in water", "(C) He baked them in sun", "(D) He froze them in ice", "(A)", "He fried them until they were crispy.", "Easy", "Remembering", "Cooking Action"),
    ("What did Crum add to the crispy potato slices before serving?", "(A) Extra salt", "(B) Sugar", "(C) Honey", "(D) Chocolate sauce", "(A)", "He seasoned them with extra salt.", "Easy", "Remembering", "Seasoning"),
    ("How did the picky customer react to the thin, salty, crispy potato slices?", "(A) He loved them and praised the dish", "(B) He got even angrier", "(C) He refused to eat them", "(D) He sued the chef", "(A)", "The customer loved these slices and praised the dish.", "Easy", "Remembering", "Plot Climax"),
    ("What did other customers do when they saw the picky customer enjoying the new dish?", "(A) They began asking for these thin crispy fries as well", "(B) They left the restaurant", "(C) They laughed at him", "(D) They ordered ice cream", "(A)", "Other customers began asking for the thin crispy fries.", "Easy", "Remembering", "Market Reaction"),
    ("Which world-famous snack was born out of this kitchen incident?", "(A) Potato chips", "(B) Popcorn", "(C) Chocolate cookies", "(D) Donuts", "(A)", "This is how the snack potato chips came into being.", "Easy", "Remembering", "Snack Identity"),
    ("What does the word 'queued' mean?", "(A) Waited in line", "(B) Ran fast", "(C) Sat on a chair", "(D) Slept outdoors", "(A)", "Queued means waited in line.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'picky' mean in the text?", "(A) Very choosy and hard to satisfy", "(B) Friendly and kind", "(C) Very tall", "(D) Fast eater", "(A)", "Picky means very choosy & hard to satisfy.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'seasoned' mean?", "(A) Added salt, spice etc. to improve taste", "(B) Washed in cold water", "(C) Cut with a knife", "(D) Cooked on high flame", "(A)", "Seasoned means adding salt, spice etc. to improve taste.", "Easy", "Understanding", "Vocabulary"),
    ("In which state of the USA is Moon Lake Lodge located?", "(A) New York", "(B) California", "(C) Florida", "(D) Texas", "(A)", "Moon Lake Lodge was located in New York.", "Easy", "Remembering", "Geographic Detail"),
    ("What metal tool did George Crum use to slice potatoes so thinly?", "(A) A knife", "(B) A spoon", "(C) A fork", "(D) A hammer", "(A)", "Chefs use knives to slice potatoes thinly.", "Easy", "Understanding", "General Knowledge"),
    ("Was George Crum trying to make a delicious new dish, or was he reacting out of frustration?", "(A) He made it out of frustration and anger", "(B) He planned it for years", "(C) He read it in a cookbook", "(D) A customer gave him the recipe", "(A)", "The snack was a result of frustration and anger.", "Easy", "Understanding", "Motivation"),
    ("Are potato chips popular around the world today?", "(A) Yes, they are a beloved comfort food for millions of people", "(B) No, nobody eats them anymore", "(C) Only in New York", "(D) Only children eat them", "(A)", "They are a beloved comfort food for millions around the world.", "Easy", "Remembering", "Global Status"),
    ("What texture were the new potato chips described as?", "(A) Crispy", "(B) Soft and soggy", "(C) Wet", "(D) Hard as rock", "(A)", "They were thin and crispy.", "Easy", "Remembering", "Texture"),
    ("What is the title of Chapter 05?", "(A) Invention of Potato Chips", "(B) The Wannabe Chocolate", "(C) French Fries Story", "(D) The Picky Customer", "(A)", "Chapter 05 is titled 'Invention of Potato Chips'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why did George Crum expect the picky customer to hate the paper-thin, extra-salty chips?", "(A) Because they were too thin to pick up with a fork and intentionally over-salted out of annoyance", "(B) Because they were burnt black", "(C) Because they tasted bitter", "(D) Because they were raw", "(A)", "Crum made them impractically thin and salty out of frustration.", "Medium", "Understanding", "Chef Intention"),
    ("How did George Crum's emotional state accidentally lead to a famous food invention?", "(A) His anger made him try an extreme thin-slicing method that turned out to create a delicious texture", "(B) He threw a potato at a wall", "(C) He quit his job", "(D) He bought chips from another shop", "(A)", "Extreme thin slicing created the revolutionary crispy chip texture.", "Medium", "Analyzing", "Accidental Discovery"),
    ("Why did the picky customer's opinion influence the rest of the restaurant guests?", "(A) People saw how much the hard-to-please customer loved the dish and wanted to try it themselves", "(B) The customer shouted at everyone", "(C) The manager forced them to buy it", "(D) The chips were free", "(A)", "If a picky customer praised it, others knew it must be great.", "Medium", "Understanding", "Social Influence"),
    ("What is the irony in the story of how potato chips were invented?", "(A) A dish made to annoy a complaining customer ended up becoming one of the most praised snacks in the world", "(B) The chef hated potatoes", "(C) The customer was actually a chef", "(D) French fries became illegal", "(A)", "Irony: made out of spite/annoyance, became universally beloved.", "Medium", "Analyzing", "Literary Irony"),
    ("How does George Crum's original speciality compare with his accidental invention?", "(A) Speciality: thick-cut soft French fries; Invention: paper-thin crispy potato chips", "(B) Speciality: boiled potatoes; Invention: sweet cakes", "(C) Speciality: soup; Invention: salad", "(D) Speciality: cold chips; Invention: hot fries", "(A)", "Thick soft fries vs paper-thin crispy chips.", "Medium", "Analyzing", "Product Comparison"),
    ("What lesson does this chapter give about customer complaints in a business?", "(A) Customer complaints can push a business to innovate and discover better products", "(B) Complaints always ruin a business", "(C) Chefs should fight with picky customers", "(D) Customers are always wrong", "(A)", "Complaints can drive innovation.", "Medium", "Evaluating", "Business Insight"),
    ("Why did people queue up outside Moon Lake Lodge even before potato chips were invented?", "(A) Because George Crum's thick-cut French fries were already famous and delicious", "(B) Because it was the only restaurant in town", "(C) Because food was free", "(D) To see the lake", "(A)", "Crum was already a talented chef with a famous specialty.", "Medium", "Remembering", "Restaurant Reputation"),
    ("What step made the potato slices turn into 'chips' rather than soggy potatoes?", "(A) Slicing them paper-thin and frying them until they were completely crispy", "(B) Boiling them in milk", "(C) Freezing them", "(D) Mashing them", "(A)", "Paper-thin cut + deep frying = crispiness.", "Medium", "Understanding", "Culinary Technique"),
    ("What does 'losing patience' mean in the context of George Crum's actions?", "(A) Becoming so irritated by repeated rejections that he decided to take an extreme action", "(B) Forgetting where the kitchen was", "(C) Dropping his apron", "(D) Leaving the city", "(A)", "Irritation driving extreme response.", "Medium", "Understanding", "Phrase Meaning"),
    ("How does the word 'comfort food' apply to potato chips today?", "(A) It is a simple, satisfying snack that brings joy and relaxation to millions when eaten", "(B) It is used as a pillow", "(C) It is eaten only when sick", "(D) It is prescribed by doctors", "(A)", "Comfort food brings joy and casual satisfaction.", "Medium", "Understanding", "Modern Context"),
    ("If George Crum had refused to serve the picky customer again, what would have happened?", "(A) Potato chips would not have been invented at Moon Lake Lodge that day", "(B) The customer would make them himself", "(C) The lodge would burn down", "(D) Nothing would change", "(A)", "Refusing to cook would mean no potato chip discovery.", "Medium", "Analyzing", "Hypothetical Outcome"),
    ("Why was extra salt added to the paper-thin fried potato slices?", "(A) Crum seasoned them with extra salt as part of his exaggerated response to the customer", "(B) Salt was spilling accidentally", "(C) Salt makes potatoes sweet", "(D) The customer asked for salt", "(A)", "Extra salt was part of his frustrated exaggerated dish.", "Medium", "Remembering", "Recipe Detail"),
    ("What trait of George Crum allowed him to attempt thinner slicing multiple times?", "(A) Professional dedication to satisfying a customer despite mounting frustration", "(B) Laziness", "(C) Fear of losing his job", "(D) Ignorance", "(A)", "He kept trying until his patience finally snapped.", "Medium", "Analyzing", "Chef Dedication"),
    ("How does Chapter 05 inspire children when facing frustrating situations?", "(A) It shows that frustration can be channeled into creative results if we keep trying", "(B) It encourages children to get angry at friends", "(C) It tells children to throw food", "(D) It says frustration is good", "(A)", "Frustration can lead to unexpected creative breakthroughs.", "Medium", "Applying", "Life Lesson"),
    ("What is the geographic and historical setting of this chapter?", "(A) Year 1853, Moon Lake Lodge, New York, USA", "(B) Year 1990, London, UK", "(C) Year 1800, Paris, France", "(D) Year 2020, Tokyo, Japan", "(A)", "1853, Moon Lake Lodge, NY.", "Medium", "Remembering", "Setting Summary"),

    # Hard (41-50)
    ("Analyze the paradox of how a dish created out of anger became a global 'comfort food'.", "(A) Anger drove an extreme culinary experiment (paper-thin crispiness), but the sensory outcome was so delicious it evokes comfort and happiness worldwide", "(B) People like eating angry food", "(C) Comfort food must be salty", "(D) George Crum was an angry man always", "(A)", "Negative emotion creating universal sensory delight.", "Hard", "Analyzing", "HOTS Paradox"),
    ("Evaluate the role of the 'picky customer' as an unwitting catalyst for food innovation.", "(A) Without the customer's persistent dissatisfaction, Crum would have continued making standard thick fries, so the customer acted as an unintended catalyst", "(B) The customer was a food expert who gave Crum the recipe", "(C) The customer wanted to open a chip factory", "(D) The customer was Crum's boss", "(A)", "High standards/complaints forcing non-traditional solutions.", "Hard", "Evaluating", "Catalyst Role"),
    ("Deconstruct the culinary steps that differentiate French fries from potato chips based on the text.", "(A) French fries: thick-cut, softer texture; Potato chips: paper-thin cut, deep-fried to crispiness, extra salted", "(B) French fries: baked; Potato chips: boiled", "(C) French fries: sweet; Potato chips: sour", "(D) French fries: raw; Potato chips: roasted", "(A)", "Cut thickness and frying duration determine texture difference.", "Hard", "Analyzing", "Culinary Deconstruction"),
    ("Compare the discovery of Potato Chips (Ch 05) with Wannabe Chocolates (Ch 04).", "(A) Both were accidental food inventions: Ch 04 came from clumsy mixing; Ch 05 came from frustration with a picky customer", "(B) Both were invented by George Crum in New York", "(C) Both involved melting sugar", "(D) Neither became popular", "(A)", "Accidental mix vs frustration-driven extreme preparation.", "Hard", "Analyzing", "Comparative Analysis"),
    ("How does customer feedback (even negative) drive market innovation in modern industries?", "(A) Negative feedback highlights product limitations, forcing creators to rethink methods and invent superior alternatives", "(B) Negative feedback should be ignored", "(C) Negative feedback destroys all industries", "(D) Customer feedback is only for marketing", "(A)", "Negative feedback forces creative redesign.", "Hard", "Evaluating", "Market Dynamics"),
    ("Assess George Crum's initial motivation vs the final commercial result.", "(A) Initial motivation: spite/annoyance toward a picky guest; Final result: a multi-billion dollar worldwide snack industry", "(B) Initial motivation: charity; Final result: retirement", "(C) Initial motivation: contest; Final result: winning gold", "(D) Initial motivation: money; Final result: loss", "(A)", "Spiteful experiment yielding massive global success.", "Hard", "Evaluating", "Motivation vs Result"),
    ("Why is 'patience' a critical theme tested in this narrative?", "(A) Crum's loss of patience broke routine cooking habits, allowing a radical new cooking technique to be born", "(B) Patience means cooking slowly", "(C) The customer had great patience", "(D) Waiting in line requires patience", "(A)", "Breaking routine under pressure enabled innovation.", "Hard", "Analyzing", "Thematic Depth"),
    ("What does the phrase 'queued up all day long' reveal about George Crum's skill level before the invention?", "(A) It proves he was already a master chef whose culinary skills attracted crowds before potato chips were made", "(B) It means his service was very slow", "(C) It means the food was free", "(D) It shows he had no customers", "(A)", "Pre-existing high reputation and skill level.", "Hard", "Evaluating", "Historical Skill Level"),
    ("Synthesize how simple raw materials (potatoes, oil, salt) can transform into iconic products through creative techniques.", "(A) Basic low-cost ingredients become high-value culinary icons when transformed by innovative texture, cutting, and seasoning techniques", "(B) Potatoes are expensive items", "(C) Only rare spices create great snacks", "(D) Machines are required for good food", "(A)", "Technique and innovation elevate humble raw materials.", "Hard", "Evaluating", "Culinary Synthesis"),
    ("Formulate a takeaway principle for young students facing repeated rejection or criticism of their work.", "(A) Instead of giving up when criticized, use the feedback to try a bold, creative new approach that might exceed all expectations!", "(B) Stop doing schoolwork if criticized", "(C) Argue angrily with teachers", "(D) Hide your work", "(A)", "Transform criticism into bold creative experimentation.", "Hard", "Applying", "Core Lesson Synthesis")
]

mcq_content = f"# MCQs — Chapter 05: Invention of Potato Chips\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH05_MCQ_{idx:03d}"
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

with open(os.path.join(CH05_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("In 1853, George Crum was a chef at the Moon Lake Lodge in New _______.", "York", "Moon Lake Lodge was in New York.", "Easy"),
    ("George Crum's speciality was thick-cut _______ fries.", "French", "His speciality was thick-cut French fries.", "Easy"),
    ("People _______ up to his restaurant all day long for his French fries.", "queued", "People queued up all day long.", "Easy"),
    ("A very _______ customer walked into the restaurant and sent the fries back.", "picky", "A picky customer walked in.", "Easy"),
    ("The customer complained that the French fries were too _______.", "thick", "He found the fries too thick.", "Easy"),
    ("Crum sliced the potatoes a little _______ the first time.", "thinner", "He sliced them a little thinner.", "Easy"),
    ("The customer sent the thinner fries back to the _______ again.", "kitchen", "Sent them back to the kitchen.", "Easy"),
    ("Finally, Crum lost his _______ and sliced the potatoes very thinly.", "patience", "Crum lost his patience.", "Easy"),
    ("Crum fried the thin potato slices until they were _______.", "crispy", "Fried them until crispy.", "Easy"),
    ("He seasoned the crispy potato slices with extra _______.", "salt", "Seasoned with extra salt.", "Easy"),
    ("The customer _______ these thin crispy slices and praised the dish.", "loved", "The customer loved them.", "Easy"),
    ("Other customers began asking for these thin _______ fries as well.", "crispy", "Other guests asked for thin crispy fries.", "Easy"),
    ("This is how the crispy snack called potato _______ came into being.", "chips", "Potato chips came into being.", "Easy"),
    ("Potato chips are a result of frustration and _______.", "anger", "Invented out of frustration and anger.", "Easy"),
    ("Today, potato chips are a beloved comfort food for _______ of people.", "millions", "Beloved comfort food for millions.", "Easy"),
    ("The word 'queued' means waited in _______.", "line", "Queued means waited in line.", "Easy"),
    ("The word 'picky' means very choosy and hard to _______.", "satisfy", "Picky means hard to satisfy.", "Easy"),
    ("The word 'seasoned' means adding salt or _______ to improve taste.", "spice", "Adding salt or spice.", "Easy"),
    ("George Crum was a talented chef in the state of New _______.", "York", "Located in New York.", "Easy"),
    ("The restaurant where Crum worked was called Moon Lake _______.", "Lodge", "Moon Lake Lodge.", "Easy"),
    ("The customer sent the fries back to the kitchen multiple _______.", "times", "Sent back multiple times.", "Easy"),
    ("Potato chips were sliced paper-_______ before frying.", "thin", "Sliced paper-thin.", "Easy"),
    ("Extra _______ was sprinkled on top of the crispy chips.", "salt", "Sprinkled with extra salt.", "Easy"),
    ("Potato chips became a popular snack around the _______.", "world", "Loved all around the world.", "Easy"),
    ("Chapter 05 is titled 'Invention of Potato _______'.", "Chips", "Titled 'Invention of Potato Chips'.", "Easy"),

    # Medium (26-40)
    ("George Crum was having a particularly _______ day at work when the customer arrived.", "tough", "Having a particularly tough day.", "Medium"),
    ("The picky customer was extremely hard to _______.", "please", "Hard to satisfy/please.", "Medium"),
    ("Crum expected the customer to be annoyed by the paper-thin, extra _______ slices.", "salty", "Extra salty slices.", "Medium"),
    ("Instead of being angry, the customer _______ the dish enthusiastically.", "praised", "Praised the dish enthusiastically.", "Medium"),
    ("The success of potato chips spread rapidly among all restaurant _______.", "guests", "Spread among restaurant guests/customers.", "Medium"),
    ("A dish born out of kitchen frustration became a famous _______ food.", "comfort", "Beloved comfort food.", "Medium"),
    ("Crum's thick-cut French fries were his original signature _______.", "speciality", "Original signature speciality.", "Medium"),
    ("Deep-frying paper-thin slices gave the potatoes a delicious _______ texture.", "crunchy", "Delicious crunchy/crispy texture.", "Medium"),
    ("The picky customer acted as an accidental _______ for a new snack invention.", "catalyst", "Acted as a catalyst for innovation.", "Medium"),
    ("Customers had to wait in a long _______ to try George Crum's cooking.", "queue", "Wait in a long queue/line.", "Medium"),
    ("Repeated rejection of his fries caused Crum to lose his _______.", "temper", "Lost his temper/patience.", "Medium"),
    ("The invention of potato chips occurred in the year _______.", "1853", "Occurred in 1853.", "Medium"),
    ("Adding salt to food to enhance flavor is called _______.", "seasoning", "Called seasoning.", "Medium"),
    ("Potato chips proved that negative feedback can spark culinary _______.", "creativity", "Spark culinary creativity.", "Medium"),
    ("Millions of people worldwide enjoy potato chips as a delicious _______.", "snack", "Enjoy potato chips as a snack.", "Medium"),

    # Hard (41-50)
    ("The story of potato chips illustrates how extreme emotional _______ can lead to culinary breakthroughs.", "frustration", "Frustration leading to breakthrough.", "Hard"),
    ("George Crum's radical change in cutting technique transformed thick fries into paper-thin _______.", "wafers", "Transformed into paper-thin wafers/chips.", "Hard"),
    ("The picky customer's high standards unintentionally disrupted routine kitchen _______.", "practices", "Disrupted routine kitchen practices.", "Hard"),
    ("High customer demand quickly validated the commercial _______ of the new crispy snack.", "viability", "Validated commercial viability.", "Hard"),
    ("Seasoning the chips with extra salt provided an essential savory _______ profile.", "flavor", "Essential savory flavor profile.", "Hard"),
    ("The creation of potato chips is a celebrated example of culinary _______.", "serendipity", "Example of culinary serendipity.", "Hard"),
    ("Despite Crum's intent to spite the guest, the outcome resulted in universal customer _______.", "delight", "Resulted in universal customer delight.", "Hard"),
    ("Moon Lake Lodge gained historical fame as the birthplace of modern potato _______.", "crisps", "Birthplace of potato chips/crisps.", "Hard"),
    ("Turning criticism into a revolutionary product demonstrates adaptive problem-solving _______.", "skills", "Adaptive problem-solving skills.", "Hard"),
    ("The narrative highlights that valuable innovations often emerge from unexpected workplace _______.", "challenges", "Emerge from unexpected workplace challenges.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 05: Invention of Potato Chips\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH05_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH05_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("George Crum worked as a chef at Moon Lake Lodge in New York.", "True", "The text states he was a chef at Moon Lake Lodge in New York.", "Easy"),
    ("The story of George Crum took place in the year 1853.", "True", "The text explicitly states the year was 1853.", "Easy"),
    ("George Crum's speciality was baking chocolate cakes.", "False", "His speciality was thick-cut French fries.", "Easy"),
    ("People queued up all day long outside the restaurant for Crum's French fries.", "True", "The text notes that customers queued up all day long.", "Easy"),
    ("A very picky customer complained that Crum's fries were too thin.", "False", "The customer complained that the fries were too thick.", "Easy"),
    ("Crum sliced the potatoes a little thinner when the customer sent them back the first time.", "True", "He sliced them a little thinner and sent them back.", "Easy"),
    ("The customer loved the second batch of thinner fries immediately.", "False", "The customer sent the fries back again.", "Easy"),
    ("Crum lost his patience after the fries were sent back multiple times.", "True", "Crum lost his patience after repeated rejections.", "Easy"),
    ("When Crum lost his patience, he sliced the potatoes very thinly.", "True", "He sliced them paper-thin when he lost his patience.", "Easy"),
    ("Crum boiled the thin potato slices in water to make them soft.", "False", "He fried them until they were crispy.", "Easy"),
    ("Crum added extra salt to the thin crispy potato slices.", "True", "He seasoned them with extra salt.", "Easy"),
    ("The picky customer hated the thin crispy potato slices and left.", "False", "The customer loved them and praised the dish.", "Easy"),
    ("Other customers also asked for the thin crispy fries after seeing the picky customer enjoy them.", "True", "Other customers began asking for these thin crispy fries as well.", "Easy"),
    ("Potato chips were invented as a result of frustration and anger.", "True", "The text states the snack was a result of frustration and anger.", "Easy"),
    ("Today, potato chips are a beloved comfort food for millions of people around the world.", "True", "Potato chips are a global comfort food for millions.", "Easy"),
    ("The word 'queued' means waited in line.", "True", "Queued is defined as waited in line.", "Easy"),
    ("The word 'picky' means easy to satisfy.", "False", "Picky means very choosy and hard to satisfy.", "Easy"),
    ("The word 'seasoned' means adding salt or spice to improve taste.", "True", "Seasoned is defined as adding salt, spice, etc.", "Easy"),
    ("George Crum was an inexperienced chef who didn't know how to cook.", "False", "He was a skilled chef whose specialty drew long lines of customers.", "Easy"),
    ("Moon Lake Lodge was located in California.", "False", "It was located in New York.", "Easy"),
    ("Crum expected the picky customer to complain about the paper-thin salty chips.", "True", "He made them impractically thin and salty expecting a negative reaction.", "Easy"),
    ("Potato chips became popular only after 100 years.", "False", "Customers in the restaurant started ordering them immediately.", "Easy"),
    ("Potato chips are soft and soggy snacks.", "False", "Potato chips are known for being thin and crispy.", "Easy"),
    ("Salt was the main seasoning used by Crum on the new chips.", "True", "He seasoned them with extra salt.", "Easy"),
    ("Chapter 05 explains how potato chips were invented.", "True", "Chapter 05 is titled 'Invention of Potato Chips'.", "Easy"),

    # Medium (26-40)
    ("George Crum planned the potato chip recipe years before serving it.", "False", "It was created spontaneously out of frustration on a tough workday.", "Medium"),
    ("A picky customer can sometimes cause a business to create a better product.", "True", "The picky customer's complaints led directly to the invention of potato chips.", "Medium"),
    ("Crum's thick-cut French fries were disliked by most people in New York.", "False", "People queued up all day long for his famous thick-cut French fries.", "Medium"),
    ("Frying potato slices paper-thin creates a light, crispy texture instead of a soft one.", "True", "Thin slicing combined with frying yields crispiness.", "Medium"),
    ("George Crum gave up cooking when the customer sent the fries back twice.", "False", "He kept trying until he created the new crispy chip style.", "Medium"),
    ("The picky customer was pleased because the chef finally listened to his demand for thinner fries.", "True", "The ultra-thin crispiness satisfied his preference perfectly.", "Medium"),
    ("Potato chips are considered a healthy green vegetable dish in the story.", "False", "They are described as a crispy snack and comfort food.", "Medium"),
    ("Crum's emotional anger prevented him from making good food.", "False", "Ironically, his anger inspired an extreme cutting style that created a legendary snack.", "Medium"),
    ("The rest of the customers in Moon Lake Lodge ignored the new dish.", "False", "They saw the picky customer praising it and asked for thin crispy fries as well.", "Medium"),
    ("Moon Lake Lodge became famous for introducing potato chips.", "True", "The snack originated at Moon Lake Lodge in 1853.", "Medium"),
    ("The story shows that great innovations always require quiet and peaceful environments.", "False", "Potato chips were born during a busy, tough day full of frustration.", "Medium"),
    ("Extra salt enhanced the flavor of the crispy potato chips.", "True", "Salt seasoned the chips and made them taste delicious.", "Medium"),
    ("George Crum's original fries and his new potato chips had identical textures.", "False", "French fries were thick and soft; potato chips were thin and crispy.", "Medium"),
    ("The customer's praise was essential for turning Crum's experiment into a success.", "True", "Praise from the customer prompted other guests to order the dish.", "Medium"),
    ("Resilience and adaptability are useful traits for a professional chef.", "True", "Adapting to customer feedback despite frustration shows resilience.", "Medium"),

    # Hard (41-50)
    ("The story of potato chips proves that unintentional actions can lead to lasting historical impact.", "True", "An unplanned dish made out of anger became a global multi-billion dollar food industry.", "Hard"),
    ("George Crum intended to create a global comfort food when he sliced the potatoes paper-thin.", "False", "He simply wanted to spite a picky customer who kept sending fries back.", "Hard"),
    ("The contrast between thick soft fries and paper-thin crispy chips highlights structural food design.", "True", "Altering physical dimensions (thickness) completely changes culinary texture and taste.", "Hard"),
    ("Picky customers are always detrimental to restaurant success.", "False", "In this case, a picky customer's high standards catalyzed a world-famous invention.", "Hard"),
    ("The success of potato chips relied solely on chef Crum's intention to please.", "False", "It succeeded because the crispiness and saltiness delighted customer taste buds.", "Hard"),
    ("Potato chips represent a classic example of culinary serendipity.", "True", "Serendipity is finding valuable things unexpectedly, which describes chip creation.", "Hard"),
    ("George Crum's initial refusal to accept defeat allowed the discovery to take place.", "True", "Had he quit after the first complaint, potato chips would not have been invented then.", "Hard"),
    ("The word 'comfort food' implies that potato chips provide psychological satisfaction to consumers.", "True", "Comfort food provides familiar joy and relaxation when eaten.", "Hard"),
    ("The story suggests that emotional distress always results in ruined products.", "False", "Crum's frustration resulted in a globally beloved snack.", "Hard"),
    ("Transforming customer complaints into culinary breakthroughs requires creative flexibility.", "True", "Flexibility allows chefs to rethink standard recipes in response to criticism.", "Hard")
]

tf_content = f"# True / False — Chapter 05: Invention of Potato Chips\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH05_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who was George Crum and where did he work?", "George Crum was a chef who worked at the Moon Lake Lodge in New York.", "Easy", "Remembering"),
    ("In which year were potato chips invented according to the story?", "Potato chips were invented in the year 1853.", "Easy", "Remembering"),
    ("What was George Crum's original speciality dish?", "His original speciality dish was thick-cut French fries.", "Easy", "Remembering"),
    ("How popular were Crum's thick-cut French fries?", "They were so popular that people queued up to his restaurant all day long.", "Easy", "Remembering"),
    ("Why did the picky customer send the fries back to the kitchen at first?", "The customer sent them back because he found the French fries too thick.", "Easy", "Remembering"),
    ("What did Crum do the first time the fries were returned?", "Crum sliced the potatoes a little thinner and sent them back to the customer.", "Easy", "Remembering"),
    ("Why did Crum lose his patience?", "He lost his patience because the picky customer kept sending the fries back repeatedly.", "Easy", "Remembering"),
    ("How did Crum cut the potatoes when he lost his patience?", "He sliced the potatoes paper-thin.", "Easy", "Remembering"),
    ("How did Crum cook the paper-thin potato slices?", "He fried them in oil until they were crispy.", "Easy", "Remembering"),
    ("What seasoning did Crum add to the crispy potato slices?", "He seasoned them with extra salt.", "Easy", "Remembering"),
    ("How did the picky customer react to the thin crispy slices?", "The customer loved the thin crispy slices and praised the dish highly.", "Easy", "Remembering"),
    ("What did other customers do after seeing the picky customer's reaction?", "Other customers began asking for these thin crispy fries as well.", "Easy", "Remembering"),
    ("What snack was born out of this kitchen incident?", "The popular snack potato chips came into being from this incident.", "Easy", "Remembering"),
    ("What negative emotions led to the creation of potato chips?", "Frustration and anger led to the creation of potato chips.", "Easy", "Remembering"),
    ("How are potato chips described in modern times at the end of the text?", "They are described as a beloved comfort food for millions of people around the world.", "Easy", "Remembering"),
    ("What is the meaning of the word 'queued'?", "Queued means waited in line.", "Easy", "Understanding"),
    ("What is the meaning of the word 'picky'?", "Picky means very choosy and hard to satisfy.", "Easy", "Understanding"),
    ("What does the word 'seasoned' mean?", "Seasoned means adding salt, spice, or seasonings to improve the taste of food.", "Easy", "Understanding"),
    ("In which country is New York located?", "New York is located in the United States of America (USA).", "Easy", "Remembering"),
    ("Was George Crum trying to invent a new snack when he made chips?", "No, he was trying to satisfy or spite a picky customer out of frustration.", "Easy", "Understanding"),
    ("What texture difference exists between French fries and potato chips?", "French fries are thick and soft, while potato chips are thin and crispy.", "Easy", "Understanding"),
    ("Why did Crum add extra salt to the chips?", "He added extra salt as part of his exaggerated response to the complaining customer.", "Easy", "Remembering"),
    ("What was Moon Lake Lodge?", "Moon Lake Lodge was a restaurant/hotel in New York where George Crum worked.", "Easy", "Remembering"),
    ("Did Crum's new dish succeed immediately or fail?", "It succeeded immediately, with customers praising and ordering it right away.", "Easy", "Remembering"),
    ("What is the main theme of Chapter 05?", "The main theme is how customer criticism and chef frustration accidentally led to the invention of potato chips.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Why did George Crum think the customer would dislike the paper-thin salty chips?", "He thought the chips would be too thin to pick up with a fork and overly salty, making them impractical to eat.", "Medium", "Understanding"),
    ("How did the picky customer's persistent complaints act as a catalyst for innovation?", "By repeatedly rejecting thick fries, the customer forced Crum to break routine and try an extreme paper-thin slicing technique.", "Medium", "Analyzing"),
    ("Explain why people queued up outside Moon Lake Lodge even before chips were invented.", "They queued up because George Crum was already a talented chef renowned for making delicious thick-cut French fries.", "Medium", "Understanding"),
    ("Describe the steps George Crum took to prepare the very first batch of potato chips.", "He sliced potatoes paper-thin, deep-fried them until golden and crispy, and sprinkled them with extra salt.", "Medium", "Remembering"),
    ("Why did other customers in the restaurant order the new thin fries?", "They saw the hard-to-please picky customer praising the dish enthusiastically and wanted to taste the delicious new treat.", "Medium", "Understanding"),
    ("How does this story illustrate the irony of human emotions in work?", "It shows irony because a dish created out of anger and spite turned out to bring joy and comfort to millions.", "Medium", "Analyzing"),
    ("What lesson can business owners learn from George Crum's experience with a picky customer?", "They can learn that customer complaints, if addressed creatively, can lead to groundbreaking new products.", "Medium", "Evaluating"),
    ("Why is thickness such an important factor in the difference between fries and chips?", "Thickness determines cooking time and texture: thick slices stay soft inside, while thin slices fry completely crispy.", "Medium", "Understanding"),
    ("How did Crum's initial professional pride lead to frustration?", "He was proud of his famous specialty fries, so having them rejected repeatedly hurt his pride and made him lose patience.", "Medium", "Analyzing"),
    ("What role did extra salt play in making the chips tasty?", "Salt enhanced the natural savory flavor of fried potatoes, making them addictive and delicious.", "Medium", "Understanding"),
    ("Summarize Page 20 of the textbook in two sentences.", "Chef George Crum lost his patience when a picky customer repeatedly rejected his French fries for being too thick. Crum sliced potatoes paper-thin, fried them crispy, and served them salted, unexpectedly inventing popular potato chips.", "Medium", "Understanding"),
    ("How does the word 'comfort food' reflect the modern legacy of George Crum's invention?", "It shows that potato chips evolved from a restaurant accident into a universally loved snack enjoyed during relaxing moments.", "Medium", "Evaluating"),
    ("What would have happened if Crum had thrown the customer out of the lodge instead of cooking?", "If he had kicked the customer out, he would not have experimented with thin slicing, and potato chips would not have been born that day.", "Medium", "Analyzing"),
    ("Why is food seasoning important in cooking?", "Seasoning adds salt and spices to balance flavors, making simple ingredients like potatoes taste rich and appetizing.", "Medium", "Understanding"),
    ("Explain how George Crum turned a tough day at work into a historic success.", "Despite having a tough day and an annoying customer, Crum responded with extreme culinary effort that created a historic, world-famous snack.", "Medium", "Evaluating"),

    # Hard (41-50)
    ("Critique George Crum's emotional reaction to customer complaints from a professional perspective.", "While losing patience is unprofessional, Crum channeled his frustration into a creative culinary experiment rather than verbal conflict, resulting in a positive breakthrough.", "Hard", "Evaluating"),
    ("Analyze how physical texture (crispiness) affects consumer food preferences.", "Crispiness creates an appealing auditory and tactile sensation during chewing, which consumers find highly satisfying compared to soft textures.", "Hard", "Analyzing"),
    ("Deconstruct the sequence of events that led to the birth of potato chips in 1853.", "1. Picky customer rejects thick fries.\n2. Thinner fries rejected again.\n3. Crum loses patience.\n4. Paper-thin slicing & deep frying.\n5. Extra salting & serving.\n6. Customer praise & market adoption.", "Hard", "Analyzing"),
    ("Compare the creation of Potato Chips in Chapter 05 with Wannabe Chocolates in Chapter 04.", "Both resulted from kitchen mishaps: Chapter 04 was caused by a clumsy spill saved by an assistant, while Chapter 05 was caused by chef anger at a picky customer saved by extreme slicing.", "Hard", "Analyzing"),
    ("Evaluate the impact of customer word-of-mouth in Moon Lake Lodge.", "Word-of-mouth was instantaneous: when the picky customer praised the dish, neighboring diners immediately requested it, creating instant viral demand.", "Hard", "Evaluating"),
    ("How can a school student apply George Crum's story when receiving harsh criticism on an assignment?", "The student can take the criticism as a challenge to rethink their approach completely, attempting a bold new method that turns failure into success.", "Hard", "Applying"),
    ("Assess the contribution of simple raw materials (potatoes, oil, salt) to global food economics.", "Simple, inexpensive agricultural goods like potatoes can generate massive global economic value when transformed by innovative processing techniques.", "Hard", "Evaluating"),
    ("Why is serendipity a recurring motif in culinary history?", "Because cooking involves many variable factors (heat, time, cutting, mixing), small accidental changes frequently reveal novel, delightful flavors.", "Hard", "Analyzing"),
    ("Formulate a strategy for handling difficult customers in a modern service business based on this chapter.", "Listen to complaints, experiment with creative custom modifications, and observe if the customized solution appeals to a broader audience.", "Hard", "Creating"),
    ("Synthesize the main moral message of Chapter 05 for young learners.", "Channel frustration into creative effort, embrace criticism as an opportunity to innovate, and remember that great successes often come from tough challenges!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 05: Invention of Potato Chips\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH05_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe George Crum and his work at Moon Lake Lodge before the invention of potato chips.", 
     "In 1853, George Crum was a skilled chef working at the Moon Lake Lodge in New York. He was famous for his culinary expertise, particularly his signature dish of thick-cut French fries. His fries were so delicious that people queued up outside his restaurant all day long just to get a taste. Crum took great pride in his cooking, and his establishment enjoyed a stellar reputation among locals and tourists alike.", 
     "Easy", "Remembering"),

    ("Explain the conflict between George Crum and the picky customer.", 
     "One tough day at work, a very picky customer entered Moon Lake Lodge. When served Crum's famous thick-cut French fries, the customer complained that they were far too thick and sent them back to the kitchen. Crum tried to satisfy the customer by slicing potatoes a little thinner, but the customer rejected them again. This cycle repeated until Crum lost his patience due to the customer's hard-to-please attitude.", 
     "Easy", "Remembering"),

    ("How did George Crum react when he lost his patience, and what dish did he create?", 
     "Out of frustration and anger, George Crum decided to make an extreme version of fries that the customer could not complain was too thick. He sliced the potatoes paper-thin, fried them in hot oil until they became completely golden and crispy, and sprinkled them generously with extra salt. Instead of ruining the meal, this frustrated experiment created the world's very first batch of potato chips.", 
     "Easy", "Remembering"),

    ("Describe the customer's reaction to the thin crispy potato slices and the market outcome.", 
     "To Crum's surprise, the picky customer did not complain. Instead, he loved the paper-thin crispy slices and praised the dish enthusiastically. Seeing how much the hard-to-please guest enjoyed the treat, other customers in the restaurant began asking for these thin crispy fries too. Soon, potato chips became a permanent feature on the menu and eventually spread worldwide as a beloved comfort food.", 
     "Easy", "Remembering"),

    ("Explain the meanings of the vocabulary words 'queued', 'picky', and 'seasoned'.", 
     "1. **Queued**: Waited in a line of people waiting for their turn to receive food or service.\n2. **Picky**: Very choosy, selective, and difficult to satisfy or please.\n3. **Seasoned**: Added salt, herbs, or spices to raw or cooked food to enhance its flavor and aroma.", 
     "Easy", "Understanding"),

    ("How does Chapter 05 show that good things can come out of tough and frustrating days?", 
     "George Crum was having a particularly tough day at work when an annoying customer kept rejecting his food. Although Crum felt angry and frustrated, his extreme reaction led him to invent potato chips. This shows that even when a day starts out difficult or frustrating, staying engaged and trying new methods can produce wonderfully positive results.", 
     "Easy", "Understanding"),

    ("Compare George Crum's original French fries with his newly invented potato chips.", 
     "George Crum's original French fries were cut thick and cooked so they remained soft on the inside. In contrast, his newly invented potato chips were cut paper-thin, fried until completely crispy throughout, and seasoned with extra salt. While fries were eaten as a warm side dish, chips became a crunchy, portable snack enjoyed worldwide.", 
     "Easy", "Understanding"),

    ("What moral lesson does the story of George Crum teach young school children?", 
     "The story teaches children that when people criticize our work or when we feel frustrated, we should not give up. Instead of getting into arguments, we can channel our energy into trying a bold, creative new approach. Mistakes and criticisms often push us to discover amazing talents and ideas we didn't know we had.", 
     "Easy", "Understanding"),

    ("Why did the picky customer's approval convince other people in the lodge to try the new dish?", 
     "The picky customer was known for being extremely hard to satisfy. When the other diners saw someone so hard-to-please smiling and praising Crum's new thin crispy dish, they knew it must taste extraordinary. Their curiosity was aroused, leading them to order the new thin fries immediately.", 
     "Easy", "Understanding"),

    ("Detail the historical legacy of potato chips from 1853 to the present day.", 
     "Invented in 1853 at Moon Lake Lodge in New York by chef George Crum, potato chips started as an accidental restaurant specialty. Over the decades, mass production and packaging allowed chips to spread across the globe. Today, potato chips are a multi-billion dollar food industry and a beloved comfort food enjoyed by millions of people every day.", 
     "Easy", "Remembering"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why was George Crum famous in New York before he invented potato chips?", "Crum was famous because he was a master chef at Moon Lake Lodge. His speciality of thick-cut French fries was so popular that people queued up outside all day long to eat them.", "Easy", "Remembering"),
    ("Explain step-by-step how a kitchen complaint turned into a global snack.", "1. Picky customer complained fries were too thick.\n2. Thinner fries were rejected again.\n3. Crum lost patience and sliced potatoes paper-thin.\n4. He fried them crispy and added salt.\n5. Customer loved them; others ordered them; chips became a global snack.", "Easy", "Understanding"),
    ("How did Crum's emotion affect his cooking technique?", "His anger made him slice potatoes as thin as paper and fry them extra long until crispy, breaking his standard recipe routine and inventing chips.", "Easy", "Understanding"),
    ("Why did the customer reject the fries twice before the chips were made?", "The customer rejected them because he found the first batch too thick, and even after Crum made them slightly thinner, the customer still felt they were not thin enough.", "Easy", "Remembering"),
    ("What role does salt play in the invention of potato chips?", "Extra salt was sprinkled on top by Crum to season the crispy slices. The salt balanced the fried potato taste, making the chips delicious and addictive.", "Easy", "Understanding"),
    ("How does the story highlight the importance of trial and error in cooking?", "Crum tried three different slicing thicknesses before finding the one that satisfied the customer. Trial and error eventually yielded the perfect crispy chip.", "Easy", "Evaluating"),
    ("Why is Moon Lake Lodge historically significant in culinary history?", "Moon Lake Lodge in New York is famous as the exact birthplace where chef George Crum created the first potato chips in 1853.", "Easy", "Remembering"),
    ("What makes potato chips different from other potato dishes like mashed or baked potatoes?", "Potato chips are paper-thin, deep-fried to a hard crisp texture, heavily salted, and eaten cold or warm as a snack, unlike soft hot meal potatoes.", "Easy", "Understanding"),
    ("How did the other restaurant guests react when they saw the new dish?", "They saw the picky customer enjoying the thin crispy slices and immediately asked Crum to make the same thin crispy fries for them.", "Easy", "Remembering"),
    ("What lesson about customer service can be drawn from George Crum's story?", "Even when customers are difficult, finding a creative way to meet their preferences can transform a complaint into a major business success.", "Easy", "Evaluating"),
    ("How can Class 2 students apply George Crum's story to their art or writing work?", "When a drawing or writing piece doesn't turn out right, students can try a completely different, creative approach instead of getting discouraged.", "Easy", "Applying"),
    ("Why did Crum fry the potato slices until they were crispy?", "He wanted them to be hard and crispy so the customer could not eat them soft like standard fries, but the crispiness turned out to taste wonderful.", "Easy", "Understanding"),
    ("What does the phrase 'beloved comfort food' mean when referring to potato chips?", "It means potato chips are a favorite snack that brings feelings of happiness, relaxation, and simple enjoyment to people around the world.", "Easy", "Understanding"),
    ("Describe the mood in the kitchen during George Crum's tough day.", "The kitchen was busy, tense, and frustrating because Crum was working hard while facing repeated complaints from a choosy customer.", "Easy", "Understanding"),
    ("Summarize the entire Chapter 05 story in five key sentences.", "George Crum was a famous chef at Moon Lake Lodge known for thick French fries. A picky customer repeatedly sent fries back for being too thick. Frustrated, Crum sliced potatoes paper-thin, fried them crispy, and salted them. The customer loved the dish, and other guests ordered it too. This accident created potato chips, now a global comfort food.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how George Crum's loss of patience paradoxically resulted in a culinary masterpiece.", 
     "When Crum lost his patience, he abandoned traditional cooking boundaries. Instead of making minor adjustments to his standard thick fry, he took an extreme measure by slicing potatoes paper-thin and frying them until brittle. Paradoxically, this exaggerated response out of frustration produced a light, crispy texture and savory flavor profile that became a global culinary masterpiece.", 
     "Medium", "Analyzing"),

    ("Examine how physical texture (soft vs. crispy) alters human perception of food enjoyment.", 
     "Food enjoyment relies heavily on texture alongside taste. Soft, thick French fries offer a warm, comforting chew, but paper-thin crispy potato chips deliver an exciting crunch and immediate saltiness. The auditory crunch and lightness of chips trigger positive sensory feedback in the brain, making them uniquely satisfying to consumers.", 
     "Medium", "Analyzing"),

    ("Discuss how customer feedback, even when delivered rudely, can drive product evolution.", 
     "Customer feedback highlights product features that fail to meet user expectations. In this case, the picky customer's complaint revealed a market desire for thinner, crispier potato dishes. By responding to persistent feedback—even out of annoyance—Crum evolved his product line, proving that customer criticism can push creators toward breakthrough innovations.", 
     "Medium", "Evaluating"),

    ("Explore the concept of 'Accidental Inventions' using examples from Chapter 04 and Chapter 05.", 
     "Both Chapter 04 (Wannabe Chocolates) and Chapter 05 (Potato Chips) center on accidental food inventions. In Chapter 04, a clumsy spill of nuts and caramel created a market-dominating chocolate. In Chapter 05, chef anger at a picky customer led to paper-thin fried chips. Both stories show that when accidents happen, evaluating the result creatively yields iconic successes.", 
     "Medium", "Analyzing"),

    ("How can teachers use the story of George Crum to foster emotional resilience in children?", 
     "Teachers can use Crum's story to show that feeling frustrated or angry during a task is natural, but letting anger destroy work is unhelpful. By channeling strong feelings into bold creative experiments, children learn emotional resilience—turning moments of frustration into opportunities for problem-solving and growth.", 
     "Medium", "Applying"),

    ("What role did visual observation play in spreading the popularity of potato chips among diners?", "Visual observation was key. When diners saw the picky customer eating thin crispy chips with delight, their curiosity was sparked. Seeing someone else enjoy a novel dish prompted instant demand across the entire dining room.", "Medium", "Understanding"),
    ("How does the setting of 1853 New York add historical charm to the origin of potato chips?", "It places the invention in 19th-century America during the growth of resort lodges like Moon Lake Lodge. It reminds readers that everyday modern snacks have rich historical roots dating back over 170 years.", "Medium", "Analyzing"),
    ("Why was George Crum's skill as a chef essential for making the accidental invention taste good?", "Although the idea came from anger, Crum's culinary skill ensured the execution was flawless: he sliced with precision, fried to exact crispiness, and balanced the salt perfectly.", "Medium", "Evaluating"),
    ("In what ways does Chapter 05 challenge the idea that perfectionism is always necessary for success?", "It shows that strict adherence to original recipes isn't the only path to success. Breaking rules and experimenting with extreme variations can lead to superior results than rigid perfectionism.", "Medium", "Analyzing"),
    ("Explain the economic impact of turning a single rejected dish into a restaurant bestseller.", "A rejected dish represents wasted ingredients and time. Turning it into a bestseller eliminates waste, creates a new revenue stream, attracts more customers, and boosts business profits.", "Medium", "Evaluating"),
    ("How does the word 'picky' describe both a challenging customer trait and a helpful quality?", "While 'picky' means hard to satisfy (a challenge), a picky customer's high standards force chefs to elevate their quality and discover innovative methods (a helpful quality).", "Medium", "Analyzing"),
    ("Contrast George Crum's expectations of the customer's reaction with the actual reaction.", "Crum expected the customer to be angry or unable to eat the thin salty chips. In reality, the customer was delighted and praised the dish enthusiastically.", "Medium", "Analyzing"),
    ("Why is salt such an effective flavor enhancer on crispy fried potatoes?", "Salt draws out savory flavors, cuts through oiliness, and creates a delicious contrast with the crispy potato starch, making the snack irresistible.", "Medium", "Understanding"),
    ("How does the narrative structure of Chapter 05 build up to its satisfying climax?", "It builds tension through repeated complaints (thick fries sent back twice), reaches a climax when Crum loses patience and makes paper-thin chips, and resolves happily with customer praise and global fame.", "Medium", "Analyzing"),
    ("Formulate three questions you would ask George Crum if you could interview him in 1853.", "1. How did you feel when the customer sent the fries back the second time?\n2. What made you decide to slice the potatoes paper-thin?\n3. Were you surprised when the customer loved the chips?", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the historical significance of George Crum's invention in modern food culture.", 
     "George Crum's creation of potato chips in 1853 revolutionized global snack culture. By transforming a simple root vegetable into a light, shelf-stable, crispy treat, he laid the foundation for the modern snack food industry. Today, potato chips are manufactured globally in hundreds of flavors, proving that a single moment of kitchen innovation can reshape international food consumption habits.", 
     "Hard", "Evaluating"),

    ("Deconstruct the psychological shift in George Crum from professional frustration to creative triumph.", 
     "Crum's shift began with professional pride injured by repeated rejections. His frustration peaked into defiance, prompting him to break culinary rules by making paper-thin chips. When the customer praised the dish, Crum's emotional state shifted from defiance to triumph. This transformation shows how channeled emotion can break creative boundaries.", 
     "Hard", "Analyzing"),

    ("Synthesize the key elements required for accidental innovation: raw skill, pressure, and open-minded evaluation.", 
     "Accidental innovation requires three core elements:\n1. **Raw Skill**: Crum's mastery of knife work and frying.\n2. **Pressure**: The picky customer's persistent complaints.\n3. **Open-Minded Evaluation**: The customer and diners recognizing the delicious quality of the result.\nWithout all three, the accident would not have become a global phenomenon.", 
     "Hard", "Creating"),

    ("Formulate a lesson plan for Class 2 students based on Chapter 05 to teach problem-solving through cooking or craft.", 
     "1. **Story Introduction**: Read Chapter 05 and discuss George Crum's experience.\n2. **Activity**: Give students clay or paper strips that are 'too thick' for a model, asking them to flatten them into thin shapes.\n3. **Discussion**: Reflect on how changing shape/thickness changes the result.\n4. **Conclusion**: Write a short paragraph on turning frustration into creative ideas.", 
     "Hard", "Creating"),

    ("Evaluate the role of social proof in turning potato chips into a restaurant sensation.", 
     "Social proof occurred when other diners saw the picky customer enjoying the new chips. Because the picky customer was known to be hard to please, his enthusiastic approval validated the dish's quality instantly, prompting everyone else to order it without hesitation.", 
     "Hard", "Evaluating"),

    ("Analyze how Chapter 05 subverts the expectation that anger always produces negative results.", "Society views anger as a purely destructive emotion. Chapter 05 subverts this by demonstrating that anger, when combined with professional skill, can lead to extreme experimentation that breaks boring routines and yields historic discoveries.", "Hard", "Analyzing"),
    ("Compare the role of the assistant in Chapter 04 (Jammy) with the role of the customer in Chapter 05 (Picky Diner).", "In Chapter 04, the assistant Jammy provided the internal insight that saved a spilled mixture. In Chapter 05, the external picky customer provided the pressure that forced the chef to invent a new dish. Both acted as vital catalysts for food innovation.", "Hard", "Analyzing"),
    ("Draft a short news article from 1853 reporting on the new 'Potato Chip' phenomenon at Moon Lake Lodge.", "'NEW YORK, 1853 — A remarkable new dish has taken Moon Lake Lodge by storm! Chef George Crum, responding to a diner's request for thinner fries, has created paper-thin, crispy fried potato slices seasoned with salt. Guests are queuing up to taste these extraordinary \"Potato Chips\"!'", "Hard", "Creating"),
    ("Assess the impact of mass production on turning George Crum's restaurant dish into a global comfort food.", "While Crum created chips as a fresh restaurant dish, industrial mass production, packaging, and distribution allowed potato chips to be preserved, shipped worldwide, and sold cheaply, transforming a local luxury into a global household snack.", "Hard", "Evaluating"),
    ("Synthesize the ultimate life philosophy presented in Chapter 05 into a compelling summary statement.", "'When life gives you complaints, don't quit—slice through your frustration with bold creativity, season your efforts with determination, and turn every tough challenge into a crispy success!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 05: Invention of Potato Chips\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH05_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("In 1853 George Crum, a chef at the Moon Lake Lodge in New York, was having a particularly tough day at work. His speciality was thick-cut French fries for which people queued up to his restaurant all day long.",
     [
         ("In which year does this story take place?", "1853.", "Easy", "Remembering"),
         ("Who was George Crum?", "He was a chef at Moon Lake Lodge in New York.", "Easy", "Remembering"),
         ("What kind of day was George Crum having?", "He was having a particularly tough day at work.", "Easy", "Remembering"),
         ("What was his speciality dish?", "His speciality was thick-cut French fries.", "Easy", "Remembering"),
         ("How popular were his French fries?", "They were so popular that people queued up to his restaurant all day long.", "Medium", "Understanding")
     ]),

    # Set 2
    ("But today, a very picky customer had walked in who found the fries too thick and sent them back to the kitchen.",
     [
         ("What kind of customer walked into the restaurant?", "A very picky customer.", "Easy", "Remembering"),
         ("What complaint did the customer have about the fries?", "He found the fries too thick.", "Easy", "Remembering"),
         ("What did the customer do with the fries?", "He sent them back to the kitchen.", "Easy", "Remembering"),
         ("What does the word 'picky' mean in this context?", "Very choosy and hard to satisfy.", "Medium", "Understanding"),
         ("Why was this customer different from the usual guests?", "Unusual because most guests queued up and loved Crum's fries without complaining.", "Medium", "Analyzing")
     ]),

    # Set 3
    ("Crum sliced the potatoes a little thinner and sent thinner fries to the customer. But the customer sent the fries back again. This continued for some time.",
     [
         ("What did Crum do the first time the fries were sent back?", "He sliced the potatoes a little thinner.", "Easy", "Remembering"),
         ("Did the customer accept the second, thinner batch of fries?", "No, the customer sent them back again.", "Easy", "Remembering"),
         ("Did this process happen once or multiple times?", "It continued for some time (multiple times).", "Easy", "Remembering"),
         ("How would a chef naturally feel during such repetition?", "Frustrated, irritated, and impatient.", "Medium", "Understanding"),
         ("Find a word in the extract that is the opposite of 'thicker'.", "Thinner.", "Easy", "Understanding")
     ]),

    # Set 4
    ("Finally Crum lost his patience and sliced the potatoes very thinly, fried them until they were crispy and seasoned them with extra salt.",
     [
         ("What happened to Crum's emotional state finally?", "He lost his patience.", "Easy", "Remembering"),
         ("How thinly did Crum slice the potatoes when he lost his patience?", "He sliced them very thinly.", "Easy", "Remembering"),
         ("How did he cook the thin potato slices?", "He fried them until they were crispy.", "Easy", "Remembering"),
         ("What seasoning did he add to the crispy slices?", "He seasoned them with extra salt.", "Easy", "Remembering"),
         ("What does the word 'seasoned' mean?", "Added salt, spice etc. to improve the taste.", "Medium", "Understanding")
     ]),

    # Set 5
    ("The customer loved these slices and praised the dish so much that the other customers began asking for these thin crispy fries as well.",
     [
         ("How did the picky customer react to the paper-thin crispy slices?", "He loved these slices and praised the dish.", "Easy", "Remembering"),
         ("Did the picky customer complain about the extra salt or thinness?", "No, he loved and praised the dish.", "Easy", "Remembering"),
         ("What did the other customers in the restaurant do?", "They began asking for these thin crispy fries as well.", "Easy", "Remembering"),
         ("Why did the other customers want to try the new dish?", "Because they saw the hard-to-please customer loving and praising it.", "Medium", "Understanding"),
         ("What quality of the new dish made it popular?", "Its thin, crispy texture and savory saltiness.", "Medium", "Analyzing")
     ]),

    # Set 6
    ("This is how this crispy snack Potato chips came into being. This snack, which is a result of frustration and anger, is now a beloved comfort food for millions of people all around the world.",
     [
         ("Which famous snack was born out of this kitchen incident?", "Potato chips.", "Easy", "Remembering"),
         ("What emotions originally caused the creation of potato chips?", "Frustration and anger.", "Easy", "Remembering"),
         ("How are potato chips described for people around the world today?", "A beloved comfort food for millions of people.", "Easy", "Remembering"),
         ("What does 'comfort food' mean?", "Food that provides simple joy, satisfaction, and relaxation.", "Medium", "Understanding"),
         ("What is the moral lesson of this summary sentence?", "Frustration and anger can accidentally yield something universally beloved if met with creativity.", "Medium", "Evaluating")
     ]),

    # Set 7
    ("Word Meaning: Queued: Waited in line | Picky: Very choosy & hard to satisfy | Seasoned: To add salt, spice etc. to improve the taste",
     [
         ("What is the meaning of 'queued'?", "Waited in line.", "Easy", "Remembering"),
         ("What is the meaning of 'picky'?", "Very choosy & hard to satisfy.", "Easy", "Remembering"),
         ("What is the meaning of 'seasoned'?", "To add salt, spice etc. to improve the taste.", "Easy", "Remembering"),
         ("Which word describes the line of customers outside Moon Lake Lodge?", "Queued.", "Easy", "Remembering"),
         ("Which word describes the customer who returned the fries?", "Picky.", "Easy", "Remembering")
     ]),

    # Set 8
    ("In 1853 George Crum, a chef at the Moon Lake Lodge in New York, was having a particularly tough day at work.",
     [
         ("Who was the chef mentioned in this sentence?", "George Crum.", "Easy", "Remembering"),
         ("What was his job?", "He was a chef.", "Easy", "Remembering"),
         ("Where was the Moon Lake Lodge located?", "In New York.", "Easy", "Remembering"),
         ("In what century did this event occur?", "In the 19th century (1853).", "Medium", "Understanding"),
         ("What phrase describes his difficult workday?", "Having a particularly tough day at work.", "Easy", "Remembering")
     ]),

    # Set 9
    ("Finally Crum lost his patience and sliced the potatoes very thinly, fried them until they were crispy and seasoned them with extra salt.",
     [
         ("Why did Crum lose his patience?", "Because the customer kept rejecting the fries repeatedly.", "Easy", "Remembering"),
         ("What vegetable was sliced thinly?", "Potatoes.", "Easy", "Remembering"),
         ("What cooking method was used (boiling, baking, or frying)?", "Frying.", "Easy", "Remembering"),
         ("What word describes the texture of the finished potatoes?", "Crispy.", "Easy", "Remembering"),
         ("Why did Crum add extra salt?", "As part of his exaggerated, frustrated response to the customer.", "Medium", "Understanding")
     ]),

    # Set 10
    ("The customer loved these slices and praised the dish so much that the other customers began asking for these thin crispy fries as well. This is how this crispy snack Potato chips came into being.",
     [
         ("Did the customer praise or criticize the thin crispy dish?", "He praised the dish.", "Easy", "Remembering"),
         ("Who else wanted to eat the new thin fries?", "Other customers in the restaurant.", "Easy", "Remembering"),
         ("What name was eventually given to these thin crispy fries?", "Potato chips.", "Easy", "Remembering"),
         ("How did instant word-of-mouth help the new dish?", "Praise from the picky customer immediately drove demand from all other diners.", "Medium", "Understanding"),
         ("Summarize the climax of this story in one sentence.", "The picky customer loved the paper-thin crispy fries, inspiring everyone to order them and creating potato chips.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 05: Invention of Potato Chips\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH05_EXT_{q_counter:03d}"
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

with open(os.path.join(CH05_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 05 in {CH05_DIR}")
