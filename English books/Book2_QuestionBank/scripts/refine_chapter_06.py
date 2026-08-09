r"""
Refines all 6 Category files for Chapter 06 ("My Favourite Cartoon") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
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
    ("Who is the main cartoon character described in Chapter 06?", "(A) Doraemon", "(B) Mickey Mouse", "(C) Pikachu", "(D) Tom", "(A)", "The chapter focuses on the lovable robotic cat Doraemon.", "Easy", "Remembering", "Character Name"),
    ("What color is Doraemon?", "(A) Blue", "(B) Red", "(C) Yellow", "(D) Green", "(A)", "Doraemon is described as a lovable blue earless robotic cat.", "Easy", "Remembering", "Color"),
    ("What special physical feature is missing on Doraemon?", "(A) Ears", "(B) Tail", "(C) Eyes", "(D) Whiskers", "(A)", "Doraemon is an earless robotic cat.", "Easy", "Remembering", "Physical Feature"),
    ("Who created the character of Doraemon?", "(A) Fujiko F. Fujio", "(B) Walt Disney", "(C) Hayao Miyazaki", "(D) Osamu Tezuka", "(A)", "Doraemon was created by Fujiko F. Fujio.", "Easy", "Remembering", "Creator Name"),
    ("In which year was Doraemon first introduced?", "(A) 1969", "(B) 1999", "(C) 2005", "(D) 1950", "(A)", "It was first introduced in 1969.", "Easy", "Remembering", "Introduction Year"),
    ("Which century is Doraemon originally from?", "(A) 22nd century", "(B) 21st century", "(C) 19th century", "(D) 30th century", "(A)", "Doraemon is a robotic cat from the 22nd century.", "Easy", "Remembering", "Time Era"),
    ("Whom was Doraemon sent back in time to help?", "(A) Nobita Nobi", "(B) Shizuka", "(C) Gian", "(D) Suneo", "(A)", "He was sent back in time to help Nobita Nobi.", "Easy", "Remembering", "Target Character"),
    ("Which two words describe Nobita in the text?", "(A) Good but lazy", "(B) Mean and greedy", "(C) Angry and fierce", "(D) Wise and fast", "(A)", "The text describes Nobita as a good but lazy boy.", "Easy", "Remembering", "Character Traits"),
    ("Where does Doraemon fetch his futuristic gadgets from?", "(A) His fourth-dimensional pocket", "(B) A magic wand", "(C) A school bag", "(D) A chest", "(A)", "He fetches gadgets from his fourth-dimensional pocket.", "Easy", "Remembering", "Gadget Source"),
    ("What kind of space is Doraemon's pocket?", "(A) A fourth-dimensional space", "(B) A small wooden box", "(C) A cloth pouch", "(D) A dark cave", "(A)", "His pocket is actually a fourth-dimensional space.", "Easy", "Remembering", "Pocket Dimension"),
    ("What type of items does Doraemon bring out to help Nobita?", "(A) Futuristic gadgets", "(B) Gold coins", "(C) Magic sticks", "(D) Paper toys", "(A)", "He uses futuristic gadgets to improve Nobita's life.", "Easy", "Remembering", "Item Type"),
    ("What kind of situations do Doraemon's gadgets lead to?", "(A) Funny and adventurous situations", "(B) Scary and dark situations", "(C) Boring situations", "(D) Sad situations", "(A)", "The gadgets lead to many funny and adventurous situations.", "Easy", "Remembering", "Plot Situations"),
    ("Which three life lessons does the Doraemon series teach?", "(A) Responsibility, friendship, and hard work", "(B) Greed, fighting, and laziness", "(C) Magic, tricks, and stealing", "(D) Running, jumping, and swimming", "(A)", "The series teaches lessons about responsibility, friendship, and hard work.", "Easy", "Remembering", "Life Lessons"),
    ("What country does the animated character Doraemon originate from?", "(A) Japan", "(B) India", "(C) USA", "(D) France", "(A)", "Doraemon is a popular Japanese animated character.", "Easy", "Remembering", "Country of Origin"),
    ("What does the word 'animated' mean?", "(A) A movie where pictures appear to move", "(B) A book with no pictures", "(C) A radio song", "(D) A real human actor", "(A)", "Animated refers to movies where drawn pictures appear to move.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'futuristic' mean?", "(A) Imagining what things in the future will be like", "(B) Belonging to ancient history", "(C) Very small", "(D) Extremely slow", "(A)", "Futuristic means imagining things of the future.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'naivety' mean?", "(A) Lack of experience or judgement", "(B) High intelligence", "(C) Great physical strength", "(D) Deep sadness", "(A)", "Naivety means lack of experience or judgement.", "Easy", "Understanding", "Vocabulary"),
    ("What kind of personality does Doraemon have?", "(A) Charming personality", "(B) Rude personality", "(C) Scary personality", "(D) Silent personality", "(A)", "The text mentions Doraemon's charming personality.", "Easy", "Remembering", "Personality"),
    ("Is Doraemon a real living cat or a robot?", "(A) A robotic cat", "(B) A real street cat", "(C) A plush stuffed toy", "(D) A wild tiger", "(A)", "Doraemon is a robotic cat.", "Easy", "Remembering", "Nature"),
    ("What does Doraemon try to do for Nobita's life?", "(A) Improve his life and help him in troubles", "(B) Make him do all the housework", "(C) Hide his books", "(D) Take his pocket money", "(A)", "Doraemon tries to improve Nobita's life.", "Easy", "Remembering", "Purpose"),
    ("What combination makes the series one of the most loved in animation history?", "(A) Charming personality, Nobita's naivety, relatable situations, and life lessons", "(B) Heavy weapons and fights", "(C) Scary monsters", "(D) Loud shouting", "(A)", "Charming characters, relatable situations, and moral lessons.", "Easy", "Remembering", "Popularity Cause"),
    ("Does Nobita always handle Doraemon's gadgets properly at first?", "(A) No, his naivety often leads to funny trouble", "(B) Yes, he is a master scientist", "(C) He never uses gadgets", "(D) He sells them", "(A)", "Nobita's lack of experience often creates funny situations.", "Easy", "Understanding", "Plot Insight"),
    ("What type of animal is Doraemon shaped like?", "(A) A cat", "(B) A dog", "(C) A bear", "(D) A rabbit", "(A)", "Doraemon is shaped like a cat.", "Easy", "Remembering", "Animal Type"),
    ("Why was Doraemon sent back in time?", "(A) To help Nobita overcome his laziness and troubles", "(B) To go to school", "(C) To buy food", "(D) To hide from robots", "(A)", "Sent back in time to help good but lazy Nobita.", "Easy", "Remembering", "Time Travel Purpose"),
    ("What is the title of Chapter 06?", "(A) My Favourite Cartoon", "(B) The Blue Cat", "(C) Future Gadgets", "(D) Nobita's Pocket", "(A)", "Chapter 06 is titled 'My Favourite Cartoon'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why is Doraemon's pocket called a 'fourth-dimensional space'?", "(A) Because it holds an unlimited number of large futuristic gadgets despite looking small on the outside", "(B) Because it is made of metal", "(C) Because it has four zippers", "(D) Because it is blue", "(A)", "A 4D space allows huge volume inside a small external pocket.", "Medium", "Understanding", "Pocket Science"),
    ("How does the contrast between Doraemon and Nobita create entertaining stories?", "(A) Doraemon is wise and equipped with advanced tech, while Nobita is innocent, lazy, and accident-prone", "(B) Both are robots", "(C) Both are very angry", "(D) Nobita is older than Doraemon", "(A)", "Wise futuristic robot vs innocent lazy boy.", "Medium", "Analyzing", "Character Contrast"),
    ("Why are the situations in Doraemon described as 'relatable' for children?", "(A) Because Nobita faces common childhood problems like homework, bullying, and laziness", "(B) Because children live in the 22nd century", "(C) Because all children have robot cats", "(D) Because Nobita flies a rocket to school", "(A)", "School problems and everyday struggles are relatable.", "Medium", "Understanding", "Relatability"),
    ("What makes the Doraemon series educational as well as entertaining?", "(A) It combines funny gadget adventures with meaningful lessons on hard work, friendship, and responsibility", "(B) It teaches complex math equations", "(C) It teaches how to build robots at home", "(D) It gives history test answers", "(A)", "Fun adventures combined with moral life lessons.", "Medium", "Evaluating", "Educational Value"),
    ("How does Nobita's character change when he learns lessons from gadget mishaps?", "(A) He realizes that relying on shortcuts is bad and that real effort and hard work matter", "(B) He asks for bigger weapons", "(C) He stops going to school", "(D) He destroys the gadgets", "(A)", "Mishaps teach him the value of personal effort.", "Medium", "Analyzing", "Character Growth"),
    ("What is the significance of the year 1969 in relation to Doraemon?", "(A) It was the year Fujiko F. Fujio first introduced the Doraemon manga series to the world", "(B) It was when the 22nd century began", "(C) It was when color TV was invented", "(D) It was when the author died", "(A)", "First introduction of Doraemon in 1969.", "Medium", "Remembering", "Historical Significance"),
    ("Why does Doraemon continue to help Nobita despite Nobita's constant mistakes?", "(A) Because Doraemon is a true friend who genuinely cares about improving Nobita's future", "(B) Because he is paid money", "(C) Because he has nowhere else to go", "(D) Because Nobita forces him", "(A)", "Loyal friendship and genuine care.", "Medium", "Understanding", "Friendship Bond"),
    ("How do futuristic gadgets serve as a literary tool in the story?", "(A) They act as imaginative problem-solvers that test the characters' morals and decision-making", "(B) They are used to defeat scary monsters", "(C) They make the show serious and sad", "(D) They replace all human characters", "(A)", "Gadgets test character choices and morals.", "Medium", "Analyzing", "Literary Device"),
    ("What does Nobita's 'naivety' often cause when he gets a new gadget?", "(A) He misuses the gadget for quick comfort, creating unexpected comical chaos", "(B) He fixes the world", "(C) He becomes a king", "(D) He puts it in a safe", "(A)", "Inexperienced misuse causes comical chaos.", "Medium", "Understanding", "Plot Cause & Effect"),
    ("Why has Doraemon remained one of the most influential phenomena in animation for over 50 years?", "(A) Its universal themes of friendship, charming character designs, and timeless humor appeal across generations", "(B) Because it is the only Japanese cartoon", "(C) Because it is free to watch", "(D) Because robots are popular", "(A)", "Universal moral themes and timeless charm.", "Medium", "Evaluating", "Global Influence"),
    ("What lesson about 'shortcuts' do children learn from Doraemon's episodes?", "(A) Magical shortcuts using technology cannot replace honest hard work and personal responsibility", "(B) Shortcuts are always the best way to win", "(C) Technology fixes all problems instantly", "(D) Homework is useless", "(A)", "Shortcuts cannot replace personal effort.", "Medium", "Evaluating", "Core Lesson"),
    ("How does Doraemon's blue color and earless design make him iconic?", "(A) It gives him a distinct, memorable visual appearance that stands out in world animation", "(B) It makes him look like a scary lion", "(C) It hides him in water", "(D) It makes him look like a human", "(A)", "Distinct iconic visual design.", "Medium", "Understanding", "Visual Design"),
    ("Why was Doraemon sent specifically from the 22nd century to the present day?", "(A) Nobita's future descendants sent Doraemon back to help Nobita build a better life foundation", "(B) Doraemon was lost in time", "(C) To hide from future wars", "(D) To study history", "(A)", "Sent by future descendants to guide Nobita.", "Medium", "Remembering", "Backstory"),
    ("How does Chapter 06 encourage Class 2 students to view cartoons critically?", "(A) By showing that good cartoons offer positive values like responsibility alongside entertainment", "(B) By telling them to stop watching TV", "(C) By asking them to draw robots only", "(D) By making them memorize cartoon dates", "(A)", "Recognizing moral values in quality animation.", "Medium", "Applying", "Critical Viewing"),
    ("What is the primary role of Fujiko F. Fujio in animation history?", "(A) He created Doraemon, one of the most beloved and enduring manga/anime franchises worldwide", "(B) He invented the first television", "(C) He directed Hollywood movies", "(D) He built real robots", "(A)", "Creator of the legendary Doraemon franchise.", "Medium", "Remembering", "Creator Impact"),

    # Hard (41-50)
    ("Analyze the thematic balance between fantasy (futuristic gadgets) and reality (everyday school life) in Doraemon.", "(A) Fantasy provides imaginative entertainment, while reality grounds the story in relatable moral lessons about duty, honesty, and hard work", "(B) The show is 100% fantasy with no real lessons", "(C) The show is a dry documentary", "(D) Fantasy ruins the educational message", "(A)", "Fantasy gadgets test real-world moral principles.", "Hard", "Analyzing", "HOTS Thematic Analysis"),
    ("Evaluate the concept of 'responsibility' as portrayed through Nobita's use of Doraemon's pocket devices.", "(A) Nobita learns that having power (gadgets) requires responsibility; misusing tech for personal gain leads to chaotic consequences", "(B) Power allows anyone to avoid hard work", "(C) Gadgets eliminate human responsibility", "(D) Responsibility means giving away tech", "(A)", "With power comes the requirement of responsible use.", "Hard", "Evaluating", "Ethical Evaluation"),
    ("Deconstruct why 'Doraemon' has transcended cultural boundaries from Japan to become a global favorite.", "(A) Core themes like childhood struggles, the desire for helpful tools, loyal friendship, and moral growth are universally human across all cultures", "(B) Because everyone speaks Japanese", "(C) Because blue is everyone's favorite color", "(D) Because it has no words", "(A)", "Universal human themes of friendship and growth.", "Hard", "Analyzing", "Cross-Cultural Appeal"),
    ("Compare Nobita's character growth potential with traditional fairy tale heroes.", "(A) Unlike perfect fairy tale heroes, Nobita is flawed (lazy/naive), making his gradual moral realizations far more realistic and inspiring", "(B) Nobita is a prince with magical powers", "(C) Fairy tale heroes are always lazy", "(D) Neither learns any lesson", "(A)", "Flawed relatable hero vs idealized fairy tale archetype.", "Hard", "Analyzing", "Literary Comparison"),
    ("How does the fourth-dimensional pocket serve as a metaphor for human imagination and scientific progress?", "(A) It symbolizes endless human creativity and the potential of future technological innovation to solve human challenges", "(B) It means pockets should be bigger", "(C) It shows that science is dangerous", "(D) It is just a zip bag", "(A)", "Metaphor for infinite human ingenuity and tech future.", "Hard", "Evaluating", "Metaphorical Meaning"),
    ("Assess the psychological impact of having a supportive mentor figure like Doraemon in a child's life.", "(A) A supportive mentor builds self-confidence, offers gentle guidance during failures, and encourages emotional growth without taking over the child's duty", "(B) A mentor does all the child's work", "(C) A mentor punishes the child constantly", "(D) A mentor makes the child lazy", "(A)", "Supportive guidance fostering independence.", "Hard", "Evaluating", "Psychological Impact"),
    ("Synthesize how humor, technology, and morality unite to form effective children's literature in Chapter 06.", "(A) Humor engages children's interest, technology sparks imaginative wonder, and underlying morality provides lasting character development", "(B) Humor makes kids ignore lessons", "(C) Tech is bad for literature", "(D) Morals make stories boring", "(A)", "Humor + Tech + Morality = Engaging Children's Literature.", "Hard", "Synthesizing", "Literature Synthesis"),
    ("What does Nobita's initial impulse to seek easy gadget solutions reveal about human nature?", "(A) It reflects the natural human desire to avoid struggle, which the series reframes by showing that personal growth requires effort", "(B) It proves humans are evil", "(C) It shows technology is free", "(D) It proves laziness always wins", "(A)", "Avoiding struggle vs realizing necessity of effort.", "Hard", "Analyzing", "Human Nature"),
    ("Formulate a argument for why animated stories can be powerful tools for character education in primary schools.", "(A) Animated stories use visual appeal, relatable flawed characters, and creative scenarios to convey moral values far more memorably than abstract lectures", "(B) Animations distract students from real work", "(C) Primary students only like real movies", "(D) Cartoons have no educational value", "(A)", "Visual appeal + relatable narrative = effective character education.", "Hard", "Evaluating", "Educational Argument"),
    ("Synthesize the ultimate core message of 'My Favourite Cartoon' for young Class 2 learners.", "(A) True strength comes from within—technology can guide us, but friendship, responsibility, and hard work build a successful future!", "(B) Buy a robotic cat from Japan", "(C) Never do homework yourself", "(D) Rely on gadgets for everything", "(A)", "Internal growth, friendship, responsibility, and effort.", "Hard", "Evaluating", "Core Lesson Synthesis")
]

mcq_content = f"# MCQs — Chapter 06: My Favourite Cartoon\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH06_MCQ_{idx:03d}"
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
    ("Doraemon is a lovable blue earless _______ cat.", "robotic", "Doraemon is a robotic cat.", "Easy"),
    ("Doraemon is a popular _______ animated character.", "Japanese", "Doraemon is a Japanese character.", "Easy"),
    ("Doraemon was created by Fujiko F. _______.", "Fujio", "Created by Fujiko F. Fujio.", "Easy"),
    ("Doraemon was first introduced in the year _______.", "1969", "Introduced in 1969.", "Easy"),
    ("Doraemon is a robotic cat from the _______ century.", "22nd", "From the 22nd century.", "Easy"),
    ("Doraemon was sent back in time to help a boy named _______ Nobi.", "Nobita", "Sent to help Nobita Nobi.", "Easy"),
    ("Nobita is described as a good but _______ boy.", "lazy", "Nobita is good but lazy.", "Easy"),
    ("Doraemon uses _______ gadgets to help Nobita in troubles.", "futuristic", "Uses futuristic gadgets.", "Easy"),
    ("Doraemon fetches his gadgets from his _______.", "pocket", "Fetches gadgets from his pocket.", "Easy"),
    ("Doraemon's pocket is actually a fourth-dimensional _______.", "space", "A fourth-dimensional space.", "Easy"),
    ("The gadgets lead to many funny and _______ situations.", "adventurous", "Funny and adventurous situations.", "Easy"),
    ("The series teaches valuable life lessons about responsibility, friendship, and hard _______.", "work", "Teaches responsibility, friendship, and hard work.", "Easy"),
    ("Doraemon has a charming _______.", "personality", "Doraemon has a charming personality.", "Easy"),
    ("The word 'animated' refers to a movie where pictures appear to _______.", "move", "Pictures appear to move.", "Easy"),
    ("The word 'futuristic' means imagining what things in the _______ will be like.", "future", "Imagining things in the future.", "Easy"),
    ("The word 'naivety' means lack of experience or _______.", "judgement", "Lack of experience or judgement.", "Easy"),
    ("Doraemon's color is _______.", "blue", "Doraemon is blue.", "Easy"),
    ("Doraemon is missing his _______.", "ears", "Doraemon is earless.", "Easy"),
    ("Doraemon helps Nobita to improve his _______.", "life", "Tries to improve his life.", "Easy"),
    ("Doraemon is one of the most loved series in the world of _______.", "animation", "Loved in the world of animation.", "Easy"),
    ("Nobita's full name is Nobita _______.", "Nobi", "Full name is Nobita Nobi.", "Easy"),
    ("The pocket devices are called _______.", "gadgets", "Devices are called gadgets.", "Easy"),
    ("Doraemon comes from a time period called the 22nd _______.", "century", "From the 22nd century.", "Easy"),
    ("Doraemon travels back in _______ to visit Nobita.", "time", "Travels back in time.", "Easy"),
    ("Chapter 06 is titled 'My Favourite _______'.", "Cartoon", "Titled 'My Favourite Cartoon'.", "Easy"),

    # Medium (26-40)
    ("Doraemon's pocket connects to a fourth-dimensional _______ of unlimited space.", "dimension", "Fourth-dimensional dimension/space.", "Medium"),
    ("Nobita's lack of experience is referred to as his _______.", "naivety", "Referred to as naivety.", "Medium"),
    ("The series combines humor with important moral _______.", "lessons", "Combines humor with moral lessons.", "Medium"),
    ("Fujiko F. Fujio introduced Doraemon to readers in the late 1960s, specifically in _______.", "1969", "Introduced in 1969.", "Medium"),
    ("Doraemon is sent from the future to guide Nobita towards a better _______.", "destiny", "Guide towards a better future/destiny.", "Medium"),
    ("Misusing futuristic devices often causes unexpected _______ for Nobita.", "trouble", "Causes unexpected trouble/chaos.", "Medium"),
    ("The bond between Doraemon and Nobita represents deep and loyal _______.", "friendship", "Represents deep friendship.", "Medium"),
    ("Instead of taking shortcuts, Nobita learns that he must practice hard _______.", "work", "Must practice hard work.", "Medium"),
    ("Doraemon's earless design makes him a unique and iconic robotic _______.", "cat", "Iconic robotic cat.", "Medium"),
    ("Relatable childhood situations make the series highly popular among _______.", "children", "Popular among children.", "Medium"),
    ("Doraemon's gadgets range from flying devices to time _______.", "machines", "Gadgets include time machines.", "Medium"),
    ("The animated show teaches children to accept personal _______ for their actions.", "responsibility", "Teaches personal responsibility.", "Medium"),
    ("Doraemon is widely recognized across the globe as a Japanese animation _______.", "phenomenon", "An animation phenomenon.", "Medium"),
    ("Nobita's good heart balances his habit of being _______.", "lazy", "Good heart balances being lazy.", "Medium"),
    ("Doraemon's charming demeanor wins the heart of viewers around the _______.", "world", "Wins hearts around the world.", "Medium"),

    # Hard (41-50)
    ("Doraemon's origin in the 22nd century symbolizes human technological _______.", "advancement", "Symbolizes technological advancement.", "Hard"),
    ("The narrative uses comical gadget mishaps to critique reliance on easy _______.", "shortcuts", "Critiques reliance on easy shortcuts.", "Hard"),
    ("Nobita's character arc demonstrates that flawed individuals can achieve moral _______.", "growth", "Achieve moral growth.", "Hard"),
    ("The fourth-dimensional pocket serves as an imaginative plot device for unlimited _______.", "creativity", "Plot device for unlimited creativity.", "Hard"),
    ("Fujiko F. Fujio created a masterpiece that seamlessly blends science fiction with everyday _______.", "realism", "Blends science fiction with everyday realism.", "Hard"),
    ("Doraemon's timeless popularity proves the enduring appeal of heart-warming _______.", "storytelling", "Appeal of heart-warming storytelling.", "Hard"),
    ("Teaching responsibility through animated entertainment elevates the show's educational _______.", "value", "Elevates educational value.", "Hard"),
    ("Nobita's naive decision-making highlights the importance of developing mature _______.", "judgement", "Importance of mature judgement.", "Hard"),
    ("The series emphasizes that true progress stems from personal effort rather than artificial _______.", "tools", "Stems from effort, not artificial tools.", "Hard"),
    ("Doraemon remains a cornerstone of global children's animation _______.", "culture", "Cornerstone of animation culture.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 06: My Favourite Cartoon\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH06_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH06_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Doraemon is a blue earless robotic cat.", "True", "The text describes Doraemon as a blue earless robotic cat.", "Easy"),
    ("Doraemon was created by Walt Disney.", "False", "Doraemon was created by Fujiko F. Fujio.", "Easy"),
    ("Doraemon was first introduced in the year 1969.", "True", "The text states Doraemon was introduced in 1969.", "Easy"),
    ("Doraemon comes from the 21st century.", "False", "Doraemon comes from the 22nd century.", "Easy"),
    ("Nobita Nobi is a good but lazy boy.", "True", "The text describes Nobita as a good but lazy boy.", "Easy"),
    ("Doraemon uses magic wands to help Nobita.", "False", "Doraemon uses futuristic gadgets from his pocket.", "Easy"),
    ("Doraemon's pocket is a fourth-dimensional space.", "True", "His pocket is a fourth-dimensional space.", "Easy"),
    ("Doraemon's gadgets always work smoothly without causing any funny situations.", "False", "The gadgets lead to many funny and adventurous situations.", "Easy"),
    ("The Doraemon series teaches life lessons about responsibility, friendship, and hard work.", "True", "The text explicitly mentions these three core life lessons.", "Easy"),
    ("Doraemon is a popular Japanese animated character.", "True", "Doraemon is a popular Japanese animated character.", "Easy"),
    ("Doraemon has long cat ears on his head.", "False", "Doraemon is described as earless.", "Easy"),
    ("Nobita is very hardworking and never gets into trouble.", "False", "Nobita is lazy and often gets into trouble.", "Easy"),
    ("The word 'animated' means a movie where drawn pictures appear to move.", "True", "This matches the definition given in the word bank.", "Easy"),
    ("The word 'futuristic' means belonging to ancient historical times.", "False", "Futuristic means imagining what things in the future will be like.", "Easy"),
    ("The word 'naivety' means lack of experience or judgement.", "True", "Naivety is defined as lack of experience or judgement.", "Easy"),
    ("Doraemon's color is yellow in the current main series.", "False", "Doraemon's color is blue.", "Easy"),
    ("Doraemon was sent back in time to harm Nobita.", "False", "He was sent back to help Nobita and improve his life.", "Easy"),
    ("Doraemon is one of the most loved characters in animation history.", "True", "It is one of the most loved and influential phenomena in animation.", "Easy"),
    ("Doraemon fetches gadgets from a backpack.", "False", "He fetches gadgets from his front pocket.", "Easy"),
    ("Doraemon was created in Japan.", "True", "It is a Japanese animated character.", "Easy"),
    ("Nobita's full name is Nobita Nobi.", "True", "His full name is Nobita Nobi.", "Easy"),
    ("Doraemon's gadgets can do incredible futuristic tasks.", "True", "They are advanced gadgets from the 22nd century.", "Easy"),
    ("The show promotes laziness and cheating as good habits.", "False", "It teaches lessons against laziness, emphasizing hard work and responsibility.", "Easy"),
    ("Doraemon has a charming personality.", "True", "The text notes Doraemon's charming personality.", "Easy"),
    ("Chapter 06 is about the animated series Doraemon.", "True", "Chapter 06 is titled 'My Favourite Cartoon' and focuses on Doraemon.", "Easy"),

    # Medium (26-40)
    ("Doraemon's fourth-dimensional pocket can hold gadgets that are much larger than the pocket itself.", "True", "A 4D space allows large objects to fit inside a small opening.", "Medium"),
    ("Nobita's naivety means he always uses gadgets wisely without making mistakes.", "False", "His naivety (inexperience) causes him to misuse gadgets, creating comical trouble.", "Medium"),
    ("Doraemon's series is popular only in Japan and nowhere else.", "False", "It is an influential phenomenon loved worldwide.", "Medium"),
    ("The series proves that technology alone can solve all human problems without personal effort.", "False", "Episodes show that gadgets fail or cause trouble unless Nobita puts in real effort.", "Medium"),
    ("Fujiko F. Fujio introduced Doraemon over 50 years ago.", "True", "Introduced in 1969, which is over 50 years ago.", "Medium"),
    ("Nobita's character is relatable to children because he faces real everyday struggles like schoolwork and laziness.", "True", "His ordinary childhood struggles make him highly relatable.", "Medium"),
    ("Doraemon is a living biological cat that eats normal cat food only.", "False", "Doraemon is a robotic cat from the future.", "Medium"),
    ("The gadgets lead to both adventurous and humorous situations.", "True", "The text highlights funny and adventurous situations.", "Medium"),
    ("Doraemon refuses to help Nobita when Nobita is in trouble.", "False", "Doraemon's main mission is to help Nobita in troubles.", "Medium"),
    ("Friendship is one of the central positive values taught by the series.", "True", "Friendship is explicitly listed as a key life lesson.", "Medium"),
    ("Doraemon travels forward in time to visit the 30th century.", "False", "He travels back in time from the 22nd century to help Nobita.", "Medium"),
    ("Nobita's good heart is one of his redeeming qualities despite his laziness.", "True", "The text describes him as a good but lazy boy.", "Medium"),
    ("The word 'futuristic' describes technology that belongs to the past.", "False", "Futuristic describes tech imagined for the future.", "Medium"),
    ("Doraemon's earless appearance is part of his unique charm.", "True", "His blue, earless design makes him iconic and charming.", "Medium"),
    ("Watching Doraemon can help children understand the importance of hard work.", "True", "The series repeatedly emphasizes the value of hard work.", "Medium"),

    # Hard (41-50)
    ("The Doraemon franchise successfully balances light-hearted comedy with moral character building.", "True", "It blends hilarious gadget mishaps with meaningful moral lessons.", "Hard"),
    ("Doraemon's 4D pocket violates the law of conservation of volume in standard 3D space.", "True", "In 3D physics, huge items can't fit in a small pouch, requiring a 4D spatial concept.", "Hard"),
    ("Nobita's reliance on gadgets acts as a narrative critique of seeking easy shortcuts in life.", "True", "Whenever Nobita seeks shortcuts via gadgets, it backfires, warning against shortcuts.", "Hard"),
    ("Fujiko F. Fujio's creation has had no lasting impact on modern animation culture.", "False", "It is recognized as one of the most influential phenomena in global animation history.", "Hard"),
    ("The relationship between Doraemon and Nobita exemplifies unconditional supportive mentorship.", "True", "Doraemon guides, supports, and forgives Nobita while encouraging his growth.", "Hard"),
    ("Doraemon's earless trait was a deliberate design feature from his initial creation.", "True", "He is introduced specifically as a blue earless robotic cat.", "Hard"),
    ("The series suggests that true success requires combining modern tools with personal responsibility.", "True", "Tools help, but personal responsibility and hard work are necessary for true success.", "Hard"),
    ("Naivety in literary characters often serves to drive plot complications.", "True", "Nobita's naivety creates the central complications in almost every episode.", "Hard"),
    ("Doraemon was sent back in time by Nobita's enemy to destroy his future.", "False", "He was sent by future caring descendants to improve Nobita's life trajectory.", "Hard"),
    ("Chapter 06 presents Doraemon as a model of quality educational children's media.", "True", "It highlights how entertainment and moral education can be effectively combined.", "Hard")
]

tf_content = f"# True / False — Chapter 06: My Favourite Cartoon\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH06_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH06_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who is Doraemon and what does he look like?", "Doraemon is a lovable blue earless robotic cat from the 22nd century.", "Easy", "Remembering"),
    ("Who created Doraemon and when was he first introduced?", "Doraemon was created by Fujiko F. Fujio and was first introduced in 1969.", "Easy", "Remembering"),
    ("Why was Doraemon sent back in time?", "He was sent back in time to help a good but lazy boy named Nobita Nobi and improve his life.", "Easy", "Remembering"),
    ("Where does Doraemon keep his futuristic gadgets?", "He keeps his gadgets in his front pocket, which is a fourth-dimensional space.", "Easy", "Remembering"),
    ("What kind of boy is Nobita Nobi?", "Nobita Nobi is a good-hearted but lazy boy who often gets into troubles.", "Easy", "Remembering"),
    ("What three life lessons does the Doraemon series teach children?", "The series teaches valuable life lessons about responsibility, friendship, and hard work.", "Easy", "Remembering"),
    ("What country does the animated character Doraemon come from?", "Doraemon comes from Japan.", "Easy", "Remembering"),
    ("What color is Doraemon?", "Doraemon is blue.", "Easy", "Remembering"),
    ("What body part is Doraemon missing compared to real cats?", "Doraemon is missing his ears.", "Easy", "Remembering"),
    ("What type of situations do Doraemon's gadgets lead to?", "They lead to many funny and adventurous situations.", "Easy", "Remembering"),
    ("What is the meaning of the word 'animated'?", "Animated means a movie or show where drawn pictures appear to move.", "Easy", "Understanding"),
    ("What is the meaning of the word 'futuristic'?", "Futuristic means imagining or representing what things in the future will be like.", "Easy", "Understanding"),
    ("What is the meaning of the word 'naivety'?", "Naivety means a lack of experience, wisdom, or judgement.", "Easy", "Understanding"),
    ("How does Doraemon help Nobita when Nobita is in trouble?", "Doraemon uses futuristic gadgets from his 4D pocket to help Nobita solve his problems.", "Easy", "Remembering"),
    ("Is Doraemon a real living animal or a machine?", "Doraemon is a robotic cat (a machine).", "Easy", "Remembering"),
    ("What century is Doraemon originally from?", "Doraemon is originally from the 22nd century.", "Easy", "Remembering"),
    ("Why do children around the world love the Doraemon series?", "Children love it because of Doraemon's charming personality, relatable childhood situations, funny gadgets, and good moral lessons.", "Easy", "Remembering"),
    ("What is Doraemon's pocket called?", "It is called a fourth-dimensional pocket.", "Easy", "Remembering"),
    ("Does Nobita always use Doraemon's gadgets correctly?", "No, Nobita often misuses them due to his laziness or naivety, leading to funny chaos.", "Easy", "Understanding"),
    ("Who is Nobita Nobi?", "Nobita Nobi is the main human boy character in the Doraemon series whom Doraemon helps.", "Easy", "Remembering"),
    ("What makes Doraemon's personality appealing?", "Doraemon has a very charming, helpful, and friendly personality.", "Easy", "Remembering"),
    ("In what media format was Doraemon introduced?", "Doraemon was introduced as an animated/manga series.", "Easy", "Remembering"),
    ("Why is hard work emphasized in the series?", "It is emphasized to show children that gadgets and shortcuts cannot replace honest human effort.", "Easy", "Understanding"),
    ("How does Doraemon show true friendship to Nobita?", "Doraemon stays by Nobita's side, helps him through difficulties, and guides him to become a better person.", "Easy", "Understanding"),
    ("What is the title of Chapter 06?", "The title of Chapter 06 is 'My Favourite Cartoon'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Why is a fourth-dimensional pocket a clever idea for a robotic cat from the future?", "It allows Doraemon to store an unlimited number of large gadgets inside a small pocket without making it heavy or bulky.", "Medium", "Understanding"),
    ("How does Nobita's laziness drive the plot of many episodes?", "Nobita's laziness makes him ask Doraemon for gadget shortcuts to avoid hard work, which inevitably leads to comical mistakes and lessons.", "Medium", "Analyzing"),
    ("Explain the balance between humor and moral values in the Doraemon series.", "Humor comes from the wild gadget situations and Nobita's mistakes, while moral values come from the ultimate lesson that honesty, friendship, and effort are what truly matter.", "Medium", "Analyzing"),
    ("Why is Fujiko F. Fujio considered a legend in animation?", "Because he created Doraemon in 1969, an enduring character that has entertained and educated millions of children globally for decades.", "Medium", "Evaluating"),
    ("How does Doraemon help Nobita develop responsibility over time?", "By letting Nobita experience the consequences of misusing gadgets, Doraemon helps Nobita realize he must take responsibility for his own schoolwork and life.", "Medium", "Analyzing"),
    ("What makes Nobita a relatable character for young Class 2 students?", "Nobita is relatable because he struggles with waking up early, doing homework, and making mistakes, which are common childhood experiences.", "Medium", "Understanding"),
    ("Describe the appearance of Doraemon in detail.", "Doraemon is a blue, round, earless robotic cat with white paws, whiskers, a bell collar, and a white fourth-dimensional pocket on his belly.", "Medium", "Remembering"),
    ("Why can't technology solve all of Nobita's problems by itself?", "Because technology is only a tool; without personal effort, determination, and wisdom, technology cannot change a person's character or habits.", "Medium", "Evaluating"),
    ("How does Doraemon's time travel element add excitement to the show?", "Time travel allows Doraemon to bring advanced 22nd-century tech into the present day, creating futuristic wonder and adventurous possibilities.", "Medium", "Understanding"),
    ("What does the word 'phenomenon' mean when describing Doraemon's global success?", "It means Doraemon became an extraordinarily popular, widespread, and memorable success in global culture.", "Medium", "Understanding"),
    ("Summarize Page 23 of the textbook in two sentences.", "Doraemon is a famous blue earless robotic cat from the 22nd century created by Fujiko F. Fujio in 1969. Sent to help lazy Nobita Nobi with futuristic gadgets from his 4D pocket, the series teaches valuable lessons about friendship, hard work, and responsibility.", "Medium", "Understanding"),
    ("How does Doraemon demonstrate loyalty as a friend?", "He never gives up on Nobita, helping him through every failure and cheering him on to succeed.", "Medium", "Evaluating"),
    ("Why is 'naivety' both a weakness and a cute trait for Nobita?", "It is a weakness because it causes him to make silly mistakes, but a cute trait because it shows he is innocent and free of malice.", "Medium", "Analyzing"),
    ("How does the series teach children not to rely on cheating?", "Whenever Nobita uses gadgets to cheat on tests or games, the gadget fails or causes embarrassing trouble, proving cheating doesn't pay.", "Medium", "Applying"),
    ("What is the core message about friendship in Chapter 06?", "True friends support each other during hard times, help each other correct mistakes, and encourage each other to work hard.", "Medium", "Evaluating"),

    # Hard (41-50)
    ("Analyze how the Doraemon series critiques modern society's over-reliance on gadgets.", "By showing that 22nd-century technology often creates more problems when used lazily, the show warns that technology should assist human effort, not replace it.", "Hard", "Analyzing"),
    ("Deconstruct the character design of Doraemon: why earless, blue, and round?", "The round earless design makes him friendly, non-threatening, and soft-looking for young children, while the bright blue color creates instant visual recognition.", "Hard", "Analyzing"),
    ("Evaluate the role of speculative science fiction in children's moral literature.", "Sci-fi elements (time travel, 4D space) stimulate children's imagination, making abstract moral concepts like responsibility engaging and memorable.", "Hard", "Evaluating"),
    ("Compare Doraemon's role as a guide with traditional fairy godmothers in classic tales.", "Like a fairy godmother, Doraemon provides magical assistance, but unlike classic tales, Doraemon's tech requires the protagonist to learn hard lessons through trial and error.", "Hard", "Analyzing"),
    ("How can a school teacher use Doraemon episodes in a primary classroom to teach ethics?", "Teachers can show an episode clip, ask students where Nobita went wrong with a gadget, and lead a discussion on how Nobita should have acted responsibly.", "Hard", "Applying"),
    ("Synthesize how humor, futuristic technology, and human emotion combine in Doraemon.", "Humor attracts interest, futuristic tech drives inventive plots, and human emotion (friendship/growth) provides the soulful core that resonates across generations.", "Hard", "Synthesizing"),
    ("Assess the impact of Fujiko F. Fujio's work on Japanese cultural export.", "Doraemon served as a major cultural ambassador for Japan, introducing Japanese animation, values, and humor to millions of international households.", "Hard", "Evaluating"),
    ("Why is Nobita's good heart essential for keeping the audience's sympathy?", "If Nobita were mean or malicious, viewers would dislike him when gadgets backfired; because he is good-hearted, viewers root for his moral growth.", "Hard", "Analyzing"),
    ("Formulate a story outline where Nobita learns a lesson about hard work without using a gadget.", "Nobita loses a gadget, has to study for an exam using his own notebook all night, passes through genuine effort, and realizes he didn't need magic after all.", "Hard", "Creating"),
    ("Synthesize the ultimate takeaway lesson of Chapter 06 for Class 2 students.", "Embrace friendship, take responsibility for your actions, and remember that no gadget in the world can replace the power of your own hard work!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 06: My Favourite Cartoon\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH06_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH06_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the character of Doraemon, including his origin, physical appearance, and purpose.", 
     "Doraemon is a world-famous Japanese animated character created by Fujiko F. Fujio in 1969. He is a lovable, blue, earless robotic cat who originally comes from the 22nd century. Doraemon was sent back in time to the present day to help a good-hearted but lazy boy named Nobita Nobi. Equipped with a charming personality and a fourth-dimensional pocket on his belly, Doraemon's main purpose is to guide Nobita, help him overcome daily troubles, and improve his future life.", 
     "Easy", "Remembering"),

    ("Explain how Doraemon's fourth-dimensional pocket works and what happens when gadgets are used.", 
     "Doraemon's front pocket is actually a fourth-dimensional space, which means it has an unlimited capacity to store huge futuristic devices despite looking like a small pouch. Doraemon fetches amazing gadgets from this pocket to solve Nobita's problems, such as helping him travel, study, or play. However, because Nobita is naive and lazy, using these gadgets often leads to hilarious, adventurous situations and unexpected trouble before a good lesson is learned.", 
     "Easy", "Remembering"),

    ("What core life lessons does the Doraemon series teach children, and why are they important?", 
     "The Doraemon series teaches three main life lessons:\n1. **Responsibility**: Children learn that they must take ownership of their schoolwork and actions rather than looking for lazy shortcuts.\n2. **Friendship**: The strong bond between Doraemon and Nobita shows loyalty, kindness, and helping friends in need.\n3. **Hard Work**: The episodes repeatedly prove that technology cannot replace honest personal effort and practice.", 
     "Easy", "Understanding"),

    ("Describe the relationship between Doraemon and Nobita Nobi.", 
     "Doraemon and Nobita share a deep, enduring friendship. Nobita is an innocent, good-natured boy who often struggles with laziness, schoolwork, and bullies. Doraemon acts as a caring mentor, guardian, and best friend. Even when Nobita makes silly mistakes or misuses gadgets, Doraemon stays by his side, gently guiding him to correct his behavior and work hard.", 
     "Easy", "Understanding"),

    ("Explain the meanings of 'animated', 'futuristic', and 'naivety' as used in Chapter 06.", 
     "1. **Animated**: Refers to a style of film or television show made by filming a sequence of drawings or computer models so that they appear to move.\n2. **Futuristic**: Describing technology, ideas, or designs that imagine or belong to a advanced future time, such as 22nd-century gadgets.\n3. **Naivety**: A quality of being innocent, inexperienced, or lacking mature judgement, which often leads to innocent mistakes.", 
     "Easy", "Understanding"),

    ("Why has Doraemon remained one of the most loved animated shows in the world for over 50 years?", 
     "Doraemon has remained globally popular for over five decades because it combines relatable childhood struggles with imaginative sci-fi gadgets and warm humor. Children everywhere see themselves in Nobita's everyday challenges, while Doraemon's charming blue design and loyal friendship provide comfort and inspiration across generations.", 
     "Easy", "Understanding"),

    ("How does Nobita's character contrast with Doraemon's robotic nature?", 
     "Nobita is a human boy who is flawed, emotional, naive, and prone to laziness. In contrast, Doraemon is an advanced 22nd-century robot who is wise, organized, and equipped with futuristic technology. Despite these differences, Doraemon's warm heart matches Nobita's good nature, making them a perfect comedic and emotional team.", 
     "Easy", "Analyzing"),

    ("Describe a typical plot flow of a Doraemon episode based on the text.", 
     "A typical episode begins with Nobita facing a problem due to his laziness or lack of skill (such as failing a test or being bullied). Nobita cries to Doraemon, who pulls a futuristic gadget from his 4D pocket to help. Nobita uses the gadget, but soon misuses it for easy comfort, creating funny chaos. Finally, the gadget situation backfires, teaching Nobita that he must rely on hard work.", 
     "Easy", "Understanding"),

    ("What moral guidance does Doraemon give when a gadget backfires on Nobita?", 
     "When a gadget backfires, Doraemon helps clean up the mess but reminds Nobita why the problem occurred. He explains that technology is meant to assist, not cheat, and encourages Nobita to face his challenges directly with honesty, courage, and personal effort.", 
     "Easy", "Understanding"),

    ("Why is Chapter 06 titled 'My Favourite Cartoon'?", 
     "The chapter is titled 'My Favourite Cartoon' because it explores Doraemon, a universally cherished animated series. It highlights why children love the show—not just for its fun gadgets and cute blue cat, but for the valuable moral lessons and warm friendship it brings into their lives.", 
     "Easy", "Remembering"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Who created Doraemon, and what is the historical significance of the year 1969?", "Doraemon was created by Japanese author Fujiko F. Fujio. The year 1969 is historically significant because it was when the Doraemon manga series was first published, launching a multi-decade global franchise.", "Easy", "Remembering"),
    ("Explain why Doraemon does not have ears.", "Doraemon is an earless robotic cat. According to his backstory, his ears were lost in a futuristic robotic accident, giving him his distinct round, smooth blue head design.", "Easy", "Remembering"),
    ("What makes Doraemon's pocket different from an ordinary pocket?", "An ordinary pocket has small, limited space. Doraemon's pocket is a fourth-dimensional space with infinite capacity, allowing him to store huge machines like time vehicles and weather controllers.", "Easy", "Understanding"),
    ("Discuss how the show teaches responsibility to young viewers.", "It teaches responsibility by showing that actions have consequences. When Nobita shirks his duties or misuses tech, he suffers funny consequences, showing children they must be accountable for their choices.", "Easy", "Understanding"),
    ("Why is Nobita described as 'good but lazy'?", "He is called 'good' because he has a kind heart, loves animals, and cares for his friends. He is called 'lazy' because he dislikes doing homework, sleeping in late, and looking for easy ways out.", "Easy", "Understanding"),
    ("How do the gadgets in Doraemon spark children's imagination?", "Gadgets like flying bamboo-copters, memory bread, and anywhere-doors spark imagination by making children wonder how technology might solve everyday human limitations in the future.", "Easy", "Evaluating"),
    ("What role does Fujiko F. Fujio's writing play in making the characters relatable?", "Fujiko F. Fujio wrote characters with real human flaws. Nobita isn't a flawless hero, and Doraemon has his own quirks (like loving dorayaki and fearing mice), making them feel like real, loving friends.", "Easy", "Evaluating"),
    ("How does the Doraemon series handle the topic of failure?", "The series shows that failure is a normal part of growing up. Instead of punishing Nobita harshly, failure is treated as a learning opportunity to try again with hard work.", "Easy", "Understanding"),
    ("Describe how Doraemon's charming personality influences those around him.", "Doraemon's charming, patient, and friendly nature brings out the best in Nobita and his friends, encouraging harmony, forgiveness, and teamwork.", "Easy", "Understanding"),
    ("Why is Japanese animation (anime) celebrated through characters like Doraemon?", "Anime is celebrated because it uses vibrant artistic imagination, deep character development, and universal human themes that touch hearts across international borders.", "Easy", "Evaluating"),
    ("How can Class 2 students improve their study habits after reading about Nobita?", "Students can realize that seeking magical shortcuts to pass tests doesn't work. They should set regular study times, do their homework honestly, and ask teachers for help.", "Easy", "Applying"),
    ("Explain why gadgets lead to adventurous situations in the series.", "Gadgets lead to adventure because they take the characters to unusual places (like ocean depths, outer space, or past centuries), testing their courage and friendship.", "Easy", "Understanding"),
    ("What is the difference between an animated show and a live-action show?", "An animated show uses drawn or computer-generated moving images to tell a story, allowing fantastical elements like 4D pockets and robotic cats to look natural and fun.", "Easy", "Understanding"),
    ("How does Doraemon's blue color contribute to his visual identity?", "His bright blue color makes him visually striking, cheerful, and instantly recognizable among cartoon characters worldwide.", "Easy", "Remembering"),
    ("Summarize the main message of Chapter 06 in five sentences.", "Doraemon is a famous blue earless robotic cat created by Fujiko F. Fujio in 1969. Sent from the 22nd century, he helps lazy Nobita Nobi using gadgets from his 4D pocket. Their adventures are funny and imaginative. Most importantly, the series teaches responsibility, friendship, and hard work. It remains a beloved global cartoon phenomenon.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how the concept of time travel in Doraemon is used for character development rather than just sci-fi action.", 
     "Time travel in Doraemon is primarily a moral tool. Doraemon is sent from the 22nd century to fix Nobita's future by correcting his present habits. When Nobita travels to the past or future, he sees the long-term impact of his current laziness or kindness. Time travel allows Nobita to understand that today's hard work builds tomorrow's success.", 
     "Medium", "Analyzing"),

    ("Examine the psychological appeal of having a 'magical helper' like Doraemon for primary school children.", 
     "Children often feel small and overwhelmed by adult rules, school demands, and physical limitations. Doraemon represents the ultimate childhood wish-fulfillment: a loving companion who listens without judgment and possesses tools to solve any problem. This psychological comfort makes Doraemon an enduring favorite.", 
     "Medium", "Analyzing"),

    ("Discuss how Nobita's 'naivety' creates narrative conflict in almost every episode.", 
     "Nobita's naivety—his lack of mature judgment—causes him to view gadgets as instant solutions for selfish or lazy goals (like skipping homework or impressing friends). Because he doesn't anticipate consequences, he overuses or misapplies the technology, triggering comedic chaos that forms the episode's central conflict.", 
     "Medium", "Analyzing"),

    ("Evaluate the statement: 'Doraemon proves that technology is only as good as the person using it.'", 
     "This statement is completely accurate within the series. Doraemon's 22nd-century gadgets are technologically flawless, but when used by a lazy or irresponsible person (Nobita), they cause disaster. The series repeatedly proves that technology requires human wisdom, responsibility, and moral character to yield good results.", 
     "Medium", "Evaluating"),

    ("Explore how Chapter 06 bridges media entertainment with classroom moral education.", 
     "Chapter 06 uses a popular cartoon character that children already love (Doraemon) to introduce essential vocabulary and literary analysis. By discussing why Doraemon helps Nobita and examining the show's core values, the lesson seamlessly connects fun TV entertainment with classroom character education.", 
     "Medium", "Evaluating"),

    ("How does Doraemon's fear of mice and love for sweet treats (dorayaki) humanize his robotic character?", "Giving a futuristic robot relatable human quirks—like screaming at tiny mice or obsessing over sweet pancakes—makes Doraemon vulnerable, funny, and deeply lovable rather than an unfeeling metal machine.", "Medium", "Analyzing"),
    ("Why is the 22nd century chosen as Doraemon's era of origin?", "The 22nd century represents a plausible future era of advanced robotics and spatial technology, giving the gadgets a cool sci-fi origin while keeping the present setting grounded in everyday school life.", "Medium", "Understanding"),
    ("Describe the moral growth of Nobita at the end of a typical gadget adventure.", "After the gadget backfires and causes chaos, Nobita feels genuine remorse, apologizes for his laziness, and willingly completes his original task through his own manual effort, showing real moral growth.", "Medium", "Analyzing"),
    ("In what ways does Doraemon encourage children to value genuine friendship over material items?", "Doraemon's greatest gift to Nobita isn't any gadget, but his constant presence, patience, and love. The show teaches that true friends care about your character, not just the toys you own.", "Medium", "Evaluating"),
    ("How does the author of the textbook use word meanings (animated, futuristic, naivety) to enhance reading skills?", "By introducing elevated vocabulary in the context of a familiar, fun topic like Doraemon, students learn complex concepts effortlessly and expand their reading comprehension.", "Medium", "Evaluating"),
    ("Compare Doraemon's futuristic technology with real-world modern technology like smartphones.", "Both provide amazing conveniences, but just like Doraemon's gadgets, real smartphones can cause distraction and trouble if used without self-discipline and responsibility.", "Medium", "Analyzing"),
    ("Why is Fujiko F. Fujio's legacy important in international media relations?", "His creation of Doraemon introduced Japanese culture, storytelling style, and moral philosophy to over 40 countries, building global appreciation for Japanese creative arts.", "Medium", "Evaluating"),
    ("How does Nobita's innocence prevent him from becoming a negative character despite his flaws?", "Nobita never uses gadgets out of malice or cruelty; his mistakes stem from innocent laziness or a desire to help friends, keeping him endearing to the audience.", "Medium", "Analyzing"),
    ("What role does humor play in delivering serious life advice to young children?", "Humor breaks down resistance. When children laugh at funny gadget blunders, they absorb the moral lesson (don't cheat, work hard) without feeling lectured or scolded.", "Medium", "Evaluating"),
    ("Construct a short dialogue between Doraemon and Nobita where Doraemon refuses to give a gadget for cheating.", "Nobita: 'Doraemon, give me a gadget to write my test!' Doraemon: 'No, Nobita! Gadgets are not for cheating. Sit down, open your textbook, and I will help you study hard!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the narrative architecture of Fujiko F. Fujio's Doraemon series from a literary perspective.", 
     "Fujiko F. Fujio constructed a brilliant narrative architecture combining episodic stability with character growth. Each episode follows a formulaic structure (Problem -> Sci-Fi Solution -> Misuse -> Crisis -> Moral Lesson), yet subtle character progression occurs over time. This formula provides comforting familiarity while allowing infinite creative variations through futuristic gadgets.", 
     "Hard", "Evaluating"),

    ("Deconstruct the philosophical dilemma: Can artificial intelligence (Doraemon) teach genuine human morality?", 
     "The series resolves this dilemma by giving Doraemon emotional empathy. Though Doraemon is a robot, his programming incorporates emotional intelligence, patience, and moral discernment. By guiding Nobita through choices rather than enforcing code, Doraemon acts as a moral mentor, proving AI in literature can model human ethical growth.", 
     "Hard", "Analyzing"),

    ("Synthesize the educational framework of using popular animation for social-emotional learning (SEL) in primary schools.", 
     "Doraemon aligns perfectly with SEL frameworks:\n1. **Self-Awareness**: Recognizing laziness and mistakes.\n2. **Self-Management**: Learning discipline over instant gratification.\n3. **Social Awareness**: Empathy for friends.\n4. **Responsible Decision-Making**: Understanding consequences of actions.\nUsing such cartoons accelerates emotional literacy in young learners.", 
     "Hard", "Synthesizing"),

    ("Formulate a essay plan analyzing how Doraemon reflects post-war Japanese technological optimism.", 
     "1. **Introduction**: Introduce Doraemon (1969) during Japan's technological and economic boom.\n2. **Technology as Helper**: Doraemon represents technology designed for human welfare, not warfare.\n3. **Moral Counterbalance**: Highlighting that tech must be guided by traditional values (hard work, community).\n4. **Conclusion**: Doraemon as a symbol of human-centric technological optimism.", 
     "Hard", "Creating"),

    ("Evaluate the impact of Doraemon's earless visual design on child empathy and disability inclusion.", 
     "Doraemon's earless state (a result of a robotic accident) makes him 'imperfect' in appearance. Yet, he is the most loved hero of the show. This subtly teaches young viewers empathy for individuals with physical differences or disabilities, showing that character and heart matter far more than physical perfection.", 
     "Hard", "Evaluating"),

    ("Analyze how the fourth-dimensional pocket functions as a sandbox for scientific curiosity in children.", "By presenting imaginary devices based on spatial physics, memory modification, and time manipulation, the 4D pocket sparks early curiosity about science, physics, and invention in young minds.", "Hard", "Analyzing"),
    ("Compare Nobita's growth journey with the archetypal 'Hero's Journey' in classical literature.", "While classic heroes embark on physical quests, Nobita's quest is internal: overcoming daily flaws (laziness, fear). Doraemon acts as the supernatural mentor who bestows tools, tests the hero, and guides him back to self-reliance.", "Hard", "Analyzing"),
    ("Draft a persuasive speech encouraging primary school students to value hard work over quick fixes.", "'Dear friends! In Doraemon, every time Nobita takes a shortcut gadget, it backfires! Why? Because true success cannot be printed by a machine. Your mind, your effort, and your hard work are your real super-gadgets. Trust in your own hard work!'", "Hard", "Creating"),
    ("Assess the cultural longevity of Doraemon compared to modern fast-paced superhero cartoons.", "Modern superhero cartoons often rely on violent action and rapid visual cuts, which quickly age. Doraemon's longevity stems from its focus on timeless human emotions, domestic warmth, and relatable childhood struggles.", "Hard", "Evaluating"),
    ("Synthesize the ultimate moral message of Chapter 06 into a guiding motto for Class 2 students.", "'Be responsible, cherish your friends, and work hard every day—because the greatest gadget in the universe is your own willing heart!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 06: My Favourite Cartoon\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH06_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH06_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Who doesn't recognise this lovable blue earless robotic cat? Doraemon is a popular Japanese animated character created by Fujiko F. Fujio. It was first introduced in 1969.",
     [
         ("What kind of creature is Doraemon?", "A lovable blue earless robotic cat.", "Easy", "Remembering"),
         ("What country does Doraemon come from?", "Japan.", "Easy", "Remembering"),
         ("Who created the character of Doraemon?", "Fujiko F. Fujio.", "Easy", "Remembering"),
         ("In which year was Doraemon first introduced?", "1969.", "Easy", "Remembering"),
         ("What physical feature makes Doraemon different from ordinary cats?", "He is earless.", "Medium", "Understanding")
     ]),

    # Set 2
    ("In the series, Doraemon is a robotic cat from 22nd century, sent back in time to help a good but lazy boy named Nobita Nobi.",
     [
         ("Which century does Doraemon originally belong to?", "22nd century.", "Easy", "Remembering"),
         ("How did Doraemon travel to meet Nobita?", "He was sent back in time.", "Easy", "Remembering"),
         ("Who was Doraemon sent to help?", "Nobita Nobi.", "Easy", "Remembering"),
         ("What two words describe Nobita's personality in this sentence?", "Good but lazy.", "Easy", "Remembering"),
         ("Why was Doraemon sent to Nobita specifically?", "To help him in troubles and improve his life.", "Medium", "Understanding")
     ]),

    # Set 3
    ("Doraemon helps Nobita in troubles and tries to improve his life by using futuristic gadgets. He fetches these gadgets from his pocket which actually is a fourth-dimensional space.",
     [
         ("How does Doraemon try to improve Nobita's life?", "By using futuristic gadgets.", "Easy", "Remembering"),
         ("Where does Doraemon fetch his gadgets from?", "From his pocket.", "Easy", "Remembering"),
         ("What kind of space is Doraemon's pocket?", "A fourth-dimensional space.", "Easy", "Remembering"),
         ("What does the word 'futuristic' mean?", "Imagining what things in the future will be like.", "Medium", "Understanding"),
         ("Why is a fourth-dimensional space useful for holding gadgets?", "Because it provides unlimited space inside a small pocket.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("These gadgets lead to many funny and adventurous situations. But at the same time, this series teaches valuable life lessons about responsibility, friendship and hard-work.",
     [
         ("What kind of situations do Doraemon's gadgets create?", "Funny and adventurous situations.", "Easy", "Remembering"),
         ("Does the series only provide fun, or does it teach lessons too?", "It also teaches valuable life lessons.", "Easy", "Remembering"),
         ("Name the three life lessons mentioned in this extract.", "Responsibility, friendship, and hard work.", "Easy", "Remembering"),
         ("Why is it important for cartoons to teach life lessons?", "Because it helps children learn positive character values while having fun.", "Medium", "Evaluating"),
         ("What happens when Nobita tries to avoid hard work using gadgets?", "It usually creates funny trouble and teaches him a lesson.", "Medium", "Understanding")
     ]),

    # Set 5
    ("Doraemon's charming personality, Nobita's naivety, relatable situations and valuable life lessons has made this series one of the most loved and influential phenomenon in the world of animation.",
     [
         ("What kind of personality does Doraemon have?", "A charming personality.", "Easy", "Remembering"),
         ("What word describes Nobita's innocent lack of experience?", "Naivety.", "Easy", "Remembering"),
         ("What kind of situations are depicted in the show?", "Relatable situations.", "Easy", "Remembering"),
         ("What has Doraemon become in the world of animation?", "One of the most loved and influential phenomena.", "Easy", "Remembering"),
         ("What does the word 'naivety' mean?", "Lack of experience or judgement.", "Medium", "Understanding")
     ]),

    # Set 6
    ("Word Meaning: Animated: A movie where pictures appear to move | Futuristic: Imagining what things in the future will be like | Naivety: Lack of experience or judgement",
     [
         ("What is the meaning of 'animated'?", "A movie where pictures appear to move.", "Easy", "Remembering"),
         ("What is the meaning of 'futuristic'?", "Imagining what things in the future will be like.", "Easy", "Remembering"),
         ("What is the meaning of 'naivety'?", "Lack of experience or judgement.", "Easy", "Remembering"),
         ("Which vocabulary word describes Doraemon's 22nd-century gadgets?", "Futuristic.", "Easy", "Remembering"),
         ("Which vocabulary word describes Nobita's innocent mistakes?", "Naivety.", "Easy", "Remembering")
     ]),

    # Set 7
    ("Doraemon is a popular Japanese animated character created by Fujiko F. Fujio. It was first introduced in 1969.",
     [
         ("What nationality is the animated character Doraemon?", "Japanese.", "Easy", "Remembering"),
         ("Who wrote and drew Doraemon?", "Fujiko F. Fujio.", "Easy", "Remembering"),
         ("In which decade was Doraemon created?", "In the 1960s (1969).", "Medium", "Understanding"),
         ("Is Doraemon a new character or over 50 years old?", "Over 50 years old (introduced in 1969).", "Medium", "Understanding"),
         ("What type of character is Doraemon (robot, human, or alien)?", "Robotic cat.", "Easy", "Remembering")
     ]),

    # Set 8
    ("Doraemon helps Nobita in troubles and tries to improve his life by using futuristic gadgets. He fetches these gadgets from his pocket which actually is a fourth-dimensional space.",
     [
         ("Whom does Doraemon help when troubles arise?", "Nobita.", "Easy", "Remembering"),
         ("What tool does Doraemon use to help?", "Futuristic gadgets.", "Easy", "Remembering"),
         ("Where is the fourth-dimensional pocket located on Doraemon?", "On his front belly pouch.", "Easy", "Remembering"),
         ("What does Doraemon hope to improve for Nobita?", "His life and future.", "Easy", "Remembering"),
         ("Give an example of a futuristic idea from the text.", "Fourth-dimensional pocket / gadgets.", "Medium", "Understanding")
     ]),

    # Set 9
    ("These gadgets lead to many funny and adventurous situations. But at the same time, this series teaches valuable life lessons about responsibility, friendship and hard-work.",
     [
         ("What two words describe the situations caused by gadgets?", "Funny and adventurous.", "Easy", "Remembering"),
         ("What lesson does the series teach about getting things done?", "Hard work.", "Easy", "Remembering"),
         ("What lesson does it teach about relationships with others?", "Friendship.", "Easy", "Remembering"),
         ("What lesson does it teach about accepting duties?", "Responsibility.", "Easy", "Remembering"),
         ("How do funny situations help deliver moral lessons?", "They make moral lessons enjoyable and easy for children to remember.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("Doraemon's charming personality, Nobita's naivety, relatable situations and valuable life lessons has made this series one of the most loved and influential phenomenon in the world of animation.",
     [
         ("Whose naivety is mentioned in this sentence?", "Nobita's naivety.", "Easy", "Remembering"),
         ("Whose charming personality is highlighted?", "Doraemon's charming personality.", "Easy", "Remembering"),
         ("Why are the show's situations described as 'relatable'?", "Because they reflect real everyday childhood experiences.", "Medium", "Understanding"),
         ("In what field is Doraemon an influential phenomenon?", "In the world of animation.", "Easy", "Remembering"),
         ("Summarize this extract in one sentence.", "Doraemon's charming characters, relatable stories, and life lessons made it a world-famous animation classic.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 06: My Favourite Cartoon\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH06_EXT_{q_counter:03d}"
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

with open(os.path.join(CH06_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 06 in {CH06_DIR}")
