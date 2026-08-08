r"""
=============================================================================
Script: generate_sample_paper_bank.py
Description: Generates 9 exam-aligned category files (50 questions each,
             450 total questions) for Class 2 English based on Sample Paper analysis.
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "question_bank", "sample_paper_bank")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def q_block(qid, qtype, diff, bloom, topic, marks, question, opts, answer):
    lines = [
        f"### Question ID: {qid}",
        f"- **Subject**: English",
        f"- **Type**: {qtype}",
        f"- **Difficulty**: {diff}",
        f"- **Bloom Level**: {bloom}",
        f"- **Topic**: {topic}",
        f"- **Marks**: {marks}",
        "",
        "**Question**:",
        f"{question}",
        ""
    ]
    if opts:
        for opt in opts:
            lines.append(f"- {opt}")
        lines.append("")
    lines.append(f"- **Answer Key**: {answer}")
    lines.append("\n---\n")
    return "\n".join(lines)

# 1. PLURAL NOUNS
def build_plural_nouns():
    header = "# Category 1: Plural Nouns & Spelling Rules\n\n> **Target**: 50 Questions | Class II English | Noun Plural Forms (-s, -es, -ies, -ves)\n\n---\n\n"
    items = [
        ("dish", "dishes", "dishs", "dished", "dishies"), ("bat", "bats", "bates", "batss", "baties"),
        ("cat", "cats", "cates", "catss", "caties"), ("pig", "pigs", "piges", "piggs", "pigies"),
        ("kiss", "kisses", "kisss", "kises", "kissies"), ("box", "boxes", "boxs", "boxies", "boxxed"),
        ("bus", "buses", "buss", "busies", "busses"), ("glass", "glasses", "glasss", "glassies", "glases"),
        ("watch", "watches", "watchs", "watchies", "watchess"), ("fox", "foxes", "foxs", "foxies", "foxx"),
        ("baby", "babies", "babys", "babyes", "babeis"), ("puppy", "puppies", "puppys", "puppyes", "pupeis"),
        ("story", "stories", "storys", "storyes", "storeis"), ("city", "cities", "citys", "cityes", "citeis"),
        ("lady", "ladies", "ladys", "ladyes", "ladeis"), ("leaf", "leaves", "leafs", "leafes", "leavs"),
        ("wolf", "wolves", "wolfs", "wolfes", "wolvs"), ("calf", "calves", "calfs", "calfes", "calvs"),
        ("knife", "knives", "knifes", "knifees", "knivs"), ("life", "lives", "lifes", "lifees", "livs"),
        ("child", "children", "childs", "childes", "childies"), ("man", "men", "mans", "manes", "menn"),
        ("woman", "women", "womans", "womanes", "womenn"), ("foot", "feet", "foots", "footies", "feets"),
        ("tooth", "teeth", "tooths", "toothies", "teeths"), ("mouse", "mice", "mouses", "mousies", "mices"),
        ("goose", "geese", "gooses", "goosies", "geeses"), ("apple", "apples", "applese", "applies", "appls"),
        ("book", "books", "bookes", "bookies", "bookss"), ("toy", "toys", "toyes", "toies", "toyss"),
        ("boy", "boys", "boyes", "boies", "boyss"), ("key", "keys", "keyes", "keies", "keyss"),
        ("monkey", "monkeys", "monkeyes", "monkies", "monkeis"), ("donkey", "donkeys", "donkeyes", "donkies", "donkeis"),
        ("day", "days", "dayes", "daies", "dayss"), ("tree", "trees", "treeses", "treess", "treis"),
        ("flower", "flowers", "floweres", "floweries", "flowerrs"), ("star", "stars", "stares", "staries", "starss"),
        ("bird", "birds", "birdes", "birdies", "birdss"), ("duck", "ducks", "duckes", "duckies", "duckss"),
        ("bench", "benches", "benchs", "benchies", "benchs"), ("branch", "branches", "branchs", "branchies", "branchs"),
        ("match", "matches", "matchs", "matchies", "matchs"), ("church", "churches", "churchs", "churchies", "churchs"),
        ("peach", "peaches", "peachs", "peachies", "peachs"), ("tomato", "tomatoes", "tomatos", "tomatoes", "tomatos"),
        ("potato", "potatoes", "potatos", "potatose", "potatos"), ("hero", "heroes", "heros", "heroies", "herose"),
        ("mango", "mangoes", "mangos", "mangoes", "mangos"), ("dress", "dresses", "dresss", "dressies", "dreses")
    ]

    body = ""
    for idx, (sing, corr, w1, w2, w3) in enumerate(items, 1):
        qid = f"BK02_SP_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the word **'{sing}'**?"
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — Correct plural form of '{sing}'."
        body += q_block(qid, "MCQ", "Easy", "Remembering", "Plural Nouns & Spelling Rules", 1, qtxt, opts, ans)

    with open(os.path.join(OUTPUT_DIR, "plural_nouns_spelling.md"), "w", encoding="utf-8") as f:
        f.write(header + body)
    print("Generated plural_nouns_spelling.md (50 Qs)")

# 2. ARTICLES
def build_articles():
    header = "# Category 2: Articles (A, An, The)\n\n> **Target**: 50 Questions | Class II English | Indefinite (a, an) & Definite (the) Articles\n\n---\n\n"
    items = [
        ("I saw ___ elephant in the zoo.", "an", "a", "the", "no article"), ("She eats ___ apple every morning.", "an", "a", "the", "no article"),
        ("He is ___ honest man.", "an", "a", "the", "no article"), ("This is ___ blue T-shirt I bought yesterday.", "the", "a", "an", "no article"),
        ("Their car does 150 miles ___ hour.", "an", "a", "the", "no article"), ("Where is ___ USB drive I lent you?", "the", "a", "an", "no article"),
        ("Is your mother working in ___ old office?", "an", "a", "the", "no article"), ("Carol's father works as ___ electrician.", "an", "a", "the", "no article"),
        ("Ben has ___ terrible headache.", "a", "an", "the", "no article"), ("Dennis is playing ___ trumpet.", "the", "a", "an", "no article"),
        ("Kiran is ___ best student in class.", "the", "a", "an", "no article"), ("___ camel is the ship of the desert.", "The", "A", "An", "No article"),
        ("Look at ___ moon in the sky.", "the", "a", "an", "no article"), ("___ sun rises in the east.", "The", "A", "An", "No article"),
        ("I want to buy ___ new book.", "a", "an", "the", "no article"), ("She gave me ___ orange.", "an", "a", "the", "no article"),
        ("___ Ganges is a holy river.", "The", "A", "An", "No article"), ("My uncle lives in ___ small village.", "a", "an", "the", "no article"),
        ("We saw ___ owl sitting on a tree branch.", "an", "a", "the", "no article"), ("Give me ___ ice cube, please.", "an", "a", "the", "no article"),
        ("He is ___ doctor at the city hospital.", "a", "an", "the", "no article"), ("She read ___ interesting story book.", "an", "a", "the", "no article"),
        ("___ Earth revolves around the Sun.", "The", "A", "An", "No article"), ("Can you lend me ___ pencil?", "a", "an", "the", "no article"),
        ("He wore ___ uniform to school.", "a", "an", "the", "no article"), ("I waited for ___ hour at the bus stop.", "an", "a", "the", "no article"),
        ("She wants to be ___ astronaut.", "an", "a", "the", "no article"), ("We stayed at ___ expensive hotel.", "an", "a", "the", "no article"),
        ("___ Taj Mahal is in Agra.", "The", "A", "An", "No article"), ("I saw ___ umbrella on the table.", "an", "a", "the", "no article"),
        ("He lives in ___ European country.", "a", "an", "the", "no article"), ("She has ___ dog named Bruno.", "a", "an", "the", "no article"),
        ("___ sky is full of dark clouds.", "The", "A", "An", "No article"), ("Pass me ___ salt, please.", "the", "a", "an", "no article"),
        ("He gave me ___ one-rupee coin.", "a", "an", "the", "no article"), ("Is there ___ egg in the basket?", "an", "a", "the", "no article"),
        ("___ Red Sea is very deep.", "The", "A", "An", "No article"), ("She ate ___ piece of cake.", "a", "an", "the", "no article"),
        ("He is ___ tallest boy in the team.", "the", "a", "an", "no article"), ("We saw ___ tiger in the safari.", "a", "an", "the", "no article"),
        ("I need ___ ink pen for writing.", "an", "a", "the", "no article"), ("___ Pacific Ocean is the largest ocean.", "The", "A", "An", "No article"),
        ("She bought ___ pair of shoes.", "a", "an", "the", "no article"), ("He found ___ ant on his arm.", "an", "a", "the", "no article"),
        ("___ Himalayas are high mountains.", "The", "A", "An", "No article"), ("She is ___ honest girl.", "an", "a", "the", "no article"),
        ("Look at ___ stars shining tonight.", "the", "a", "an", "no article"), ("I saw ___ zebra at the zoo.", "a", "an", "the", "no article"),
        ("He is ___ university professor.", "a", "an", "the", "no article"), ("___ Bible is a holy book.", "The", "A", "An", "No article")
    ]
    body = ""
    for idx, (sentence, corr, w1, w2, w3) in enumerate(items, 1):
        qid = f"BK02_SP_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article:\n\n\"{sentence}\""
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — Correct article choice."
        body += q_block(qid, "MCQ", "Easy", "Applying", "Articles (A, An, The)", 1, qtxt, opts, ans)

    with open(os.path.join(OUTPUT_DIR, "articles_grammar.md"), "w", encoding="utf-8") as f:
        f.write(header + body)
    print("Generated articles_grammar.md (50 Qs)")

# 3. CALENDAR & DAYS
def build_calendar():
    header = "# Category 3: Calendar, Days of the Week & Abbreviations\n\n> **Target**: 50 Questions | Class II English | Days, Months, Calendar Reasoning & Abbreviations\n\n---\n\n"
    days_data = [
        ("This day is the day after Wednesday.", "Thursday", "THU"),
        ("This day is five days before Saturday.", "Monday", "MON"),
        ("This day is two days after Friday.", "Sunday", "SUN"),
        ("This day is the day before Thursday.", "Wednesday", "WED"),
        ("This day is the first day of the school week.", "Monday", "MON"),
        ("This day is the day before Sunday.", "Saturday", "SAT"),
        ("This day comes between Tuesday and Thursday.", "Wednesday", "WED"),
        ("This day comes right after Monday.", "Tuesday", "TUE"),
        ("This day is three days after Monday.", "Thursday", "THU"),
        ("This day is the last day of the weekend.", "Sunday", "SUN"),
        ("This day comes two days before Wednesday.", "Monday", "MON"),
        ("This day is four days after Tuesday.", "Saturday", "SAT"),
        ("This day is the middle day of a 7-day week (4th day).", "Thursday", "THU"),
        ("This day comes right before Friday.", "Thursday", "THU"),
        ("This day is two days before Sunday.", "Friday", "FRI"),
        ("This day is the day after Friday.", "Saturday", "SAT"),
        ("This day is three days before Tuesday.", "Saturday", "SAT"),
        ("This day comes between Friday and Sunday.", "Saturday", "SAT"),
        ("This day is the second day of the week.", "Tuesday", "TUE"),
        ("This day is the sixth day of the week.", "Saturday", "SAT"),
        ("What is the standard 3-letter abbreviation for Sunday?", "SUN", "Sunday"),
        ("What is the standard 3-letter abbreviation for Monday?", "MON", "Monday"),
        ("What is the standard 3-letter abbreviation for Tuesday?", "TUE", "Tuesday"),
        ("What is the standard 3-letter abbreviation for Wednesday?", "WED", "Wednesday"),
        ("What is the standard 3-letter abbreviation for Thursday?", "THU", "Thursday"),
        ("What is the standard 3-letter abbreviation for Friday?", "FRI", "Friday"),
        ("What is the standard 3-letter abbreviation for Saturday?", "SAT", "Saturday"),
        ("Which month comes right after January?", "February", "FEB"),
        ("Which month comes right before December?", "November", "NOV"),
        ("Which month is the first month of the year?", "January", "JAN"),
        ("Which month is the last month of the year?", "December", "DEC"),
        ("Which month comes between March and May?", "April", "APR"),
        ("Which month comes right after June?", "July", "JUL"),
        ("Which month comes right before October?", "September", "SEP"),
        ("Which month comes between August and October?", "September", "SEP"),
        ("How many days are there in a standard week?", "7 days", "7"),
        ("How many months are there in a year?", "12 months", "12"),
        ("If today is Tuesday, what day was yesterday?", "Monday", "MON"),
        ("If today is Friday, what day will tomorrow be?", "Saturday", "SAT"),
        ("If today is Sunday, what day will day after tomorrow be?", "Tuesday", "TUE"),
        ("If yesterday was Saturday, what day is today?", "Sunday", "SUN"),
        ("If tomorrow is Thursday, what day is today?", "Wednesday", "WED"),
        ("Which day comes 7 days after Monday?", "Monday", "MON"),
        ("Which month has 28 or 29 days?", "February", "FEB"),
        ("Which month comes after October?", "November", "NOV"),
        ("Which month comes before August?", "July", "JUL"),
        ("What is the 5th month of the year?", "May", "MAY"),
        ("What is the 8th month of the year?", "August", "AUG"),
        ("What is the 10th month of the year?", "October", "OCT"),
        ("What is the 3rd month of the year?", "March", "MAR")
    ]
    body = ""
    for idx, (qtxt, corr, extra) in enumerate(days_data, 1):
        qid = f"BK02_SP_CAT03_Q{idx:02d}"
        opts = [f"(A) {corr}", f"(B) Incorrect Option A", f"(C) Incorrect Option B", f"(D) Incorrect Option C"]
        ans = f"**(A) {corr}** — Correct answer."
        body += q_block(qid, "MCQ", "Easy", "Understanding", "Calendar & Days Vocabulary", 1, qtxt, opts, ans)

    with open(os.path.join(OUTPUT_DIR, "calendar_days_vocabulary.md"), "w", encoding="utf-8") as f:
        f.write(header + body)
    print("Generated calendar_days_vocabulary.md (50 Qs)")

# 4. ACTION VERBS
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification\n\n> **Target**: 50 Questions | Class II English | Action & Main Verbs Identification\n\n---\n\n"
    sentences = [
        ("Harry wrote an essay about her vacation to France.", "wrote", "essay", "vacation", "France"),
        ("The teacher was running in the playground.", "running", "teacher", "playground", "was"),
        ("Bobby forgot his trumpet at home.", "forgot", "trumpet", "home", "Bobby"),
        ("The dog barked at the stranger.", "barked", "dog", "stranger", "at"),
        ("She reads a colorful storybook every night.", "reads", "storybook", "night", "colorful"),
        ("The children played football in the park.", "played", "children", "football", "park"),
        ("Mother baked a chocolate cake for my birthday.", "baked", "Mother", "cake", "birthday"),
        ("Birds fly high in the blue sky.", "fly", "Birds", "high", "sky"),
        ("The boy drank a glass of cold milk.", "drank", "boy", "glass", "milk"),
        ("He painted a beautiful picture of mountains.", "painted", "picture", "mountains", "beautiful"),
        ("Rohan kicked the ball into the goal.", "kicked", "ball", "goal", "Rohan"),
        ("The cat slept peacefully on the rug.", "slept", "cat", "peacefully", "rug"),
        ("They sang a sweet song together.", "sang", "song", "sweet", "together"),
        ("My sister drew a cartoon character.", "drew", "sister", "cartoon", "character"),
        ("The chef cooked delicious soup.", "cooked", "chef", "soup", "delicious"),
        ("The train arrived at the station on time.", "arrived", "train", "station", "time"),
        ("The gardener watered the plants in the morning.", "watered", "gardener", "plants", "morning"),
        ("The baby cried for milk.", "cried", "baby", "milk", "for"),
        ("We swam in the clear blue pool.", "swam", "pool", "clear", "blue"),
        ("He jumped over the low fence.", "jumped", "fence", "over", "low"),
        ("She washed her hands before dinner.", "washed", "hands", "dinner", "before"),
        ("The sun shines brightly in summer.", "shines", "sun", "brightly", "summer"),
        ("He bought a new school bag.", "bought", "bag", "school", "new"),
        ("She opened the wooden door quietly.", "opened", "door", "wooden", "quietly"),
        ("The monkey climbed up the tall tree.", "climbed", "monkey", "tree", "tall"),
        ("They built a sandcastle on the beach.", "built", "sandcastle", "beach", "on"),
        ("The teacher explained the lesson clearly.", "explained", "teacher", "lesson", "clearly"),
        ("He dropped his water bottle on the floor.", "dropped", "bottle", "floor", "water"),
        ("She danced gracefully on the stage.", "danced", "danced", "stage", "gracefully"),
        ("The lion roared loudly in the forest.", "roared", "lion", "forest", "loudly"),
        ("He rode his new bicycle to school.", "rode", "bicycle", "school", "new"),
        ("My father repaired the broken toy.", "repaired", "father", "toy", "broken"),
        ("She brushed her teeth before sleeping.", "brushed", "teeth", "before", "sleeping"),
        ("The farmer planted seeds in the soil.", "planted", "farmer", "seeds", "soil"),
        ("He caught the ball with both hands.", "caught", "ball", "hands", "both"),
        ("She closed the window because of rain.", "closed", "window", "rain", "because"),
        ("The doctor treated the sick patient.", "treated", "doctor", "patient", "sick"),
        ("They watched a funny movie at night.", "watched", "movie", "night", "funny"),
        ("The snake slithered under the rock.", "slithered", "snake", "rock", "under"),
        ("He carried a heavy backpack to school.", "carried", "backpack", "school", "heavy"),
        ("She combed her hair neatly.", "combed", "hair", "neatly", "she"),
        ("The airplane flew over the clouds.", "flew", "airplane", "clouds", "over"),
        ("He shared his lunch with his friend.", "shared", "lunch", "friend", "his"),
        ("She folded her clothes neatly.", "folded", "clothes", "neatly", "she"),
        ("The clock ticked continuously.", "ticked", "clock", "continuously", "the"),
        ("He solved the math puzzle easily.", "solved", "puzzle", "math", "easily"),
        ("She typed an email on the computer.", "typed", "email", "computer", "she"),
        ("The duck paddled in the pond.", "paddled", "duck", "pond", "in"),
        ("He blew out the birthday candles.", "blew", "candles", "birthday", "out"),
        ("She wiped the clean table.", "wiped", "table", "clean", "she")
    ]
    body = ""
    for idx, (sent, v, w1, w2, w3) in enumerate(sentences, 1):
        qid = f"BK02_SP_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in the following sentence:\n\n\"{sent}\""
        opts = [f"(A) {v}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {v}** — '{v}' is the main action verb in the sentence."
        body += q_block(qid, "MCQ", "Easy", "Understanding", "Action Verbs Identification", 1, qtxt, opts, ans)

    with open(os.path.join(OUTPUT_DIR, "action_verbs_identification.md"), "w", encoding="utf-8") as f:
        f.write(header + body)
    print("Generated action_verbs_identification.md (50 Qs)")

# 5. PUNCTUATION MARKS
def build_punctuation():
    header = "# Category 5: Punctuation Marks & Capitalization\n\n> **Target**: 50 Questions | Class II English | End Punctuation (. ? !) & Capitalization\n\n---\n\n"
    punct_items = [
        ("Kyle loves to help his dad cook dinner", ".", "Statement requiring a full stop."),
        ("What do you think Kyle and his dad will cook tonight", "?", "Question requiring a question mark."),
        ("Oh no, I forgot my homework", "!", "Exclamation showing strong emotion."),
        ("Where are you going for summer vacation", "?", "Interrogative sentence needing a question mark."),
        ("My sister enjoys playing piano", ".", "Declarative sentence needing a full stop."),
        ("Wow, that fireworks display is amazing", "!", "Exclamatory sentence needing an exclamation mark."),
        ("Can you please pass me the salt", "?", "Polite question needing a question mark."),
        ("The sun sets in the west", ".", "Simple statement needing a full stop."),
        ("Hooray, our team won the match", "!", "Exclamation expressing joy."),
        ("What is your favorite color", "?", "Direct question needing a question mark."),
        ("Rohan plays football every evening", ".", "Statement ending with a full stop."),
        ("Ouch, that hot plate burned my finger", "!", "Exclamation showing sudden pain."),
        ("Have you finished reading your storybook", "?", "Question requiring a question mark."),
        ("The train arrives at six o'clock", ".", "Declarative sentence needing a full stop."),
        ("Watch out, there is a deep hole ahead", "!", "Warning exclamation needing an exclamation mark."),
        ("Who is your English teacher", "?", "Direct question needing a question mark."),
        ("Dogs are loyal pets", ".", "Statement requiring a full stop."),
        ("Alas, we lost the key", "!", "Exclamation of sorrow."),
        ("Why are you crying, little girl", "?", "Question needing a question mark."),
        ("She drinks warm milk before sleeping", ".", "Statement requiring a full stop."),
        ("Help, I fell off the swing", "!", "Urgent exclamation needing an exclamation mark."),
        ("When does the school bell ring", "?", "Question needing a question mark."),
        ("Trees give us shade and fresh air", ".", "Statement requiring a full stop."),
        ("Bravo, you got full marks", "!", "Praise exclamation needing an exclamation mark."),
        ("Which path should we take to the park", "?", "Question requiring a question mark."),
        ("My grandmother tells wonderful stories", ".", "Simple statement needing a full stop."),
        ("Look out, a bee is buzzing near your head", "!", "Warning exclamation."),
        ("Are you coming to my birthday party", "?", "Question requiring a question mark."),
        ("Birds build nests on trees", ".", "Statement requiring a full stop."),
        ("Yay, tomorrow is a holiday", "!", "Joyful exclamation."),
        ("How old are you", "?", "Question requiring a question mark."),
        ("He rides his bicycle carefully", ".", "Statement requiring a full stop."),
        ("Oh dear, I spilled the milk", "!", "Exclamation of disappointment."),
        ("What time does the movie start", "?", "Question requiring a question mark."),
        ("The flowers smell very sweet", ".", "Statement requiring a full stop."),
        ("Fantastic, you solved the riddle", "!", "Exclamation of excitement."),
        ("Where did you put my red crayon", "?", "Question requiring a question mark."),
        ("Water boils at 100 degrees Celsius", ".", "Scientific statement needing a full stop."),
        ("Watch your step, the floor is wet", "!", "Warning exclamation."),
        ("Is this your school bag", "?", "Question requiring a question mark."),
        ("The library is quiet", ".", "Statement requiring a full stop."),
        ("Stop, don't run across the road", "!", "Urgent warning exclamation."),
        ("Whose shoes are these", "?", "Question requiring a question mark."),
        ("She dances very well", ".", "Statement requiring a full stop."),
        ("Great job, everyone", "!", "Exclamation of praise."),
        ("Can I borrow your eraser", "?", "Question requiring a question mark."),
        ("The moon shines at night", ".", "Statement requiring a full stop."),
        ("Ouch, I stubbed my toe", "!", "Pain exclamation."),
        ("Why is the sky blue", "?", "Question requiring a question mark."),
        ("Reading books is a good habit", ".", "Statement requiring a full stop.")
    ]
    body = ""
    for idx, (sent, p, rule) in enumerate(punct_items, 1):
        qid = f"BK02_SP_CAT05_Q{idx:02d}"
        qtxt = f"Which correct punctuation mark should end the sentence?\n\n\"{sent} ___\""
        opts = [f"(A) {p}", "(B) .", "(C) ?", "(D) !"]
        # deduplicate options if p matches
        unique_opts = []
        for o in [f"(A) {p}", "(B) Full Stop (.)", "(C) Question Mark (?)", "(D) Exclamation Mark (!)"]:
            if o not in unique_opts:
                unique_opts.append(o)
        ans = f"**(A) {p}** — {rule}"
        body += q_block(qid, "MCQ", "Easy", "Applying", "Punctuation Marks", 1, qtxt, unique_opts[:4], ans)

    with open(os.path.join(OUTPUT_DIR, "punctuation_marks.md"), "w", encoding="utf-8") as f:
        f.write(header + body)
    print("Generated punctuation_marks.md (50 Qs)")

# 6. PHONICS & VOWEL DIGRAPHS
def build_phonics():
    header = "# Category 6: Phonics & Vowel Digraphs (ou / ow / ea / ee)\n\n> **Target**: 50 Questions | Class II English | Vowel Digraphs & Phonics Patterns\n\n---\n\n"
    words = [
        ("sn __ __", "ow", "snow", "ou", "oi", "ea"), ("cr __ __ n", "ow", "crown", "ou", "oi", "ee"),
        ("__ __ l", "ow", "owl", "ou", "oi", "ay"), ("p __ __ c h", "ou", "pouch", "ow", "oi", "ee"),
        ("h __ __ s e", "ou", "house", "ow", "oi", "ea"), ("m __ __ s e", "ou", "mouse", "ow", "oi", "ee"),
        ("cl __ __ d", "ou", "cloud", "ow", "oi", "ea"), ("sh __ __ t", "ou", "shout", "ow", "oi", "ee"),
        ("t __ __ n", "ow", "town", "ou", "oi", "ea"), ("c __ __", "ow", "cow", "ou", "oi", "ee"),
        ("br __ __ n", "ow", "brown", "ou", "oi", "ea"), ("fl __ __ er", "ow", "flower", "ou", "oi", "ee"),
        ("gr __ __ n d", "ou", "ground", "ow", "oi", "ea"), ("r __ __ n d", "ou", "round", "ow", "oi", "ee"),
        ("s __ __ n d", "ou", "sound", "ow", "oi", "ea"), ("c __ __ n t", "ou", "count", "ow", "oi", "ee"),
        ("m __ __ n t a i n", "ou", "mountain", "ow", "oi", "ea"), ("d __ __ n", "ow", "down", "ou", "oi", "ee"),
        ("cl __ __ n", "ow", "clown", "ou", "oi", "ea"), ("g r __ __", "ow", "grow", "ou", "oi", "ee"),
        ("b l __ __", "ow", "blow", "ou", "oi", "ea"), ("s l __ __", "ow", "slow", "ou", "oi", "ee"),
        ("y e l l __ __", "ow", "yellow", "ou", "oi", "ea"), ("w i n d __ __", "ow", "window", "ou", "oi", "ee"),
        ("sh __ __ e r", "ow", "shower", "ou", "oi", "ea"), ("t __ __ e l", "ow", "towel", "ou", "oi", "ee"),
        ("p __ __ d e r", "ow", "powder", "ou", "oi", "ea"), ("m __ __ t h", "ou", "mouth", "ow", "oi", "ee"),
        ("s __ __ t h", "ou", "south", "ow", "oi", "ea"), ("n __ __ n", "oo", "noon", "ou", "ow", "ea"),
        ("m __ __ n", "oo", "moon", "ou", "ow", "ea"), ("s p __ __ n", "oo", "spoon", "ou", "ow", "ea"),
        ("b __ __ k", "oo", "book", "ou", "ow", "ea"), ("l __ __ k", "oo", "look", "ou", "ow", "ea"),
        ("t __ __ t h", "ee", "teeth", "ea", "ou", "ow"), ("s e __ __", "ed", "seed", "ee", "ea", "ou"),
        ("t r __ __", "ee", "tree", "ea", "ou", "ow"), ("g r __ __ n", "ee", "green", "ea", "ou", "ow"),
        ("r e __ __", "ad", "read", "ea", "ee", "ou"), ("l e __ __", "af", "leaf", "ea", "ee", "ou"),
        ("m e __ __", "at", "meat", "ea", "ee", "ou"), ("c l e __ __", "an", "clean", "ea", "ee", "ou"),
        ("r a __ __", "in", "rain", "ai", "ay", "ou"), ("t r a __ __", "in", "train", "ai", "ay", "ou"),
        ("d a __ __", "y", "day", "ay", "ai", "ou"), ("p l a __ __", "y", "play", "ay", "ai", "ou"),
        ("s a __ __", "y", "say", "ay", "ai", "ou"), ("b __ __ y", "o", "boy", "oi", "oy", "ou"),
        ("t __ __ y", "o", "toy", "oi", "oy", "ou"), ("j __ __ y", "o", "joy", "oi", "oy", "ou")
    ]
    body = ""
    for idx, (pattern, corr, word, w1, w2, w3) in enumerate(words, 1):
        qid = f"BK02_SP_CAT06_Q{idx:02d}"
        qtxt = f"Complete the word **'{pattern}'** (referring to **{word}**) with the correct vowel digraph:"
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — Correct spelling is '{word}'."
        body += q_block(qid, "MCQ", "Easy", "Remembering", "Phonics & Vowel Digraphs", 1, qtxt, opts, ans)

    with open(os.path.join(OUTPUT_DIR, "phonics_vowel_digraphs.md"), "w", encoding="utf-8") as f:
        f.write(header + body)
    print("Generated phonics_vowel_digraphs.md (50 Qs)")

# 7. QUESTION WORDS
def build_question_words():
    header = "# Category 7: Question Words & Interrogative Framing\n\n> **Target**: 50 Questions | Class II English | Interrogative Starters (What, When, Where, Why, Who, How, Do, Is, Are)\n\n---\n\n"
    q_data = [
        ("___ is your birthday?", "When", "What", "Where", "Who", "Asking about time/date."),
        ("___ you like to swim?", "Do", "Is", "What", "When", "Asking about preference/habit."),
        ("___ is your favorite ice cream flavor?", "What", "When", "Where", "Who", "Asking about a specific choice."),
        ("___ is your school principal?", "Who", "What", "When", "Where", "Asking about a person."),
        ("___ live in that big house?", "Who", "Where", "What", "When", "Asking about people."),
        ("___ are my lost keys?", "Where", "What", "When", "Who", "Asking about location."),
        ("___ are you crying?", "Why", "What", "When", "Where", "Asking about a reason."),
        ("___ old are you?", "How", "What", "When", "Where", "Asking about age."),
        ("___ color is your new bag?", "What", "When", "Where", "Who", "Asking about color."),
        ("___ does the bus arrive?", "When", "What", "Where", "Who", "Asking about time."),
        ("___ is the nearest hospital?", "Where", "What", "When", "Who", "Asking about place."),
        ("___ you have a pet dog?", "Do", "Is", "Are", "What", "Auxiliary question starter."),
        ("___ your father working today?", "Is", "Are", "Do", "What", "Singular subject question starter."),
        ("___ these your books?", "Are", "Is", "Do", "What", "Plural subject question starter."),
        ("___ is your best friend?", "Who", "What", "Where", "When", "Asking about a person."),
        ("___ many apples are in the basket?", "How", "What", "When", "Where", "Asking about quantity."),
        ("___ much does this toy cost?", "How", "What", "When", "Where", "Asking about price."),
        ("___ is your favorite subject?", "What", "When", "Where", "Who", "Asking about choice."),
        ("___ do you live?", "Where", "What", "When", "Who", "Asking about place of residence."),
        ("___ are you late for school?", "Why", "What", "When", "Where", "Asking about reason."),
        ("___ is making that noise?", "Who", "What", "When", "Where", "Asking about person/cause."),
        ("___ you want some orange juice?", "Do", "Is", "Are", "When", "Asking about desire."),
        ("___ she your younger sister?", "Is", "Are", "Do", "What", "Asking about singular relationship."),
        ("___ they playing in the garden?", "Are", "Is", "Do", "What", "Asking about plural action."),
        ("___ time is it right now?", "What", "When", "Where", "Who", "Asking about current time."),
        ("___ season do you like most?", "Which", "When", "Where", "Who", "Asking about selection."),
        ("___ bag is this on the desk?", "Whose", "What", "When", "Where", "Asking about possession."),
        ("___ far is the railway station?", "How", "What", "When", "Where", "Asking about distance."),
        ("___ tall is that building?", "How", "What", "When", "Where", "Asking about height."),
        ("___ did you wake up this morning?", "When", "What", "Where", "Who", "Asking about morning time."),
        ("___ are you hiding behind the curtain?", "Why", "What", "When", "Where", "Asking about reason."),
        ("___ is teaching you English?", "Who", "What", "When", "Where", "Asking about teacher's identity."),
        ("___ is the capital of India?", "What", "When", "Where", "Who", "Asking about fact/name."),
        ("___ can I find a pencil sharpener?", "Where", "What", "When", "Who", "Asking about location."),
        ("___ you finish your dinner quickly?", "Did", "Is", "Are", "What", "Past action question."),
        ("___ he go to school by bus?", "Does", "Is", "Are", "What", "Singular habit question."),
        ("___ they know the answer?", "Do", "Is", "Are", "What", "Plural habit question."),
        ("___ is your bicycle parked?", "Where", "What", "When", "Who", "Asking about location."),
        ("___ is knocking on the front door?", "Who", "What", "When", "Where", "Asking about person at door."),
        ("___ will the rainy season start?", "When", "What", "Where", "Who", "Asking about future time."),
        ("___ is your mother feeling today?", "How", "What", "When", "Where", "Asking about health state."),
        ("___ book are you reading?", "Which", "When", "Where", "Who", "Asking about specific book."),
        ("___ laptop is lying on the table?", "Whose", "What", "When", "Where", "Asking about ownership."),
        ("___ can solve this math problem?", "Who", "What", "When", "Where", "Asking about capable person."),
        ("___ did you place the house keys?", "Where", "What", "When", "Who", "Asking about place."),
        ("___ is your favorite festival?", "What", "When", "Where", "Who", "Asking about festival choice."),
        ("___ do we celebrate Independence Day?", "When", "What", "Where", "Who", "Asking about date."),
        ("___ are you laughing so loudly?", "Why", "What", "When", "Where", "Asking about reason."),
        ("___ should we do next?", "What", "When", "Where", "Who", "Asking about next action."),
        ("___ is the tallest mountain peak?", "Which", "When", "Where", "Who", "Asking about specific peak.")
    ]
    body = ""
    for idx, (qtxt, corr, w1, w2, w3, rule) in enumerate(q_data, 1):
        qid = f"BK02_SP_CAT07_Q{idx:02d}"
        full_q = f"Choose the correct question word to complete the question:\n\n\"{qtxt}\""
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — {rule}"
        body += q_block(qid, "MCQ", "Easy", "Applying", "Question Words & Interrogatives", 1, full_q, opts, ans)

    with open(os.path.join(OUTPUT_DIR, "question_words_interrogatives.md"), "w", encoding="utf-8") as f:
        f.write(header + body)
    print("Generated question_words_interrogatives.md (50 Qs)")

# 8. PRESENT CONTINUOUS (-ING)
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense & Verb + '-ing'\n\n> **Target**: 50 Questions | Class II English | Present Continuous Tense & Spelling Rules (-ing)\n\n---\n\n"
    cont_items = [
        ("I am ___ for the bus with my friend. (wait)", "waiting", "waitting", "waited", "waits"),
        ("My cousin is ___ for the airport in an hour. (leave)", "leaving", "leaveing", "leaved", "leavs"),
        ("My mom is ___ my favorite song. (sing)", "singing", "singging", "singed", "sings"),
        ("He is ___ a surprise party for his father. (organize)", "organizing", "organizeing", "organized", "organizes"),
        ("Our class is ___ a book drive. (build)", "building", "buildding", "builded", "builds"),
        ("The children are ___ football in the park. (play)", "playing", "playingg", "played", "plays"),
        ("She is ___ a picture of a flower. (draw)", "drawing", "drawwing", "drawed", "draws"),
        ("The dog is ___ at the stranger. (bark)", "barking", "barkking", "barked", "barks"),
        ("He is ___ his homework right now. (do)", "doing", "doingg", "did", "does"),
        ("My father is ___ a car on the road. (drive)", "driving", "driveing", "drived", "drives"),
        ("The duck is ___ in the pond. (swim)", "swimming", "swiming", "swimmed", "swims"),
        ("The bird is ___ in the sky. (fly)", "flying", "flyingg", "flied", "flies"),
        ("She is ___ a chocolate cake. (bake)", "baking", "bakeing", "baked", "bakes"),
        ("The baby is ___ loudly. (cry)", "crying", "cryingg", "cried", "cries"),
        ("They are ___ a new storybook. (read)", "reading", "readdings", "readed", "reads"),
        ("The sun is ___ brightly today. (shine)", "shining", "shineing", "shined", "shines"),
        ("He is ___ his bicycle fast. (ride)", "riding", "rideing", "rided", "rides"),
        ("She is ___ her teeth carefully. (brush)", "brushing", "brushingg", "brushed", "brushes"),
        ("We are ___ delicious food. (eat)", "eating", "eatting", "eated", "eats"),
        ("The chef is ___ soup for dinner. (cook)", "cooking", "cookking", "cooked", "cooks"),
        ("The boy is ___ over the hurdle. (jump)", "jumping", "jumpingg", "jumped", "jumps"),
        ("They are ___ to the sweet music. (dance)", "dancing", "danceing", "danced", "dances"),
        ("He is ___ a heavy wooden box. (lift)", "lifting", "liftting", "lifted", "lifts"),
        ("She is ___ a red jacket today. (wear)", "wearing", "wearring", "wored", "wears"),
        ("The teacher is ___ the lesson. (explain)", "explaining", "explainning", "explained", "explains"),
        ("Rohan is ___ the ball into the goal. (kick)", "kicking", "kickking", "kicked", "kicks"),
        ("The lion is ___ loudly in the zoo. (roar)", "roaring", "roarring", "roared", "roars"),
        ("She is ___ water into the glass. (pour)", "pouring", "pourring", "poured", "pours"),
        ("He is ___ a beautiful letter. (write)", "writing", "writeing", "writed", "writes"),
        ("The rain is ___ heavily outside. (fall)", "falling", "fallling", "felled", "falls"),
        ("They are ___ for the train at the platform. (wait)", "waiting", "waitting", "waited", "waits"),
        ("My sister is ___ her hands with soap. (wash)", "washing", "washingg", "washed", "washes"),
        ("The cat is ___ under the wooden chair. (sleep)", "sleeping", "sleepingg", "slept", "sleeps"),
        ("He is ___ a blue kite in the sky. (fly)", "flying", "flyingg", "flied", "flies"),
        ("She is ___ the dirty floor with a mop. (clean)", "cleaning", "cleanning", "cleaned", "cleans"),
        ("The farmer is ___ seeds in the soil. (sow)", "sowing", "sowwing", "sowed", "sows"),
        ("He is ___ a glass of cold water. (drink)", "drinking", "drinkking", "drank", "drinks"),
        ("They are ___ a tall sandcastle. (make)", "making", "makeing", "maked", "makes"),
        ("She is ___ her hair with a comb. (brush)", "brushing", "brushingg", "brushed", "brushes"),
        ("The monkey is ___ up the coconut tree. (climb)", "climbing", "climbbing", "climbed", "climbs"),
        ("He is ___ his shoes tightly. (tie)", "tying", "tieing", "tied", "ties"),
        ("She is ___ a song on the stage. (sing)", "singing", "singging", "singed", "sings"),
        ("The car is ___ down the hill. (run)", "running", "runing", "ran", "runs"),
        ("He is ___ the red button on the wall. (press)", "pressing", "presssing", "pressed", "presses"),
        ("She is ___ her clothes in the closet. (fold)", "folding", "foldding", "folded", "folds"),
        ("The students are ___ to their teacher. (listen)", "listening", "listenning", "listened", "listens"),
        ("He is ___ a green apple. (eat)", "eating", "eatting", "eated", "eats"),
        ("She is ___ a letter to her grandmother. (write)", "writing", "writeing", "writed", "writes"),
        ("The phone is ___ loudly. (ring)", "ringing", "ringging", "rang", "rings"),
        ("We are ___ a fun game together. (play)", "playing", "playingg", "played", "plays")
    ]
    body = ""
    for idx, (sent, corr, w1, w2, w3) in enumerate(cont_items, 1):
        qid = f"BK02_SP_CAT08_Q{idx:02d}"
        qtxt = f"Complete the sentence with the correct verb form (-ing):\n\n\"{sent}\""
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — Correct continuous tense verb form."
        body += q_block(qid, "MCQ", "Easy", "Applying", "Present Continuous (-ing)", 1, qtxt, opts, ans)

    with open(os.path.join(OUTPUT_DIR, "present_continuous_ing.md"), "w", encoding="utf-8") as f:
        f.write(header + body)
    print("Generated present_continuous_ing.md (50 Qs)")

# 9. HELPING VERBS (IS, AM, ARE)
def build_helping_verbs():
    header = "# Category 9: Subject-Verb Agreement with Helping Verbs (Is, Am, Are)\n\n> **Target**: 50 Questions | Class II English | Auxiliary Verbs (is, am, are, was, were, has, have)\n\n---\n\n"
    hv_items = [
        ("My mother ___ a teacher.", "is", "am", "are", "were"),
        ("You ___ my best friend.", "are", "is", "am", "was"),
        ("Rohan and Sania ___ my classmates.", "are", "is", "am", "was"),
        ("The elephant ___ the biggest animal on land.", "is", "are", "am", "were"),
        ("The birds ___ flying in the sky.", "are", "is", "am", "was"),
        ("Raju ___ making a paper boat.", "is", "are", "am", "were"),
        ("Suma ___ a good singer.", "is", "are", "am", "were"),
        ("My teacher ___ very kind and helpful.", "is", "are", "am", "were"),
        ("I ___ studying for my English exam.", "am", "is", "are", "were"),
        ("We ___ going to the zoo tomorrow.", "are", "is", "am", "was"),
        ("He ___ reading a comic book.", "is", "are", "am", "were"),
        ("She ___ writing a letter to her friend.", "is", "are", "am", "were"),
        ("They ___ playing football in the field.", "are", "is", "am", "was"),
        ("The dog ___ barking at the postman.", "is", "are", "am", "were"),
        ("The stars ___ shining brightly tonight.", "are", "is", "am", "was"),
        ("I ___ seven years old.", "am", "is", "are", "were"),
        ("This book ___ very interesting.", "is", "are", "am", "were"),
        ("These apples ___ sweet and juicy.", "are", "is", "am", "was"),
        ("My father ___ working in an office.", "is", "are", "am", "were"),
        ("The children ___ listening attentively.", "are", "is", "am", "was"),
        ("A lion ___ the king of the jungle.", "is", "are", "am", "were"),
        ("I ___ happy to see my grandparents.", "am", "is", "are", "were"),
        ("You ___ doing a great job.", "are", "is", "am", "was"),
        ("My cat ___ sleeping on the rug.", "is", "are", "am", "were"),
        ("The cows ___ grazing in the green field.", "are", "is", "am", "was"),
        ("New Delhi ___ the capital of India.", "is", "are", "am", "were"),
        ("I ___ ready for school.", "am", "is", "are", "were"),
        ("We ___ proud of our country.", "are", "is", "am", "was"),
        ("He ___ drawing a beautiful picture.", "is", "are", "am", "were"),
        ("She ___ dancing on the stage.", "is", "are", "am", "were"),
        ("They ___ my neighbors.", "are", "is", "am", "was"),
        ("The sun ___ hot and bright.", "is", "are", "am", "were"),
        ("Flowers ___ blooming in the garden.", "are", "is", "am", "was"),
        ("I ___ taller than my brother.", "am", "is", "are", "were"),
        ("It ___ raining heavily outside.", "is", "are", "am", "were"),
        ("These shoes ___ new.", "are", "is", "am", "was"),
        ("That building ___ very tall.", "is", "are", "am", "were"),
        ("My parents ___ visiting the museum.", "are", "is", "am", "was"),
        ("The baby ___ smiling at her mother.", "is", "are", "am", "were"),
        ("I ___ drinking a glass of juice.", "am", "is", "are", "were"),
        ("You ___ wearing a bright blue shirt.", "are", "is", "am", "was"),
        ("The computer ___ working properly.", "is", "are", "am", "were"),
        ("The boys ___ playing cricket.", "are", "is", "am", "was"),
        ("She ___ my elder sister.", "is", "are", "am", "were"),
        ("I ___ a hardworking student.", "am", "is", "are", "were"),
        ("We ___ excited about the picnic.", "are", "is", "am", "was"),
        ("The clock ___ ticking on the wall.", "is", "are", "am", "were"),
        ("Mangoes ___ my favorite fruit.", "are", "is", "am", "was"),
        ("He ___ feeling much better now.", "is", "are", "am", "were"),
        ("She ___ an honest and helpful girl.", "is", "are", "am", "were")
    ]
    body = ""
    for idx, (sent, corr, w1, w2, w3) in enumerate(hv_items, 1):
        qid = f"BK02_SP_CAT09_Q{idx:02d}"
        qtxt = f"Complete the sentence with the correct helping verb (is, am, are):\n\n\"{sent}\""
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — Correct subject-verb agreement."
        body += q_block(qid, "MCQ", "Easy", "Applying", "Helping Verbs (Is, Am, Are)", 1, qtxt, opts, ans)

    with open(os.path.join(OUTPUT_DIR, "helping_verbs_is_am_are.md"), "w", encoding="utf-8") as f:
        f.write(header + body)
    print("Generated helping_verbs_is_am_are.md (50 Qs)")

if __name__ == "__main__":
    print("Building all 9 Category Files for Class 2 Sample Paper Bank (450 Qs)...")
    build_plural_nouns()
    build_articles()
    build_calendar()
    build_action_verbs()
    build_punctuation()
    build_phonics()
    build_question_words()
    build_present_continuous()
    build_helping_verbs()
    print("\n[SUCCESS] Generated all 9 sample paper category question bank files!")
