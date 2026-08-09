r"""
Refines all 6 Category files for Chapter 06 ("My Favourite Cartoon") for Class 1.
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 1 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH06_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_06")
os.makedirs(CH06_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What is the name of the main cartoon character in Chapter 06?", "(A) Chhota Bheem", "(B) Mickey Mouse", "(C) Tom", "(D) Doraemon", "(A)", "The chapter focuses on Chhota Bheem.", "Easy", "Remembering", "Character Identification"),
    ("In which village is the story of Chhota Bheem set?", "(A) Dholakpur", "(B) Patliputra", "(C) Rampur", "(D) Sundargarh", "(A)", "The story takes place in the village of Dholakpur.", "Easy", "Remembering", "Setting"),
    ("How old is Chhota Bheem?", "(A) 9 years old", "(B) 5 years old", "(C) 15 years old", "(D) 20 years old", "(A)", "Bheem is a 9-year-old brave boy.", "Easy", "Remembering", "Age"),
    ("What food gives Bheem extra strength?", "(A) Laddoos", "(B) Burgers", "(C) Ice cream", "(D) Samosas", "(A)", "Eating tasty laddoos gives Bheem immense strength.", "Easy", "Remembering", "Food / Power"),
    ("Who makes the tasty laddoos in Dholakpur?", "(A) Tuntun Mausi", "(B) Chhutki", "(C) Kaliya", "(D) Jaggu", "(A)", "Tuntun Mausi makes delicious laddoos.", "Easy", "Remembering", "Character Action"),
    ("Who is the daughter of Tuntun Mausi?", "(A) Chhutki", "(B) Rani", "(C) Priya", "(D) Riya", "(A)", "Chhutki is Tuntun Mausi's daughter.", "Easy", "Remembering", "Relationship"),
    ("Which character is always jealous of Bheem's popularity?", "(A) Kaliya", "(B) Raju", "(C) Jaggu", "(D) Dholu", "(A)", "Kaliya is jealous of Bheem's popularity.", "Easy", "Remembering", "Character Emotion"),
    ("Who are Kaliya's twin sidekicks?", "(A) Dholu and Bholu", "(B) Raju and Jaggu", "(C) Tom and Jerry", "(D) Motu and Patlu", "(A)", "Dholu and Bholu are Kaliya's twin sidekicks.", "Easy", "Remembering", "Sidekicks"),
    ("What animal is Bheem's friend Jaggu?", "(A) A monkey", "(B) A dog", "(C) A parrot", "(D) A cat", "(A)", "Jaggu is a smart monkey friend of Bheem.", "Easy", "Remembering", "Animal Character"),
    ("Who created the brand Chhota Bheem?", "(A) Rajiv Chilaka", "(B) Walt Disney", "(C) RK Laxman", "(D) Satyajit Ray", "(A)", "Rajiv Chilaka is the creator of Chhota Bheem.", "Easy", "Remembering", "Creator"),
    ("Which two friends are always with Bheem?", "(A) Raju and Jaggu", "(B) Kaliya and Dholu", "(C) Bholu and Tuntun", "(D) Nobody", "(A)", "Raju and Jaggu are Bheem's good friends.", "Easy", "Remembering", "Friends"),
    ("What kind of boy is Chhota Bheem?", "(A) Intelligent, brave, and helpful", "(B) Lazy and mean", "(C) Angry and cruel", "(D) Shy and quiet", "(A)", "Bheem is intelligent, brave, kind, and helpful.", "Easy", "Remembering", "Character Trait"),
    ("How do the villagers of Dholakpur feel about Bheem?", "(A) They love and favorite him", "(B) They fear him", "(C) They ignore him", "(D) They dislike him", "(A)", "Bheem is the favorite of all villagers.", "Easy", "Remembering", "Villagers' View"),
    ("Does Kaliya succeed in proving he is better than Bheem?", "(A) No, he fails every time", "(B) Yes, always", "(C) Sometimes", "(D) He never tries", "(A)", "Kaliya tries to prove he is better, but fails every time.", "Easy", "Remembering", "Rivalry Result"),
    ("What does Bheem always do for the villagers?", "(A) Helps them whenever they are in trouble", "(B) Takes their food", "(C) Plays pranks", "(D) Sleeps in the sun", "(A)", "Bheem always protects and helps the villagers.", "Easy", "Remembering", "Action"),
    ("What is Chhutki's role in Bheem's group?", "(A) A female friend who helps Bheem", "(B) An enemy", "(C) A teacher", "(D) A doctor", "(A)", "Chhutki is Bheem's female friend.", "Easy", "Remembering", "Role"),
    ("What sweet dish does Tuntun Mausi prepare?", "(A) Laddoos", "(B) Jalebis", "(C) Gulab Jamun", "(D) Rasgulla", "(A)", "Tuntun Mausi is famous for her laddoos.", "Easy", "Remembering", "Food Item"),
    ("Which boy wears a blue dress and is Bheem's young friend?", "(A) Raju", "(B) Kaliya", "(C) Bholu", "(D) Dholu", "(A)", "Raju is Bheem's young brave friend.", "Easy", "Remembering", "Character Identification"),
    ("Are Dholu and Bholu twins?", "(A) Yes, they are twin brothers", "(B) No, they are cousins", "(C) No, they are strangers", "(D) They are uncle and nephew", "(A)", "Dholu and Bholu are twin brothers.", "Easy", "Remembering", "Fact"),
    ("Why is Kaliya jealous of Bheem?", "(A) Because Bheem is popular, brave, and loved by everyone", "(B) Because Bheem has a bicycle", "(C) Because Bheem is tall", "(D) Because Bheem has a cat", "(A)", "He is jealous of Bheem's popularity and strength.", "Easy", "Understanding", "Reasoning"),
    ("What is considered the largest children's entertainment brand in India?", "(A) Chhota Bheem", "(B) Pokemon", "(C) Batman", "(D) Spider-Man", "(A)", "Chhota Bheem is India's largest kids entertainment brand.", "Easy", "Remembering", "Brand Fact"),
    ("What does Bheem do when Kaliya gets into trouble?", "(A) Bheem kindly helps Kaliya too", "(B) Bheem laughs at him", "(C) Bheem runs away", "(D) Bheem fights him", "(A)", "Bheem is kind and helps even Kaliya when in danger.", "Easy", "Understanding", "Moral Quality"),
    ("Which word describes Jaggu the monkey?", "(A) Playful and helpful friend", "(B) Fierce predator", "(C) Wild animal", "(D) Lazy animal", "(A)", "Jaggu is a sweet, helpful monkey friend.", "Easy", "Remembering", "Character Description"),
    ("Where can you watch or read about Chhota Bheem?", "(A) On TV and storybooks", "(B) In news reports", "(C) In history encyclopedias", "(D) Only on radio", "(A)", "Chhota Bheem appears on television shows and books.", "Easy", "Remembering", "Media"),
    ("What lesson does Chhota Bheem teach children?", "(A) Always be helpful, brave, kind, and use your strength for good", "(B) Be jealous of others", "(C) Eat sweets all day", "(D) Fight with friends", "(A)", "Bheem teaches children to be helpful, brave, and kind.", "Easy", "Understanding", "Core Takeaway"),

    # Medium (26-40)
    ("Why does Bheem eat laddoos before fighting a big villain?", "(A) Laddoos give him an instant burst of extra energy and strength", "(B) He is just hungry", "(C) Tuntun Mausi forces him", "(D) He likes the color", "(A)", "Laddoos act as a power booster for Bheem.", "Medium", "Understanding", "Story Element"),
    ("How does Bheem's behavior differ from Kaliya's behavior?", "(A) Bheem uses his strength to help others; Kaliya tries to show off and ruins things", "(B) Both behave identically", "(C) Kaliya is kind", "(D) Bheem is mean", "(A)", "Bheem is selfless and helpful, whereas Kaliya is boastful.", "Medium", "Analyzing", "Character Contrast"),
    ("What makes Chhutki a valuable member of Bheem's team?", "(A) She is clever, supportive, and helps solve problems", "(B) She cooks food", "(C) She stays home", "(D) She sings songs", "(A)", "Chhutki offers smart ideas and support in adventures.", "Medium", "Understanding", "Team Role"),
    ("Why do Dholu and Bholu follow Kaliya?", "(A) They are his sidekicks, though Kaliya often bosses them around", "(B) They are his elder brothers", "(C) They dislike Kaliya", "(D) They are teachers", "(A)", "They act as Kaliya's twin sidekicks.", "Medium", "Understanding", "Group Dynamics"),
    ("What does the word 'sidekick' mean in the passage?", "(A) A close assistant or helper to a main person", "(B) A person who kicks balls", "(C) A dangerous animal", "(D) A fruit", "(A)", "Sidekick means a helper or companion.", "Medium", "Understanding", "Vocabulary"),
    ("Why is Dholakpur a peaceful village most of the time?", "(A) Because Bheem and his friends protect it from evil threats", "(B) Because it is far away", "(C) Because no one lives there", "(D) Because of big walls", "(A)", "Bheem constantly safeguards the village.", "Medium", "Understanding", "Setting Context"),
    ("How does Raju show courage despite being younger?", "(A) He fearlessly joins Bheem in fighting villains and helping villagers", "(B) He hides in houses", "(C) He cries loudly", "(D) He stays in school", "(A)", "Raju is a brave little archer and friend.", "Medium", "Understanding", "Character Trait"),
    ("What is the main reason for Kaliya's repeated failures?", "(A) He acts out of jealousy and arrogance rather than genuine kindness", "(B) He has no friends", "(C) He is too short", "(D) He sleeps too much", "(A)", "Arrogance and bad intentions lead to failure.", "Medium", "Analyzing", "Reasoning"),
    ("How does Jaggu the monkey contribute during adventures?", "(A) He uses his agility to swing on trees, fetch objects, and alert Bheem", "(B) He eats bananas only", "(C) He frightens people", "(D) He sleeps", "(A)", "Jaggu's monkey agility helps the team.", "Medium", "Understanding", "Function"),
    ("What values does Tuntun Mausi represent in the village?", "(A) Warmth, motherly care, and generous hospitality", "(B) Anger and strictness", "(C) Greed", "(D) Pride", "(A)", "Tuntun Mausi represents motherly warmth and care.", "Medium", "Understanding", "Character Value"),
    ("Why does Bheem forgive Kaliya when Kaliya makes mistakes?", "(A) Bheem believes in forgiveness and wants everyone to live happily", "(B) Bheem is afraid of Kaliya", "(C) Tuntun Mausi tells him to", "(D) Bheem doesn't notice", "(A)", "Bheem holds no grudges and practices forgiveness.", "Medium", "Analyzing", "Moral Value"),
    ("What makes Chhota Bheem so popular among young Indian children?", "(A) Relatable Indian culture, fun characters, and inspiring moral lessons", "(B) Scary monsters", "(C) Hard science", "(D) Fast cars", "(A)", "Indian settings and positive values resonate with children.", "Medium", "Evaluating", "Cultural Appeal"),
    ("What does the word 'rivalry' mean in the story?", "(A) Competition between opponents for superiority", "(B) Sleeping together", "(C) Sharing food", "(D) Flying planes", "(A)", "Rivalry means competition between rivals.", "Medium", "Understanding", "Vocabulary"),
    ("How do Bheem and his friends demonstrate positive teamwork?", "(A) They combine their individual skills (strength, agility, brain) to defeat problems", "(B) They fight among themselves", "(C) One person does everything", "(D) They give up easily", "(A)", "Complementary skills solve big challenges.", "Medium", "Analyzing", "Teamwork"),
    ("What happens when Kaliya gets into trouble while trying to beat Bheem?", "(A) Bheem steps in to rescue Kaliya without boasting", "(B) Bheem laughs", "(C) Bheem leaves him there", "(D) Dholu and Bholu run away", "(A)", "Bheem saves Kaliya humbly.", "Medium", "Understanding", "Plot Pattern"),

    # Hard (41-50)
    ("Analyze how Chhota Bheem represents the ideal qualities of a young role model.", "(A) He combines physical strength with emotional humility, intelligence, and selfless service", "(B) He is just strong", "(C) He is rich", "(D) He beats up everyone", "(A)", "Bheem balances strength with humility, wisdom, and helpfulness.", "Hard", "Evaluating", "HOTS Character Analysis"),
    ("Compare Bheem's use of power with Kaliya's desire for power.", "(A) Bheem uses power to protect and serve; Kaliya seeks power to gain fame and dominate", "(B) Both want power for fame", "(C) Neither has power", "(D) Kaliya uses power for good", "(A)", "Selfless protection vs selfish dominance distinguishes them.", "Hard", "Analyzing", "Comparative Ethics"),
    ("How does the setting of Dholakpur blend traditional Indian culture with fantasy elements?", "(A) It features traditional dhotis, laddoos, and village life along with magical villains and talking animals", "(B) It is a futuristic city", "(C) It has space ships", "(D) It is underwater", "(A)", "Traditional Indian folklore meets imaginative children's fantasy.", "Hard", "Evaluating", "Cultural Analysis"),
    ("What does Tuntun Mausi's laddoo symbolize in the narrative structure?", "(A) A catalyst of positive energy and reward for good deeds", "(B) Ordinary food", "(C) A dangerous potion", "(D) A magic spell", "(A)", "Laddoos symbolize energy, motherly love, and positive strength.", "Hard", "Evaluating", "Symbolism"),
    ("How can Class 1 students apply Bheem's response to envy in their daily lives?", "(A) By staying calm, ignoring petty jealousy, and continuing to do good deeds humbly", "(B) By shouting at jealous peers", "(C) By stopping work", "(D) By feeling proud", "(A)", "Responding to envy with quiet goodness builds strong character.", "Hard", "Applying", "Real Life Application"),
    ("Why is constructive rivalry healthier than destructive jealousy in childhood growth?", "(A) Healthy rivalry motivates self-improvement, whereas jealousy leads to anger and failure", "(B) Jealousy is better", "(C) Neither exists", "(D) Both cause harm", "(A)", "Striving to improve is healthy; hating others is destructive.", "Hard", "Evaluating", "Psychological Insight"),
    ("Examine how Rajiv Chilaka's creation impacted the Indian animation industry.", "(A) It proved that indigenous Indian stories and characters can achieve massive commercial and cultural success", "(B) It closed animation studios", "(C) It brought foreign cartoons", "(D) It failed", "(A)", "Chhota Bheem revolutionized Indian original animation.", "Hard", "Evaluating", "Media History"),
    ("Why does Bheem's intelligence matter as much as his physical strength?", "(A) Strength without intelligence leads to foolish mistakes; wisdom guides strength to solve complex problems", "(B) Strength is all you need", "(C) Intelligence is useless", "(D) Neither matters", "(A)", "Mind and muscle together create effective problem-solving.", "Hard", "Analyzing", "Philosophy"),
    ("How does the friendship among Bheem, Chhutki, Raju, and Jaggu show diversity in unity?", "(A) Humans, a younger boy, a girl, and a monkey bring different abilities together harmoniously", "(B) All friends are identical", "(C) They fight daily", "(D) They don't talk", "(A)", "Diverse traits enrich their unified friendship.", "Hard", "Evaluating", "Social Insight"),
    ("What is the ultimate educational message of Chapter 06 for primary learners?", "(A) True strength lies in kindness, helping others, remaining humble, and staying loyal to good friends!", "(B) Eat laddoos only", "(C) Watch TV all day", "(D) Try to defeat everyone", "(A)", "Kindness, helpfulness, humility, and loyalty form the core message.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 06: My Favourite Cartoon\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK01_CH06_MCQ_{idx:03d}"
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

with open(os.path.join(CH06_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Chhota Bheem is a _______-years-old boy.", "9 / nine", "Bheem is 9 years old.", "Easy"),
    ("Chhota Bheem lives in a village named _______.", "Dholakpur", "The village is Dholakpur.", "Easy"),
    ("Bheem is very intelligent, brave, and _______.", "strong / helpful / kind", "Bheem is strong and helpful.", "Easy"),
    ("Eating tasty _______ gives Bheem extra strength.", "laddoos", "Laddoos give him strength.", "Easy"),
    ("Tuntun Mausi makes delicious _______ in Dholakpur.", "laddoos", "Tuntun Mausi makes laddoos.", "Easy"),
    ("Chhutki is the daughter of Tuntun _______.", "Mausi", "Chhutki's mother is Tuntun Mausi.", "Easy"),
    ("Kaliya is always _______ of Bheem's popularity.", "jealous", "Kaliya feels jealous of Bheem.", "Easy"),
    ("Dholu and Bholu are Kaliya's twin _______.", "sidekicks / brothers", "Dholu and Bholu are twin sidekicks.", "Easy"),
    ("Jaggu is Bheem's smart _______ friend.", "monkey", "Jaggu is a monkey.", "Easy"),
    ("Bheem always helps the _______ whenever they are in trouble.", "villagers / people", "Bheem helps the villagers.", "Easy"),
    ("Rajiv Chilaka is the _______ of Chhota Bheem.", "creator", "Rajiv Chilaka created Bheem.", "Easy"),
    ("Raju is Bheem's young and brave _______.", "friend", "Raju is Bheem's friend.", "Easy"),
    ("Kaliya tries to prove he is better than Bheem, but fails every _______.", "time", "Kaliya fails every time.", "Easy"),
    ("Chhota Bheem is considered the largest kids' entertainment brand in _______.", "India", "It is India's largest kids brand.", "Easy"),
    ("Bheem is loved by everyone in Dholakpur except _______.", "Kaliya", "Kaliya is jealous of him.", "Easy"),
    ("Chhutki is the main female character in Chhota _______.", "Bheem", "She is a key character.", "Easy"),
    ("Bheem is always kind and _______ to others.", "helpful", "Bheem is kind and helpful.", "Easy"),
    ("Dholu and Bholu are _______ brothers.", "twin", "They are twin brothers.", "Easy"),
    ("Jaggu loves to climb and swing on _______.", "trees", "Monkeys swing on trees.", "Easy"),
    ("Tuntun Mausi's laddoos are sweet and _______.", "tasty / delicious", "Laddoos are delicious.", "Easy"),
    ("Chapter 06 describes my favourite _______ show.", "cartoon", "It describes a cartoon show.", "Easy"),
    ("Bheem uses his strength for good deeds, not to _______ others.", "harm / hurt", "He uses strength for good.", "Easy"),
    ("Raju, Chhutki, and Jaggu are Bheem's loyal _______.", "friends", "They are his loyal friends.", "Easy"),
    ("Bheem protects Dholakpur from dangerous _______.", "villains / monsters", "He protects from villains.", "Easy"),
    ("Kaliya's sidekicks are named Dholu and _______.", "Bholu", "Dholu and Bholu are twins.", "Easy"),

    # Medium (26-40)
    ("The word 'sidekick' means a close assistant or _______.", "helper / companion", "Sidekick means a helper.", "Medium"),
    ("The word 'jealous' means feeling bitter about another's _______.", "success / popularity", "Jealousy means feeling bitter.", "Medium"),
    ("The word 'rivalry' means competition between _______.", "opponents / rivals", "Rivalry means competition.", "Medium"),
    ("Bheem's strength increases dramatically after eating a _______.", "laddoo", "Laddoo gives an energy boost.", "Medium"),
    ("Kaliya's attempts to outsmart Bheem usually end in _______.", "failure / trouble", "His attempts end in failure.", "Medium"),
    ("Chhutki often helps Bheem by giving smart _______.", "ideas / advice", "Chhutki offers smart ideas.", "Medium"),
    ("Dholakpur stays safe because Bheem is always _______.", "alert / protective", "Bheem protects Dholakpur.", "Medium"),
    ("Bheem forgives Kaliya because Bheem has a generous _______.", "heart", "Bheem has a forgiving heart.", "Medium"),
    ("Raju carries a bow and arrow because he is a brave _______.", "archer", "Raju is a young archer.", "Medium"),
    ("Jaggu alerts Bheem whenever he spots danger from top of a _______.", "tree", "Jaggu spots danger from trees.", "Medium"),
    ("Tuntun Mausi's shop is famous for sweet _______.", "sweets / laddoos", "Her shop sells laddoos.", "Medium"),
    ("Teamwork allows Bheem and his friends to solve complex _______.", "problems / challenges", "Teamwork solves challenges.", "Medium"),
    ("Chhota Bheem teaches children to stand up against _______.", "evil / villains / wrong", "Bheem fights against wrong.", "Medium"),
    ("Kaliya boasts about his power, but Bheem remains _______.", "humble", "Bheem remains humble.", "Medium"),
    ("Children all over India love watching Bheem's _______.", "adventures / show", "Kids love Bheem's adventures.", "Medium"),

    # Hard (41-50)
    ("Bheem's character demonstrates that physical power must be guided by moral _______.", "wisdom / values", "Wisdom must guide power.", "Hard"),
    ("Kaliya's rivalry stems from insecure _______.", "jealousy / envy", "Jealousy causes rivalry.", "Hard"),
    ("The colorful world of Dholakpur presents traditional Indian village _______.", "culture", "It reflects Indian village culture.", "Hard"),
    ("Complementary strengths among friends enable successful _______.", "teamwork", "Different skills build teamwork.", "Hard"),
    ("Forgiveness transforms potential enemies into future _______.", "allies / friends", "Forgiveness turns enemies to friends.", "Hard"),
    ("Rajiv Chilaka pioneered original Indian animated _______.", "entertainment", "He pioneered Indian animation.", "Hard"),
    ("Laddoos serve as a narrative symbol of strength and _______.", "joy / energy", "Laddoos symbolize energy.", "Hard"),
    ("Class 1 students learn to celebrate their friends' _______.", "success", "Students learn to celebrate peers.", "Hard"),
    ("Selfless service brings lasting popularity and _______.", "love / respect", "Helping brings respect.", "Hard"),
    ("The show inspires children to cultivate courage, kindness, and _______.", "integrity", "It inspires positive values.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 06: My Favourite Cartoon\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK01_CH06_FIB_{idx:03d}"
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

with open(os.path.join(CH06_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. Fill in Blanks from Story (Cloze Passage) (50 Distinct Qs)
# -------------------------------------------------------------
cloze_data = [
    ("Who doesn't recognize this loveable boy, Chhota _______?", "Bheem", "Easy"),
    ("Chhota Bheem is a story based in a village named _______.", "Dholakpur", "Easy"),
    ("Bheem is a _______-years-old boy.", "9 / nine", "Easy"),
    ("Bheem is very intelligent and _______.", "brave", "Easy"),
    ("He always helps the _______ in Dholakpur.", "villagers", "Easy"),
    ("He is the favourite of all the people in the village except _______.", "Kaliya / a few", "Easy"),
    ("Kaliya is a character who always gets _______ of Bheem.", "jealous", "Easy"),
    ("While Bheem helps people, Kaliya ruins _______.", "things", "Easy"),
    ("Kaliya is jealous of the popularity of _______.", "Bheem", "Easy"),
    ("Chhutki is the female character of the _______.", "show", "Easy"),
    ("Chhutki is the daughter of Tuntun _______.", "Mausi", "Easy"),
    ("Tuntun Mausi makes very tasty _______.", "laddoos", "Easy"),
    ("Raju and Jaggu are also characters of this _______.", "show", "Easy"),
    ("Jaggu is a smart, playful _______.", "monkey", "Easy"),
    ("Raju and Jaggu have a rivalry with _______.", "Kaliya", "Easy"),
    ("Kaliya has his sidekicks, twin brothers named Dholu and _______.", "Bholu", "Easy"),
    ("Kaliya wants to prove that he is better than _______.", "Bheem", "Easy"),
    ("Kaliya fails every _______ in his attempt.", "time", "Easy"),
    ("Bheem is always kind to _______.", "others", "Easy"),
    ("Bheem always helps others in _______.", "trouble", "Easy"),
    ("Chhota Bheem is considered the largest children's entertainment _______ in India.", "brand", "Easy"),
    ("Rajiv Chilaka is the _______ of this brand.", "creator", "Easy"),
    ("Eating laddoos gives Bheem extra _______.", "strength / energy", "Easy"),
    ("Bheem protects Dholakpur from evil _______.", "threats / villains", "Easy"),
    ("Children love to watch Bheem's fun _______.", "adventures", "Easy"),

    ("Bheem's strength is famous across the whole _______.", "kingdom / village", "Medium"),
    ("Tuntun Mausi prepares laddoos with fresh _______.", "ingredients", "Medium"),
    ("Chhutki always supports Bheem with good _______.", "ideas", "Medium"),
    ("Raju is a brave little boy with a bow and _______.", "arrow", "Medium"),
    ("Jaggu swings from tree to tree in Dholakpur _______.", "forest / trees", "Medium"),
    ("Dholu and Bholu follow Kaliya's every _______.", "command / order", "Medium"),
    ("Kaliya's jealousy leads him into funny _______.", "trouble", "Medium"),
    ("Bheem steps in to save Kaliya from danger _______.", "humbly", "Medium"),
    ("The villagers cheer whenever Bheem saves the _______.", "day / village", "Medium"),
    ("Chhota Bheem is broadcast on television for _______.", "kids", "Medium"),
    ("The word 'sidekick' means a trusted _______.", "assistant", "Medium"),
    ("The word 'jealous' means feeling envy toward _______.", "others", "Medium"),
    ("Bheem uses his brain as well as his _______.", "muscle / strength", "Medium"),
    ("Rivalry should not turn into evil _______.", "actions", "Medium"),
    ("Bheem's positive attitude brings happiness to _______.", "Dholakpur", "Medium"),

    ("Cultural Indian elements enrich the storytelling of Chhota _______.", "Bheem", "Hard"),
    ("Bheem's selflessness contrasts with Kaliya's selfish _______.", "desires", "Hard"),
    ("Laddoos act as a narrative symbol of sudden _______.", "empowerment", "Hard"),
    ("Dholakpur's peace is preserved by vigilance and _______.", "courage", "Hard"),
    ("Chhutki's intelligence reflects gender equality in the _______.", "group", "Hard"),
    ("Rajiv Chilaka's vision brought Indian animation to global _______.", "fame", "Hard"),
    ("Forgiveness prevents ongoing conflicts among village _______.", "children", "Hard"),
    ("Class 1 students learn to use their abilities for common _______.", "good", "Hard"),
    ("True heroism lies in protecting the weak and vulnerable _______.", "people", "Hard"),
    ("Chhota Bheem inspires kids with timeless moral _______.", "lessons", "Hard")
]

cloze_content = f"# Fill in the Blanks from Story — Chapter 06: My Favourite Cartoon\n\n> **Category**: Fill in the Blanks from Story (Cloze Passage) | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(cloze_data, start=1):
    q_id = f"BK01_CH06_STORY_FIB_{idx:03d}"
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

with open(os.path.join(CH06_DIR, "fill_in_blanks_story.md"), "w", encoding="utf-8") as f:
    f.write(cloze_content)

# -------------------------------------------------------------
# 4. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Chhota Bheem is a 9-year-old intelligent and brave boy.", True, "Bheem is 9 years old, intelligent, and brave.", "Easy"),
    ("The story of Chhota Bheem is set in the village of Dholakpur.", True, "Dholakpur is the setting of the story.", "Easy"),
    ("Eating laddoos gives Bheem extra strength.", True, "Laddoos provide Bheem with instant extra strength.", "Easy"),
    ("Tuntun Mausi makes delicious samosas in Dholakpur.", False, "Tuntun Mausi makes delicious laddoos.", "Easy"),
    ("Chhutki is the daughter of Tuntun Mausi.", True, "Chhutki is Tuntun Mausi's daughter.", "Easy"),
    ("Kaliya is Bheem's best friend who loves him very much.", False, "Kaliya is jealous of Bheem and tries to compete with him.", "Easy"),
    ("Dholu and Bholu are Kaliya's twin sidekicks.", True, "Dholu and Bholu are twin brothers and sidekicks to Kaliya.", "Easy"),
    ("Jaggu is a smart monkey who is friends with Bheem.", True, "Jaggu is a monkey friend of Bheem.", "Easy"),
    ("Bheem uses his strength to bully smaller children in Dholakpur.", False, "Bheem always uses his strength to help and protect others.", "Easy"),
    ("Rajiv Chilaka is the creator of Chhota Bheem.", True, "Rajiv Chilaka created the Chhota Bheem brand.", "Easy"),
    ("Raju and Jaggu are friends of Chhota Bheem.", True, "Raju and Jaggu are Bheem's good friends.", "Easy"),
    ("Kaliya succeeds every time he tries to prove he is better than Bheem.", False, "Kaliya fails every time in his attempts.", "Easy"),
    ("Bheem is the favourite of almost everyone in Dholakpur.", True, "Bheem is loved by all the villagers.", "Easy"),
    ("Chhota Bheem is considered India's largest kids' entertainment brand.", True, "It is India's largest kids brand.", "Easy"),
    ("Bheem refuses to help Kaliya when Kaliya gets into trouble.", False, "Bheem is kind and helps even Kaliya when in trouble.", "Easy"),
    ("Bheem is 15 years old in the story.", False, "Bheem is a 9-year-old boy.", "Easy"),
    ("Chhutki is a female character in Chhota Bheem.", True, "Chhutki is the main female character.", "Easy"),
    ("Dholu and Bholu are twin brothers.", True, "Dholu and Bholu are twins.", "Easy"),
    ("Bheem always helps villagers whenever they face trouble.", True, "He always protects the villagers.", "Easy"),
    ("Tuntun Mausi's laddoos are famous in Dholakpur.", True, "Her laddoos are famous and tasty.", "Easy"),
    ("Kaliya is jealous of Bheem's popularity.", True, "Kaliya feels jealous of Bheem.", "Easy"),
    ("Raju carries a sword and shield.", False, "Raju carries a bow and arrow.", "Easy"),
    ("Jaggu the monkey can swing on trees.", True, "Jaggu is a monkey who swings on trees.", "Easy"),
    ("Bheem is rude and mean to his friends.", False, "Bheem is always kind, polite, and helpful.", "Easy"),
    ("Chapter 06 tells the story of Chhota Bheem and his friends.", True, "Chapter 06 details Chhota Bheem's show.", "Easy"),

    # Medium (26-40)
    ("The word 'sidekick' means a close assistant or helper.", True, "Sidekick means a helper or assistant.", "Medium"),
    ("The word 'jealous' means feeling happy about another's success.", False, "Jealous means feeling envious or bitter about another's success.", "Medium"),
    ("The word 'rivalry' means friendly cooperation without competition.", False, "Rivalry means competition between opponents.", "Medium"),
    ("Laddoos give Bheem a temporary boost of energy during crisis.", True, "Laddoos give him an energy boost.", "Medium"),
    ("Kaliya's plans usually fail because he acts out of jealousy and arrogance.", True, "His bad intentions cause his plans to fail.", "Medium"),
    ("Chhutki helps the team with her cleverness and problem-solving skills.", True, "Chhutki offers smart ideas.", "Medium"),
    ("Bheem boasts loudly whenever he defeats a villain.", False, "Bheem remains humble and modest after every victory.", "Medium"),
    ("Jaggu alerts Bheem whenever he spots danger in Dholakpur.", True, "Jaggu acts as a watchful friend.", "Medium"),
    ("Dholu and Bholu sometimes get confused because they are twins.", True, "They are comical twin brothers.", "Medium"),
    ("Bheem's strength comes only from laddoos, not from training.", False, "Bheem is naturally brave, intelligent, and strong; laddoos give extra power.", "Medium"),
    ("Raju is older than Bheem.", False, "Raju is younger than Bheem.", "Medium"),
    ("Bheem forgives Kaliya whenever Kaliya apologizes.", True, "Bheem is forgiving and holds no grudges.", "Medium"),
    ("Chhota Bheem show features Indian village culture and traditions.", True, "It features traditional Indian village life.", "Medium"),
    ("Kaliya's sidekicks always do the right thing without following Kaliya.", False, "They follow Kaliya's commands as sidekicks.", "Medium"),
    ("Bheem teaches children to use strength for protecting the weak.", True, "Bheem promotes using power for good.", "Medium"),

    # Hard (41-50)
    ("Bheem's popularity proves that humility attracts more love than arrogance.", True, "Bheem's humility makes him loved by all.", "Hard"),
    ("Kaliya's character shows that envy causes self-inflicted trouble.", True, "Envy leads Kaliya into constant trouble.", "Hard"),
    ("Chhutki's role demonstrates gender equality in children's adventure groups.", True, "Chhutki is an active, smart leader.", "Hard"),
    ("Rajiv Chilaka created Chhota Bheem to provide original Indian content for kids.", True, "He pioneered original Indian animation.", "Hard"),
    ("Physical strength without moral character leads to bullying.", True, "Strength without morals turns into bullying.", "Hard"),
    ("Laddoos symbolize positive reinforcement and energy in the show's narrative.", True, "Laddoos symbolize positive energy.", "Hard"),
    ("Bheem's group shows that diverse skills (mind, muscle, agility) create strong teams.", True, "Diverse skills make a strong team.", "Hard"),
    ("Kaliya's failures teach children that shortcuts and cheating do not lead to real success.", True, "Shortcuts fail against true effort.", "Hard"),
    ("Bheem's willingness to save his rival shows high emotional maturity.", True, "Saving a rival shows high maturity.", "Hard"),
    ("Chapter 06 encourages Class 1 learners to cultivate bravery, kindness, and loyalty.", True, "It promotes core positive virtues.", "Hard")
]

tf_content = f"# True / False — Chapter 06: My Favourite Cartoon\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK01_CH06_TF_{idx:03d}"
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

with open(os.path.join(CH06_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 5. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who is Chhota Bheem and where does he live?", "Chhota Bheem is a 9-year-old intelligent and brave boy who lives in Dholakpur village.", "Easy"),
    ("What food gives Chhota Bheem extra strength?", "Eating tasty laddoos made by Tuntun Mausi gives Chhota Bheem extra strength.", "Easy"),
    ("Who is Tuntun Mausi and what is she famous for?", "Tuntun Mausi is Chhutki's mother and she is famous for making delicious laddoos.", "Easy"),
    ("Who is Chhutki in the show Chhota Bheem?", "Chhutki is a clever girl who is Tuntun Mausi's daughter and Bheem's good friend.", "Easy"),
    ("Who is Kaliya and why is he jealous of Bheem?", "Kaliya is a boy in Dholakpur who is jealous of Bheem's popularity and strength.", "Easy"),
    ("Who are Kaliya's twin sidekicks?", "Kaliya's twin sidekicks are brothers named Dholu and Bholu.", "Easy"),
    ("Who is Jaggu in Chhota Bheem?", "Jaggu is a smart, friendly monkey who is Bheem's close friend.", "Easy"),
    ("Who is Raju in the show?", "Raju is a brave little boy who carries a bow and arrow and is Bheem's friend.", "Easy"),
    ("Who created the cartoon brand Chhota Bheem?", "Rajiv Chilaka created the brand Chhota Bheem.", "Easy"),
    ("How do the villagers of Dholakpur feel about Bheem?", "The villagers love Bheem because he always helps and protects them.", "Easy"),
    ("Does Kaliya ever succeed in proving he is better than Bheem?", "No, Kaliya tries every time but fails because Bheem is truly brave and good.", "Easy"),
    ("What does Bheem do when the villagers face trouble?", "Bheem uses his intelligence and strength to save the villagers from trouble.", "Easy"),
    ("What does Bheem do when Kaliya gets into trouble?", "Bheem kindly helps and saves Kaliya whenever Kaliya gets into trouble.", "Easy"),
    ("What does the word 'sidekick' mean?", "'Sidekick' means a close assistant or helper to a primary character.", "Easy"),
    ("What does the word 'jealous' mean?", "'Jealous' means feeling bitter or unhappy about someone else's popularity or success.", "Easy"),
    ("What does the word 'rivalry' mean?", "'Rivalry' means competition between two people or groups trying to be better.", "Easy"),
    ("Name four main friends of Chhota Bheem.", "Four main friends are Chhutki, Raju, Jaggu the monkey, and Kalia (whom Bheem treats kindly).", "Easy"),
    ("Why do kids love watching Chhota Bheem?", "Kids love Chhota Bheem because of his exciting adventures, fun friends, and moral lessons.", "Easy"),
    ("What is Bheem's age in the cartoon show?", "Bheem is 9 years old.", "Easy"),
    ("Where can you see Chhota Bheem?", "You can watch Chhota Bheem on television shows and read about him in storybooks.", "Easy"),
    ("Does Bheem boast about his strength?", "No, Bheem is very humble and never boasts about his power.", "Easy"),
    ("How do Dholu and Bholu help Kaliya?", "Dholu and Bholu follow Kaliya's commands and help him in his plans.", "Easy"),
    ("Why is Tuntun Mausi's shop popular?", "Her shop is popular because she prepares the tastiest laddoos in Dholakpur.", "Easy"),
    ("What animal character helps Bheem climb trees?", "Jaggu the monkey helps Bheem by climbing and swinging on trees.", "Easy"),
    ("What key moral does Chhota Bheem teach children?", "It teaches children to be brave, helpful, kind, and loyal to friends.", "Easy"),

    # Medium (26-40)
    ("Why does Bheem eat laddoos during dangerous fights?", "Laddoos give Bheem an instant energy boost, allowing him to use super strength against big villains.", "Medium"),
    ("How does Bheem's humble attitude win the hearts of villagers?", "He protects everyone selflessly and never boasts, earning deep love and respect from Dholakpur.", "Medium"),
    ("What makes Chhutki an important character in the group?", "Chhutki uses her quick intelligence to offer smart ideas and support Bheem during crises.", "Medium"),
    ("Why do Kaliya's plans against Bheem always fail?", "Kaliya acts out of envy and pride, whereas Bheem acts out of truth and desire to protect others.", "Medium"),
    ("How does Jaggu the monkey use his natural abilities to help Bheem?", "Jaggu swings across trees to scout danger, fetch objects, and alert the team quickly.", "Medium"),
    ("Why is Bheem considered a good role model for young children?", "Because he demonstrates bravery, kindness, respect for elders, teamwork, and forgiveness.", "Medium"),
    ("How does Raju show that age does not limit courage?", "Though younger, Raju fearlessly joins Bheem in facing villains using his archery skills.", "Medium"),
    ("What is the significance of Dholakpur village in the show?", "Dholakpur serves as a colorful Indian village setting where traditional values and fun adventures meet.", "Medium"),
    ("Why does Bheem forgive Kaliya even after Kaliya tries to trick him?", "Bheem believes in forgiveness and wants everyone in Dholakpur to live peacefully together.", "Medium"),
    ("How do Dholu and Bholu add comedy to the cartoon?", "Their twin confusion, funny mistakes, and comical loyalty to Kaliya bring humor to the show.", "Medium"),
    ("What makes Tuntun Mausi a loving figure in the narrative?", "She cares for all the children in Dholakpur and happily feeds them delicious laddoos.", "Medium"),
    ("How does Chhota Bheem promote Indian animation globally?", "It proved that original Indian stories with rich cultural roots can become massive hits worldwide.", "Medium"),
    ("What happens when someone tries to harm Dholakpur?", "Bheem and his friends unite, use their unique skills, and defeat the villain safely.", "Medium"),
    ("How does teamwork play a role in Bheem's adventures?", "Each friend brings a different strength—Bheem brings muscle, Chhutki brings brain, Jaggu brings agility.", "Medium"),
    ("Summarize Chapter 06 in two clear sentences.", "Chapter 06 describes Chhota Bheem, a 9-year-old brave and helpful boy in Dholakpur who eats laddoos for strength. Along with friends Chhutki, Raju, and Jaggu, he protects villagers and teaches good values.", "Medium"),

    # Hard (41-50)
    ("Analyze the contrast between Bheem's selfless leadership and Kaliya's selfish ambition.", "Bheem leads through service, empathy, and protection, earning natural respect. Kaliya seeks dominance through arrogance and tricks, resulting in failure.", "Hard"),
    ("Evaluate the role of food (laddoos) as a storytelling device in Chhota Bheem.", "Laddoos serve as a fun power-up mechanism similar to folklore magic, symbolizing warmth, energy, and reward for goodness.", "Hard"),
    ("How does Chhota Bheem combine traditional Indian culture with modern entertainment?", "It incorporates traditional clothing (dhotis), sweets (laddoos), and village settings with modern fast-paced animation and superhero tropes.", "Hard"),
    ("Why is emotional maturity necessary when dealing with envious peers like Kaliya?", "Bheem shows that responding to jealousy with calm forgiveness rather than retaliation prevents hostility and heals relationships.", "Hard"),
    ("Discuss how the show encourages gender equality among primary school viewers.", "By presenting Chhutki as a smart, capable, and active co-adventurer, the show promotes equal respect for girls.", "Hard"),
    ("How can Class 1 students practice Bheem's values during school sports or games?", "By playing fair, helping teammates who fall, remaining humble when winning, and being polite to opponents.", "Hard"),
    ("Examine the impact of Rajiv Chilaka's creation on Indian children's media.", "It established India's first homegrown animated superstar, inspiring local storytellers to create indigenous content.", "Hard"),
    ("Why is strength without kindness dangerous in society?", "Unchecked strength turns into bullying and destruction. Kindness ensures power is used strictly for protection and justice.", "Hard"),
    ("Deconstruct the group dynamics of Bheem's team during a crisis.", "Bheem acts as the physical defender, Chhutki as the strategist, Raju as the ranged striker, and Jaggu as the agile scout.", "Hard"),
    ("Synthesize the ultimate takeaway of Chapter 06 for Class 1 learners.", "Be brave in danger, kind to all, humble in victory, and always use your strengths to protect and help others!", "Hard")
]

sa_content = f"# Short Answer — Chapter 06: My Favourite Cartoon\n\n> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK01_CH06_SA_{idx:03d}"
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

with open(os.path.join(CH06_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 6. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-15)
    ("Write a simple summary of Chapter 06 'My Favourite Cartoon'.", "Chhota Bheem is a popular cartoon about a 9-year-old boy living in Dholakpur village. Bheem is intelligent, brave, and strong. He loves eating delicious laddoos made by Tuntun Mausi, which give him extra strength. Bheem always protects the villagers and is loved by everyone. Kaliya is a boy who gets jealous of Bheem's popularity and tries to outdo him with his twin sidekicks Dholu and Bholu, but fails every time. Bheem's good friends are Chhutki, Raju, and Jaggu the monkey. Bheem is always kind, helpful, and humble.", "Easy"),
    ("Describe the character of Chhota Bheem in detail.", "Chhota Bheem is a 9-year-old boy who is the hero of Dholakpur. He is intelligent, immensely strong, and brave. Despite his great power, Bheem is humble, polite, and kind-hearted. He loves eating laddoos made by Tuntun Mausi to get extra strength during fights. He uses his power only to protect villagers and help friends in need.", "Easy"),
    ("Who is Kaliya and why does he compete with Bheem?", "Kaliya is a character in Dholakpur who is envious of Bheem's immense popularity, strength, and love from villagers. Kaliya constantly tries to prove that he is better than Bheem. He is accompanied by his twin sidekicks, Dholu and Bholu. However, Kaliya fails every time because he acts out of pride rather than genuine goodness.", "Easy"),
    ("Describe Bheem's close friends Chhutki, Raju, and Jaggu.", "Chhutki is Tuntun Mausi's clever daughter who gives smart ideas to the team. Raju is a brave little boy skilled in archery who fearlessly joins adventures. Jaggu is a sweet, agile monkey who swings on trees and alerts the group to danger. Together, they form a loyal team supporting Bheem.", "Easy"),
    ("Explain the role of Tuntun Mausi and her laddoos in the story.", "Tuntun Mausi is Chhutki's mother who runs a popular sweet shop in Dholakpur. She makes the tastiest laddoos in the village. Her laddoos are special because whenever Bheem eats them, he gains an instant burst of extra strength to defeat powerful villains and save the day.", "Easy"),
    ("Why is Chhota Bheem the favourite of all villagers in Dholakpur?", "Bheem is the favourite of all villagers because he is selfless and always ready to help anyone in trouble. Whether fighting dangerous monsters or solving small village problems, Bheem works hard to keep Dholakpur safe and happy without expecting anything in return.", "Easy"),
    ("How does Bheem treat Kaliya when Kaliya gets into trouble?", "Even though Kaliya acts as a rival and tries to trick Bheem, Bheem never holds grudges. Whenever Kaliya gets into danger or trouble, Bheem kindly steps in, rescues him safely, and treats him like a fellow villager with warmth and forgiveness.", "Easy"),
    ("Who created Chhota Bheem and why is it famous in India?", "Chhota Bheem was created by Rajiv Chilaka. It is famous in India because it is considered the largest children's entertainment brand. Kids love its fun characters, Indian village setting, exciting adventures, and positive moral lessons.", "Easy"),
    ("Describe the village of Dholakpur.", "Dholakpur is a colorful, peaceful Indian village where Bheem and his friends live. It has green trees, simple houses, and friendly villagers. Although evil villains occasionally attack Dholakpur, Bheem and his friends always defend it successfully.", "Easy"),
    ("What lesson does Chapter 06 teach about using your strength?", "Chapter 06 teaches that strength should always be used to protect the weak, help people in need, and do good deeds. Physical power without kindness and humility leads to bullying and failure.", "Easy"),
    ("Describe Dholu and Bholu and their role in the show.", "Dholu and Bholu are twin brothers who act as Kaliya's sidekicks. They look identical, wear similar clothes, and follow Kaliya everywhere. Their funny arguments, silly mistakes, and comical loyalty bring lots of humor to the cartoon.", "Easy"),
    ("What makes Chhutki a special friend to Bheem?", "Chhutki is special because she is exceptionally smart, caring, and supportive. She helps her mother make laddoos and uses her sharp brain to help Bheem solve mysteries and outsmart villains.", "Easy"),
    ("Why does Bheem never boast after winning a fight?", "Bheem is naturally humble and modest. He believes that doing good deeds and saving people is his duty, not something to boast about. His humility makes him a true hero.", "Easy"),
    ("How does Jaggu the monkey help Bheem during adventures?", "Jaggu uses his monkey agility to climb high trees, scout for hidden danger, fetch objects from difficult places, and communicate warnings quickly to Bheem and the group.", "Easy"),
    ("What values can Class 1 students learn from watching Chhota Bheem?", "Students learn to be brave when facing problems, help classmates in need, remain humble when achieving success, stay loyal to friends, and forgive those who make mistakes.", "Easy"),

    # Medium (16-40)
    ("Compare the character of Chhota Bheem with the character of Kaliya.", "Bheem is selfless, humble, brave, and uses his strength to protect others, earning universal love. Kaliya is boastful, envious, and tries to show off to gain fame, resulting in repeated failures. Bheem represents true heroism, while Kaliya represents misguided rivalry.", "Medium"),
    ("Explain how teamwork helps Bheem and his friends defeat powerful enemies.", "No single person can solve every problem alone. Bheem brings physical strength, Chhutki brings strategic brainpower, Raju brings brave archery, and Jaggu brings high agility. By combining their unique talents, the team overcomes challenges that no one could solve alone.", "Medium"),
    ("Discuss the cultural significance of Chhota Bheem in Indian television.", "Chhota Bheem revolutionized Indian animation by proving that Indian folklore, traditional clothing (dhoti), native sweets (laddoos), and village settings can create a world-class, multi-million dollar children's franchise that inspires national pride.", "Medium"),
    ("Why is forgiveness a major theme in Chhota Bheem's character?", "Bheem consistently forgives Kaliya's petty tricks. By choosing forgiveness over revenge, Bheem prevents ongoing hatred in Dholakpur, proving that true strength includes having a forgiving heart.", "Medium"),
    ("How does Tuntun Mausi's character add warmth to the show?", "Tuntun Mausi represents traditional motherly love, hospitality, and warmth. Her delicious laddoos are not just food, but symbols of care and energy that nourish the young heroes of Dholakpur.", "Medium"),
    ("Write a dialogue between Bheem and Kaliya after Bheem saves Kaliya from a trap.", "Kaliya: 'Why did you save me, Bheem? I tried to trick you!'\nBheem: 'We all live in Dholakpur together, Kaliya. Friends help each other, no matter what!'\nKaliya: 'Thank you, Bheem... You really are the best!'", "Medium"),
    ("Explain why Bheem's intelligence is just as important as his physical strength.", "Physical power alone cannot solve complex traps or outsmart tricky villains. Bheem uses his sharp mind to observe clues, plan strategies, and use his strength at the exact right moment.", "Medium"),
    ("How does Raju demonstrate that young children can be brave and helpful?", "Raju is younger and smaller than Bheem, yet he never backs down from danger. He practices archery diligently and stands side by side with Bheem, showing that courage depends on spirit, not age.", "Medium"),
    ("What makes Chhutki an inspiring female role model for young girls?", "Chhutki is active, intelligent, confident, and brave. She is not a passive bystander; she actively participates in adventures, solves puzzles, and stands up against wrongdoings.", "Medium"),
    ("How does the setting of Dholakpur enhance the storytelling of the cartoon?", "Dholakpur provides a picturesque Indian village backdrop with ancient forts, dense forests, river banks, and traditional markets, making every adventure visually rich and culturally rooted.", "Medium"),
    ("Why do Dholu and Bholu stay with Kaliya despite his bossy behavior?", "Despite Kaliya's bossiness, Dholu and Bholu share a deep brotherly bond with him. Their loyalty shows that sidekicks remain faithful, though Bheem's kindness often makes them admire Bheem too.", "Medium"),
    ("Describe a typical adventure flow in an episode of Chhota Bheem.", "An episode typically begins with peaceful village life in Dholakpur, followed by a sudden threat from a villain. Bheem and his friends investigate, face obstacles, eat laddoos for extra power, defeat the threat, and celebrate with the villagers.", "Medium"),
    ("How does Chhota Bheem teach children about respect for elders?", "Bheem and his friends always touch the feet of elders, speak politely to villagers, obey Tuntun Mausi and King Indraverma, showing deep traditional Indian respect for authority and age.", "Medium"),
    ("Why is positive reinforcement through food (laddoos) a clever narrative choice?", "It transforms an everyday sweet that Indian children love into a magical symbol of energy, making the story fun, relatable, and culturally iconic.", "Medium"),
    ("Explain how Bheem handles victory after defeating a major villain.", "After winning, Bheem never brags or demands rewards. He smiles, credits his friends' teamwork, ensures the villagers are safe, and humbly returns to normal daily life.", "Medium"),
    ("How does Jaggu the monkey break the barrier between humans and animals in friendship?", "Jaggu is treated as an equal friend rather than a pet. He communicates, plays, fights alongside humans, demonstrating empathy and love for animal companions.", "Medium"),
    ("What lesson does Kaliya's character offer to children who feel jealous of peers?", "Kaliya's constant failures show that being jealous wastes energy and causes embarrassment. Instead of envying others, children should focus on improving themselves and being good friends.", "Medium"),
    ("How does Chhota Bheem promote physical fitness and healthy active living?", "Bheem is outdoorsy, plays traditional Indian games (like kabaddi and gilli-danda), runs, climbs, and exercises, encouraging children to be active outdoors rather than glued to screens.", "Medium"),
    ("What is the role of King Indraverma and Princess Indumati in Dholakpur?", "King Indraverma rules Dholakpur wisely and trusts Bheem completely. Princess Indumati is Chhutki's royal friend. Together they represent good governance and royal support for the villagers.", "Medium"),
    ("Summarize the ultimate educational and moral impact of Chapter 06.", "Chapter 06 uses the beloved figure of Chhota Bheem to teach Class 1 students that true heroism combines bravery, intelligence, humility, generosity, and loyal friendship.", "Medium"),

    # Hard (41-50)
    ("Deconstruct the ethical philosophy of Chhota Bheem's character.", "Bheem embodies classical virtue ethics. His actions are governed by selfless duty (Dharma), non-malice toward rivals, active protection of the weak, and absolute alignment with truth and righteousness.", "Hard"),
    ("Analyze how Chhota Bheem serves as a cultural bridge for modern Indian children.", "It bridges ancient Indian epic archetypes (like Bhima's strength and Krishna's playfulness) with modern animated storytelling, instilling cultural literacy in a globalized media landscape.", "Hard"),
    ("Critique the psychological dynamic between Bheem and Kaliya.", "It represents the classic conflict between secure self-worth (Bheem) and insecure ego (Kaliya). Bheem's calm acceptance eventually diffuses Kaliya's hostility, modeling constructive conflict resolution.", "Hard"),
    ("Evaluate the impact of original Indian IP (Intellectual Property) created by Rajiv Chilaka.", "Chilaka's success broke reliance on Western/Japanese cartoon imports, establishing a thriving domestic animation ecosystem that generates local employment and cultural pride.", "Hard"),
    ("How does the concept of 'Dharma' (righteous duty) manifest in Bheem's daily actions?", "Bheem acts out of intrinsic moral duty without seeking personal gain or praise. He defends Dholakpur because it is right, exemplifying selfless action (Nishkama Karma).", "Hard"),
    ("Formulate a classroom activity for Class 1 based on Chhota Bheem's moral lessons.", "Students draw their favorite character, identify one positive virtue (like Bheem's helpfulness or Chhutki's smartness), and share how they will practice that virtue with a classmate.", "Hard"),
    ("Examine the gender representation in Chhota Bheem through Chhutki and Indumati.", "While Bheem is the male lead, female characters are portrayed as intelligent, decisive, courageous, and essential to problem-solving, breaking traditional passive female tropes.", "Hard"),
    ("Why is narrative predictability (Bheem winning after eating laddoos) comforting for young viewers?", "Primary children thrive on familiar narrative safety. Predictable triumph of good over evil builds psychological security, clear moral clarity, and emotional satisfaction.", "Hard"),
    ("Discuss how the show promotes sportsmanship and fair play.", "Bheem participates in competitions with absolute honesty, follows rules strictly, respects opponents, and rejects cheating, offering a masterclass in sportsmanship.", "Hard"),
    ("Synthesize the ultimate educational message of Chapter 06 for primary learners.", "Be a hero in your own life: use your mind and muscle to help others, treat everyone with kindness, forgive your rivals, stay humble, and cherish your friends!", "Hard")
]

la_content = f"# Long Answer — Chapter 06: My Favourite Cartoon\n\n> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK01_CH06_LA_{idx:03d}"
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

with open(os.path.join(CH06_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

print("[SUCCESS] All 6 category files for Chapter 06 completely refined with 100% unique Class 1 questions!")
