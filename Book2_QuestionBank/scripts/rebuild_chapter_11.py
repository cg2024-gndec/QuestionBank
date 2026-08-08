r"""
=============================================================================
Script: rebuild_chapter_11.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 11:
             "A Little Bird I Am" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH11_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_11")
os.makedirs(CH11_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 11: A Little Bird I Am\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("bird", "birds", "birdes", "birdies", "birdz", "A", "Regular noun adding -s."),
        ("field", "fields", "fieldes", "fieldies", "fieldz", "A", "Regular noun adding -s."),
        ("cage", "cages", "cagies", "cagees", "cagez", "A", "Regular noun ending in -e adds -s."),
        ("prisoner", "prisoners", "prisoneres", "prisoneries", "prisonerz", "A", "Regular noun adding -s."),
        ("song", "songs", "songes", "songies", "songz", "A", "Regular noun adding -s."),
        ("wing", "wings", "winges", "wingies", "wingz", "A", "Regular noun adding -s."),
        ("day", "days", "daies", "dayes", "dayz", "A", "Vowel + y adds -s."),
        ("sky", "skies", "skys", "skyes", "skiz", "A", "Consonant + y changes to -ies."),
        ("feather", "feathers", "featheres", "featheries", "featherz", "A", "Regular noun adding -s."),
        ("bar", "bars", "bares", "baries", "barz", "A", "Regular noun adding -s."),
        ("note", "notes", "noties", "notees", "notez", "A", "Regular noun ending in -e adds -s."),
        ("voice", "voices", "voicies", "voicees", "voicez", "A", "Regular noun ending in -e adds -s."),
        ("branch", "branches", "branchs", "branchies", "branchz", "A", "Nouns ending in -ch add -es."),
        ("wish", "wishes", "wishs", "wishies", "wished", "A", "Nouns ending in -sh add -es."),
        ("leaf", "leaves", "leafs", "leafes", "leavies", "A", "Nouns ending in -f change -f to -ves."),
        ("story", "stories", "storys", "storyes", "storiz", "A", "Consonant + y changes to -ies."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH11_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 11 (*A Little Bird I Am*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The poem describes two (bird / birds) singing in their cages.", "birds", "bird", "birdes", "birdies", "A", "Plural noun 'birds'."),
        ("The bird misses the open (field / fields) of air.", "fields", "field", "fieldes", "fieldies", "A", "Plural noun 'fields'."),
        ("The captive birds sit inside their wooden (cage / cages).", "cages", "cage", "cagies", "cagees", "A", "Regular noun ending in -e adds -s (cages)."),
        ("Identify the INCORRECT plural spelling in this list: birds, wings, skys, songs.", "skys", "birds", "wings", "songs", "A", "Plural of sky is 'skies', not 'skys'."),
        ("Choose the sentence with the correct plural noun form:", "The bird spread both wings and sang sweet songs.", "The bird spread both winges and sang sweet songes.", "The bird spread both wingies and sang sweet songies.", "The bird spread both wingz and sang sweet songz.", "A", "wings (-s) and songs (-s) are correct."),
        ("Which noun forms its plural by changing consonant + y to -ies?", "sky -> skies", "day -> days", "bird -> birds", "cage -> cages", "A", "Sky ends in consonant + y, so plural is skies."),
        ("Change the singular noun in brackets to plural: 'The bird lost three ____ (feather) from its wing.'", "feathers", "featheres", "featheries", "featherz", "A", "Regular noun adding -s (feathers)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The birds sing sweet notes behind iron bars.", "The birdes sing sweet noties behind iron bares.", "The birds sing sweet notees behind iron barz.", "The birdz sing sweet notes behind iron baries.", "A", "birds, notes, bars are all correctly spelt plurals."),
        ("What is the correct plural of 'wandering wing'?", "wandering wings", "wandering winges", "wandering wingies", "wandering wingz", "A", "Regular noun adding -s."),
        ("The bird sings during all the (day / days) of the week.", "days", "daies", "day", "dayes", "A", "Vowel + y adds -s (days)."),
        ("Many (bird / birds) are kept as pets in cages.", "birds", "birdes", "birdies", "birdz", "A", "Plural of bird is birds."),
        ("Many (person / people) enjoy listening to bird songs.", "people", "persons", "peoples", "persones", "A", "Irregular plural of person is people."),
        ("How many (cage / cages) were placed on the porch?", "cages", "cage", "cagies", "cagees", "A", "Regular noun ending in -e adds -s (cages)."),
        ("The bird remembers flying over green (branch / branches).", "branches", "branchs", "branchies", "branchz", "A", "Nouns ending in -ch add -es (branches)."),
        ("Which plural noun rule applies to the word **'wishes'**?", "Add -es to nouns ending in -sh", "Add -s to vowel + y", "Change -f to -ves", "Change -y to -ies", "A", "Wish ends in -sh, so it adds -es."),
        ("The birds send sweet (song / songs) to God.", "songs", "songes", "songies", "songz", "A", "Plural of song is songs."),
        ("Identify the correct plural form of 'child':", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("The bird's (voice / voices) sound joyful.", "voices", "voicees", "voicies", "voicez", "A", "Regular noun ending in -e adds -s (voices).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH11_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The prisoner bird sang a song in the cage.'", "The prisoner birds sang songs in the cages.", "The prisoneres birdes sang songes in the cagees.", "The prisoner birds sang song in the cages.", "The prisoner birdz sang songies in the cagies.", "A", "Plural of prisoner->prisoners, bird->birds, song->songs, cage->cages."),
        ("Analyze the error: 'The bird has much songs.' Why is 'much' inappropriate here?", "'songs' is a plural countable noun, so 'many songs' should be used.", "'songs' should be 'songes'.", "'songs' should be 'songies'.", "No error.", "A", "Countable plural nouns take 'many', not 'much'."),
        ("Complete the paragraph with correct plurals: 'The two ____ (bird) spread four ____ (wing) and sang five ____ (song).'", "birds, wings, songs", "birdes, winges, songes", "birdz, wingies, songies", "birdees, wings, songs", "A", "birds (-s), wings (-s), songs (-s)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **children** watched **birds** flap their **wings**.", "The **childs** watched **birdes** flap their **winges**.", "The **childrens** watched **birdies** flap their **wingies**.", "The **childes** watched **birds** flap their **wingz**.", "A", "children (irregular), birds (-s), wings (-s)."),
        ("Which group contains ONLY irregular plural nouns?", "children, people, men, feet", "birds, cages, wings, songs", "skies, stories, cities, countries", "leaves, thieves, wolves, knives", "A", "children, people, men, feet change forms without standard -s/-es."),
        ("Why does 'day' become 'days' but 'sky' becomes 'skies'?", "Because 'day' has a vowel before y (a+y -> -s), while 'sky' has a consonant before y (k+y -> -ies).", "Because 'day' is short and 'sky' is high.", "Because 'day' is time and 'sky' is air.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The two familys visited the zoo and saw many mouses.'", "'familys' should be 'families' and 'mouses' should be 'mice'.", "'familys' should be 'family' and 'mouses' should be 'mices'.", "'zoo' should be 'zoos' only.", "There are no mistakes in the sentence.", "A", "families (consonant + y) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'The birds flapped their ____ (foot) and stretched their ____ (wing).'", "feet, wings", "foots, winges", "feets, wings", "foots, wingies", "A", "Plural of foot is feet, plural of wing is wings."),
        ("Analyze this sentence: 'The bird sings in the air.' Can 'air' be pluralized as 'airs' in general physical sense?", "No, 'air' is an uncountable material noun; 'airs' means arrogant behavior.", "Yes, 'airs' is standard for oxygen.", "No, it becomes 'airess'.", "Yes, 'an air' is correct.", "A", "Air as atmosphere is an uncountable mass noun."),
        ("Fill in the blanks: 'The two ____ (child) listened to three ____ (song) of the bird.'", "children, songs", "childs, songes", "childrens, songies", "childes, songs", "A", "child -> children; song -> songs."),
        ("Select the option that shows correct plural transformation for ALL three words: 'leaf', 'story', 'branch'", "leaves, stories, branches", "leafs, storys, branchs", "leaves, storyes, branchies", "leafes, stories, foxen", "A", "leaf -> leaves; story -> stories; branch -> branches."),
        ("HOTS Reasoning: Why do we say 'the bird sings with joy' rather than 'joys'?", "Because 'joy' in the sense of happiness is an abstract uncountable noun.", "Because joy is happy.", "Because cage is small.", "Because bird is little.", "A", "Uncountable abstract noun takes singular form."),
        ("Transform into singular: 'The birds sang songs in the cages.'", "The bird sang a song in the cage.", "The birds sang a song in the cage.", "The bird sing a song in the cage.", "The bird sang songs in the cage.", "A", "Singular forms: bird, song, cage."),
        ("Identify the correct rule for forming the plural of **'cage'**:", "Add -s because it is a regular noun ending in -e (cages).", "Add -es (cagees).", "Change -e to -ves (caves).", "Change vowel sound.", "A", "Regular noun ending in -e adds -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH11_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 11: A Little Bird I Am\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("I am ___ little bird in a cage.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'little'."),
        ("The bird is shut from ___ fields of air.", "the", "a", "an", "no article", "A", "Use 'the' for specific fields of air."),
        ("The bird sits in ___ wooden cage.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'wooden'."),
        ("It is pleased to be ___ prisoner for God.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'prisoner'."),
        ("The bird sings ___ sweet song all day long.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'sweet'."),
        ("___ Panchatantra/Poetry lesson presents the little bird.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra/Poetry'."),
        ("The bird sings for ___ whole day long.", "the", "a", "an", "no article", "A", "Use 'the' in fixed phrase 'the whole day long'."),
        ("God gave the bird ___ airy sky to remember.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'airy'."),
        ("___ bird is happy because it pleases God.", "The", "A", "An", "No article", "A", "Definite article 'The' specifies the bird in the poem."),
        ("It has ___ unusual feeling of joy in captivity.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unusual'."),
        ("God bound its ___ wandering wing.", "no article", "a", "an", "the", "A", "Possessive pronoun 'its' takes no article before 'wandering wing'."),
        ("It is ___ honest prayer of devotion.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ song of the bird reaches God.", "The", "A", "An", "No article", "A", "Use 'The' for specific song of the bird."),
        ("The bird sits upon ___ perching bar.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'perching'."),
        ("They created ___ peaceful room for the bird cage.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'peaceful'."),
        ("The bird sings with ___ open heart.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'open'."),
        ("The bird finds ___ happiness in pleasing God.", "no article", "a", "an", "the", "A", "Abstract noun 'happiness' takes no indefinite article here."),
        ("___ sun shines outside the bird's cage.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH11_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The speaker is ___ little bird in ___ small cage.", "a, a", "an, a", "a, an", "the, a", "A", "'a little bird' (consonant sound), 'a small cage' (consonant sound)."),
        ("Why do we say '**a** bird' but '**an** airy sky'?", "Because 'bird' begins with a consonant sound (b) and 'airy' with a vowel sound (a).", "Because birds fly.", "Because sky is blue.", "Because cages are small.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "A little bird sits in a cage.", "An little bird sits in an cage.", "The a little bird sits in cage.", "A little bird sits in an cage.", "A", "'A little bird' (consonant sound), 'a cage' (consonant sound)."),
        ("Fill in the blanks: 'The bird sings ___ song to ___ Lord.'", "a, the", "an, a", "a, an", "the, a", "A", "'a song' (consonant /s/), 'the Lord' (specific title)."),
        ("Identify the INCORRECT article in: 'The bird has **a** open wing.'", "'a' should be 'an'", "'a' should be 'the'", "'open' should be 'a open'", "No mistake", "A", "'open' starts with vowel sound /o/, so it takes 'an'."),
        ("Which article completes the sentence? 'The song is ___ inspiring tune in the poem.'", "an", "a", "the", "no article", "A", "'inspiring' starts with vowel sound /i/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ bird sang from ___ cage.'", "The, the", "A, a", "An, an", "The, a", "A", "'The bird' (specific bird), 'the cage' (specific cage)."),
        ("Why do we use 'an' before 'open wing' in 'The bird stretched **an** open wing'?", "Because 'open' begins with the vowel sound /o/.", "Because wing is a noun.", "Because bird is small.", "Because cage is shut.", "A", "'open' starts with vowel sound /o/."),
        ("Complete the dialogue: Child: 'Is that ___ caged bird?' Speaker: 'Yes, it is ___ happy bird!'", "a, a", "a, an", "an, the", "the, the", "A", "'a caged bird' (consonant sound), 'a happy bird' (consonant sound)."),
        ("Select the correct sentence:", "A bird is a cheerful creature.", "An bird is a cheerful creature.", "The bird is an cheerful creature.", "An bird is an cheerful creature.", "A", "'A bird' (consonant sound), 'a cheerful creature' (consonant sound)."),
        ("Fill in the blank: 'The bird sings for ___ long time every day.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The bird sings with **___ devotion** to God.", "He caught ___ bird.", "She opened ___ cage.", "They heard ___ song.", "A", "Abstract noun 'devotion' takes no indefinite article here."),
        ("Choose the correct sentence for poem summary:", "Faith and joy give peace to the soul.", "A faith and a joy give peace.", "An faith and an joy give peace.", "The faith a gives peace.", "A", "Abstract concepts take no indefinite articles in general moral sense."),
        ("Fill in the blanks: 'The poet spent ___ hour writing ___ beautiful poem.'", "an, a", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'a beautiful poem' (consonant b)."),
        ("Which sentence uses 'the' correctly for specific poem phrases?", "The bird sits in the cage and sings the whole day long.", "A bird sits in a cage and sings a whole day long.", "An bird sits in an cage and sings an whole day long.", "Bird sits in cage and sings whole day long.", "A", "Fixed phrase 'the whole day long' and specific 'the cage'."),
        ("Identify the article error: 'The bird gave **a** explanation of **an** short song.'", "'an short' should be 'a short' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an short' should be 'a short'", "No error", "A", "'an explanation' (vowel /e/) and 'a short song' (consonant /s/)."),
        ("Complete: 'It was ___ unexpected song of joy in ___ cage.'", "an, the", "a, an", "the, the", "an, an", "A", "an unexpected (/u/), the cage (specific)."),
        ("Choose the correct option: '___ sun set while the bird sang.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH11_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'The bird sings **a** song to **the** God.' Correct the error:", "'the God' -> 'God' (proper noun God takes no article in this devotional context).", "'a song' -> 'an song'.", "'The bird' -> 'An bird'.", "No error.", "A", "Proper name God takes no article in devotional poetry."),
        ("Fill in all three blanks: '___ bird in ___ cage sang ___ sweet melody.'", "The, the, a", "A, a, a", "An, a, the", "The, a, a", "A", "'The bird' (specific), 'the cage' (specific), 'a sweet melody' (consonant sound)."),
        ("Identify why 'the' is used in: 'I sing **the** whole day long.'", "Because 'the whole day long' is an idiomatic time phrase specifying full duration.", "Because day is a noun.", "Because bird is small.", "Because cage is iron.", "A", "'the whole day long' is a fixed idiomatic duration phrase."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** eagle to fly past the cage.'", "'a hour' should be 'an hour' and 'a eagle' should be 'an eagle'.", "'a hour' should be 'the hour' and 'a eagle' should be 'a eagle'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'eagle' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A little bird sat in a cage. The bird sang a sweet song. God listened to the song.", "An little bird sat in an cage. A bird sang an sweet song.", "The little bird sat in a cage. Bird sang a sweet song.", "A little bird sat in a cage. The song was an honest.", "A", "A little bird (first mention), a cage (consonant), The bird (second mention), a sweet song (consonant), God (no article), the song (second mention)."),
        ("Why is it correct to write 'a unique song' but 'an unusual song'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because song is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the poem summary: '___ captive bird offers ___ praise to ___ Almighty.'", "A, no article, the", "An, a, an", "The, the, the", "A, a, a", "A", "A captive bird, praise (uncountable mass noun, no article), the Almighty (divine title takes 'the')."),
        ("Analyze this sentence: 'The bird loves **the** Creator.' Why is 'the' appropriate?", "Because 'the Creator' is a capitalized title referring uniquely to God.", "Because Creator is a verb.", "Because bird is in cage.", "Because wing is bound.", "A", "'the Creator' specifies the unique divine title."),
        ("Correct the sentence: 'An little bird has a open wing in a cage.'", "A little bird has an open wing in a cage.", "The little bird has an open wing in an cage.", "An little bird has the open wing in a cage.", "A little bird has a open wing in a cage.", "A", "'A little' (/l/ sound), 'an open' (vowel /o/), 'a cage' (consonant /k/)."),
        ("Fill in the blanks: '___ songs of ___ little bird pleased ___ God.'", "The, the, no article", "A, a, a", "No article, a, an", "An, the, a", "A", "'The songs' (specific), 'the little bird' (specific), God (proper name, no article)."),
        ("Spot the missing article: 'Bird sat in cage and sang to God.'", "Missing 'A' before 'Bird' and 'a' before 'cage' -> 'A bird sat in a cage...'", "Missing 'an' before 'God'", "Missing 'a' before 'to'", "No article is missing", "A", "Singular countable nouns 'bird' and 'cage' require articles."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An eagle flew past a window of the house.", "A eagle flew past an window of a house.", "The eagle flew past an window of an house.", "An eagle flew past an window of the house.", "A", "An eagle (vowel), a window (consonant), the house (specific)."),
        ("Rewrite correctly: 'The bird is a honest prisoner with an sweet voice.'", "The bird is an honest prisoner with a sweet voice.", "The bird is a honest prisoner with a sweet voice.", "The bird is an honest prisoner with an sweet voice.", "The bird is the honest prisoner with an sweet voice.", "A", "'an honest' (silent h), 'a sweet voice' (consonant /s/)."),
        ("Identify the correct rule for capitalizing divine names/pronouns in devotional poetry (God, Him, He, Thee):", "Divine names and personal pronouns referring to God in sacred/poetic text are capitalized.", "Divine names are never capitalized.", "Divine names are capitalized only at end of line.", "Divine names must be written in ALL CAPS.", "A", "Devotional text capitalizes references to God.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH11_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 11: A Little Bird I Am\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("The bird sings **'the whole day long'**. How many hours make up **1 full day (24 hours)**?", "24 hours", "12 hours", "48 hours", "10 hours", "A", "1 full day = 24 hours."),
        ("How many daytime hours are between 6:00 AM and 6:00 PM?", "12 hours", "24 hours", "6 hours", "18 hours", "A", "12 daytime hours."),
        ("What is the standard abbreviation for **Sunday**?", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard abbreviation."),
        ("Which day comes right after Saturday?", "Sunday", "Monday", "Friday", "Thursday", "A", "Sunday follows Saturday."),
        ("What is the abbreviation for **Monday**?", "Mon.", "Mnd.", "Mo.", "Mn.", "A", "Mon. is standard abbreviation."),
        ("The bird sings in the **morning**, **afternoon**, and **evening**. What time of day comes right after afternoon?", "Evening", "Night", "Morning", "Dawn", "A", "Evening follows afternoon."),
        ("What is the abbreviation for **Friday**?", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard abbreviation."),
        ("What time of day is 12:00 AM?", "Midnight", "Noon", "Afternoon", "Dawn", "A", "Midnight is 12:00 AM."),
        ("What is the abbreviation for **Saturday**?", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard abbreviation."),
        ("Which month comes right before September?", "August", "July", "October", "November", "A", "August comes before September."),
        ("What is the short abbreviation for **September**?", "Sept. or Sep.", "Spt.", "Septe.", "St.", "A", "Sept. or Sep. is standard abbreviation."),
        ("Which month comes right after September?", "October", "November", "August", "July", "A", "October comes after September."),
        ("What is the short abbreviation for **October**?", "Oct.", "Octo.", "Oc.", "Ot.", "A", "Oct. is standard abbreviation."),
        ("If today is Sunday, what day was yesterday?", "Saturday", "Monday", "Friday", "Thursday", "A", "Yesterday was Saturday."),
        ("If today is Sunday, what day will tomorrow be?", "Monday", "Saturday", "Tuesday", "Wednesday", "A", "Tomorrow will be Monday."),
        ("What is the abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("Which day comes between Tuesday and Thursday?", "Wednesday", "Friday", "Monday", "Sunday", "A", "Wednesday is between Tuesday and Thursday."),
        ("Which month comes right before October?", "September", "August", "November", "December", "A", "September comes before October.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH11_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The bird sang continuously from **Monday** to **Friday**. For how many days did it sing?", "5 days", "4 days", "6 days", "7 days", "A", "Monday to Friday inclusive is 5 days."),
        ("The bird sang from **7:00 AM to 1:00 PM**. How many hours did it sing?", "6 hours", "5 hours", "7 hours", "4 hours", "A", "1:00 PM - 7:00 AM = 6 hours."),
        ("Match the day with its abbreviation: **Tuesday**", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. is standard."),
        ("If the bird sings every day for **1 week**, how many days is that?", "7 days", "5 days", "10 days", "14 days", "A", "1 week = 7 days."),
        ("Identify the correctly spelt month name:", "September", "Septembre", "Septemberr", "Septembere", "A", "September is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Sunday - Snd.", "D", "Sunday abbreviation is Sun., not Snd."),
        ("Calculate: How many days are in **September**?", "30 days", "31 days", "28 days", "29 days", "A", "September has 30 days."),
        ("Which month has 30 days and comes right after August?", "September", "October", "July", "November", "A", "September has 30 days and follows August."),
        ("Rearrange in correct chronological order: Fri, Sun, Sat, Thu", "Thu, Fri, Sat, Sun", "Fri, Thu, Sat, Sun", "Sun, Sat, Fri, Thu", "Thu, Sat, Fri, Sun", "A", "Thursday -> Friday -> Saturday -> Sunday."),
        ("What day is 4 days before Sunday?", "Wednesday", "Thursday", "Tuesday", "Monday", "A", "Sunday - 4 days = Saturday(1), Friday(2), Thursday(3), Wednesday(4)."),
        ("If a bird singing contest lasts for 2 weeks, how many days is that?", "14 days (2 x 7)", "10 days", "20 days", "7 days", "A", "2 weeks x 7 days = 14 days."),
        ("Select the month that has 31 days:", "October", "September", "April", "June", "A", "October has 31 days."),
        ("Which abbreviation stands for **October**?", "Oct.", "Octo.", "Oc.", "Ot.", "A", "Oct. is standard abbreviation."),
        ("If today is **Sun.**, what day will it be after 7 days?", "Sunday", "Monday", "Saturday", "Friday", "A", "7 days is a full week cycle, landing on Sunday again."),
        ("The bird rested from **12:00 PM to 2:00 PM**. How many hours did it rest?", "2 hours", "1 hour", "3 hours", "4 hours", "A", "2:00 PM - 12:00 PM = 2 hours."),
        ("Identify the word that means 'occurring every single day':", "Daily", "Weekly", "Monthly", "Yearly", "A", "Daily means every day."),
        ("Which of the following is a weekend day?", "Saturday", "Monday", "Tuesday", "Wednesday", "A", "Saturday is a weekend day."),
        ("Choose the correct abbreviation for **September**:", "Sept. or Sep.", "Spt.", "Septe.", "St.", "A", "Sept. or Sep. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH11_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("The poet Louisa May Alcott wrote poems in the **19th century** (1800s). How many years are in 1 century?", "100 years", "10 years", "50 years", "500 years", "A", "1 century = 100 years."),
        ("If the little bird sings for **10 hours a day** for 7 days, how many total hours does it sing in a week?", "70 hours (10 x 7)", "50 hours", "60 hours", "100 hours", "A", "10 x 7 = 70 hours."),
        ("Solve the calendar puzzle: If 1st September was a Friday, what day of the week was 8th September?", "Friday", "Saturday", "Thursday", "Monday", "A", "1 + 7 = 8th September, landing on Friday."),
        ("Analyze this schedule: Bird sings in morning on Mon, Wed, Fri; Sings in evening on Tue, Thu, Sat. On which day does it rest?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If a bird observation project lasted a fortnight, how many days did it cover?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Jul, Aug, Oct, Sep, Nov'", "October and September are in wrong order.", "August is in wrong position.", "November should be first.", "No error.", "A", "September comes before October (Jul, Aug, Sep, Oct, Nov)."),
        ("September has **30 days**. What date was the day right after 30th September?", "1st October", "31st September", "29th September", "1st November", "A", "September has 30 days, so next day is 1st October."),
        ("If yesterday was two days before Saturday, what day is tomorrow?", "Saturday", "Friday", "Sunday", "Thursday", "A", "Two days before Saturday = Thursday (yesterday). Today = Friday. Tomorrow = Saturday."),
        ("Calculate: How many days are there in total during **September** and **October** combined?", "61 days (30 + 31)", "60 days", "62 days", "59 days", "A", "September (30) + October (31) = 61 days."),
        ("HOTS Reasoning: What does the phrase 'I sing the whole day long' mean metaphorically in the poem?", "It signifies constant, unwavering devotion and cheerfulness throughout all hours of life.", "It means the bird never sleeps.", "It means the cage is loud.", "It means night never comes.", "A", "Metaphor for unceasing devotion and positive attitude."),
        ("Identify the correct statement about a non-leap year:", "A non-leap year has 365 days and February has 28 days.", "A non-leap year has 366 days.", "February has 30 days.", "A non-leap year occurs every 4 years.", "A", "Standard year has 365 days (Feb = 28 days)."),
        ("The bird sang 60 songs in 3 hours. How many songs did it sing per hour on average?", "20 songs per hour", "10 songs", "30 songs", "15 songs", "A", "60 / 3 = 20 songs per hour."),
        ("Which month pair both have 31 days and come right after each other at the end of summer?", "July and August", "June and July", "August and September", "September and October", "A", "July (31) and August (31) are consecutive 31-day months.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH11_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 11: A Little Bird I Am\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("I **sit** and sing in my cage.", "sit", "little", "bird", "cage", "A", "'sit' is the physical action verb."),
        ("The little bird **sings** to Him who placed it there.", "sings", "little", "bird", "placed", "A", "'sings' is the main action verb."),
        ("God **placed** the bird in the cage.", "placed", "God", "bird", "cage", "A", "'placed' is the action verb."),
        ("The bird **pleases** God with its song.", "pleases", "bird", "God", "song", "A", "'pleases' is the action verb."),
        ("I **love** to please Him whom most I love.", "love", "please", "Him", "most", "A", "'love' is the emotional action verb."),
        ("God **doth listen** to my song.", "listen / doth listen", "God", "song", "my", "A", "'listen' is the action verb."),
        ("He **caught** my wandering wing.", "caught", "He", "wandering", "wing", "A", "'caught' is the physical action verb."),
        ("God **bound** my wandering wing.", "bound", "God", "wandering", "wing", "A", "'bound' is the physical action verb."),
        ("He **bends** to hear me sing.", "bends", "He", "hear", "sing", "A", "'bends' is the physical action verb."),
        ("God **hears** the bird's sweet melody.", "hears", "God", "bird's", "melody", "A", "'hears' is the sensory action verb."),
        ("The bird **flies** in the open sky in its memories.", "flies", "bird", "open", "sky", "A", "'flies' is the physical action verb."),
        ("Birds **chirp** happily on tree branches.", "chirp", "birds", "happily", "branches", "A", "'chirp' is the action verb."),
        ("The bird **accepts** its cage with joy.", "accepts", "bird", "cage", "joy", "A", "'accepts' is the action verb."),
        ("The little bird **praises** the Lord all day.", "praises", "bird", "Lord", "day", "A", "'praises' is the action verb."),
        ("Children **listen** to the bird's song.", "listen", "children", "bird's", "song", "A", "'listen' is the sensory action verb."),
        ("The bird **flaps** its wings gently.", "flaps", "bird", "wings", "gently", "A", "'flaps' is the physical action verb."),
        ("The song **echoes** through the room.", "echoes", "song", "through", "room", "A", "'echoes' is the action verb."),
        ("The bird **trusts** God completely.", "trusts", "bird", "God", "completely", "A", "'trusts' is the mental action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH11_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 11:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'The caged bird **happily** **sings** **sweet** **tunes**.'", "sings", "happily", "sweet", "tunes", "A", "'sings' shows action; 'happily' is adverb, 'sweet' is adjective, 'tunes' is noun."),
        ("Identify BOTH action verbs in: 'The bird **sits** in the cage and **sings** all day.'", "sits, sings", "bird, cage", "day, sits", "sings, cage", "A", "'sits' and 'sings' are both action verbs."),
        ("What is the old English action verb form of 'does' used in the poem ('Doth listen')?", "doth", "does", "doing", "did", "A", "'doth' is the archaic form of 'does'."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "I will **sing** a sweet song to God.", "The bird sang a beautiful **song**.", "I heard a joyful **song**.", "That is my favorite **song**.", "A", "In (A), 'sing' acts as the main action verb."),
        ("Find the action verb in: 'He bends to hear me sing.'", "bends / hear / sing", "He", "me", "there", "A", "'bends', 'hear', 'sing' are action verbs."),
        ("Which sentence contains NO physical action verb?", "A little bird I am.", "I sit and sing.", "He caught my wing.", "He bends to hear me.", "A", "'A little bird I am' contains linking verb 'am', but no physical action verb."),
        ("Change the action verb 'sing' to past tense: 'The bird (sing) a song yesterday.'", "sang", "singed", "singing", "sings", "A", "Past tense of sing is sang."),
        ("Identify the action verb: 'The bird sings and pleases God.'", "sings, pleases", "bird, God", "song, bird", "pleases, God", "A", "'sings' and 'pleases' are action verbs."),
        ("Select the action verb that completes the sentence: 'The bird ____ its devotion through music.'", "expresses / demonstrates", "sweet", "cage", "bird", "A", "'expresses' / 'demonstrates' is an action verb."),
        ("Which word is an action verb? (prisoner, cage, caught, little)", "caught", "prisoner", "cage", "little", "A", "'caught' is an action verb; others are nouns/adjectives."),
        ("What action does God perform when listening to the bird's song in the poem?", "bends / listens", "cage", "prisoner", "naught", "A", "God bends to listen (action verb)."),
        ("Identify the action verb in: 'The bird loves to please its Creator.'", "loves / please", "bird", "its", "Creator", "A", "'loves' and 'please' are action verbs."),
        ("Choose the correct action verb: 'God ____ the bird's wandering wing.'", "bound / caught", "sweet", "little", "cage", "A", "'bound' / 'caught' is the action verb."),
        ("Identify the action verb in: 'The bird sings the whole day long.'", "sings", "bird", "whole", "day", "A", "'sings' is the action verb."),
        ("Which of these words is NOT an action verb? (sing, listen, prisoner, bend)", "prisoner", "sing", "listen", "bend", "A", "'prisoner' is a noun; others are action verbs."),
        ("Identify the action verb in: 'The bird rests upon the wooden perch.'", "rests", "bird", "wooden", "perch", "A", "'rests' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The song ____ the hearts of listeners.'", "touches / warms", "sweet", "cage", "bird", "A", "'touches' / 'warms' is an action verb."),
        ("What action verb completes the sentence? 'The bird ____ contentment in its cage.'", "feels / finds", "happy", "cage", "little", "A", "'feels' / 'finds' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH11_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The captive bird sweetly sang and praised its Creator.' How many total ACTION VERBS are present?", "2 action verbs ('sang', 'praised')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'sang' and 'praised' are action verbs; 'sweetly', 'captive' are adverbs/adjectives."),
        ("Categorize the verbs: In 'The bird **is** a prisoner, but it **sings** gladly', classify 'is' and 'sings'.", "'is' is a linking verb; 'sings' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'is' is action; 'sings' is linking.", "A", "'is' links state of being; 'sings' shows action."),
        ("Replace the weak verb with a strong action verb: 'The bird **makes** music for God.'", "The bird **pours out** music for God.", "The bird **was near** God.", "The bird **saw** God.", "The bird **looked at** God.", "A", "'pours out' is a much stronger, poetic action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "The bird **sits** in the cage, **sings** praises, and **pleases** God.", "The bird is small, sweet, and caged.", "A little bird I am in a cage.", "It is pleased to be a prisoner.", "A", "sits, sings, pleases are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "The bird **sings** to Him who placed it there.", "The bird was **little**.", "The cage was **wooden**.", "The song was **sweet**.", "A", "'sings' is an action verb."),
        ("Spot the incorrect verb tense: 'The bird **sing** to God yesterday.' Correct it for past simple:", "'sang' is the past action verb form.", "'sing' should be 'singing'.", "'sing' should be 'sings'.", "'sing' should be 'will sing'.", "A", "Past simple of sing is sang."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (God places bird in cage, bird sits inside, bird sings praises, God listens)", "God places bird in cage -> bird sits inside -> bird sings praises -> God listens", "God listens -> bird sings praises -> bird sits inside -> God places bird", "bird sings praises -> God listens -> God places bird -> bird sits inside", "bird sits -> God listens -> God places -> bird sings", "A", "Chrono order: place in cage, sit, sing, listen."),
        ("Identify the verb error in dialogue: Bird said, 'I have **sing** for Thee all day!'", "'sing' is incorrect; the past participle form is 'sung' ('have sung').", "'sing' should be 'singing'.", "'sing' should be 'sings'.", "No error.", "A", "Perfect tense requires past participle 'sung'."),
        ("Analyze this sentence: 'The bird **transcends** its physical cage through spiritual song.' What type of action verb is 'transcends'?", "Abstract/spiritual action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'transcends' is an action verb describing spiritual elevation."),
        ("Which sentence uses action verbs to show cause and effect?", "The bird **sings** sweetly, so God **listens** with delight.", "The bird is little and the cage is wood.", "Louisa May Alcott wrote the poem.", "The fields of air are wide.", "A", "'sings' (cause action) -> 'listens' (effect action)."),
        ("Spot the missing action verb: 'The bird ____ its wings and ____ praises to God.'", "flaps, sings", "little, sweet", "was, was", "quick, slow", "A", "'flaps' and 'sings' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'surrenders' in 'The bird surrenders its freedom to God' considered a DEEP spiritual action verb?", "Because it describes actively accepting divine will over personal desires.", "Because surrendering requires climbing.", "Because bird is in cage.", "Because it is a noun.", "A", "Descriptive action verb conveying spiritual submission."),
        ("Transform the action verb to future tense: 'The bird **sings** tomorrow morning.'", "The bird **will sing** tomorrow morning.", "The bird **sang** tomorrow morning.", "The bird **is singing** tomorrow morning.", "The bird **sings** tomorrow morning.", "A", "'will sing' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The birds **sing** praises to God.", "The birds **sings** praises to God.", "A bird **sing** praises to God.", "The birds **is singing** praises to God.", "A", "Plural subject 'birds' takes base verb 'sing' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH11_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 11: A Little Bird I Am\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'A little bird I am__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'What does the bird like to do all day__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized when referring to God or Him in devotional poetry?", "First letter (e.g., God, Him, He, Thee)", "The last letter", "All letters", "No letters", "A", "Devotional references to God require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'The bird has feathers__ wings__ and a beak.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows deep emotion in: 'Because, my God, it pleases Thee!__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense emotion/devotion."),
        ("Select the proper noun (author's name) that MUST start with capital letters:", "Louisa May Alcott", "little bird", "cage", "song", "A", "'Louisa May Alcott' as author's name starts with capital letters."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'the poem was written by Louisa May Alcott.'", "the -> The", "written -> Written", "poem -> Poem", "by -> By", "A", "First word of sentence 'The' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'I sing the whole day long [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which divine name is capitalized correctly?", "God", "god", "gOd", "GOD", "A", "Capital letter for proper divine name God."),
        ("What mark goes after a speaker tag: 'The bird said__ \"I love to sing for Him!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'he said, \"i am a little bird.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The bird sits in the cage.", "The bird sits in the cage?", "The bird sits in the cage,", "The bird sits in the cage;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like 'the **bird's** song'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which poem title is capitalized correctly?", "A Little Bird I Am", "a little bird i am", "A little Bird i Am", "A LITTLE BIRD I AM", "A", "Title capitalization."),
        ("What punctuation mark is used around poem lines: '___A little bird I am___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Quotation marks enclose exact poem line quotes.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH11_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "The poem \"A Little Bird I Am\" was written by Louisa May Alcott.", "the poem \"a little bird i am\" was written by louisa may alcott.", "The poem \"a Little Bird I am\" was written by Louisa may Alcott?", "the Poem \"A Little Bird I Am\" Was Written By Louisa May Alcott.", "A", "Title \"A Little Bird I Am\", author Louisa May Alcott capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Why does the bird sing in its cage?", "Why does the bird sing in its cage.", "Why does the bird sing in its cage!", "Why does the bird sing in its cage,", "A", "Question starting with 'Why' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'the little bird sings to God all day.'", "'the' should be capitalized ('The'); 'God' is correct.", "'God' should be lowercase.", "'bird' should be uppercase.", "No mistake.", "A", "First word of sentence 'The' must be capitalized."),
        ("Choose the correctly punctuated dialogue sentence:", "\"I sing the whole day long,\" said the little bird.", "i sing the whole day long said the little bird.", "\"I sing the whole day long\" said the little bird", "I sing the whole day long, said the little bird.", "A", "Quotation marks around dialogue, comma inside quote, capital I."),
        ("Identify where a COMMA is missing: 'The bird has wings feathers and a sweet voice.'", "Between 'wings' and 'feathers' ('wings, feathers')", "After 'The'", "After 'voice'", "No comma needed", "A", "Commas separate items in list: 'wings, feathers and a sweet voice'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is the bird's sweet song.", "This is the birds' sweet song.", "This is the birds sweet song.", "This is the bird's' sweet song.", "A", "bird's indicates singular possession."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "Because, my God, it pleases Thee!", "Because, my God, it pleases Thee?", "Because, my God, it pleases Thee.", "Because, my God, it pleases Thee,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'cannot'?", "can't", "ca'nt", "cant'", "c'ant", "A", "can't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "Louisa May Alcott wrote a poem about a bird praised to God.", "louisa may alcott wrote a poem about a bird praised to god.", "Louisa May Alcott Wrote A Poem About A Bird Praised To God.", "louisa May Alcott wrote poem to God.", "A", "'Louisa May Alcott', 'God' capitalized as proper names."),
        ("What punctuation mark belongs in the blank? 'The bird sang, \"It pleases Thee__\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses emotion."),
        ("Choose the correct form for 'will not':", "won't", "wo'nt", "wont'", "w'ont", "A", "won't is standard contraction."),
        ("Identify the punctuation error: 'The bird is in a cage, it sings happily.'", "Comma splice between two independent clauses (should be full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for God and author:", "God listens to the bird in Louisa May Alcott's poem.", "god listens to the bird in louisa may alcott's poem.", "God listens to the bird in louisa May Alcott's poem.", "god Listens to the bird in Louisa may alcott's poem.", "A", "Names 'God', 'Louisa May Alcott' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "The bird's cage was placed near the window.", "The birds' cage was placed near the window.", "The birds cage was placed near the window.", "The bird's' cage was placed near the window.", "A", "bird's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'The poem mentions ____'", "cages, wings, and songs.", "cages wings and songs.", "cages; wings; and songs.", "cages: wings: and songs.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "Why is the bird pleased to be a prisoner?", "Why is the bird pleased to be a prisoner.", "Why is the bird pleased to be a prisoner!", "why is the bird pleased to be a prisoner.", "A", "Capital W, ends with question mark ?"),
        ("Fix the sentence: 'who wrote a little bird i am'", "Who wrote \"A Little Bird I Am\"?", "Who wrote a little bird i am.", "who wrote A Little Bird I Am!", "Where is Alcott?", "A", "Capital W, title quotes, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "The bird said, \"He bends to hear me sing!\"", "The bird said \"he bends to hear me sing!\"", "the bird said, \"He bends to hear me sing!\"", "The bird said, \"He bends to hear me sing.\"", "A", "Capital T, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH11_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on sunday louisa may alcott wrote a poem where the bird said, because my god it pleases thee'", "5 errors (on->On, sunday->Sunday, louisa may alcott->Louisa May Alcott, god->God, thee->Thee, quotation marks, exclamation mark)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, author name, divine capitalization, quotation marks, exclamation mark."),
        ("Correct the entire dialogue paragraph: 'the bird said why should i complain god replied i hear your song'", "\"Why should I complain?\" said the bird. God replied, \"I hear your song.\"", "the bird said \"why should i complain\" god replied \"i hear your song.\"", "The bird said, Why should I complain. God replied, I hear your song.", "\"Why should I complain?\" Said the bird. God replied \"I hear your song?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'The bird**'**s song is sweet, and it**'**s happy to sing.'", "First 's is possessive (song of the bird); second 's is contraction (it is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "bird's song = song of the bird; it's = it is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"I sing all day,\" Said the little bird.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'I' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "The bird is in a cage, but its spirit is free.", "The bird is in a cage but, its spirit is free.", "The bird is in a cage but its spirit is free!", "The bird is in a cage; but its spirit is free?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'louisa may alcott wrote a little bird i am on sunday 15th may 1880'", "Louisa May Alcott wrote \"A Little Bird I Am\" on Sunday, 15th May 1880.", "louisa may alcott wrote a little bird i am on sunday, 15th may 1880.", "Louisa May Alcott wrote A Little Bird I Am on Sunday 15th May 1880", "Louisa may alcott wrote A Little Bird I Am on sunday 15th may 1880.", "A", "Author name, title quotes, Sunday, 15th May 1880, period."),
        ("Identify why exclamation mark is necessary here: '\"Because, my God, it pleases Thee!\"'", "Because the speaker is expressing intense spiritual devotion and joy.", "Because bird is in cage.", "Because wing is bound.", "Because sentence is long.", "A", "Exclamation mark communicates intense spiritual devotion."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Louisa May Alcott, the famous author, wrote this poem.", "Louisa May Alcott the famous author wrote this poem.", "Louisa May Alcott, the famous author wrote this poem.", "Louisa May Alcott the famous author, wrote this poem.", "A", "Appositive phrase 'the famous author' is set off by commas."),
        ("Analyze the use of archaic spelling in poem text: 'Naught have I else to do...'", "Archaic word 'Naught' means 'nothing' in old English poetry.", "Naught replaces comma.", "Naught indicates question.", "Naught is a proper noun.", "A", "'Naught' is old English for 'nothing'."),
        ("Identify the correct sentence with direct speech quote within text:", "The poet wrote, \"I sing the whole day long,\" and we felt inspired.", "The poet wrote \"I sing the whole day long\" and we felt inspired.", "The poet wrote, 'I sing the whole day long,' and we felt inspired.", "The poet wrote: \"I sing the whole day long\" and we felt inspired.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The birds cage was hung near the window.'", "Missing apostrophe in 'bird's' -> 'The bird's cage...'", "Missing apostrophe in 'window''", "Missing apostrophe in 'hung''", "No apostrophe needed", "A", "'The bird's cage' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'God, said the bird, hears my song.' vs 'God said, \"The bird hears my song.\"'", "In the first, the bird says God hears its song; in the second, God says the bird hears His song.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who hears."),
        ("Correct all 4 errors in: 'whats the poems title asked the child'", "\"What's the poem's title?\" asked the child.", "whats the poems title? asked the child.", "\"What's the poems title.\" asked the child.", "\"whats the poems title?\" Asked the child.", "A", "Quotation marks, capital W, possessive poem's, question mark, period at end."),
        ("Identify the rule for capitalizing divine titles like 'the Creator' or 'the Almighty':", "Titles referring to God take initial capital letters.", "Divine titles are never capitalized.", "Divine titles are capitalized only at end of line.", "Divine titles must be written in ALL CAPS.", "A", "Proper divine titles take initial capitals.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH11_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 11: A Little Bird I Am\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'hear'** (in Chapter 11)?", "ea", "ee", "ai", "ou", "A", "'ea' is the vowel digraph in hear."),
        ("Identify the vowel digraph in the word **'please'**:", "ea", "ee", "oa", "ui", "A", "'ea' forms the long /e/ vowel sound in please."),
        ("Which word from the poem contains the **'ou'** vowel digraph?", "bound", "bird", "sing", "cage", "A", "'bound' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'clean'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in clean."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'ou'** vowel digraph: 'God bound my wandering wing.'", "bound", "wandering", "wing", "God", "A", "'bound' contains 'ou' vowel digraph."),
        ("Which word from the poem rhymes with **'air'**?", "there", "are", "arm", "art", "A", "'there' rhymes with 'air'."),
        ("Which word from the poem rhymes with **'sing'**?", "wing", "song", "sun", "sat", "A", "'wing' rhymes with 'sing'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the poem rhymes with **'long'**?", "song", "lone", "lung", "lane", "A", "'song' rhymes with 'long'."),
        ("Identify the vowel digraph in **'sweet'**:", "ee", "ea", "oo", "ui", "A", "'ee' makes long /e/ sound in sweet."),
        ("Which word from Chapter 11 has the **'ea'** digraph making a long /e/ sound?", "hear", "head", "heavy", "dead", "A", "'hear' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letters in **'caught'** (as in 'He caught my wing'):", "ugh", "c", "a", "t", "A", "Silent 'ugh' in caught."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "high", "bought", "bowl", "baker", "A", "'igh' in high makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They walked around the bird cage.'", "around", "cage", "bird", "they", "A", "'around' contains 'ou' digraph."),
        ("Which word rhymes with **'cage'**?", "page", "sat", "so", "seat", "A", "'page' rhymes with 'cage'."),
        ("Identify the silent letter in the word **'listen'** (as in 'doth listen'):", "t", "l", "i", "s", "A", "Silent 't' in listen.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH11_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'hear'** and **'bread'**. What is the difference?", "'hear' has long /e/ sound; 'bread' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'hear' has short /e/; 'bread' has long /e/.", "A", "'ea' can make long /e/ (hear) or short /e/ (bread)."),
        ("Select the word pair from Chapter 11 that has the SAME vowel digraph sound:", "hear - please", "air - bread", "bound - roar", "sing - sweet", "A", "'hear' (ea) and 'please' (ea) both make long /e/ sound."),
        ("Which word contains SILENT letters? (caught, bird, sing, cage)", "caught", "bird", "sing", "cage", "A", "'caught' has silent 'ugh'."),
        ("Identify the odd one out based on vowel sound: (hear, please, clean, bread)", "bread", "hear", "please", "clean", "A", "'bread' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for auditory perception? 'h__r'", "ea", "ee", "ai", "ou", "A", "'hear' uses 'ea' digraph."),
        ("Group these story words by digraph: **bound**, **out**, **around**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'He doth listen to my song.'", "doth", "listen", "song", "my", "A", "'doth' contains unvoiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (know, show, blow, all of these)", "all of these", "know", "show", "blow", "A", "know, show, blow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'please'**:", "ea", "ae", "ur", "or", "A", "'ea' is the vowel digraph in please."),
        ("Which word from the story has silent **'t'**? (listen, whistle, castle, all of these)", "all of these", "listen", "whistle", "castle", "A", "listen, whistle, castle all have silent 't'."),
        ("Select the rhyming pair from the poem: 'air' and ____.", "there", "bird", "cage", "sing", "A", "'air' rhymes with 'there' in the poem."),
        ("Select the rhyming pair from the poem: 'sing' and ____.", "wing", "song", "bird", "cage", "A", "'sing' rhymes with 'wing' in the poem."),
        ("Select the rhyming pair from the poem: 'long' and ____.", "song", "wing", "air", "there", "A", "'long' rhymes with 'song' in the poem."),
        ("Find the R-controlled vowel sound in: 'God created the **air** / **bird**.'", "er/ir sound in bird", "ea", "ou", "ai", "A", "R-controlled vowel in bird."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 11 vocabulary: (place, please, cage, place)", "place", "please", "cage", "place and cage", "A", "place (/s/ sound) has soft 'c' before 'e'."),
        ("Which word has a soft **'g'** sound? (cage, gentle, magic, all of these)", "all of these", "cage", "gentle", "magic", "A", "cage, gentle, magic all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ea'** digraph for listening:", "hear", "her", "here", "hier", "A", "hear is standard spelling with 'ea'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH11_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'place'** sound like /s/, but 'c' in **'cage'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound (place); before 'a', 'o', 'u' it makes hard /k/ sound (cage).", "Because place is wide.", "Because cage is iron.", "There is no rule.", "A", "Soft 'c' rule: c + e, i, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (hear, please, bread, heavy, lead [metal])", "Long /e/: hear, please; Short /e/: bread, heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: bread; Short /e/: hear", "A", "hear, please make long /e/; bread, heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "caught - listen", "bird - cage", "sing - wing", "air - song", "A", "'caught' (silent ugh) and 'listen' (silent t)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "spring / spread", "sing", "wing", "cage", "A", "'spr' blend type."),
        ("Examine the hard vs soft 'g' rule: Why is 'g' soft in **'cage'** but hard in **'God'**?", "'g' followed by 'e', 'i', or 'y' makes soft /j/ sound (cage); 'g' before 'o' or 'a','u' makes hard /g/ sound (God).", "Because cage is small.", "Because God is holy.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "caught", "bird", "sing", "cage", "A", "'caught' has vowel digraph 'au' and silent 'gh'."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'bound'**?", "bound - out", "voice - coin", "paid - day", "boat - coat", "A", "'bound' and 'out' share /ow/ diphthong sound."),
        ("Analyze homophones: 'The bird can **hear** / **here** the song.' Which word means listen to sound?", "hear", "here", "hier", "heare", "A", "'hear' (perceive sound) and 'here' (this location) are homophones."),
        ("Identify the phonic pattern in **'wandering'**: What vowel sound does the first 'a' make?", "Short /o/ or /ah/ sound", "Long /a/ sound", "Silent sound", "Short /u/ sound", "A", "'wan-der-ing' 'a' makes short /o/ sound (/wondring/)."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (cages, songs, wings, fields)", "songs / wings / fields", "cages", "nests", "bars", "A", "Plurals ending in voiced consonants take /z/ ending sound (songs, wings)."),
        ("Spot the word where 't' is SILENT: (listen, whistle, castle, all of these)", "all of these", "listen", "whistle", "castle", "A", "'t' is silent in listen, whistle, castle."),
        ("HOTS Reasoning: Why do 'hear' and 'here' sound identical but have different spellings and meanings?", "They are homophones (same sound, different spelling/meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share pronunciation but differ in spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "songbird / doorstep", "prisoner", "wandering", "pleases", "A", "songbird = song + bird."),
        ("Determine the syllable count and stress: How many syllables are in **'wandering'**?", "3 syllables (wan-der-ing)", "2 syllables", "4 syllables", "1 syllable", "A", "wan-der-ing has 3 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH11_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 11: A Little Bird I Am\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ does the speaker say it is in the first line of the poem?", "What", "Who", "Where", "Why", "A", "'What' asks about identity ('A little bird I am')."),
        ("___ is the little bird confined?", "Where", "Who", "What", "Why", "A", "'Where' asks about location ('in my cage')."),
        ("___ does the bird do in its cage all day long?", "What", "Who", "Where", "Why", "A", "'What' asks about activity ('sit and sing')."),
        ("___ does the bird sing to?", "Whom / Who", "What", "Where", "Why", "A", "'Whom' asks about recipient ('to Him who placed me there')."),
        ("___ placed the bird in the cage?", "Who", "What", "Where", "Why", "A", "'Who' asks about person/Creator (God / Him)."),
        ("___ is the bird pleased to be a prisoner?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason ('Because, my God, it pleases Thee!')."),
        ("___ long does the bird sing?", "How", "Who", "Where", "Why", "A", "'How long' asks about duration ('the whole day long')."),
        ("___ listens to the bird's song?", "Who", "What", "Where", "Why", "A", "'Who' asks about listener ('He whom most I love to please')."),
        ("___ did God catch and bind?", "What", "Who", "Where", "Why", "A", "'What' asks about object ('my wandering wing')."),
        ("___ wrote the poem 'A Little Bird I Am'?", "Who", "What", "Where", "Why", "A", "'Who' asks about author (Louisa May Alcott)."),
        ("___ does the word 'Thee' mean in old English?", "What", "Who", "Where", "Why", "A", "'What' asks about meaning ('You')."),
        ("___ does the word 'Naught' mean in the poem?", "What", "Who", "Where", "Why", "A", "'What' asks about meaning ('Nothing')."),
        ("___ does the word 'Doth' mean in the poem?", "What", "Who", "Where", "Why", "A", "'What' asks about meaning ('Does')."),
        ("___ attitude does the bird show toward being in a cage?", "What", "Who", "Where", "Why", "A", "'What attitude' asks about disposition (contentment, joy, devotion)."),
        ("___ does God do while the bird sings?", "What", "Who", "Where", "Why", "A", "'What' asks about action ('He bends to hear me sing')."),
        ("___ does the bird love to please most of all?", "Whom / Who", "What", "Where", "Why", "A", "'Whom' asks about God."),
        ("___ fields is the bird shut from?", "Which", "Who", "Where", "Why", "A", "'Which fields' asks about 'fields of air'."),
        ("___ quality makes the bird happy inside its cage?", "What / Which", "Who", "Where", "Why", "A", "'What quality' asks about devotion/faith.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH11_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ is the bird happy in its cage?' Answer: 'Because its confinement pleases God.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ is the bird kept?' Answer: 'In a cage, shut from fields of air.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for DURATION: '___ long does the bird sing every day?'", "How", "Where", "Who", "Why", "A", "'How long' inquires about duration ('the whole day long')."),
        ("Form an asking sentence: 'The bird sings to God.' -> '____ does the bird sing to?'", "Whom / Who", "What", "Why", "Where", "A", "'Whom' inquires about recipient."),
        ("Identify the INCORRECT question word usage: '**Why** wrote the poem A Little Bird I Am?'", "'Why' should be 'Who'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'Who wrote the poem...' asks for author identity."),
        ("Select the proper interrogative sentence:", "Why is the bird well pleased to be a prisoner?", "Why the bird is well pleased to be a prisoner?", "Why does the bird is pleased?", "Why bird pleased?", "A", "Interrogative word + auxiliary 'is' + subject + predicate."),
        ("Which question word asks about MANNER or METHOD? '___ does the bird express its love for God?'", "How", "Who", "What", "Where", "A", "'How' inquires about method/manner (by singing praises all day long)."),
        ("Complete the question: '___ of the poem's stanzas describes God listening to the song?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific stanzas (the second stanza)."),
        ("Change statement to question: 'The bird sits in a cage.' -> '____ does the bird sit?'", "Where", "Who", "Why", "What", "A", "'Where' asks for location."),
        ("Fill in the blank: '___ sweet is the bird's song?'", "How", "What", "Where", "Why", "A", "'How sweet' measures degree."),
        ("Identify the question word in: 'Whom does the bird love to please most?'", "Whom", "does", "bird", "please", "A", "'Whom' is the interrogative pronoun asking about God."),
        ("Choose the question that matches this answer: 'Because it pleases God.'", "Why is the bird pleased to be a prisoner?", "Where does the bird fly?", "Who built the cage?", "What is a wing?", "A", "'Why is the bird pleased...' matches answer starting with 'Because...'."),
        ("Fill in the blank: '___ old English word in the poem means nothing?'", "Which", "Who", "Why", "Where", "A", "'Which word' asks for identification (Naught)."),
        ("Complete: '___ lines are in each stanza of the poem?'", "How many", "How much", "Who", "Where", "A", "'How many' asks about countable quantity (lines)."),
        ("Select the correct question for: 'He caught and bound my wandering wing.'", "What did God do to the bird's wing?", "Where did the bird go?", "Why do birds eat seeds?", "Who is Louisa May Alcott?", "A", "'What did God do...' asks for action."),
        ("Which question word inquires about POSSESSION? '___ wing was bound by God?'", "Whose", "Who", "Where", "Why", "A", "'Whose wing' asks about ownership/subject."),
        ("Form question: 'The bird sings many songs.' -> '____ songs does the bird sing?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why does the bird sing in a cage.' Correct it:", "Why does the bird sing in a cage?", "Why does the bird sing in a cage!", "Why does the bird sing in a cage,", "Why does the bird sing in a cage;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH11_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why does the bird sing to Him who placed it there?' What is the syntax pattern?", "Question Word + Helping Verb (does) + Subject (the bird) + Main Verb (sing) + Prepositional Phrase + Relative Clause", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ songs' vs '___ devotion'", "'How many' for countable songs; 'How much' for uncountable devotion.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for songs; 'How many' for devotion.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where the bird sits in the poem?' Correct it:", "Where **does** the bird sit in the poem?", "Where the bird sit in the poem?", "Where sat the bird in the poem?", "Where do the bird sits in the poem?", "A", "Present simple questions require auxiliary 'does' before singular subject 'the bird' and base verb 'sit'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the poem's thematic progression?", "Where is the bird -> Why is it singing -> Who listens to its song -> How does it feel about confinement", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals setting, core action, divine audience, and inner attitude."),
        ("Transform the statement into a formal question: 'The bird finds spiritual freedom despite physical imprisonment.'", "How does the little bird achieve spiritual transcendence despite its physical imprisonment?", "Where is the cage?", "Who is Alcott?", "What is a wing?", "A", "Directly targets spiritual transcendence theme."),
        ("Analyze this ambiguous question: 'What does he do?' How can it be made precise?", "Add specific context: 'How does God respond when the caged bird sings its song of devotion?'", "Make it shorter: 'What he?'", "Change to: 'Where he?'", "Remove 'What'.", "A", "Adding specific context clarifies divine response."),
        ("Choose the correct question pair for dialogue: Child: '___ is the bird not sad in the cage?' Mother: '___ about reading how its song pleases God?'", "Why, How", "Who, Where", "Where, How", "When, Whose", "A", "Why (reason for lack of sadness), How about (suggestion)."),
        ("Spot the DOUBLE auxiliary error: 'Why does the bird sang in its cage?'", "'does' requires base verb 'sing', not past tense 'sang'.", "'does' should be 'is'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'does' must be followed by base form of verb ('sing')."),
        ("Reconstruct question from answer: Answer: 'The bird sings the whole day long to please God.'", "Question: 'Why and for how long does the bird sing?'", "Question: 'Where did they fly?'", "Question: 'Who bought the bird?'", "Question: 'Why is air cold?'", "A", "Targets purpose and duration."),
        ("Form indirect question: 'The child asked why the bird was happy in a cage.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ is contentment in all circumstances a powerful virtue taught in the poem?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the spiritual moral reason."),
        ("HOTS Reasoning: Why is 'Who' used for God/Him but 'Which' used when selecting from stanzas of the poem?", "'Who' is used for divine person/Creator; 'Which' is used when choosing from a defined limited set of poetic stanzas.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the stanzas...' selects from a defined group."),
        ("Correct all errors in: 'why does the bird sing to god in the poem'", "Why does the bird sing to God in the poem?", "Why does the bird sing to god in the poem.", "Whom does the bird sing to God?", "Why do the bird sing to God?", "A", "Capital W, capital G, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 11:", "How does Louisa May Alcott use the metaphor of a caged bird to illustrate true inner freedom and spiritual devotion?", "What does the bird do all day?", "Where is the bird?", "Who wrote the poem?", "A", "Asks student to evaluate poetic metaphor and spiritual theme.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH11_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 11: A Little Bird I Am\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The little bird is **sitting** in its cage.", "sitting", "bird", "is", "cage", "A", "'sitting' is verb + -ing form."),
        ("The bird is **singing** praises to God.", "singing", "bird", "is", "praises", "A", "'singing' is verb + -ing form."),
        ("God is **listening** to the bird's song.", "listening", "God", "is", "song", "A", "'listening' is verb + -ing form."),
        ("God is **bending** to hear the little bird.", "bending", "God", "is", "bird", "A", "'bending' is verb + -ing form."),
        ("The bird is **pleasing** its Creator through song.", "pleasing", "bird", "is", "Creator", "A", "'pleasing' is verb + -ing form."),
        ("The captive bird is **enjoying** its sweet music.", "enjoying", "bird", "is", "music", "A", "'enjoying' is verb + -ing form."),
        ("The sun is **shining** on the wooden cage.", "shining", "sun", "is", "cage", "A", "'shining' is verb + -ing form."),
        ("The bird is **staying** cheerful all day long.", "staying", "bird", "is", "cheerful", "A", "'staying' is verb + -ing form."),
        ("The bird is **flapping** its wings inside the cage.", "flapping", "bird", "is", "wings", "A", "'flapping' is verb + -ing form."),
        ("Children are **listening** to the bird's sweet voice.", "listening", "children", "are", "voice", "A", "'listening' is verb + -ing form."),
        ("The song is **echoing** through the quiet room.", "echoing", "song", "is", "room", "A", "'echoing' is verb + -ing form."),
        ("The bird is **feeling** happy despite the cage.", "feeling", "bird", "is", "happy", "A", "'feeling' is verb + -ing form."),
        ("The poet is **writing** a poem about contentment.", "writing", "poet", "is", "poem", "A", "'writing' is verb + -ing form."),
        ("The bird is **offering** its heart to God.", "offering", "bird", "is", "heart", "A", "'offering' is verb + -ing form."),
        ("The notes are **rising** up to heaven.", "rising", "notes", "are", "heaven", "A", "'rising' is verb + -ing form."),
        ("The bird is **trusting** in God's love.", "trusting", "bird", "is", "love", "A", "'trusting' is verb + -ing form."),
        ("The wind is **blowing** outside the window.", "blowing", "wind", "is", "window", "A", "'blowing' is verb + -ing form."),
        ("The bird is **living** peacefully in its cage.", "living", "bird", "is", "cage", "A", "'living' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH11_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'sit'**? (The bird is ____ in the cage.)", "sitting (double final consonant)", "siting", "sittting", "siteing", "A", "CVC rule: double final consonant before -ing (sitting)."),
        ("What is the correct -ing spelling rule for **'sing'**? (The bird is ____.)", "singing (add -ing)", "singging", "singeing", "singng", "A", "Regular verb adding -ing (singing)."),
        ("What is the correct -ing spelling rule for **'please'**? (The song is ____ God.)", "pleasing (drop final silent e)", "pleaseing", "pleasving", "pleasng", "A", "Drop final silent 'e' before adding -ing (pleasing)."),
        ("Fill in the blank with present continuous form: 'The bird (sing) ____ a song right now.'", "is singing", "was sing", "are sing", "is singed", "A", "Singular subject takes 'is singing'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The bird is singing to God right now.", "The bird sang to God yesterday.", "The bird will sing to God tomorrow.", "The bird sang yesterday.", "A", "'is singing' is present continuous."),
        ("Fill in the blanks: 'The bird ____ (sit) on the perch and ____ (sing) praises.'", "is sitting, is singing", "are sitting, are singing", "is sit, is sing", "was sitting, were singing", "A", "Singular 'bird' takes 'is sitting' and 'is singing'."),
        ("Identify the spelling mistake in: 'The bird is **siting** in the cage.'", "'siting' should be 'sitting'", "'siting' should be 'sitting'", "'is' should be 'are'", "No mistake", "A", "Sit doubles final t before -ing (sitting)."),
        ("Select the correct -ing form for **'write'**:", "writing", "writeing", "writting", "writng", "A", "Drop silent 'e': write -> writing."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "Listen! The bird is singing a sweet melody.", "The bird sang a sweet melody yesterday.", "The bird sings every morning.", "The bird will sing tomorrow.", "A", "Present continuous ('is singing') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (read) Louisa May Alcott's poem.'", "am reading", "is reading", "are reading", "am readeing", "A", "Subject 'I' takes 'am reading'."),
        ("Choose the correct form: 'God ____ (listening) to the bird's prayer.'", "is listening", "are listening", "am listening", "is listen", "A", "Singular subject 'God' takes 'is listening'."),
        ("Identify the verb in: 'Why are you singing in the cage?'", "are singing", "Why", "you", "cage", "A", "Helping verb 'are' + main verb 'singing' form present continuous."),
        ("What is the -ing form of **'bend'**?", "bending", "bendding", "bendeing", "bendng", "A", "Regular verb adding -ing (bending)."),
        ("What is the -ing form of **'fly'**?", "flying", "flyying", "flieing", "flyng", "A", "Vowel+y verb adding -ing (flying)."),
        ("Change simple present to continuous: 'The bird sings.' -> 'The bird ____.'", "is singing", "sang", "was singing", "will sing", "A", "is singing."),
        ("Fill in the blank: 'The notes ____ (rising) to heaven.'", "are rising", "is rising", "am rising", "rised", "A", "Plural subject 'notes' takes 'are rising'."),
        ("Identify the correct present continuous sentence:", "Look! God is bending to hear the bird.", "Look! God bends to hear the bird.", "Look! God bent to hear the bird.", "Look! God bending to hear the bird.", "A", "Exclamation 'Look!' introduces action happening now ('is bending')."),
        ("Select the correct -ing form for **'hear'**:", "hearing", "heareing", "hearring", "hearng", "A", "Regular verb adding -ing (hearing).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH11_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (sit, please, sing)", "sit -> sitting (double consonant), please -> pleasing (drop e), sing -> singing (add -ing)", "All just add -ing.", "All double the last letter.", "sit -> siting, please -> pleaseing, sing -> singging", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'The bird sat while God listened.'", "The bird is sitting while God is listening.", "The bird sitting while God listening.", "The bird was sitting while God listened.", "The bird will sit while God listens.", "A", "Both verbs transformed to present continuous (is sitting, is listening)."),
        ("Spot the missing auxiliary verb in: 'The bird singing and God listening.' Correct it:", "'The bird **is** singing and God **is** listening.'", "'The bird singing and God listening.'", "'The bird **are** singing and God **are** listening.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'The bird is **loving** God' when expressing deep faith?", "Because 'love' as an emotional state is a stative verb, preferring simple present 'loves'.", "Because 'loving' is hard to spell.", "Because bird is in cage.", "Because wing is bound.", "A", "Stative verbs (love, trust, believe) prefer simple present."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The birds of the forest are singing loudly.", "The birds of the forest is singing loudly.", "The birds of the forest am singing loudly.", "The birds of the forest singing loudly.", "A", "Plural subject ('birds') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'The bird is complaining about its cage.' -> Negative:", "The bird is **not** complaining about its cage.", "The bird not complaining about its cage.", "The bird are no complaining about its cage.", "The bird isn't complain about its cage.", "A", "Add 'not' between auxiliary 'is' and main verb 'complaining'."),
        ("Spot all THREE spelling errors: 'She is **siting** near cage, **runing** away, and **dieing** of joy.'", "'siting' -> 'sitting'; 'runing' -> 'running'; 'dieing' -> 'dying'", "'siting' -> 'siting'; 'runing' -> 'runing'; 'dieing' -> 'dieing'", "No errors.", "Only 'runing' is wrong.", "A", "sitting (double t), running (double n), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'The little bird is singing praises.'", "**Is** the little bird singing praises?", "Are the little bird singing praises?", "The little bird singing praises?", "Why the little bird is singing praises?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The choir **is performing** the poem tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While the bird is singing, God is listening.", "While bird sang, God is listening.", "Bird is singing while God listened.", "Bird sing while God listen.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'The bird is singging in the cage.'", "'singging' should be 'singing' (single 'g').", "'is' should be 'are'.", "'cage' should be capitalized.", "No error.", "A", "Sing + ing = singing."),
        ("HOTS Reasoning: Compare 'The bird sang' (Past Simple) vs 'The bird is singing' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means song stopped.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the bird ____ (singing) in the cage?'", "is, singing", "are, singing", "am, singing", "do, singing", "A", "Singular subject bird takes 'is ... singing'."),
        ("Identify the correct present continuous sentence describing devotional expression:", "The little bird is pouring out its heart in song.", "The little bird is pour out its heart in song.", "The little bird are pouring out its heart in song.", "The little bird pouring out its heart in song.", "A", "Singular subject 'little bird' + is + pouring.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH11_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 11: A Little Bird I Am\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("A little bird I ___, shut from the fields of air.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am' ('A little bird I am')."),
        ("The bird ___ in a cage.", "is", "are", "am", "be", "A", "Singular subject 'The bird' takes 'is'."),
        ("I ___ happy to please God.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The cage ___ made of wood and iron.", "is", "are", "am", "be", "A", "Singular subject 'cage' takes 'is'."),
        ("The wings ___ bound by God.", "are", "is", "am", "be", "A", "Plural subject 'wings' takes 'are'."),
        ("God ___ listening to the bird's song.", "is", "are", "am", "be", "A", "Singular subject 'God' takes 'is'."),
        ("The songs ___ sweet and full of devotion.", "are", "is", "am", "be", "A", "Plural subject 'songs' takes 'are'."),
        ("Louisa May Alcott ___ the author of this poem.", "is", "are", "am", "be", "A", "Singular subject takes 'is'."),
        ("I ___ singing the whole day long.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The prisoner ___ content with its lot.", "is", "are", "am", "be", "A", "Singular 'prisoner' takes 'is'."),
        ("The bars of the cage ___ strong.", "are", "is", "am", "be", "A", "Plural 'bars' takes 'are'."),
        ("The bird ___ pleased because it pleases God.", "is", "are", "am", "be", "A", "Singular 'bird' takes 'is'."),
        ("You ___ reading a beautiful poem.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The poet ___ expressing spiritual contentment.", "is", "are", "am", "be", "A", "Singular 'poet' takes 'is'."),
        ("The birds ___ singing on the trees outside.", "are", "is", "am", "be", "A", "Plural 'birds' takes 'are'."),
        ("I ___ grateful for all my blessings.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The melody ___ uplifting and peaceful.", "is", "are", "am", "be", "A", "Singular 'melody' takes 'is'."),
        ("The notes of the song ___ rising to heaven.", "are", "is", "am", "be", "A", "Plural 'notes' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH11_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'The bird and its cage ____ part of the poem's imagery.'", "are", "is", "am", "be", "A", "Compound subject ('The bird and its cage') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "A little bird I am.", "A little bird I is.", "A little bird I are.", "A little bird I be.", "A", "First line of poem uses correct 'I am'."),
        ("Fill in the blanks: 'I ____ singing, and the bird ____ listening.'", "am, is", "is, is", "are, is", "am, are", "A", "'I am', 'the bird is'."),
        ("Identify the mistake in: 'The songs of the bird **is** sweet.'", "'is' should be 'are' because 'songs' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'songs' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you inspired by the bird's faith?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither cage nor bars ____ dimming the bird's joy.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject 'bars' treated as singular concept/nearer subject 'bars' (or plural) -> 'is' for singular concept 'bars' or 'are'. Here singular second subject 'noise/bar' takes 'is'."),
        ("Select the correct sentence for poem moral:", "Faith and contentment are powerful virtues.", "Faith and contentment is powerful virtues.", "Faith and contentment am powerful virtues.", "Faith and contentment be powerful virtues.", "A", "Compound subject 'Faith and contentment' takes 'are'."),
        ("Complete the conversation: Child: 'Where ____ the bird?' Mother: 'It ____ in the cage!'", "is, is", "are, are", "is, are", "are, is", "A", "Singular 'the bird' -> is; singular 'It' -> is."),
        ("Identify where 'is' is used incorrectly:", "The wings **is** bound.", "The bird is small.", "The cage is wooden.", "God is listening.", "A", "'The wings is' should be 'The wings are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The flock of birds ____ flying home.'", "is", "are", "am", "be", "A", "Collective noun 'flock' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The song of the bird ____ pleasing to God.'", "is", "are", "am", "be", "A", "Singular 'song' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am a little bird shut from the fields of air.", "I is a little bird shut from the fields of air.", "I are a little bird shut from the fields of air.", "I be a little bird shut from the fields of air.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many lessons in this short poem.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many lessons'."),
        ("Fill in the blank: 'There ____ a sweet message of faith in line 6.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a sweet message'."),
        ("Choose the correct sentence:", "What are the birds doing in their cages?", "What is the birds doing in their cages?", "What am the birds doing in their cages?", "What be the birds doing in their cages?", "A", "Plural subject 'the birds' takes 'are'."),
        ("Identify the correct form: 'The bird, as well as its song, ____ dedicated to God.'", "is", "are", "am", "be", "A", "Subject is singular 'The bird' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both love and devotion ____ expressed in the poem.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The bird ____ small, but its faith ____ great.'", "is, is", "are, is", "am, are", "is, are", "A", "'bird is', 'faith is'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH11_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the bird's songs **____** sung for God.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'songs' is plural.", "am — because it refers to speaker.", "be — because songs are sweet.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A choir of little birds **are** singing in the garden.'", "'are' should be 'is' because the subject is singular noun 'choir'.", "'are' should be 'am'.", "'birds' should be 'bird'.", "No error.", "A", "'A choir' is singular, so it requires 'is singing'."),
        ("Compare: (1) 'The bird and its song **are** sweet.' vs (2) 'The bird, along with its song, **is** sweet.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving 'The bird' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone who reads the poem **____** moved by the bird's faith.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The wings **is** bound, I **is** singing, and the songs **is** sweet.'", "'wings is' -> 'wings are'; 'I is' -> 'I am'; 'songs is' -> 'songs are'", "'wings is' -> 'wings am'; 'I is' -> 'I are'; 'songs is' -> 'songs am'", "Only 'I is' is wrong.", "No errors present.", "A", "wings are (plural), I am (1st person), songs are (plural)."),
        ("Fill in the blanks in this complex sentence: 'Not only the cage but also the bars **____** surrounding the bird, while God **____** listening.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer plural subject ('bars' -> are); 'God' -> is."),
        ("Transform to negative: 'A little bird I am.'", "A little bird I **am not**.", "A little bird I is not.", "A little bird I are not.", "A little bird I no am.", "A", "Add 'not' after 1st person helping verb 'am'."),
        ("Analyze inverted subject position: 'Inside the small cage **____** sitting a little bird.'", "is", "are", "am", "be", "A", "Subject is singular 'a little bird', appearing after verb, requiring 'is'."),
        ("Determine agreement with uncountable nouns: 'The music from the bird's song **____** filling the room.'", "is", "are", "am", "be", "A", "Uncountable noun 'music' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the lyrics of the poem you asked for.'", "Here **are** the lyrics of the poem you asked for.", "Here am the lyrics of the poem you asked for.", "Here be the lyrics of the poem you asked for.", "No error.", "A", "Plural subject 'lyrics' requires 'Here are...''"),
        ("Identify the sentence where 'am' acts as a MAIN linking verb rather than a helping verb:", "A little bird I **am**.", "I **am** singing a song.", "I **am** listening to the bird.", "I **am** reading Alcott's poem.", "A", "In 'A little bird I am', 'am' is the main linking verb connecting subject I to predicate noun a little bird."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because bird is small.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither physical cage nor bound wings **____** stopping the song, because faith **____** strong.'", "are, is", "is, are", "is, is", "are, are", "A", "'bound wings' is closer plural subject -> are; 'faith' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "A little bird I am, the cage is small, and its songs are sweet.", "A little bird I is, the cage are small, and its songs is sweet.", "A little bird I are, the cage am small, and its songs am sweet.", "A little bird I am, the cage is small, and its songs is sweet.", "A", "I am (1st person), cage is (singular), songs are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH11_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 11
# ---------------------------------------------------------------------------
def rebuild_chapter_11():
    print("Rebuilding Chapter 11 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH11_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 11 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_11()
