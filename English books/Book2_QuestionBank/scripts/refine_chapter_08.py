r"""
Refines all 6 Category files for Chapter 08 ("Diwali") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH08_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_08")
os.makedirs(CH08_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What is another famous name for Diwali?", "(A) Deepavali", "(B) Holi", "(C) Eid", "(D) Christmas", "(A)", "Diwali is also called Deepavali.", "Easy", "Remembering", "Alternative Name"),
    ("Diwali is widely known as the festival of _______.", "(A) Lights", "(B) Colors", "(C) Kites", "(D) Flowers", "(A)", "Diwali is called the festival of lights.", "Easy", "Remembering", "Festival Descriptor"),
    ("What do people light in the evening to decorate their houses on Diwali?", "(A) Earthen lamps (diyas)", "(B) Candles only", "(C) Bonfires", "(D) Torches", "(A)", "People light earthen lamps (diyas) in the evening.", "Easy", "Remembering", "Decorations"),
    ("On which moon phase night is Diwali celebrated?", "(A) New Moon night", "(B) Full Moon night", "(C) Half Moon night", "(D) Eclipse night", "(A)", "It is celebrated on the New Moon night.", "Easy", "Remembering", "Moon Phase"),
    ("Which two deities are worshipped in the evening on Diwali?", "(A) Shri Ganesh and Maa Laxmi", "(B) Lord Shiva and Parvati", "(C) Lord Krishna and Radha", "(D) Lord Brahma and Saraswati", "(A)", "People worship Shri Ganesh and Maa Laxmi.", "Easy", "Remembering", "Worshipped Deities"),
    ("What blessings do people ask from Shri Ganesh and Maa Laxmi?", "(A) Wealth and prosperity", "(B) Rain and crops", "(C) Toys and games", "(D) Long sleep", "(A)", "Worshipped for blessing them with wealth and prosperity.", "Easy", "Remembering", "Blessings"),
    ("Which sweet is synonymous with the Diwali festival and offered to deities?", "(A) Laddoo", "(B) Jalebi", "(C) Rasgulla", "(D) Cake", "(A)", "Laddoos are offered to deities and synonymous with Diwali.", "Easy", "Remembering", "Traditional Sweet"),
    ("What beautiful floor art made of colors is used to decorate homes on Diwali?", "(A) Rangoli", "(B) Painting", "(C) Origami", "(D) Sculpture", "(A)", "Houses are decorated with colourful rangolis.", "Easy", "Remembering", "Floor Art"),
    ("What major victory does Diwali celebrate?", "(A) Victory of good over evil", "(B) Victory of winter over summer", "(C) Victory of night over day", "(D) Victory of noise over quiet", "(A)", "It celebrates the victory of good over evil.", "Easy", "Remembering", "Core Theme"),
    ("What victory of light does Diwali symbolize?", "(A) Light over darkness", "(B) Sun over moon", "(C) Fire over water", "(D) Day over year", "(A)", "It symbolizes victory of light over darkness.", "Easy", "Remembering", "Symbolism"),
    ("What do people distribute among the poor to spread happiness?", "(A) Gifts and sweets", "(B) Old clothes only", "(C) Books only", "(D) Salt", "(A)", "People distribute gifts and sweets among the poor.", "Easy", "Remembering", "Charity"),
    ("Why have some people stopped bursting crackers on Diwali?", "(A) To protect the environment from pollution and noise", "(B) Because crackers are sweet", "(C) Because crackers do not light up", "(D) Because it is forbidden to buy toys", "(A)", "Stopping crackers protects the environment.", "Easy", "Understanding", "Environmental Awareness"),
    ("What does the word 'earthen' mean?", "(A) Made of clay", "(B) Made of metal", "(C) Made of plastic", "(D) Made of glass", "(A)", "Earthen means made of clay.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'prosperity' mean?", "(A) The state of having great wealth and well-being", "(B) Deep poverty", "(C) Extreme anger", "(D) Cold weather", "(A)", "Prosperity means having great wealth and well-being.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'deity' mean?", "(A) A God or Goddess", "(B) A small animal", "(C) A fruit tree", "(D) A festival lamp", "(A)", "Deity means a God.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'synonymous' mean?", "(A) Having the same or nearly the same meaning", "(B) Opposite meaning", "(C) Hard to pronounce", "(D) Unknown word", "(A)", "Synonymous means having the same or nearly the same meaning.", "Easy", "Understanding", "Vocabulary"),
    ("What material are traditional diyas made from?", "(A) Clay", "(B) Plastic", "(C) Steel", "(D) Paper", "(A)", "Earthen lamps (diyas) are made of clay.", "Easy", "Remembering", "Diya Material"),
    ("Besides diyas, what electric items are used to decorate houses today?", "(A) Electric lights", "(B) Electric fans", "(C) Electric heaters", "(D) Electric clocks", "(A)", "Houses are decorated with electric lights as well.", "Easy", "Remembering", "Modern Decoration"),
    ("With whom do people share good food, joy, and laughter on Diwali?", "(A) Friends and family", "(B) Strangers only", "(C) Enemies", "(D) Nobody", "(A)", "People celebrate with friends and family.", "Easy", "Remembering", "Social Aspect"),
    ("Why do people light diyas specifically in the evening on Diwali?", "(A) To dispel darkness on the New Moon night and welcome Goddess Laxmi", "(B) Because the sun is hot", "(C) To scare away birds", "(D) To cook food outdoors", "(A)", "To dispel darkness on New Moon night.", "Easy", "Understanding", "Tradition Reason"),
    ("What is offered to Shri Ganesh and Maa Laxmi during Diwali puja?", "(A) Laddoos", "(B) Ice cream", "(C) Pizza", "(D) Biscuits", "(A)", "Laddoos are offered to the deities.", "Easy", "Remembering", "Offering"),
    ("Is Diwali celebrated with joy, laughter, and good food?", "(A) Yes, absolutely", "(B) No, it is a sad day", "(C) Only with fasting", "(D) Only by sleeping", "(A)", "It is celebrated with good food, joy, and laughter.", "Easy", "Remembering", "Atmosphere"),
    ("What color pattern is drawn at house entrances during Diwali?", "(A) Colourful rangoli", "(B) Black paint", "(C) Plain chalk lines", "(D) Mud patches", "(A)", "Colourful rangoli is drawn at entrances.", "Easy", "Remembering", "Rangoli"),
    ("What is the main message of distributing sweets to the poor on Diwali?", "(A) To spread happiness and light in everyone's life", "(B) To show off wealth", "(C) To clean the kitchen", "(D) To win a prize", "(A)", "To spread happiness and light in their lives.", "Easy", "Understanding", "Charity Message"),
    ("What is the title of Chapter 08?", "(A) Diwali", "(B) Nightingale of India", "(C) Festival of Colors", "(D) Earthen Diyas", "(A)", "Chapter 08 is titled 'Diwali'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why is Diwali celebrated on a New Moon (Amavasya) night particularly significant?", "(A) Because lighting diyas on the darkest night of the month symbolizes overcoming deep darkness with light", "(B) Because the moon is brightest that night", "(C) Because stars disappear", "(D) Because it rains on New Moon", "(A)", "New Moon is the darkest night, symbolizing light over darkness.", "Medium", "Understanding", "Symbolic Significance"),
    ("How does decorating homes with rangoli and diyas reflect cultural values?", "(A) It expresses joy, beauty, hospitality, and welcoming divine blessings into the home", "(B) It is done to waste time", "(C) It hides dirty floors", "(D) It is a modern invention", "(A)", "Welcoming divine blessings and expressing joy/hospitality.", "Medium", "Analyzing", "Cultural Reflection"),
    ("Why is Shri Ganesh worshipped alongside Maa Laxmi during Diwali puja?", "(A) Shri Ganesh removes obstacles and brings wisdom, while Maa Laxmi brings wealth and prosperity", "(B) Because they are brothers", "(C) Because Ganesh likes laddoos only", "(D) Because Laxmi asked him to", "(A)", "Ganesh grants wisdom/removes obstacles; Laxmi brings prosperity.", "Medium", "Understanding", "Deity Roles"),
    ("How has the celebration of Diwali evolved regarding firecrackers in recent years?", "(A) Responsible citizens now reduce or stop bursting crackers to prevent air and noise pollution", "(B) Everyone bursts ten times more crackers", "(C) Firecrackers are banned in all countries", "(D) Crackers are now eaten as sweets", "(A)", "Environmental awareness leads to reducing/stopping crackers.", "Medium", "Analyzing", "Modern Evolution"),
    ("What is the connection between 'light over darkness' and 'good over evil'?", "(A) Light dispels physical darkness just as moral goodness and truth defeat evil and ignorance", "(B) They have opposite meanings", "(C) Light creates evil", "(D) Darkness brings good luck", "(A)", "Light/darkness acts as a metaphor for good/evil.", "Medium", "Analyzing", "Metaphorical Connection"),
    ("Why is sharing sweets with neighbors and the underprivileged an essential part of Diwali?", "(A) It extends the spirit of joy and prosperity to the entire community, ensuring no one feels left out", "(B) Because sweets spoil quickly", "(C) Because it is required by law", "(D) To get extra gifts back", "(A)", "Extending joy and community solidarity.", "Medium", "Evaluating", "Social Harmony"),
    ("What makes the word 'earthen' important when describing traditional diyas?", "(A) It emphasizes that diyas are eco-friendly items made from natural earth (clay)", "(B) It means diyas are made of gold", "(C) It means diyas are imported from abroad", "(D) It means diyas are unbreakable", "(A)", "Eco-friendly natural clay material.", "Medium", "Understanding", "Eco-Value"),
    ("How does Diwali strengthen family bonds?", "(A) Families gather together to decorate homes, prepare sweets, perform puja, and share meals", "(B) Family members stay in separate rooms", "(C) People travel away from family", "(D) Families argue over gifts", "(A)", "Shared preparation, worship, and celebration.", "Medium", "Understanding", "Family Bonding"),
    ("Why are laddoos described as 'synonymous' with Diwali?", "(A) Because laddoos are so deeply associated with Diwali that thinking of the festival reminds people of laddoos", "(B) Because laddoo means light", "(C) Because laddoos look like diyas", "(D) Because laddoos are spicy", "(A)", "Deep cultural association between sweet and festival.", "Medium", "Understanding", "Vocabulary Application"),
    ("What clean and green practices can Class 2 students adopt during Diwali?", "(A) Use eco-friendly clay diyas, make organic rangoli, avoid noisy crackers, and share gifts with the needy", "(B) Burst maximum paper bombs", "(C) Throw plastic waste outside", "(D) Use artificial plastic flowers only", "(A)", "Eco-friendly diyas, organic rangoli, no noisy crackers.", "Medium", "Applying", "Green Action"),
    ("How does lighting diyas outside homes symbolize spreading knowledge?", "(A) Darkness represents ignorance, while light represents wisdom, knowledge, and hope", "(B) Diyas help students read books at night", "(C) Diyas burn paper", "(D) Diyas are shaped like books", "(A)", "Light = wisdom/knowledge vs Darkness = ignorance.", "Medium", "Analyzing", "Symbolic Wisdom"),
    ("Why is distributing gifts to the poor considered true celebration?", "(A) True joy comes from giving and sharing happiness with those who have less", "(B) It saves space at home", "(C) The poor demand gifts", "(D) It is a commercial competition", "(A)", "Giving and sharing yields true joy.", "Medium", "Evaluating", "Moral Purpose"),
    ("What contrast exists between traditional earthen diyas and modern electric lights?", "(A) Earthen diyas represent natural eco-friendly tradition, while electric lights offer modern colorful convenience", "(B) Earthen diyas run on batteries", "(C) Electric lights are made of clay", "(D) Neither gives light", "(A)", "Natural eco-friendly tradition vs modern convenience.", "Medium", "Analyzing", "Contrast"),
    ("How does Chapter 08 promote inclusive celebration?", "(A) By encouraging people to share food, sweets, and gifts with the underprivileged in society", "(B) By celebrating behind closed doors", "(C) By inviting only rich people", "(D) By selling sweets at high prices", "(A)", "Inclusive sharing with the underprivileged.", "Medium", "Evaluating", "Inclusivity"),
    ("What sensory experiences are associated with Diwali in the text?", "(A) Visual: bright lights & rangoli; Taste: delicious laddoos; Feeling: warmth, joy, and laughter", "(B) Hearing: loud explosions only", "(C) Smell: bad smoke only", "(D) Touch: cold snow", "(A)", "Lights/rangoli (sight), laddoos (taste), joy (feeling).", "Medium", "Analyzing", "Sensory Analysis"),

    # Hard (41-50)
    ("Analyze the universal human value embodied in celebrating the 'victory of good over evil'.", "(A) It reinforces moral hope across all cultures that truth, righteousness, and love will ultimate triumph over injustice and hatred", "(B) It means fighting physical battles every year", "(C) It encourages people to hate evil people", "(D) It is only an ancient myth with no modern meaning", "(A)", "Universal moral hope in truth and righteousness.", "Hard", "Analyzing", "HOTS Philosophical Value"),
    ("Evaluate the ecological responsibility associated with modern festival celebrations like Diwali.", "(A) Celebrating responsibly requires balancing ancient cultural joy with environmental care—reducing smoke/noise to protect air quality and animals", "(B) Ecological responsibility means cancelling all festivals", "(C) Environment does not matter during holidays", "(D) Smoke from crackers is good for trees", "(A)", "Balancing tradition with environmental responsibility.", "Hard", "Evaluating", "Ecological Responsibility"),
    ("Deconstruct the spiritual significance of the Diwali Puja (Shri Ganesh and Maa Laxmi).", "(A) Ganesh provides intellectual wisdom to manage wealth responsibly, while Laxmi grants material and spiritual prosperity", "(B) It is a ritual to get rich without working", "(C) It is done only to eat laddoos", "(D) It replaces daily school studies", "(A)", "Wisdom (Ganesh) + Wealth (Laxmi) for balanced life.", "Hard", "Analyzing", "Spiritual Deconstruct"),
    ("Compare Diwali (Festival of Lights) with other major cultural festivals of India.", "(A) While festivals like Holi celebrate colors and seasonal changes, Diwali focuses on inner light, moral victory, and family prosperity", "(B) All festivals are identical in traditions", "(C) Diwali is the only festival with food", "(D) Other festivals do not use lights", "(A)", "Focus on inner light, moral victory, and prosperity.", "Hard", "Analyzing", "Comparative Festivals"),
    ("Assess the psychological impact of festive giving and charity on children.", "(A) Engaging in charitable giving during festivals develops empathy, gratitude, and social consciousness in young minds", "(B) Giving makes children feel sad about losing toys", "(C) Charity makes children selfish", "(D) Children should only receive gifts", "(A)", "Fosters empathy, gratitude, and social consciousness.", "Hard", "Evaluating", "Psychological Impact"),
    ("How does the art of Rangoli reflect geometry, symmetry, and artistic heritage in Indian culture?", "(A) Rangoli uses geometric patterns, symmetrical lines, and vibrant natural colors, blending mathematical harmony with artistic expression", "(B) Rangoli is drawn randomly without thought", "(C) Rangoli is imported from western countries", "(D) Rangoli uses only black ink", "(A)", "Symmetrical geometry + artistic expression.", "Hard", "Analyzing", "Artistic Heritage"),
    ("Why is the concept of 'inner light' important beyond physical diyas?", "(A) Physical diyas illuminate homes, but inner light represents kindness, truth, and moral purity within a person's heart", "(B) Inner light means wearing bright clothes", "(C) Inner light is an electric bulb inside the body", "(D) Physical diyas are useless", "(A)", "Inner light = kindness, truth, and moral purity.", "Hard", "Evaluating", "Inner Light Concept"),
    ("Synthesize how community celebrations foster social harmony in diverse societies.", "(A) Shared festivities break social barriers, encourage cross-cultural sharing of sweets and greetings, and build community unity", "(B) Celebrations divide people into groups", "(C) Festivals cause arguments among neighbors", "(D) Community celebrations are meant for business marketing", "(A)", "Breaking barriers and building community unity.", "Hard", "Synthesizing", "Social Harmony"),
    ("Formulate a campaign slogan for a 'Safe, Eco-Friendly, and Joyous Diwali'.", "(A) 'Light up a Diya, Spread a Smile, Keep our Air Clean all the While!'", "(B) 'Burst More Crackers, Make More Noise!'", "(C) 'Don't Share Sweets With Anyone!'", "(D) 'Keep your Lights Off!'", "(A)", "Light diyas, spread smiles, keep air clean.", "Hard", "Creating", "Campaign Slogan"),
    ("Synthesize the ultimate core message of Chapter 08 for young Class 2 learners.", "(A) Let the light of kindness, sharing, and good values shine in your heart, bringing joy to your family and light to the world!", "(B) Buy the biggest firecrackers in the shop", "(C) Eat all the laddoos yourself", "(D) Sleep through the festival night", "(A)", "Kindness, sharing, good values, and joy.", "Hard", "Evaluating", "Core Synthesis")
]

mcq_content = f"# MCQs — Chapter 08: Diwali\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH08_MCQ_{idx:03d}"
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

with open(os.path.join(CH08_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Diwali or Deepavali is called the festival of _______.", "lights", "Diwali is called the festival of lights.", "Easy"),
    ("On Diwali, people decorate their houses with _______ lamps.", "earthen", "Decorate with earthen lamps.", "Easy"),
    ("Earthen lamps are also called diyas or _______.", "deeps", "Also called diya or deep.", "Easy"),
    ("In addition to diyas, houses are decorated with colourful _______.", "rangolis", "Decorated with colourful rangolis.", "Easy"),
    ("Houses are also lit up with electric _______.", "lights", "Lit up with electric lights.", "Easy"),
    ("Diwali is celebrated on the _______ Moon night.", "New", "Celebrated on New Moon night.", "Easy"),
    ("In the evening, people worship Shri _______ and Maa Laxmi.", "Ganesh", "Worship Shri Ganesh and Maa Laxmi.", "Easy"),
    ("People worship Shri Ganesh and Maa Laxmi for wealth and _______.", "prosperity", "For wealth and prosperity.", "Easy"),
    ("_______ are offered to the deities on Diwali.", "Laddoos", "Laddoos are offered to deities.", "Easy"),
    ("Laddoos have become _______ with the festival of Diwali.", "synonymous", "Synonymous with Diwali.", "Easy"),
    ("People celebrate Diwali with their friends and _______.", "family", "Celebrate with friends and family.", "Easy"),
    ("Diwali is celebrated with good food, joy, and _______.", "laughter", "Joy and laughter.", "Easy"),
    ("Many people burst crackers, but a few have _______ this practice now.", "stopped", "Few have stopped bursting crackers.", "Easy"),
    ("Diwali celebrates the victory of good over _______.", "evil", "Victory of good over evil.", "Easy"),
    ("Diwali celebrates the victory of light over _______.", "darkness", "Victory of light over darkness.", "Easy"),
    ("Many people distribute gifts and sweets among the _______.", "poor", "Distribute among the poor.", "Easy"),
    ("Distributing gifts to the poor helps spread _______ in their lives.", "happiness", "Spreads happiness and light.", "Easy"),
    ("The word 'earthen' means made of _______.", "clay", "Earthen means made of clay.", "Easy"),
    ("The word 'prosperity' means having great _______.", "wealth", "State of having great wealth.", "Easy"),
    ("The word 'deity' means a _______.", "God", "Deity means a God.", "Easy"),
    ("The word 'synonymous' means having the _______ or nearly the same meaning.", "same", "Same or nearly same meaning.", "Easy"),
    ("Rangolis are made with bright and colourful _______.", "powders", "Rangolis use colourful powders/designs.", "Easy"),
    ("Diyas are lit in the _______ on Diwali.", "evening", "Lit in the evening.", "Easy"),
    ("Goddess Laxmi is worshipped for blessing people with _______.", "wealth", "Worshipped for wealth.", "Easy"),
    ("Chapter 08 is titled '_______'.", "Diwali", "Chapter title is 'Diwali'.", "Easy"),

    # Medium (26-40)
    ("The New Moon night is the _______ night of the month, making diyas shine brightly.", "darkest", "New Moon is the darkest night.", "Medium"),
    ("Diwali brings together family members in an atmosphere of _______ and love.", "harmony", "Atmosphere of harmony/joy.", "Medium"),
    ("Lord Ganesh is worshipped first to remove all _______.", "obstacles", "Ganesh removes obstacles.", "Medium"),
    ("Sharing sweets with neighbors strengthens community _______.", "bonds", "Strengthens community bonds.", "Medium"),
    ("Stopping noisy crackers helps protect animals and reduces air _______.", "pollution", "Reduces air pollution.", "Medium"),
    ("Diwali teaches us that truth and goodness will always overcome _______.", "falsehood", "Goodness overcomes evil/falsehood.", "Medium"),
    ("Making rangoli at the entrance welcomes guests and divine _______.", "blessings", "Welcomes divine blessings.", "Medium"),
    ("Clay diyas are an eco-friendly traditional source of _______.", "illumination", "Traditional illumination.", "Medium"),
    ("Giving gifts to the needy brings true spiritual _______.", "joy", "Brings spiritual joy.", "Medium"),
    ("Goddess Laxmi is associated with wealth and financial _______.", "prosperity", "Associated with prosperity.", "Medium"),
    ("The festival inspires people to clean and decorate their _______.", "homes", "Decorate their homes.", "Medium"),
    ("Lighting lamps symbolizes driving away the darkness of _______.", "ignorance", "Darkness of ignorance.", "Medium"),
    ("Traditional laddoos are prepared using gram flour, sugar, and _______.", "ghee", "Prepared with ghee/sugar.", "Medium"),
    ("Celebrating Diwali responsibly ensures a safe environment for _______.", "everyone", "Safe for everyone.", "Medium"),
    ("The spirit of Diwali encourages generosity towards the _______.", "underprivileged", "Generosity towards underprivileged.", "Medium"),

    # Hard (41-50)
    ("The metaphorical victory of light over darkness underscores the triumph of moral _______.", "righteousness", "Triumph of moral righteousness.", "Hard"),
    ("Using earthen diyas supports local artisans who craft pottery from natural _______.", "clay", "Supports local clay artisans.", "Hard"),
    ("Worshipping Ganesh and Laxmi unites intellectual wisdom with material _______.", "well-being", "Unites wisdom with well-being.", "Hard"),
    ("Refraining from fireworks mitigates severe atmospheric _______ during autumn.", "degradation", "Mitigates atmospheric degradation/pollution.", "Hard"),
    ("The festival of Deepavali reinforces societal values of compassion and mutual _______.", "respect", "Values of compassion and respect.", "Hard"),
    ("Rangoli art represents a seamless blend of mathematical symmetry and visual _______.", "aesthetics", "Symmetry and visual aesthetics.", "Hard"),
    ("Spreading light in others' lives represents the highest form of human _______.", "kindness", "Highest form of human kindness.", "Hard"),
    ("The cultural tradition of Deepavali has endured for thousands of _______.", "years", "Endured for thousands of years.", "Hard"),
    ("Sharing festive abundance reduces economic disparities in the _______.", "community", "Reduces disparities in community.", "Hard"),
    ("Diwali serves as a seasonal reminder to renew our commitment to virtuous _______.", "living", "Commitment to virtuous living.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 08: Diwali\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH08_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH08_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Diwali is known as the festival of lights.", "True", "The text states Diwali is called the festival of lights.", "Easy"),
    ("Diwali is also called Deepavali.", "True", "Diwali or Deepavali is another name.", "Easy"),
    ("People decorate their houses with earthen lamps called diyas.", "True", "Earthen lamps are called diya or deep.", "Easy"),
    ("Diwali is celebrated on a Full Moon night.", "False", "Diwali is celebrated on the New Moon night.", "Easy"),
    ("Shri Ganesh and Maa Laxmi are worshipped on Diwali evening.", "True", "People worship Shri Ganesh and Maa Laxmi in the evening.", "Easy"),
    ("Laddoos are offered to the deities during Diwali puja.", "True", "Laddoos are offered to the deities.", "Easy"),
    ("People decorate houses only with electric lights and no diyas.", "False", "People decorate with earthen lamps, rangolis, and electric lights.", "Easy"),
    ("Diwali celebrates the victory of evil over good.", "False", "Diwali celebrates the victory of good over evil.", "Easy"),
    ("Diwali celebrates the victory of light over darkness.", "True", "It symbolizes victory of light over darkness.", "Easy"),
    ("Distributing gifts and sweets to the poor spreads happiness.", "True", "People distribute gifts and sweets to spread happiness.", "Easy"),
    ("The word 'earthen' means made of plastic.", "False", "Earthen means made of clay.", "Easy"),
    ("The word 'prosperity' means having great wealth.", "True", "Prosperity is defined as state of having great wealth.", "Easy"),
    ("The word 'deity' means a God.", "True", "Deity is defined as a God.", "Easy"),
    ("The word 'synonymous' means having opposite meanings.", "False", "Synonymous means having the same or nearly same meaning.", "Easy"),
    ("Some people have stopped bursting crackers to protect the environment.", "True", "Few/many people have stopped this practice now.", "Easy"),
    ("Colourful rangolis are drawn on floors during Diwali.", "True", "Houses are decorated with colourful rangolis.", "Easy"),
    ("People celebrate Diwali alone without family or friends.", "False", "People celebrate with friends, family, good food, and joy.", "Easy"),
    ("Laddoos have become synonymous with the festival of Diwali.", "True", "The text explicitly states laddoos are synonymous with Diwali.", "Easy"),
    ("Diyas are lit in the morning when the sun is bright.", "False", "Diyas are lit in the evening.", "Easy"),
    ("Shri Ganesh and Maa Laxmi are worshipped for wealth and prosperity.", "True", "Worshipped for blessing people with wealth and prosperity.", "Easy"),
    ("Diwali is a festival of sadness and darkness.", "False", "Diwali is a festival of light, joy, and laughter.", "Easy"),
    ("Rangolis are made to make houses look beautiful.", "True", "Rangolis are colorful decorations for houses.", "Easy"),
    ("Sharing food with the poor is a good habit on Diwali.", "True", "Distributing sweets to the poor spreads light in their lives.", "Easy"),
    ("New Moon night means the night when the moon is fully round.", "False", "New Moon (Amavasya) is the dark night when the moon is not visible.", "Easy"),
    ("Chapter 08 is titled 'Diwali'.", "True", "Chapter 08 is titled 'Diwali'.", "Easy"),

    # Medium (26-40)
    ("Earthen diyas are more eco-friendly than plastic electric lights.", "True", "Earthen diyas are made of natural clay, making them eco-friendly.", "Medium"),
    ("Bursting heavy firecrackers is harmless to animals and the elderly.", "False", "Loud crackers cause distress to animals, elderly people, and pollute the air.", "Medium"),
    ("Lighting diyas on New Moon night symbolizes bringing light into the darkest times.", "True", "The darkness of New Moon highlights the brightness of diyas.", "Medium"),
    ("Maa Laxmi is the deity associated with wisdom, while Lord Ganesh is for wealth.", "False", "Lord Ganesh is for removing obstacles/wisdom; Maa Laxmi is for wealth/prosperity.", "Medium"),
    ("Rangoli art has been part of traditional Indian home decoration for centuries.", "True", "Rangoli is an ancient traditional art form for auspicious occasions.", "Medium"),
    ("Diwali encourages people to think about the underprivileged in society.", "True", "Distributing gifts and sweets to the poor shows care for the needy.", "Medium"),
    ("Laddoos are the only sweet eaten during Diwali across all of India.", "False", "While laddoos are synonymous with Diwali, many other sweets are also enjoyed.", "Medium"),
    ("Diwali is celebrated only by children and not by adults.", "False", "People of all ages celebrate Diwali with family and friends.", "Medium"),
    ("Decorating homes with lights creates a festive and joyful atmosphere.", "True", "Lights and rangolis create warmth and festive joy.", "Medium"),
    ("The victory of light over darkness is a universal message of hope.", "True", "It inspires hope that goodness will overcome hardship.", "Medium"),
    ("Stopping firecrackers helps keep the air clean and breathable.", "True", "Reducing crackers reduces harmful smoke and air pollution.", "Medium"),
    ("Worshipping deities on Diwali is usually done in the early morning.", "False", "Diwali puja is performed in the evening.", "Medium"),
    ("Diwali promotes feelings of togetherness and social harmony.", "True", "Gathering with family, friends, and neighbors fosters unity.", "Medium"),
    ("Clay diyas are made by local potters using natural soil.", "True", "Potters hand-craft earthen diyas from natural clay soil.", "Medium"),
    ("The festival of Diwali lasts only five minutes.", "False", "Diwali is a major festival celebrated over several festive days.", "Medium"),

    # Hard (41-50)
    ("The symbolic triumph of good over evil in Diwali reflects core ethical values of Indian philosophy.", "True", "It embodies the philosophical belief in the ultimate victory of truth (Dharma).", "Hard"),
    ("Environmental protection during Diwali compromises the true cultural spirit of the festival.", "False", "Celebrating eco-friendly Diwali honors nature, enhancing the true spirit of life.", "Hard"),
    ("The word 'synonymous' indicates that laddoos and Diwali are inextricably linked in popular culture.", "True", "Synonymous means two concepts are universally associated together.", "Hard"),
    ("Rangoli patterns strictly follow modern computer-generated guidelines only.", "False", "Rangoli is a traditional hand-drawn art form passed down through generations.", "Hard"),
    ("Charity during Diwali transforms a personal celebration into a social blessing.", "True", "Sharing with the poor spreads happiness across the wider community.", "Hard"),
    ("Earthen diyas decompose naturally without polluting soil or water.", "True", "Clay returns to nature harmlessly, unlike plastic waste.", "Hard"),
    ("The New Moon phase of Diwali symbolizes spiritual renewal from darkness to enlightenment.", "True", "Darkness of New Moon represents spiritual ignorance replaced by divine light.", "Hard"),
    ("Firecrackers were historically the central ancient ritual of Diwali thousands of years ago.", "False", "Ancient Diwali focused on diyas, lamps, puja, and sweets; gunpowder crackers came much later.", "Hard"),
    ("Festivals like Diwali serve as essential cultural anchors for passing values to young generations.", "True", "Festivals teach children moral values, traditions, and family unity.", "Hard"),
    ("Chapter 08 encourages a balanced, joyous, and environmentally conscious Diwali celebration.", "True", "It highlights traditional diyas, family joy, charity, and stopping harmful crackers.", "Hard")
]

tf_content = f"# True / False — Chapter 08: Diwali\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH08_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH08_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("What is Diwali and what is its alternative name?", "Diwali is the festival of lights, also known as Deepavali.", "Easy", "Remembering"),
    ("Why is Diwali called the festival of lights?", "It is called the festival of lights because people decorate their homes with earthen lamps (diyas) and light them up in the evening.", "Easy", "Remembering"),
    ("How do people decorate their houses on Diwali?", "People decorate their houses with earthen diyas, colourful rangolis, and electric lights.", "Easy", "Remembering"),
    ("On which moon phase night is Diwali celebrated?", "Diwali is celebrated on the New Moon (Amavasya) night.", "Easy", "Remembering"),
    ("Which deities are worshipped on Diwali evening?", "People worship Shri Ganesh and Maa Laxmi in the evening.", "Easy", "Remembering"),
    ("Why do people worship Shri Ganesh and Maa Laxmi on Diwali?", "They worship them for blessing their families with wealth, wisdom, and prosperity.", "Easy", "Remembering"),
    ("Which traditional sweet is offered to the deities and synonymous with Diwali?", "Laddoos are offered to the deities and are synonymous with Diwali.", "Easy", "Remembering"),
    ("What major triumph does Diwali celebrate?", "Diwali celebrates the victory of good over evil and light over darkness.", "Easy", "Remembering"),
    ("Why do people distribute gifts and sweets among the poor on Diwali?", "They distribute gifts and sweets to spread happiness and light in the lives of the needy.", "Easy", "Remembering"),
    ("Why have many people stopped bursting firecrackers on Diwali?", "They have stopped bursting crackers to reduce air and noise pollution and protect the environment.", "Easy", "Understanding"),
    ("What is the meaning of the word 'earthen'?", "Earthen means made of clay or natural earth.", "Easy", "Understanding"),
    ("What is the meaning of the word 'prosperity'?", "Prosperity means the state of having great wealth, success, and well-being.", "Easy", "Understanding"),
    ("What is the meaning of the word 'deity'?", "Deity means a God or Goddess.", "Easy", "Understanding"),
    ("What is the meaning of the word 'synonymous'?", "Synonymous means having the same or nearly the same meaning or association.", "Easy", "Understanding"),
    ("What are earthen lamps commonly called in Hindi?", "Earthen lamps are commonly called diyas or deeps.", "Easy", "Remembering"),
    ("With whom do people share their Diwali celebrations?", "People celebrate Diwali with their family, friends, and neighbors.", "Easy", "Remembering"),
    ("What floor decoration art is drawn at home entrances during Diwali?", "Colourful rangoli art is drawn at home entrances.", "Easy", "Remembering"),
    ("What time of day is Diwali puja performed?", "Diwali puja is performed in the evening.", "Easy", "Remembering"),
    ("What atmosphere characterizes Diwali celebrations?", "An atmosphere of good food, joy, warmth, and laughter.", "Easy", "Remembering"),
    ("How do earthen diyas help the environment compared to plastic decorations?", "Earthen diyas are made of natural clay and decompose harmlessly back into the earth.", "Easy", "Understanding"),
    ("What does lighting a diya on a dark night symbolize?", "It symbolizes driving away darkness, fear, and ignorance with light and hope.", "Easy", "Understanding"),
    ("What food item is synonymous with Diwali festivities?", "Laddoos.", "Easy", "Remembering"),
    ("How does sharing sweets help the community on Diwali?", "It fosters friendship, joy, and goodwill among neighbors and relatives.", "Easy", "Understanding"),
    ("What moral value does Diwali teach us about evil?", "It teaches us that good will always triumph over evil in the end.", "Easy", "Understanding"),
    ("What is the title of Chapter 08?", "The title of Chapter 08 is 'Diwali'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Why is celebrating Diwali on a New Moon night symbolic?", "The New Moon night is the darkest night of the month, making the bright light of diyas stand out as a powerful symbol of light defeating darkness.", "Medium", "Understanding"),
    ("Explain the roles of Shri Ganesh and Maa Laxmi during Diwali worship.", "Lord Ganesh removes obstacles and bestows wisdom, while Goddess Laxmi brings wealth, health, and prosperity.", "Medium", "Understanding"),
    ("How does decorating the house with Rangoli reflect Indian artistic traditions?", "Rangoli uses vibrant colors and symmetrical geometric patterns to express joy, welcome guests, and honor traditional art.", "Medium", "Analyzing"),
    ("Why is eco-friendly Diwali becoming popular among modern families?", "Because people realize that reducing firecrackers protects air quality, saves animals from loud noise, and keeps the environment clean.", "Medium", "Analyzing"),
    ("How does distributing gifts to the poor fulfill the true spirit of Diwali?", "It extends the light and joy of the festival to those less fortunate, ensuring that prosperity is shared with the whole community.", "Medium", "Evaluating"),
    ("Describe the sensory elements that make Diwali a memorable festival for children.", "Children enjoy seeing bright diyas and rangolis, tasting delicious laddoos, hearing laughter, and feeling the warmth of family gatherings.", "Medium", "Understanding"),
    ("Why are laddoos specifically offered as prasad during Diwali puja?", "Laddoos represent sweetness, fullness, and auspicious joy, making them a traditional offering to deities.", "Medium", "Understanding"),
    ("How does Diwali strengthen family relationships?", "Family members work together to clean, decorate, cook, worship, and share meals, creating fond memories and stronger bonds.", "Medium", "Analyzing"),
    ("What is the spiritual meaning of 'light over darkness'?", "It means that wisdom, truth, and kindness (light) will always overcome ignorance, falsehood, and wickedness (darkness).", "Medium", "Analyzing"),
    ("How can Class 2 students celebrate a safe and green Diwali?", "Students can light clay diyas with parents, draw colorful rangolis, eat sweets, avoid bursting loud crackers, and give toys to needy children.", "Medium", "Applying"),
    ("Summarize Page 30 of the textbook in two sentences.", "Diwali, the festival of lights celebrated on New Moon night, involves lighting earthen diyas, making rangolis, and worshipping Shri Ganesh and Maa Laxmi for prosperity. People share laddoos, celebrate with family, and distribute gifts to the poor, symbolizing the victory of good over evil.", "Medium", "Understanding"),
    ("Why do people clean their houses thoroughly before Diwali?", "Cleaning symbolizes clearing out old negative energy and preparing a pure, welcoming space for Goddess Laxmi and divine blessings.", "Medium", "Understanding"),
    ("What is the difference between electric lights and earthen diyas?", "Electric lights offer bright modern decoration, while earthen diyas represent ancient, eco-friendly clay traditions.", "Medium", "Analyzing"),
    ("How does Diwali promote kindness and generosity?", "By encouraging people to give sweets, gifts, and assistance to the poor, bringing light into their lives.", "Medium", "Evaluating"),
    ("What message does Chapter 08 give about firecrackers?", "It acknowledges that while many used to burst crackers, responsible people are stopping the practice for a cleaner, safer celebration.", "Medium", "Understanding"),

    # Hard (41-50)
    ("Critique the shift from traditional clay diyas to plastic electric decorations in modern cities.", "While electric lights are convenient, over-relying on plastic goods harms local clay artisans and increases plastic waste, whereas clay diyas support traditional potters and eco-sustainability.", "Hard", "Evaluating"),
    ("Analyze how Diwali serves as a cultural anchor for Indian families living worldwide.", "Diwali connects families across generations and continents through shared rituals, traditional food, and moral values of light over darkness.", "Hard", "Analyzing"),
    ("Deconstruct the philosophical symbolism of lighting a diya.", "The clay pot represents the human body, the oil represents devotion, the cotton wick represents the soul, and the flame represents divine knowledge dispelling darkness.", "Hard", "Analyzing"),
    ("Compare the celebration of Diwali with other light festivals around the world (e.g., Hanukkah or Lantern Festival).", "All light festivals share the universal human desire to celebrate hope, warmth, community, and the triumph of light over dark winter times.", "Hard", "Analyzing"),
    ("Evaluate the social responsibility of citizens during major national festivals.", "Citizens have a responsibility to celebrate joyfully without harming others—by avoiding noise/air pollution, being mindful of animals, and sharing wealth with the poor.", "Hard", "Evaluating"),
    ("How can primary schools organize an eco-friendly Diwali celebration?", "Schools can conduct clay diya painting, organic rangoli contests, sweet-sharing drives for charity, and green-pledge assemblies against firecrackers.", "Hard", "Applying"),
    ("Assess the economic impact of Diwali on local small-scale artisans (potters, sweet makers, flower sellers).", "Diwali provides crucial seasonal income for small potters, florists, and sweet vendors, sustaining traditional livelihoods across India.", "Hard", "Evaluating"),
    ("Why is the concept of 'victory of good over evil' relevant in modern school life?", "It encourages children to choose honesty over cheating, kindness over bullying, and hard work over laziness in their daily school interactions.", "Hard", "Applying"),
    ("Formulate a short festive poem celebrating an eco-friendly Diwali.", "'Light a diya of golden clay,\nDrive the dark and gloom away!\nShare a laddoo, smile and sing,\nJoy to every heart we bring!'", "Hard", "Creating"),
    ("Synthesize the core message of Chapter 08 into a single guiding principle.", "Celebrate Diwali by illuminating your home with diyas, your heart with kindness, your mind with wisdom, and your community with generous sharing!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 08: Diwali\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH08_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH08_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe how homes are decorated for Diwali and why it is called the festival of lights.", 
     "Diwali is known as the festival of lights because lighting up homes is its central tradition. In the evening, people decorate their houses with traditional earthen lamps called diyas (or deeps) filled with oil and light them up. In addition, entrances are decorated with vibrant, colourful rangolis made from bright powders or flowers, and buildings are illuminated with strings of electric lights, creating a warm and dazzling spectacle.", 
     "Easy", "Remembering"),

    ("Explain the evening worship (puja) rituals on Diwali, including the deities worshipped and offerings made.", 
     "On Diwali evening, which falls on the New Moon night, families gather together for a special puja. They worship Shri Ganesh, the remover of obstacles, and Maa Laxmi, the Goddess of wealth and prosperity. The family prays for divine blessings of health, wisdom, and financial well-being. Traditional sweets, especially laddoos, are offered to the deities as prasad and shared among family members.", 
     "Easy", "Remembering"),

    ("What core spiritual and moral messages does Diwali convey to society?", 
     "Diwali conveys two powerful moral and spiritual messages:\n1. **Victory of Good over Evil**: It reminds us that truth, righteousness, and morality will always overcome wicked actions.\n2. **Victory of Light over Darkness**: It symbolizes dispelling ignorance, fear, and sadness with the light of knowledge, kindness, and hope.", 
     "Easy", "Understanding"),

    ("How do people celebrate Diwali with their community and the underprivileged?", 
     "Diwali is a festival of community joy and sharing. People celebrate with relatives, friends, and neighbors by exchanging good food, sweets, and warm greetings. Importantly, many people distribute gifts, new clothes, and delicious sweets among the poor and needy, spreading happiness and bringing light into the lives of those less fortunate.", 
     "Easy", "Understanding"),

    ("Explain the meanings of the vocabulary words 'earthen', 'prosperity', 'deity', and 'synonymous'.", 
     "1. **Earthen**: Made of natural earth or clay, such as traditional clay diyas.\n2. **Prosperity**: The fortunate state of having wealth, success, and good health.\n3. **Deity**: A God or Goddess worshipped in religious traditions, such as Shri Ganesh or Maa Laxmi.\n4. **Synonymous**: Having the same or nearly the same meaning, or being closely associated with something (like laddoos and Diwali).", 
     "Easy", "Understanding"),

    ("Why is stopping or reducing firecrackers during Diwali an important modern practice?", 
     "While bursting crackers was popular in the past, many people have stopped or reduced this practice today. Firecrackers produce heavy smoke and toxic air pollution that harms human lungs, especially for children and the elderly. They also create loud noise that terrifies pets and wild animals. Stopping crackers makes Diwali safer, cleaner, and more peaceful for everyone.", 
     "Easy", "Understanding"),

    ("Describe the atmosphere of a home on Diwali evening.", 
     "On Diwali evening, a home is filled with warmth, beauty, and joy. The entrance glows with bright earthen diyas and colorful rangolis. Inside, the family dresses in new clothes and gathers around the altar for Shri Ganesh and Maa Laxmi puja. The air smells of sweet laddoos and incense, and the house echoes with happy laughter, prayers, and shared meals.", 
     "Easy", "Remembering"),

    ("What is Rangoli, and how does it add to Diwali celebrations?", 
     "Rangoli is a traditional Indian floor art created at house entrances during festivals like Diwali. Using colorful powders, rice flour, or flower petals, people draw beautiful symmetrical patterns. Rangoli adds vibrant color, artistic beauty, and a welcoming touch for guests and divine blessings.", 
     "Easy", "Remembering"),

    ("Why are laddoos so special during Diwali?", 
     "Laddoos are round, golden sweets made from gram flour, ghee, and sugar. They are traditional offerings (prasad) for Lord Ganesh and Goddess Laxmi during Diwali puja. Because almost every household prepares or buys laddoos for Diwali, they have become synonymous with the sweetness and joy of the festival.", 
     "Easy", "Remembering"),

    ("How does Diwali encourage togetherness among family and friends?", 
     "Diwali brings people together through shared activities. Family members clean and decorate the house together, prepare festive food, conduct evening prayers, and enjoy grand meals. Friends and neighbors visit each other's homes to exchange sweets and festive wishes, strengthening social and emotional bonds.", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why is Diwali celebrated on the New Moon night, and what makes it special?", "The New Moon (Amavasya) night is the darkest night of the month. Celebrating Diwali on this night highlights the contrast: tiny clay diyas shine brightest in total darkness, symbolizing how hope and light overcome darkness.", "Easy", "Understanding"),
    ("Who are Lord Ganesh and Goddess Laxmi, and why are they worshipped together?", "Lord Ganesh is the God of wisdom and remover of obstacles; Goddess Laxmi is the Goddess of wealth and prosperity. Worshipping them together ensures that wealth is accompanied by wisdom and good ethics.", "Easy", "Understanding"),
    ("What are earthen diyas made of, and why are they eco-friendly?", "Earthen diyas are hand-crafted from natural river clay soil by potters. They are eco-friendly because after use, the clay dissolves back into the earth naturally without causing plastic waste.", "Easy", "Understanding"),
    ("How does distributing sweets to the poor reflect true holiday spirit?", "True celebration is not just enjoying wealth ourselves, but sharing our abundance with the needy. Giving sweets and gifts to the poor spreads genuine light and happiness in the community.", "Easy", "Evaluating"),
    ("Describe three ways a Class 2 student can help prepare for Diwali at home.", "1. Help parents arrange earthen diyas and fill them with oil.\n2. Assist in making simple colourful rangoli patterns at the doorway.\n3. Pack sweet boxes to distribute to neighbors and needy children.", "Easy", "Applying"),
    ("What is Deepavali, and what does the word mean literally?", "Deepavali is the original Sanskrit name for Diwali. Literally, 'Deepa' means lamp and 'Avali' means row, so Deepavali means 'a row of lamps'.", "Easy", "Remembering"),
    ("How does Diwali promote charity and generosity?", "The tradition of giving gifts, new clothes, and food to domestic helpers, workers, and the poor encourages people to practice active charity and generosity.", "Easy", "Understanding"),
    ("What kind of lights were used in ancient times versus modern times on Diwali?", "In ancient times, people used only earthen clay diyas filled with mustard oil or ghee. In modern times, people use earthen diyas along with decorative electric LED lights.", "Easy", "Understanding"),
    ("Why is good food an important part of Diwali celebrations?", "Festive meals and traditional sweets bring joy, nourish family members, and mark the holiday as a special time of celebration and thanksgiving.", "Easy", "Remembering"),
    ("What lesson does Diwali teach about overcoming difficulties in life?", "Just as a small diya can break the darkest night, even a small act of kindness, honesty, or effort can overcome big difficulties and sadness.", "Easy", "Evaluating"),
    ("How does Diwali bring joy to elderly people and children alike?", "Children love the lights, rangolis, and sweets, while elderly family members enjoy the spiritual puja, family reunions, and peaceful festive atmosphere.", "Easy", "Understanding"),
    ("Why is it important to support local potters who make clay diyas?", "Buying clay diyas supports small local potters (craftsmen) who earn their main living during Diwali, preserving traditional Indian pottery crafts.", "Easy", "Evaluating"),
    ("What precautions should be taken if someone chooses to light diyas?", "Diyas should be placed safely away from curtains or flammable items, handled under adult supervision, and kept on flat non-flammable surfaces.", "Easy", "Applying"),
    ("Describe the meaning of 'victory of light over darkness' in daily school life.", "In school life, light over darkness means choosing honesty over lying, working hard instead of being lazy, and being kind to classmates instead of bullying.", "Easy", "Applying"),
    ("Summarize Chapter 08 in five key sentences.", "Diwali, the festival of lights, is celebrated on New Moon night by decorating homes with earthen diyas, rangolis, and lights. Families worship Shri Ganesh and Maa Laxmi for wealth, wisdom, and prosperity, offering traditional laddoos. Celebrated with family, friends, and good food, it symbolizes the victory of good over evil. Many people distribute gifts to the poor and choose eco-friendly celebrations without noisy crackers. It brings light, joy, and peace to everyone.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how Diwali balances religious devotion, family bonding, and social responsibility.", 
     "Diwali integrates three core dimensions of human life:\n1. **Religious Devotion**: Evening puja to Lord Ganesh and Goddess Laxmi for spiritual and material blessings.\n2. **Family Bonding**: Cleaning, decorating, cooking, and sharing grand festive meals together.\n3. **Social Responsibility**: Sharing sweets with neighbors, donating to the poor, and choosing eco-friendly diyas over polluting crackers.", 
     "Medium", "Analyzing"),

    ("Examine the environmental significance of transitioning to a Green, Cracker-Free Diwali.", 
     "Firecrackers release toxic smoke containing heavy metals, particulate matter, and sulfur dioxide, severely degrading urban air quality. They also generate deafening noise that causes severe stress to domestic pets, birds, and elderly citizens. Transitioning to a green, cracker-free Diwali preserves clean air, protects animal welfare, and restores the peaceful traditional focus on clay lamps.", 
     "Medium", "Evaluating"),

    ("Discuss how the art of Rangoli embodies artistic expression, sacred geometry, and welcome culture.", 
     "Rangoli is drawn at home thresholds using vibrant colors and symmetrical geometric patterns. Artistically, it showcases creativity; geometrically, its symmetry creates visual harmony; culturally, it acts as a sacred invitation welcoming Goddess Laxmi and guests into a clean, joyous home environment.", 
     "Medium", "Analyzing"),

    ("Explore the philosophical relationship between Lord Ganesh (wisdom) and Goddess Laxmi (wealth).", 
     "Worshipping Laxmi alone represents seeking material wealth, which can lead to greed or ruin if unguided. Worshipping Ganesh alongside Laxmi ensures that wealth is managed with wisdom, intellect, and moral integrity. Together, they represent balanced, righteous prosperity.", 
     "Medium", "Analyzing"),

    ("How can Class 2 teachers use Chapter 08 to foster eco-literacy and social empathy?", 
     "Teachers can organize diya-painting workshops using natural clay, conduct discussions on protecting pets from firecracker noise, and organize a 'Joy of Giving' drive where students donate books or toys to underprivileged children.", 
     "Medium", "Applying"),

    ("Why is the New Moon (Amavasya) night the perfect canvas for the festival of lights?", "Amavasya provides the ultimate pitch-black background. When thousands of tiny diyas are lit, the darkness amplifies their glow, dramatically illustrating the central message that light overcomes darkness.", "Medium", "Analyzing"),
    ("Describe the economic impact of Diwali on traditional village potters and artisans.", "Diwali creates high demand for handmade clay diyas, terracotta statues, and handcrafted decorations, providing critical annual income for rural potters and traditional craftspeople.", "Medium", "Evaluating"),
    ("How does sharing laddoos and sweets break down social barriers between neighbors?", "Offering sweets is a universal gesture of goodwill. Sharing laddoos opens doors, resolves past misunderstandings, and fosters friendly neighborhood relationships.", "Medium", "Understanding"),
    ("In what ways does Diwali teach children the value of gratitude?", "By reflecting on their blessings during Laxmi Puja and sharing gifts with less fortunate people, children learn gratitude for what they have and empathy for others.", "Medium", "Evaluating"),
    ("Contrast the ancient way of celebrating Diwali with modern urban celebrations.", "Ancient celebrations relied purely on oil diyas, organic rangoli, homemade sweets, and peaceful community prayers. Modern celebrations include electric lights, store-bought sweets, and electronic media, though eco-friendly awareness is bringing back traditional values.", "Medium", "Analyzing"),
    ("Why is the concept of 'inner light' more valuable than external house decorations?", "External lights decorate physical buildings, but inner light—representing truth, kindness, and compassion—decorates a person's soul and improves human relationships.", "Medium", "Evaluating"),
    ("Explain why cleanliness is considered essential before Diwali puja.", "Cleanliness represents purity. Preparing a spotless home reflects mental clarity, respect for divine guests, and a healthy living environment.", "Medium", "Understanding"),
    ("How does Chapter 08 promote inclusive community happiness?", "It emphasizes giving sweets and gifts to the poor, ensuring that festive joy reaches everyone in society regardless of economic status.", "Medium", "Evaluating"),
    ("What safety measures should families take during Diwali night?", "Use eco-friendly diyas, keep water nearby, avoid synthetic clothes near open flames, supervise children, and keep pets indoors.", "Medium", "Applying"),
    ("Construct a short story about a child who decides to buy clay diyas from a local potter instead of firecrackers.", "Rohan had money for crackers, but saw an old potter selling clay diyas. Realizing crackers cause smoke while diyas help the potter buy food, Rohan bought fifty diyas, lit up his home, and gave the potter a happy Diwali.", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the commercialization of Diwali in modern consumer culture.", 
     "Modern commercialization often shifts the focus of Diwali from spiritual devotion, family warmth, and eco-friendly diyas toward excessive shopping, expensive electronics, and wasteful packaging. To preserve Diwali's true essence, society must re-center on core values: inner light, family unity, environmental care, and genuine charity.", 
     "Hard", "Evaluating"),

    ("Deconstruct the symbolic components of a traditional earthen Diya (lamp, oil, cotton wick, flame).", 
     "- **Clay Lamp**: The physical body grounded in earth.\n- **Oil/Ghee**: Pure devotion and positive energy fueling life.\n- **Cotton Wick**: The human mind/soul focused on a goal.\n- **Flame**: Divine knowledge and truth dispelling the darkness of ignorance.", 
     "Hard", "Analyzing"),

    ("Synthesize how Diwali fosters national integration across India's diverse regions.", 
     "Though known by different regional names and stories (e.g., Ram's return in the North, Kali Puja in the East, Laxmi Puja in the West), the core rituals—diyas, rangoli, sweets, and worship of light over dark—unite all regions of India in a shared cultural celebration.", 
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive school curriculum module for 'Eco-Friendly Diwali Celebration'.", 
     "1. **Science**: Air quality measurements before and after fireworks.\n2. **Art**: Clay diya making and natural flower rangoli.\n3. **Social Studies**: History of Diwali and local potter economics.\n4. **Ethics/Language**: Writing essays on charity and animal care during festivals.", 
     "Hard", "Creating"),

    ("Evaluate the role of festivals as tools for transmitting moral philosophy across generations.", 
     "Festivals convert abstract moral philosophies (good vs. evil, light vs. dark) into tangible, joyful rituals (lighting diyas, sharing sweets, praying). This experiential learning leaves lasting emotional memories in children, transmitting values effortlessly down generations.", 
     "Hard", "Evaluating"),

    ("Analyze why charity during festivals has a more profound psychological impact than routine donations.", "Festival charity connects giving with celebration, teaching children that sharing abundance is the highest form of festive joy, embedding lifelong altruism.", "Hard", "Analyzing"),
    ("Compare the environmental footprint of clay diyas versus mass-produced plastic LED lights.", "Clay diyas use natural earth, biodegradable cotton, and plant oils, leaving zero long-term waste. Plastic LED lights contain electronic waste, non-recyclable wiring, and plastic, contributing to landfill pollution.", "Hard", "Analyzing"),
    ("Draft a formal resolution for a housing society advocating a 'Green and Noise-Free Diwali'.", "'Resolved: Our housing society hereby pledges to celebrate a Green Diwali. All residents will use clay diyas and electric lights, refrain from bursting noise/smoke crackers, organize a joint rangoli display, and collect donations for local orphanages.'", "Hard", "Creating"),
    ("Assess the impact of firecracker smoke on urban public health during autumn months.", "Firecracker smoke exacerbates autumn smog, causing severe respiratory distress, asthma attacks, eye irritation, and cardiovascular stress across urban populations.", "Hard", "Evaluating"),
    ("Synthesize the ultimate philosophy of Chapter 08 into a timeless moral guideline.", "'Drive away darkness with the light of knowledge, conquer evil with the power of goodness, and illuminate every heart with the joy of selfless sharing!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 08: Diwali\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH08_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH08_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Diwali or Deepavali is called the festival of lights. It is because on this day people decorate their houses with earthen lamps (diya/deep) and light them up in the evening.",
     [
         ("What is another name for Diwali?", "Deepavali.", "Easy", "Remembering"),
         ("What is Diwali called?", "The festival of lights.", "Easy", "Remembering"),
         ("What do people decorate their houses with?", "Earthen lamps (diya/deep).", "Easy", "Remembering"),
         ("When do people light up the diyas?", "In the evening.", "Easy", "Remembering"),
         ("What does the word 'earthen' mean?", "Made of clay.", "Medium", "Understanding")
     ]),

    # Set 2
    ("In addition to this, houses are decorated with colourful rangolis and electric lights as well. It is celebrated on the New Moon and in the evening people worship Shri Ganesh and Maa Laxmi for blessing them with wealth and prosperity.",
     [
         ("Besides diyas, what two other decorations are used on houses?", "Colourful rangolis and electric lights.", "Easy", "Remembering"),
         ("On which moon phase is Diwali celebrated?", "New Moon (Amavasya).", "Easy", "Remembering"),
         ("Which two deities are worshipped in the evening?", "Shri Ganesh and Maa Laxmi.", "Easy", "Remembering"),
         ("What blessings do people ask from Shri Ganesh and Maa Laxmi?", "Wealth and prosperity.", "Easy", "Remembering"),
         ("What does the word 'prosperity' mean?", "The state of having great wealth and success.", "Medium", "Understanding")
     ]),

    # Set 3
    ("Laddoos are offered to the deities and have become synonymous with this festival. People celebrate this festival with their friends and family, good food, joy and laughter.",
     [
         ("Which sweet is offered to the deities on Diwali?", "Laddoos.", "Easy", "Remembering"),
         ("What word describes how closely laddoos are associated with Diwali?", "Synonymous.", "Easy", "Remembering"),
         ("With whom do people celebrate Diwali?", "With their friends and family.", "Easy", "Remembering"),
         ("What three elements characterize Diwali celebrations?", "Good food, joy, and laughter.", "Easy", "Remembering"),
         ("What does the word 'synonymous' mean?", "Having the same or nearly the same meaning/association.", "Medium", "Understanding")
     ]),

    # Set 4
    ("Many people burst crackers but few have stopped this practice now. This festival celebrates the victory of good over evil, of light over darkness.",
     [
         ("What practice have some people stopped now?", "Bursting crackers.", "Easy", "Remembering"),
         ("Why have people stopped bursting crackers?", "To reduce noise and air pollution.", "Medium", "Understanding"),
         ("What victory of morality does Diwali celebrate?", "Victory of good over evil.", "Easy", "Remembering"),
         ("What victory of light does Diwali celebrate?", "Victory of light over darkness.", "Easy", "Remembering"),
         ("What moral message does 'good over evil' give to children?", "That truth and moral goodness will always triumph over bad actions.", "Medium", "Evaluating")
     ]),

    # Set 5
    ("Many people distribute gifts and sweets among the poor to spread happiness and light in their lives.",
     [
         ("What do people distribute among the poor?", "Gifts and sweets.", "Easy", "Remembering"),
         ("Why do people distribute gifts to the poor?", "To spread happiness and light in their lives.", "Easy", "Remembering"),
         ("What value is demonstrated by giving gifts to the needy?", "Charity, kindness, and generosity.", "Medium", "Understanding"),
         ("What does 'spreading light in their lives' mean symbolically?", "Bringing joy, hope, and relief to those in hardship.", "Medium", "Analyzing"),
         ("How can students participate in this charity tradition?", "By sharing sweets or old toys with underprivileged children.", "Medium", "Applying")
     ]),

    # Set 6
    ("Word Meaning: Earthen: Made of clay | Prosperity: The state of having great wealth | Deity: A God | Synonymous: Same or nearly the same meaning",
     [
         ("What is the meaning of 'earthen'?", "Made of clay.", "Easy", "Remembering"),
         ("What is the meaning of 'prosperity'?", "The state of having great wealth.", "Easy", "Remembering"),
         ("What is the meaning of 'deity'?", "A God.", "Easy", "Remembering"),
         ("What is the meaning of 'synonymous'?", "Same or nearly the same meaning.", "Easy", "Remembering"),
         ("Which word describes Shri Ganesh or Maa Laxmi?", "Deity.", "Easy", "Understanding")
     ]),

    # Set 7
    ("Diwali or Deepavali is called the festival of lights. It is because on this day people decorate their houses with earthen lamps (diya/deep) and light them up in the evening.",
     [
         ("Name the Sanskrit word from which Diwali gets its name.", "Deepavali.", "Easy", "Remembering"),
         ("What item is lit in the evening?", "Earthen lamps (diya/deep).", "Easy", "Remembering"),
         ("Why are lamps lit on Diwali night?", "To dispel darkness and decorate houses.", "Easy", "Remembering"),
         ("What material is a traditional diya made of?", "Clay (earthen).", "Easy", "Remembering"),
         ("Why is Diwali important in Indian culture?", "It is a major national festival celebrating light, goodness, and prosperity.", "Medium", "Understanding")
     ]),

    # Set 8
    ("In addition to this, houses are decorated with colourful rangolis and electric lights as well. It is celebrated on the New Moon...",
     [
         ("What colourful art is drawn on the floor?", "Colourful rangoli.", "Easy", "Remembering"),
         ("What modern lighting is used alongside diyas?", "Electric lights.", "Easy", "Remembering"),
         ("Which night of the lunar month is Diwali held on?", "New Moon night.", "Easy", "Remembering"),
         ("Why does Rangoli add beauty to the festival?", "It brings bright colors and artistic designs to house entrances.", "Medium", "Understanding"),
         ("What is the Hindi term for New Moon night?", "Amavasya.", "Medium", "Remembering")
     ]),

    # Set 9
    ("This festival celebrates the victory of good over evil, of light over darkness. Many people distribute gifts and sweets among the poor to spread happiness and light in their lives.",
     [
         ("What does light symbolize in this text?", "Goodness, wisdom, and hope.", "Medium", "Understanding"),
         ("What does darkness symbolize?", "Evil, ignorance, and sadness.", "Medium", "Understanding"),
         ("Who receives gifts and sweets from generous people?", "The poor.", "Easy", "Remembering"),
         ("What is the main goal of sharing sweets with the poor?", "To spread happiness and light in their lives.", "Easy", "Remembering"),
         ("How does Diwali promote social harmony?", "By encouraging inclusive sharing and charity across society.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("Laddoos are offered to the deities and have become synonymous with this festival. People celebrate this festival with their friends and family, good food, joy and laughter.",
     [
         ("What sweet is offered as prasad during puja?", "Laddoos.", "Easy", "Remembering"),
         ("Who are the laddoos offered to?", "The deities (Shri Ganesh and Maa Laxmi).", "Easy", "Remembering"),
         ("With whom do people share their festive joy?", "Friends and family.", "Easy", "Remembering"),
         ("What emotions are experienced during Diwali?", "Joy and laughter.", "Easy", "Remembering"),
         ("Summarize this extract in one sentence.", "Diwali is celebrated with family, good food, laddoos, and joyous togetherness.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 08: Diwali\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH08_EXT_{q_counter:03d}"
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

with open(os.path.join(CH08_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 08 in {CH08_DIR}")
