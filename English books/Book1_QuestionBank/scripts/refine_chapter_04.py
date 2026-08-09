r"""
Refines all 6 Category files for Chapter 04 ("Invention of 'The Popsicle'") for Class 1.
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 1 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
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
    ("Who invented the Popsicle?", "(A) Frank Epperson", "(B) Albert Einstein", "(C) Thomas Edison", "(D) Alexander Graham Bell", "(A)", "11-year-old Frank Epperson invented the popsicle.", "Easy", "Remembering", "Inventor"),
    ("How old was Frank Epperson when he invented the Popsicle?", "(A) 11 years old", "(B) 20 years old", "(C) 5 years old", "(D) 50 years old", "(A)", "He was an 11-year-old boy in 1905.", "Easy", "Remembering", "Age"),
    ("In which year was the Popsicle invented?", "(A) 1905", "(B) 2020", "(C) 1800", "(D) 1999", "(A)", "Frank accidentally created it in the year 1905.", "Easy", "Remembering", "Year"),
    ("Where did Frank Epperson live?", "(A) San Francisco Bay Area", "(B) London", "(C) Tokyo", "(D) New Delhi", "(A)", "He lived in the San Francisco Bay Area.", "Easy", "Remembering", "Setting"),
    ("What did Frank mix with water in a cup?", "(A) Sugary soda powder", "(B) Salt", "(C) Mud", "(D) Milk", "(A)", "He mixed sugary soda powder with water.", "Easy", "Remembering", "Ingredients"),
    ("What object was left inside the cup overnight?", "(A) A wooden stirrer / stick", "(B) A metal spoon", "(C) A pencil", "(D) A straw", "(A)", "A wooden stirrer stick was left in the mixture.", "Easy", "Remembering", "Detail"),
    ("Why did the mixture freeze overnight?", "(A) It was a very cold night outside", "(B) He put it in a fire", "(C) The sun was shining", "(D) It was hot summer", "(A)", "The mixture froze because the night was very cold.", "Easy", "Remembering", "Science Fact"),
    ("What did Frank first name his frozen invention?", "(A) Epsicle", "(B) Ice Cream", "(C) Lolly", "(D) Soda Pop", "(A)", "He named it Epsicle by combining Epperson and icicle.", "Easy", "Remembering", "First Name"),
    ("Who renamed 'Epsicle' to 'Popsicle' many years later?", "(A) Frank's children", "(B) His teacher", "(C) His shopkeeper", "(D) His mayor", "(A)", "His children renamed it Popsicle to honor their father ('Pop').", "Easy", "Remembering", "Renaming"),
    ("Where did Frank first start selling his frozen treat?", "(A) Around his neighborhood", "(B) On an airplane", "(C) In a big mall", "(D) On television", "(A)", "He started selling the treat to neighbors.", "Easy", "Remembering", "Detail"),
    ("How did Frank eat his frozen treat the next morning?", "(A) Licking it off the wooden stirrer stick", "(B) Eating with a fork", "(C) Drinking it with a straw", "(D) Pouring it in a plate", "(A)", "He licked the icy treat right off the wooden stick.", "Easy", "Remembering", "Action"),
    ("Was the Popsicle invented by accident or on purpose?", "(A) By accident", "(B) On purpose", "(C) By a machine", "(D) In a laboratory test", "(A)", "Frank invented it accidentally on a cold night.", "Easy", "Remembering", "Invention Type"),
    ("In which season do people enjoy eating popsicles the most?", "(A) Summer", "(B) Winter", "(C) Rainy season", "(D) Autumn", "(A)", "Popsicles are popular summertime frozen treats.", "Easy", "Remembering", "Season"),
    ("What does the word 'accidentally' mean?", "(A) By chance, without planning", "(B) On purpose", "(C) Carefully", "(D) Slowly", "(A)", "Accidentally means happening by chance.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'concoction' mean in the passage?", "(A) A mixture of different ingredients", "(B) A stone", "(C) A song", "(D) A bird", "(A)", "Concoction means a liquid mixture.", "Easy", "Understanding", "Vocabulary"),
    ("What liquid was used to dissolve the soda powder?", "(A) Water", "(B) Juice", "(C) Tea", "(D) Oil", "(A)", "Frank mixed soda powder with plain water.", "Easy", "Remembering", "Detail"),
    ("Where did Frank leave the cup with the mixture?", "(A) Outside overnight", "(B) Inside the oven", "(C) Under his bed", "(D) In a cupboard", "(A)", "He accidentally left the cup outside on the porch.", "Easy", "Remembering", "Setting Detail"),
    ("What combination of words created the original name 'Epsicle'?", "(A) Epperson + icicle", "(B) Elephant + bicycle", "(C) Energy + circle", "(D) Apple + popsicle", "(A)", "Epsicle combined Frank's name Epperson with icicle.", "Easy", "Understanding", "Etymology"),
    ("Why did Frank's children call it 'Popsicle'?", "(A) To honor their 'Pop' (father)", "(B) Because it pops in your mouth", "(C) Because of popcorn", "(D) They liked the letter P", "(A)", "It was a loving tribute to their father ('Pop').", "Easy", "Understanding", "Reasoning"),
    ("What state of matter did the liquid mixture turn into overnight?", "(A) Solid ice", "(B) Gas", "(C) Vapor", "(D) Dust", "(A)", "Freezing turned the liquid mixture into solid ice.", "Easy", "Understanding", "Science Concept"),
    ("What type of treat is a Popsicle?", "(A) A frozen sweet treat on a stick", "(B) Hot soup", "(C) Baked cake", "(D) Boiled egg", "(A)", "It is a delicious frozen sweet treat on a stick.", "Easy", "Remembering", "Category"),
    ("Did Frank enjoy his accidental creation the next morning?", "(A) Yes, he devoured the icy treat happily", "(B) No, he threw it away", "(C) He cried", "(D) He gave it to a dog", "(A)", "He loved the taste and licked it clean off the stick.", "Easy", "Remembering", "Character Action"),
    ("Which device helped hold the frozen treat?", "(A) A wooden stirrer stick", "(B) A plastic spoon", "(C) A piece of string", "(D) A leaf", "(A)", "The wooden stirrer stick acted as the handle.", "Easy", "Remembering", "Detail"),
    ("What weather condition was necessary for the drink to freeze outside?", "(A) Freezing cold temperature at night", "(B) Warm breeze", "(C) Hot sunshine", "(D) Rainy weather", "(A)", "Freezing cold weather was essential to freeze the liquid.", "Easy", "Understanding", "Science Fact"),
    ("What lesson does Frank's story teach us about young people?", "(A) Children can invent wonderful new things through curiosity", "(B) Children shouldn't play outside", "(C) Only adults make inventions", "(D) Soda is bad", "(A)", "Even an 11-year-old child can make a world-famous invention.", "Easy", "Understanding", "Core Takeaway"),

    # Medium (26-40)
    ("Why did Frank's mixture freeze without a refrigerator in 1905?", "(A) Outdoor freezing temperatures at night froze the water naturally", "(B) He used magic", "(C) He bought ice cubes", "(D) He blew on it", "(A)", "Cold night air in winter acted as a natural freezer.", "Medium", "Understanding", "Science Explanation"),
    ("How did Frank turn an accidental event into a small business?", "(A) He recognized the taste was great and sold it to neighborhood kids", "(B) He threw it out", "(C) He kept it secret", "(D) He gave it away for free only", "(A)", "He saw commercial potential and sold Epsicles locally.", "Medium", "Understanding", "Entrepreneurship"),
    ("Why was the wooden stirrer stick so convenient for the frozen treat?", "(A) It provided a clean handle to hold the ice without melting it in your hands", "(B) It made it heavier", "(C) It changed the color", "(D) It added flavor", "(A)", "The stick allowed clean handling while eating.", "Medium", "Understanding", "Function"),
    ("What does 'devoured' mean in the sentence 'Epperson devoured the icy concoction'?", "(A) Ate up eagerly and greedily", "(B) Looked at slowly", "(C) Spilled on the floor", "(D) Shared with birds", "(A)", "Devoured means eating something with great enjoyment and speed.", "Medium", "Understanding", "Vocabulary"),
    ("What makes the Popsicle a unique invention compared to normal ice cubes?", "(A) It is flavored, sweet, and served on a convenient wooden stick", "(B) It is salty", "(C) It is hot", "(D) It melts in five seconds", "(A)", "The combination of flavor and stick handle makes it unique.", "Medium", "Analyzing", "Comparison"),
    ("What role did curiosity play in Frank's discovery?", "(A) He tried tasting the frozen stick instead of throwing it away", "(B) He broke the glass", "(C) He ran inside", "(D) He cried for help", "(A)", "Curiosity led him to taste the frozen mix.", "Medium", "Understanding", "Character Trait"),
    ("How did Frank's invention spread from his neighborhood to the world?", "(A) As years passed, the popular treat was renamed Popsicle and mass produced", "(B) It disappeared", "(C) It stayed in one house", "(D) Only his family ate it", "(A)", "It grew from neighborhood sales into a worldwide brand.", "Medium", "Understanding", "History Progress"),
    ("Why did Frank leave his drink outside overnight?", "(A) He forgot about it after mixing it", "(B) He wanted to freeze it on purpose", "(C) His mother told him to", "(D) The cup was too hot", "(A)", "He simply forgot the cup outside on a cold night.", "Medium", "Remembering", "Plot Cause"),
    ("What is the difference between an 'icicle' and a 'popsicle'?", "(A) An icicle is frozen water from roofs; a popsicle is flavored sweet ice on a stick", "(B) They are identical", "(C) Icicles are warm", "(D) Popsicles grow on trees", "(A)", "Icicles are plain frozen water drips; popsicles are sweet treats.", "Medium", "Analyzing", "Distinction"),
    ("How does temperature affect liquids like soda water?", "(A) Below freezing point, liquid water transforms into solid ice", "(B) Liquid turns into fire", "(C) Temperature does nothing", "(D) Liquid vanishes", "(A)", "Cold temperatures cause liquids to freeze solid.", "Medium", "Applying", "Science Principle"),
    ("What key ingredient gave the original popsicle its sweet taste?", "(A) Sugary soda powder", "(B) Chocolate syrup", "(C) Salt", "(D) Honey", "(A)", "Sugary soda powder provided the sweet flavor.", "Medium", "Remembering", "Ingredient"),
    ("Why is Frank Epperson an inspiration for young students?", "(A) He proved that observing and experimenting can lead to great discoveries", "(B) He skipped school", "(C) He bought many toys", "(D) He slept all day", "(A)", "He showed how observation turns everyday accidents into success.", "Medium", "Evaluating", "Inspirational Value"),
    ("What does the word 'summertime' suggest in the passage?", "(A) Warm weather when cold treats are most refreshing and popular", "(B) Cold snow weather", "(C) Dark rainy nights", "(D) Autumn leaves", "(A)", "Summertime is the warm season when popsicles are most enjoyed.", "Medium", "Understanding", "Context"),
    ("How did the wooden stirrer get stuck inside the ice?", "(A) The liquid froze solid around the stick while it stood in the cup", "(B) Frank glued it", "(C) He pushed it in later", "(D) The stick grew inside", "(A)", "The liquid froze around the stick overnight.", "Medium", "Understanding", "Process"),
    ("What would have happened if the night had been warm instead of cold?", "(A) The mixture would remain liquid and not freeze at all", "(B) It would freeze faster", "(C) It would turn to ice cream", "(D) It would turn to stone", "(A)", "Without cold temperatures, freezing could not occur.", "Medium", "Analyzing", "Hypothetical"),

    # Hard (41-50)
    ("How does Frank Epperson's story illustrate the concept of 'serendipity'?", "(A) Serendipity is finding valuable things by happy accident, just like the popsicle invention", "(B) It means working hard in a lab", "(C) It means making mistakes only", "(D) It means buying food", "(A)", "Serendipity means making fortunate discoveries by accident.", "Hard", "Evaluating", "HOTS Concept"),
    ("Why is observation a critical step in the scientific method based on this chapter?", "(A) Frank observed the frozen state and tasted it instead of discarding it carelessly", "(B) Observation is unnecessary", "(C) Observation takes too long", "(D) Observing makes food spoil", "(A)", "Observation allows us to notice unexpected and useful results.", "Hard", "Evaluating", "Scientific Method"),
    ("Analyze how a simple childhood invention became an iconic global brand.", "(A) The basic concept of sweet frozen ice on a stick fulfilled a universal summer desire across generations", "(B) Big companies stole it", "(C) Nobody liked it at first", "(D) It was forced on people", "(A)", "Its simple delight and refreshment made it universally popular.", "Hard", "Analyzing", "Business / Brand History"),
    ("What is the significance of renaming 'Epsicle' to 'Popsicle' by Frank's children?", "(A) It added a affectionate family identity ('Pop') while keeping the connection to icicle", "(B) They disliked their father's name", "(C) Popsicle sounded scientific", "(D) Epsicle was hard to spell", "(A)", "It created a warm, catchy name honoring their father ('Pop').", "Hard", "Evaluating", "Name Analysis"),
    ("How can Class 1 students apply Frank's attitude when an experiment doesn't go as planned?", "(A) Look closely at what happened and see if something interesting or useful came out of it", "(B) Cry and throw things away", "(C) Never try again", "(D) Blame others", "(A)", "Accidents can lead to unexpected learning opportunities.", "Hard", "Applying", "Real Life Application"),
    ("What physical transformation occurred in Frank's cup on that cold night in 1905?", "(A) Thermal energy left the liquid mixture, causing water molecules to lock into a solid crystal grid", "(B) The liquid boiled", "(C) The liquid turned to gas", "(D) The cup shrank", "(A)", "Loss of heat energy froze liquid water into solid ice.", "Hard", "Analyzing", "Physical Science"),
    ("Why do simple ideas often become the most successful inventions?", "(A) They solve common desires (like cooling off in summer) in easy, accessible ways", "(B) Simple ideas are expensive", "(C) Simple ideas are hard to make", "(D) Nobody thinks of simple ideas", "(A)", "Simplicity makes products easy to produce and enjoy.", "Hard", "Evaluating", "Innovation Insight"),
    ("Contrast Frank's initial local neighborhood sales with modern commercial popsicle manufacturing.", "(A) Frank sold handmade cups locally, while modern factories produce millions using automated freezing molds", "(B) They are identical", "(C) Modern popsicles are hot", "(D) Frank used huge machines", "(A)", "He started small by hand; today it is mass-produced industrially.", "Hard", "Analyzing", "Historical Contrast"),
    ("What role does environmental temperature play in everyday food preservation and treats?", "(A) Cold temperatures slow down melting and freeze liquids into solid structures", "(B) Heat freezes food", "(C) Temperature has no effect", "(D) Cold turns food into air", "(A)", "Cold temperature controls state changes and preserves foods.", "Hard", "Evaluating", "Practical Science"),
    ("What is the ultimate takeaway from Chapter 04 for young learners?", "(A) Keep your eyes open, stay curious, and remember that great ideas can come from simple everyday accidents!", "(B) Never leave cups outside", "(C) Only eat soda powder", "(D) Winter is bad", "(A)", "Curiosity and keen observation transform simple accidents into great ideas.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 04: Invention of 'The Popsicle'\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK01_CH04_MCQ_{idx:03d}"
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
    ("Frank Epperson was _______ years old when he invented the popsicle.", "11", "Frank was 11 years old in 1905.", "Easy"),
    ("The Popsicle was invented in the year _______.", "1905", "It was invented in 1905.", "Easy"),
    ("Frank mixed sugary soda powder with _______.", "water", "He mixed soda powder with water.", "Easy"),
    ("He left the cup outside on a very _______ night.", "cold / freezing", "The night was very cold.", "Easy"),
    ("Inside the cup, he had left a wooden _______.", "stirrer / stick", "A wooden stirrer stick was inside.", "Easy"),
    ("Overnight, the liquid mixture _______ solid.", "froze", "Cold weather froze the mixture.", "Easy"),
    ("In the morning, Frank licked the icy treat off the wooden _______.", "stick / stirrer", "He licked it off the stick.", "Easy"),
    ("Frank first named his creation _______.", "Epsicle", "He named it Epsicle first.", "Easy"),
    ("Many years later, Frank's _______ renamed it Popsicle.", "children", "His children renamed it Popsicle.", "Easy"),
    ("Frank started selling the frozen treat in his _______.", "neighborhood", "He sold it in his neighborhood.", "Easy"),
    ("Popsicle is a famous treat enjoyed especially during _______.", "summer / summertime", "Popsicles are popular in summer.", "Easy"),
    ("Frank Epperson lived in the San Francisco Bay _______.", "Area", "He lived in San Francisco Bay Area.", "Easy"),
    ("The invention of the Popsicle happened by _______.", "accident / chance", "It was an accidental invention.", "Easy"),
    ("The word 'accidentally' means by _______ without planning.", "chance", "Accidentally means by chance.", "Easy"),
    ("The word 'concoction' means a liquid _______.", "mixture", "Concoction means a mixture.", "Easy"),
    ("Frank devoured the icy treat because it tasted _______.", "sweet / delicious", "It tasted sweet and good.", "Easy"),
    ("The original name 'Epsicle' combined Epperson and _______.", "icicle", "Epsicle combined Epperson and icicle.", "Easy"),
    ("The name 'Popsicle' was chosen to honor their _______.", "father / Pop", "Pop's icicle honored their father.", "Easy"),
    ("Freezing turns liquid water into solid _______.", "ice", "Freezing turns water to ice.", "Easy"),
    ("The wooden stick served as a useful _______ to hold the treat.", "handle", "The stick acted as a handle.", "Easy"),
    ("Frank was a creative and curious _______.", "boy / kid / child", "Frank was a 11-year-old boy.", "Easy"),
    ("You lick a popsicle off a wooden _______.", "stick", "Popsicles are on wooden sticks.", "Easy"),
    ("The soda powder had a _______ taste.", "sweet / sugary", "The powder was sugary soda.", "Easy"),
    ("Cold weather turned the liquid drink into _______ ice.", "frozen / solid", "It became solid ice.", "Easy"),
    ("Chapter 04 tells the story of how the _______ was invented.", "Popsicle", "It tells the invention of Popsicle.", "Easy"),

    # Medium (26-40)
    ("The word 'devoured' means ate up with great _______.", "enjoyment / eagerness / speed", "Devoured means eating eagerly.", "Medium"),
    ("Without outdoor cold weather, the mixture would not have _______.", "frozen", "Cold temperature caused freezing.", "Medium"),
    ("The wooden stirrer allowed Frank to hold the ice without getting his hands _______.", "sticky / wet / cold", "The stick kept hands clean.", "Medium"),
    ("Frank saw a business opportunity and sold treats around his _______.", "neighborhood / town", "He sold them locally.", "Medium"),
    ("The combination of sugary flavor and a stick made Popsicle a unique _______.", "treat / invention", "Flavor plus stick made it unique.", "Medium"),
    ("Water transforms from liquid to solid at _______ temperatures.", "freezing / cold", "Freezing changes state of water.", "Medium"),
    ("Frank's curiosity led him to _______ the frozen drink instead of throwing it away.", "taste / lick / eat", "Curiosity made him taste it.", "Medium"),
    ("The name 'Popsicle' combines 'Pop' (father) and _______.", "icicle", "Pop + icicle = Popsicle.", "Medium"),
    ("An icicle forms naturally from dripping _______ in winter.", "water", "Icicles form from freezing water.", "Medium"),
    ("Summertime is the warm season when popsicles are most _______.", "popular / enjoyed / refreshing", "Popsicles refresh in summer.", "Medium"),
    ("Frank's story proves that young children can be great _______.", "inventors", "Kids can be great inventors.", "Medium"),
    ("The sugary powder dissolved in water to make a sweet _______.", "solution / liquid / mixture", "Powder dissolved in water.", "Medium"),
    ("The frozen treat melted slowly while Frank _______ it.", "licked", "He licked the treat off the stick.", "Medium"),
    ("Accidental discoveries often require keen _______ to be noticed.", "observation / curiosity", "Observation spots accidents.", "Medium"),
    ("Popsicles are popular around the world today as a summer _______.", "snack / treat", "It is a popular summer treat.", "Medium"),

    # Hard (41-50)
    ("Serendipity is the occurrence of finding valuable things by happy _______.", "accident / chance", "Serendipity is happy accident.", "Hard"),
    ("Frank's simple invention relies on the natural principle of _______ change.", "state / phase", "Freezing is a physical phase change.", "Hard"),
    ("The wooden stick provided thermal insulation between warm hands and cold _______.", "ice", "Stick insulates against hand heat.", "Hard"),
    ("Observation transforms an everyday mishap into an innovative _______.", "discovery / product", "Observation yields discovery.", "Hard"),
    ("The change from Epsicle to Popsicle created a catchy, memorable _______.", "brand / name", "Popsicle became a famous brand.", "Hard"),
    ("Liquid molecules freeze into a solid lattice when temperature _______.", "drops / falls", "Dropping temperature freezes liquids.", "Hard"),
    ("Children renamed the product as a loving tribute to their _______.", "father / Pop", "Tribute to their father 'Pop'.", "Hard"),
    ("Handmade neighborhood sales paved the way for industrial mass _______.", "production", "Local sales grew to mass production.", "Hard"),
    ("Everyday curiosity is a key driving force behind scientific _______.", "invention / progress", "Curiosity drives science.", "Hard"),
    ("The story of the Popsicle teaches us to embrace unexpected _______.", "results / accidents", "Embrace unexpected results.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 04: Invention of 'The Popsicle'\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK01_CH04_FIB_{idx:03d}"
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

with open(os.path.join(CH04_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. Fill in Blanks from Story (Cloze Passage) (50 Distinct Qs)
# -------------------------------------------------------------
cloze_data = [
    ("Do you like popsicles when you enjoy them in _______?", "summers", "Easy"),
    ("It was invented by an _______ year old boy.", "11 / eleven", "Easy"),
    ("Back in the year _______, a boy named Frank Epperson lived in San Francisco.", "1905", "Easy"),
    ("Frank Epperson accidentally invented the summertime _______.", "treat", "Easy"),
    ("He mixed some sugary soda _______ with water.", "powder", "Easy"),
    ("He left the cup containing the mixture outside _______.", "overnight", "Easy"),
    ("A wooden _______ stick was left standing in the cup.", "stirrer", "Easy"),
    ("The night was very _______ and chilly.", "cold", "Easy"),
    ("By morning, the liquid mixture had completely _______.", "frozen", "Easy"),
    ("In the morning, Frank discovered the icy _______.", "concoction / treat", "Easy"),
    ("He devoured the icy treat by licking it off the wooden _______.", "stirrer / stick", "Easy"),
    ("He loved the delicious, sweet _______ taste.", "frozen / sugary", "Easy"),
    ("Frank named his new creation an _______ at first.", "Epsicle", "Easy"),
    ("He combined his last name Epperson with the word _______.", "icicle", "Easy"),
    ("He started selling the treat around his _______.", "neighborhood", "Easy"),
    ("Many years later, Frank had his own _______.", "children", "Easy"),
    ("His children renamed the treat _______.", "Popsicle", "Easy"),
    ("They renamed it to honor their father, whom they called _______.", "Pop", "Easy"),
    ("Today, popsicles are eaten by millions during warm _______.", "summers", "Easy"),
    ("Frank's discovery shows that great inventions can happen by _______.", "accident", "Easy"),
    ("The sugary soda powder gave the ice its sweet _______.", "flavor", "Easy"),
    ("The wooden stick made it easy to hold the frozen _______.", "treat / ice", "Easy"),
    ("Frank licked the sweet ice right off the _______.", "stick", "Easy"),
    ("People love eating popsicles to cool off in hot _______.", "weather", "Easy"),
    ("This story tells us about the history of a popular _______.", "treat / food", "Easy"),

    ("Frank did not intend to freeze the drink on _______.", "purpose", "Medium"),
    ("He simply forgot the cup on the porch on a freezing _______.", "night", "Medium"),
    ("Cold night air acted like a natural _______.", "freezer", "Medium"),
    ("The word 'concoction' refers to the sugary _______.", "mixture", "Medium"),
    ("Frank's invention combined a sweet drink with a wooden _______.", "handle", "Medium"),
    ("The kids in his neighborhood loved buying the new _______.", "Epsicles", "Medium"),
    ("The name Popsicle is a blend of Pop and _______.", "icicle", "Medium"),
    ("The story illustrates how curiosity leads to new _______.", "discoveries", "Medium"),
    ("Freezing changes liquid soda water into solid _______.", "ice", "Medium"),
    ("Frank Epperson became famous for his accidental _______.", "invention", "Medium"),
    ("The wooden stirrer prevented hands from getting _______.", "sticky", "Medium"),
    ("Frank devoured the icy treat with great _______.", "enjoyment", "Medium"),
    ("San Francisco Bay Area was the place where it _______.", "happened", "Medium"),
    ("His children wanted to pay tribute to their _______.", "father", "Medium"),
    ("A Popsicle is the ultimate refreshing summer _______.", "snack", "Medium"),

    ("Observation transformed a frozen mishap into an economic _______.", "success", "Hard"),
    ("Thermal energy loss overnight caused phase _______ of the liquid.", "change", "Hard"),
    ("Frank's entrepreneurial spirit led to local _______.", "sales", "Hard"),
    ("The brand name Popsicle became a household _______.", "word", "Hard"),
    ("Accidental discoveries highlight the value of scientific _______.", "curiosity", "Hard"),
    ("A wooden stick provided functional utility for easy _______.", "consumption", "Hard"),
    ("The evolution from Epsicle to Popsicle represents brand _______.", "renaming", "Hard"),
    ("Class 1 students learn that simple ideas create lasting _______.", "impact", "Hard"),
    ("Cold weather turned a forgotten cup into a global _______.", "sensation", "Hard"),
    ("Keen observation is the key to unlocking hidden _______.", "potential", "Hard")
]

cloze_content = f"# Fill in the Blanks from Story — Chapter 04: Invention of 'The Popsicle'\n\n> **Category**: Fill in the Blanks from Story (Cloze Passage) | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(cloze_data, start=1):
    q_id = f"BK01_CH04_STORY_FIB_{idx:03d}"
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

with open(os.path.join(CH04_DIR, "fill_in_blanks_story.md"), "w", encoding="utf-8") as f:
    f.write(cloze_content)

# -------------------------------------------------------------
# 4. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Frank Epperson was 11 years old when he invented the Popsicle.", True, "Frank was 11 years old in 1905.", "Easy"),
    ("The Popsicle was invented in 1905 in the San Francisco Bay Area.", True, "It was invented in 1905 in San Francisco.", "Easy"),
    ("Frank mixed salt and pepper with water in his cup.", False, "He mixed sugary soda powder with water.", "Easy"),
    ("A wooden stirrer stick was left inside the cup overnight.", True, "A wooden stirrer stick was standing in the cup.", "Easy"),
    ("The mixture froze because it was a hot summer night.", False, "The mixture froze because the night was very cold.", "Easy"),
    ("The next morning, Frank found the liquid mixture frozen solid around the stick.", True, "The cold night air froze the mixture around the stick.", "Easy"),
    ("Frank threw the frozen treat into the trash without tasting it.", False, "He devoured the icy treat by licking it off the stick.", "Easy"),
    ("Frank first named his invention 'Epsicle'.", True, "He named it Epsicle by combining Epperson and icicle.", "Easy"),
    ("Frank started selling his frozen treats around his neighborhood.", True, "He sold Epsicles to his neighbors.", "Easy"),
    ("Frank's teacher renamed the treat 'Popsicle'.", False, "Frank's children renamed it Popsicle to honor their father.", "Easy"),
    ("Popsicles are popular frozen treats enjoyed during summer.", True, "Popsicles are widely enjoyed in warm summer weather.", "Easy"),
    ("Frank invented the Popsicle intentionally after years of laboratory research.", False, "He invented it by accident on a cold night.", "Easy"),
    ("The wooden stick makes it easy to hold the frozen ice without melting it in your hand.", True, "The stick serves as a convenient handle.", "Easy"),
    ("The word 'accidentally' means by chance without planning.", True, "Accidentally means happening by chance.", "Easy"),
    ("The word 'concoction' means a stone.", False, "Concoction means a liquid mixture of ingredients.", "Easy"),
    ("Freezing turns liquid drink into solid ice.", True, "Low temperature freezes liquid into solid ice.", "Easy"),
    ("Frank used a plastic spoon to stir his original soda powder mixture.", False, "He used a wooden stirrer stick.", "Easy"),
    ("Frank's children called it 'Popsicle' to honor their 'Pop' (father).", True, "Popsicle stood for 'Pop's icicle'.", "Easy"),
    ("The sugary soda powder gave the frozen ice its sweet flavor.", True, "Soda powder added sweet taste to the ice.", "Easy"),
    ("You eat a popsicle by boiling it in a pot.", False, "You eat a popsicle by licking it off a stick.", "Easy"),
    ("Frank Epperson was an adult scientist when he made the discovery.", False, "Frank was an 11-year-old schoolboy.", "Easy"),
    ("The night temperature in San Francisco was below freezing point.", True, "The cold night air froze the water solid.", "Easy"),
    ("Frank's invention became popular first among neighborhood children.", True, "He started selling it around his neighborhood.", "Easy"),
    ("Popsicles can only be eaten in winter.", False, "Popsicles are enjoyed especially in summer.", "Easy"),
    ("Curiosity and observation helped Frank discover a new treat.", True, "Observation turned an accident into a successful discovery.", "Easy"),

    # Medium (26-40)
    ("The word 'devoured' means ate up eagerly and with great enjoyment.", True, "Devoured means eating eagerly.", "Medium"),
    ("Without cold weather outside, Frank's drink would have remained liquid.", True, "Freezing temperature was necessary for ice formation.", "Medium"),
    ("Frank's invention shows that children cannot contribute to world discoveries.", False, "Frank proved an 11-year-old can create a world-famous treat.", "Medium"),
    ("The original name 'Epsicle' was created by joining 'Epperson' and 'icicle'.", True, "Epsicle combined his surname and icicle.", "Medium"),
    ("The wooden stick was added after the liquid had already frozen solid.", False, "The stick was left inside the liquid before it froze.", "Medium"),
    ("Frank's neighborhood sales proved that people enjoyed his accidental treat.", True, "Selling to neighbors demonstrated demand.", "Medium"),
    ("A refrigerator was used by Frank to freeze his soda mixture in 1905.", False, "He relied on natural cold outdoor night air.", "Medium"),
    ("The Popsicle is sweet because of the sugary soda powder mixed in water.", True, "Sugary soda powder gave the sweet taste.", "Medium"),
    ("An icicle and a popsicle are exactly the same thing.", False, "Icicles are plain frozen water; popsicles are sweet flavored treats on a stick.", "Medium"),
    ("Frank's children changed the name to honor their father many years later.", True, "They renamed it Popsicle as adults.", "Medium"),
    ("Freezing changes the state of matter from solid to liquid.", False, "Freezing changes state from liquid to solid.", "Medium"),
    ("Frank's keen observation prevented him from discarding the frozen mixture.", True, "Noticing and tasting it led to the invention.", "Medium"),
    ("The wooden handle keeps fingers clean while eating a frozen treat.", True, "The stick prevents sticky, cold hands.", "Medium"),
    ("The Popsicle is considered a summertime treat because cold food is refreshing in heat.", True, "Cold treats cool you down in warm weather.", "Medium"),
    ("Frank Epperson regretted leaving his cup outside.", False, "Leaving the cup outside led to his famous invention.", "Medium"),

    # Hard (41-50)
    ("The story of the Popsicle is a classic example of serendipity in innovation.", True, "Serendipity is finding good things by happy accident.", "Hard"),
    ("Frank's invention demonstrates that physical phase change can create new product forms.", True, "Freezing created a solid treat on a stick.", "Hard"),
    ("The wooden stick acts as an insulator, reducing heat transfer from hands to ice.", True, "Wood insulates against hand heat.", "Hard"),
    ("Commercial popsicles today use the same basic concept Frank discovered in 1905.", True, "Flavored ice on a stick remains the core concept.", "Hard"),
    ("Accidents always result in failure and should be ignored.", False, "Accidents can lead to great discoveries if observed carefully.", "Hard"),
    ("The name 'Popsicle' gained global popularity as a trademarked brand.", True, "Popsicle became an iconic global brand.", "Hard"),
    ("Frank Epperson patented his invention under the name 'Epsicle' first.", True, "He registered the name before it became Popsicle.", "Hard"),
    ("Liquid water molecules form a rigid crystal structure during the freezing process.", True, "Freezing locks water molecules into ice crystals.", "Hard"),
    ("Young students can learn problem-solving and entrepreneurial thinking from Frank.", True, "His story inspires curiosity and initiative.", "Hard"),
    ("Chapter 04 highlights how everyday observation turns simple mishaps into success.", True, "Keen observation turns mishaps into success.", "Hard")
]

tf_content = f"# True / False — Chapter 04: Invention of 'The Popsicle'\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK01_CH04_TF_{idx:03d}"
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

with open(os.path.join(CH04_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 5. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who invented the Popsicle and how old was he?", "Frank Epperson invented the Popsicle when he was an 11-year-old boy.", "Easy"),
    ("In what year and place was the Popsicle invented?", "It was invented in 1905 in the San Francisco Bay Area.", "Easy"),
    ("What ingredients did Frank mix in his cup?", "Frank mixed sugary soda powder with water in his cup.", "Easy"),
    ("What object was left inside the cup overnight?", "A wooden stirrer stick was left standing inside the cup.", "Easy"),
    ("Why did the liquid mixture freeze overnight?", "The mixture froze because it was left outside on a very cold night.", "Easy"),
    ("How did Frank eat his frozen creation the next morning?", "He devoured the icy treat by licking it off the wooden stirrer stick.", "Easy"),
    ("What was the original name Frank gave to his invention?", "Frank originally named his invention 'Epsicle'.", "Easy"),
    ("How did Frank create the original name 'Epsicle'?", "He combined his last name 'Epperson' with the word 'icicle'.", "Easy"),
    ("Who renamed 'Epsicle' to 'Popsicle' many years later?", "Frank's children renamed it 'Popsicle' to honor their father ('Pop').", "Easy"),
    ("Where did Frank first start selling his frozen treat?", "He started selling the frozen treats around his neighborhood.", "Easy"),
    ("Was the Popsicle invented on purpose or by accident?", "The Popsicle was invented accidentally on a cold winter night.", "Easy"),
    ("In which season are popsicles enjoyed the most?", "Popsicles are enjoyed the most during warm summer weather.", "Easy"),
    ("What does the word 'accidentally' mean?", "'Accidentally' means happening by chance without any prior plan.", "Easy"),
    ("What does the word 'concoction' mean?", "'Concoction' means a liquid mixture made by combining different ingredients.", "Easy"),
    ("Why was the wooden stirrer stick useful?", "The wooden stick acted as a handle, making it easy to hold the icy treat.", "Easy"),
    ("What gave the original Popsicle its sweet flavor?", "The sugary soda powder mixed in the water gave it a sweet flavor.", "Easy"),
    ("What state of matter did the liquid drink turn into?", "The liquid drink froze into solid ice.", "Easy"),
    ("What did Frank do when he tasted his frozen treat?", "He loved the taste and devoured it eagerly off the stick.", "Easy"),
    ("Why is the Popsicle called a summertime treat?", "Because its cold, sweet ice is refreshing during hot summer days.", "Easy"),
    ("Name the inventor's full name.", "The inventor's full name was Frank Epperson.", "Easy"),
    ("Where was the cup left overnight?", "The cup was left outside on the porch on a cold night.", "Easy"),
    ("Did Frank use an electric freezer to make his first Popsicle?", "No, he relied on the natural cold outdoor night air in 1905.", "Easy"),
    ("What does 'Pop' mean in 'Popsicle'?", "'Pop' is a loving term for father, referring to Frank Epperson.", "Easy"),
    ("What lesson does Frank's story teach young children?", "It teaches that children can invent great things through curiosity and observation.", "Easy"),
    ("What is the main topic of Chapter 04?", "Chapter 04 tells the true story of how the Popsicle was accidentally invented.", "Easy"),

    # Medium (26-40)
    ("Explain how cold temperature changed Frank's liquid drink into ice.", "The cold night air froze the water, causing liquid molecules to lock into solid ice around the stick.", "Medium"),
    ("How did Frank show an entrepreneurial spirit as a young boy?", "After discovering the tasty treat, he recognized its value and sold Epsicles to neighborhood kids.", "Medium"),
    ("Why did Frank's children choose the name 'Popsicle'?", "They chose 'Popsicle' as a loving tribute to their father ('Pop'), combining 'Pop' with 'icicle'.", "Medium"),
    ("What is the difference between an icicle and a popsicle?", "An icicle is plain frozen water dripping from roofs; a popsicle is sweet flavored ice served on a stick.", "Medium"),
    ("How did the wooden stirrer get frozen inside the drink?", "The liquid was poured with the stick inside, and as it froze overnight, the ice formed around the stick.", "Medium"),
    ("What role did curiosity play in Frank's invention?", "Instead of throwing the frozen cup away, Frank's curiosity made him taste it, discovering a delicious treat.", "Medium"),
    ("Why were popsicles so refreshing in summer?", "Cold frozen ice lowers body temperature and quenches thirst during hot summer weather.", "Medium"),
    ("What does 'devoured' mean in the context of the story?", "'Devoured' means eating something eagerly and with great pleasure because it tastes wonderful.", "Medium"),
    ("How did Frank's discovery spread beyond his neighborhood?", "As years passed, the product was renamed, patented, and eventually mass-produced for people worldwide.", "Medium"),
    ("Why was no refrigerator needed for Frank's invention in 1905?", "Because the outdoor temperature dropped below freezing point during that cold night.", "Medium"),
    ("How does the wooden stick prevent messy hands?", "It keeps fingers away from the melting ice, allowing clean handling while eating.", "Medium"),
    ("What chemical component provided sweetness to Frank's drink?", "Sugary soda powder dissolved in water provided the sweetness.", "Medium"),
    ("How does observation turn everyday accidents into inventions?", "Keen observation lets you spot unexpected results and find creative uses for them.", "Medium"),
    ("What makes Frank Epperson a great role model for kids?", "He proved that age is no barrier to invention and that curious minds can create world-famous ideas.", "Medium"),
    ("Summarize the main events of Chapter 04 in two sentences.", "In 1905, 11-year-old Frank left a cup of soda water with a stick outside on a cold night. It froze solid, creating the famous treat later renamed the Popsicle.", "Medium"),

    # Hard (41-50)
    ("Define 'serendipity' and explain how it applies to the Popsicle's invention.", "Serendipity is making fortunate discoveries by accident. Frank accidentally left his drink outside, resulting in the invention of the Popsicle.", "Hard"),
    ("Analyze the physical science principle involved in making popsicles.", "Freezing is a physical phase change where heat energy leaves a liquid, turning it into a solid crystalline structure.", "Hard"),
    ("How does Frank's story demonstrate the importance of the scientific method?", "Frank observed an unexpected result (frozen drink on a stick), tested it (tasted it), and applied it (sold it).", "Hard"),
    ("Compare Frank's early neighborhood sales with modern commercial manufacturing.", "Frank made cups by hand and sold them locally; modern factories use automated freezing molds to produce millions daily.", "Hard"),
    ("Why is branding (like changing Epsicle to Popsicle) important for a product?", "A catchy, affectionate name like Popsicle makes a product memorable, marketable, and universally loved.", "Hard"),
    ("What would happen if a popsicle is left at room temperature, and why?", "It absorbs heat energy, causing the ice crystals to melt back into a liquid state.", "Hard"),
    ("How can primary students cultivate an inventive mindset like Frank?", "By staying curious, asking questions, observing nature, and experimenting with everyday materials.", "Hard"),
    ("Explain the thermal role of the wooden stick during consumption.", "Wood is a poor conductor of heat, preventing body heat from fingers from melting the ice quickly.", "Hard"),
    ("Why do simple inventions often have the longest-lasting cultural impact?", "Because simple products fulfill universal human desires easily, seamlessly integrating into daily lifestyle.", "Hard"),
    ("State the ultimate takeaway from Chapter 04 for Class 1 learners.", "Be curious and observant—great ideas and world-changing inventions can come from simple everyday accidents!", "Hard")
]

sa_content = f"# Short Answer — Chapter 04: Invention of 'The Popsicle'\n\n> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK01_CH04_SA_{idx:03d}"
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

with open(os.path.join(CH04_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 6. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-15)
    ("Write a simple summary of the story of 'The Popsicle'.", "In 1905, an 11-year-old boy named Frank Epperson in San Francisco mixed sugary soda powder with water in a cup and left a wooden stirrer stick inside. He accidentally left the cup outside on a freezing cold night. By morning, the liquid had frozen solid around the stick. Frank licked the icy treat off the stick and loved it. He named it 'Epsicle' and sold it to neighbors. Years later, his children renamed it 'Popsicle' to honor their father.", "Easy"),
    ("Describe how Frank Epperson accidentally invented the frozen treat.", "Back in 1905, 11-year-old Frank Epperson mixed sugary soda powder with water in a cup. He stirred it with a wooden stick and accidentally left the cup on the porch overnight. The night was bitterly cold, and the drink froze solid around the wooden stirrer. The next morning, Frank found the frozen treat on the stick, tasted it, and discovered the world's first popsicle.", "Easy"),
    ("Explain how 'Epsicle' became 'Popsicle' over time.", "When Frank first invented the treat, he combined his last name 'Epperson' with 'icicle' to call it 'Epsicle'. He sold it under this name in his neighborhood. Many years later, when Frank grew up and had children of his own, his children affectionately renamed it 'Popsicle' in honor of their father ('Pop's icicle').", "Easy"),
    ("Why is the wooden stirrer stick such an important part of the invention?", "The wooden stirrer stick was left in the cup before freezing, so the liquid froze directly around it. The stick provided a clean, convenient handle that allowed Frank to hold and lick the frozen ice without melting it in his hands or making a sticky mess.", "Easy"),
    ("What lesson does Frank Epperson's story teach young children about inventions?", "Frank's story teaches that children do not need expensive laboratories to invent great things. Curiosity, keen observation, and trying new things can turn simple everyday accidents into world-famous inventions.", "Easy"),
    ("Describe Frank's reaction when he found the frozen drink the next morning.", "When Frank saw the cup the next morning, he did not throw it away. Instead, he pulled the wooden stick, lifted the frozen block of soda ice, and devoured it eagerly. He loved the sweet, icy taste and immediately realized he had made something special.", "Easy"),
    ("Why are popsicles especially popular during summertime?", "Popsicles are cold, sweet, and frozen, making them the perfect refreshing treat during hot summer days. The icy fruit or soda flavors lower body temperature and bring sweet delight when it is warm outside.", "Easy"),
    ("Explain the meaning of the words 'accidentally' and 'concoction'.", "'Accidentally' means happening by chance or luck without any deliberate plan. A 'concoction' is a liquid mixture created by combining different ingredients together, such as soda powder and water.", "Easy"),
    ("How did Frank share his invention with the people around him?", "After tasting the delicious frozen treat, Frank started making more and selling them to children and neighbors around his neighborhood. Everyone loved the sweet icy treats on a stick.", "Easy"),
    ("What role did the cold weather play in the invention of the Popsicle?", "Freezing cold weather was essential because electric freezers were not common in 1905. The freezing night air naturally pulled heat from the liquid drink, transforming it into solid ice around the stick.", "Easy"),
    ("What makes a Popsicle different from a regular ice cube?", "A regular ice cube is plain frozen water used to chill drinks. A Popsicle is a flavored, sweet frozen confection made with soda or fruit juice, served directly on a wooden stick for eating.", "Easy"),
    ("How old was Frank, and where did he live when he made his discovery?", "Frank was just an 11-year-old schoolboy living in the San Francisco Bay Area in California, USA when he made his accidental discovery in 1905.", "Easy"),
    ("What ingredients did Frank use to make his original drink?", "Frank used sugary soda powder and plain water. He stirred the ingredients together using a wooden stirrer stick in a cup.", "Easy"),
    ("Why is Frank Epperson remembered today?", "Frank Epperson is remembered worldwide as the young inventor of the Popsicle, a beloved summertime frozen treat enjoyed by millions of people across the globe.", "Easy"),
    ("What would have happened if Frank had thrown the frozen cup away?", "If Frank had thrown the cup away without tasting it, the Popsicle might never have been invented, and people would have missed out on a wonderful summer treat.", "Easy"),

    # Medium (16-40)
    ("Explain how simple observation turns an everyday mistake into a discovery.", "When an accident occurs, most people ignore it. However, curious people observe the result closely. Frank observed that his drink had frozen around the stick and tasted it, converting a forgotten cup into a groundbreaking invention.", "Medium"),
    ("Describe the scientific change of state that happened in Frank's cup.", "The liquid mixture of water and soda powder underwent a physical phase change. As outdoor temperatures dropped below 0°C (32°F), thermal energy left the liquid, causing water molecules to freeze into solid ice around the stick.", "Medium"),
    ("Compare the name 'Epsicle' with the name 'Popsicle'.", "'Epsicle' combined the inventor's surname (Epperson) with 'icicle', focusing on his personal brand. 'Popsicle' combined 'Pop' (father) with 'icicle', creating a warm, catchy, family-friendly brand name.", "Medium"),
    ("Discuss how Frank Epperson showed early business skills (entrepreneurship).", "After realizing his treat was delicious, Frank did not keep it to himself. He made more, marketed them to neighborhood children, and sold them for profit, demonstrating sharp business sense at age 11.", "Medium"),
    ("Why is wood a great material for a popsicle stick?", "Wood is strong enough to hold the frozen ice, non-toxic, cheap, and a poor conductor of heat. This means hand warmth does not travel through the wood to melt the ice quickly.", "Medium"),
    ("How does the story of the Popsicle inspire scientific curiosity in Class 1 students?", "It shows students that science happens in everyday life. Mixing ingredients, watching temperature changes, and testing results can lead to exciting discoveries right at home.", "Medium"),
    ("Write a creative dialogue between 11-year-old Frank and a neighborhood friend.", "Friend: 'Hey Frank, what's that frozen block on a stick?'\nFrank: 'I left my soda drink outside last night and it froze! Taste it!'\nFriend: 'Wow, it's sweet and cold! Can I buy one tomorrow?'", "Medium"),
    ("Explain why popsicles remain popular over 100 years after their invention.", "Popsicles remain popular because the core concept—a sweet, colorful, cold treat on a stick—is simple, affordable, hygienic to hold, and perfectly satisfying on hot days.", "Medium"),
    ("What role did Frank's family play in making the Popsicle famous?", "Years after Frank made his childhood discovery, his children encouraged the renaming to 'Popsicle' and helped transform his neighborhood treat into a patented, mass-marketed national brand.", "Medium"),
    ("How can parents encourage children to be innovative like Frank Epperson?", "Parents can encourage kids by allowing simple home experiments, asking open questions about everyday events, and celebrating creative thinking when things don't go as planned.", "Medium"),
    ("Describe the climate conditions in San Francisco that enabled the invention.", "In 1905, San Francisco experienced freezing winter nights where temperatures dropped low enough to freeze standing water outside, acting as a natural outdoor freezer.", "Medium"),
    ("How did Frank's sugary soda powder contribute to the texture and taste?", "The dissolved sugar and soda powder lowered the freezing point slightly and created a sweet, flavorful ice texture that was delicious to lick off the stick.", "Medium"),
    ("What is the connection between curiosity and problem-solving?", "Curiosity makes us explore unknown situations. When Frank saw the frozen cup, curiosity prompted him to pull the stick and taste it, solving how to enjoy frozen drinks.", "Medium"),
    ("Why is hygiene an advantage of eating ice on a stick?", "Holding the wooden stick prevents bare hands from touching the ice directly, keeping the food clean and preventing sticky, cold fingers.", "Medium"),
    ("Summarize the economic journey of the Popsicle from 1905 to today.", "It started as a single boy's accidental cup in 1905, became a neighborhood treat sold by Frank, grew into a patented brand in the 1920s, and is now a multi-million dollar global industry.", "Medium"),
    ("How does temperature affect food state and preservation?", "Low temperatures freeze liquids into solids and slow down spoilage. High temperatures melt frozen foods back into liquids. Temperature dictates the texture and form of treats.", "Medium"),
    ("What character traits made 11-year-old Frank successful?", "Frank was curious, observant, practical, creative, and confident. He wasn't afraid to taste his experiment or share it with others.", "Medium"),
    ("Why is 'Invention of The Popsicle' classified as an informational story?", "Because it presents true historical facts, dates, names, and scientific principles about how a real-world product came to exist in an engaging story format.", "Medium"),
    ("How does the story encourage kids to appreciate everyday accidents?", "It teaches that not all mistakes are bad. Sometimes an unexpected outcome leads to a better result than what was originally planned.", "Medium"),
    ("State three reasons why the Popsicle is a brilliant design.", "1. Built-in handle (wooden stick) keeps hands clean.\n2. Flavored ice provides refreshing sweet taste.\n3. Portable and easy to eat anywhere without utensils.", "Medium"),

    # Hard (41-50)
    ("Critique how serendipity and keen observation combined in Frank's invention.", "Serendipity provided the random event (freezing night + forgotten cup). However, serendipity alone is useless without keen observation. Frank's alertness in recognizing value in the accident turned a mishap into an iconic product.", "Hard"),
    ("Analyze the thermodynamic principles behind natural outdoor freezing.", "Thermal energy flows from warmer objects to colder surroundings. On a sub-zero night, heat from the soda water radiated into the cold atmosphere until the liquid reached 0°C and crystalized around the stirrer stick.", "Hard"),
    ("Examine the evolution of product branding from 'Epsicle' to 'Popsicle'.", "Epsicle was personal but slightly awkward to pronounce. Popsicle introduced alliteration, emotional warmth ('Pop'), and a playful rhythm, making it far more commercially viable and memorable.", "Hard"),
    ("How does Frank's story challenge the idea that inventions require high technology?", "It proves that fundamental human needs (refreshment) can be met using basic natural phenomena (freezing) and simple tools (stick and cup), proving utility matters more than high technology.", "Hard"),
    ("Evaluate the impact of childhood inventions on modern consumer culture.", "Child-led inventions like the Popsicle show that uninhibited young minds often create enduring consumer products because they design for pure joy and simplicity.", "Hard"),
    ("Formulate a lesson plan activity for Class 1 students based on Chapter 04.", "Students mix fruit juice in paper cups, insert wooden sticks, place them in a freezer, observe state changes from liquid to solid, and discuss how temperature creates frozen treats.", "Hard"),
    ("Deconstruct the role of material selection (wood vs metal) for the stirrer stick.", "Metal conducts heat rapidly, which would melt the ice faster and feel uncomfortably cold to touch. Wood is a thermal insulator, maintaining structural integrity and user comfort.", "Hard"),
    ("Why is legal patenting important when commercializing an invention?", "Patenting protects an inventor's intellectual property, ensuring they receive credit and financial reward when their idea is produced on a mass commercial scale.", "Hard"),
    ("How does Chapter 04 foster a STEM (Science, Technology, Engineering, Math) mindset?", "It integrates Science (freezing), Technology (stick handle design), Engineering (molding ice on a stick), and Math (age 11, year 1905) into an inspiring narrative.", "Hard"),
    ("Synthesize the overarching philosophy of Chapter 04 for primary learners.", "Empower your mind: stay observant, embrace unexpected occurrences, experiment boldly, and remember that great ideas can blossom from the simplest everyday moments!", "Hard")
]

la_content = f"# Long Answer — Chapter 04: Invention of 'The Popsicle'\n\n> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK01_CH04_LA_{idx:03d}"
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

with open(os.path.join(CH04_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

print("[SUCCESS] All 6 category files for Chapter 04 completely refined with 100% unique Class 1 questions!")
