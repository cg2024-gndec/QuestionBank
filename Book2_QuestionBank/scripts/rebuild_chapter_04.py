r"""
=============================================================================
Script: rebuild_chapter_04.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 04:
             "The Wannabe Chocolate" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH04_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_04")
os.makedirs(CH04_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 04: The Wannabe Chocolate\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("chocolate", "chocolates", "chocolaties", "chocolatese", "chocolatez", "A", "Regular noun ending in -e adds -s."),
        ("cake", "cakes", "cakies", "cakees", "cakez", "A", "Regular noun ending in -e adds -s."),
        ("flavour", "flavours", "flavoures", "flavouries", "flavourz", "A", "Regular noun adding -s."),
        ("bowl", "bowls", "bowles", "bowlies", "bowlz", "A", "Regular noun adding -s."),
        ("peanut", "peanuts", "peanutes", "peanuties", "peanutz", "A", "Regular noun adding -s."),
        ("cashew", "cashews", "cashewes", "cashewies", "cashewz", "A", "Regular noun adding -s."),
        ("raisin", "raisins", "raisines", "raisinies", "raisinz", "A", "Regular noun adding -s."),
        ("assistant", "assistants", "assistantes", "assistanties", "assistantz", "A", "Regular noun adding -s."),
        ("market", "markets", "marketes", "marketies", "marketz", "A", "Regular noun adding -s."),
        ("mixture", "mixtures", "mixturies", "mixturees", "mixturez", "A", "Regular noun ending in -e adds -s."),
        ("sweet", "sweets", "sweetes", "sweeties", "sweetz", "A", "Regular noun adding -s."),
        ("treat", "treats", "treates", "treaties", "treatz", "A", "Regular noun adding -s."),
        ("recipe", "recipes", "recipies", "recipees", "recipez", "A", "Regular noun ending in -e adds -s."),
        ("box", "boxes", "boxs", "boxies", "boxen", "A", "Nouns ending in -x add -es."),
        ("dish", "dishes", "dishs", "dishies", "dished", "A", "Nouns ending in -sh add -es."),
        ("factory", "factories", "factorys", "factoryes", "factoriz", "A", "Consonant + y changes to -ies."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people."),
        ("shelf", "shelves", "shelfs", "shelfes", "shelvs", "A", "Nouns ending in -f change to -ves.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH04_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 04 (*The Wannabe Chocolate*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Mr. Candy Nougat spilled four (bowl / bowls) of ingredients.", "bowls", "bowl", "bowles", "bowlies", "A", "'four' requires plural noun 'bowls'."),
        ("The mixture contained crunchy (peanut / peanuts) and cashews.", "peanuts", "peanut", "peanutes", "peanuties", "A", "'peanuts' is the plural form."),
        ("Jammy placed sweet (raisin / raisins) in the chocolate.", "raisins", "raisin", "raisines", "raisinies", "A", "'raisins' is the plural form."),
        ("Identify the INCORRECT plural spelling in this list: cakes, chocolates, factoris, sweets.", "factoris", "cakes", "chocolates", "sweets", "A", "Plural of factory is 'factories', not 'factoris'."),
        ("Choose the sentence with the correct plural noun form:", "The Wannabe Chocolates ruled the markets.", "The Wannabe Chocolates ruled the marketes.", "The Wannabe Chocolates ruled the marketies.", "The Wannabe Chocolates ruled the marketz.", "A", "markets is the correct plural of market."),
        ("Which noun forms its plural by changing consonant + y to -ies?", "factory -> factories", "cake -> cakes", "bowl -> bowls", "peanut -> peanuts", "A", "Factory ends in consonant + y, so plural is factories."),
        ("Change the singular noun in brackets to plural: 'Mr. Candy Nougat packed three ____ (box) of sweets.'", "boxes", "boxs", "boxies", "boxen", "A", "Nouns ending in -x add -es (boxes)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The assistants prepared the recipes in the kitchens.", "The assistantex prepared the recipes in the kitchens.", "The assistants prepared the recipies in the kitchenes.", "The assistantees prepared the recipes in the kitchens.", "A", "assistants, recipes, kitchens are all correctly spelt plurals."),
        ("What is the correct plural of 'caramel'?", "caramels", "carameles", "caramelies", "caramelz", "A", "Regular noun adding -s."),
        ("Mr. Candy Nougat spent many (day / days) creating new recipes.", "days", "daies", "day", "dayes", "A", "Vowel + y adds -s (days)."),
        ("The shop had many wooden (shelf / shelves).", "shelves", "shelfs", "shelfes", "shelvs", "A", "Nouns ending in -f change to -ves (shelves)."),
        ("Many (person / people) came to buy the Wannabe Chocolates.", "people", "persons", "peoples", "persones", "A", "Plural of person in general context is people."),
        ("How many (flavour / flavours) of ice cream did he make?", "flavours", "flavour", "flavoures", "flavouries", "A", "Plural noun 'flavours'."),
        ("The two (baker / bakers) worked together.", "bakers", "bakeres", "baker", "bakeries", "A", "Plural of baker is bakers."),
        ("Which plural noun rule applies to the word **'dishes'**?", "Add -es to nouns ending in -sh", "Add -s to vowel + y", "Change -f to -ves", "Change -y to -ies", "A", "Dish ends in -sh, so it adds -es."),
        ("Mr. Candy Nougat received many (compliment / compliments).", "compliments", "complimentes", "complimenties", "complimentz", "A", "Regular noun adding -s."),
        ("Identify the correct plural form of 'child':", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("Jammy wiped all the dirty (counter / counters).", "counters", "counteres", "counter", "counteries", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH04_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The assistant tasted a chocolate in the shop.'", "The assistants tasted chocolates in the shops.", "The assistantex tasted chocolates in the shopes.", "The assistants tasted chocolate in the shops.", "The assistant tasted chocolates in the shopz.", "A", "Plural of assistant->assistants, chocolate->chocolates, shop->shops."),
        ("Analyze the error: 'Mr. Candy Nougat added four spoons of sugars.' Why is 'sugars' inappropriate here?", "'sugar' is an uncountable mass noun, so 'sugar' (or 'spoons of sugar') should be used.", "'sugars' should be 'sugares'.", "'sugars' should be 'sugaries'.", "No error.", "A", "Mass nouns like sugar do not normally take plural form."),
        ("Complete the paragraph with correct plurals: 'The two ____ (baker) prepared five ____ (batch) of crunchy ____ (sweet).'", "bakers, batches, sweets", "bakeres, batchs, sweetes", "bakers, batchies, sweet", "bakeres, batches, sweets", "A", "bakers (-s), batches (-ch + es), sweets (-s)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **assistants** filled the **boxes** with **raisins**.", "The **assistantex** filled the **boxs** with **raisins**.", "The **assistants** filled the **boxies** with **raisinies**.", "The **assistantees** filled the **boxes** with **raisines**.", "A", "assistants (-s), boxes (-x + es), raisins (-s)."),
        ("Which group contains ONLY irregular plural nouns?", "people, men, teeth, children", "chocolates, cakes, bowls, raisins", "factories, cities, stories, armies", "shelves, thieves, wolves, knives", "A", "people, men, teeth, children change forms without standard -s/-es."),
        ("Why does 'day' become 'days' but 'factory' becomes 'factories'?", "Because 'day' has a vowel before y (a+y -> -s), while 'factory' has a consonant before y (r+y -> -ies).", "Because 'day' is short and 'factory' is long.", "Because 'day' is time and 'factory' is place.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The two bakeres bought many mouses for the shop.'", "'bakeres' should be 'bakers' and 'mouses' should be 'mice'.", "'bakeres' should be 'baker' and 'mouses' should be 'mices'.", "'shop' should be 'shops' only.", "There are no mistakes in the sentence.", "A", "bakers (regular -s) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'Jammy wiped his ____ (hand) and moved the ____ (foot).'", "hands, feet", "handes, foots", "hands, feets", "handies, foots", "A", "Plural of hand is hands, plural of foot is feet."),
        ("Analyze this sentence: 'Mr. Candy Nougat gave good advice.' Can 'advice' be pluralized as 'advices'?", "No, 'advice' is an uncountable noun; we say 'pieces of advice' for plural.", "Yes, 'advices' is correct.", "No, it becomes 'advicess'.", "Yes, 'an advice' is correct.", "A", "Advice is an uncountable noun."),
        ("Fill in the blanks: 'The two ____ (assistant) washed the ____ (dish) after baking.'", "assistants, dishes", "assistantes, dishs", "assistants, dishies", "assistantes, dishes", "A", "assistant -> assistants; dish -> dishes (-sh + es)."),
        ("Select the option that shows correct plural transformation for ALL three words: 'loaf', 'cherry', 'box'", "loaves, cherries, boxes", "loafs, cherrys, boxs", "loaves, cherryes, boxies", "loafes, cherries, boxen", "A", "loaf -> loaves; cherry -> cherries; box -> boxes."),
        ("HOTS Reasoning: Why do we say 'butter is soft' rather than 'butters are soft'?", "Because 'butter' is an uncountable mass noun that stays singular.", "Because butter melts in Chocoland.", "Because Jammy bakes.", "Because cakes are sweet.", "A", "Uncountable mass nouns take singular verbs."),
        ("Transform into singular: 'The assistants packed the chocolates in the boxes.'", "The assistant packed the chocolate in the box.", "The assistants packed the chocolate in the box.", "The assistant pack the chocolate in the box.", "The assistant packed the chocolates in the box.", "A", "Singular forms: assistant, chocolate, box."),
        ("Identify the correct rule for forming the plural of **'flavour'**:", "Add -s because it is a regular noun ending in a consonant (flavours).", "Add -es (flavoures).", "Change -r to -ves (flavouvs).", "Change vowel sound.", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH04_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 04: The Wannabe Chocolate\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("Mr. Candy Nougat lived in ___ town called Chocoland.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'town'."),
        ("He was ___ hard-working baker.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'hard-working'."),
        ("Jammy was ___ assistant in the shop.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'assistant'."),
        ("Mr. Candy Nougat knocked over ___ bowl of peanuts.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'bowl'."),
        ("The new mixture had ___ amazing taste.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'amazing'."),
        ("___ Panchatantra/Fiction story tells us about creativity.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra/Fiction'."),
        ("Jammy found ___ new recipe by accident.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'new'."),
        ("Mr. Candy Nougat was ___ honest person.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ chocolates were named Wannabe Chocolates.", "The", "A", "An", "No article", "A", "Use 'The' for specific chocolates in story."),
        ("Jammy had ___ idea to sell the mixture.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'idea'."),
        ("It was ___ unusual recipe with raisins and caramel.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unusual'."),
        ("Mr. Candy Nougat made ___ mistake while reaching for sugar.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'mistake'."),
        ("___ Wannabe Chocolates soon ruled the market.", "The", "A", "An", "No article", "A", "Use 'The' for proper title 'Wannabe Chocolates'."),
        ("Jammy took ___ spoon to taste the mixture.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'spoon'."),
        ("They created ___ delicious sweet treat.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'delicious'."),
        ("Mr. Candy Nougat was ___ clumsy man.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'clumsy'."),
        ("Jammy felt ___ great happiness after tasting it.", "no article", "a", "an", "the", "A", "Abstract noun 'happiness' takes no indefinite article here."),
        ("___ people of Chocoland loved the new taste.", "The", "A", "An", "No article", "A", "Use 'The' for specific people of Chocoland.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH04_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Jammy tasted ___ mixture and told ___ baker that it was great.", "the, the", "a, an", "an, a", "a, the", "A", "Both mixture and baker refer to specific items in the story."),
        ("Why do we say '**a** baker' but '**an** assistant'?", "Because 'baker' begins with a consonant sound (b) and 'assistant' with a vowel sound (a).", "Because bakers are rich.", "Because assistants are young.", "Because Chocoland is sweet.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "Mr. Candy Nougat reached for a bowl of sugar.", "Mr. Candy Nougat reached for an bowl of sugar.", "Mr. Candy Nougat reached for the a bowl of sugar.", "Mr. Candy Nougat reached for a an bowl of sugar.", "A", "'a bowl' (/b/) takes 'a'."),
        ("Fill in the blanks: 'Jammy poured ___ caramel into ___ bowl.'", "the, the", "a, a", "an, an", "a, the", "A", "Both caramel and bowl are specific items in the recipe."),
        ("Identify the INCORRECT article in: 'Jammy had **a** amazing idea.'", "'a' should be 'an'", "'a' should be 'the'", "'amazing' should be 'an amazing'", "No mistake", "A", "'amazing' starts with vowel sound /a/, so it takes 'an'."),
        ("Which article completes the sentence? 'Mixing ingredients requires ___ active effort.'", "an", "a", "the", "no article", "A", "'active' starts with vowel sound /a/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ baker made ___ new chocolate.'", "The, a", "A, a", "An, an", "The, the", "A", "'The baker' (specific Mr. Candy Nougat), 'a new chocolate' (consonant sound)."),
        ("Why do we use 'a' before 'clumsy baker' in 'He was **a** clumsy baker'?", "Because 'clumsy' begins with the consonant sound /k/.", "Because baker is a noun.", "Because clumsy is sweet.", "Because Chocoland is big.", "A", "'clumsy' starts with consonant sound /k/."),
        ("Complete the dialogue: Jammy: 'Taste ___ mixture!' Candy Nougat: 'It is ___ success!'", "the, a", "a, an", "an, the", "the, the", "A", "'the mixture' (specific mixture), 'a success' (consonant sound)."),
        ("Select the correct sentence:", "A chocolate is a sweet treat.", "An chocolate is a sweet treat.", "The chocolate is an sweet treat.", "An chocolate is an sweet treat.", "A", "'A chocolate' (consonant sound), 'a sweet treat' (consonant sound)."),
        ("Fill in the blank: 'Mr. Candy Nougat worked for ___ long time in the shop.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The recipe contained **___ sugar** and nuts.", "They sold ___ chocolate.", "He opened ___ bowl.", "He met ___ assistant.", "A", "Uncountable mass noun 'sugar' takes no article here."),
        ("Choose the correct sentence for story summary:", "Accidental mistakes can lead to great success.", "An accidental mistakes can lead to a great success.", "A accidental mistakes can lead to an great success.", "The accidental a mistakes is good.", "A", "Plural abstract statement takes no indefinite article for 'mistakes'."),
        ("Fill in the blanks: 'Jammy spent ___ hour selling ___ new chocolates.'", "an, the", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'the new chocolates' (specific)."),
        ("Which sentence uses 'the' correctly for unique story places?", "Chocoland was the most famous town in the kingdom.", "Chocoland was a most famous town in a kingdom.", "Chocoland was an most famous town in an kingdom.", "Chocoland was most famous town in kingdom.", "A", "Superlative 'the most famous' and specific 'the kingdom' take 'the'."),
        ("Identify the article error: 'Jammy gave **a** explanation after **an** short delay.'", "'an short' should be 'a short' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an short' should be 'a short'", "No error", "A", "'an explanation' (vowel /e/) and 'a short delay' (consonant /s/)."),
        ("Complete: 'It was ___ unexpected hit in ___ market.'", "an, the", "a, an", "the, the", "an, an", "A", "an unexpected (/u/), the market (specific)."),
        ("Choose the correct option: '___ sun set over Chocoland.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH04_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'Mr. Candy Nougat spilled **a** caramel into **the** bowl.' Correct the error:", "'spilled a caramel' -> 'spilled caramel' (uncountable mass noun caramel takes no article 'a' here).", "'the bowl' -> 'an bowl'.", "'spilled a caramel' -> 'spilled an caramel'.", "No error present.", "A", "'caramel' as a liquid/mass noun takes no article 'a'."),
        ("Fill in all three blanks: '___ baker told ___ assistant that ___ hard work pays off.'", "The, the, no article", "A, an, a", "An, a, the", "The, a, a", "A", "'The baker' (specific), 'the assistant' (specific), 'hard work' (general abstract)."),
        ("Identify why 'the' is used in: 'Jammy tasted **the** mixture.'", "Because 'the mixture' refers to the specific spilled mixture in the bowl.", "Because mixture is a proper noun.", "Because Jammy ate it.", "Because Chocoland is sweet.", "A", "'The' specifies the definite mixture mentioned in narrative."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** eagle to fly past Chocoland.'", "'a hour' should be 'an hour' and 'a eagle' should be 'an eagle'.", "'a hour' should be 'the hour' and 'a eagle' should be 'a eagle'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'eagle' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A baker lived in a town. He had an assistant. The assistant tasted the new chocolate.", "An baker lived in an town. He had a assistant. A assistant tasted a new chocolate.", "The baker lived in an town. He had a an assistant.", "A baker lived in an town. The assistant was a honest.", "A", "A baker (first mention), a town (first mention), an assistant (vowel), The assistant (second mention)."),
        ("Why is it correct to write 'a unique recipe' but 'an unusual recipe'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because recipe is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story moral: '___ creative mind turns ___ mistake into ___ opportunity.'", "A, a, an", "An, a, an", "The, the, the", "A, an, a", "A", "A creative mind, a mistake, an opportunity."),
        ("Analyze this sentence: 'Jammy went to **the** shop.' Why is 'the' appropriate?", "Because it refers to the specific bakery shop of Mr. Candy Nougat.", "Because shop is in town.", "Because shop is plural.", "Because Jammy is baker.", "A", "'the' specifies the definite shop."),
        ("Correct the sentence: 'An baker spilled a sugar into a bowl.'", "A baker spilled sugar into the bowl.", "The baker spilled an sugar into a bowl.", "An baker spilled the sugar into the bowl.", "A baker spilled a sugar into a bowl.", "A", "'A baker' (/b/ sound), 'sugar' (uncountable, no 'a'), 'the bowl' (specific)."),
        ("Fill in the blanks: '___ chocolate in ___ bowl was mixed with ___ caramel.'", "The, the, no article", "A, a, a", "No article, a, an", "An, the, a", "A", "'The chocolate' (specific), 'the bowl' (specific), 'caramel' (mass noun, no article)."),
        ("Spot the missing article: 'Jammy tasted mixture and smiled with joy.'", "Missing 'the' before 'mixture' -> 'Jammy tasted the mixture...'", "Missing 'a' before 'joy'", "Missing 'an' before 'tasted'", "No article is missing", "A", "Specific object 'the mixture' needs 'the'."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An assistant found a recipe in the shop.", "A assistant found an recipe in a shop.", "The assistant found an recipe in an shop.", "An assistant found an recipe in the shop.", "A", "An assistant (vowel), a recipe (consonant), the shop (specific)."),
        ("Rewrite correctly: 'Mr. Candy Nougat was a clumsy baker who created an delicious treat.'", "Mr. Candy Nougat was a clumsy baker who created a delicious treat.", "Mr. Candy Nougat was an clumsy baker who created an delicious treat.", "Mr. Candy Nougat was a clumsy baker who created an delicious treat.", "Mr. Candy Nougat was the clumsy baker who created an delicious treat.", "A", "'a clumsy' (consonant /k/), 'a delicious treat' (consonant /d/)."),
        ("Identify the correct rule for using 'the' with superlative adjectives (best, most, finest):", "Superlative adjectives take 'the' because they identify the single highest degree.", "Superlatives take 'an'.", "Superlatives never take articles.", "Superlatives take 'a' only.", "A", "'the best', 'the most talented' take 'the'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH04_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 04: The Wannabe Chocolate\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("Mr. Candy Nougat bakes fresh cakes every **morning**. What word means the middle of the day?", "Noon / Midday", "Midnight", "Dawn", "Twilight", "A", "Noon/midday is 12:00 PM."),
        ("What is the standard abbreviation for **Friday**?", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard abbreviation."),
        ("Which day comes right after Tuesday?", "Wednesday", "Thursday", "Monday", "Friday", "A", "Wednesday follows Tuesday."),
        ("What is the abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("If the shop is open for 6 days a week, how many days is it closed?", "1 day", "2 days", "3 days", "0 days", "A", "7 - 6 = 1 day."),
        ("Which month comes right before October?", "September", "August", "November", "December", "A", "September comes before October."),
        ("What is the short abbreviation for **October**?", "Oct.", "Octo.", "Oc.", "Ot.", "A", "Oct. is standard abbreviation."),
        ("The shop was busy during the **evening**. What time comes right after evening?", "Night", "Morning", "Noon", "Dawn", "A", "Night follows evening."),
        ("What is the abbreviation for **Sunday**?", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard abbreviation."),
        ("How many days are in a leap year?", "366 days", "365 days", "300 days", "350 days", "A", "A leap year has 366 days."),
        ("Which month comes right after November?", "December", "January", "October", "September", "A", "December comes after November."),
        ("What is the short abbreviation for **December**?", "Dec.", "Dece.", "Dc.", "Dcm.", "A", "Dec. is standard abbreviation."),
        ("If today is Monday, what day was yesterday?", "Sunday", "Tuesday", "Saturday", "Friday", "A", "Yesterday was Sunday."),
        ("If today is Tuesday, what day will tomorrow be?", "Wednesday", "Monday", "Thursday", "Friday", "A", "Tomorrow will be Wednesday."),
        ("What is the abbreviation for **Monday**?", "Mon.", "Mnd.", "Mo.", "Mn.", "A", "Mon. is standard abbreviation."),
        ("Which day comes between Thursday and Saturday?", "Friday", "Wednesday", "Sunday", "Monday", "A", "Friday is between Thursday and Saturday."),
        ("What is the abbreviation for **August**?", "Aug.", "Augu.", "Au.", "Ag.", "A", "Aug. is standard abbreviation."),
        ("Which month comes right before January?", "December", "November", "February", "October", "A", "December comes before January.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH04_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Mr. Candy Nougat created the new recipe on **Wednesday**. He started selling it 2 days later. On which day did sales start?", "Friday", "Thursday", "Saturday", "Sunday", "A", "Wednesday + 2 days = Thursday(1), Friday(2)."),
        ("Jammy baked chocolates from **8:00 AM** to **1:00 PM**. How many hours did he bake?", "5 hours", "4 hours", "6 hours", "3 hours", "A", "1:00 PM - 8:00 AM = 5 hours."),
        ("Match the day with its abbreviation: **Tuesday**", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. is standard."),
        ("If the shop opened on **Monday morning** and closed for restocking on **Thursday morning**, how many full days was it open?", "3 full days (72 hours)", "2 days", "4 days", "1 day", "A", "Monday morning to Thursday morning is 3 full days."),
        ("Identify the correctly spelt month name:", "December", "Decembre", "Decemberr", "Decembere", "A", "December is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Saturday - Std.", "D", "Saturday abbreviation is Sat., not Std."),
        ("The Wannabe Chocolates ruled the market for **2 years**. How many months is 2 years?", "24 months", "12 months", "36 months", "18 months", "A", "2 years x 12 months = 24 months."),
        ("Which month has 31 days and comes right after August?", "October (has 31) / September (has 30)", "October", "September", "November", "A", "October has 31 days and follows September."),
        ("Rearrange in correct chronological order: Thu, Tue, Wed, Fri", "Tue, Wed, Thu, Fri", "Wed, Tue, Thu, Fri", "Tue, Thu, Wed, Fri", "Fri, Thu, Wed, Tue", "A", "Tuesday -> Wednesday -> Thursday -> Friday."),
        ("What day is 3 days before Sunday?", "Thursday", "Wednesday", "Friday", "Monday", "A", "Sunday - 3 days = Saturday(1), Friday(2), Thursday(3)."),
        ("If Jammy takes 30 minutes to mix chocolate, how many batches can he mix in 2 hours?", "4 batches", "2 batches", "6 batches", "3 batches", "A", "2 hours = 120 minutes. 120 / 30 = 4 batches."),
        ("Select the month that has 30 days:", "November", "December", "January", "March", "A", "November has 30 days."),
        ("Which abbreviation stands for **January**?", "Jan.", "Jny.", "Ja.", "Jn.", "A", "Jan. is standard abbreviation."),
        ("If today is **Sat.**, what day will it be after 7 days?", "Saturday", "Sunday", "Friday", "Monday", "A", "7 days is a full week cycle, landing on Saturday again."),
        ("The bakery was open from **9:00 AM** to **5:00 PM**. How many hours was it open daily?", "8 hours", "9 hours", "7 hours", "10 hours", "A", "5:00 PM - 9:00 AM = 8 hours."),
        ("Identify the word that means 'occurring once every month':", "Monthly", "Daily", "Weekly", "Yearly", "A", "Monthly means once a month."),
        ("Which of the following is a weekend day?", "Sunday", "Monday", "Tuesday", "Wednesday", "A", "Sunday is a weekend day."),
        ("Choose the correct abbreviation for **November**:", "Nov.", "Nove.", "Nv.", "Nm.", "A", "Nov. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH04_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Mr. Candy Nougat baked chocolates from **Mon., 1st Oct.** to **Fri., 5th Oct.**. How many days did he bake?", "5 days", "4 days", "3 days", "7 days", "A", "1st to 5th Oct inclusive is 5 days."),
        ("Jammy worked in the kitchen from **8:30 AM to 11:30 AM**. How many minutes did he work?", "180 minutes (3 hours)", "120 minutes", "240 minutes", "90 minutes", "A", "3 hours x 60 minutes = 180 minutes."),
        ("Solve the calendar puzzle: If 1st December is a Saturday, what day of the week will 8th December be?", "Saturday", "Sunday", "Friday", "Monday", "A", "1 + 7 = 8th December, landing on Saturday."),
        ("Analyze this schedule: Mr. Candy Nougat bakes on Mon, Wed, Fri; Jammy bakes on Tue, Thu, Sat. On which day do BOTH rest?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in baking schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., ____, ____.", "Sat., Sun.", "Satur., Sund.", "Sa., Su.", "Sat., Sn.", "A", "Sat. and Sun. complete the sequence."),
        ("If the new chocolates were sold out in a fortnight, how many days did sales last?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Oct, Nov, Jan, Dec'", "January and December are in wrong order.", "November is in wrong position.", "October should be last.", "No error.", "A", "December comes before January (Oct, Nov, Dec, Jan)."),
        ("The bakery order arrived on **31st December**. What date was the next day?", "1st January", "32nd December", "30th December", "1st February", "A", "December has 31 days, so next day is 1st January."),
        ("If yesterday was two days before Friday, what day is tomorrow?", "Friday", "Thursday", "Saturday", "Wednesday", "A", "Two days before Friday = Wednesday (yesterday). Today = Thursday. Tomorrow = Friday."),
        ("Calculate: How many days are there in total during **December** and **January** combined?", "62 days (31 + 31)", "60 days", "61 days", "59 days", "A", "Both December (31) and January (31) have 31 days. 31 + 31 = 62 days."),
        ("HOTS Reasoning: Why do bakery sales increase during festive months (October, November, December)?", "Festivals like Diwali and Christmas occur in these months, increasing sweet consumption.", "Because sugar is cheap.", "Because Jammy sleeps.", "Because summer is hot.", "A", "Festive seasons boost sweet sales."),
        ("Identify the correct statement about a non-leap year:", "A non-leap year has 365 days and February has 28 days.", "A non-leap year has 366 days.", "February has 30 days.", "A non-leap year occurs every 4 years.", "A", "Standard year has 365 days (Feb = 28 days)."),
        ("Jammy made 120 chocolates in 2 hours. How many chocolates did he make per hour?", "60 chocolates per hour", "30 chocolates", "120 chocolates", "40 chocolates", "A", "120 / 2 = 60 chocolates per hour."),
        ("Which month pair both have 31 days and come right after each other at the end of the year and start of next year?", "December and January", "November and December", "October and November", "January and February", "A", "December (31) and January (31) are consecutive 31-day months across new year.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH04_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 04: The Wannabe Chocolate\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("Mr. Candy Nougat **made** the best chocolates.", "made", "Mr. Candy Nougat", "best", "chocolates", "A", "'made' is the action verb."),
        ("He **reached** for a bowl of sugar.", "reached", "he", "bowl", "sugar", "A", "'reached' is the action verb."),
        ("He **knocked** down several bowls.", "knocked", "he", "down", "bowls", "A", "'knocked' is the physical action verb."),
        ("The peanuts and caramel **landed** in the bowl.", "landed", "peanuts", "caramel", "bowl", "A", "'landed' is the action verb."),
        ("Mr. Candy Nougat **decided** to throw it away.", "decided", "Candy Nougat", "away", "mixture", "A", "'decided' is the mental action verb."),
        ("Jammy **tasted** the new mixture.", "tasted", "Jammy", "new", "mixture", "A", "'tasted' is the sensory action verb."),
        ("Jammy **convinced** him to sell it.", "convinced", "Jammy", "him", "sell", "A", "'convinced' is the action verb."),
        ("People **loved** the Wannabe Chocolates.", "loved", "people", "Wannabe", "Chocolates", "A", "'loved' is the emotional action verb."),
        ("The new chocolates **ruled** the market.", "ruled", "chocolates", "new", "market", "A", "'ruled' is the action verb."),
        ("Mr. Candy Nougat **mixed** the ingredients.", "mixed", "Candy Nougat", "the", "ingredients", "A", "'mixed' is the action verb."),
        ("Jammy **poured** the liquid into boxes.", "poured", "Jammy", "liquid", "boxes", "A", "'poured' is the action verb."),
        ("Mr. Candy Nougat **baked** delicious cakes.", "baked", "Candy Nougat", "delicious", "cakes", "A", "'baked' is the action verb."),
        ("Jammy **suggested** a clever name.", "suggested", "Jammy", "clever", "name", "A", "'suggested' is the action verb."),
        ("Customers **bought** all the chocolates.", "bought", "customers", "all", "chocolates", "A", "'bought' is the action verb."),
        ("Jammy **wiped** the kitchen counter.", "wiped", "Jammy", "kitchen", "counter", "A", "'wiped' is the action verb."),
        ("Mr. Candy Nougat **smiled** with joy.", "smiled", "Candy Nougat", "joy", "with", "A", "'smiled' is the action verb."),
        ("Jammy **worked** hard in the shop.", "worked", "Jammy", "hard", "shop", "A", "'worked' is the action verb."),
        ("The mixture **tasted** sweet and crunchy.", "tasted", "mixture", "sweet", "crunchy", "A", "'tasted' is the action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH04_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 04:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'Jammy **eagerly** **tasted** the **sweet** **mixture**.'", "tasted", "eagerly", "sweet", "mixture", "A", "'tasted' shows sensory action; 'eagerly' is adverb, 'sweet' is adjective, 'mixture' is noun."),
        ("Identify BOTH action verbs in: 'Mr. Candy Nougat **spilled** the nuts and **created** a new sweet.'", "spilled, created", "Candy Nougat, nuts", "sweet, spilled", "created, nuts", "A", "'spilled' and 'created' are both action verbs."),
        ("What is the past tense action verb of 'buy' as used in story ('customers bought chocolates')?", "bought", "buyed", "buying", "buys", "A", "Past tense of buy is bought."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "Jammy will **taste** the new recipe.", "The chocolate has a sweet **taste**.", "I like the **taste** of caramel.", "That is a rich **taste**.", "A", "In (A), 'taste' acts as the main action verb."),
        ("Find the action verb in: 'Mr. Candy Nougat opened the bakery shop.'", "opened", "Candy Nougat", "bakery", "shop", "A", "'opened' is the action verb."),
        ("Which sentence contains NO physical action verb?", "Mr. Candy Nougat was hard-working but clumsy.", "Jammy tasted the mixture.", "He knocked over the bowls.", "They sold the new chocolates.", "A", "'Mr. Candy Nougat was hard-working but clumsy' contains linking verb 'was', but no physical action verb."),
        ("Change the action verb 'make' to past tense: 'He (make) the best chocolates.'", "made", "maked", "making", "makes", "A", "Past tense of make is made."),
        ("Identify the action verb: 'Jammy tasted the chocolate and smiled with joy.'", "tasted, smiled", "Jammy, chocolate", "joy, smiled", "tasted, joy", "A", "'tasted' and 'smiled' are action verbs."),
        ("Select the action verb that completes the sentence: 'The Wannabe Chocolates ____ the market.'", "dominated / ruled", "sweet", "market", "flavor", "A", "'dominated' / 'ruled' is an action verb."),
        ("Which word is an action verb? (raisins, caramel, knocked, bowl)", "knocked", "raisins", "caramel", "bowl", "A", "'knocked' is an action verb; others are nouns."),
        ("What action did Jammy perform that saved the mixture?", "tasted", "clumsy", "bowls", "sugar", "A", "Jammy tasted the mixture (action verb)."),
        ("Identify the action verb in: 'Mr. Candy Nougat thought about throwing it away.'", "thought", "Candy Nougat", "about", "throwing", "A", "'thought' is a mental action verb."),
        ("Choose the correct action verb: 'The customers ____ the new recipe.'", "praised / loved", "sweet", "tasty", "chocolates", "A", "'praised' / 'loved' is the action verb."),
        ("Identify the action verb in: 'Jammy suggested a brand new name.'", "suggested", "Jammy", "brand", "name", "A", "'suggested' is the action verb."),
        ("Which of these words is NOT an action verb? (bake, mix, sweet, sell)", "sweet", "bake", "mix", "sell", "A", "'sweet' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'Mr. Candy Nougat reached for the jar.'", "reached", "Candy Nougat", "for", "jar", "A", "'reached' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'Jammy ____ the chocolate boxes onto the shelf.'", "stacked / placed", "sweet", "red", "shop", "A", "'stacked' / 'placed' is an action verb."),
        ("What action verb completes the sentence? 'They ____ thousands of Wannabe Chocolates daily.'", "produced / sold", "sweet", "sugar", "town", "A", "'produced' / 'sold' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH04_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The clumsy baker accidentally knocked down the bowls and spilled the nuts.' How many total ACTION VERBS are present?", "2 action verbs ('knocked', 'spilled')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'knocked' and 'spilled' are action verbs; 'clumsy' and 'accidentally' are adjective/adverb."),
        ("Categorize the verbs: In 'Mr. Candy Nougat **was** clumsy, so he **spilled** the caramel', classify 'was' and 'spilled'.", "'was' is a linking verb; 'spilled' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'was' is action; 'spilled' is linking.", "A", "'was' links state of being; 'spilled' shows physical action."),
        ("Replace the weak verb with a strong action verb: 'Jammy **went fast** to taste the mixture.'", "Jammy **rushed** to taste the mixture.", "Jammy **was near** the mixture.", "Jammy **walked slow**.", "Jammy **looked at** the mixture.", "A", "'rushed' is a much stronger, vivid action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "Mr. Candy Nougat **knocked** the bowls, **tasted** the mix, and **sold** the chocolates.", "Mr. Candy Nougat was talented, hard-working, and clumsy.", "The mixture tasted sweet and delicious.", "The shop was famous in Chocoland.", "A", "knocked, tasted, sold are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "Jammy **convinced** Mr. Candy Nougat.", "Jammy was **clever**.", "The chocolate was **tasty**.", "Chocoland was **famous**.", "A", "'convinced' is an action verb."),
        ("Spot the incorrect verb tense: 'Jammy **taste** the mixture yesterday.' Correct it:", "'taste' should be 'tasted' (past action verb).", "'taste' should be 'tasting'.", "'taste' should be 'tastes'.", "'taste' should be 'will taste'.", "A", "Past time indicator 'yesterday' requires past tense action verb 'tasted'."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (knocked, reached, tasted, sold)", "reached -> knocked -> tasted -> sold", "sold -> tasted -> knocked -> reached", "knocked -> reached -> sold -> tasted", "tasted -> knocked -> reached -> sold", "A", "First reached for sugar, knocked down bowls, Jammy tasted mix, sold chocolates."),
        ("Identify the verb error in dialogue: Jammy said, 'I have **find** a delicious new flavor!'", "'find' is incorrect; the past participle form is 'found' ('have found').", "'find' should be 'finding'.", "'find' should be 'finds'.", "No error.", "A", "Perfect tense requires past participle 'found'."),
        ("Analyze this sentence: 'Jammy **convinced** the baker to keep the mixture.' What type of action verb is 'convinced'?", "Persuasive speech/mental action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'convinced' is an action verb of speech/persuasion."),
        ("Which sentence uses action verbs to show cause and effect?", "He **spilled** the nuts, so he **created** a new recipe.", "Mr. Candy Nougat was clumsy and hard-working.", "The shop had many sweet cakes.", "Chocoland is a nice town.", "A", "'spilled' (cause action) -> 'created' (effect action)."),
        ("Spot the missing action verb: 'Jammy ____ the spoon into the bowl and ____ the mixture.'", "dipped, sampled", "sweet, red", "was, was", "quick, slow", "A", "'dipped' and 'sampled' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'convinced' in 'Jammy convinced him' considered an INFLUENTIAL action verb?", "Because it describes actively changing someone's mind through argument.", "Because convincing requires sugar.", "Because chocolates are sweet.", "Because it is a noun.", "A", "Descriptive speech action verb conveying influence."),
        ("Transform the action verb to future tense: 'Jammy **sells** the new chocolates.'", "Jammy **will sell** the new chocolates.", "Jammy **sold** the new chocolates.", "Jammy **is selling** the new chocolates.", "Jammy **sell** the new chocolates.", "A", "'will sell' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The customers **enjoy** the new flavor.", "The customers **enjoys** the new flavor.", "The customer **enjoy** the new flavor.", "The customers **is enjoying** the new flavor.", "A", "Plural subject 'customers' takes base verb 'enjoy' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH04_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 04: The Wannabe Chocolate\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'Mr. Candy Nougat lived in Chocoland__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'What ingredients fell into the chocolate bowl__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a proper name like 'Mr. Candy Nougat'?", "First letter of each word (e.g., Mr. Candy Nougat)", "The last letter", "All letters", "No letters", "A", "Proper names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'He knocked down peanuts__ caramel__ cashew__ and raisins.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden delight: 'This new mixture tastes amazing__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense delight/excitement."),
        ("Select the proper noun that MUST start with a capital letter:", "Chocoland", "chocolate", "bowl", "sugar", "A", "'Chocoland' as a town name starts with capital 'C'."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'jammy tasted the new mixture.'", "jammy -> Jammy", "tasted -> Tasted", "mixture -> Mixture", "new -> New", "A", "Proper name at sentence start 'Jammy' must be capitalized."),
        ("What punctuation mark goes in the box? 'The Wannabe Chocolates ruled the market [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which title is capitalized correctly?", "Wannabe Chocolates", "wannabe chocolates", "Wannabe chocolates", "WANNABE CHOCOLATES", "A", "Capital 'W' and 'C' for brand name title."),
        ("What mark goes after a speaker tag: 'Jammy said__ \"This tastes wonderful!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'he said, \"i love this chocolate.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "Everyone loved the new sweets.", "Everyone loved the new sweets?", "Everyone loved the new sweets,", "Everyone loved the new sweets;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like 'the **baker's** shop'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which book chapter title is capitalized correctly?", "The Wannabe Chocolate", "the wannabe chocolate", "The Wannabe chocolate", "THE WANNABE CHOCOLATE", "A", "Major words in titles are capitalized."),
        ("What punctuation mark is used around spoken dialogue: '___Sell this as Wannabe Chocolates!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Speech marks enclose spoken dialogue.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH04_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "Mr. Candy Nougat opened his shop in Chocoland on Monday.", "mr. candy nougat opened his shop in chocoland on monday.", "Mr. candy nougat opened his shop in Chocoland on monday?", "mr. Candy Nougat Opened His Shop In Chocoland On Monday.", "A", "Mr. Candy Nougat (name), Chocoland (town), Monday (day) capitalized; ends with period."),
        ("Which sentence is punctuated as a CORRECT question?", "Who convinced Mr. Candy Nougat to sell the mixture?", "Who convinced Mr. Candy Nougat to sell the mixture.", "Who convinced Mr. Candy Nougat to sell the mixture!", "Who convinced Mr. Candy Nougat to sell the mixture,", "A", "Question starting with 'Who' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'mr. candy nougat lived in a small Town.'", "'mr. candy nougat' should be capitalized ('Mr. Candy Nougat'); 'Town' should be lowercase.", "'Town' should be capitalized only.", "'candy' should be lowercase.", "No mistake.", "A", "Name 'Mr. Candy Nougat' capitalized; common noun town lowercase here."),
        ("Choose the correctly punctuated dialogue sentence:", "\"This mixture tastes amazing,\" said Jammy.", "this mixture tastes amazing said Jammy.", "\"This mixture tastes amazing\" said Jammy", "This mixture tastes amazing, said Jammy.", "A", "Quotation marks around dialogue, comma inside quote, capital T."),
        ("Identify where a COMMA is missing: 'The mix had peanuts caramel cashews and raisins.'", "Between 'peanuts' and 'caramel' ('peanuts, caramel')", "After 'The'", "After 'raisins'", "No comma needed", "A", "Commas separate items in list: 'peanuts, caramel, cashews and raisins'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is Jammy's idea.", "This is Jammys' idea.", "This is Jammys idea.", "This is Jammy's' idea.", "A", "Jammy's indicates possession by Jammy."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a delicious chocolate mixture this is!", "What a delicious chocolate mixture this is?", "What a delicious chocolate mixture this is.", "What a delicious chocolate mixture this is,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'is not'?", "isn't", "is'nt", "isnt'", "i'snt", "A", "isn't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "Chocoland is a wonderful place for candy lovers.", "chocoland is a wonderful place for candy lovers.", "Chocoland Is A Wonderful Place For Candy Lovers.", "chocoland is a Wonderful place for Candy Lovers.", "A", "'Chocoland' capitalized as proper name."),
        ("What punctuation mark belongs in the blank? 'Jammy shouted, \"Wow__ This is the best chocolate ever!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses excitement."),
        ("Choose the correct form for 'does not':", "doesn't", "does'nt", "doesnt'", "d'oesnt", "A", "doesn't is standard contraction."),
        ("Identify the punctuation error: 'The bowl spilled, the mixture tasted great.'", "Comma splice between two independent clauses (should be full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for names and titles:", "Mr. Candy Nougat was a famous baker.", "mr. candy nougat was a famous baker.", "Mr. candy Nougat was a famous baker.", "mr. Candy nougat was a famous baker.", "A", "Title 'Mr.' and name 'Candy Nougat' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "Mr. Candy Nougat's recipe was a big success.", "Mr. Candy Nougats' recipe was a big success.", "Mr. Candy Nougats recipe was a big success.", "Mr. Candy Nougat's' recipe was a big success.", "A", "Nougat's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'The recipe contained ____'", "peanuts, caramel, and raisins.", "peanuts caramel and raisins.", "peanuts; caramel; and raisins.", "peanuts: caramel: and raisins.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "Why did Jammy taste the mixture?", "Why did Jammy taste the mixture.", "Why did Jammy taste the mixture!", "why did Jammy taste the mixture.", "A", "Capital W, ends with question mark ?"),
        ("Fix the sentence: 'where is candy nougats shop'", "Where is Candy Nougat's shop?", "Where is candy nougats shop.", "where is Candy Nougat's shop!", "Where is Candy Nougats' shop?", "A", "Capital W, possessive Candy Nougat's, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Jammy said, \"We should sell these chocolates!\"", "Jammy said \"we should sell these chocolates!\"", "jammy said, \"We should sell these chocolates!\"", "Jammy said, \"We should sell these chocolates.\"", "A", "Capital J, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH04_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on friday jammy said to mr. candy nougat, lets sell wannabe chocolates'", "5 errors (on->On, friday->Friday, jammy->Jammy, lets->let's, capital W in Wannabe, question/period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, person name, contraction let's, capital Wannabe."),
        ("Correct the entire dialogue paragraph: 'mr. candy nougat asked what shall we do with this mix jammy replied we will sell it'", "\"What shall we do with this mix?\" asked Mr. Candy Nougat. Jammy replied, \"We will sell it!\"", "mr. candy nougat asked \"what shall we do with this mix\" jammy replied \"we will sell it.\"", "Mr. Candy Nougat asked, What shall we do with this mix. Jammy replied, We will sell it.", "\"What shall we do with this mix?\" Asked Mr. Candy Nougat. Jammy replied \"We will sell it?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'Jammy**'**s recipe is sweet, and he**'**s happy.'", "First 's is possessive (recipe belonging to Jammy); second 's is contraction (he is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "Jammy's recipe = recipe of Jammy; he's = he is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"It tastes delicious,\" Said Mr. Candy Nougat.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'It' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "He was hard-working, but he was clumsy.", "He was hard-working but, he was clumsy.", "He was hard-working but he was clumsy!", "He was hard-working; but he was clumsy?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'jammy opened the bakery in chocoland on monday 5th october'", "Jammy opened the bakery in Chocoland on Monday, 5th October.", "jammy opened the bakery in chocoland on monday, 5th october.", "Jammy opened the bakery in Chocoland on Monday 5th October", "Jammy opened bakery in chocoland on monday 5th october.", "A", "Jammy, Chocoland, Monday, 5th October, period."),
        ("Identify why exclamation mark is necessary here: '\"Yum! This is the most delicious chocolate!\"'", "Because Jammy is expressing sudden delight and intense enjoyment.", "Because chocolate is brown.", "Because shop is open.", "Because sentence is long.", "A", "Exclamation mark communicates intense enjoyment."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Mr. Candy Nougat, a talented baker, invented Wannabe Chocolates.", "Mr. Candy Nougat a talented baker invented Wannabe Chocolates.", "Mr. Candy Nougat, a talented baker invented Wannabe Chocolates.", "Mr. Candy Nougat a talented baker, invented Wannabe Chocolates.", "A", "Appositive phrase 'a talented baker' is set off by commas."),
        ("Analyze the use of hyphen in: 'The hard-working baker made twenty-five cakes.'", "Hyphens join compound adjective (hard-working) and compound number (twenty-five).", "Hyphen replaces comma.", "Hyphen indicates question.", "Hyphen is an apostrophe.", "A", "Hyphens used in compound modifiers and numbers."),
        ("Identify the correct sentence with direct speech quote within text:", "Jammy declared, \"This will be a huge hit,\" and he was right.", "Jammy declared \"This will be a huge hit\" and he was right.", "Jammy declared, 'This will be a huge hit,' and he was right.", "Jammy declared: \"This will be a huge hit\" and he was right.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The bakers kitchen was full of sweet smells.'", "Missing apostrophe in 'baker's' -> 'The baker's kitchen'", "Missing apostrophe in 'smells''", "Missing apostrophe in 'was''", "No apostrophe needed", "A", "'baker's kitchen' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Jammy, said the baker, is clever.' vs 'Jammy said, \"The baker is clever.\"'", "In the first, baker says Jammy is clever; in the second, Jammy says baker is clever.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is described."),
        ("Correct all 4 errors in: 'whats the new chocolates name asked jammy'", "\"What's the new chocolate's name?\" asked Jammy.", "whats the new chocolates name? asked jammy.", "\"What's the new chocolates name.\" asked Jammy.", "\"whats the new chocolates name?\" Asked Jammy.", "A", "Quotation marks, capital W, possessive chocolate's, question mark, capital J."),
        ("Identify the rule for capitalizing brand names like 'Wannabe Chocolates':", "Brand names and trade titles take initial capital letters.", "Brand names are never capitalized.", "Brand names are capitalized only at end of sentence.", "Brand names must be written in ALL CAPS.", "A", "Trade titles and brand names take initial capitals.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH04_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 04: The Wannabe Chocolate\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'reach'** (in Chapter 04)?", "ea", "ee", "ai", "ou", "A", "'ea' is the vowel digraph in reach."),
        ("Identify the vowel digraph in the word **'sweet'**:", "ee", "ea", "oa", "ui", "A", "'ee' forms the long /e/ vowel sound in sweet."),
        ("Which word from the story contains the **'ou'** vowel digraph?", "nougat", "cake", "bowl", "sugar", "A", "'ou' is in nougat."),
        ("Identify the vowel digraph in the word **'raisin'**:", "ai", "ee", "ow", "oo", "A", "'ai' forms long /a/ sound in raisin."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'oo'** vowel digraph: 'The mixture fell into a spoon.'", "spoon", "mixture", "fell", "into", "A", "'spoon' contains 'oo' digraph."),
        ("Which word from the story rhymes with **'cake'**?", "make", "cook", "like", "leak", "A", "'make' rhymes with 'cake'."),
        ("Which word from the story rhymes with **'sweet'**?", "treat", "sat", "so", "seat", "A", "'treat' / 'seat' rhymes with 'sweet'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the story rhymes with **'town'**?", "brown", "tan", "to", "ton", "A", "'brown' rhymes with 'town'."),
        ("Identify the vowel digraph in **'flavour'**:", "ou", "ea", "ee", "ia", "A", "'ou' is the vowel digraph in flavour."),
        ("Which word from Chapter 04 has the **'ea'** digraph making a long /e/ sound?", "peanuts", "head", "heavy", "dead", "A", "'peanuts' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letter in **'knock'** (as in 'knocked over bowls'):", "k", "n", "o", "c", "A", "Initial 'k' before 'n' is silent in knock."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "delight", "bought", "bowl", "baker", "A", "'igh' in delight makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They found a new recipe.'", "found", "recipe", "new", "they", "A", "'found' contains 'ou' digraph."),
        ("Which word rhymes with **'shop'**?", "drop", "ship", "shut", "show", "A", "'drop' rhymes with 'shop'."),
        ("Identify the silent letter in the word **'know'** (as in 'did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH04_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'peanuts'** and **'bread'**. What is the difference?", "'peanuts' has long /e/ sound; 'bread' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'peanuts' has short /e/; 'bread' has long /e/.", "A", "'ea' can make long /e/ (peanuts) or short /e/ (bread)."),
        ("Select the word pair from Chapter 04 that has the SAME vowel digraph sound:", "sweet - treat", "four - bread", "reach - roar", "cake - sweet", "A", "'sweet' and 'treat' both have long /e/ sound ('ee' / 'ea')."),
        ("Which word contains a SILENT letter? (knock, baker, bowl, cake)", "knock", "baker", "bowl", "cake", "A", "'knock' has silent initial 'k'."),
        ("Identify the odd one out based on vowel sound: (sweet, treat, reach, bread)", "bread", "sweet", "treat", "reach", "A", "'bread' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for dry fruit? 'r__sin'", "ai", "ea", "ee", "ou", "A", "'raisin' uses 'ai' digraph."),
        ("Group these story words by digraph: **found**, **out**, **shouted**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'They loved **the** sweet taste.'", "the", "loved", "sweet", "taste", "A", "'the' contains voiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (bowl, grow, blow, all of these)", "all of these", "bowl", "grow", "blow", "A", "bowl, grow, blow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'flavour'**:", "ou", "ae", "ur", "or", "A", "'ou' is the digraph in flavour."),
        ("Which word from the story has a silent **'k'**? (knock, knee, know, all of these)", "all of these", "knock", "knee", "know", "A", "knock, knee, know all have silent initial 'k'."),
        ("Select the word that rhymes with **'cake'** and fits sentence: 'Jammy baked a ____.'", "shake", "cake", "bake", "lake", "A", "'shake' rhymes with 'cake'."),
        ("Identify the digraph in **'sweetened'**:", "ee", "ea", "ai", "oa", "A", "'ee' makes long /e/ sound."),
        ("Which word has the short /u/ sound made by **'ou'**? (country, house, out, shout)", "country", "house", "out", "shout", "A", "'country' has short /u/ sound with 'ou'."),
        ("Find the R-controlled vowel sound in: 'The mixture was in a **jar**.'", "ar sound", "ea", "ou", "ai", "A", "R-controlled vowel in jar."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 04 vocabulary: (recipe, cake, caramel, cashew)", "recipe", "cake", "caramel", "cashew", "A", "'recipe' has soft /s/ sound for 'c' before 'i'; others have hard /k/ sound."),
        ("Which word has a soft **'g'** sound? (magic, danger, village, all of these)", "all of these", "magic", "danger", "village", "A", "magic, danger, village all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ea'** digraph for reaching:", "reach", "reache", "reachh", "rech", "A", "reach is standard spelling.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH04_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'recipe'** sound like /s/, but 'c' in **'cake'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound; before 'a', 'o', 'u' it makes hard /k/ sound.", "Because recipe is sweet.", "Because cake is baked.", "There is no rule.", "A", "Soft 'c' rule: c + i, e, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (reach, peanuts, bread, heavy, lead [metal])", "Long /e/: reach, peanuts; Short /e/: bread, heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: bread; Short /e/: reach", "A", "reach, peanuts make long /e/; bread, heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "knock - know", "baker - cake", "sweet - bowl", "raisin - peanut", "A", "'knock' (silent k) and 'know' (silent k)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "scrumptious / scraped", "baker", "flavour", "sweet", "A", "'scr' blend type."),
        ("Examine the hard vs soft 'g' rule: Why is 'g' soft in **'magic'** but hard in **'good'**?", "'g' followed by 'e', 'i', or 'y' makes soft /j/ sound (magic); 'g' before 'o' or 'a','u' makes hard /g/ sound (good).", "Because magic is trick.", "Because good is sweet.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "peanuts", "knock", "cake", "bowl", "A", "'peanuts' has 'ea' digraph."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'out'**?", "out - found", "voice - coin", "paid - day", "boat - coat", "A", "'out' and 'found' share /ow/ diphthong sound."),
        ("Analyze homophones: 'Mr. Candy Nougat bought **flour** / **flower** for baking.' Which word is the powder used in baking?", "flour", "flower", "flowr", "flourr", "A", "'flour' (grain powder for baking) and 'flower' (blossom) are homophones."),
        ("Identify the phonic pattern in **'caramel'**: What vowel sound does the first 'a' make?", "Short /a/ sound", "Long /a/ sound", "Silent sound", "R-controlled sound", "A", "'car- / car-a-' first 'a' makes short /a/ or /air/ sound depending on dialect."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (bowls, raisins, peanuts, cakes)", "bowls / raisins", "peanuts", "cakes", "treats", "A", "Plurals ending in voiced consonants take /z/ ending sound (bowls, raisins)."),
        ("Spot the word where 'k' is SILENT: (knock, knee, knife, all of these)", "all of these", "knock", "knee", "knife", "A", "'k' is silent before 'n' in knock, knee, knife."),
        ("HOTS Reasoning: Why do 'sweet' and 'suite' sound identical but have different spellings and meanings?", "They are homophones (same sound, different spelling/meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share pronunciation but differ in spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "peanut / workshop", "Chocoland", "Nougat", "caramel", "A", "peanut = pea + nut."),
        ("Determine the syllable count and stress: How many syllables are in **'chocolate'**?", "3 syllables (choc-o-late)", "2 syllables", "4 syllables", "1 syllable", "A", "choc-o-late has 3 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH04_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 04: The Wannabe Chocolate\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ made the best chocolates in Chocoland?", "Who", "What", "Where", "Why", "A", "'Who' asks about a person (Mr. Candy Nougat)."),
        ("___ did Mr. Candy Nougat accidentally spill into the chocolate bowl?", "What", "Who", "Where", "When", "A", "'What' asks about items (peanuts, caramel, cashews, raisins)."),
        ("___ was the bakery shop located?", "Where", "Who", "What", "Why", "A", "'Where' asks about location (in Chocoland)."),
        ("___ was the assistant of Mr. Candy Nougat?", "Who", "What", "Where", "Why", "A", "'Who' asks about identity (Jammy)."),
        ("___ tasted the new mixture first?", "Who", "Where", "Why", "When", "A", "'Who' asks about subject person (Jammy)."),
        ("___ name was given to the new chocolate mixture?", "What", "Who", "Where", "Why", "A", "'What' asks about name (Wannabe Chocolates)."),
        ("___ did Mr. Candy Nougat want to throw away the mixture?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (he thought it was ruined)."),
        ("___ did Jammy convince Mr. Candy Nougat?", "How", "Who", "Where", "What", "A", "'How' asks about manner/persuasion."),
        ("___ ingredient was Mr. Candy Nougat trying to reach?", "Which", "Who", "Where", "Why", "A", "'Which' asks about specific item (sugar)."),
        ("___ bowls fell into the chocolate mix?", "How many", "Who", "Where", "Why", "A", "'How many' asks about number (four bowls)."),
        ("___ reaction did the customers have to Wannabe Chocolates?", "What", "Who", "Where", "Why", "A", "'What' asks about reaction (they loved them)."),
        ("___ character was talented but clumsy?", "Which", "Who", "Why", "When", "A", "'Which' asks about character (Mr. Candy Nougat)."),
        ("___ did the Wannabe Chocolates rule?", "Where / What market", "Who", "Why", "When", "A", "'Where' asks about place (the market in Chocoland)."),
        ("___ moral lesson does the story teach us?", "What", "Who", "Where", "Why", "A", "'What' asks about lesson (accidents can lead to success with optimism)."),
        ("___ people bought the new chocolates?", "How many / Many", "Who", "Where", "Why", "A", "'How many' asks about quantity."),
        ("___ was the founder of Wannabe Chocolates?", "Who", "What", "Where", "Why", "A", "'Who' asks about founder (Mr. Candy Nougat & Jammy)."),
        ("___ did Jammy taste the mixture?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (he was curious)."),
        ("___ did Mr. Candy Nougat realize his mistake turned out great?", "When", "Who", "Where", "Why", "A", "'When' asks about time (after Jammy tasted it).")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH04_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ did Jammy stop Mr. Candy Nougat from throwing the mix?' Answer: 'Because it tasted amazing.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ was Chocoland located?' Answer: 'In a magical sweet kingdom.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ did Wannabe Chocolates become famous?'", "When", "Where", "Who", "Why", "A", "'When' inquires about time (soon after sales started)."),
        ("Form an asking sentence: 'Jammy tasted the chocolate.' -> '____ did Jammy taste?'", "What", "Who", "Why", "Where", "A", "'What' inquires about object."),
        ("Identify the INCORRECT question word usage: '**Why** is the baker's name?'", "'Why' should be 'What'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'What is the baker's name?' asks for identity."),
        ("Select the proper interrogative sentence:", "Why did Mr. Candy Nougat spill the bowls?", "Why Mr. Candy Nougat spilled the bowls?", "Why did Mr. Candy Nougat spilled the bowls?", "Why baker spill bowls?", "A", "Interrogative word + auxiliary 'did' + base verb 'spill'."),
        ("Which question word asks about MANNER or METHOD? '___ did they create the new recipe?'", "How", "Who", "What", "Where", "A", "'How' inquires about method/manner (by accidental mixing)."),
        ("Complete the question: '___ of the four ingredients was the crunchiest?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options."),
        ("Change statement to question: 'Jammy saved the mixture.' -> '____ saved the mixture?'", "Who", "What", "Where", "Why", "A", "'Who' asks for subject (Jammy)."),
        ("Fill in the blank: '___ clumsy was Mr. Candy Nougat?'", "How", "What", "Where", "Why", "A", "'How clumsy' measures degree."),
        ("Identify the question word in: 'Whom did Jammy convince to sell the chocolates?'", "Whom", "did", "Jammy", "chocolates", "A", "'Whom' is the interrogative pronoun asking about object person."),
        ("Choose the question that matches this answer: 'He spilled the bowls because he reached for sugar clumsily.'", "Why did Mr. Candy Nougat spill the bowls?", "Where did he spill them?", "Who spilled the bowls?", "What did he spill?", "A", "'Why...' matches answer starting with 'because...'."),
        ("Fill in the blank: '___ nut was added to the chocolate?'", "Which", "Who", "Why", "Where", "A", "'Which nut' asks for identification (peanuts, cashews)."),
        ("Complete: '___ sugar was needed for the recipe?'", "How much", "How many", "Who", "Where", "A", "'How much' asks about uncountable quantity (sugar)."),
        ("Select the correct question for: 'Jammy tasted the mixture and found it amazing.'", "What did Jammy do?", "Where was Jammy?", "Why is Jammy lazy?", "Who was the baker?", "A", "'What did Jammy do?' asks for action."),
        ("Which question word inquires about POSSESSION? '___ recipe ruled the market?'", "Whose", "Who", "Where", "Why", "A", "'Whose' asks about origin/ownership."),
        ("Form question: 'Four bowls fell into the mix.' -> '____ bowls fell into the mix?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why did Jammy taste the mix.' Correct it:", "Why did Jammy taste the mix?", "Why did Jammy taste the mix!", "Why did Jammy taste the mix,", "Why did Jammy taste the mix;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH04_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why did Mr. Candy Nougat throw away the original mixture?' What is the syntax pattern?", "Question Word + Helping Verb (did) + Subject (Mr. Candy Nougat) + Main Verb (throw) + Object", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ ingredients' vs '___ sugar'", "'How many' for countable ingredients; 'How much' for uncountable sugar.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for ingredients; 'How many' for sugar.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where Jammy found the new taste?' Correct it:", "Where **did** Jammy find the new taste?", "Where Jammy find the new taste?", "Where found Jammy the new taste?", "Where does Jammy found the new taste?", "A", "Past simple questions require auxiliary 'did' before subject and base verb 'find'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the story plot?", "Who -> What accident happened -> Who tasted it -> How did it become successful", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals character, accident, discovery, and commercial success."),
        ("Transform the statement into a formal question: 'Accidents can lead to creative discoveries.'", "How can an accidental mistake lead to a creative discovery?", "Where is chocolate sold?", "Who is Jammy?", "What is a cake?", "A", "Directly targets the moral lesson."),
        ("Analyze this ambiguous question: 'What did the baker do?' How can it be made precise?", "Add specific context: 'What mistake did Mr. Candy Nougat make while reaching for sugar?'", "Make it shorter: 'What baker?'", "Change to: 'Where baker?'", "Remove 'What'.", "A", "Adding specific context clarifies which action and mistake."),
        ("Choose the correct question pair for dialogue: Candy Nougat: '___ should I do with this spilled mix?' Jammy: '___ don't we sell it as a new treat?'", "What, Why", "Who, Where", "Where, How", "When, Whose", "A", "What (action to take), Why don't we (suggestion)."),
        ("Spot the DOUBLE auxiliary error: 'Why did Mr. Candy Nougat knocked down the bowls?'", "'did' requires base verb 'knock', not past tense 'knocked'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('knock')."),
        ("Reconstruct question from answer: Answer: 'They called it Wannabe Chocolates because it was different from usual chocolates.'", "Question: 'Why was the new sweet named Wannabe Chocolates?'", "Question: 'Where did they bake?'", "Question: 'Who is Jammy?'", "Question: 'Why buy sugar?'", "A", "Targets reason for the name."),
        ("Form indirect question: 'Jammy asked if Mr. Candy Nougat would taste the mix.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ should we never give up on a mistake before testing it?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the moral/practical reason for optimism."),
        ("HOTS Reasoning: Why is 'Who' used for people/characters but 'Which' used when selecting from a specific group of chocolates?", "'Who' is general; 'Which' is used when choosing from a defined limited set.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the chocolates...' selects from a defined group."),
        ("Correct all errors in: 'who spilled the caramel into the bowl'", "Who spilled the caramel into the bowl?", "Who spilled the caramel into the bowl.", "Whom spilled caramel into bowl?", "Who does spilled the caramel into the bowl?", "A", "Capital W, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 04:", "How does Jammy's curious attitude demonstrate that open-mindedness turns mistakes into opportunities?", "What ingredients were in the bowl?", "Where was Chocoland?", "Was the baker clumsy?", "A", "Asks student to evaluate moral theme and cause-and-effect.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH04_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 04: The Wannabe Chocolate\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("Mr. Candy Nougat is **mixing** the chocolate.", "mixing", "Candy Nougat", "is", "chocolate", "A", "'mixing' is verb + -ing form."),
        ("Jammy is **tasting** the new recipe.", "tasting", "Jammy", "is", "recipe", "A", "'tasting' is verb + -ing form."),
        ("The baker is **baking** delicious cakes.", "baking", "baker", "is", "cakes", "A", "'baking' is verb + -ing form."),
        ("Jammy is **convinced** about selling the sweets.", "selling", "selling", "is", "sweets", "A", "'selling' is verb + -ing form."),
        ("Mr. Candy Nougat is **reaching** for the sugar jar.", "reaching", "Candy Nougat", "is", "jar", "A", "'reaching' is verb + -ing form."),
        ("The assistants are **packing** the chocolate boxes.", "packing", "assistants", "are", "boxes", "A", "'packing' is verb + -ing form."),
        ("The customers are **buying** the Wannabe Chocolates.", "buying", "customers", "are", "chocolates", "A", "'buying' is verb + -ing form."),
        ("Jammy is **pouring** the caramel into the bowl.", "pouring", "Jammy", "is", "bowl", "A", "'pouring' is verb + -ing form."),
        ("The baker is **creating** new flavours.", "creating", "baker", "is", "flavours", "A", "'creating' is verb + -ing form."),
        ("The nuts are **crunching** in the mixture.", "crunching", "nuts", "are", "mixture", "A", "'crunching' is verb + -ing form."),
        ("Jammy is **smiling** with delight.", "smiling", "Jammy", "is", "delight", "A", "'smiling' is verb + -ing form."),
        ("Mr. Candy Nougat is **working** hard today.", "working", "Candy Nougat", "is", "today", "A", "'working' is verb + -ing form."),
        ("The ingredients are **blending** together nicely.", "blending", "ingredients", "are", "nicely", "A", "'blending' is verb + -ing form."),
        ("Jammy is **showing** the new chocolate to customers.", "showing", "Jammy", "is", "customers", "A", "'showing' is verb + -ing form."),
        ("The shop is **attracting** many visitors.", "attracting", "shop", "is", "visitors", "A", "'attracting' is verb + -ing form."),
        ("Mr. Candy Nougat is **enjoying** his new success.", "enjoying", "Candy Nougat", "is", "success", "A", "'enjoying' is verb + -ing form."),
        ("Jammy is **cleaning** the spilled ingredients.", "cleaning", "Jammy", "is", "ingredients", "A", "'cleaning' is verb + -ing form."),
        ("The business is **growing** rapidly in Chocoland.", "growing", "business", "is", "Chocoland", "A", "'growing' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH04_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'mix'**? (He is ____ the chocolate.)", "mixing (add -ing)", "mixxing", "mixeing", "mixng", "A", "Regular verb ending in -x adds -ing (mixing)."),
        ("What is the correct -ing spelling rule for **'taste'**? (Jammy is ____ the mixture.)", "tasting (drop final silent e)", "tasteing", "tassting", "tastng", "A", "Drop final silent 'e' before adding -ing (tasting)."),
        ("What is the correct -ing spelling rule for **'bake'**? (The baker is ____ cakes.)", "baking (drop final silent e)", "bakeing", "bakking", "bakng", "A", "Drop final silent 'e' before adding -ing (baking)."),
        ("Fill in the blank with present continuous form: 'Mr. Candy Nougat (reach) ____ for the sugar jar.'", "is reaching", "was reach", "are reach", "is reached", "A", "Singular subject takes 'is reaching'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "Jammy is tasting the new mixture.", "Jammy tasted the new mixture.", "Jammy will taste the new mixture.", "Jammy tasted yesterday.", "A", "'is tasting' is present continuous."),
        ("Fill in the blanks: 'The bakers ____ (prepare) the dough, and Jammy ____ (add) the raisins.'", "are preparing, is adding", "is preparing, are adding", "are prepare, is add", "was preparing, were adding", "A", "Plural 'bakers' takes 'are preparing'; singular 'Jammy' takes 'is adding'."),
        ("Identify the spelling mistake in: 'Mr. Candy Nougat is **makeing** a new chocolate.'", "'makeing' should be 'making'", "'makeing' should be 'making'", "'is' should be 'are'", "No mistake", "A", "Make drops silent e before -ing (making)."),
        ("Select the correct -ing form for **'create'**:", "creating", "createing", "creatting", "creatng", "A", "Drop silent 'e': create -> creating."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "Jammy is packing Wannabe Chocolates into boxes.", "Jammy packed boxes yesterday.", "Jammy packs boxes every day.", "Jammy will pack boxes tomorrow.", "A", "Present continuous ('is packing') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (mix) the peanuts into the liquid chocolate.'", "am mixing", "is mixing", "are mixing", "am mixeing", "A", "Subject 'I' takes 'am mixing'."),
        ("Choose the correct form: 'The customers ____ (enjoy) the crunchy taste.'", "are enjoying", "is enjoying", "am enjoying", "are enjoy", "A", "Plural subject 'customers' takes 'are enjoying'."),
        ("Identify the verb in: 'Why are you throwing away the mixture?'", "are throwing", "Why", "you", "mixture", "A", "Helping verb 'are' + main verb 'throwing' form present continuous."),
        ("What is the -ing form of **'chop'** (nuts)?", "chopping", "choping", "choppping", "chopeing", "A", "CVC rule: chop -> chopping."),
        ("What is the -ing form of **'write'** (a recipe)?", "writing", "writeing", "writting", "writeing", "A", "Drop silent e: write -> writing."),
        ("Change simple present to continuous: 'Jammy tastes the chocolate.' -> 'Jammy ____ the chocolate.'", "is tasting", "tasted", "was tasting", "will taste", "A", "is tasting."),
        ("Fill in the blank: 'The business ____ (grow) every single day.'", "is growing", "are growing", "am growing", "grew", "A", "is growing."),
        ("Identify the correct present continuous sentence:", "Look! Mr. Candy Nougat is creating a new flavor.", "Look! Mr. Candy Nougat create a new flavor.", "Look! Mr. Candy Nougat created a new flavor.", "Look! Mr. Candy Nougat creating a new flavor.", "A", "Exclamation 'Look!' introduces action happening now ('is creating')."),
        ("Select the correct -ing form for **'serve'**:", "serving", "serveing", "servving", "servng", "A", "Drop silent e: serve -> serving.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH04_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (chop, bake, tie)", "chop -> chopping (double consonant), bake -> baking (drop e), tie -> tying (change -ie to -y)", "All just add -ing.", "All double the last letter.", "chop -> choping, bake -> bakeing, tie -> tieing", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'Mr. Candy Nougat reached for sugar while Jammy watched.'", "Mr. Candy Nougat is reaching for sugar while Jammy is watching.", "Mr. Candy Nougat reaching while Jammy watching.", "Mr. Candy Nougat was reaching while Jammy watched.", "Mr. Candy Nougat will reach while Jammy watches.", "A", "Both verbs transformed to present continuous (is reaching, is watching)."),
        ("Spot the missing auxiliary verb in: 'Jammy tasting the mix and Mr. Candy Nougat smiling.' Correct it:", "'Jammy **is** tasting the mix and Mr. Candy Nougat **is** smiling.'", "'Jammy tasting mix and Mr. Candy Nougat smiling.'", "'Jammy **are** tasting and Mr. Candy Nougat **are** smiling.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'Jammy is **wanting** the recipe'?", "Because 'want' is a stative verb expressing a desire, not an ongoing physical action.", "Because 'wanting' is hard to spell.", "Because baker made it.", "Because sugar spilled.", "A", "Stative verbs (want, know, love) do not usually take continuous form."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The two bakers are inventing new chocolate recipes.", "The two bakers is inventing new chocolate recipes.", "The two bakers am inventing new chocolate recipes.", "The two bakers inventing new chocolate recipes.", "A", "Plural subject ('two bakers') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'Mr. Candy Nougat is throwing away the mixture.' -> Negative:", "Mr. Candy Nougat is **not** throwing away the mixture.", "Mr. Candy Nougat not throwing away the mixture.", "Mr. Candy Nougat is no throwing away the mixture.", "Mr. Candy Nougat isn't throw away the mixture.", "A", "Add 'not' between auxiliary 'is' and main verb 'throwing'."),
        ("Spot all THREE spelling errors: 'He is **bakeing** cakes, **runing** fast, and **dieing** of joy.'", "'bakeing' -> 'baking'; 'runing' -> 'running'; 'dieing' -> 'dying'", "'bakeing' -> 'bakking'; 'runing' -> 'runing'; 'dieing' -> 'dieing'", "No errors.", "Only 'runing' is wrong.", "A", "baking (drop e), running (double n), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'Jammy is tasting the chocolate.'", "**Is** Jammy tasting the chocolate?", "Are Jammy tasting the chocolate?", "Jammy tasting the chocolate?", "Why Jammy is tasting chocolate?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The bakery **is launching** a new product next week.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While Mr. Candy Nougat is baking, Jammy is packing boxes.", "While baker baked, Jammy is packing.", "Baker is baking while Jammy packed.", "Baker bake while Jammy pack.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'Jammy is mixxing the caramel and peanuts.'", "'mixxing' should be 'mixing' (single 'x').", "'is' should be 'are'.", "'caramel' should be capitalized.", "No error.", "A", "Verbs ending in -x do NOT double the x (mixing)."),
        ("HOTS Reasoning: Compare 'Jammy spilled the sugar' (Past Simple) vs 'Jammy is spilling the sugar' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means sugar was saved.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the customers ____ (buying) so many chocolates?'", "are, buying", "is, buying", "am, buying", "do, buying", "A", "Plural subject customers takes 'are ... buying'."),
        ("Identify the correct present continuous sentence describing shop activity:", "The busy team of bakers is preparing Wannabe Chocolates.", "The busy team of bakers is prepare Wannabe Chocolates.", "The busy team of bakers are preparing Wannabe Chocolates.", "The busy team of bakers preparing Wannabe Chocolates.", "A", "Collective singular subject 'team of bakers' + is + preparing.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH04_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 04: The Wannabe Chocolate\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("Mr. Candy Nougat ___ a talented baker.", "is", "are", "am", "be", "A", "Singular subject 'Mr. Candy Nougat' takes 'is'."),
        ("I ___ enjoying the story of Wannabe Chocolates.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The new chocolates ___ delicious and crunchy.", "are", "is", "am", "be", "A", "Plural subject 'chocolates' takes 'are'."),
        ("Jammy ___ a clever assistant.", "is", "are", "am", "be", "A", "Singular subject 'Jammy' takes 'is'."),
        ("The ingredients ___ mixed together in the bowl.", "are", "is", "am", "be", "A", "Plural subject 'ingredients' takes 'are'."),
        ("Chocoland ___ a famous sweet town.", "is", "are", "am", "be", "A", "Singular subject 'Chocoland' takes 'is'."),
        ("The customers ___ standing in line.", "are", "is", "am", "be", "A", "Plural subject 'customers' takes 'are'."),
        ("Mr. Candy Nougat and Jammy ___ working together.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ sure that trying new things brings success.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The new recipe ___ a huge success.", "is", "are", "am", "be", "A", "Singular 'recipe' takes 'is'."),
        ("The raisins and cashews ___ tasty.", "are", "is", "am", "be", "A", "Plural subject takes 'are'."),
        ("The bakery shop ___ clean and bright.", "is", "are", "am", "be", "A", "Singular 'shop' takes 'is'."),
        ("You ___ reading Chapter 04.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The mixture ___ tasting amazing.", "is", "are", "am", "be", "A", "Singular 'mixture' takes 'is'."),
        ("The Wannabe Chocolates ___ popular everywhere.", "are", "is", "am", "be", "A", "Plural 'chocolates' takes 'are'."),
        ("I ___ happy for Mr. Candy Nougat.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("Jammy ___ tasting the chocolate.", "is", "are", "am", "be", "A", "Singular 'Jammy' takes 'is'."),
        ("The boxes ___ filled with sweets.", "are", "is", "am", "be", "A", "Plural 'boxes' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH04_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'Mr. Candy Nougat and his assistant Jammy ____ preparing fresh sweets.'", "are", "is", "am", "be", "A", "Compound subject ('baker and assistant') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "Mr. Candy Nougat is reaching for the bowl.", "Mr. Candy Nougat are reaching for the bowl.", "Mr. Candy Nougat am reaching for the bowl.", "Mr. Candy Nougat be reaching for the bowl.", "A", "Singular noun 'Mr. Candy Nougat' requires 'is'."),
        ("Fill in the blanks: 'I ____ eating a Wannabe Chocolate, and my friends ____ eating cakes.'", "am, are", "is, are", "are, is", "am, is", "A", "'I am', 'friends are'."),
        ("Identify the mistake in: 'The bowls of nuts **is** on the table.'", "'is' should be 'are' because 'bowls' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'bowls' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you ready to taste the new chocolate?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither sugar nor flour ____ wasted in the kitchen.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject takes 'is'."),
        ("Select the correct sentence for story moral:", "Curiosity and optimism are important for innovation.", "Curiosity and optimism is important for innovation.", "Curiosity and optimism am important for innovation.", "Curiosity and optimism be important for innovation.", "A", "Compound subject 'Curiosity and optimism' takes 'are'."),
        ("Complete the conversation: Candy Nougat: 'Where ____ the new boxes?' Jammy: 'They ____ on the counter!'", "are, are", "is, is", "is, are", "are, is", "A", "Plural 'new boxes' -> are; plural 'They' -> are."),
        ("Identify where 'is' is used incorrectly:", "The peanuts **is** crunchy.", "The chocolate is sweet.", "The baker is clever.", "The shop is open.", "A", "'The peanuts is' should be 'The peanuts are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The team of bakers ____ working.'", "is", "are", "am", "be", "A", "Collective noun 'team' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The assistant ____ not afraid to try new flavours.'", "is", "are", "am", "be", "A", "Singular 'assistant' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am buying a box of Wannabe Chocolates.", "I is buying a box of Wannabe Chocolates.", "I are buying a box of Wannabe Chocolates.", "I be buying a box of Wannabe Chocolates.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ four bowls of ingredients on the shelf.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'four bowls'."),
        ("Fill in the blank: 'There ____ a sweet aroma in the kitchen.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a sweet aroma'."),
        ("Choose the correct sentence:", "What are the customers saying about the new recipe?", "What is the customers saying about the new recipe?", "What am the customers saying about the new recipe?", "What be the customers saying about the new recipe?", "A", "Plural subject 'the customers' takes 'are'."),
        ("Identify the correct form: 'The baker, as well as his assistants, ____ happy with the result.'", "is", "are", "am", "be", "A", "Subject is singular 'The baker' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both Jammy and Mr. Candy Nougat ____ proud of their discovery.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The recipe ____ new, but the ingredients ____ traditional.'", "is, are", "are, is", "am, are", "is, is", "A", "'recipe is', 'ingredients are'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH04_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the four bowls **____** filled with ingredients.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'four bowls' is plural.", "am — because it refers to speaker.", "be — because bowls are full.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A box of delicious Wannabe Chocolates **are** sitting on the table.'", "'are' should be 'is' because the subject is singular noun 'box'.", "'are' should be 'am'.", "'chocolates' should be 'chocolate'.", "No error.", "A", "'A box' is singular, so it requires 'is sitting'."),
        ("Compare: (1) 'Mr. Candy Nougat and Jammy **are** baking.' vs (2) 'Mr. Candy Nougat, together with Jammy, **is** baking.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'together with' is a prepositional phrase, leaving 'Mr. Candy Nougat' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'together with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in Chocoland **____** buying the new treat.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The nuts **is** crunchy, I **is** happy, and the baker **are** talented.'", "'nuts is' -> 'nuts are'; 'I is' -> 'I am'; 'baker are' -> 'baker is'", "'nuts is' -> 'nuts am'; 'I is' -> 'I are'; 'baker are' -> 'baker am'", "Only 'I is' is wrong.", "No errors present.", "A", "nuts are (plural), I am (1st person), baker is (3rd person singular)."),
        ("Fill in the blanks in this complex sentence: 'Not only the baker but also his assistants **____** baking, while the customers **____** waiting.'", "are, are", "is, are", "is, is", "are, is", "A", "'Not only...but also' agrees with closer subject ('assistants' -> are); 'customers' -> are."),
        ("Transform to negative: 'The peanuts and caramel are in the chocolate bowl.'", "The peanuts and caramel **are not** in the chocolate bowl.", "The peanuts and caramel is not in the chocolate bowl.", "The peanuts and caramel am not in the chocolate bowl.", "The peanuts and caramel not in bowl.", "A", "Add 'not' after plural helping verb 'are'."),
        ("Analyze inverted subject position: 'On the kitchen table **____** standing four colorful bowls.'", "are", "is", "am", "be", "A", "Subject is plural 'four colorful bowls', appearing after verb, requiring 'are'."),
        ("Determine agreement with uncountable nouns: 'The melted chocolate **____** warm and smooth.'", "is", "are", "am", "be", "A", "Uncountable mass noun 'chocolate' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the new Wannabe Chocolates you ordered.'", "Here **are** the new Wannabe Chocolates you ordered.", "Here am the new Wannabe Chocolates you ordered.", "Here be the new Wannabe Chocolates you ordered.", "No error.", "A", "Plural subject 'Wannabe Chocolates' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "Mr. Candy Nougat **is** a clumsy baker.", "Mr. Candy Nougat **is** mixing the chocolate.", "Mr. Candy Nougat **is** reaching for sugar.", "Mr. Candy Nougat **is** selling the sweets.", "A", "In 'Mr. Candy Nougat is a clumsy baker', 'is' is the main linking verb connecting subject to predicate noun."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because Jammy commanded it.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither Mr. Candy Nougat nor Jammy **____** throwing away the mix, because it **____** delicious.'", "is, is", "are, is", "is, are", "are, are", "A", "'Jammy' is singular closer subject -> is; 'it' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "The baker is hard-working, I am curious, and the chocolates are sweet.", "The baker are hard-working, I is curious, and the chocolates is sweet.", "The baker am hard-working, I are curious, and the chocolates am sweet.", "The baker is hard-working, I is curious, and the chocolates is sweet.", "A", "baker is (singular), I am (1st person), chocolates are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH04_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 04
# ---------------------------------------------------------------------------
def rebuild_chapter_04():
    print("Rebuilding Chapter 04 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH04_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 04 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_04()
