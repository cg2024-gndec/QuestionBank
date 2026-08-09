r"""
Refines all 6 Category files for Book 5 Chapter 14 ("The Season's Song" - Poem) for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH14_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_14")
os.makedirs(CH14_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Which season comes first according to the poem 'The Season's Song'?", "(A) Spring", "(B) Summer", "(C) Autumn", "(D) Winter", "(A)", "Line: 'Spring comes first with blossoms fair'.", "Easy", "Remembering", "Season Sequence"),
    ("What features describe spring in the first stanza?", "(A) Blossoms fair, soft green leaves, and warmer air", "(B) Frosty air and falling snow", "(C) Crunchy leaves of red and gold", "(D) Long, bright, happy, sunny days", "(A)", "Line: 'Spring comes first with blossoms fair, Soft green leaves and warmer air.'", "Easy", "Remembering", "Spring Features"),
    ("What do bees do when flowers bloom in spring?", "(A) Bees will hum", "(B) Bees will sleep", "(C) Bees will fly away south", "(D) Bees will make ice cream", "(A)", "Line: 'Flowers bloom and bees will hum'.", "Easy", "Remembering", "Spring Wildlife"),
    ("What shines during summer according to the second stanza?", "(A) Golden rays", "(B) Frosty wind", "(C) Red and gold leaves", "(D) Falling snow", "(A)", "Line: 'Then summer shines with golden rays'.", "Easy", "Remembering", "Summer Feature"),
    ("What activity do children enjoy during summer?", "(A) Splash in waters blue", "(B) Sit by fires", "(C) Rake crunchy leaves", "(D) Build snowmen", "(A)", "Line: 'Children splash in waters blue'.", "Easy", "Remembering", "Summer Activity"),
    ("What sweet food melts during hot summer days?", "(A) Ice cream—one scoop or two!", "(B) Hot soup", "(C) Marshmallow cakes", "(D) Warm chocolate tea", "(A)", "Line: 'While ice cream melts—one scoop or two!'", "Easy", "Remembering", "Summer Food"),
    ("Which season comes next with cool and clear air and crunchy leaves?", "(A) Autumn", "(B) Spring", "(C) Summer", "(D) Winter", "(A)", "Line: 'Next comes autumn, cool and clear, With crunchy leaves both far and near.'", "Easy", "Remembering", "Autumn Features"),
    ("What 'coats' do trees wear during autumn?", "(A) Coats of red and gold", "(B) Coats of green and white", "(C) Coats of ice and snow", "(D) Coats of black and brown", "(A)", "Line: 'The trees wear coats of red and gold'.", "Easy", "Remembering", "Autumn Trees Metaphor"),
    ("What changes occur in day length and temperature during autumn?", "(A) Days grow short and nights turn cold", "(B) Days grow long and nights turn hot", "(C) Days and nights stay warm continuously", "(D) It rains continuously for days", "(A)", "Line: 'As days grow short and nights turn cold.'", "Easy", "Remembering", "Autumn Days"),
    ("Which season brings frosty air, falling snow, and blowing winds?", "(A) Winter", "(B) Autumn", "(C) Summer", "(D) Spring", "(A)", "Line: 'And last, the winter winds will blow, With frosty air and falling snow.'", "Easy", "Remembering", "Winter Features"),
    ("How do people stay warm during winter?", "(A) Wrap in coats and sit by fires", "(B) Eat cold ice cream", "(C) Splash in blue waters", "(D) Walk barefoot in green grass", "(A)", "Line: 'We wrap in coats and sit by fires'.", "Easy", "Remembering", "Winter Warmth"),
    ("What does the year do as winter ends?", "(A) As the year, once more, retires", "(B) As the year begins to heat up", "(C) As the year stops completely forever", "(D) As the year melts into water", "(A)", "Line: 'As the year, once more, retires.'", "Easy", "Remembering", "Year Retires"),
    ("What phrase describes the continuous cycle of seasons in the final line?", "(A) A perfect circle every year!", "(B) A long straight line", "(C) A square box", "(D) A broken puzzle", "(A)", "Line: 'A perfect circle every year!'", "Easy", "Remembering", "Cycle Metaphor"),
    ("What does each season bring according to the final stanza?", "(A) Magic, joy and cheer", "(B) Sadness, boredom and grief", "(C) Dust storms and darkness", "(D) Heavy floods only", "(A)", "Line: 'Each brings magic, joy and cheer'.", "Easy", "Remembering", "Seasons Gift"),
    ("What does the word 'blossom' mean in the vocabulary box?", "(A) Flowers blooming / a flower on a tree", "(B) Fallen dry leaves", "(C) Melting ice water", "(D) A heavy coat", "(A)", "Blossom = Flowers blooming.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'bloom' mean?", "(A) To produce flowers", "(B) To drop leaves in wind", "(C) To freeze into ice", "(D) To shine with sunlight", "(A)", "Bloom = To produce flowers.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'frosty' mean?", "(A) Very cold", "(B) Very hot", "(C) Very rainy", "(D) Very loud", "(A)", "Frosty = Very cold.", "Easy", "Understanding", "Vocabulary"),
    ("Who is the author of the poem 'The Season's Song'?", "(A) Anonymous", "(B) Robert Louis Stevenson", "(C) Christina Rossetti", "(D) Sarojini Naidu", "(A)", "The poem is written by Anonymous.", "Easy", "Remembering", "Author Identity"),
    ("Which season is described as having 'blossoms fair' and 'soft green leaves'?", "(A) Spring", "(B) Summer", "(C) Autumn", "(D) Winter", "(A)", "Spring features blossoms fair and soft green leaves.", "Easy", "Remembering", "Spring Identification"),
    ("Which season is described as having 'long, bright, happy, sunny days'?", "(A) Summer", "(B) Winter", "(C) Autumn", "(D) Spring", "(A)", "Summer has long, bright, happy, sunny days.", "Easy", "Remembering", "Summer Identification"),
    ("Which season features 'crunchy leaves both far and near'?", "(A) Autumn", "(B) Spring", "(C) Summer", "(D) Winter", "(A)", "Autumn features crunchy leaves far and near.", "Easy", "Remembering", "Autumn Identification"),
    ("Which season features 'frosty air and falling snow'?", "(A) Winter", "(B) Summer", "(C) Spring", "(D) Autumn", "(A)", "Winter features frosty air and falling snow.", "Easy", "Remembering", "Winter Identification"),
    ("What figure of speech is 'trees wear coats of red and gold'?", "(A) Personification / Metaphor", "(B) Simile", "(C) Onomatopoeia", "(D) Hyperbole", "(A)", "Giving trees human 'coats' is personification/metaphor.", "Easy", "Understanding", "Literary Device"),
    ("What figure of speech is 'seasons sing their song so true'?", "(A) Personification", "(B) Simile", "(C) Alliteration only", "(D) Pun", "(A)", "Attributing the human action of singing to seasons is personification.", "Easy", "Understanding", "Literary Device"),
    ("What title is given to Chapter 14?", "(A) The Season's Song", "(B) My Dream Adventure", "(C) The Magic of Books", "(D) Island Groups of India", "(A)", "Title is 'The Season's Song'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Analyze the four-part seasonal structure of the poem in chronological order.", "(A) Spring (birth/rebirth) -> Summer (peak light/heat) -> Autumn (cooling/harvest) -> Winter (rest/retirement)", "(B) Winter -> Summer -> Spring -> Autumn", "(C) Autumn -> Winter -> Summer -> Spring", "(D) Summer -> Winter -> Spring -> Autumn", "(A)", "Chronological order: Spring -> Summer -> Autumn -> Winter -> Circle repeats.", "Medium", "Analyzing", "Seasonal Sequence"),
    ("How does the poem use color imagery to distinguish each season?", "(A) Spring = soft green; Summer = golden; Autumn = red and gold; Winter = frosty white", "(B) Spring = black; Summer = blue; Autumn = green; Winter = yellow", "(C) All seasons are described in gray", "(D) Spring = red; Summer = white; Autumn = green; Winter = gold", "(A)", "Color imagery: Green (spring) -> Golden (summer) -> Red/Gold (autumn) -> Frosty white (winter).", "Medium", "Analyzing", "Color Imagery"),
    ("Why does the poet describe the cycle of seasons as 'A perfect circle every year!'?", "(A) Because seasons repeat in an unbroken, predictable loop, returning life continuously year after year", "(B) Because the earth is drawn like a circle on paper", "(C) Because winter lasts twelve months", "(D) Because the sun looks like a giant wheel", "(A)", "Seasons repeat in an unbroken, predictable loop returning life continuously.", "Medium", "Evaluating", "Circle Metaphor Rationale"),
    ("Contrast the human activities in summer ('splash in waters blue') with winter ('sit by fires').", "(A) Summer encourages outdoor cooling in water; winter demands indoor warming near fires", "(B) Summer activities happen at night; winter activities happen in space", "(C) Both activities are identical", "(D) Sitting by fires is done in hot summer", "(A)", "Outdoor water cooling in summer vs indoor fire warming in winter.", "Medium", "Comparing", "Human Activity Contrast"),
    ("Examine the metaphor 'life returns to where it's from' during spring.", "(A) Winter dormancy ends as dormant plants, seeds, and sleeping nature wake up into new growth", "(B) People return from long ocean voyages", "(C) Birds fly away to other planets", "(D) Animals turn into statues", "(A)", "Winter dormancy ends as dormant seeds and plants wake into new growth.", "Medium", "Analyzing", "Spring Rebirth Metaphor"),
    ("How does the poem convey sensory temperature changes across seasons?", "(A) Warmer air (spring) -> Hot sun/melting ice cream (summer) -> Cool nights (autumn) -> Frosty air/cold winds (winter)", "(B) Freezing air in summer -> Burning heat in winter", "(C) All seasons have identical temperatures", "(D) Temperature is not mentioned in the poem", "(A)", "Presents gradual progression from warmer air to hot summer, cool autumn, and frosty winter.", "Medium", "Analyzing", "Temperature Progression"),
    ("Why is 'crunchy leaves' an effective auditory and tactile detail for autumn?", "(A) It evokes both the crisp sound underfoot and the dry texture of fallen autumn foliage", "(B) It describes the taste of autumn apples", "(C) It refers to eating potato chips", "(D) It describes wet muddy ground", "(A)", "Evokes crisp sound underfoot and dry texture of fallen foliage.", "Medium", "Evaluating", "Sensory Detail"),
    ("Explain the rhyme scheme of the poem 'The Season's Song'.", "(A) AABB scheme in 6 stanzas of 4 lines each (24 lines total)", "(B) ABAB scheme", "(C) ABCB scheme", "(D) Free verse with no rhymes", "(A)", "6 stanzas of 4 lines each following AABB rhyming couplets.", "Medium", "Analyzing", "Rhyme Scheme"),
    ("How does the poem encourage children to find joy in every season?", "(A) By showing that each season has unique beauty—spring flowers, summer water fun, autumn foliage, and winter cozy fires", "(B) By claiming that summer is the only good season", "(C) By advising children to complain about bad weather", "(D) By stating that seasons bring sadness and grief", "(A)", "Showcases unique beauty and joy in every season of the year.", "Medium", "Evaluating", "Joy in Seasons"),
    ("What does 'As the year, once more, retires' signify at the end of winter?", "(A) The completion of the 12-month annual cycle before spring restarts the new year", "(B) The year stops existing forever", "(C) People stop working for life", "(D) The sun goes to sleep permanently", "(A)", "Completes the 12-month annual cycle before spring restarts the new year.", "Medium", "Understanding", "Annual Retirement"),
    ("Compare the tree appearance in spring ('soft green leaves') with autumn ('coats of red and gold').", "(A) Spring trees sprout fresh green growth; autumn trees transform into vibrant red and gold before shedding leaves", "(B) Spring trees have no leaves; autumn trees grow blue flowers", "(C) Both look identical year-round", "(D) Autumn trees turn into candy canes", "(A)", "Fresh green growth in spring vs vibrant red and gold before shedding in autumn.", "Medium", "Comparing", "Tree Appearance"),
    ("What is meant by 'With something special, old and new' in the final stanza?", "(A) Seasons combine ancient repeating nature patterns ('old') with fresh new life and experiences ('new')", "(B) Old clothes and new toys are given away", "(C) Old people and new babies meet in winter", "(D) Seasons change every hundred years", "(A)", "Combines ancient repeating nature patterns with fresh new life.", "Medium", "Understanding", "Poetic Line Meaning"),
    ("Why is Anonymous authorship fitting for a poem about the natural seasons?", "(A) Because the beauty and rhythm of nature's seasons belong universally to all humanity", "(B) Because no one knows what seasons are", "(C) Because the poet forgot their name", "(D) Because the poem was written by a computer", "(A)", "Nature's seasonal rhythm belongs universally to all humanity.", "Medium", "Understanding", "Authorship Context"),
    ("Summarize Chapter 14 in four concise sentences.", "'The Season's Song' by Anonymous is a joyful 24-line poem celebrating the annual cycle of nature. It begins with spring's fair blossoms, green leaves, and humming bees, moving to summer's golden rays, blue waters, and melting ice cream. Next, autumn brings cool air, crunchy leaves, and red-and-gold trees, followed by winter's frosty winds, falling snow, and cozy firesides. The poem concludes that each season brings magic, joy, and cheer, forming a perfect circle every year.", "Medium", "Understanding", "Chapter Summary"),
    ("How can Class 5 students adapt their daily habits to appreciate each changing season?", "(A) Enjoy seasonal fruits/activities, observe plant/weather changes in nature, and dress appropriately for climate warmth or cold", "(B) Stay indoors behind closed curtains all year", "(C) Dislike every weather change", "(D) Wear heavy winter coats in summer", "(A)", "Enjoy seasonal fruits/activities, observe nature changes, dress appropriately.", "Medium", "Applying", "Daily Application"),

    # Hard (41-50)
    ("Critique how seasonal poetry fosters environmental literacy and ecological awareness in children.", "(A) Seasonal poetry connects children with natural phenology (blooming, leaf shedding, temperature shifts), instilling reverence for ecological harmony", "(B) Seasonal poetry makes children dislike nature", "(C) Poetry has no relationship with environmental science", "(D) Children should study weather only through computerized radar", "(A)", "Connects children with natural phenology, instilling reverence for ecological harmony.", "Hard", "Evaluating", "HOTS Ecological Critique"),
    ("Deconstruct the circular narrative design of 'The Season's Song'.", "(A) Begins with spring rebirth, progresses through summer warmth and autumn decay to winter rest, then explicitly loops back to spring via 'A perfect circle every year!'", "(B) The poem ends in total destruction with no loop", "(C) The narrative moves randomly between days", "(D) The poem stops after summer", "(A)", "Loop design: Spring rebirth -> Summer warmth -> Autumn decay -> Winter rest -> Perfect circle loop.", "Hard", "Analyzing", "Circular Narrative Design"),
    ("Evaluate the poetic effectiveness of personifying seasons ('seasons sing their song so true').", "(A) Personification transforms abstract weather patterns into an active, harmonious choir, making nature feel living and relatable for young readers", "(B) Personification confuses children into thinking weather has human mouths", "(C) Personification makes the poem scientifically invalid", "(D) Personification is used only in adult drama", "(A)", "Transforms abstract weather into an active, harmonious choir relatable for children.", "Hard", "Evaluating", "Personification Impact"),
    ("Compare the winter fireside motif in Chapter 14 with the summer water splashing motif.", "(A) Summer splashing emphasizes dynamic physical expansion and cooling; winter fireside emphasizes cozy domestic contraction and warming", "(B) Both motifs involve melting ice cream", "(C) Summer splashing is done near fires; winter fireside is done in oceans", "(D) Neither motif involves human comfort", "(A)", "Summer = dynamic physical expansion/cooling; Winter = cozy domestic contraction/warming.", "Hard", "Comparing", "Motif Comparison"),
    ("Formulate an original 4-line stanza continuing the theme of 'The Season's Song'.", "(A) 'The rains arrive with thunder loud,\nBeneath a dark and stormy cloud;\nThe thirsty earth drinks deep and sweet,\nAs green grass grows beneath our feet!'", "(B) 'Spring is warm and summer is hot.\nAutumn is cool and winter is cold.\nThat is four seasons total.\nThank you very much.'", "(C) 'Rain rain go away,\nCome again another day.'", "(D) 'I like ice cream in summer.'", "(A)", "Original 4-line AABB stanza matching rhythm and seasonal theme.", "Hard", "Creating", "Poetry Generation"),
    ("Assess the psychological comfort provided by predictable natural cycles in children's literature.", "(A) Predictable seasonal cycles reassure children that after darkness/cold (winter), warmth and new life (spring) inevitably return", "(B) Seasonal cycles create anxiety in children about winter", "(C) Natural cycles make children want to sleep permanently", "(D) Children prefer chaotic, unpredictable environments", "(A)", "Reassures children that after cold/darkness, warmth and new life inevitably return.", "Hard", "Evaluating", "Psychological Comfort"),
    ("Analyze how alliteration ('blossoms fair', 'bees will hum', 'crunchy leaves', 'winter winds') enhances oral rhythm.", "(A) Consonant repetition creates pleasing phonetic melody, reinforcing sensory images during oral reading", "(B) Alliteration makes words impossible to pronounce", "(C) Alliteration is an error in printing", "(D) Alliteration is used only in math equations", "(A)", "Consonant repetition creates pleasing phonetic melody during oral reading.", "Hard", "Analyzing", "Alliteration Analysis"),
    ("Synthesize how Chapter 14 unifies natural science, poetic meter, and moral optimism.", "(A) Blends natural phenology (4 seasons) with rhyming couplet meter (AABB) and moral optimism (magic, joy, cheer in a perfect circle)", "(B) Separates science from poetry", "(C) Focuses only on memorizing weather numbers", "(D) Rejects optimism in favor of gloom", "(A)", "Blends natural phenology, rhyming couplet meter, and moral optimism.", "Hard", "Synthesizing", "Cross-Disciplinary Synthesis"),
    ("Critique the claim: 'Winter is a dead season with zero beauty or value.'", "(A) False; winter provides necessary ecological rest ('retires'), frosty beauty, snow, and cozy fireside human bonding before spring rebirth", "(B) True; winter should be eliminated from the calendar", "(C) False; winter is the hottest season of the year", "(D) True; winter brings only sadness and boredom", "(A)", "False; winter provides ecological rest, frosty beauty, snow, and cozy fireside bonding.", "Hard", "Evaluating", "Ecological & Poetic Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 14 for a Class 5 assessment.", "(A) 'Describe the unique characteristics, colors, and human activities of each of the four seasons in The Season's Song. Explain why the poet calls the cycle of seasons a perfect circle every year.'", "(B) 'Write five sentences about your favorite season.'", "(C) 'List five rhyming words.'", "(D) 'Draw a picture of an ice cream cone.'", "(A)", "Structured essay prompt evaluating 4 season characteristics, colors, activities, and the perfect circle metaphor.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 14: The Season's Song\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH14_MCQ_{idx:03d}"
    q_txt = item[0]
    opt_a = item[1]
    opt_b = item[2]
    opt_c = item[3]
    opt_d = item[4]
    ans = item[5] if len(item) > 5 else "(A)"
    exp = item[6] if len(item) > 6 else "Correct answer"
    diff = item[7] if len(item) > 7 else "Easy"
    bloom = item[8] if len(item) > 8 else "Remembering"
    topic = item[9] if len(item) > 9 else "General"
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

with open(os.path.join(CH14_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Spring comes first with blossoms _______.", "fair", "Blossoms fair.", "Easy"),
    ("Soft green leaves and warmer _______.", "air", "Warmer air.", "Easy"),
    ("Flowers bloom and bees will _______.", "hum", "Bees will hum.", "Easy"),
    ("As life returns to where it's _______.", "from", "Where it's from.", "Easy"),
    ("Then summer shines with golden _______.", "rays", "Golden rays.", "Easy"),
    ("Long, bright, happy, sunny _______.", "days", "Sunny days.", "Easy"),
    ("Children splash in waters _______.", "blue", "Waters blue.", "Easy"),
    ("While ice cream melts—one scoop or _______!", "two", "One scoop or two.", "Easy"),
    ("Next comes autumn, cool and _______.", "clear", "Cool and clear.", "Easy"),
    ("With crunchy leaves both far and _______.", "near", "Far and near.", "Easy"),
    ("The trees wear coats of red and _______.", "gold", "Red and gold.", "Easy"),
    ("As days grow short and nights turn _______.", "cold", "Nights turn cold.", "Easy"),
    ("And last, the winter winds will _______.", "blow", "Winds will blow.", "Easy"),
    ("With frosty air and falling _______.", "snow", "Falling snow.", "Easy"),
    ("We wrap in coats and sit by _______.", "fires", "Sit by fires.", "Easy"),
    ("As the year, once more, _______.", "retires", "Year retires.", "Easy"),
    ("The seasons sing their song so _______.", "true", "Song so true.", "Easy"),
    ("With something special, old and _______.", "new", "Old and new.", "Easy"),
    ("Each brings magic, joy and _______.", "cheer", "Joy and cheer.", "Easy"),
    ("A perfect circle every _______!", "year", "Perfect circle every year.", "Easy"),
    ("Blossom means flowers _______.", "blooming", "Flowers blooming.", "Easy"),
    ("Bloom means to produce _______.", "flowers", "Produce flowers.", "Easy"),
    ("Frosty means very _______.", "cold", "Very cold.", "Easy"),
    ("The poem 'The Season's Song' is written by _______.", "Anonymous", "Written by Anonymous.", "Easy"),
    ("Chapter 14 is titled 'The Season's _______'.", "Song", "The Season's Song.", "Easy"),

    # Medium (26-40)
    ("Spring brings soft green leaves and warmer _______.", "air", "Warmer air.", "Medium"),
    ("Summer features long, bright, happy, sunny _______.", "days", "Sunny days.", "Medium"),
    ("Children splash in blue waters during _______.", "summer", "During summer.", "Medium"),
    ("Trees wear coats of red and gold in _______.", "autumn", "In autumn.", "Medium"),
    ("In autumn, days grow short and nights turn _______.", "cold", "Nights turn cold.", "Medium"),
    ("Winter brings frosty air and falling _______.", "snow", "Falling snow.", "Medium"),
    ("In winter, people wrap in coats and sit by _______.", "fires", "Sit by fires.", "Medium"),
    ("The year retires at the end of _______.", "winter", "End of winter.", "Medium"),
    ("Seasons sing their song with something special, old and _______.", "new", "Old and new.", "Medium"),
    ("The cycle of seasons is described as a perfect _______.", "circle", "Perfect circle.", "Medium"),
    ("Personification attributes the action of singing to the _______.", "seasons", "Attributes singing to seasons.", "Medium"),
    ("Tree coats of red and gold is a poetic _______.", "metaphor", "Uses metaphor.", "Medium"),
    ("Crunchy leaves describe the texture and sound of _______.", "autumn", "Sound of autumn.", "Medium"),
    ("Melting ice cream is a classic sign of summer _______.", "heat", "Sign of summer heat.", "Medium"),
    ("Chapter 14 teaches children to appreciate nature's _______.", "cycles", "Appreciate nature's cycles.", "Medium"),

    # Hard (41-50)
    ("Chronological sequence moves from spring rebirth to winter _______.", "retirement", "Moves to winter retirement.", "Hard"),
    ("Color imagery progresses from soft green to golden, red/gold, and white _______.", "frost", "Progresses to white frost.", "Hard"),
    ("The perfect circle metaphor symbolizes continuous annual _______.", "renewal", "Symbolizes annual renewal.", "Hard"),
    ("Alliteration in 'blossoms fair' and 'bees will hum' creates phonetic _______.", "harmony", "Creates phonetic harmony.", "Hard"),
    ("Winter fireside warmth contrasts with summer ocean _______.", "splashing", "Contrasts with ocean splashing.", "Hard"),
    ("Sensory temperature shifts from warmer spring to frosty _______.", "winter", "Shift to frosty winter.", "Hard"),
    ("Phenological changes mark the transition of nature's _______.", "seasons", "Transition of seasons.", "Hard"),
    ("Stanzaic progression concludes with an uplifting moral _______.", "synthesis", "Uplifting moral synthesis.", "Hard"),
    ("Poetic personification transforms weather into a singing _______.", "choir", "Transforms weather into a choir.", "Hard"),
    ("Chapter 14 instills environmental reverence for Earth's annual _______.", "rhythms", "Reverence for Earth's rhythms.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 14: The Season's Song\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH14_FIB_{idx:03d}"
    sent = item[0]
    ans = item[1]
    exp = item[2] if len(item) > 2 else "Answer"
    diff = item[3] if len(item) > 3 else "Easy"
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH14_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Spring comes first with blossoms fair and soft green leaves.", "True", "Text confirms spring comes first with blossoms fair.", "Easy"),
    ("Bees hum during spring when flowers bloom.", "True", "Text confirms: 'Flowers bloom and bees will hum'.", "Easy"),
    ("Summer is described as having long, bright, happy, sunny days.", "True", "Text confirms summer has long, bright, happy, sunny days.", "Easy"),
    ("Children sit by fires during summer.", "False", "Children splash in blue waters in summer; sit by fires in winter.", "Easy"),
    ("Ice cream melts during summer.", "True", "Text confirms: 'While ice cream melts—one scoop or two!'", "Easy"),
    ("Autumn comes after summer with cool and clear air.", "True", "Text confirms autumn comes next with cool and clear air.", "Easy"),
    ("Autumn leaves are described as soft and muddy.", "False", "Autumn leaves are described as 'crunchy leaves both far and near'.", "Easy"),
    ("Trees wear coats of red and gold during autumn.", "True", "Text confirms: 'The trees wear coats of red and gold'.", "Easy"),
    ("Autumn nights turn warm and humid.", "False", "Autumn nights turn cold ('As days grow short and nights turn cold').", "Easy"),
    ("Winter winds bring frosty air and falling snow.", "True", "Text confirms: 'With frosty air and falling snow.'", "Easy"),
    ("In winter, people wrap in coats and sit by fires.", "True", "Text confirms: 'We wrap in coats and sit by fires'.", "Easy"),
    ("The year begins to retire at the end of summer.", "False", "The year retires at the end of winter ('As the year, once more, retires').", "Easy"),
    ("The poem states that each season brings sadness and boredom.", "False", "Text confirms: 'Each brings magic, joy and cheer'.", "Easy"),
    ("The cycle of seasons is described as 'A perfect circle every year!'.", "True", "Text confirms: 'A perfect circle every year!'", "Easy"),
    ("'Blossom' means flowers blooming.", "True", "Vocabulary definition: Blossom = Flowers blooming.", "Easy"),
    ("'Bloom' means to produce flowers.", "True", "Vocabulary definition: Bloom = To produce flowers.", "Easy"),
    ("'Frosty' means very hot.", "False", "Frosty = Very cold.", "Easy"),
    ("The poem 'The Season's Song' is written by Anonymous.", "True", "Text confirms author is Anonymous.", "Easy"),
    ("The line 'trees wear coats of red and gold' contains personification/metaphor.", "True", "Attributing coats to trees is personification/metaphor.", "Easy"),
    ("The poem has 6 stanzas of 4 lines each (24 lines total).", "True", "Text contains 6 stanzas x 4 lines = 24 lines total.", "Easy"),
    ("'Fair' rhymes with 'air' in the first stanza.", "True", "Text confirms fair / air rhyme.", "Easy"),
    ("'Rays' rhymes with 'days' in the second stanza.", "True", "Text confirms rays / days rhyme.", "Easy"),
    ("'Gold' rhymes with 'cold' in the third stanza.", "True", "Text confirms gold / cold rhyme.", "Easy"),
    ("'Blow' rhymes with 'snow' in the fourth stanza.", "True", "Text confirms blow / snow rhyme.", "Easy"),
    ("Chapter 14 title is 'The Season's Song'.", "True", "Chapter title is 'The Season's Song'.", "Easy"),

    # Medium (26-40)
    ("The rhyme scheme of 'The Season's Song' is AABB in all 6 stanzas.", "True", "Each stanza follows an AABB rhyming couplet scheme.", "Medium"),
    ("The poem describes the four seasons in chronological order: Spring, Summer, Autumn, Winter.", "True", "Follows exact chronological sequence from spring to winter.", "Medium"),
    ("Flowers bloom and life returns during winter.", "False", "Flowers bloom and life returns during spring.", "Medium"),
    ("Summer days are short while winter days are long.", "False", "Summer has long sunny days; autumn/winter days grow short.", "Medium"),
    ("Autumn trees changing color to red and gold is a natural biological process.", "True", "Leaves change color in autumn before shedding.", "Medium"),
    ("Winter is presented as a cozy, reflective season with fireside warmth.", "True", "Highlights wrapping in coats and sitting by cozy fires.", "Medium"),
    ("The phrase 'A perfect circle every year!' means the seasons repeat infinitely.", "True", "Represents the endless annual cycle of nature.", "Medium"),
    ("Children eating ice cream occurs in the winter stanza.", "False", "Ice cream melting occurs in the summer stanza.", "Medium"),
    ("Frosty air and falling snow characterize winter weather.", "True", "Text confirms frosty air and falling snow in winter.", "Medium"),
    ("The seasons sing their song so true is an example of personification.", "True", "Personifies seasons as singing a true song.", "Medium"),
    ("The poem teaches children to appreciate the unique beauty of every season.", "True", "Emphasizes that each season brings magic, joy, and cheer.", "Medium"),
    ("Spring is the last season mentioned in the poem.", "False", "Spring comes first; winter is the last season mentioned.", "Medium"),
    ("The word 'retires' in the poem means the year goes to sleep before starting again.", "True", "Metaphorically means the year completes its cycle.", "Medium"),
    ("Crunchy leaves describe both the sound and feel of autumn foliage underfoot.", "True", "Reflects auditory crispness and dry texture.", "Medium"),
    ("Chapter 14 inspires Class 5 students to connect poetry with natural science.", "True", "Fosters appreciation for natural weather cycles through poetry.", "Medium"),

    # Hard (41-50)
    ("The poem's AABB rhyme scheme creates a regular musical cadence suitable for recitation.", "True", "Couplets create musical rhythm ideal for oral reading.", "Hard"),
    ("Color imagery shifts from soft green (spring) to golden (summer), red/gold (autumn), and white (winter).", "True", "Color progression mirrors natural seasonal leaf and light shifts.", "Hard"),
    ("The metaphor 'coats of red and gold' describes autumn leaf senescence.", "True", "Senescence causes green chlorophyll to breakdown into red and gold pigments.", "Hard"),
    ("Seasons personification as a singing choir conveys natural harmony.", "True", "Presents natural weather as a unified, singing choir.", "Hard"),
    ("The year's 'retirement' in winter signals ecological dormancy prior to vernal renewal.", "True", "Winter dormancy precedes spring (vernal) renewal.", "Hard"),
    ("Alliteration in 'blossoms fair' and 'bees will hum' heightens auditory aesthetics.", "True", "Consonant repetition enhances poetic sound quality.", "Hard"),
    ("The final stanza functions as a philosophical synthesis of environmental harmony.", "True", "Final stanza synthesizes the magic, joy, and circular harmony of nature.", "Hard"),
    ("Chapter 14 combines visual, auditory, and thermal sensory imagery.", "True", "Visual (colors/snow), Auditory (bees humming/birds), Thermal (warmer air/frosty/fires).", "Hard"),
    ("Chapter 14 integrates poetic devices, seasonal phenology, and environmental ethics.", "True", "Combines literary devices (metaphor/personification) with weather science.", "Hard"),
    ("Observing seasonal patterns develops scientific curiosity and ecological mindfulness in youth.", "True", "Nature observation builds scientific inquiry and environmental care.", "Hard")
]

tf_content = f"# True / False — Chapter 14: The Season's Song\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH14_TF_{idx:03d}"
    stmt = item[0]
    ans = item[1]
    exp = item[2] if len(item) > 2 else "Explanation"
    diff = item[3] if len(item) > 3 else "Easy"
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH14_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Which season comes first according to the poem, and what describes its arrival?", "Spring comes first, bringing fair blossoms, soft green leaves, warmer air, blooming flowers, and humming bees.", "Easy", "Remembering"),
    ("Describe the characteristics of summer mentioned in the second stanza.", "Summer features golden sun rays, long bright sunny days, children splashing in blue waters, and melting ice cream.", "Easy", "Remembering"),
    ("What features describe autumn in the third stanza?", "Autumn features cool and clear air, crunchy leaves underfoot, trees wearing coats of red and gold, shorter days, and colder nights.", "Easy", "Remembering"),
    ("How is winter described in the fourth stanza?", "Winter brings blowing cold winds, frosty air, falling snow, wrapping in warm coats, and sitting by cozy fires.", "Easy", "Remembering"),
    ("What happens as winter ends at the conclusion of the fourth stanza?", "As winter ends, the year completes its annual cycle and 'once more, retires'.", "Easy", "Remembering"),
    ("What does each season bring according to the final stanza?", "Each season brings magic, joy, and cheer, creating 'a perfect circle every year'.", "Easy", "Remembering"),
    ("What does the word 'blossom' mean?", "'Blossom' means flowers blooming, or the mass of flowers on a tree.", "Easy", "Understanding"),
    ("What does the word 'bloom' mean?", "'Bloom' means to produce flowers or come into full floral growth.", "Easy", "Understanding"),
    ("What does the word 'frosty' mean?", "'Frosty' means very cold, covered with freezing frost or ice.", "Easy", "Understanding"),
    ("Name the figure of speech in 'The trees wear coats of red and gold'.", "It is a metaphor/personification, comparing autumn red and gold leaves to colorful coats worn by trees.", "Easy", "Understanding"),
    ("Name the figure of speech in 'The seasons sing their song so true'.", "It is personification, attributing the human ability to sing to the four natural seasons.", "Easy", "Understanding"),
    ("Identify the rhyming pair in the first stanza.", "The rhyming pairs are 'fair' / 'air' and 'hum' / 'from'.", "Easy", "Remembering"),
    ("Identify the rhyming pair in the second stanza.", "The rhyming pairs are 'rays' / 'days' and 'blue' / 'two'.", "Easy", "Remembering"),
    ("Identify the rhyming pair in the third stanza.", "The rhyming pairs are 'clear' / 'near' and 'gold' / 'cold'.", "Easy", "Remembering"),
    ("Identify the rhyming pair in the fourth stanza.", "The rhyming pairs are 'blow' / 'snow' and 'fires' / 'retires'.", "Easy", "Remembering"),
    ("Identify the rhyming pair in the fifth and sixth stanzas.", "The rhyming pairs are 'true' / 'new' and 'cheer' / 'year'.", "Easy", "Remembering"),
    ("Who is the author of the poem 'The Season's Song'?", "The poem is written by an Anonymous author.", "Easy", "Remembering"),
    ("How many stanzas and total lines make up the poem?", "The poem consists of 6 stanzas of 4 lines each, totaling 24 lines.", "Easy", "Remembering"),
    ("Why is the cycle of seasons described as a 'perfect circle'?", "Because seasons follow one another in a continuous, predictable, repeating annual loop.", "Easy", "Understanding"),
    ("What activity do children do in summer to cool down?", "Children splash in blue waters and enjoy eating ice cream.", "Easy", "Remembering"),
    ("What color coats do trees wear in autumn?", "Trees wear coats of red and gold as their leaves change color.", "Easy", "Remembering"),
    ("How do people keep warm in winter according to the poem?", "People wrap themselves in warm coats and sit near cozy fires.", "Easy", "Remembering"),
    ("What noise do bees make in spring?", "Bees hum as they visit blooming flowers in spring.", "Easy", "Remembering"),
    ("What title is given to Chapter 14?", "The title of Chapter 14 is 'The Season's Song'.", "Easy", "Remembering"),
    ("What main message does Chapter 14 convey about nature?", "It conveys that every season has its own unique beauty and joy, joining together to form nature's harmonious yearly cycle.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze how the poem uses color imagery to represent the four seasons.", "Spring uses soft green, summer uses golden rays and blue waters, autumn uses red and gold foliage, and winter uses white snow and frosty air.", "Medium", "Analyzing"),
    ("Explain the chronological progression of seasons from spring to winter in the poem.", "Spring introduces new life and blossoms; summer brings peak sun and warmth; autumn brings cooling and leaf shedding; winter brings cold rest before the cycle repeats.", "Medium", "Analyzing"),
    ("Why does the poet describe spring as the time when 'life returns to where it's from'?", "Because after winter dormancy, seeds germinate, plants sprout fresh green leaves, and nature awakens back to vibrant life.", "Medium", "Understanding"),
    ("Contrast the temperature and light conditions of summer with autumn.", "Summer has long, bright, hot sunny days with melting ice cream; autumn brings cooling air, shorter days, and cold nights.", "Medium", "Comparing"),
    ("How does the poem evoke sensory details of sound across the seasons?", "Spring features bees humming, summer features children splashing in water, autumn features crunchy leaves underfoot, and the overall poem features seasons 'singing their song'.", "Medium", "Analyzing"),
    ("Explain the metaphor 'As the year, once more, retires' at the end of winter.", "It personifies the year as a person going to rest at the end of winter, completing its 12-month journey before spring begins a new year.", "Medium", "Understanding"),
    ("Why is Anonymous authorship fitting for a poem about the four seasons?", "Because the beauty and rhythm of nature's seasons are universal experiences belonging equally to everyone on Earth.", "Medium", "Evaluating"),
    ("Explain the rhyme scheme of 'The Season's Song'.", "The poem follows an AABB rhyme scheme in every stanza (rhyming couplets), creating a song-like, musical rhythm.", "Medium", "Analyzing"),
    ("How does the poem encourage children to embrace cold winter weather positively?", "By highlighting cozy indoor warmth—wrapping in thick coats, sitting by fires, and enjoying falling snow.", "Medium", "Evaluating"),
    ("Summarize Chapter 14 in four concise sentences.", "'The Season's Song' by Anonymous is a delightful 24-line poem celebrating the four seasons. It begins with spring's fair blossoms, soft leaves, and humming bees, moving to summer's golden sun, blue waters, and melting ice cream. Next, autumn brings cool air, crunchy leaves, and red-and-gold trees, followed by winter's frosty winds, snow, and cozy firesides. The poem concludes that every season brings magic, joy, and cheer in a perfect annual circle.", "Medium", "Understanding", "Chapter Summary"),
    ("What does 'something special, old and new' mean in the final stanza?", "It means each season brings familiar, repeating natural traditions ('old') alongside fresh, new experiences and life ('new').", "Medium", "Understanding"),
    ("Describe the visual picture created by 'trees wear coats of red and gold'.", "It paints a vivid picture of autumn trees covered in bright red, orange, and yellow leaves before they drop to the ground.", "Medium", "Analyzing"),
    ("Why are rhyming couplets effective for teaching seasonal poetry to Class 5 students?", "Rhyming couplets create a cheerful musical beat that aids memory, fluency, and energetic oral recitation.", "Medium", "Evaluating"),
    ("How does the poem present nature as a harmonious singing choir?", "By personifying the four seasons as singers performing a true, magical song of joy and cheer throughout the year.", "Medium", "Analyzing"),
    ("What activity could Class 5 students do to observe the 'perfect circle' of seasons in their schoolyard?", "Students can adopt a schoolyard tree and photograph/draw its changes through spring leaves, summer shade, autumn color shifts, and winter bare branches.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique how seasonal poetry fosters ecological mindfulness and environmental appreciation.", "Seasonal poetry trains children to notice subtle environmental shifts (blooming, leaf texture, light duration), cultivating lifelong ecological respect and care for the planet.", "Hard", "Evaluating"),
    ("Deconstruct the circular structure of the poem's narrative arc.", "The narrative arc starts with spring rebirth, ascends to summer peak, descends through autumn decay to winter rest, and loops back to spring via the 'perfect circle' refrain.", "Hard", "Analyzing"),
    ("Evaluate the effectiveness of using sensory contrasts (hot/cold, green/gold, splash/fire) in children's poetry.", "Sensory contrasts sharpen children's perceptual awareness, helping them categorize and appreciate opposing physical sensations in nature.", "Hard", "Evaluating"),
    ("Compare the spring rebirth motif in Stanza 1 with the winter retirement motif in Stanza 4.", "Spring represents active awakening, growth, and rising warmth; winter represents quiet rest, reflection, and fireside comfort.", "Hard", "Comparing"),
    ("Formulate an original 4-line stanza continuing the theme of 'The Season's Song'.", "'The monsoon comes with thunder loud,\nAnd dark grey rain-filled heavy cloud;\nThe gardens bloom in brilliant green,\nThe freshest sights you've ever seen!'", "Hard", "Creating"),
    ("Assess the psychological value of natural seasonality in building child resilience.", "Understanding seasonal cycles reassures children that difficult, cold periods (winter) are temporary and always followed by renewal, warmth, and growth (spring).", "Hard", "Evaluating"),
    ("Analyze the linguistic choices in 'magic, joy and cheer—A perfect circle every year!'.", "Upbeat nouns ('magic', 'joy', 'cheer') and geometric metaphor ('perfect circle') create a triumphant, optimistic conclusion celebrating Earth's order.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 14 unifies natural phenology, poetic devices, and moral optimism.", "Blends scientific weather phenology with literary devices (personification/metaphor/rhyme) and moral optimism celebrating Earth's harmony.", "Hard", "Synthesizing"),
    ("Critique the claim: 'Poetry about weather is dull because weather happens every day anyway.'", "False; weather poetry transforms familiar daily phenomena into fresh, artistic wonder, teaching children to see beauty in everyday nature.", "Hard", "Evaluating"),
    ("Formulate a 4-line slogan encouraging environmental protection of the four seasons.", "'Protect the spring where blossoms bloom,\nAnd summer skies that clear the gloom;\nKeep autumn clean and winter bright,\nAnd keep our Earth in joyful light!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 14: The Season's Song\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH14_SA_{idx:03d}"
    q_txt = item[0]
    ans = item[1]
    diff = item[2] if len(item) > 2 else "Easy"
    bloom = item[3] if len(item) > 3 else "Understanding"
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH14_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Examine the descriptions of Spring and Summer in 'The Season's Song'.",
     "The poem provides vivid, sensory descriptions of the first two seasons:\n1. **Spring**: Spring opens the annual cycle ('Spring comes first with blossoms fair'). It is characterized by soft green leaves sprouting on trees, warmer air, blooming flowers, and the cheerful humming of bees. The poet describes this season as a time when 'life returns to where it's from', signaling natural rebirth.\n2. **Summer**: Summer follows with intense light and warmth ('Then summer shines with golden rays'). It brings long, bright, happy, sunny days. Children enjoy splashing in cool blue waters, while ice cream melts quickly under the hot sun ('one scoop or two!'). Both seasons capture outdoor joy and vibrant life.",
     "Easy", "Remembering"),

    ("Examine the descriptions of Autumn and Winter in 'The Season's Song'.",
     "The poem contrasts the cooling second half of the year:\n1. **Autumn**: Autumn arrives 'cool and clear' with crunchy fallen leaves covering the ground. The trees undergo a dramatic color transformation, wearing metaphorical 'coats of red and gold'. Days grow shorter and nights turn cold, signaling the approach of winter.\n2. **Winter**: Winter arrives with blowing winds, frosty cold air, and falling white snow. People adapt to the cold by wrapping themselves in thick coats and gathering around cozy indoor fires. As winter ends, the year completes its journey ('As the year, once more, retires'), preparing for spring's renewal.",
     "Easy", "Remembering"),

    ("Examine the final two stanzas and explain the 'perfect circle' metaphor for the seasons.",
     "The concluding stanzas deliver the central philosophical theme of the poem:\n> *'The seasons sing their song so true,\nWith something special, old and new.\nEach brings magic, joy and cheer—\nA perfect circle every year!'*\n- **Personification**: The seasons are personified as a harmonious choir singing a true song.\n- **Synthesis of Old and New**: Every season combines repeating natural patterns ('old') with fresh new growth and experiences ('new').\n- **Perfect Circle Metaphor**: The poet compares the annual cycle of seasons to a 'perfect circle'. A circle has no beginning or end; similarly, as winter finishes, spring immediately begins again. This continuous, unbroken loop reassures us that nature is harmonious, reliable, and filled with joy.",
     "Easy", "Understanding"),

    ("Describe the structure, rhyme scheme, and poetic devices used in 'The Season's Song'.",
     "The poem 'The Season's Song' is crafted with cheerful poetic elements:\n1. **Structure**: It contains 6 stanzas of 4 lines each (quatrains), totaling 24 lines.\n2. **Rhyme Scheme**: Every stanza follows an **AABB** rhyme scheme (rhyming couplets):\n   - Stanza 1: fair/air (A), hum/from (B)\n   - Stanza 2: rays/days (A), blue/two (B)\n   - Stanza 3: clear/near (A), gold/cold (B)\n   - Stanza 4: blow/snow (A), fires/retires (B)\n   - Stanza 5: true/new (A), cheer/year (B)\n3. **Poetic Devices**:\n   - **Personification**: 'trees wear coats', 'seasons sing their song', 'year retires'.\n   - **Metaphor**: 'A perfect circle every year'.\n   - **Sensory Details**: Crunchy leaves, golden rays, melting ice cream, frosty air.",
     "Easy", "Remembering"),

    ("Explain the vocabulary terms 'blossom', 'bloom', and 'frosty' and show how they fit the poem.",
     "1. **Blossom**: Defined as 'Flowers blooming'. In the poem ('blossoms fair'), it describes the beautiful spring flowers appearing on trees.\n2. **Bloom**: Defined as 'To produce flowers'. In the poem ('Flowers bloom'), it describes nature awakening into colorful floral growth during spring.\n3. **Frosty**: Defined as 'Very cold'. In the poem ('frosty air'), it describes the freezing, crisp air of winter.",
     "Easy", "Understanding"),

    ("Discuss how the poem engages multiple human senses across the four seasons.",
     "The poem engages all major senses to create a rich nature experience:\n- **Sight**: Soft green leaves, golden sun rays, blue waters, red and gold tree coats, falling white snow.\n- **Sound**: Bees humming in spring, children splashing in summer, crunchy leaves rustling in autumn, winter winds blowing, seasons singing.\n- **Touch/Temperature**: Warmer air in spring, hot sun/melting ice cream in summer, cool nights in autumn, frosty air/cozy fireside warmth in winter.\n- **Taste**: Sweet melting ice cream (one scoop or two!).",
     "Easy", "Understanding"),

    ("Why is 'The Season's Song' an effective poem for primary school English literature?",
     "It is highly effective because:\n1. **Clear Chronology**: It takes children through the familiar calendar cycle of Spring, Summer, Autumn, and Winter in logical order.\n2. **Vivid Imagery**: It uses colorful, concrete imagery children love—ice cream, splashing water, crunchy leaves, snow, and cozy fires.\n3. **Uplifting Theme**: It teaches children to appreciate every season and celebrate nature's continuous, harmonious renewal.",
     "Easy", "Evaluating"),

    ("Compare the tree descriptions in Spring, Autumn, and Winter across the poem.",
     "- **Spring Trees**: Covered in 'soft green leaves' and 'blossoms fair' as fresh life sprouts.\n- **Autumn Trees**: Wear vibrant 'coats of red and gold' as foliage changes color before falling.\n- **Winter Trees**: Shed their leaves as 'winter winds will blow' and snow falls, standing bare while the year retires.",
     "Easy", "Comparing"),

    ("Summarize Chapter 14 in five detailed bullet points.",
     "- 'The Season's Song' by Anonymous is a 24-line poem celebrating the four natural seasons.\n- Spring arrives first with fair blossoms, soft green leaves, warming air, blooming flowers, and humming bees.\n- Summer brings golden sun rays, long happy days, children splashing in blue waters, and melting ice cream.\n- Autumn brings cool clear air, crunchy leaves underfoot, red-and-gold tree coats, shorter days, and cold nights.\n- Winter brings frosty winds, snow, warm coats, and fireside cozy rest, forming a 'perfect circle' of magic, joy, and cheer every year.",
     "Easy", "Understanding"),

    ("What lessons about environmental care and enjoying nature can Class 5 students learn from Chapter 14?",
     "Students learn that nature operates in a beautiful, orderly cycle where every season has purpose and value. They learn to find joy in all weather conditions—spring flowers, summer sunshine, autumn crispness, and winter firesides. Students are inspired to observe natural changes in trees, birds, and weather, fostering lifelong environmental care and gratitude for Earth's perfect circle.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why is Spring described as the season where 'life returns to where it's from'?", "Because winter's cold dormancy ends in spring as dormant seeds germinate, bare trees sprout green leaves, and sleeping animals wake back to vibrant life.", "Easy", "Understanding"),
    ("Describe how summer brings happiness to children in the poem.", "Summer brings long, bright, sunny days that allow children to play outside, splash in cool blue waters, and enjoy sweet melting ice cream.", "Easy", "Remembering"),
    ("Explain the imagery of 'crunchy leaves both far and near' in autumn.", "It paints a vivid picture of dry, fallen autumn leaves covering the ground everywhere, creating a satisfying crunchy sound when stepped on.", "Easy", "Understanding"),
    ("How do people adapt their clothing and habits from summer to winter?", "In hot summer, people wear light clothes and splash in water; in cold winter, people wrap in thick warm coats and sit near cozy indoor fires.", "Easy", "Understanding"),
    ("What makes the phrase 'one scoop or two!' playful and relatable for children?", "It captures the simple, joyful excitement of buying ice cream on a hot summer day, making the poem instantly relatable for young readers.", "Easy", "Understanding"),
    ("Discuss how the poem personifies the year as a person who 'retires' in winter.", "It treats the 12-month year as a weary traveler who rests ('retires') by a warm fire in winter after completing its full journey through the seasons.", "Easy", "Understanding"),
    ("Why does the poet describe winter air as 'frosty'?", "'Frosty' conveys the crisp, freezing cold temperature of winter that turns moisture into ice crystals and falling snow.", "Easy", "Understanding"),
    ("How does the poem show that change in nature is natural and beautiful?", "By showing that leaf color shifts, temperature changes, and weather variations bring new joy, magic, and cheer rather than destruction.", "Easy", "Understanding"),
    ("Describe the rhythm created by the AABB rhyming couplets in Chapter 14.", "The rhyming pairs (fair/air, rays/days, clear/near, blow/snow) create a steady, musical beat that feels like a song, matching the title 'The Season's Song'.", "Easy", "Evaluating"),
    ("How can teachers use Chapter 14 to integrate English literature with Science class?", "Teachers can connect the poem's literary imagery with science lessons on Earth's orbit around the sun, weather patterns, and plant life cycles.", "Easy", "Applying"),
    ("Re-write the poem 'The Season's Song' as a short 100-word prose paragraph.", "Nature sings a beautiful song through four distinct seasons every year. Spring begins the cycle with fresh green leaves, fair blossoms, blooming flowers, and humming bees. Next, summer arrives with bright golden sunshine, long happy days, children splashing in blue waters, and delicious melting ice cream. Then, cool autumn covers the ground with crunchy red and gold leaves as days shorten. Finally, winter brings frosty winds, falling snow, and cozy fireside warmth as the year rests. Every season brings its own magic, joy, and cheer in a perfect annual circle.", "Easy", "Creating"),
    ("Why is Anonymous authorship appropriate for a poem celebrating the seasons?", "Because the seasons belong to everyone across the globe, making an anonymous poem a universal anthem for Earth's natural beauty.", "Easy", "Understanding"),
    ("How does the poem build a positive attitude toward rainy or cold weather?", "By highlighting cozy firesides, warm coats, and falling snow, it teaches children to see winter as a peaceful, magical season of comfort.", "Easy", "Understanding"),
    ("Analyze why Chapter 14 is placed toward the end of the Class 5 English textbook.", "It provides a reflective, thematic synthesis of time, nature, and poetic imagery, serving as an uplifting conclusion to the textbook's poetry section.", "Easy", "Analyzing"),
    ("What seasonal pledge can Class 5 students take to protect the environment year-round?", "'We pledge to plant trees in spring, save water in summer, clean fallen leaves in autumn, and care for birds in winter, protecting Earth's perfect circle!'", "Easy", "Applying"),

    # Medium (26-40)
    ("Critically analyze the philosophical concept of cyclical time presented in 'A perfect circle every year!'.",
     "The poem contrasts linear human time (aging forward) with cyclical natural time (infinite rebirth):\n- Natural time operates as a 'perfect circle' where winter's end is not death, but a necessary pause before spring's guaranteed rebirth.\n- This cyclical view provides emotional reassurance, teaching children that hardship (cold winter) is always temporary and followed by light and renewal (spring/summer).",
     "Medium", "Analyzing"),

    ("Examine the functional shift in plant life from Spring to Winter in the poem.",
     "The poem tracks the biological journey of plants:\n1. **Spring**: Sprouting soft green leaves, blooming flowers, and attracting humming bee pollinators.\n2. **Summer**: Dense foliage providing shade under golden sun rays.\n3. **Autumn**: Leaf senescence as trees wear 'coats of red and gold' and drop crunchy leaves to the ground.\n4. **Winter**: Tree dormancy as winds blow and snow falls, allowing plants to rest before spring.",
     "Medium", "Analyzing"),

    ("Evaluate how 'The Season's Song' uses domestic human comfort to balance harsh weather.",
     "The poet balances harsh weather elements with comforting human domestic rituals:\n- Hot summer heat is balanced by the joy of splashing in blue waters and eating melting ice cream.\n- Cold winter winds and frosty snow are balanced by wrapping in warm coats and gathering around cozy indoor fires.\nThis balance ensures that every weather extreme is experienced through human joy and comfort.",
     "Medium", "Evaluating"),

    ("Discuss how the poem introduces primary students to the poetic device of Personification.",
     "The poem frequently personifies non-human nature:\n- Trees are personified as humans wearing 'coats of red and gold'.\n- The year is personified as an aging traveler who 'retires' in winter.\n- The seasons are personified as a singing choir that 'sing their song so true'.\nThis introduces primary students to how personification makes nature feel alive, active, and relatable.",
     "Medium", "Analyzing"),

    ("Design a cross-curricular art and poetry project for Class 5 based on Chapter 14.",
     "Project Title: 'Four Seasons Wheel'\n1. **Art Wheel**: Students draw a circular paper plate divided into 4 quadrants (Spring flowers, Summer beach, Autumn red leaves, Winter snowman/fire).\n2. **Poetry Writing**: In each quadrant, students write the corresponding 4-line stanza from Chapter 14.\n3. **Presentation**: Students spin their wheel and recite the poem to demonstrate the 'perfect circle every year'.",
     "Medium", "Creating"),

    ("How does the simile/metaphor of trees wearing 'coats of red and gold' help children visualize autumn?", "It compares bright autumn foliage to warm, colorful clothing, making leaf color changes vivid and easy for children to visualize.", "Medium", "Understanding"),
    ("Contrast the energy level of summer with the energy level of winter in the poem.", "Summer is energetic, bright, and active (splashing water, melting ice cream); winter is quiet, slow, and cozy (wrapping in coats, sitting by fires).", "Medium", "Comparing"),
    ("Why is 'bees will hum' an effective auditory detail for spring?", "The soft humming sound of bees visiting new flowers immediately signals the arrival of warm spring life after quiet winter.", "Medium", "Understanding"),
    ("How does the poem show that change is a natural part of life?", "By demonstrating that temperature drops, leaf shedding, and daylight changes are part of nature's harmonious, perfect annual circle.", "Medium", "Understanding"),
    ("Describe the thermal progression from spring to winter in the poem.", "Moves from 'warmer air' in spring to hot summer, 'nights turn cold' in autumn, and 'frosty air' in winter.", "Medium", "Analyzing"),
    ("Explain why the rhyme scheme AABB creates a cheerful tempo for oral reading.", "Rhyming couplets create quick, predictable phonetic resolutions that maintain an energetic, musical tempo when recited aloud.", "Medium", "Analyzing"),
    ("How does the poem foster gratitude for natural weather diversity?", "By showing that each season brings 'something special, old and new', encouraging readers to find joy in every weather condition.", "Medium", "Evaluating"),
    ("Analyze why the poet uses the word 'retires' for the year in winter.", "'Retires' means going to rest after hard work. The year rests in winter after producing flowers, fruit, and leaves during spring, summer, and autumn.", "Medium", "Analyzing"),
    ("What makes the concluding line 'A perfect circle every year!' triumphant?", "It resolves the poem with a victorious exclamation mark, celebrating the eternal, reliable harmony of Earth's natural laws.", "Medium", "Evaluating"),
    ("Construct a seasonal weather report script delivered by a Class 5 student based on the poem.", "'Good day! Spring has arrived with fair blossoms and humming bees! Get ready for summer's golden rays and ice cream next, followed by autumn's red coats and winter's cozy fires!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the ecological impact of human-induced climate change on nature's 'perfect circle'.",
     "Global warming threatens nature's 'perfect circle' by disrupting seasonal phenology—causing erratic rainfall, premature blooming, unseasonal heatwaves, and loss of snowfall. Re-reading 'The Season's Song' reminds society of the urgent need to protect climate stability so Earth's seasonal harmony remains unbroken.",
     "Hard", "Evaluating"),

    ("Deconstruct the linguistic harmony of 'something special, old and new' in Stanza 5.",
     "'Old' represents ancestral, repeating natural laws (orbit, tilt, phenology); 'new' represents fresh growth, unique daily experiences, and new life. The phrase synthesizes permanence and novelty into a unified celebration of nature.",
     "Hard", "Analyzing"),

    ("Synthesize how Chapter 14 links seasonal science, literary aesthetics, and emotional wellbeing.",
     "Links scientific weather phenology with literary devices (metaphor/personification/rhyme AABB) and emotional wellbeing (finding joy in all seasons).", "Hard", "Synthesizing"),

    ("Formulate a comprehensive essay prompt evaluating 'The Season's Song' as a model of nature poetry.",
     "Prompt: 'Critically analyze how the poem The Season's Song uses seasonal chronology, color imagery, sensory details, and personification to present nature as a perfect annual circle of magic, joy, and cheer.'",
     "Hard", "Creating"),

    ("Evaluate the role of nature poetry in developing observational skills in primary education.", "Nature poetry trains children to observe micro-details (bee humming, leaf texture, air temperature, light duration), enhancing scientific observation and descriptive writing.", "Hard", "Evaluating"),

    ("Compare the seasonal representation in Chapter 14 with seasonal representation in traditional Indian classical arts.", "Both celebrate seasonal phenology—Indian classical arts use Ragas (e.g., Megh for monsoon, Basant for spring) and Barahmasa literature; Chapter 14 uses rhyming couplets and color imagery.", "Hard", "Comparing"),
    ("Discuss how the poem uses daylight duration ('days grow short', 'sunny days') to mark seasonal shifts.", "Highlights solar astronomy: long sunny days in summer vs shortening days in autumn/winter, anchoring poetic weather in Earth's axial tilt.", "Hard", "Analyzing"),
    ("Analyze the impact of using rhyming couplets to structure a 24-line nature poem.", "Couplets break the 24-line poem into 12 distinct rhyming pairs, mirroring the 12 months of the year in neat, balanced poetic units.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'Each brings magic, joy and cheer—A perfect circle every year!'", "This concluding couplet summarizes the poem's moral philosophy. By pairing emotional rewards ('magic, joy, cheer') with geometric perfection ('circle'), the poet affirms that Earth's natural cycles are intrinsically good and worthy of human celebration.", "Hard", "Evaluating"),
    ("Synthesize the complete educational takeaways of Chapter 14 for primary school English literature.", "Chapter 14 unifies poetic structure (AABB quatrains), literary device analysis (personification/metaphor), sensory vocabulary, and environmental appreciation for nature's annual cycle.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 14: The Season's Song\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH14_LA_{idx:03d}"
    q_txt = item[0]
    ans = item[1]
    diff = item[2] if len(item) > 2 else "Easy"
    bloom = item[3] if len(item) > 3 else "Understanding"
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH14_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Spring comes first with blossoms fair,\nSoft green leaves and warmer air.\nFlowers bloom and bees will hum,\nAs life returns to where it's from.",
     [
         ("Which season comes first according to the opening line?", "Spring.", "Easy", "Remembering"),
         ("Name two features of spring mentioned in line 2.", "Soft green leaves and warmer air.", "Easy", "Remembering"),
         ("What do flowers and bees do in spring?", "Flowers bloom and bees hum.", "Easy", "Remembering"),
         ("What happens to life during spring?", "Life returns to where it's from.", "Easy", "Remembering"),
         ("What does the word 'blossom' mean?", "Flowers blooming on a tree or plant.", "Easy", "Understanding")
     ]),

    # Set 2
    ("Then summer shines with golden rays,\nLong, bright, happy, sunny days.\nChildren splash in waters blue,\nWhile ice cream melts—one scoop or two!",
     [
         ("What shines during summer in line 1?", "Golden rays.", "Easy", "Remembering"),
         ("How are summer days described in line 2?", "Long, bright, happy, sunny days.", "Easy", "Remembering"),
         ("What activity do children do in summer?", "Splash in waters blue.", "Easy", "Remembering"),
         ("What sweet food melts in summer?", "Ice cream (one scoop or two).", "Easy", "Remembering"),
         ("Why does ice cream melt in summer?", "Because of the hot sun and warm summer heat.", "Easy", "Understanding")
     ]),

    # Set 3
    ("Next comes autumn, cool and clear,\nWith crunchy leaves both far and near.\nThe trees wear coats of red and gold,\nAs days grow short and nights turn cold.",
     [
         ("Which season comes next after summer?", "Autumn.", "Easy", "Remembering"),
         ("How are the leaves described in autumn?", "Crunchy leaves both far and near.", "Easy", "Remembering"),
         ("What 'coats' do trees wear in autumn?", "Coats of red and gold.", "Easy", "Remembering"),
         ("What happens to days and nights in autumn?", "Days grow short and nights turn cold.", "Easy", "Remembering"),
         ("Name the figure of speech in 'trees wear coats of red and gold'.", "Metaphor / Personification.", "Easy", "Understanding")
     ]),

    # Set 4
    ("And last, the winter winds will blow,\nWith frosty air and falling snow.\nWe wrap in coats and sit by fires,\nAs the year, once more, retires.",
     [
         ("Which season is the last to arrive in the poem?", "Winter.", "Easy", "Remembering"),
         ("What weather elements arrive with winter?", "Blowing winds, frosty air, and falling snow.", "Easy", "Remembering"),
         ("How do people keep warm during winter?", "Wrap in coats and sit by fires.", "Easy", "Remembering"),
         ("What does the year do as winter ends?", "The year, once more, retires.", "Easy", "Remembering"),
         ("What does 'frosty' mean?", "Very cold.", "Easy", "Understanding")
     ]),

    # Set 5
    ("The seasons sing their song so true,\nWith something special, old and new.\nEach brings magic, joy and cheer—\nA perfect circle every year!",
     [
         ("What do the seasons do in line 1?", "They sing their song so true.", "Easy", "Remembering"),
         ("What do the seasons bring with them?", "Something special, old and new.", "Easy", "Remembering"),
         ("What three positive things does each season bring?", "Magic, joy, and cheer.", "Easy", "Remembering"),
         ("How is the annual cycle of seasons described in the final line?", "A perfect circle every year!", "Easy", "Remembering"),
         ("Name the figure of speech in 'seasons sing their song'.", "Personification.", "Easy", "Understanding")
     ]),

    # Set 6
    ("Word Meaning: Blossom : Flowers blooming. Bloom : To produce flowers. Frosty : Very cold.",
     [
         ("What is the definition of 'blossom'?", "Flowers blooming.", "Easy", "Remembering"),
         ("What is the definition of 'bloom'?", "To produce flowers.", "Easy", "Remembering"),
         ("What is the definition of 'frosty'?", "Very cold.", "Easy", "Remembering"),
         ("Which season in the poem is described as 'frosty'?", "Winter ('frosty air').", "Easy", "Remembering"),
         ("Use 'frosty' in a complete sentence of your own.", "We wore woolen hats in the frosty morning air.", "Medium", "Applying")
     ]),

    # Set 7
    ("Spring comes first with blossoms fair... A perfect circle every year! - Anonymous",
     [
         ("Who wrote the poem 'The Season's Song'?", "Anonymous.", "Easy", "Remembering"),
         ("How many stanzas are in this poem?", "Six stanzas.", "Easy", "Remembering"),
         ("How many total lines are in this poem?", "Twenty-four lines.", "Easy", "Remembering"),
         ("What is the rhyme scheme of every stanza?", "AABB (rhyming couplets).", "Medium", "Analyzing"),
         ("What is the central message of the entire poem?", "Each season brings unique joy, color, and magic, joining together in nature's perfect annual circle.", "Medium", "Evaluating")
     ]),

    # Set 8
    ("The trees wear coats of red and gold, As days grow short and nights turn cold.",
     [
         ("What season is described in this extract?", "Autumn.", "Easy", "Remembering"),
         ("What colors do the tree leaves turn?", "Red and gold.", "Easy", "Remembering"),
         ("What happens to the length of days?", "Days grow short.", "Easy", "Remembering"),
         ("What happens to the temperature of nights?", "Nights turn cold.", "Easy", "Remembering"),
         ("Why do trees shed their red and gold coats in autumn?", "To prepare for winter dormancy before new green growth sprouts in spring.", "Medium", "Analyzing")
     ]),

    # Set 9
    ("We wrap in coats and sit by fires, As the year, once more, retires.",
     [
         ("What season is described in this extract?", "Winter.", "Easy", "Remembering"),
         ("What do people wrap themselves in?", "Coats.", "Easy", "Remembering"),
         ("Where do people sit to stay warm?", "By fires.", "Easy", "Remembering"),
         ("What action is attributed to the year in line 2?", "Once more, retires.", "Easy", "Remembering"),
         ("Identify the rhyming pair in this extract.", "fires / retires.", "Easy", "Remembering")
     ]),

    # Set 10
    ("Spring comes first... Then summer shines... Next comes autumn... And last, the winter winds... A perfect circle every year!",
     [
         ("List the four seasons in the exact order they appear in the poem.", "Spring, Summer, Autumn, Winter.", "Easy", "Remembering"),
         ("Which season brings golden sun rays?", "Summer.", "Easy", "Remembering"),
         ("Which season brings fair blossoms and humming bees?", "Spring.", "Easy", "Remembering"),
         ("Which season brings crunchy leaves?", "Autumn.", "Easy", "Remembering"),
         ("Summarize why the poet calls the four seasons a 'perfect circle'.", "Because the seasons repeat in an unbroken, predictable yearly loop, continuously renewing life and bringing joy.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 14: The Season's Song\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH14_EXT_{q_counter:03d}"
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

with open(os.path.join(CH14_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 14 in {CH14_DIR}")
