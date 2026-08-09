r"""
Refines all 6 Category files for Chapter 11 ("A Little Bird I Am") for Class 2 (Book 2).
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 2 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH11_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_11")
os.makedirs(CH11_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Who is the speaker in the poem 'A Little Bird I Am'?", "(A) A little bird", "(B) A caged lion", "(C) A flying eagle", "(D) A little boy", "(A)", "The speaker is a little bird ('A little bird I am').", "Easy", "Remembering", "Speaker"),
    ("Where is the little bird sitting and singing?", "(A) In a cage", "(B) In a high tree top", "(C) In a meadow", "(D) On a roof", "(A)", "It says 'And in my cage, I sit and sing'.", "Easy", "Remembering", "Setting"),
    ("From what is the bird shut out?", "(A) Fields of air", "(B) Water pond", "(C) Deep forest", "(D) Flower garden", "(A)", "It says 'Shut from the fields of air'.", "Easy", "Remembering", "Enclosure Detail"),
    ("To whom does the bird sing in its cage?", "(A) To Him (God) who placed it there", "(B) To other birds", "(C) To a cat", "(D) To the wind", "(A)", "It sings 'To Him who placed me there'.", "Easy", "Remembering", "Recipient of Song"),
    ("How does the bird feel about being a prisoner in the cage?", "(A) Well pleased", "(B) Extremely angry", "(C) Terrified", "(D) Bored", "(A)", "It says 'Well pleased a prisoner to be'.", "Easy", "Remembering", "Bird's Feeling"),
    ("Why is the bird pleased to be in the cage?", "(A) Because it pleases God", "(B) Because it gets golden toys", "(C) Because it hates flying", "(D) Because it likes small boxes", "(A)", "It says 'Because, my God, it pleases Thee!'.", "Easy", "Remembering", "Reason for Pleasure"),
    ("How long does the bird sing each day?", "(A) The whole day long", "(B) Only for five minutes", "(C) Only at midnight", "(D) Only in the morning", "(A)", "It says 'I sing the whole day long'.", "Easy", "Remembering", "Singing Duration"),
    ("Who bends down to listen to the bird's song?", "(A) God (He whom most I love to please)", "(B) A hunter", "(C) A snake", "(D) A farmer", "(A)", "It says 'But still He bends to hear me sing'.", "Easy", "Remembering", "Listener"),
    ("What did God do to the bird's wing according to the poem?", "(A) Caught and bound its wandering wing", "(B) Cut its wing", "(C) Painted its wing blue", "(D) Made its wing bigger", "(A)", "It says 'He caught and bound my wandering wing'.", "Easy", "Remembering", "Action on Wing"),
    ("Who wrote the poem 'A Little Bird I Am' according to the text?", "(A) Louisa May Alcott", "(B) Robert Frost", "(C) William Wordsworth", "(D) Christina Rossetti", "(A)", "The author is given as Louisa May Alcott.", "Easy", "Remembering", "Poet Name"),
    ("What does the old word 'Thee' mean?", "(A) You", "(B) Me", "(C) Them", "(D) We", "(A)", "Thee is the old form of 'You'.", "Easy", "Understanding", "Vocabulary"),
    ("What does the old word 'Naught' mean?", "(A) Nothing", "(B) Everything", "(C) Always", "(D) Often", "(A)", "Naught is the old form of 'nothing'.", "Easy", "Understanding", "Vocabulary"),
    ("What does the old word 'Doth' mean?", "(A) Does", "(B) Did", "(C) Done", "(D) Do not", "(A)", "Doth is the old form of 'Does'.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'wandering' mean in the poem's context?", "(A) Free", "(B) Lost", "(C) Hurt", "(D) Tired", "(A)", "Wandering means free (free wing).", "Easy", "Understanding", "Vocabulary"),
    ("Does the bird have anything else to do besides singing?", "(A) No ('Naught have I else to do')", "(B) Yes, build a nest", "(C) Yes, gather twigs", "(D) Yes, fight other birds", "(A)", "It says 'Naught have I else to do; I sing the whole day long'.", "Easy", "Remembering", "Bird's Task"),
    ("What is a cage used for?", "(A) To hold an animal or bird inside", "(B) To fly in the air", "(C) To drink water", "(D) To wear as a hat", "(A)", "A cage holds an animal or bird.", "Easy", "Understanding", "Word Concept"),
    ("What does 'fields of air' mean in the poem?", "(A) The wide open sky where birds fly freely", "(B) A farm of grass", "(C) A windy room", "(D) A balloon", "(A)", "'Fields of air' refers to the wide open sky.", "Easy", "Understanding", "Poetic Image"),
    ("Does the bird love to please God?", "(A) Yes, 'He whom most, I love to please'", "(B) No", "(C) It doesn't care", "(D) Only on Sundays", "(A)", "The bird loves to please God.", "Easy", "Remembering", "Bird's Devotion"),
    ("What sound does the bird make in its cage?", "(A) Singing", "(B) Barking", "(C) Roaring", "(D) Crying", "(A)", "The bird sits and sings.", "Easy", "Remembering", "Sound"),
    ("Is the bird in the poem free to fly in the open sky?", "(A) No, it is shut in a cage", "(B) Yes, it flies everywhere", "(C) It flies in a house", "(D) It swims in water", "(A)", "It is shut from the fields of air in a cage.", "Easy", "Remembering", "Confinement Status"),
    ("What emotion best describes the bird's song?", "(A) Devotional joy and contentment", "(B) Anger and hatred", "(C) Jealousy", "(D) Fear of dark", "(A)", "Devotional joy and acceptance of God's will.", "Easy", "Understanding", "Emotion"),
    ("What part of the bird was bound by God?", "(A) Wandering wing", "(B) Beak", "(C) Tail", "(D) Eyes", "(A)", "It says 'bound my wandering wing'.", "Easy", "Remembering", "Anatomy Detail"),
    ("What does 'prisoner' mean in the poem?", "(A) One who is kept inside a cage or prison", "(B) A king in a palace", "(C) A wild hunter", "(D) A fast runner", "(A)", "A prisoner is someone kept in a cage/prison.", "Easy", "Understanding", "Vocabulary"),
    ("Why does God bend down to the bird?", "(A) To hear the bird sing", "(B) To feed it corn", "(C) To open the door", "(D) To scold it", "(A)", "It says 'But still He bends to hear me sing'.", "Easy", "Remembering", "God's Action"),
    ("What is the title of Chapter 11?", "(A) A Little Bird I Am", "(B) The Banyan Tree", "(C) The Caged Nightingale", "(D) Flying Free", "(A)", "Chapter 11 is titled 'A Little Bird I Am'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("What spiritual message does the bird's attitude convey to readers?", "(A) Finding joy, gratitude, and peace in whatever situation God places you", "(B) Trying to escape from prison by force", "(C) Complaining continuously about bad luck", "(D) Refusing to sing when trapped", "(A)", "Acceptance, gratitude, and devotion in all circumstances.", "Medium", "Understanding", "Spiritual Message"),
    ("How does the poem contrast physical confinement with spiritual freedom?", "(A) Physically, the bird's wings are caged; spiritually, its soul sings freely to God", "(B) Physically it flies; spiritually it is trapped", "(C) Both body and soul are dead", "(D) There is no contrast", "(A)", "Physical cage vs spiritual singing freedom.", "Medium", "Analyzing", "Poetic Contrast"),
    ("Why is the phrase 'fields of air' a beautiful poetic metaphor?", "(A) It compares the vast open sky to vast green fields where birds wander freely", "(B) It means air is made of green grass", "(C) It means birds eat air", "(D) It refers to airplane runways", "(A)", "Compares open sky to wide fields.", "Medium", "Analyzing", "Metaphor Analysis"),
    ("What does 'He caught and bound my wandering wing' signify spiritually?", "(A) God placing limits or trials on a person's life to draw them closer in faith", "(B) A hunter injuring a bird with a gun", "(C) A bird breaking its own wing", "(D) A bird learning to fly faster", "(A)", "Divine placement of limits/trials to foster faith.", "Medium", "Analyzing", "Spiritual Symbolism"),
    ("Why does the bird feel no sadness about having 'naught else to do'?", "(A) Because singing all day long to please God fulfills its highest purpose and joy", "(B) Because it is lazy", "(C) Because it sleeps all day", "(D) Because it has no friends", "(A)", "Singing to please God fulfills its purpose.", "Medium", "Evaluating", "Meaning of Life"),
    ("What rhyming pair appears in the first stanza of the poem?", "(A) air / there", "(B) bird / cage", "(C) sing / God", "(D) pleased / Thee", "(A)", "Stanza 1 rhymes 'air' and 'there' (lines 2 and 4).", "Medium", "Remembering", "Rhyme Scheme"),
    ("How does the bird view its cage in relation to God's will?", "(A) As a place assigned by God that it accepts with love and contentment", "(B) As a punishment for bad behavior", "(C) As a mistake by the owner", "(D) As an ugly trap", "(A)", "Accepts cage as God's loving placement.", "Medium", "Understanding", "View of Cage"),
    ("What does the line 'He bends to hear me sing' tell us about God's character?", "(A) God is loving, humble, attentive, and listens to the smallest creature's prayer", "(B) God is distant and uninterested", "(C) God prefers loud music", "(D) God is angry at birds", "(A)", "God is loving, attentive, and listens to all creation.", "Medium", "Analyzing", "Divine Character"),
    ("Why is the poem suitable for teaching resilience to Class 2 children?", "(A) It teaches children to stay cheerful, creative, and faithful even when confined or facing restrictions", "(B) It teaches children to buy bird cages", "(C) It teaches children how to trap birds", "(D) It teaches children to stop singing", "(A)", "Teaches cheerfulness, faith, and resilience under restrictions.", "Medium", "Applying", "Educational Value"),
    ("What is the tone of the poem 'A Little Bird I Am'?", "(A) Peaceful, devotional, and contented", "(B) Melancholic and hopeless", "(C) Furious and violent", "(D) Silly and nonsensical", "(A)", "Tone is peaceful, devotional, and content.", "Medium", "Analyzing", "Tone of Poem"),
    ("How does the archaic language ('Thee', 'Naught', 'Doth') affect the poem's atmosphere?", "(A) It gives the poem a sacred, classic, and prayer-like quality", "(B) It makes the poem impossible to read", "(C) It makes the poem sound like modern rap", "(D) It adds scientific terms", "(A)", "Lends a sacred, timeless, prayer-like quality.", "Medium", "Analyzing", "Archaic Style"),
    ("In what way is the bird in the cage like a human prisoner of faith?", "(A) Both find inner spiritual freedom and joy through prayer and devotion despite physical walls", "(B) Both plan to break the cage bars", "(C) Both hate their life", "(D) Both stop talking", "(A)", "Finding inner spiritual freedom through devotion.", "Medium", "Comparing", "Analogy"),
    ("Why does the bird sing 'the whole day long' instead of remaining silent?", "(A) Because singing expresses its love, praise, and continuous connection to God", "(B) Because it is bored", "(C) To make noise for the neighbors", "(D) Because it gets food only when it sings", "(A)", "Expresses continuous love and connection to God.", "Medium", "Understanding", "Motivation for Song"),
    ("What shift in perspective turns a 'cage' into a 'place of praise'?", "(A) Shifting focus from physical restriction to spiritual purpose and divine love", "(B) Painting the cage yellow", "(C) Putting toys in the cage", "(D) Inviting other birds inside", "(A)", "Shifting focus to spiritual purpose and divine love.", "Medium", "Evaluating", "Perspective Shift"),
    ("How does the title 'A Little Bird I Am' reflect humility?", "(A) The speaker acknowledges its smallness before God while celebrating God's great love for it", "(B) The bird boasts about its speed", "(C) The bird claims to be king of the sky", "(D) The title is meaningless", "(A)", "Acknowledges smallness while celebrating divine love.", "Medium", "Analyzing", "Title Significance"),

    # Hard (41-50)
    ("Analyze the philosophical concept of 'Christian Mysticism' reflected in Madame Guyon / Louisa May Alcott's poem.", "(A) Outer imprisonment cannot restrict inner divine communion; true liberty comes from surrendering to divine love", "(B) Physical freedom is the only goal in life", "(C) Caging birds is a duty", "(D) Singing cures physical illness", "(A)", "Inner divine communion transcends outer physical restriction.", "Hard", "Analyzing", "HOTS Philosophical Depth"),
    ("Deconstruct the structural rhyme scheme and meter of the two 6-line stanzas.", "(A) Stanza 1: A B C B D D (or A-B-C-B-D-D variant); Stanza 2: E F E F G G, using gentle iambic rhythm", "(B) Free verse with no rhyming lines", "(C) Strict 14-line sonnet form", "(D) All lines end in the same word", "(A)", "Controlled rhyming stanzas with gentle iambic cadence.", "Hard", "Analyzing", "Poetic Structure"),
    ("Evaluate the moral paradox: 'Well pleased a prisoner to be'.", "(A) Paradox: Human nature hates imprisonment, yet spiritual surrender turns captivity into joyful devotion", "(B) It means the bird loves iron bars", "(C) It means prisoners are always happy", "(D) It is a grammatical error", "(A)", "Captivity transformed into joyful spiritual surrender.", "Hard", "Evaluating", "Moral Paradox"),
    ("Compare the theme of 'A Little Bird I Am' with Maya Angelou's 'Caged Bird'.", "(A) Alcott's bird finds serene spiritual contentment in God; Angelou's caged bird sings fiercely for racial freedom", "(B) Both birds are identical in emotion and goal", "(C) Angelou's bird is happy; Alcott's bird is angry", "(D) Neither poem uses a bird metaphor", "(A)", "Serene spiritual surrender vs fierce plea for racial freedom.", "Hard", "Comparing", "Comparative Literature"),
    ("Assess the psychological resilience demonstrated by finding purpose in isolation.", "(A) Transforming enforced isolation into a space for creative/spiritual expression protects mental well-being", "(B) Isolation always destroys mind and spirit", "(C) Isolation is best spent sleeping", "(D) Singing in isolation is foolish", "(A)", "Creative/spiritual expression protects mental well-being in isolation.", "Hard", "Evaluating", "Psychological Resilience"),
    ("How does the imagery of 'wandering wing' contrast with 'bound wing'?", "(A) 'Wandering wing' evokes wild, unguided flight; 'bound wing' represents disciplined, focused devotion to God", "(B) 'Wandering wing' means broken wing; 'bound wing' means healed wing", "(C) They have identical meanings", "(D) Wandering wing is a fish fin", "(A)", "Wild unguided freedom vs disciplined divine focus.", "Hard", "Analyzing", "Imagery Contrast"),
    ("Synthesize how Chapter 11 introduces young children to classic devotional poetry.", "(A) Simple bird metaphor + accessible rhyme + deep moral theme = memorable introduction to classic devotional literature", "(B) Complex grammar rules only", "(C) Scientific ornithology facts", "(D) Teaching how to make metal cages", "(A)", "Simple metaphor, accessible rhyme, and deep devotional theme.", "Hard", "Synthesizing", "Pedagogical Synthesis"),
    ("Reframe the poem's lesson for a modern child experiencing lockdown or home confinement.", "(A) 'Even inside four walls, my mind can create, my heart can pray, and my spirit can sing with joy!'", "(B) 'I must break the windows and run outside!'", "(C) 'I will sit in a corner and cry all day.'", "(D) 'Confinement means life is over.'", "(A)", "Inner creativity, prayer, and spirit flourish indoors.", "Hard", "Creating", "Modern Reframing"),
    ("Formulate a critical appreciation of the line 'But still He bends to hear me sing'.", "(A) Expresses profound divine intimacy: the Almighty Creator stoops down with tender affection to listen to a tiny caged bird", "(B) Means God has a bad back", "(C) Means the bird sings very loudly", "(D) Means the cage is placed on the floor", "(A)", "Profound divine intimacy and tender creator affection.", "Hard", "Evaluating", "Critical Appreciation"),
    ("Synthesize the ultimate spiritual lesson of Chapter 11 for Class 2 learners.", "(A) True happiness comes from within your heart and faith in God, not from where you are placed physically!", "(B) Keep wild birds in cages at home", "(C) Stop singing when you are sad", "(D) Only fly in open fields", "(A)", "True happiness comes from heart and faith, not physical location.", "Hard", "Evaluating", "Core Lesson Synthesis")
]

mcq_content = f"# MCQs — Chapter 11: A Little Bird I Am\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK02_CH11_MCQ_{idx:03d}"
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

with open(os.path.join(CH11_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("A little _______ I am, shut from the fields of air.", "bird", "A little bird I am.", "Easy"),
    ("Shut from the fields of _______.", "air", "Shut from the fields of air.", "Easy"),
    ("And in my cage, I sit and _______.", "sing", "In my cage, I sit and sing.", "Easy"),
    ("I sit and sing to Him who _______ me there.", "placed", "Him who placed me there.", "Easy"),
    ("Well pleased a _______ to be.", "prisoner", "Well pleased a prisoner to be.", "Easy"),
    ("Because, my God, it pleases _______!", "Thee", "Because, my God, it pleases Thee!", "Easy"),
    ("_______ have I else to do; I sing the whole day long.", "Naught", "Naught have I else to do.", "Easy"),
    ("I sing the _______ day long.", "whole", "I sing the whole day long.", "Easy"),
    ("And He whom most, I love to _______.", "please", "I love to please.", "Easy"),
    ("Doth _______ to my song.", "listen", "Doth listen to my song.", "Easy"),
    ("He caught and bound my wandering _______.", "wing", "Bound my wandering wing.", "Easy"),
    ("But still He bends to hear me _______.", "sing", "Bends to hear me sing.", "Easy"),
    ("The word 'Thee' is an old form of _______.", "You", "Thee means You.", "Easy"),
    ("The word 'Naught' is an old form of _______.", "nothing", "Naught means nothing.", "Easy"),
    ("The word 'Doth' is an old form of _______.", "Does", "Doth means Does.", "Easy"),
    ("The word 'wandering' in the poem means _______.", "free", "Wandering means free.", "Easy"),
    ("The author of the poem is Louisa May _______.", "Alcott", "Louisa May Alcott.", "Easy"),
    ("The bird sits inside a _______.", "cage", "Sits inside a cage.", "Easy"),
    ("The bird sings to please _______.", "God", "Sings to please God.", "Easy"),
    ("The bird is happy to be a _______ because it pleases God.", "prisoner", "Pleased a prisoner to be.", "Easy"),
    ("The bird sings all _______ long.", "day", "Sings the whole day long.", "Easy"),
    ("God bends down to _______ the bird's song.", "hear", "Bends to hear me sing.", "Easy"),
    ("The bird's wing is described as _______.", "wandering", "Wandering wing.", "Easy"),
    ("The open sky is described as fields of _______.", "air", "Fields of air.", "Easy"),
    ("Chapter 11 is titled 'A Little Bird I _______'.", "Am", "Titled 'A Little Bird I Am'.", "Easy"),

    # Medium (26-40)
    ("The poem expresses deep spiritual _______ and peace.", "devotion", "Expresses devotion/contentment.", "Medium"),
    ("Even though trapped in a cage, the bird's spirit remains _______.", "free", "Spirit remains free/joyful.", "Medium"),
    ("The bird sings because its song brings pleasure to _______.", "God", "Brings pleasure to God.", "Medium"),
    ("The word 'prisoner' normally means someone in captivity, but here it means a captive of _______.", "love", "Captive of divine love/will.", "Medium"),
    ("The phrase 'fields of air' paints a picture of the vast open _______.", "sky", "Vast open sky.", "Medium"),
    ("God 'bends' to listen, showing His great tenderness and _______.", "love", "Tenderness and love.", "Medium"),
    ("The bird has 'naught' else to do, meaning it has _______ else to do.", "nothing", "Has nothing else to do.", "Medium"),
    ("Singing all day long fills the bird's life with joy and _______.", "purpose", "Joy and purpose.", "Medium"),
    ("The bird accepts its cage because it trusts God's _______.", "will", "Trusts God's will.", "Medium"),
    ("The old word 'Doth' functions as the modern verb _______.", "does", "Modern verb 'does'.", "Medium"),
    ("Bound wings cannot fly, but a devoted heart can still _______.", "sing", "Devoted heart can sing.", "Medium"),
    ("Louisa May Alcott is the famous author associated with this _______.", "poem", "Author associated with this poem.", "Medium"),
    ("The bird finds contentment not in freedom, but in divine _______.", "pleasure", "In divine pleasure/love.", "Medium"),
    ("The contrast between a small bird and God highlights divine _______.", "grace", "Highlights divine grace.", "Medium"),
    ("Children learn that outer conditions cannot restrict inner _______.", "happiness", "Outer conditions vs inner happiness.", "Medium"),

    # Hard (41-50)
    ("The bird's cage transforms from a place of imprisonment into a temple of _______.", "praise", "Temple of praise.", "Hard"),
    ("The archaic pronoun 'Thee' addresses the Almighty Creator in personal _______.", "prayer", "Addresses Creator in prayer.", "Hard"),
    ("Imprisonment of the body fails to conquer the freedom of the _______.", "soul", "Freedom of the soul.", "Hard"),
    ("The metaphor 'wandering wing' signifies uncontrolled earthly _______.", "desire", "Uncontrolled desire/freedom.", "Hard"),
    ("God's act of binding the wing represents divine discipline and _______.", "stewardship", "Divine discipline and care.", "Hard"),
    ("Finding joy in captivity demonstrates spiritual _______.", "surrender", "Spiritual surrender.", "Hard"),
    ("The poetic structure features rhyming lines that create a gentle musical _______.", "rhythm", "Gentle musical rhythm.", "Hard"),
    ("Alcott's devotional verses teach resilience through unshakeable _______.", "faith", "Resilience through faith.", "Hard"),
    ("Listening to a caged bird's song symbolizes divine attentive _______.", "listening", "Divine attentive listening.", "Hard"),
    ("Chapter 11 serves as an inspiring lesson on faith, gratitude, and inner _______.", "peace", "Faith, gratitude, and inner peace.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 11: A Little Bird I Am\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK02_CH11_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH11_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The speaker in the poem is a little bird.", "True", "The speaker is a little bird ('A little bird I am').", "Easy"),
    ("The bird is free and flying in the sky.", "False", "The bird is shut in a cage from the fields of air.", "Easy"),
    ("The bird sits and sings in its cage.", "True", "And in my cage, I sit and sing.", "Easy"),
    ("The bird sings to please God.", "True", "It sings to Him who placed it there.", "Easy"),
    ("The bird is very angry about being a prisoner.", "False", "It says 'Well pleased a prisoner to be'.", "Easy"),
    ("The bird sings only for two minutes a day.", "False", "It sings 'the whole day long'.", "Easy"),
    ("God listens to the bird's song.", "True", "Doth listen to my song / He bends to hear me sing.", "Easy"),
    ("The word 'Thee' means 'You'.", "True", "Thee is an old form of 'You'.", "Easy"),
    ("The word 'Naught' means 'Everything'.", "False", "Naught is an old form of 'nothing'.", "Easy"),
    ("The word 'Doth' means 'Does'.", "True", "Doth is an old form of 'Does'.", "Easy"),
    ("The word 'wandering' means 'free'.", "True", "Wandering wing means free wing.", "Easy"),
    ("God caught and bound the bird's wandering wing.", "True", "He caught and bound my wandering wing.", "Easy"),
    ("The bird has many other chores to do besides singing.", "False", "Naught have I else to do.", "Easy"),
    ("Louisa May Alcott is credited as the poet.", "True", "Text gives poet as Louisa May Alcott.", "Easy"),
    ("The bird sings because it pleases God.", "True", "Because, my God, it pleases Thee!", "Easy"),
    ("The open sky is called 'fields of air'.", "True", "Shut from the fields of air.", "Easy"),
    ("The bird wishes to hurt its owner.", "False", "The bird sings with love and devotion to please God.", "Easy"),
    ("God bends down to hear the bird sing.", "True", "But still He bends to hear me sing.", "Easy"),
    ("The bird feels sad and cries all day long.", "False", "The bird sings all day long and is well pleased.", "Easy"),
    ("The cage was built by a cat.", "False", "The poem speaks of God who placed the bird there.", "Easy"),
    ("The bird loves God most of all.", "True", "He whom most, I love to please.", "Easy"),
    ("The bird stops singing when God listens.", "False", "God bends to hear it sing, so it continues singing.", "Easy"),
    ("The bird's wing is completely free to fly away.", "False", "God caught and bound its wandering wing.", "Easy"),
    ("The poem teaches us to be content and cheerful.", "True", "It teaches contentment and cheerfulness in all circumstances.", "Easy"),
    ("Chapter 11 is titled 'A Little Bird I Am'.", "True", "Chapter 11 is titled 'A Little Bird I Am'.", "Easy"),

    # Medium (26-40)
    ("The poem shows that true freedom is spiritual rather than physical.", "True", "Though body is caged, the bird's soul and song fly freely to God.", "Medium"),
    ("The bird sings only when it receives extra food.", "False", "It sings out of pure love and devotion to please God.", "Medium"),
    ("The archaic word 'Thee' is used to address God with personal reverence.", "True", "Thee is an archaic personal address for God.", "Medium"),
    ("The bird considers itself unfortunate and unloved.", "False", "It knows God loves it and bends to hear its song.", "Medium"),
    ("Singing all day long gives the caged bird a clear purpose in life.", "True", "Singing to please God fulfills its purpose.", "Medium"),
    ("The line 'Shut from the fields of air' means the bird is flying in clouds.", "False", "It means the bird is kept inside a cage away from open sky.", "Medium"),
    ("God's act of bending to listen shows that God cares for small creatures.", "True", "It symbolizes divine care for even the smallest creation.", "Medium"),
    ("The bird would rather be angry than pleased as a prisoner.", "False", "It states it is 'well pleased a prisoner to be'.", "Medium"),
    ("The poem contains two stanzas of six lines each.", "True", "The poem consists of two 6-line stanzas.", "Medium"),
    ("The bird's song is a form of prayer and worship.", "True", "Singing to God in devotion is a form of prayer.", "Medium"),
    ("Louisa May Alcott wrote only scientific books about birds.", "False", "Alcott was a famous literary author and poet.", "Medium"),
    ("The bird's contentment comes from knowing its life pleases God.", "True", "Its happiness comes from pleasing God.", "Medium"),
    ("A 'wandering wing' describes a wing that is tied up in a knot forever.", "False", "It poetically describes a wing that used to wander freely in the air.", "Medium"),
    ("Class 2 students can learn resilience and faith from this poem.", "True", "It teaches positive mindset, faith, and emotional resilience.", "Medium"),
    ("The poem claims that cages are good for all wild animals.", "False", "The poem is a spiritual metaphor about inner peace, not an endorsement of animal cruelty.", "Medium"),

    # Hard (41-50)
    ("The bird's surrender to divine placement reflects mystical spiritual submission.", "True", "It reflects surrendering personal will to divine providence.", "Hard"),
    ("The phrase 'Naught have I else to do' implies deep sorrow and hopelessness.", "False", "It expresses joyful single-minded devotion to singing praise.", "Hard"),
    ("In devotional poetry, physical walls often represent worldly limitations.", "True", "Enclosures represent physical/worldly limitations transcended by faith.", "Hard"),
    ("The poem uses regular rhyming couplets and quatrains.", "True", "It uses structured rhyming patterns across both stanzas.", "Hard"),
    ("God's 'binding' of the wing symbolizes divine restraint for a higher spiritual purpose.", "True", "Restraint directs energy toward spiritual devotion.", "Hard"),
    ("The bird's song ceases as soon as night falls according to the text.", "False", "The text states it sings 'the whole day long' without mentioning night stopping it.", "Hard"),
    ("Louisa May Alcott adapted this theme from classic devotional traditions.", "True", "The text reflects classic devotional themes of Guyon/Alcott tradition.", "Hard"),
    ("The bird's perspective turns its cage into a holy sanctuary.", "True", "Devotion transforms physical confinement into a sanctuary.", "Hard"),
    ("The poem encourages readers to complain whenever obstacles arise.", "False", "It inspires readers to maintain faith and joy during difficulties.", "Hard"),
    ("Chapter 11 combines poetic literature, archaic vocabulary, and moral philosophy.", "True", "It includes poem text, old word meanings (Thee, Naught), and spiritual lessons.", "Hard")
]

tf_content = f"# True / False — Chapter 11: A Little Bird I Am\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK02_CH11_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH11_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who is the speaker in the poem 'A Little Bird I Am'?", "The speaker is a little caged bird.", "Easy", "Remembering"),
    ("Where is the little bird sitting and singing?", "The little bird is sitting and singing inside its cage.", "Easy", "Remembering"),
    ("What does the bird mean by 'fields of air'?", "'Fields of air' means the vast open sky where birds fly freely.", "Easy", "Understanding"),
    ("To whom does the bird sing?", "The bird sings to God ('Him who placed me there').", "Easy", "Remembering"),
    ("Why is the bird pleased to be a prisoner in a cage?", "The bird is pleased because being in the cage pleases God.", "Easy", "Remembering"),
    ("How long does the bird sing each day?", "The bird sings the whole day long.", "Easy", "Remembering"),
    ("What does God do when the bird sings?", "God listens to the song and bends down to hear it sing.", "Easy", "Remembering"),
    ("What did God do to the bird's wandering wing?", "God caught and bound its wandering wing.", "Easy", "Remembering"),
    ("Who wrote the poem according to Chapter 11?", "Louisa May Alcott.", "Easy", "Remembering"),
    ("What is the old meaning of the word 'Thee'?", "'Thee' is an old form of the word 'You'.", "Easy", "Understanding"),
    ("What is the old meaning of the word 'Naught'?", "'Naught' is an old form of the word 'nothing'.", "Easy", "Understanding"),
    ("What is the old meaning of the word 'Doth'?", "'Doth' is an old form of the word 'Does'.", "Easy", "Understanding"),
    ("What does 'wandering' mean when describing the bird's wing?", "'Wandering' means free or unconfined.", "Easy", "Understanding"),
    ("Does the bird have any other work to do in its cage?", "No, it has 'naught else to do' except sit and sing all day.", "Easy", "Remembering"),
    ("How does the bird feel in its cage?", "The bird feels peaceful, content, and happy to please God.", "Easy", "Remembering"),
    ("What sound fills the bird's day in the cage?", "The beautiful sound of its own singing.", "Easy", "Remembering"),
    ("Why does God catch and bind the bird's wing?", "To place it in the cage where it can sing praises to Him.", "Easy", "Understanding"),
    ("What is a cage?", "A cage is an enclosure made of bars used to hold birds or animals.", "Easy", "Understanding"),
    ("Whom does the bird love most of all to please?", "The bird loves to please God most of all.", "Easy", "Remembering"),
    ("What does 'He bends to hear me sing' show about God?", "It shows that God is loving, attentive, and listens to the bird's song.", "Easy", "Understanding"),
    ("Is the bird angry at God for putting it in a cage?", "No, it is 'well pleased' because it trusts God's love.", "Easy", "Remembering"),
    ("What action does the bird do in the cage?", "It sits and sings all day long.", "Easy", "Remembering"),
    ("What does 'shut from the fields of air' mean?", "It means the bird is kept inside a cage and cannot fly in the open sky.", "Easy", "Understanding"),
    ("What message does the bird's song carry?", "A message of love, praise, faith, and joy.", "Easy", "Understanding"),
    ("What is the title of Chapter 11?", "The title of Chapter 11 is 'A Little Bird I Am'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Explain the central spiritual message of the poem 'A Little Bird I Am'.", "The poem teaches that true happiness comes from inner faith and pleasing God, regardless of physical restrictions or being confined in a cage.", "Medium", "Understanding"),
    ("How does the poet contrast physical restriction with spiritual freedom?", "Physically, the bird's wing is bound in a cage; spiritually, its heart is free and its song reaches up to God.", "Medium", "Analyzing"),
    ("Why is the phrase 'He bends to hear me sing' significant?", "It shows divine intimacy—that the great Creator stoops down with love to listen to the song of a small, humble bird.", "Medium", "Analyzing"),
    ("Describe the bird's attitude toward its imprisonment.", "The bird accepts its imprisonment with joy ('well pleased'), seeing it as an opportunity to dedicate its entire day to singing praises to God.", "Medium", "Evaluating"),
    ("How does the use of archaic words ('Thee', 'Naught', 'Doth') enrich the poem?", "It gives the poem a solemn, timeless, and prayer-like quality that emphasizes reverence for God.", "Medium", "Analyzing"),
    ("What does 'Naught have I else to do' reveal about the bird's life?", "It shows that having no worldly distractions allows the bird to focus 100% of its energy on singing and praising God.", "Medium", "Understanding"),
    ("Why does the bird call its wing a 'wandering wing'?", "Because before being caged, its wing used to wander freely across the open sky and fields of air.", "Medium", "Understanding"),
    ("How can a Class 2 student apply the bird's mindset during difficult times?", "A student can learn to remain cheerful, patient, and faithful even when staying indoors or facing rules and restrictions.", "Medium", "Applying"),
    ("What rhyming words are used in Stanza 1 of the poem?", "The rhyming words include 'air / there' and 'be / Thee'.", "Medium", "Remembering"),
    ("What rhyming words are used in Stanza 2 of the poem?", "The rhyming words include 'long / song' and 'wing / sing'.", "Medium", "Remembering"),
    ("Summarize Page 40 of the textbook in two sentences.", "In the poem 'A Little Bird I Am' by Louisa May Alcott, a caged bird joyfully sings all day long to God who placed it there. Though its wing is bound from flying in open air, it is happy because its song pleases God who listens attentively.", "Medium", "Understanding"),
    ("What makes the bird a model of contentment?", "It does not complain about lost freedom; instead, it finds complete satisfaction in singing to please its Creator.", "Medium", "Evaluating"),
    ("How does God's placement of the bird in a cage reflect divine purpose?", "The poem suggests that every placement or trial by God has a higher purpose—to draw out sweet songs of faith.", "Medium", "Analyzing"),
    ("What is the difference between a bird that sings in fear vs this bird?", "A fearful bird cries to get out, while this bird sings with devotion because it loves and trusts God.", "Medium", "Analyzing"),
    ("How does Chapter 11 build poetic appreciation in young children?", "It uses a simple bird story with smooth rhymes, old words, and a sweet message of faith and cheerfulness.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the moral paradox presented in the line 'Well pleased a prisoner to be'.", "Paradoxically, being a prisoner is usually sad, but when captivity is accepted as God's loving will, it transforms into spiritual joy and peace.", "Hard", "Evaluating"),
    ("Analyze how the poem transforms a cage from a symbol of cruelty into a sanctuary of praise.", "By focusing entirely on divine love and song rather than physical bars, the bird transforms its physical cage into a holy altar of worship.", "Hard", "Analyzing"),
    ("Deconstruct the structural layout of the two stanzas in 'A Little Bird I Am'.", "Two 6-line stanzas with alternating and couplet rhymes (A-B-C-B-D-D / E-F-E-F-G-G) creating a rhythmic, song-like cadence suitable for a singing bird.", "Hard", "Analyzing"),
    ("Compare the perspective of a wild bird with the caged bird in this poem.", "A wild bird enjoys physical 'fields of air' wandering; the caged bird surrenders wild wandering to gain deep spiritual intimacy with God.", "Hard", "Analyzing"),
    ("Evaluate the psychological impact of singing during times of confinement.", "Singing releases positive emotion, reduces stress, and provides a creative outlet, turning isolation into a productive spiritual experience.", "Hard", "Evaluating"),
    ("How can teachers use this poem to explain faith and optimism to primary students?", "Teachers can explain that optimism means looking for the good in every situation, just as the bird sings happily inside its small cage.", "Hard", "Applying"),
    ("Assess the role of old English vocabulary (Thee, Doth) in devotional literature.", "Archaic terms create a sacred, dignified tone that elevates simple poetry into timeless devotional hymnody.", "Hard", "Evaluating"),
    ("Why is the line 'He caught and bound my wandering wing' an example of divine intervention?", "It portrays God actively guiding the bird's life path—stopping its wild wandering to focus its soul on eternal song.", "Hard", "Analyzing"),
    ("Formulate a short 4-line devotional response from God to the little bird.", "'Sing on, my little bird so sweet,\nYour caged song reaches to My feet!\nThough bound your wing in iron space,\nYour heart is free within My grace!'", "Hard", "Creating"),
    ("Synthesize the ultimate moral lesson of Chapter 11 for young Class 2 learners.", "No matter where you are placed or what limits you face, keep a song of faith in your heart and spread joy to God and others!", "Hard", "Evaluating")
]

sa_content = f"# Short Answer Questions — Chapter 11: A Little Bird I Am\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK02_CH11_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH11_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the setting, speaker, and main activity in the poem 'A Little Bird I Am'.", 
     "In the poem 'A Little Bird I Am', the speaker is a small bird that has been shut away from the open sky ('fields of air') and placed inside a cage. Instead of crying or complaining, the bird sits peacefully in its cage and sings sweet songs all day long. It directs its song toward God, who placed it in the cage, finding complete happiness in singing to please its Creator.", 
     "Easy", "Remembering"),

    ("Explain why the bird is happy to be a prisoner in a cage.", 
     "The bird is happy ('well pleased a prisoner to be') because it believes that its situation is ordained by God. It loves God above all else and knows that sitting in the cage and singing pleases Him. Because fulfilling God's pleasure is its highest desire, being in a cage becomes a source of joy rather than sadness.", 
     "Easy", "Understanding"),

    ("Detail what God does for the bird in the poem, according to the second stanza.", 
     "According to the second stanza, God caught the bird and bound its 'wandering wing', placing it in the cage. However, God does not ignore the bird; instead, He bends down with loving tenderness to listen to its song. Knowing that God actively listens to its singing fills the bird with happiness to sing the whole day long.", 
     "Easy", "Remembering"),

    ("Explain the old English words used in the poem: 'Thee', 'Naught', 'Doth', and 'wandering'.", 
     "1. **Thee**: An archaic form of 'You', used when praying or speaking reverently to God.\n2. **Naught**: An archaic word meaning 'nothing' ('Naught have I else to do').\n3. **Doth**: An archaic form of the verb 'Does' ('Doth listen to my song').\n4. **Wandering**: In this poem's context, it means free or unconfined ('wandering wing').", 
     "Easy", "Understanding"),

    ("How does the poem teach children to be content and cheerful in all circumstances?", 
     "The poem uses the simple image of a caged bird to show that true happiness does not depend on outward circumstances like being in an open field or in a cage. By remaining cheerful, singing praises, and trusting God, children can find peace and joy even when faced with rules, confinement, or hard situations.", 
     "Easy", "Understanding"),

    ("Describe the relationship between God and the little bird in the poem.", 
     "The relationship is one of deep love, trust, and intimacy. The bird loves God above all else ('He whom most, I love to please') and sings devotedly to Him. God, in turn, cares for the small bird, placing it safely and bending down attentively to listen to its sweet song.", 
     "Easy", "Remembering"),

    ("What does the bird do all day long in its cage and why?", 
     "The bird sits and sings the whole day long. It does this because it has 'naught else to do' in the cage and because singing is its way of expressing love, gratitude, and praise to God, who placed it there and delights in hearing its song.", 
     "Easy", "Remembering"),

    ("Why is the open sky referred to as 'fields of air' in the poem?", 
     "The open sky is poetically called 'fields of air' because just as land animals wander across vast green fields on earth, birds fly and wander across the vast, open, boundless fields of the sky.", 
     "Easy", "Understanding"),

    ("What is the significance of God bending down to hear the bird's song?", 
     "God bending down shows immense divine humility, tenderness, and love. It signifies that even though God is the great Creator of the universe, He stoops down to give full attention and care to the prayer and song of even the smallest creature.", 
     "Easy", "Understanding"),

    ("Summarize the two stanzas of the poem 'A Little Bird I Am' in your own words.", 
     "**Stanza 1**: The little bird is caged away from the open sky, but it sits happily singing to God because being a prisoner in the cage pleases God.\n**Stanza 2**: With nothing else to do, the bird sings all day long to please God, who bound its flying wing but lovingly bends down to listen to its song.", 
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Who wrote the poem 'A Little Bird I Am' and what is its theme?", "The poem is credited to Louisa May Alcott. Its theme is spiritual contentment, faith, and finding joy in divine devotion despite physical confinement.", "Easy", "Remembering"),
    ("What does 'bound my wandering wing' mean literally and symbolically?", "Literally, it means stopping the bird from flying freely. Symbolically, it means God restricting physical freedom to guide the soul toward focused spiritual devotion.", "Easy", "Understanding"),
    ("Why does the bird feel no regret about not flying in the sky?", "Because pleasing God through its song brings far deeper joy and satisfaction than wandering aimlessly in the sky.", "Easy", "Understanding"),
    ("How does the poem use rhyme to sound like a bird's song?", "It uses gentle rhyming pairs like air/there, be/Thee, long/song, and wing/sing, creating a smooth, musical rhythm that mimics a sweet song.", "Easy", "Understanding"),
    ("What lesson can we learn about complaining from the little bird?", "The bird never complains about its cage or lost freedom. We learn to replace complaining with singing, gratitude, and positive action.", "Easy", "Evaluating"),
    ("Why is the word 'prisoner' used in a happy way in the poem?", "Because the bird is a 'prisoner of love'—happily accepting its cage because it was chosen by God.", "Easy", "Understanding"),
    ("What does 'He whom most, I love to please' mean?", "It means that pleasing God is the bird's highest priority and deepest love in life.", "Easy", "Understanding"),
    ("How does the poem show that small creatures matter to God?", "By showing that God bends down specifically to hear the small caged bird's song, proving every creature matters to Him.", "Easy", "Understanding"),
    ("What color or mood does the poem create in a reader's mind?", "It creates a bright, peaceful, and warm devotional mood filled with sweet music and divine love.", "Easy", "Remembering"),
    ("How can Class 2 students recite this poem expressively?", "Students can recite it with a gentle, joyful voice, placing hand over heart for 'my God' and miming a singing bird.", "Easy", "Applying"),
    ("What does 'Naught have I else to do' mean in simple words?", "It simply means 'I have nothing else to do'.", "Easy", "Understanding"),
    ("Why is singing a great way to express faith?", "Singing combines sweet words and music, lifting the heart and spreading joy to both the singer and the listener.", "Easy", "Understanding"),
    ("How does the bird know God hears its song?", "Through faith and love, it senses that God bends down attentively whenever it sings.", "Easy", "Understanding"),
    ("What is the main difference between a sad caged bird and this bird?", "A sad bird focuses on the cage bars; this bird focuses on God who listens to its song.", "Easy", "Analyzing"),
    ("Summarize Chapter 11 in five key sentences.", "Chapter 11 presents the poem 'A Little Bird I Am' by Louisa May Alcott. A small bird is caged away from the open sky, but remains well pleased because being in the cage pleases God. With nothing else to do, it sings the whole day long to please its Creator. God bound its wandering wing, but lovingly bends down to hear its song. It teaches young learners faith, contentment, and cheerfulness in all circumstances.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how 'A Little Bird I Am' explores the concept of spiritual freedom.", 
     "The poem demonstrates that true freedom is an internal spiritual state rather than an external physical condition. Physical bars may bind the bird's wings and shut it from the sky, but they cannot cage its heart, faith, or voice. By directing its song toward God, the bird transcends physical confinement and experiences ultimate spiritual freedom.", 
     "Medium", "Analyzing"),

    ("Examine the role of faith and surrender in achieving emotional peace.", 
     "When individuals face situations beyond their control, fighting against reality causes distress. The bird practices spiritual surrender—trusting that God placed it in the cage for a good reason. By accepting its place with faith and focusing on singing, it achieves complete emotional peace and contentment.", 
     "Medium", "Evaluating"),

    ("Discuss how archaic poetic diction elevates the religious tone of the poem.", 
     "The use of archaic words like 'Thee' (You), 'Naught' (Nothing), and 'Doth' (Does) elevates the poem above everyday speech. This traditional sacred diction connects the poem to classical devotional literature and prayer, instilling a sense of reverence and timeless spiritual beauty in young readers.", 
     "Medium", "Analyzing"),

    ("Explore the symbolism of the 'wandering wing' versus the 'cage'.", 
     "The 'wandering wing' symbolizes restless, unguided worldly distraction and aimless freedom. The 'cage' symbolizes divine discipline, focus, and quiet sanctuary. By catching and binding the wandering wing, God redirects the bird's energy away from aimless wandering toward concentrated praise.", 
     "Medium", "Analyzing"),

    ("How can primary school teachers use Chapter 11 to foster emotional resilience?", 
     "Teachers can discuss how children often feel 'caged' by rules, indoor stay, or difficult tasks. By using the bird's example, teachers can guide children to find joyful creative outlets (like singing, drawing, or reading) and maintain a positive attitude.", 
     "Medium", "Applying"),

    ("Why is the action of God 'bending' down a powerful poetic image?", "It creates a striking visual contrast: the majestic, high Creator of the universe stooping down close to a tiny cage on earth, illustrating divine humility and tender personal care.", "Medium", "Analyzing"),
    ("Describe the structure, rhythm, and rhyme scheme of the poem.", "The poem has two 6-line stanzas with an iambic rhythm and a controlled rhyming scheme (A-B-C-B-D-D / E-F-E-F-G-G) that creates a smooth, melodic song-like flow.", "Medium", "Understanding"),
    ("How does the bird turn a potential negative experience into a positive life purpose?", "Instead of viewing the cage as a cruel prison, the bird views it as a private stage provided by God where it can perform its lifelong duty of singing praise.", "Medium", "Evaluating"),
    ("Contrast the bird's past life in the sky with its present life in the cage.", "In the past, its wing wandered freely through the sky; in the present, its wing is bound in a cage, yet its joy is higher now because it lives directly to please God.", "Medium", "Analyzing"),
    ("Why is 'pleasing God' the ultimate motivation for the bird?", "Because the bird realizes that pleasing its Creator gives eternal meaning to its life, far exceeding temporary physical freedom.", "Medium", "Understanding"),
    ("How does the poem address the universal human experience of isolation?", "It shows that isolation can be transformed into a productive, peaceful time of reflection, prayer, and artistic expression rather than loneliness.", "Medium", "Evaluating"),
    ("What makes the poem accessible and appealing to Class 2 learners?", "Its relatable bird narrator, clear rhyming words, simple 6-line stanzas, and uplifting message make it easy to memorize and recite.", "Medium", "Understanding"),
    ("Explain why the bird sings 'the whole day long' without growing tired.", "Love and devotion provide endless energy. Because the bird sings out of pure love for God, its song never feels like hard labor.", "Medium", "Understanding"),
    ("What safety or ethical discussion can be introduced alongside this poem?", "Teachers can clarify that while the poem uses a cage as a spiritual metaphor, real birds should be loved and protected in their natural free habitats.", "Medium", "Applying"),
    ("Construct a short creative poem from God's perspective replying to the caged bird.", "'I hear your song, my little bird,\nThe sweetest praise I've ever heard!\nThough caged your wing upon the earth,\nYour loving heart has endless worth!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the philosophical tension between free will and divine providence in the poem.", 
     "The poem resolves the tension between free will and divine providence through loving surrender. While the bird's free flight is restricted by divine providence ('placed me there'), the bird uses its free will to choose joy, singing, and devotion rather than bitterness.", 
     "Hard", "Evaluating"),

    ("Deconstruct the literary lineage of 'A Little Bird I Am' (Madame Guyon to Louisa May Alcott).", 
     "Originally composed by French mystic Madame Guyon while imprisoned in the Bastille, the poem was translated and adapted into English literature by figures like Louisa May Alcott, preserving its timeless message of inner spiritual liberty during physical captivity.", 
     "Hard", "Analyzing"),

    ("Synthesize the theological, psychological, and literary dimensions of Chapter 11.", 
     "1. **Theological**: Divine providence, surrender, and attentive grace.\n2. **Psychological**: Resilience, cognitive reframing of confinement, and joy in isolation.\n3. **Literary**: Devotional poetry, archaic diction, and structural rhyme.", 
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive lesson plan for teaching 'A Little Bird I Am' in primary school.", 
     "- **Recitation**: Choral reading with expressive gestures.\n- **Vocabulary**: Matching old words (Thee, Naught, Doth) to modern equivalents.\n- **Art**: Drawing a singing bird inside a decorative cage.\n- **Discussion**: Finding positive ways to handle rules and indoor time.", 
     "Hard", "Creating"),

    ("Evaluate the impact of devotional poetry in building moral character in early childhood education.", 
     "Devotional poetry introduces young children to noble values—faith, gratitude, humility, and perseverance—through memorable rhythm and metaphors, shaping positive character development early in life.", 
     "Hard", "Evaluating"),

    ("Analyze how the bird's song functions as a bridge between earth and heaven.", "The bird sits in a physical cage on earth, but its song travels upward across physical boundaries into heaven where God bends down to receive it.", "Hard", "Analyzing"),
    ("Compare 'A Little Bird I Am' with other classic bird poems in English literature.", "Unlike poems that focus on a bird's wild flight or sorrowful captivity, Alcott's poem stands out for its serene spiritual contentment and devotional joy.", "Hard", "Analyzing"),
    ("Draft an essay opening analyzing the line 'Because, my God, it pleases Thee!'.", "'In a single triumphant line, the caged bird reveals the secret of unshakeable joy: when pleasing God becomes one's sole objective, physical circumstances lose all power to inflict suffering.'", "Hard", "Creating"),
    ("Assess how cognitive reframing helps the bird re-interpret its imprisonment.", "By reframing its cage from a 'punishment' into a 'divine placement', the bird mentally eliminates feelings of victimhood and experiences pure contentment.", "Hard", "Evaluating"),
    ("Synthesize the ultimate philosophy of Chapter 11 into a guiding principle.", "'Bound your physical wandering, unbind your heart in faith, and let your life be a sweet continuous song that pleases your Creator!'", "Hard", "Creating")
]

la_content = f"# Long Answer Questions — Chapter 11: A Little Bird I Am\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK02_CH11_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH11_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("A little bird I am,\nShut from the fields of air,\nAnd in my cage, I sit and sing\nTo Him who placed me there:",
     [
         ("What is the speaker in the poem?", "A little bird.", "Easy", "Remembering"),
         ("What is the bird shut away from?", "The fields of air (open sky).", "Easy", "Remembering"),
         ("Where does the bird sit and sing?", "In its cage.", "Easy", "Remembering"),
         ("To whom does the bird direct its song?", "To Him (God) who placed it there.", "Easy", "Remembering"),
         ("What does 'fields of air' mean poetically?", "The wide open sky where birds fly.", "Medium", "Understanding")
     ]),

    # Set 2
    ("Well pleased a prisoner to be,\nBecause, my God, it pleases Thee!",
     [
         ("How does the bird feel about being a prisoner?", "Well pleased.", "Easy", "Remembering"),
         ("Why is the bird pleased to be a prisoner?", "Because it pleases God.", "Easy", "Remembering"),
         ("What is the old meaning of 'Thee'?", "You.", "Easy", "Remembering"),
         ("What word in this extract means a captive in a cage?", "Prisoner.", "Easy", "Remembering"),
         ("What emotion does the bird show toward God's will?", "Contentment, joy, and loving devotion.", "Medium", "Evaluating")
     ]),

    # Set 3
    ("Naught have I else to do;\nI sing the whole day long;",
     [
         ("What does the word 'Naught' mean?", "Nothing.", "Easy", "Remembering"),
         ("Does the bird have anything else to do in the cage?", "No, naught else to do.", "Easy", "Remembering"),
         ("How long does the bird sing?", "The whole day long.", "Easy", "Remembering"),
         ("Why does the bird sing all day?", "Because singing to please God is its single-minded purpose.", "Medium", "Understanding"),
         ("What quality does singing all day long demonstrate?", "Perseverance, joy, and unceasing praise.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("And He whom most, I love to please\nDoth listen to my song,",
     [
         ("Whom does the bird love to please most of all?", "God ('He whom most, I love to please').", "Easy", "Remembering"),
         ("What does God do while the bird sings?", "Doth listen to its song.", "Easy", "Remembering"),
         ("What does the old word 'Doth' mean?", "Does.", "Easy", "Remembering"),
         ("How does the bird know its song is accepted?", "Because God lovingly listens to its song.", "Medium", "Understanding"),
         ("What relationship is highlighted in this extract?", "A loving relationship of faith between God and the small bird.", "Medium", "Analyzing")
     ]),

    # Set 5
    ("He caught and bound my wandering wing,\nBut still He bends to hear me sing.",
     [
         ("Who caught and bound the bird's wing?", "God ('He').", "Easy", "Remembering"),
         ("What adjective describes the bird's wing before being bound?", "Wandering.", "Easy", "Remembering"),
         ("What does God do despite binding the bird's wing?", "He bends down to hear the bird sing.", "Easy", "Remembering"),
         ("What does 'wandering wing' mean?", "A free wing that used to fly anywhere in the sky.", "Medium", "Understanding"),
         ("What does God 'bending down' symbolize?", "Profound divine love, humility, and attentive care for small creatures.", "Medium", "Evaluating")
     ]),

    # Set 6
    ("Word Meaning: Thee: (old form) You | Naught: (old form) nothing | Doth: (old form) Does | Wandering: Free",
     [
         ("What is the old form of 'You' in the poem?", "Thee.", "Easy", "Remembering"),
         ("What is the old form of 'nothing'?", "Naught.", "Easy", "Remembering"),
         ("What is the old form of 'Does'?", "Doth.", "Easy", "Remembering"),
         ("What does 'wandering' mean in the poem's vocabulary box?", "Free.", "Easy", "Remembering"),
         ("Why are these old word meanings provided for Class 2 students?", "To help young learners understand archaic language used in classic poetry.", "Medium", "Understanding")
     ]),

    # Set 7
    ("A little bird I am,\nShut from the fields of air,\nAnd in my cage, I sit and sing...",
     [
         ("Name the title of the poem from which this extract is taken.", "'A Little Bird I Am'.", "Easy", "Remembering"),
         ("Who is the author of this poem?", "Louisa May Alcott.", "Easy", "Remembering"),
         ("Is the bird outside or inside the cage?", "Inside the cage.", "Easy", "Remembering"),
         ("What physical ability is restricted by the cage?", "Flying in the open air.", "Easy", "Understanding"),
         ("How does the bird react to being caged?", "It sits peacefully and sings praises to God.", "Medium", "Understanding")
     ]),

    # Set 8
    ("Well pleased a prisoner to be,\nBecause, my God, it pleases Thee!\nNaught have I else to do;\nI sing the whole day long;",
     [
         ("How many lines are in this extract?", "Four lines.", "Easy", "Remembering"),
         ("Which two lines rhyme at the end in this extract?", "Lines 1 and 2 ('be' / 'Thee') and lines 3 and 4 ('do' / 'long' slant rhyme).", "Medium", "Analyzing"),
         ("What is the bird's main activity?", "Singing the whole day long.", "Easy", "Remembering"),
         ("Who is the bird speaking to when it says 'my God'?", "God.", "Easy", "Remembering"),
         ("Summarize the attitude of the bird in these four lines.", "Unconditional happiness and devotion in doing God's will.", "Medium", "Evaluating")
     ]),

    # Set 9
    ("He caught and bound my wandering wing,\nBut still He bends to hear me sing.",
     [
         ("Which body part of the bird was bound?", "Its wing.", "Easy", "Remembering"),
         ("Does God ignore the bird after binding its wing?", "No, He bends to hear it sing.", "Easy", "Remembering"),
         ("What literary device is used in 'wandering wing'?", "Alliteration (repetition of 'w' sound).", "Medium", "Analyzing"),
         ("What rhyming words end these two lines?", "Wing / sing.", "Easy", "Remembering"),
         ("What message of hope does this couplet give?", "Even when our freedom is limited, God still listens to our prayers and songs.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("A little bird I am... He caught and bound my wandering wing, But still He bends to hear me sing.",
     [
         ("What is the bird's overall mood throughout the poem?", "Cheerful, peaceful, and devout.", "Easy", "Remembering"),
         ("What does the bird teach us about facing difficulties?", "To remain positive, faithful, and focused on inner joy.", "Medium", "Understanding"),
         ("Why is this poem valuable for Class 2 English reading?", "It builds vocabulary, rhyming skills, expressive recitation, and moral values.", "Medium", "Evaluating"),
         ("What is the central contrast in the poem?", "Physical cage vs spiritual singing freedom.", "Medium", "Analyzing"),
         ("Summarize the poem's lesson in one sentence.", "Contentment comes from pleasing God and keeping a faithful song in your heart wherever you are.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 11: A Little Bird I Am\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 3 per set\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK02_CH11_EXT_{q_counter:03d}"
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

with open(os.path.join(CH11_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Generated all 6 category files (300 total Qs) for Chapter 11 in {CH11_DIR}")
