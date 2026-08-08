r"""
=============================================================================
Script: rebuild_chapter_05.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 05:
             "Invention of Potato Chips" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH05_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_05")
os.makedirs(CH05_DIR, exist_ok=True)

def make_q_block(qid, qtype, diff, bloom, topic, marks, question, opts, answer):
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

# ---------------------------------------------------------------------------
# 1. Plural Nouns & Spelling Rules (50 Qs)
# ---------------------------------------------------------------------------
def build_plural_nouns():
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 05: Invention of Potato Chips\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("chip", "chips", "chipies", "chipse", "chipz", "A", "Regular noun adding -s."),
        ("potato", "potatoes", "potatos", "potatoeses", "potatoies", "A", "Nouns ending in -o add -es."),
        ("fry", "fries", "frys", "fryes", "friez", "A", "Consonant + y changes to -ies."),
        ("chef", "chefs", "chefes", "chev", "chefies", "A", "Regular noun ending in -f adds -s (chefs)."),
        ("customer", "customers", "customeres", "customeries", "customerz", "A", "Regular noun adding -s."),
        ("slice", "slices", "slicies", "slicees", "slicez", "A", "Regular noun ending in -e adds -s."),
        ("line", "lines", "linies", "linees", "linez", "A", "Regular noun ending in -e adds -s."),
        ("kitchen", "kitchens", "kitchenes", "kitchenies", "kitchenz", "A", "Regular noun adding -s."),
        ("restaurant", "restaurants", "restaurantes", "restauranties", "restaurantz", "A", "Regular noun adding -s."),
        ("year", "years", "yeares", "yearies", "yearz", "A", "Regular noun adding -s."),
        ("day", "days", "daies", "dayes", "dayz", "A", "Vowel + y adds -s."),
        ("dish", "dishes", "dishs", "dishies", "dished", "A", "Nouns ending in -sh add -es."),
        ("batch", "batches", "batchs", "batchies", "batched", "A", "Nouns ending in -ch add -es."),
        ("box", "boxes", "boxs", "boxies", "boxen", "A", "Nouns ending in -x add -es."),
        ("snack", "snacks", "snackes", "snackies", "snackz", "A", "Regular noun adding -s."),
        ("million", "millions", "milliones", "millionies", "millionz", "A", "Regular noun adding -s."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people."),
        ("knife", "knives", "knifes", "knifees", "knivs", "A", "Nouns ending in -fe change to -ves.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH05_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 05 (*Invention of Potato Chips*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("George Crum prepared three (batch / batches) of French fries.", "batches", "batch", "batchs", "batchies", "A", "'three' requires plural noun 'batches'."),
        ("He sliced five (potato / potatoes) very thinly.", "potatoes", "potato", "potatos", "potatoies", "A", "'potatoes' is the correct plural ending in -es."),
        ("The customer sent back the French (fry / fries).", "fries", "fry", "frys", "fryes", "A", "Consonant + y changes to -ies (fries)."),
        ("Identify the INCORRECT plural spelling in this list: chefs, slices, potatos, dishes.", "potatos", "chefs", "slices", "dishes", "A", "Plural of potato is 'potatoes' (-es), not 'potatos'."),
        ("Choose the sentence with the correct plural noun form:", "Many customers loved the crispy potato chips.", "Many customeres loved the crispy potato chips.", "Many customeries loved the crispy potato chips.", "Many customerz loved the crispy potato chips.", "A", "customers is the correct plural of customer."),
        ("Which noun forms its plural by changing -o to -oes?", "potato -> potatoes", "chip -> chips", "slice -> slices", "chef -> chefs", "A", "Potato ends in consonant + o, so plural adds -es."),
        ("Change the singular noun in brackets to plural: 'George Crum used two sharp ____ (knife).' ", "knives", "knifes", "knifees", "knivs", "A", "Nouns ending in -fe change to -ves (knives)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The chefs prepared the dishes in the kitchens.", "The chev prepared the dishs in the kitchens.", "The chefs prepared the dishies in the kitchenes.", "The chefees prepared the dishes in the kitchens.", "A", "chefs, dishes, kitchens are all correctly spelt plurals."),
        ("What is the correct plural of 'restaurant'?", "restaurants", "restaurantes", "restauranties", "restaurantz", "A", "Regular noun adding -s."),
        ("The restaurant was busy for many (day / days).", "days", "daies", "day", "dayes", "A", "Vowel + y adds -s (days)."),
        ("George Crum placed the chips on clean (plate / plates).", "plates", "platess", "platies", "platez", "A", "Plural of plate is plates."),
        ("Millions of (person / people) enjoy potato chips today.", "people", "persons", "peoples", "persones", "A", "Plural of person in general context is people."),
        ("How many (slice / slices) of potato did Crum fry?", "slices", "slice", "slicies", "slicees", "A", "Plural noun 'slices'."),
        ("The three (chef / chefs) worked together in the lodge.", "chefs", "chefes", "chev", "chefies", "A", "Plural of chef is chefs."),
        ("Which plural noun rule applies to the word **'boxes'**?", "Add -es to nouns ending in -x", "Add -s to vowel + y", "Change -f to -ves", "Change -y to -ies", "A", "Box ends in -x, so it adds -es."),
        ("George Crum received many (compliment / compliments).", "compliments", "complimentes", "complimenties", "complimentz", "A", "Regular noun adding -s."),
        ("Identify the correct plural form of 'child':", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("The waiters carried many (tray / trays) of chips.", "trays", "traies", "trayes", "trayz", "A", "Vowel + y adds -s (trays).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH05_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The chef fried a potato in the kitchen.'", "The chefs fried potatoes in the kitchens.", "The chev fried potatos in the kitchenes.", "The chefs fried potato in the kitchens.", "The chef fried potatoes in the kitchenz.", "A", "Plural of chef->chefs, potato->potatoes, kitchen->kitchens."),
        ("Analyze the error: 'George Crum added three pinches of salts.' Why is 'salts' inappropriate here?", "'salt' is an uncountable mass noun, so 'salt' (or 'pinches of salt') should be used.", "'salts' should be 'saltes'.", "'salts' should be 'salties'.", "No error.", "A", "Mass nouns like salt do not normally take plural form."),
        ("Complete the paragraph with correct plurals: 'The two ____ (chef) prepared five ____ (dish) of crispy ____ (potato).'", "chefs, dishes, potatoes", "chev, dishs, potatos", "chefs, dishies, potato", "chefes, dishes, potatoes", "A", "chefs (-s), dishes (-sh + es), potatoes (-o + es)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **chefs** placed the **slices** into the **boxes**.", "The **chev** placed the **slicies** into the **boxs**.", "The **chefs** placed the **slicees** into the **boxies**.", "The **chefees** placed the **slices** into the **boxes**.", "A", "chefs (-s), slices (-s), boxes (-x + es)."),
        ("Which group contains ONLY irregular plural nouns?", "people, men, teeth, children", "chips, potatoes, chefs, slices", "factories, cities, stories, armies", "leaves, thieves, wolves, knives", "A", "people, men, teeth, children change forms without standard -s/-es."),
        ("Why does 'tray' become 'trays' but 'fry' becomes 'fries'?", "Because 'tray' has a vowel before y (a+y -> -s), while 'fry' has a consonant before y (r+y -> -ies).", "Because 'tray' is short and 'fry' is long.", "Because 'tray' is an object and 'fry' is food.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The two chefes bought many mouses for the lodge.'", "'chefes' should be 'chefs' and 'mouses' should be 'mice'.", "'chefes' should be 'chef' and 'mouses' should be 'mices'.", "'lodge' should be 'lodges' only.", "There are no mistakes in the sentence.", "A", "chefs (regular -s) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'Crum wiped his ____ (hand) and moved his ____ (foot).'", "hands, feet", "handes, foots", "hands, feets", "handies, foots", "A", "Plural of hand is hands, plural of foot is feet."),
        ("Analyze this sentence: 'George Crum gave advice to young cooks.' Can 'advice' be pluralized as 'advices'?", "No, 'advice' is an uncountable noun; we say 'pieces of advice' for plural.", "Yes, 'advices' is correct.", "No, it becomes 'advicess'.", "Yes, 'an advice' is correct.", "A", "Advice is an uncountable noun."),
        ("Fill in the blanks: 'The two ____ (customer) ate three ____ (batch) of chips.'", "customers, batches", "customeres, batchs", "customers, batchies", "customeres, batches", "A", "customer -> customers; batch -> batches (-ch + es)."),
        ("Select the option that shows correct plural transformation for ALL three words: 'loaf', 'city', 'box'", "loaves, cities, boxes", "loafs, citys, boxs", "loaves, cityes, boxies", "loafes, cities, foxen", "A", "loaf -> loaves; city -> cities; box -> boxes."),
        ("HOTS Reasoning: Why do we say 'oil is hot' rather than 'oils are hot'?", "Because 'oil' is an uncountable material noun that stays singular.", "Because oil burns.", "Because Crum fried chips.", "Because chips are crispy.", "A", "Uncountable material nouns take singular verbs."),
        ("Transform into singular: 'The chefs fried the potatoes in the kitchens.'", "The chef fried the potato in the kitchen.", "The chefs fried the potato in the kitchen.", "The chef fry the potato in the kitchen.", "The chef fried the potatoes in the kitchen.", "A", "Singular forms: chef, potato, kitchen."),
        ("Identify the correct rule for forming the plural of **'snack'**:", "Add -s because it is a regular noun ending in a consonant (snacks).", "Add -es (snackes).", "Change -k to -ves (snavs).", "Change vowel sound.", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH05_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 05: Invention of Potato Chips\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("George Crum was ___ chef at Moon Lake Lodge.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'chef'."),
        ("Moon Lake Lodge was located in ___ New York town.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'New'."),
        ("___ picky customer complained about the French fries.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'picky'."),
        ("George Crum created ___ invention by accident.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'invention'."),
        ("He sliced the potato into ___ thin piece.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'thin'."),
        ("___ History story tells us about potato chips.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'History'."),
        ("The chef added ___ extra pinch of salt.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'extra'."),
        ("George Crum was ___ honest hard-working man.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ potato chips became popular worldwide.", "The", "A", "An", "No article", "A", "Use 'The' for specific chips invented in story."),
        ("George Crum had ___ tough day at work.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'tough'."),
        ("It was ___ unusual reaction from the customer.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unusual'."),
        ("George Crum made ___ crispy snack out of frustration.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'crispy'."),
        ("___ customer loved the paper-thin fries.", "The", "A", "An", "No article", "A", "Use 'The' for specific customer in story."),
        ("George Crum took ___ potato from the basket.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'potato'."),
        ("They created ___ delicious comfort food.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'delicious'."),
        ("George Crum was ___ talented cook.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'talented'."),
        ("Potato chips bring ___ joy to millions of people.", "no article", "a", "an", "the", "A", "Abstract noun 'joy' takes no indefinite article here."),
        ("___ sun set while Crum worked in the kitchen.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH05_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The customer sent back ___ fries and demanded ___ thinner slice.", "the, a", "a, an", "an, a", "a, the", "A", "'the fries' (specific fries), 'a thinner slice' (consonant sound)."),
        ("Why do we say '**a** chef' but '**an** invention'?", "Because 'chef' begins with a consonant sound (sh) and 'invention' with a vowel sound (i).", "Because chefs cook.", "Because inventions are big.", "Because New York is far.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "George Crum was a chef at a famous lodge.", "George Crum was an chef at an famous lodge.", "George Crum was the a chef.", "George Crum was a an chef.", "A", "'a chef' (/sh/) and 'a famous' (/f/) both take 'a'."),
        ("Fill in the blanks: 'Crum fried ___ potatoes in ___ hot oil.'", "the, no article", "a, a", "an, an", "a, the", "A", "'the potatoes' (specific), 'hot oil' (uncountable mass noun, no article)."),
        ("Identify the INCORRECT article in: 'George Crum created **a** extra crispy chip.'", "'a' should be 'an'", "'a' should be 'the'", "'extra' should be 'a extra'", "No mistake", "A", "'extra' starts with vowel sound /e/, so it takes 'an'."),
        ("Which article completes the sentence? 'Baking requires ___ active kitchen team.'", "an", "a", "the", "no article", "A", "'active' starts with vowel sound /a/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ customer loved ___ new dish.'", "The, the", "A, a", "An, an", "The, a", "A", "'The customer' (specific picky customer), 'the new dish' (specific potato chips)."),
        ("Why do we use 'a' before 'picky customer' in 'He was **a** picky customer'?", "Because 'picky' begins with the consonant sound /p/.", "Because customer is a noun.", "Because picky means choosy.", "Because lodge is big.", "A", "'picky' starts with consonant sound /p/."),
        ("Complete the dialogue: Customer: 'Bring me ___ thinner fry!' Crum: 'I will slice ___ potato paper-thin!'", "a, the", "a, an", "an, the", "the, the", "A", "'a thinner fry' (consonant sound), 'the potato' (specific potato)."),
        ("Select the sentence:", "A potato chip is a popular snack.", "An potato chip is a popular snack.", "The potato chip is an popular snack.", "An potato chip is an popular snack.", "A", "'A potato chip' (consonant sound), 'a popular snack' (consonant sound)."),
        ("Fill in the blank: 'The customers queued for ___ long time outside the lodge.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "George Crum seasoned the chips with **___ salt**.", "He sliced ___ potato.", "He opened ___ kitchen.", "He met ___ customer.", "A", "Uncountable mass noun 'salt' takes no article here."),
        ("Choose the correct sentence for story summary:", "Frustration can lead to a great invention.", "An frustration can lead to an great invention.", "A frustration can lead to a great invention.", "The frustration a can lead to an invention.", "A", "Abstract concept 'Frustration' takes no indefinite article."),
        ("Fill in the blanks: 'Crum spent ___ hour frying ___ thin slices.'", "an, the", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'the thin slices' (specific)."),
        ("Which sentence uses 'the' correctly for unique story places?", "Moon Lake Lodge was the most popular resort in New York.", "Moon Lake Lodge was a most popular resort in a New York.", "Moon Lake Lodge was an most popular resort.", "Moon Lake Lodge was most popular resort.", "A", "Superlative 'the most popular' takes 'the'."),
        ("Identify the article error: 'George Crum gave **a** explanation after **an** short argument.'", "'an short' should be 'a short' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an short' should be 'a short'", "No error", "A", "'an explanation' (vowel /e/) and 'a short argument' (consonant /s/)."),
        ("Complete: 'It was ___ unexpected hit at ___ restaurant.'", "an, the", "a, an", "the, the", "an, an", "A", "an unexpected (/u/), the restaurant (specific)."),
        ("Choose the correct option: '___ sun shone over Moon Lake Lodge.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH05_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'George Crum added **a** salt to **the** potatoes.' Correct the error:", "'added a salt' -> 'added salt' (uncountable mass noun salt takes no article 'a').", "'the potatoes' -> 'an potatoes'.", "'added a salt' -> 'added an salt'.", "No error present.", "A", "'salt' is uncountable and takes no article 'a'."),
        ("Fill in all three blanks: '___ chef told ___ customer that ___ patience is necessary.'", "The, the, no article", "A, an, a", "An, a, the", "The, a, a", "A", "'The chef' (specific), 'the customer' (specific), 'patience' (general abstract)."),
        ("Identify why 'the' is used in: 'The customer loved **the** thin crispy fries.'", "Because 'the thin crispy fries' refers to the specific new dish made by Crum.", "Because fries is a proper noun.", "Because customer ate it.", "Because lodge is in New York.", "A", "'The' specifies the definite dish mentioned in narrative."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** eagle to fly past Moon Lake Lodge.'", "'a hour' should be 'an hour' and 'a eagle' should be 'an eagle'.", "'a hour' should be 'the hour' and 'a eagle' should be 'a eagle'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'eagle' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A chef worked at a lodge. He met a picky customer. The customer complained about the fries.", "An chef worked at an lodge. He met an picky customer. A customer complained about a fries.", "The chef worked at an lodge. He met a an customer.", "A chef worked at an lodge. The customer was a honest.", "A", "A chef (first mention), a lodge (first mention), a picky customer (consonant), The customer (second mention)."),
        ("Why is it correct to write 'a unique recipe' but 'an unusual recipe'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because recipe is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story moral: '___ angry moment led to ___ famous invention in ___ culinary history.'", "An, a, no article", "A, an, a", "The, the, the", "An, an, a", "A", "An angry moment (/a/), a famous invention (/f/), culinary history (uncountable/general, no article)."),
        ("Analyze this sentence: 'George Crum went to **the** kitchen.' Why is 'the' appropriate?", "Because it refers to the specific kitchen of Moon Lake Lodge.", "Because kitchen is in New York.", "Because kitchen is plural.", "Because Crum is chef.", "A", "'the' specifies the definite kitchen."),
        ("Correct the sentence: 'An chef fried a potatoes in a hot oil.'", "A chef fried the potatoes in hot oil.", "The chef fried an potatoes in a hot oil.", "An chef fried the potatoes in the hot oil.", "A chef fried a potatoes in a hot oil.", "A", "'A chef' (/sh/ sound), 'the potatoes' (plural), 'hot oil' (mass noun, no 'a')."),
        ("Fill in the blanks: '___ chips in ___ basket were seasoned with ___ salt.'", "The, the, no article", "A, a, a", "No article, a, an", "An, the, a", "A", "'The chips' (specific), 'the basket' (specific), 'salt' (mass noun, no article)."),
        ("Spot the missing article: 'Customer tasted dish and praised chef.'", "Missing 'The' before 'Customer' -> 'The customer tasted the dish and praised the chef.'", "Missing 'a' before 'praised'", "Missing 'an' before 'tasted'", "No article is missing", "A", "Specific nouns 'The customer', 'the dish', 'the chef' all require 'the'."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An assistant brought a potato to the chef.", "A assistant brought an potato to a chef.", "The assistant brought an potato to an chef.", "An assistant brought an potato to the chef.", "A", "An assistant (vowel), a potato (consonant), the chef (specific)."),
        ("Rewrite correctly: 'George Crum was a honest chef who made an crispy snack.'", "George Crum was an honest chef who made a crispy snack.", "George Crum was a honest chef who made a crispy snack.", "George Crum was an honest chef who made an crispy snack.", "George Crum was the honest chef who made an crispy snack.", "A", "'an honest' (silent h), 'a crispy snack' (consonant /k/)."),
        ("Identify the correct rule for using 'the' with ordinal numbers (first, second, third, fourth):", "Ordinal numbers take 'the' when identifying specific items in a series.", "Ordinal numbers take 'an'.", "Ordinal numbers never take articles.", "Ordinal numbers take 'a' only.", "A", "'The first', 'the second' take 'the'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH05_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 05: Invention of Potato Chips\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_days = [
        ("Potato chips were invented in the year **1853**. How many years are in 1 century?", "100 years", "10 years", "50 years", "1000 years", "A", "1 century = 100 years."),
        ("What is the standard abbreviation for **Saturday**?", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard abbreviation."),
        ("Which day comes right after Wednesday?", "Thursday", "Friday", "Tuesday", "Saturday", "A", "Thursday follows Wednesday."),
        ("What is the abbreviation for **Thursday**?", "Thu. / Thurs.", "Thr.", "Ths.", "Tu.", "A", "Thu. is standard abbreviation."),
        ("If customers queued for 5 days straight, how many weekdays were they queuing (Mon-Fri)?", "5 weekdays", "2 weekdays", "7 weekdays", "3 weekdays", "A", "Mon to Fri is 5 weekdays."),
        ("Which month comes right before November?", "October", "September", "December", "August", "A", "October comes before November."),
        ("What is the short abbreviation for **November**?", "Nov.", "Nove.", "Nv.", "Nm.", "A", "Nov. is standard abbreviation."),
        ("George Crum worked in the kitchen all day long from **morning** to **evening**. What time of day is 12:00 PM?", "Noon / Midday", "Midnight", "Dawn", "Twilight", "A", "Noon/midday is 12:00 PM."),
        ("What is the abbreviation for **Monday**?", "Mon.", "Mnd.", "Mo.", "Mn.", "A", "Mon. is standard abbreviation."),
        ("How many days are in a standard non-leap year?", "365 days", "366 days", "300 days", "350 days", "A", "Standard year has 365 days."),
        ("Which month comes right after July?", "August", "September", "June", "May", "A", "August comes after July."),
        ("What is the short abbreviation for **August**?", "Aug.", "Augu.", "Au.", "Ag.", "A", "Aug. is standard abbreviation."),
        ("If today is Tuesday, what day was yesterday?", "Monday", "Wednesday", "Sunday", "Saturday", "A", "Yesterday was Monday."),
        ("If today is Wednesday, what day will tomorrow be?", "Thursday", "Tuesday", "Friday", "Saturday", "A", "Tomorrow will be Thursday."),
        ("What is the abbreviation for **Tuesday**?", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. is standard abbreviation."),
        ("Which day comes between Friday and Sunday?", "Saturday", "Thursday", "Monday", "Wednesday", "A", "Saturday is between Friday and Sunday."),
        ("What is the abbreviation for **October**?", "Oct.", "Octo.", "Oc.", "Ot.", "A", "Oct. is standard abbreviation."),
        ("Which month comes right before February?", "January", "December", "March", "November", "A", "January comes before February.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_days, start=1):
        qid = f"BK02_CH05_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}" ]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The picky customer visited the lodge on **Thursday**. Crum created the crispy chips on **Friday**. On which day were potato chips invented?", "Friday", "Thursday", "Saturday", "Wednesday", "A", "Friday is the day Crum fried the paper-thin chips."),
        ("George Crum worked from **9:00 AM to 6:00 PM** on the day of the invention. How many hours did he work?", "9 hours", "8 hours", "10 hours", "7 hours", "A", "6:00 PM - 9:00 AM = 9 hours."),
        ("Match the day with its abbreviation: **Wednesday**", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard."),
        ("If Moon Lake Lodge was open from **Monday to Saturday**, how many days a week was it open?", "6 days", "5 days", "7 days", "4 days", "A", "Mon, Tue, Wed, Thu, Fri, Sat = 6 days."),
        ("Identify the correctly spelt month name:", "September", "Septembre", "Septemberr", "Septembere", "A", "September is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Sunday - Snd.", "D", "Sunday abbreviation is Sun., not Snd."),
        ("Potato chips were invented in **1853**. How many years ago was 1853 from the year 1863?", "10 years", "5 years", "20 years", "100 years", "A", "1863 - 1853 = 10 years."),
        ("Which month has 31 days and comes right before August?", "July", "June", "September", "May", "A", "July has 31 days and precedes August."),
        ("Rearrange in correct chronological order: Fri, Tue, Wed, Thu", "Tue, Wed, Thu, Fri", "Wed, Tue, Thu, Fri", "Tue, Thu, Wed, Fri", "Fri, Thu, Wed, Tue", "A", "Tuesday -> Wednesday -> Thursday -> Friday."),
        ("What day is 2 days before Saturday?", "Thursday", "Friday", "Wednesday", "Sunday", "A", "Saturday - 2 days = Friday(1), Thursday(2)."),
        ("If Crum fried each batch of chips in 15 minutes, how many batches could he fry in 1 hour?", "4 batches", "2 batches", "6 batches", "3 batches", "A", "1 hour = 60 minutes. 60 / 15 = 4 batches."),
        ("Select the month that has 30 days:", "June", "July", "August", "October", "A", "June has 30 days."),
        ("Which abbreviation stands for **April**?", "Apr.", "Ap.", "Apl.", "Aprl.", "A", "Apr. is standard abbreviation."),
        ("If today is **Sun.**, what day will it be after 7 days?", "Sunday", "Monday", "Saturday", "Friday", "A", "7 days is a full week cycle, landing on Sunday again."),
        ("The restaurant kitchen operated from **10:00 AM to 10:00 PM**. How many hours was the kitchen active?", "12 hours", "10 hours", "14 hours", "8 hours", "A", "10:00 PM - 10:00 AM = 12 hours."),
        ("Identify the word that means 'occurring once every day':", "Daily", "Weekly", "Monthly", "Yearly", "A", "Daily means once a day."),
        ("Which of the following is a weekday (work day)?", "Wednesday", "Sunday", "Saturday", "Weekend", "A", "Wednesday is a weekday."),
        ("Choose the correct abbreviation for **October**:", "Oct.", "Octo.", "Oc.", "Ot.", "A", "Oct. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH05_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("George Crum worked as a chef from **Mon., 1st Aug.** to **Fri., 5th Aug.**. How many days did he work in that period?", "5 days", "4 days", "3 days", "7 days", "A", "1st to 5th Aug inclusive is 5 days."),
        ("George Crum prepared chips continuously from **1:15 PM to 2:15 PM**. For how many minutes did he fry chips?", "60 minutes (1 hour)", "45 minutes", "90 minutes", "30 minutes", "A", "1 hour = 60 minutes."),
        ("Solve the calendar puzzle: If 1st August 1853 was a Monday, what day of the week was 8th August 1853?", "Monday", "Tuesday", "Sunday", "Friday", "A", "1 + 7 = 8th August, landing on Monday."),
        ("Analyze this schedule: Crum cooked on Mon, Wed, Fri; Assistant cooked on Tue, Thu, Sat. On which day did BOTH rest?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in cooking schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If potato chips became a hit in a fortnight, how many days did it take to become popular?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Jul, Aug, Oct, Sep, Nov'", "October and September are in wrong order.", "August is in wrong position.", "November should be first.", "No error.", "A", "September comes before October (Jul, Aug, Sep, Oct, Nov)."),
        ("The summer season at Moon Lake Lodge ended on **31st August**. What date was the next day?", "1st September", "32nd August", "30th August", "1st October", "A", "August has 31 days, so next day is 1st September."),
        ("If yesterday was two days before Saturday, what day is tomorrow?", "Saturday", "Friday", "Sunday", "Thursday", "A", "Two days before Saturday = Thursday (yesterday). Today = Friday. Tomorrow = Saturday."),
        ("Calculate: How many days are there in total during **July** and **August** combined?", "62 days (31 + 31)", "60 days", "61 days", "59 days", "A", "Both July (31) and August (31) have 31 days. 31 + 31 = 62 days."),
        ("HOTS Reasoning: Why did summer resorts like Moon Lake Lodge have more customers in July and August?", "July and August are warm summer vacation months when tourists travel to resorts.", "Because chips are cold.", "Because winter is hot.", "Because chef was sleeping.", "A", "Summer vacation months attract hotel guests."),
        ("Identify the correct statement about a leap year:", "A leap year has 366 days and February has 29 days.", "A leap year has 365 days.", "February has 28 days in leap year.", "A leap year occurs every 3 years.", "A", "Leap year has 366 days (Feb = 29 days)."),
        ("George Crum prepared 100 bags of chips in 4 hours. How many bags did he prepare per hour?", "25 bags per hour", "50 bags", "100 bags", "20 bags", "A", "100 / 4 = 25 bags per hour."),
        ("Which month pair both have 31 days and come right after each other in mid-summer?", "July and August", "June and July", "August and September", "May and June", "A", "July (31) and August (31) are consecutive 31-day summer months.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH05_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 05: Invention of Potato Chips\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("George Crum **worked** as a chef at Moon Lake Lodge.", "worked", "George Crum", "chef", "Lodge", "A", "'worked' is the action verb."),
        ("A picky customer **walked** into the restaurant.", "walked", "picky", "customer", "restaurant", "A", "'walked' is the action verb."),
        ("The customer **complained** about the thick fries.", "complained", "customer", "thick", "fries", "A", "'complained' is the vocal/mental action verb."),
        ("Crum **sliced** the potatoes very thinly.", "sliced", "Crum", "potatoes", "thinly", "A", "'sliced' is the physical action verb."),
        ("Crum **fried** the potato slices until crispy.", "fried", "Crum", "slices", "crispy", "A", "'fried' is the physical action verb."),
        ("He **seasoned** the chips with extra salt.", "seasoned", "he", "chips", "extra", "A", "'seasoned' is the action verb."),
        ("The customer **loved** the thin crispy chips.", "loved", "customer", "thin", "chips", "A", "'loved' is the emotional action verb."),
        ("Other customers **asked** for the new snack.", "asked", "other", "customers", "snack", "A", "'asked' is the vocal action verb."),
        ("People **queued** up outside the restaurant.", "queued", "people", "outside", "restaurant", "A", "'queued' is the action verb."),
        ("Crum **lost** his patience during work.", "lost", "Crum", "patience", "during", "A", "'lost' is the action verb."),
        ("The customer **returned** the plate to the kitchen.", "returned", "customer", "plate", "kitchen", "A", "'returned' is the action verb."),
        ("George Crum **invented** a popular snack.", "invented", "George Crum", "popular", "snack", "A", "'invented' is the action verb."),
        ("The chef **served** the crispy chips on a plate.", "served", "chef", "crispy", "plate", "A", "'served' is the action verb."),
        ("People **enjoy** potato chips all over the world.", "enjoy", "people", "chips", "world", "A", "'enjoy' is the action verb."),
        ("Crum **cut** the potatoes into paper-thin slices.", "cut", "Crum", "potatoes", "slices", "A", "'cut' is the action verb."),
        ("The customer **praised** the new dish.", "praised", "customer", "new", "dish", "A", "'praised' is the action verb."),
        ("The oil **bubbled** in the deep pan.", "bubbled", "oil", "deep", "pan", "A", "'bubbled' is the action verb."),
        ("George Crum **proved** that anger can bring creativity.", "proved", "George Crum", "anger", "creativity", "A", "'proved' is the action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH05_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 05:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'George Crum **skillfully** **sliced** the **fresh** **potatoes**.'", "sliced", "skillfully", "fresh", "potatoes", "A", "'sliced' shows physical action; 'skillfully' is adverb, 'fresh' is adjective, 'potatoes' is noun."),
        ("Identify BOTH action verbs in: 'George Crum **fried** the slices and **seasoned** them with salt.'", "fried, seasoned", "Crum, slices", "salt, fried", "seasoned, salt", "A", "'fried' and 'seasoned' are both action verbs."),
        ("What is the past tense action verb of 'send' as used in story ('sent them back to kitchen')?", "sent", "sended", "sending", "sends", "A", "Past tense of send is sent."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "George Crum will **slice** the potatoes.", "The knife made a clean **slice**.", "Give me a **slice** of cake.", "That is a thick **slice**.", "A", "In (A), 'slice' acts as the main action verb."),
        ("Find the action verb in: 'The customer tasted the thin crispy fries.'", "tasted", "customer", "thin", "fries", "A", "'tasted' is the action verb."),
        ("Which sentence contains NO physical action verb?", "George Crum was an experienced chef.", "He sliced the potatoes thin.", "He fried them in hot oil.", "He served the chips to customers.", "A", "'George Crum was an experienced chef' contains linking verb 'was', but no physical action verb."),
        ("Change the action verb 'lose' to past tense: 'Crum (lose) his patience.'", "lost", "losed", "losing", "loses", "A", "Past tense of lose is lost."),
        ("Identify the action verb: 'The customer ate the chips and praised the chef.'", "ate, praised", "customer, chips", "chef, ate", "praised, chips", "A", "'ate' and 'praised' are action verbs."),
        ("Select the action verb that completes the sentence: 'Potato chips ____ popular around the globe.'", "became / remain", "crispy", "snack", "salty", "A", "'became' / 'remain' is an action verb."),
        ("Which word is an action verb? (potatoes, salt, seasoned, kitchen)", "seasoned", "potatoes", "salt", "kitchen", "A", "'seasoned' is an action verb; others are nouns."),
        ("What action did Crum perform out of frustration?", "sliced", "picky", "fries", "salt", "A", "He sliced the potatoes paper-thin (action verb)."),
        ("Identify the action verb in: 'George Crum thought of a clever trick.'", "thought", "Crum", "clever", "trick", "A", "'thought' is a mental action verb."),
        ("Choose the correct action verb: 'The customers ____ in line for the fries.'", "queued", "line", "long", "restaurant", "A", "'queued' is the action verb."),
        ("Identify the action verb in: 'The picky customer rejected the thick fries.'", "rejected", "picky", "customer", "thick", "A", "'rejected' is the action verb."),
        ("Which of these words is NOT an action verb? (fry, slice, salty, serve)", "salty", "fry", "slice", "serve", "A", "'salty' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'George Crum sprinkled extra salt.'", "sprinkled", "George Crum", "extra", "salt", "A", "'sprinkled' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The waiter ____ the dish to the customer's table.'", "carried / brought", "salty", "thin", "plate", "A", "'carried' / 'brought' is an action verb."),
        ("What action verb completes the sentence? 'Millions of people ____ potato chips every day.'", "consume / eat", "delicious", "snack", "world", "A", "'consume' / 'eat' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH05_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The frustrated chef angrily sliced the potatoes and fried them until crispy.' How many total ACTION VERBS are present?", "2 action verbs ('sliced', 'fried')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'sliced' and 'fried' are action verbs; 'frustrated', 'angrily', 'crispy' are adjectives/adverbs."),
        ("Categorize the verbs: In 'George Crum **was** frustrated, so he **sliced** the potatoes thin', classify 'was' and 'sliced'.", "'was' is a linking verb; 'sliced' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'was' is action; 'sliced' is linking.", "A", "'was' links state of being; 'sliced' shows physical action."),
        ("Replace the weak verb with a strong action verb: 'Crum **put** extra salt on the chips.'", "Crum **generously seasoned** the chips with salt.", "Crum **was near** the salt.", "Crum **saw** the salt.", "Crum **looked at** the salt.", "A", "'generously seasoned' is a much stronger, vivid action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "George Crum **sliced** the potatoes, **fried** them, and **served** the chips.", "George Crum was talented, angry, and famous.", "The chips were thin, salty, and crispy.", "The restaurant was located in New York.", "A", "sliced, fried, served are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "The customer **demanded** thinner fries.", "The customer was **picky**.", "The fries were **thick**.", "The chef was **busy**.", "A", "'demanded' is an action verb."),
        ("Spot the incorrect verb tense: 'Crum **slice** the potatoes paper-thin yesterday.' Correct it:", "'slice' should be 'sliced' (past action verb).", "'slice' should be 'slicing'.", "'slice' should be 'slices'.", "'slice' should be 'will slice'.", "A", "Past time indicator 'yesterday' requires past tense action verb 'sliced'."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (complained, sliced, fried, praised)", "complained -> sliced -> fried -> praised", "praised -> fried -> sliced -> complained", "sliced -> complained -> praised -> fried", "fried -> sliced -> praised -> complained", "A", "First customer complained, Crum sliced potatoes, fried them, customer praised dish."),
        ("Identify the verb error in dialogue: Picky customer said, 'I have **send** back these fries twice!'", "'send' is incorrect; the past participle form is 'sent' ('have sent').", "'send' should be 'sending'.", "'send' should be 'sends'.", "No error.", "A", "Perfect tense requires past participle 'sent'."),
        ("Analyze this sentence: 'George Crum **invented** potato chips out of anger.' What type of action verb is 'invented'?", "Creative/Production action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'invented' is an action verb describing creative production."),
        ("Which sentence uses action verbs to show cause and effect?", "Crum **sliced** the potatoes paper-thin, so the customer **loved** them.", "Crum was a chef and the lodge was in New York.", "The fries were thick and salty.", "People queued outside the shop.", "A", "'sliced' (cause action) -> 'loved' (effect action)."),
        ("Spot the missing action verb: 'Crum ____ the thin slices into boiling oil and ____ them with salt.'", "dropped, sprinkled", "salty, hot", "was, was", "quick, slow", "A", "'dropped' and 'sprinkled' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'demanded' in 'Customer demanded thinner fries' considered an IMPERATIVE action verb?", "Because it describes an urgent, authoritative request for action.", "Because demanding requires potatoes.", "Because fries are food.", "Because it is a noun.", "A", "Descriptive speech action verb conveying imperative request."),
        ("Transform the action verb to future tense: 'George Crum **invents** a new snack.'", "George Crum **will invent** a new snack.", "George Crum **invented** a new snack.", "George Crum **is inventing** a new snack.", "George Crum **invent** a new snack.", "A", "'will invent' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "Millions of people **enjoy** potato chips.", "Millions of people **enjoys** potato chips.", "A person **enjoy** potato chips.", "Millions of people **is enjoying** potato chips.", "A", "Plural subject 'people' takes base verb 'enjoy' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH05_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 05: Invention of Potato Chips\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'George Crum worked at Moon Lake Lodge__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'Why did the customer send the fries back__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a proper name like 'George Crum'?", "First letter of each word (e.g., George Crum)", "The last letter", "All letters", "No letters", "A", "Proper names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'The chef prepared fries__ chips__ and snacks.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden delight: 'These paper-thin chips taste amazing__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense delight/excitement."),
        ("Select the proper noun that MUST start with a capital letter:", "New York", "potato", "kitchen", "salt", "A", "'New York' as a city/state name starts with capital letters."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'george Crum was a talented chef.'", "george -> George", "talented -> Talented", "chef -> Chef", "was -> Was", "A", "First name 'George' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'Millions of people enjoy potato chips today [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which place name is capitalized correctly?", "Moon Lake Lodge", "moon lake lodge", "Moon lake Lodge", "MOON LAKE LODGE", "A", "Capital letters for proper resort name."),
        ("What mark goes after a speaker tag: 'The customer complained__ \"These fries are too thick!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'the chef said, \"i will make them thinner.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The customer praised the new dish.", "The customer praised the new dish?", "The customer praised the new dish,", "The customer praised the new dish;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like 'the **chef's** recipe'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which book chapter title is capitalized correctly?", "Invention of Potato Chips", "invention of potato chips", "Invention Of Potato Chips", "INVENTION OF POTATO CHIPS", "A", "Major words in titles are capitalized."),
        ("What punctuation mark is used around spoken dialogue: '___These chips are delicious!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Speech marks enclose spoken dialogue.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH05_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "George Crum worked at Moon Lake Lodge in New York on Monday.", "george crum worked at moon lake lodge in new york on monday.", "George Crum worked at moon lake lodge in New York on monday?", "george Crum Worked At Moon Lake Lodge In New York On Monday.", "A", "George Crum (name), Moon Lake Lodge (place), New York (city), Monday (day) capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Why did the customer complain about the French fries?", "Why did the customer complain about the French fries.", "Why did the customer complain about the French fries!", "Why did the customer complain about the French fries,", "A", "Question starting with 'Why' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'george Crum cooked in a kitchen near the Lake.'", "'george' should be capitalized ('George'); 'Lake' should be lowercase.", "'Lake' should be capitalized only.", "'kitchen' should be capitalized.", "No mistake.", "A", "First name 'George' capitalized; common noun lake lowercase here."),
        ("Choose the correctly punctuated dialogue sentence:", "\"These fries are much too thick,\" complained the customer.", "these fries are much too thick complained the customer.", "\"These fries are much too thick\" complained the customer", "These fries are much too thick, complained the customer.", "A", "Quotation marks around dialogue, comma inside quote, capital T."),
        ("Identify where a COMMA is missing: 'Crum prepared fries chips and snacks.'", "Between 'fries' and 'chips' ('fries, chips')", "After 'Crum'", "After 'snacks'", "No comma needed", "A", "Commas separate items in list: 'fries, chips and snacks'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is George Crum's recipe.", "This is George Crums' recipe.", "This is George Crums recipe.", "This is George Crum's' recipe.", "A", "Crum's indicates possession by Crum."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a crispy and delicious snack this is!", "What a crispy and delicious snack this is?", "What a crispy and delicious snack this is.", "What a crispy and delicious snack this is,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'was not'?", "wasn't", "was'nt", "wasnt'", "w'asnt", "A", "wasn't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "George Crum lived in New York in 1853.", "george crum lived in new york in 1853.", "George Crum Lived In New York In 1853.", "george Crum lived in New York in 1853.", "A", "'George Crum' and 'New York' capitalized as proper names."),
        ("What punctuation mark belongs in the blank? 'The customer exclaimed, \"Delicious__ I love these thin chips!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses delight."),
        ("Choose the correct form for 'did not':", "didn't", "did'nt", "didnt'", "d'idnt", "A", "didn't is standard contraction."),
        ("Identify the punctuation error: 'The customer ate the chips, he asked for more.'", "Comma splice between two independent clauses (should be full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for names and places:", "George Crum worked at Moon Lake Lodge in New York.", "george crum worked at moon lake lodge in new york.", "George Crum worked at moon Lake lodge in New York.", "george Crum worked at Moon Lake lodge in new york.", "A", "Names 'George Crum', 'Moon Lake Lodge', 'New York' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "The customer's plate was empty.", "The customers' plate was empty.", "The customers plate was empty.", "The customer's' plate was empty.", "A", "customer's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'Crum added ____'", "salt, pepper, and spices.", "salt pepper and spices.", "salt; pepper; and spices.", "salt: pepper: and spices.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "How were potato chips invented?", "How were potato chips invented.", "How were potato chips invented!", "how were potato chips invented.", "A", "Capital H, ends with question mark ?"),
        ("Fix the sentence: 'where is crums restaurant'", "Where is Crum's restaurant?", "Where is crums restaurant.", "where is Crum's restaurant!", "Where is Crums' restaurant?", "A", "Capital W, possessive Crum's, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Crum said, \"I will slice them paper-thin!\"", "Crum said \"i will slice them paper-thin!\"", "crum said, \"I will slice them paper-thin!\"", "Crum said, \"I will slice them paper-thin.\"", "A", "Capital C, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH05_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'in 1853 george crum worked in new york and said, try these chips'", "5 errors (in->In, george crum->George Crum, new york->New York, quotation marks, capital T in Try, period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, person name, place name, quotation marks, capital Try, period."),
        ("Correct the entire dialogue paragraph: 'the customer complained these fries are too thick george crum replied i will make them thinner'", "\"These fries are too thick!\" complained the customer. George Crum replied, \"I will make them thinner.\"", "the customer complained \"these fries are too thick\" george crum replied \"i will make them thinner.\"", "The customer complained, These fries are too thick. George Crum replied, I will make them thinner.", "\"These fries are too thick?\" Complained the customer. George Crum replied \"I will make them thinner?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'Crum**'**s chips are crispy, and he**'**s famous.'", "First 's is possessive (chips belonging to Crum); second 's is contraction (he is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "Crum's chips = chips of Crum; he's = he is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"These chips are paper-thin,\" Said George Crum.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'These' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "Crum was frustrated, but he created a great dish.", "Crum was frustrated but, he created a great dish.", "Crum was frustrated but he created a great dish!", "Crum was frustrated; but he created a great dish?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'george crum worked at moon lake lodge on monday 15th august 1853'", "George Crum worked at Moon Lake Lodge on Monday, 15th August 1853.", "george crum worked at moon lake lodge on monday, 15th august 1853.", "George Crum worked at Moon Lake Lodge on Monday 15th August 1853", "George Crum worked at Moon Lake lodge on monday 15th august 1853.", "A", "George Crum, Moon Lake Lodge, Monday, 15th August 1853, period."),
        ("Identify why exclamation mark is necessary here: '\"These are delicious! I want more!\"'", "Because the customer is expressing high enthusiasm and delight.", "Because fries are hot.", "Because kitchen is busy.", "Because sentence is long.", "A", "Exclamation mark communicates high enthusiasm/delight."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "George Crum, a chef at Moon Lake Lodge, invented potato chips.", "George Crum a chef at Moon Lake Lodge invented potato chips.", "George Crum, a chef at Moon Lake Lodge invented potato chips.", "George Crum a chef at Moon Lake Lodge, invented potato chips.", "A", "Appositive phrase 'a chef at Moon Lake Lodge' is set off by commas."),
        ("Analyze the use of hyphen in: 'The paper-thin potato chips were crispy.'", "Hyphen joins compound adjective (paper-thin).", "Hyphen replaces comma.", "Hyphen indicates question.", "Hyphen is an apostrophe.", "A", "Compound adjectives modifying nouns take hyphens."),
        ("Identify the correct sentence with direct speech quote within text:", "George Crum announced, \"The chips are ready,\" and served them.", "George Crum announced \"The chips are ready\" and served them.", "George Crum announced, 'The chips are ready,' and served them.", "George Crum announced: \"The chips are ready\" and served them.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The customers plate was filled with crispy chips.'", "Missing apostrophe in 'customer's' -> 'The customer's plate'", "Missing apostrophe in 'chips''", "Missing apostrophe in 'was''", "No apostrophe needed", "A", "'customer's plate' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Crum, said the customer, is a genius.' vs 'Crum said, \"The customer is a genius.\"'", "In the first, customer calls Crum a genius; in the second, Crum calls customer a genius.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is described."),
        ("Correct all 4 errors in: 'whats the chefs name asked the customer'", "\"What's the chef's name?\" asked the customer.", "whats the chefs name? asked the customer.", "\"What's the chefs name.\" asked the customer.", "\"whats the chefs name?\" Asked the customer.", "A", "Quotation marks, capital W, possessive chef's, question mark, period at end."),
        ("Identify the rule for capitalizing geographical place names like 'New York':", "Specific proper place names (cities, states, resorts) take initial capital letters.", "Place names are never capitalized.", "Place names are capitalized only at end of sentence.", "Place names must be written in ALL CAPS.", "A", "Proper place names take initial capitals.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH05_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 05: Invention of Potato Chips\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'seasoned'** (in Chapter 05)?", "ea", "ee", "ai", "ou", "A", "'ea' is the vowel digraph in seasoned."),
        ("Identify the vowel digraph in the word **'queued'**:", "ue / eu", "ea", "oa", "ui", "A", "'ue' / 'eu' forms the vowel combination in queued."),
        ("Which word from the story contains the **'ie'** vowel digraph?", "fries", "potato", "chip", "salt", "A", "'ie' forms long /i/ sound in fries."),
        ("Identify the vowel digraph in the word **'beach'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in beach."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'oo'** vowel digraph: 'George Crum worked at Moon Lake Lodge.'", "Moon", "George", "Crum", "Lodge", "A", "'Moon' contains 'oo' digraph."),
        ("Which word from the story rhymes with **'chip'**?", "dip", "chop", "chat", "cheep", "A", "'dip' rhymes with 'chip'."),
        ("Which word from the story rhymes with **'fry'**?", "sky", "free", "few", "fan", "A", "'sky' rhymes with 'fry'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the story rhymes with **'slice'**?", "nice", "slow", "slip", "slate", "A", "'nice' rhymes with 'slice'."),
        ("Identify the vowel digraph in **'oil'** (used for frying):", "oi", "ea", "ee", "ia", "A", "'oi' is the vowel digraph in oil."),
        ("Which word from Chapter 05 has the **'ea'** digraph making a long /e/ sound?", "seasoned", "head", "heavy", "dead", "A", "'seasoned' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letter in **'talk'** (as in 'people talk about chips'):", "l", "t", "a", "k", "A", "Silent 'l' in talk."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "delight", "bought", "bowl", "baker", "A", "'igh' in delight makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They found a new snack.'", "found", "snack", "new", "they", "A", "'found' contains 'ou' digraph."),
        ("Which word rhymes with **'dish'**?", "fish", "dash", "door", "deck", "A", "'fish' rhymes with 'dish'."),
        ("Identify the silent letter in the word **'know'** (as in 'did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH05_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'seasoned'** and **'bread'**. What is the difference?", "'seasoned' has long /e/ sound; 'bread' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'seasoned' has short /e/; 'bread' has long /e/.", "A", "'ea' can make long /e/ (seasoned) or short /e/ (bread)."),
        ("Select the word pair from Chapter 05 that has the SAME vowel digraph sound:", "Moon - spoon", "fries - bread", "seasoned - roar", "chip - sweet", "A", "'Moon' and 'spoon' both have 'oo' long /oo/ sound."),
        ("Which word contains a SILENT letter? (slice, chip, salt, cook)", "slice", "chip", "salt", "cook", "A", "'slice' has silent final 'e'."),
        ("Identify the odd one out based on vowel sound: (season, tea, beach, bread)", "bread", "season", "tea", "beach", "A", "'bread' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for oil cooking? 'fr__ing'", "y", "ie", "ea", "ee", "A", "'frying' uses 'y' for long /i/ sound."),
        ("Group these story words by digraph: **found**, **out**, **shouted**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'The chef made **thin** slices.'", "thin", "chef", "made", "slices", "A", "'thin' contains unvoiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (bowl, grow, slow, all of these)", "all of these", "bowl", "grow", "slow", "A", "bowl, grow, slow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'season'**:", "ea", "on", "se", "as", "A", "'ea' is the digraph in season."),
        ("Which word from the story has a silent **'k'**? (knife, knock, knee, all of these)", "all of these", "knife", "knock", "knee", "A", "knife, knock, knee all have silent initial 'k'."),
        ("Select the word that rhymes with **'slice'** and fits sentence: 'The chips were very ____.'", "nice", "rice", "mice", "twice", "A", "'nice' rhymes with 'slice'."),
        ("Identify the digraph in **'creamy'**:", "ea", "ee", "ai", "oa", "A", "'ea' makes long /e/ sound."),
        ("Which word has the short /u/ sound made by **'ou'**? (tough, house, out, shout)", "tough", "house", "out", "shout", "A", "'tough' has short /u/ sound with 'ou'."),
        ("Find the R-controlled vowel sound in: 'The customer visited the **park**.'", "ar sound", "ea", "ou", "ai", "A", "R-controlled vowel in park."),
        ("Which word contains the **'oi'** diphthong/digraph? (boil, point, choice, all of these)", "all of these", "boil", "point", "choice", "A", "boil, point, choice all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 05 vocabulary: (slice, chef, crispy, customer)", "slice", "chef", "crispy", "customer", "A", "'slice' has soft /s/ sound for 'c' before 'e'; others have hard /k/ or /sh/ sound."),
        ("Which word has a soft **'g'** sound? (George, lodge, magic, all of these)", "all of these", "George", "lodge", "magic", "A", "George, lodge, magic all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ea'** digraph for adding salt:", "seasoned", "seasonnd", "seazoned", "sesoned", "A", "seasoned is standard spelling.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH05_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'slice'** sound like /s/, but 'c' in **'crispy'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound; before 'r', 'a', 'o', 'u' it makes hard /k/ sound.", "Because slice is thin.", "Because crispy is salty.", "There is no rule.", "A", "Soft 'c' rule: c + i, e, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (seasoned, beach, bread, heavy, lead [metal])", "Long /e/: seasoned, beach; Short /e/: bread, heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: bread; Short /e/: seasoned", "A", "seasoned, beach make long /e/; bread, heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "slice - knife", "chip - salt", "fry - cook", "snack - bowl", "A", "'slice' (silent e) and 'knife' (silent k and e)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "sprinkled / scraped", "chef", "fry", "slice", "A", "'spr' / 'scr' blend types."),
        ("Examine the hard vs soft 'g' rule: Why is 'g' soft in **'George'** but hard in **'good'**?", "'g' followed by 'e', 'i', or 'y' makes soft /j/ sound (George); 'g' before 'o' or 'a','u' makes hard /g/ sound (good).", "Because George is a chef.", "Because good is tasty.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "seasoned", "chip", "potatoes", "salt", "A", "'seasoned' has 'ea' digraph and silent 'e' in -ed."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'out'**?", "out - found", "boil - coin", "paid - day", "boat - coat", "A", "'out' and 'found' share /ow/ diphthong sound."),
        ("Analyze homophones: 'Crum added **salt** / **assault**.' Which word is the seasoning?", "salt", "assault", "solt", "salte", "A", "'salt' is the seasoning mineral."),
        ("Identify the phonic pattern in **'potatoes'**: What vowel sound does the second 'o' make?", "Long /o/ sound", "Short /o/ sound", "Silent sound", "Long /a/ sound", "A", "'po-ta-toes' second 'o' makes long /o/ sound."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (chips, potatoes, slices, chefs)", "potatoes / slices", "chips", "chefs", "snacks", "A", "Plurals ending in voiced vowels take /z/ ending sound (potatoes)."),
        ("Spot the word where 'k' is SILENT: (knife, knock, knee, all of these)", "all of these", "knife", "knock", "knee", "A", "'k' is silent before 'n' in knife, knock, knee."),
        ("HOTS Reasoning: Why do 'fries' and 'guys' sound identical at the end but have different spellings?", "They use different letter patterns ('ies' vs 'uys') to produce the long /iz/ sound.", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Both 'ies' and 'uys' produce /iz/ ending sound."),
        ("Identify the compound word from story concepts containing two simple words:", "potato / chef", "Moonlight / workshop", "New York", "Lodge", "B", "Moonlight = moon + light."),
        ("Determine the syllable count and stress: How many syllables are in **'frustration'**?", "3 syllables (frus-tra-tion)", "2 syllables", "4 syllables", "1 syllable", "A", "frus-tra-tion has 3 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH05_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 05: Invention of Potato Chips\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ was George Crum?", "Who", "What", "Where", "Why", "A", "'Who' asks about a person (a chef at Moon Lake Lodge)."),
        ("___ was George Crum's original speciality dish?", "What", "Who", "Where", "When", "A", "'What' asks about a thing (thick-cut French fries)."),
        ("___ was Moon Lake Lodge located?", "Where", "Who", "What", "Why", "A", "'Where' asks about location (in New York)."),
        ("___ complained that the fries were too thick?", "Who", "What", "Where", "Why", "A", "'Who' asks about identity (a picky customer)."),
        ("___ did George Crum do when the customer sent back the fries?", "What", "Where", "Why", "When", "A", "'What' asks about action (sliced them paper-thin and fried them)."),
        ("___ did George Crum invent by accident out of frustration?", "What", "Who", "Where", "Why", "A", "'What' asks about invention (potato chips)."),
        ("___ did the customer keep sending the fries back?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (he found them too thick)."),
        ("___ did the customer react when he ate the thin crispy chips?", "How", "Who", "Where", "What", "A", "'How' asks about manner/reaction (loved and praised them)."),
        ("___ year were potato chips invented?", "Which / In what year", "Who", "Where", "Why", "A", "'Which' asks about specific year (1853)."),
        ("___ times did the customer send back the fries?", "How many", "Who", "Where", "Why", "A", "'How many' asks about number (several times)."),
        ("___ seasoning did Crum add to the paper-thin chips?", "What", "Who", "Where", "Why", "A", "'What' asks about seasoning (extra salt)."),
        ("___ customer asked for the new thin crispy fries next?", "Which", "Who", "Why", "When", "A", "'Which' / 'Who' asks about other customers."),
        ("___ did potato chips become popular?", "Where", "Who", "Why", "What", "A", "'Where' asks about place (all around the world)."),
        ("___ lesson does the story teach us?", "What", "Who", "Where", "Why", "A", "'What' asks about lesson (frustration and accidents can lead to great inventions)."),
        ("___ people enjoy potato chips today?", "How many", "Who", "Where", "Why", "A", "'How many' asks about quantity (millions of people)."),
        ("___ created the world's first potato chips?", "Who", "What", "Where", "Why", "A", "'Who' asks about inventor (George Crum)."),
        ("___ did Crum lose his patience?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (customer kept complaining)."),
        ("___ did other customers start demanding the new dish?", "When", "Who", "Where", "Why", "A", "'When' asks about time (after seeing the picky customer praise it).")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH05_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ did Crum slice the potatoes so thin?' Answer: 'Because he lost his patience with the picky customer.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ was Moon Lake Lodge?' Answer: 'In New York.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ were potato chips invented?'", "When", "Where", "Who", "Why", "A", "'When' inquires about time (in 1853)."),
        ("Form an asking sentence: 'Crum fried the slices.' -> '____ did Crum fry?'", "What", "Who", "Why", "Where", "A", "'What' inquires about object."),
        ("Identify the INCORRECT question word usage: '**Why** is the chef's name?'", "'Why' should be 'What'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'What is the chef's name?' asks for identity."),
        ("Select the proper interrogative sentence:", "Why did the customer send back the fries?", "Why the customer sent back the fries?", "Why did the customer sent back the fries?", "Why customer send back fries?", "A", "Interrogative word + auxiliary 'did' + base verb 'send'."),
        ("Which question word asks about MANNER or METHOD? '___ did Crum make the chips crispy?'", "How", "Who", "What", "Where", "A", "'How' inquires about method/manner (by frying in hot oil and seasoning with salt)."),
        ("Complete the question: '___ of the two dishes was thinner?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options."),
        ("Change statement to question: 'George Crum created potato chips.' -> '____ created potato chips?'", "Who", "What", "Where", "Why", "A", "'Who' asks for subject (George Crum)."),
        ("Fill in the blank: '___ thin did Crum slice the potatoes?'", "How", "What", "Where", "Why", "A", "'How thin' measures degree."),
        ("Identify the question word in: 'Whom did the customer complain to?'", "Whom", "did", "customer", "complain", "A", "'Whom' is the interrogative pronoun asking about object person."),
        ("Choose the question that matches this answer: 'He made them thin because he was frustrated.'", "Why did Crum make the fries paper-thin?", "Where did Crum cook?", "Who ate the fries?", "What did he cook?", "A", "'Why...' matches answer starting with 'because...'."),
        ("Fill in the blank: '___ dish was served at Moon Lake Lodge?'", "Which", "Who", "Why", "Where", "A", "'Which dish' asks for identification."),
        ("Complete: '___ salt did Crum add to the chips?'", "How much", "How many", "Who", "Where", "A", "'How much' asks about uncountable quantity (salt)."),
        ("Select the correct question for: 'George Crum sliced the potatoes paper-thin.'", "What did George Crum do?", "Where was George Crum?", "Why is George Crum lazy?", "Who was the customer?", "A", "'What did George Crum do?' asks for action."),
        ("Which question word inquires about POSSESSION? '___ recipe became famous worldwide?'", "Whose", "Who", "Where", "Why", "A", "'Whose' asks about origin/ownership."),
        ("Form question: 'Many customers queued up.' -> '____ customers queued up?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why did the customer complain.' Correct it:", "Why did the customer complain?", "Why did the customer complain!", "Why did the customer complain,", "Why did the customer complain;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH05_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why did George Crum fry the potatoes paper-thin?' What is the syntax pattern?", "Question Word + Helping Verb (did) + Subject (George Crum) + Main Verb (fry) + Object + Adverb", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ potatoes' vs '___ salt'", "'How many' for countable potatoes; 'How much' for uncountable salt.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for potatoes; 'How many' for salt.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where George Crum invented potato chips?' Correct it:", "Where **did** George Crum invent potato chips?", "Where George Crum invent potato chips?", "Where invented George Crum potato chips?", "Where does George Crum invented potato chips?", "A", "Past simple questions require auxiliary 'did' before subject and base verb 'invent'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the story plot?", "Who -> What was the original dish -> Why did customer complain -> How was potato chips invented", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals character, original state, conflict, and breakthrough resolution."),
        ("Transform the statement into a formal question: 'Frustration can lead to innovative comfort food.'", "How did chef's frustration lead to the creation of a beloved comfort food?", "Where is New York?", "Who is Crum?", "What is a potato?", "A", "Directly targets the moral lesson."),
        ("Analyze this ambiguous question: 'What did the chef do?' How can it be made precise?", "Add specific context: 'What method did George Crum use to prepare the paper-thin potato slices?'", "Make it shorter: 'What chef?'", "Change to: 'Where chef?'", "Remove 'What'.", "A", "Adding specific context clarifies which action."),
        ("Choose the correct question pair for dialogue: Customer: '___ are these fries so thick?' Crum: '___ about trying these paper-thin crispy chips?'", "Why, How", "Who, Where", "Where, How", "When, Whose", "A", "Why (reason for thick fries), How about (suggestion)."),
        ("Spot the DOUBLE auxiliary error: 'Why did George Crum sliced the potatoes thin?'", "'did' requires base verb 'slice', not past tense 'sliced'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('slice')."),
        ("Reconstruct question from answer: Answer: 'Potato chips were invented in 1853 at Moon Lake Lodge in New York.'", "Question: 'When and where were potato chips invented?'", "Question: 'Where did Crum fly?'", "Question: 'Who is picky customer?'", "Question: 'Why chips salty?'", "A", "Targets time and place of invention."),
        ("Form indirect question: 'The customer asked if the chef could make thinner fries.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ should we remain creative even when frustrated?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the practical/moral reason for persistence."),
        ("HOTS Reasoning: Why is 'Who' used for people/characters but 'Which' used when selecting from a specific group of snacks?", "'Who' is general; 'Which' is used when choosing from a defined limited set.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the snacks...' selects from a defined group."),
        ("Correct all errors in: 'who invented potato chips in 1853'", "Who invented potato chips in 1853?", "Who invented potato chips in 1853.", "Whom invented potato chips?", "Who does invented potato chips in 1853?", "A", "Capital W, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 05:", "How does George Crum's response to criticism show that challenges can inspire culinary innovation?", "What was the chef's name?", "Where was the lodge?", "Were the chips salty?", "A", "Asks student to evaluate moral theme and cause-and-effect.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH05_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 05: Invention of Potato Chips\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("George Crum is **slicing** the potatoes thinly.", "slicing", "Candy Crum", "is", "potatoes", "A", "'slicing' is verb + -ing form."),
        ("The chef is **frying** the thin potato slices.", "frying", "chef", "is", "slices", "A", "'frying' is verb + -ing form."),
        ("The customer is **complaining** about the thick fries.", "complaining", "customer", "is", "fries", "A", "'complaining' is verb + -ing form."),
        ("George Crum is **seasoning** the chips with salt.", "seasoning", "Crum", "is", "salt", "A", "'seasoning' is verb + -ing form."),
        ("The waiters are **serving** the crispy chips.", "serving", "waiters", "are", "chips", "A", "'serving' is verb + -ing form."),
        ("The customers are **queuing** outside the restaurant.", "queuing", "customers", "are", "restaurant", "A", "'queuing' is verb + -ing form."),
        ("George Crum is **working** hard in the kitchen.", "working", "Crum", "is", "kitchen", "A", "'working' is verb + -ing form."),
        ("The customer is **tasting** the paper-thin chips.", "tasting", "customer", "is", "chips", "A", "'tasting' is verb + -ing form."),
        ("The oil is **sizzling** in the deep pan.", "sizzling", "oil", "is", "pan", "A", "'sizzling' is verb + -ing form."),
        ("The people are **asking** for the new crispy snack.", "asking", "people", "are", "snack", "A", "'asking' is verb + -ing form."),
        ("George Crum is **pacing** across the kitchen floor.", "pacing", "Crum", "is", "floor", "A", "'pacing' is verb + -ing form."),
        ("The customer is **praising** the chef's new dish.", "praising", "customer", "is", "dish", "A", "'praising' is verb + -ing form."),
        ("The assistant is **packing** chips into paper bags.", "packing", "assistant", "is", "bags", "A", "'packing' is verb + -ing form."),
        ("George Crum is **creating** a brand new snack.", "creating", "Crum", "is", "snack", "A", "'creating' is verb + -ing form."),
        ("The children are **enjoying** potato chips at home.", "enjoying", "children", "are", "home", "A", "'enjoying' is verb + -ing form."),
        ("The kitchen staff is **cleaning** the deep fryers.", "cleaning", "staff", "is", "fryers", "A", "'cleaning' is verb + -ing form."),
        ("The restaurant is **gaining** fame for potato chips.", "gaining", "restaurant", "is", "fame", "A", "'gaining' is verb + -ing form."),
        ("George Crum is **sprinkling** salt over the hot chips.", "sprinkling", "Crum", "is", "chips", "A", "'sprinkling' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH05_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'slice'**? (He is ____ the potato.)", "slicing (drop final silent e)", "sliceing", "sliccing", "slicng", "A", "Drop final silent 'e' before adding -ing (slicing)."),
        ("What is the correct -ing spelling rule for **'fry'**? (Crum is ____ the chips.)", "frying (add -ing)", "flieing", "fryying", "fryng", "A", "Vowel/consonant + y verb adding -ing (frying)."),
        ("What is the correct -ing spelling rule for **'chop'**? (The cook is ____ potatoes.)", "chopping (double final consonant)", "choping", "choppping", "chopeing", "A", "CVC rule: double final consonant before -ing (chopping)."),
        ("Fill in the blank with present continuous form: 'George Crum (slice) ____ the potatoes thinly.'", "is slicing", "was slice", "are slice", "is sliced", "A", "Singular subject takes 'is slicing'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The chef is frying thin potato slices.", "The chef fried thin potato slices.", "The chef will fry thin potato slices.", "The chef fried yesterday.", "A", "'is frying' is present continuous."),
        ("Fill in the blanks: 'The chefs ____ (prepare) the meals, and Crum ____ (season) the chips.'", "are preparing, is seasoning", "is preparing, are seasoning", "are prepare, is season", "was preparing, were seasoning", "A", "Plural 'chefs' takes 'are preparing'; singular 'Crum' takes 'is seasoning'."),
        ("Identify the spelling mistake in: 'George Crum is **slicceing** the potatoes.'", "'slicceing' should be 'slicing'", "'slicceing' should be 'slicing'", "'is' should be 'are'", "No mistake", "A", "Slice drops silent e before -ing (slicing)."),
        ("Select the correct -ing form for **'serve'**:", "serving", "serveing", "servving", "servng", "A", "Drop silent 'e': serve -> serving."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "George Crum is sprinkling salt on the hot chips.", "George Crum sprinkled salt yesterday.", "George Crum sprinkles salt every day.", "George Crum will sprinkle salt tomorrow.", "A", "Present continuous ('is sprinkling') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (queue) in line to buy potato chips.'", "am queuing", "is queuing", "are queuing", "am queueing", "A", "Subject 'I' takes 'am queuing'."),
        ("Choose the correct form: 'The customers ____ (praise) the new crispy dish.'", "are praising", "is praising", "am praising", "are praise", "A", "Plural subject 'customers' takes 'are praising'."),
        ("Identify the verb in: 'Why are you sending back the French fries?'", "are sending", "Why", "you", "fries", "A", "Helping verb 'are' + main verb 'sending' form present continuous."),
        ("What is the -ing form of **'cut'**?", "cutting", "cuting", "cuttting", "cuteing", "A", "CVC rule: cut -> cutting."),
        ("What is the -ing form of **'season'**?", "seasoning", "seasonning", "seasoneing", "seasonng", "A", "Regular verb adding -ing (seasoning)."),
        ("Change simple present to continuous: 'Crum fries chips.' -> 'Crum ____ chips.'", "is frying", "fried", "was frying", "will fry", "A", "is frying."),
        ("Fill in the blank: 'The popularity ____ (growing) across the country.'", "is growing", "are growing", "am growing", "grew", "A", "is growing."),
        ("Identify the correct present continuous sentence:", "Look! The customer is eating the entire plate.", "Look! The customer eat the entire plate.", "Look! The customer ate the entire plate.", "Look! The customer eating the entire plate.", "A", "Exclamation 'Look!' introduces action happening now ('is eating')."),
        ("Select the correct -ing form for **'taste'**:", "tasting", "tasteing", "tassting", "tastng", "A", "Drop silent e: taste -> tasting.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH05_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (cut, slice, fry)", "cut -> cutting (double consonant), slice -> slicing (drop e), fry -> frying (add -ing)", "All just add -ing.", "All double the last letter.", "cut -> cuting, slice -> sliceing, fry -> friing", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'Crum sliced the potatoes while the customer waited.'", "Crum is slicing the potatoes while the customer is waiting.", "Crum slicing while customer waiting.", "Crum was slicing while customer waited.", "Crum will slice while customer waits.", "A", "Both verbs transformed to present continuous (is slicing, is waiting)."),
        ("Spot the missing auxiliary verb in: 'Crum frying the chips and customers queuing.' Correct it:", "'Crum **is** frying the chips and customers **are** queuing.'", "'Crum frying chips and customers queuing.'", "'Crum **are** frying and customers **is** queuing.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'The customer is **preferring** crispy chips'?", "Because 'prefer' is a stative verb expressing a preference, not an ongoing physical action.", "Because 'preferring' is hard to spell.", "Because Crum fried them.", "Because salt was extra.", "A", "Stative verbs (prefer, know, love) do not usually take continuous form."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The chefs at the lodge are frying thin potato slices.", "The chefs at the lodge is frying thin potato slices.", "The chefs at the lodge am frying thin potato slices.", "The chefs at the lodge frying thin potato slices.", "A", "Plural subject ('chefs') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'Crum is serving thick fries.' -> Negative:", "Crum is **not** serving thick fries.", "Crum not serving thick fries.", "Crum is no serving thick fries.", "Crum isn't serve thick fries.", "A", "Add 'not' between auxiliary 'is' and main verb 'serving'."),
        ("Spot all THREE spelling errors: 'He is **slicingg** potatoes, **runing** around, and **dieing** to cook.'", "'slicingg' -> 'slicing'; 'runing' -> 'running'; 'dieing' -> 'dying'", "'slicingg' -> 'slicng'; 'runing' -> 'runing'; 'dieing' -> 'dieing'", "No errors.", "Only 'runing' is wrong.", "A", "slicing (single g), running (double n), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'George Crum is preparing the new dish.'", "**Is** George Crum preparing the new dish?", "Are George Crum preparing the new dish?", "George Crum preparing the new dish?", "Why George Crum is preparing dish?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The restaurant **is opening** a new branch next month.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While Crum is frying the chips, the waiters are serving the guests.", "While Crum fried, waiters are serving.", "Crum is frying while waiters served.", "Crum fry while waiters serve.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'Crum is fryying the paper-thin potatoes.'", "'fryying' should be 'frying' (single 'y').", "'is' should be 'are'.", "'potatoes' should be capitalized.", "No error.", "A", "Fry + ing = frying."),
        ("HOTS Reasoning: Compare 'Crum fried the chips' (Past Simple) vs 'Crum is frying the chips' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means chips were burnt.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the customers ____ (asking) for thin fries?'", "are, asking", "is, asking", "am, asking", "do, asking", "A", "Plural subject customers takes 'are ... asking'."),
        ("Identify the correct present continuous sentence describing kitchen work:", "The entire kitchen team is preparing potato chips.", "The entire kitchen team is prepare potato chips.", "The entire kitchen team are preparing potato chips.", "The entire kitchen team preparing potato chips.", "A", "Collective singular subject 'kitchen team' + is + preparing.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH05_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 05: Invention of Potato Chips\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("George Crum ___ a famous chef.", "is", "are", "am", "be", "A", "Singular subject 'George Crum' takes 'is'."),
        ("I ___ enjoying the story of potato chips.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The potato chips ___ thin and crispy.", "are", "is", "am", "be", "A", "Plural subject 'potato chips' takes 'are'."),
        ("Moon Lake Lodge ___ located in New York.", "is", "are", "am", "be", "A", "Singular subject 'Moon Lake Lodge' takes 'is'."),
        ("The French fries ___ too thick for the customer.", "are", "is", "am", "be", "A", "Plural subject 'French fries' takes 'are'."),
        ("The picky customer ___ hard to satisfy.", "is", "are", "am", "be", "A", "Singular subject 'picky customer' takes 'is'."),
        ("The people ___ waiting in line.", "are", "is", "am", "be", "A", "Plural subject 'people' takes 'are'."),
        ("George Crum and his assistant ___ working in the kitchen.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ sure that potato chips are popular everywhere.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The new snack ___ crispy and salty.", "is", "are", "am", "be", "A", "Singular 'snack' takes 'is'."),
        ("The slices of potato ___ very thin.", "are", "is", "am", "be", "A", "Plural subject 'slices' takes 'are'."),
        ("The kitchen ___ hot and busy.", "is", "are", "am", "be", "A", "Singular 'kitchen' takes 'is'."),
        ("You ___ reading Chapter 05.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The customer ___ praising the dish.", "is", "are", "am", "be", "A", "Singular 'customer' takes 'is'."),
        ("The chips ___ seasoned with extra salt.", "are", "is", "am", "be", "A", "Plural 'chips' takes 'are'."),
        ("I ___ glad Crum tried a new method.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("George Crum ___ slicing potatoes.", "is", "are", "am", "be", "A", "Singular 'George Crum' takes 'is'."),
        ("The waiters ___ carrying trays of chips.", "are", "is", "am", "be", "A", "Plural 'waiters' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH05_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'George Crum and the restaurant staff ____ preparing meals for the guests.'", "are", "is", "am", "be", "A", "Compound subject ('chef and staff') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "George Crum is frying the thin potato slices.", "George Crum are frying the thin potato slices.", "George Crum am frying the thin potato slices.", "George Crum be frying the thin potato slices.", "A", "Singular noun 'George Crum' requires 'is'."),
        ("Fill in the blanks: 'I ____ eating potato chips, and my friends ____ eating French fries.'", "am, are", "is, are", "are, is", "am, is", "A", "'I am', 'friends are'."),
        ("Identify the mistake in: 'The slices of potato **is** frying in hot oil.'", "'is' should be 'are' because 'slices' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'slices' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you interested in trying this new crispy snack?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither salt nor oil ____ wasted in the kitchen.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject takes 'is'."),
        ("Select the correct sentence for story moral:", "Frustration and challenge are opportunities for innovation.", "Frustration and challenge is opportunities for innovation.", "Frustration and challenge am opportunities for innovation.", "Frustration and challenge be opportunities for innovation.", "A", "Compound subject 'Frustration and challenge' takes 'are'."),
        ("Complete the conversation: Chef: 'Where ____ the thin slices?' Assistant: 'They ____ in the deep fryer!'", "are, are", "is, is", "is, are", "are, is", "A", "Plural 'thin slices' -> are; plural 'They' -> are."),
        ("Identify where 'is' is used incorrectly:", "The chips **is** salty.", "The chef is busy.", "The customer is picky.", "The lodge is famous.", "A", "'The chips is' should be 'The chips are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The crowd of customers ____ waiting outside.'", "is", "are", "am", "be", "A", "Collective noun 'crowd' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The picky customer ____ not easy to please.'", "is", "are", "am", "be", "A", "Singular 'customer' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am ordering a plate of potato chips.", "I is ordering a plate of potato chips.", "I are ordering a plate of potato chips.", "I be ordering a plate of potato chips.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many customers queuing outside.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many customers'."),
        ("Fill in the blank: 'There ____ a delicious smell coming from the kitchen.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a delicious smell'."),
        ("Choose the correct sentence:", "What are the customers asking for today?", "What is the customers asking for today?", "What am the customers asking for today?", "What be the customers asking for today?", "A", "Plural subject 'the customers' takes 'are'."),
        ("Identify the correct form: 'The chef, as well as his assistants, ____ proud of the new dish.'", "is", "are", "am", "be", "A", "Subject is singular 'The chef' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both George Crum and the customer ____ satisfied with the result.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The original fries ____ thick, but the new chips ____ thin.'", "were / are, are", "is, is", "am, are", "is, are", "A", "'fries are', 'chips are'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH05_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the potato slices **____** fried until crispy.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'potato slices' is plural.", "am — because it refers to speaker.", "be — because slices are thin.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A batch of thin crispy potato chips **are** ready to serve.'", "'are' should be 'is' because the subject is singular noun 'batch'.", "'are' should be 'am'.", "'chips' should be 'chip'.", "No error.", "A", "'A batch' is singular, so it requires 'is ready'."),
        ("Compare: (1) 'George Crum and the waiter **are** working.' vs (2) 'George Crum, along with the waiter, **is** working.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving 'George Crum' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the restaurant **____** enjoying the chips.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The chips **is** salty, I **is** full, and the chef **are** talented.'", "'chips is' -> 'chips are'; 'I is' -> 'I am'; 'chef are' -> 'chef is'", "'chips is' -> 'chips am'; 'I is' -> 'I are'; 'chef are' -> 'chef am'", "Only 'I is' is wrong.", "No errors present.", "A", "chips are (plural), I am (1st person), chef is (3rd person singular)."),
        ("Fill in the blanks in this complex sentence: 'Not only the chef but also the waiters **____** busy, while the customer **____** smiling.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer subject ('waiters' -> are); 'customer' -> is."),
        ("Transform to negative: 'The potato chips and salt are on the table.'", "The potato chips and salt **are not** on the table.", "The potato chips and salt is not on the table.", "The potato chips and salt am not on the table.", "The potato chips and salt not on table.", "A", "Add 'not' after plural helping verb 'are'."),
        ("Analyze inverted subject position: 'In the busy kitchen **____** standing chef George Crum.'", "is", "are", "am", "be", "A", "Subject is singular 'chef George Crum', appearing after verb, requiring 'is'."),
        ("Determine agreement with uncountable nouns: 'The salt used for seasoning **____** fine and white.'", "is", "are", "am", "be", "A", "Uncountable mass noun 'salt' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the paper-thin chips you asked for.'", "Here **are** the paper-thin chips you asked for.", "Here am the paper-thin chips you asked for.", "Here be the paper-thin chips you asked for.", "No error.", "A", "Plural subject 'paper-thin chips' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "George Crum **is** an innovative chef.", "George Crum **is** slicing the potatoes.", "George Crum **is** frying the chips.", "George Crum **is** serving the guests.", "A", "In 'George Crum is an innovative chef', 'is' is the main linking verb connecting subject to predicate noun."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because Crum commanded it.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither Crum nor his assistants **____** throwing away the chips, because the dish **____** popular.'", "are, is", "is, are", "is, is", "are, are", "A", "'assistants' is closer plural subject -> are; 'dish' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "The chef is talented, I am hungry, and the chips are salty.", "The chef are talented, I is hungry, and the chips is salty.", "The chef am talented, I are hungry, and the chips am salty.", "The chef is talented, I is hungry, and the chips is salty.", "A", "chef is (singular), I am (1st person), chips are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH05_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 05
# ---------------------------------------------------------------------------
def rebuild_chapter_05():
    print("Rebuilding Chapter 05 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

    files_and_generators = [
        ("plural_nouns_spelling.md", build_plural_nouns),
        ("articles_grammar.md", build_articles_grammar),
        ("calendar_days_vocabulary.md", build_calendar_days),
        ("action_verbs_identification.md", build_action_verbs),
        ("punctuation_marks.md", build_punctuation_marks),
        ("phonics_vowel_digraphs.md", build_phonics_digraphs),
        ("question_words_interrogatives.md", build_question_words),
        ("present_continuous_ing.md", build_present_continuous),
        ("helping_verbs_is_am_are.md", build_helping_verbs)
    ]

    for fname, gen_func in files_and_generators:
        filepath = os.path.join(CH05_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 05 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_05()
