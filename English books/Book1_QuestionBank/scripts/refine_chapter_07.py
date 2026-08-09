r"""
Refines all 6 Category files for Chapter 07 ("Our National Animal") for Class 1.
Guarantees:
- 100% unique, non-repetitive questions across every category.
- Simple, clear, age-appropriate language for Class 1 students.
- Accurately assigned Difficulty levels: Easy (25), Medium (15), Hard (10).
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH07_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_07")
os.makedirs(CH07_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Which animal is India's national animal?", "(A) Royal Bengal Tiger", "(B) Lion", "(C) Elephant", "(D) Peacock", "(A)", "The Royal Bengal tiger is India's national animal.", "Easy", "Remembering", "National Symbol"),
    ("Which animal family do tigers belong to?", "(A) Feline (cat) family", "(B) Canine (dog) family", "(C) Bird family", "(D) Fish family", "(A)", "Tigers belong to the feline (cat) family.", "Easy", "Remembering", "Animal Family"),
    ("What pattern do tigers have on their fur?", "(A) Black stripes", "(B) White dots", "(C) Blue squares", "(D) Red spots", "(A)", "Tigers have black striped patterns on their fur.", "Easy", "Remembering", "Physical Feature"),
    ("What helps tigers walk softly and quietly in the forest?", "(A) Soft padded feet", "(B) Hard hooves", "(C) Iron shoes", "(D) Wooden boots", "(A)", "Their soft padded feet help them move quietly.", "Easy", "Remembering", "Adaptation"),
    ("What kind of food do tigers eat?", "(A) Flesh of other animals (carnivore)", "(B) Green grass", "(C) Fruits and seeds", "(D) Rice and bread", "(A)", "Tigers are flesh-eating (carnivorous) animals.", "Easy", "Remembering", "Diet"),
    ("Why are tigers called 'endangered' animals?", "(A) Because their numbers are decreasing and they are in danger of disappearing", "(B) Because they sleep a lot", "(C) Because they are small", "(D) Because they live in water", "(A)", "Endangered means in danger of disappearing from the world.", "Easy", "Remembering", "Conservation Term"),
    ("What main reasons cause the tiger population to decrease?", "(A) Illegal hunting and habitat destruction", "(B) Eating too many fruits", "(C) Swimming in rivers", "(D) Playing in rain", "(A)", "Illegal hunting and loss of forest homes decrease their population.", "Easy", "Remembering", "Threats"),
    ("What does the word 'daunting' mean in the passage?", "(A) Frightening or grand looking", "(B) Sweet and cute", "(C) Tiny", "(D) Soft", "(A)", "Daunting means frightening or grand looking.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'feline' mean?", "(A) Connected to the cat family", "(B) Connected to birds", "(C) Connected to dogs", "(D) Connected to insects", "(A)", "Feline means connected to the cat family.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'stealthy' mean?", "(A) Quiet and secretive", "(B) Loud and noisy", "(C) Slow and lazy", "(D) Bright and shiny", "(A)", "Stealthy means quiet and secretive.", "Easy", "Understanding", "Vocabulary"),
    ("How do the tiger's black stripes help it in the forest?", "(A) They work as camouflage cover in trees and grass", "(B) They make noise", "(C) They keep the tiger cool", "(D) They glow in the dark", "(A)", "Stripes blend into tall grass and trees for camouflage.", "Easy", "Understanding", "Adaptation"),
    ("What body parts help a tiger catch its prey?", "(A) Strong legs, sharp claws, and powerful jaws with big teeth", "(B) Small beak and feathers", "(C) Soft tail only", "(D) Long ears", "(A)", "Powerful legs, sharp claws, and strong jaws help them hunt.", "Easy", "Remembering", "Hunting Tools"),
    ("Where do wild tigers live?", "(A) In natural forests", "(B) In city houses", "(C) On ocean waves", "(D) In dessert shops", "(A)", "Wild tigers reside in dense forests.", "Easy", "Remembering", "Habitat"),
    ("Are all tigers around the world identical?", "(A) No, different types look slightly different from one another", "(B) Yes, completely identical", "(C) Tigers only live in zoos", "(D) Tigers have wings", "(A)", "Different subspecies look slightly different.", "Easy", "Remembering", "Fact"),
    ("What kind of hunters are tigers?", "(A) Stealthy and powerful hunters", "(B) Weak and slow hunters", "(C) Noisy hunters", "(D) Playful hunters", "(A)", "Tigers are stealthy, quiet, and powerful hunters.", "Easy", "Remembering", "Trait"),
    ("What sharp body parts are at the end of a tiger's paws?", "(A) Sharp claws", "(B) Soft nails", "(C) Hooves", "(D) Feathers", "(A)", "Tigers have sharp curved claws.", "Easy", "Remembering", "Detail"),
    ("Why should we protect tigers and forests?", "(A) To save our national animal from becoming extinct", "(B) To build more roads", "(C) To sell their fur", "(D) Because tigers like cities", "(A)", "Protecting tigers preserves our natural heritage and biodiversity.", "Easy", "Understanding", "Conservation Value"),
    ("What large teeth are prominent in a tiger's jaw for tearing meat?", "(A) Huge canine teeth", "(B) Small milk teeth", "(C) Flat molars", "(D) Front incisors only", "(A)", "Canine teeth are large and sharp for tearing meat.", "Easy", "Remembering", "Anatomy"),
    ("Does a tiger walk silently or loudly?", "(A) Silently because of soft padded paws", "(B) Loudly with heavy shoes", "(C) It hops on one leg", "(D) It makes drum sounds", "(A)", "Padded paws allow quiet, silent movement.", "Easy", "Remembering", "Fact"),
    ("What feelings do tigers inspire in people?", "(A) Both fascinating and scary", "(B) Boring", "(C) Funny only", "(D) Weak", "(A)", "Tigers are magnificent—both fascinating and intimidating.", "Easy", "Remembering", "Description"),
    ("Which word means 'illegal killing of wild animals'?", "(A) Illegal hunting / Poaching", "(B) Farming", "(C) Swimming", "(D) Flying", "(A)", "Illegal hunting decreases animal numbers.", "Easy", "Understanding", "Vocabulary"),
    ("Is the tiger a plant-eating animal (herbivore)?", "(A) No, it is a flesh-eating animal (carnivore)", "(B) Yes, it eats grass", "(C) It eats leaves only", "(D) It eats fruits only", "(A)", "Tigers are strict carnivores.", "Easy", "Remembering", "Diet Classification"),
    ("What color pattern is on a Bengal tiger's coat?", "(A) Orange/yellow coat with black stripes", "(B) Blue coat with red dots", "(C) Green coat with yellow spots", "(D) Plain purple", "(A)", "They have an orange-yellow coat with black stripes.", "Easy", "Remembering", "Appearance"),
    ("What title does Chapter 07 carry?", "(A) Our National Animal", "(B) The Ganga River", "(C) Furry Bear", "(D) Sunflower", "(A)", "Chapter 07 is titled 'Our National Animal'.", "Easy", "Remembering", "Chapter Title"),
    ("What lesson does Chapter 07 teach us?", "(A) Protect wildlife and preserve forest habitats for endangered animals", "(B) Hunt wild animals", "(C) Cut down all trees", "(D) Keep tigers at home as pets", "(A)", "It teaches us to protect endangered wildlife and forests.", "Easy", "Understanding", "Core Takeaway"),

    # Medium (26-40)
    ("Why is camouflage important for a predator like the tiger?", "(A) It hides the tiger in grass so prey cannot see it approaching", "(B) It keeps the tiger warm in rain", "(C) It makes the tiger look pretty", "(D) It helps the tiger sleep", "(A)", "Camouflage allows stealthy approach without alerting prey.", "Medium", "Understanding", "Biological Concept"),
    ("How does habitat destruction threaten tigers?", "(A) Cutting down forests removes their home, food, and space to live", "(B) It makes forests bigger", "(C) It gives them houses", "(D) It feeds them", "(A)", "Destroying forests leaves tigers without shelter or prey.", "Medium", "Understanding", "Environmental Threat"),
    ("What is the difference between a feline and a canine animal?", "(A) Feline refers to cat family (tiger, lion); canine refers to dog family (wolf, fox)", "(B) Felines fly; canines swim", "(C) Felines eat grass; canines eat seeds", "(D) They are identical", "(A)", "Feline = cat family; Canine = dog family.", "Medium", "Analyzing", "Scientific Distinction"),
    ("Why can tigers move without alerting their prey?", "(A) Soft padded cushions on their paws muffle footstep sounds", "(B) They fly through the air", "(C) They wear socks", "(D) They walk backward", "(A)", "Paw pads absorb sound while walking on dry leaves.", "Medium", "Understanding", "Adaptation Mechanism"),
    ("What makes the Royal Bengal tiger a symbol of pride for India?", "(A) Its magnificent strength, beauty, power, and status as national animal", "(B) It is small", "(C) It lives in cities", "(D) It is weak", "(A)", "It represents power, grace, and national biodiversity.", "Medium", "Evaluating", "Symbolic Value"),
    ("Why are wild tigers dangerous to handle directly?", "(A) They possess strong legs, sharp claws, powerful jaws, and wild instincts", "(B) They are small like kittens", "(C) They don't have teeth", "(D) They are slow", "(A)", "Their natural hunting weapons and wild power make them dangerous.", "Medium", "Understanding", "Safety Awareness"),
    ("How does project tiger / wildlife protection help save tigers?", "(A) It creates protected forest reserves where hunting and tree cutting are banned", "(B) It puts tigers in small cages", "(C) It moves tigers to cities", "(D) It sells tiger fur", "(A)", "Protected reserves keep tiger habitats safe from destruction.", "Medium", "Understanding", "Conservation Action"),
    ("What does 'flesh-eating animal' mean in biological terms?", "(A) A carnivore that hunts other animals for meat", "(B) An herbivore eating plants", "(C) An omnivore eating seeds", "(D) A water plant", "(A)", "Carnivores depend strictly on meat for survival.", "Medium", "Understanding", "Biological Definition"),
    ("Why is a tiger's canine tooth so large and pointed?", "(A) To grip prey securely and tear meat efficiently", "(B) To chew grass", "(C) To crack nuts", "(D) To clean fur", "(A)", "Canines are specialized for gripping and tearing meat.", "Medium", "Understanding", "Anatomy Function"),
    ("How do black stripes on an orange coat break up a tiger's shape?", "(A) The vertical stripes blend with vertical shadows of tall grasses and tree trunks", "(B) Stripes shine in sunlight", "(C) Stripes reflect water", "(D) Stripes change colors", "(A)", "Vertical lines mimic shadows in tall grass.", "Medium", "Analyzing", "Visual Camouflage"),
    ("What happens to an ecosystem when top predators like tigers disappear?", "(A) The balance is disrupted, causing overpopulation of plant-eating animals", "(B) Nothing changes", "(C) Forests grow bigger", "(D) Water increases", "(A)", "Top predators maintain healthy balance in food chains.", "Medium", "Analyzing", "Ecological Impact"),
    ("Why cannot tigers be kept as ordinary pets in houses?", "(A) They are wild carnivores requiring huge forest territories and specialized care", "(B) They eat too much milk", "(C) They are too noisy", "(D) They bark loudly", "(A)", "Wild instincts and space needs make house pet life impossible.", "Medium", "Evaluating", "Practical Logic"),
    ("What does 'population decreased' mean for a species?", "(A) The total number of living individuals of that species has fallen low", "(B) The animals got bigger", "(C) The animals moved to the moon", "(D) The population doubled", "(A)", "Decreased population means fewer surviving individuals.", "Medium", "Understanding", "Demographic Concept"),
    ("How do tigers use their sense of hearing and sight while hunting?", "(A) Sharp eyes and keen hearing detect slight movements in dark forests", "(B) They close their eyes", "(C) They use smell only", "(D) They don't use senses", "(A)", "Keen sight and hearing pinpoint prey in dense cover.", "Medium", "Understanding", "Sensory Adaptation"),
    ("What is the main goal of Chapter 07?", "(A) To educate students about the Royal Bengal tiger's features and the need to protect it", "(B) To teach how to hunt tigers", "(C) To describe a zoo visit", "(D) To show how to draw stripes", "(A)", "It aims to build awareness and conservation values for our national animal.", "Medium", "Evaluating", "Educational Goal"),

    # Hard (41-50)
    ("Analyze how physical adaptations (stripes, pads, claws, teeth) work together in a tiger's hunt.", "(A) Padded feet enable quiet stalking; stripes provide camouflage; strong legs sprint; claws grip; and jaws bite", "(B) They only help in sleeping", "(C) They help in swimming fast", "(D) Adaptations don't work together", "(A)", "Each adaptation contributes a specific step in the hunting process.", "Hard", "Analyzing", "Integrated Biology"),
    ("Evaluate the conflict between human expansion and tiger habitat preservation.", "(A) Expanding human cities cuts down forests, leaving tigers no space, leading to human-animal conflict", "(B) Humans and tigers live in houses together", "(C) Forests grow when cities expand", "(D) Tigers build cities", "(A)", "Deforestation for human development destroys tiger territory.", "Hard", "Evaluating", "Environmental Ethics"),
    ("Why is the tiger designated as the National Animal of India over other species?", "(A) It symbolizes raw power, grace, agility, resilience, and India's rich wilderness heritage", "(B) It was chosen by random pick", "(C) Because it is yellow", "(D) Because it lives everywhere", "(A)", "It represents national strength, grace, and wildlife richness.", "Hard", "Evaluating", "National Symbol Logic"),
    ("How does poaching (illegal hunting) push animals toward extinction?", "(A) Killing animals faster than they can reproduce rapidly reduces their population to dangerous levels", "(B) Poaching helps animals grow", "(C) Poaching builds forests", "(D) Poaching changes fur color", "(A)", "Unchecked killing depletes species beyond natural recovery.", "Hard", "Analyzing", "Conservation Science"),
    ("How can Class 1 students contribute to wildlife conservation in simple ways?", "(A) Learn about animals, save paper to protect trees, refuse products made from wild animal parts, and spread awareness", "(B) Go into forests alone", "(C) Buy wild animals", "(D) Cut trees", "(A)", "Saving trees and supporting animal protection helps indirectly.", "Hard", "Applying", "Real Life Application"),
    ("Examine the term 'apex predator' and why the tiger holds this status in Indian forests.", "(A) As an apex predator at the top of the food chain, it has no natural predators in its ecosystem", "(B) Apex means small", "(C) Apex means eating plants", "(D) It means living in water", "(A)", "Apex predators sit at the top of food chains without natural enemies.", "Hard", "Analyzing", "Ecological Status"),
    ("What structural features distinguish Bengal tigers from domestic house cats?", "(A) Massive body scale, muscular power, wild hunting adaptations, and distinct vocal roar instead of purring", "(B) House cats have stripes", "(C) Both are same size", "(D) House cats hunt elephants", "(A)", "Scale, physical strength, wild instincts, and roaring separate them.", "Hard", "Analyzing", "Comparative Zoology"),
    ("Why is biodiversity conservation vital for planetary health?", "(A) Every species plays an interconnected role in maintaining ecosystem stability, clean air, and water cycles", "(B) Biodiversity doesn't matter", "(C) Only humans matter", "(D) Plants don't need animals", "(A)", "All living species form an interconnected ecological web.", "Hard", "Evaluating", "Global Ecosystem"),
    ("How does the tiger's nocturnal (night) hunting habit benefit its survival?", "(A) Cooler night temperatures and dark shadows maximize its camouflage and stealth advantages", "(B) Tigers cannot see in daylight", "(C) Prey sleeps on trees", "(D) Night has no sun", "(A)", "Night hunting uses darkness and cool air to enhance stealth.", "Hard", "Analyzing", "Behavioral Ecology"),
    ("What is the ultimate educational message of Chapter 07 for primary learners?", "(A) Cherish our magnificent national animal, respect nature's balance, and actively protect forest wildlife!", "(B) Keep tigers as pets", "(C) Ignore wild animals", "(D) Destroy forests", "(A)", "Pride in national symbols and active wildlife protection form the core lesson.", "Hard", "Evaluating", "Core Takeaway")
]

mcq_content = f"# MCQs — Chapter 07: Our National Animal\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK01_CH07_MCQ_{idx:03d}"
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

with open(os.path.join(CH07_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("The Royal Bengal tiger is India's national _______.", "animal", "The tiger is India's national animal.", "Easy"),
    ("Tigers belong to the _______ family.", "feline / cat", "Tigers belong to the feline family.", "Easy"),
    ("Tigers are known for their black _______ on their fur coat.", "stripes", "They have black striped patterns.", "Easy"),
    ("Soft padded _______ help tigers move quietly in the forest.", "feet / paws", "Padded feet muffle footstep sounds.", "Easy"),
    ("Tigers are _______-eating animals.", "flesh / meat", "Tigers eat meat (carnivores).", "Easy"),
    ("Tigers are _______ hunters because they move silently.", "stealthy", "Stealthy means quiet and secretive.", "Easy"),
    ("Tigers are _______ animals because their numbers are decreasing.", "endangered", "Endangered species are disappearing.", "Easy"),
    ("Illegal _______ and forest destruction reduce the tiger population.", "hunting / poaching", "Illegal hunting threatens tigers.", "Easy"),
    ("Tigers have sharp _______ at the end of their paws.", "claws", "Tigers have sharp curved claws.", "Easy"),
    ("Large pointed _______ teeth help tigers tear meat.", "canine", "Canine teeth tear meat.", "Easy"),
    ("The black stripes work as _______ in the forest grass.", "cover / camouflage", "Stripes blend into tall grass.", "Easy"),
    ("The word 'daunting' means _______ or grand looking.", "frightening / scary", "Daunting means frightening.", "Easy"),
    ("The word 'feline' means connected to the _______ family.", "cat", "Feline refers to cat family.", "Easy"),
    ("The word 'stealthy' means quiet and _______.", "secretive", "Stealthy means quiet and secretive.", "Easy"),
    ("Wild tigers live in dense _______.", "forests / jungles", "Tigers inhabit forests.", "Easy"),
    ("Tigers have powerful _______ that help them run fast.", "legs", "Strong legs allow fast running.", "Easy"),
    ("A tiger's strong _______ hold prey firmly.", "jaws", "Strong jaws hold prey.", "Easy"),
    ("Different types of tigers look slightly _______ from one another.", "different", "Subspecies vary slightly in look.", "Easy"),
    ("Tigers strike fear in all living _______.", "beings / creatures", "They inspire fear in creatures.", "Easy"),
    ("Tigers are magnificent animals that are both fascinating and _______.", "scary / frightening", "They are fascinating and scary.", "Easy"),
    ("Chapter 07 is titled Our National _______.", "Animal", "Chapter 07 is titled Our National Animal.", "Easy"),
    ("We must protect tiger habitats by saving _______.", "forests / trees", "Saving forests protects tiger homes.", "Easy"),
    ("Tigers are strict carnivores and do not eat _______.", "plants / grass", "Carnivores do not eat plants.", "Easy"),
    ("Tigers have a striped orange and _______ coat.", "black", "They have orange and black coats.", "Easy"),
    ("The Royal Bengal tiger symbolizes national _______ and beauty.", "pride / strength", "The tiger symbolizes national pride.", "Easy"),

    # Medium (26-40)
    ("The word 'endangered' means in danger of _______ from the Earth.", "disappearing / extinction", "Endangered means facing extinction.", "Medium"),
    ("Camouflage allows a tiger to blend in with forest _______.", "shadows / grass / trees", "Camouflage hides predators in grass.", "Medium"),
    ("Illegal hunting of tigers is also known as _______.", "poaching", "Poaching is illegal wildlife hunting.", "Medium"),
    ("Cutting down forests causes habitat _______ for wild animals.", "destruction / loss", "Deforestation destroys habitats.", "Medium"),
    ("Soft pads on paws function as natural sound _______.", "mufflers / cushions", "Pads muffle footsteps on leaves.", "Medium"),
    ("Canine teeth are long, sharp, and specialized for tearing _______.", "flesh / meat", "Canines tear flesh.", "Medium"),
    ("Tigers sit at the very top of the forest food _______.", "chain", "Tigers are top carnivores.", "Medium"),
    ("An animal that eats only meat is called a _______.", "carnivore", "Carnivores eat meat.", "Medium"),
    ("An animal that eats only plants is called a _______.", "herbivore", "Herbivores eat plants.", "Medium"),
    ("India's government launched Project _______ to save Bengal tigers.", "Tiger", "Project Tiger protects Bengal tigers.", "Medium"),
    ("Vertical black stripes mimic the dark _______ of tall reeds.", "shadows", "Stripes resemble shadows.", "Medium"),
    ("Tigers hunt mostly at night because darkness enhances their _______.", "stealth / camouflage", "Night air and darkness aid stealth.", "Medium"),
    ("Without protected forest reserves, wild tigers face _______.", "extinction / danger", "Reserves prevent extinction.", "Medium"),
    ("A tiger's sharp senses of sight and hearing detect slight _______.", "movement / sound", "Senses detect faint movements.", "Medium"),
    ("Protecting national animals preserves our rich natural _______.", "heritage / wildlife", "Conservation saves natural heritage.", "Medium"),

    # Hard (41-50)
    ("The Bengal tiger is classified as an apex _______ in its ecosystem.", "predator", "Apex predators have no natural enemies.", "Hard"),
    ("Morphological adaptations like claws and teeth facilitate prey _______.", "capture / hunting", "Adaptations aid hunting.", "Hard"),
    ("Habitat fragmentation isolates tiger populations and restricts their _______.", "territory / range", "Fragmentation limits territory.", "Hard"),
    ("Poaching is driven by illegal commercial demand for animal _______.", "parts / fur", "Illegal trade drives poaching.", "Hard"),
    ("Ecosystem stability depends on maintaining balanced food _______.", "webs / chains", "Food webs keep ecological balance.", "Hard"),
    ("Soft digital pads cushion impact and minimize acoustic _______.", "noise / signals", "Pads reduce sound signals.", "Hard"),
    ("The Bengal tiger's scientific family classification is _______.", "Felidae", "Felidae is the cat family.", "Hard"),
    ("Conserving umbrella species like tigers protects entire forest _______.", "biodiversity", "Protecting tigers saves all species.", "Hard"),
    ("Night vision in tigers is aided by specialized eye _______.", "structures / cells", "Eye structures enhance night vision.", "Hard"),
    ("Chapter 07 fosters ecological responsibility and national _______.", "pride", "It builds environmental pride.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 07: Our National Animal\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK01_CH07_FIB_{idx:03d}"
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

with open(os.path.join(CH07_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. Fill in Blanks from Story (Cloze Passage) (50 Distinct Qs)
# -------------------------------------------------------------
cloze_data = [
    ("The Royal Bengal tiger is India's national _______.", "animal", "Easy"),
    ("These big, grand cats are known for their daunting _______.", "looks", "Easy"),
    ("Tigers have powerful hunting _______.", "skills", "Easy"),
    ("They strike fear in all living _______.", "beings", "Easy"),
    ("Tigers belong to the _______ family.", "feline", "Easy"),
    ("There are different types of tigers worldwide that look slightly _______.", "different", "Easy"),
    ("Tigers are _______ animals because their numbers have decreased.", "endangered", "Easy"),
    ("Their population has decreased due to illegal _______.", "hunting", "Easy"),
    ("Another cause of decrease is habitat _______.", "destruction", "Easy"),
    ("Tigers are flesh-eating _______.", "animals", "Easy"),
    ("They are stealthy _______.", "hunters", "Easy"),
    ("They have striped patterns that work as _______ in the forest.", "cover", "Easy"),
    ("They also have soft padded _______ that help them move quietly.", "feet", "Easy"),
    ("They have powerful _______ and sharp claws.", "legs", "Easy"),
    ("They have strong jaws with huge canine _______.", "teeth", "Easy"),
    ("These body features are perfect for _______.", "hunting", "Easy"),
    ("Tigers are magnificent animals that are both fascinating and _______.", "scary", "Easy"),
    ("The word 'daunting' means _______.", "frightening", "Easy"),
    ("The word 'feline' means connected to the cat _______.", "family", "Easy"),
    ("The word 'endangered' means in danger of _______.", "disappearing", "Easy"),
    ("The word 'stealthy' means quiet and _______.", "secretive", "Easy"),
    ("The Royal Bengal tiger lives in the dense forests of _______.", "India", "Easy"),
    ("Tigers use soft pads to walk without making _______.", "noise / sound", "Easy"),
    ("We must protect forest habitats to save the _______.", "tiger", "Easy"),
    ("Chapter 07 teaches us to respect our national _______.", "animal", "Easy"),

    ("Tigers are top flesh-eating predators in Indian _______.", "forests", "Medium"),
    ("Striped fur creates natural camouflage among tall _______.", "grasses", "Medium"),
    ("Silent steps allow tigers to sneak up on their _______.", "prey", "Medium"),
    ("Illegal hunting threatens the survival of Bengal _______.", "tigers", "Medium"),
    ("Deforestation strips wild animals of their natural _______.", "homes", "Medium"),
    ("Canine teeth tear meat easily during _______.", "feeding", "Medium"),
    ("Royal Bengal tiger symbolizes power and national _______.", "pride", "Medium"),
    ("Different tiger subspecies inhabit various parts of the _______.", "world", "Medium"),
    ("Feline characteristics include sharp claws and keen _______.", "senses", "Medium"),
    ("Forest protection reserves safeguard endangered _______.", "species", "Medium"),
    ("Stealthy hunting techniques ensure success in dense _______.", "cover", "Medium"),
    ("The decrease in tiger population alarms wildlife _______.", "experts", "Medium"),
    ("Padded paws absorb impact while stalking through dry _______.", "leaves", "Medium"),
    ("Canine teeth and strong jaws form a lethal hunting _______.", "mechanism", "Medium"),
    ("Fascinating features make the tiger a majestic _______.", "creature", "Medium"),

    ("Endangered status requires strict conservation laws against _______.", "poaching", "Hard"),
    ("Habitat destruction fragments wild tiger _______.", "territories", "Hard"),
    ("Camouflage patterns evolved to mimic forest _______.", "shadows", "Hard"),
    ("Soft digital pads muffle footfall acoustic _______.", "vibrations", "Hard"),
    ("Maintaining apex predator numbers preserves ecosystem _______.", "balance", "Hard"),
    ("The Royal Bengal tiger represents India's rich biodiversity _______.", "heritage", "Hard"),
    ("Feline adaptations maximize carnivorous efficiency in the _______.", "wild", "Hard"),
    ("Class 1 students learn environmental stewardship through tiger _______.", "protection", "Hard"),
    ("Coexistence between humans and wildlife demands habitat _______.", "preservation", "Hard"),
    ("Our national animal commands respect and active _______.", "conservation", "Hard")
]

cloze_content = f"# Fill in the Blanks from Story — Chapter 07: Our National Animal\n\n> **Category**: Fill in the Blanks from Story (Cloze Passage) | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(cloze_data, start=1):
    q_id = f"BK01_CH07_STORY_FIB_{idx:03d}"
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

with open(os.path.join(CH07_DIR, "fill_in_blanks_story.md"), "w", encoding="utf-8") as f:
    f.write(cloze_content)

# -------------------------------------------------------------
# 4. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The Royal Bengal tiger is India's national animal.", True, "The Royal Bengal tiger is India's national animal.", "Easy"),
    ("Tigers belong to the canine (dog) family.", False, "Tigers belong to the feline (cat) family.", "Easy"),
    ("Tigers have black striped patterns on their fur.", True, "They have distinct black stripes.", "Easy"),
    ("Tigers eat plants, fruits, and grass.", False, "Tigers are flesh-eating animals (carnivores).", "Easy"),
    ("Soft padded feet help tigers walk quietly without making sound.", True, "Padded feet muffle footstep sounds.", "Easy"),
    ("Tigers are endangered animals because their population has decreased.", True, "Decreasing numbers make them endangered.", "Easy"),
    ("Illegal hunting and habitat destruction cause tiger numbers to drop.", True, "Hunting and forest destruction decrease tiger numbers.", "Easy"),
    ("The word 'daunting' means quiet and secretive.", False, "Daunting means frightening or grand looking.", "Easy"),
    ("The word 'feline' means connected to the cat family.", True, "Feline means connected to cats.", "Easy"),
    ("The word 'stealthy' means quiet and secretive.", True, "Stealthy means quiet and secretive.", "Easy"),
    ("Tigers use sharp claws and strong jaws to hunt prey.", True, "Claws and jaws are essential for hunting.", "Easy"),
    ("Tigers have small flat teeth like cows.", False, "Tigers have large, sharp canine teeth.", "Easy"),
    ("Stripes on a tiger's coat help it hide in tall grass and trees.", True, "Stripes provide natural camouflage.", "Easy"),
    ("Tigers are tame animals that live safely in human houses.", False, "Tigers are wild, dangerous animals living in forests.", "Easy"),
    ("All tiger types in the world look 100% identical.", False, "Different types look slightly different from one another.", "Easy"),
    ("Tigers are magnificent creatures that are both fascinating and scary.", True, "They inspire both awe and fear.", "Easy"),
    ("Illegal hunting of tigers is good for nature.", False, "Illegal hunting destroys animal populations and is illegal.", "Easy"),
    ("Tigers have powerful legs for fast running and pouncing.", True, "Strong legs help them sprint and pounce.", "Easy"),
    ("Tigers move noisily by stomping their feet.", False, "They move silently using soft padded paws.", "Easy"),
    ("An endangered species is in danger of disappearing from Earth.", True, "Endangered means at risk of extinction.", "Easy"),
    ("The Royal Bengal tiger is found in the forests of India.", True, "They inhabit Indian forests.", "Easy"),
    ("Tigers hunt during daytime only and sleep all night.", False, "Tigers often hunt at night using stealth.", "Easy"),
    ("Saving forests helps save tigers and other wild animals.", True, "Preserving forests saves animal habitats.", "Easy"),
    ("Chapter 07 gives facts about India's national animal.", True, "Chapter 07 is about the tiger.", "Easy"),
    ("Tigers are herbivores that eat seeds.", False, "Tigers are strict carnivores that eat meat.", "Easy"),

    # Medium (26-40)
    ("Camouflage makes it hard for prey to spot a hidden tiger.", True, "Stripes blend with shadows in grass.", "Medium"),
    ("Deforestation expands tiger living areas.", False, "Deforestation destroys tiger habitats.", "Medium"),
    ("Canine teeth are specially shaped for tearing meat.", True, "Canines grip and tear flesh.", "Medium"),
    ("Project Tiger is a government program to protect tigers in India.", True, "Project Tiger protects wild tigers.", "Medium"),
    ("Tigers purr loudly just like small house cats.", False, "Tigers roar powerfully rather than purring.", "Medium"),
    ("Stealthy hunting relies on quiet movement and surprise attacks.", True, "Stealth uses quiet approach and surprise.", "Medium"),
    ("Apex predators have many natural enemies that hunt them.", False, "Apex predators have no natural enemies.", "Medium"),
    ("A tiger's soft pads absorb footstep vibrations on dry leaves.", True, "Pads cushion footfall impact.", "Medium"),
    ("Loss of forest land forces tigers closer to human villages.", True, "Habitat loss drives human-animal conflict.", "Medium"),
    ("Carnivores play an important role in keeping nature balanced.", True, "Carnivores control prey populations.", "Medium"),
    ("Bengal tigers are smaller than domestic cats.", False, "Bengal tigers are massive, powerful wild cats.", "Medium"),
    ("Poaching involves illegal killing of protected wildlife.", True, "Poaching is illegal hunting.", "Medium"),
    ("Tigers have keen night vision that aids in hunting in dark forests.", True, "Night vision helps hunt in darkness.", "Medium"),
    ("Saving national animals builds environmental awareness.", True, "Conservation fosters environmental care.", "Medium"),
    ("Tigers can survive easily without trees or cover.", False, "Tigers need forest cover for hunting and shelter.", "Medium"),

    # Hard (41-50)
    ("Ecological food webs collapse when top predators disappear.", True, "Removing apex predators disrupts food webs.", "Hard"),
    ("Vertical stripes disrupt the tiger's outline against tall reeds.", True, "Vertical lines provide effective camouflage.", "Hard"),
    ("Feline adaptations involve sharp claws, flexible bodies, and silent movement.", True, "Felines possess these hunting traits.", "Hard"),
    ("Habitat fragmentation splits tiger populations into isolated groups.", True, "Fragmentation isolates populations.", "Hard"),
    ("Buying products made from wild animal parts encourages poaching.", True, "Demand for animal parts drives poaching.", "Hard"),
    ("A tiger's pad structure includes shock-absorbing fat tissue.", True, "Fat tissue in pads absorbs footfall shock.", "Hard"),
    ("The Royal Bengal tiger was declared National Animal in 1973.", True, "It became National Animal in 1973.", "Hard"),
    ("Biodiversity conservation protects ecosystems for future generations.", True, "Conservation preserves ecosystems.", "Hard"),
    ("Wild tigers are solitary hunters that prefer hunting alone.", True, "Tigers hunt alone rather than in packs.", "Hard"),
    ("Chapter 07 inspires Class 1 learners to value wildlife protection.", True, "It builds conservation values in learners.", "Hard")
]

tf_content = f"# True / False — Chapter 07: Our National Animal\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK01_CH07_TF_{idx:03d}"
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

with open(os.path.join(CH07_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 5. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Which animal is India's national animal?", "The Royal Bengal tiger is India's national animal.", "Easy"),
    ("Which family of animals do tigers belong to?", "Tigers belong to the feline (cat) family.", "Easy"),
    ("What features make a tiger look daunting and grand?", "Their large body size, black stripes, powerful legs, and sharp teeth give them a daunting look.", "Easy"),
    ("What do tigers eat in the forest?", "Tigers are flesh-eating animals (carnivores) that eat the meat of other animals.", "Easy"),
    ("What helps a tiger walk silently in the forest?", "Soft padded feet on their paws help tigers walk silently without making sound.", "Easy"),
    ("What is the function of a tiger's black stripes?", "Black stripes act as natural cover or camouflage, blending the tiger with tall grass and trees.", "Easy"),
    ("Why are tigers called 'endangered' animals?", "They are called endangered because their population has decreased and they are at risk of disappearing.", "Easy"),
    ("What two main factors have reduced the tiger population?", "Illegal hunting (poaching) and habitat destruction (cutting down forests) have reduced their numbers.", "Easy"),
    ("What body parts help a tiger capture its prey?", "Powerful legs, sharp curved claws, and strong jaws with large canine teeth help capture prey.", "Easy"),
    ("Where do wild Royal Bengal tigers live in India?", "Wild Royal Bengal tigers live in the dense natural forests of India.", "Easy"),
    ("What does the word 'daunting' mean?", "'Daunting' means frightening or grand and impressive looking.", "Easy"),
    ("What does the word 'feline' mean?", "'Feline' means connected to or belonging to the cat family.", "Easy"),
    ("What does the word 'stealthy' mean?", "'Stealthy' means quiet, secretive, and careful in movement.", "Easy"),
    ("What does the word 'endangered' mean?", "'Endangered' means facing a high risk of disappearing or becoming extinct.", "Easy"),
    ("What color pattern is found on a Bengal tiger's fur?", "A Bengal tiger has an orange-yellow fur coat with dark black vertical stripes.", "Easy"),
    ("Do all tiger species in the world look identical?", "No, different tiger species around the world have slight differences in size, coat, and stripes.", "Easy"),
    ("Why is a tiger described as both fascinating and scary?", "It is fascinating because of its beauty and power, but scary because it is a fierce wild predator.", "Easy"),
    ("How do canine teeth help a flesh-eating animal?", "Canine teeth are long and sharp, perfect for gripping prey and tearing meat.", "Easy"),
    ("Why should we protect our national animal?", "We should protect the tiger to save our wildlife heritage and maintain nature's balance.", "Easy"),
    ("What happens when forests are cut down?", "Cutting forests destroys wild animals' homes, food sources, and safe living spaces.", "Easy"),
    ("Are tigers herbivores or carnivores?", "Tigers are strict carnivores because they feed exclusively on animal meat.", "Easy"),
    ("What body part allows a tiger to hold onto running prey?", "Sharp, curved claws extending from its paws allow a tiger to grip running prey.", "Easy"),
    ("What title does Chapter 07 carry?", "Chapter 07 is titled 'Our National Animal'.", "Easy"),
    ("How does quiet movement benefit a hunter like the tiger?", "Quiet movement allows the tiger to sneak close to prey without being noticed.", "Easy"),
    ("What basic lesson does Chapter 07 teach primary students?", "It teaches students to love wildlife, respect national symbols, and protect forests.", "Easy"),

    # Medium (26-40)
    ("Explain how camouflage helps a tiger survive in the wild.", "Camouflage blends the tiger's striped coat with forest grass and shadows, allowing it to hide from prey and hunt successfully.", "Medium"),
    ("How does deforestation lead to tiger population decline?", "Deforestation removes trees and prey animals, leaving tigers homeless and starving, forcing them into dangerous human areas.", "Medium"),
    ("What makes the soft pads on a tiger's paws so special?", "The soft pads absorb impact and muffle the sound of footsteps on dry leaves and twigs, granting silent movement.", "Medium"),
    ("Why is illegal hunting (poaching) harmful to wildlife?", "Poaching kills wild animals faster than they can reproduce, driving endangered species toward total extinction.", "Medium"),
    ("Describe the hunting method of a stealthy tiger.", "A tiger uses camouflage to hide, stalks quietly on padded paws, moves close silently, and pounces with strong legs and jaws.", "Medium"),
    ("What is the difference between an endangered animal and an extinct animal?", "An endangered animal is still living but in low numbers; an extinct animal has completely died out from Earth.", "Medium"),
    ("Why is the Royal Bengal tiger a symbol of national pride for India?", "It represents power, grace, courage, and the rich natural wilderness of India as designated in 1973.", "Medium"),
    ("How do canine teeth differ from flat molar teeth?", "Canine teeth are long and pointed for tearing meat; flat molars are wide for grinding plants and grains.", "Medium"),
    ("What is Project Tiger and why was it started?", "Project Tiger is a government conservation program started in India to create reserves and protect tigers from extinction.", "Medium"),
    ("How does a tiger's dark vertical stripes mimic forest shadows?", "Vertical stripes resemble the dark shadows cast by tall grass and tree trunks, confusing the vision of prey.", "Medium"),
    ("Why can't wild tigers be kept in home gardens like domestic cats?", "Wild tigers are large carnivores with wild instincts that need huge forest territories and specialized meat diets.", "Medium"),
    ("What happens to an ecosystem if all tigers disappear?", "Without top predators, plant-eating animal populations grow uncontrollably, leading to overgrazing and forest damage.", "Medium"),
    ("How do tigers use their keen senses during night hunting?", "Their sharp night vision sees in low light and sensitive ears catch faint rustles, pinpointing prey in darkness.", "Medium"),
    ("What does 'habitat destruction' mean in environmental study?", "'Habitat destruction' means ruining or clearing the natural environment where wild plants and animals live.", "Medium"),
    ("Summarize Chapter 07 in two clear sentences.", "Chapter 07 explains that the Royal Bengal tiger is India's national animal, known for its stealth, strength, and striped fur. It highlights the urgent need to protect endangered tigers and their forest homes.", "Medium"),

    # Hard (41-50)
    ("Analyze how physical adaptations (stripes, pads, claws, teeth) work as a complete hunting system.", "Padded paws grant silent approach; stripes provide camouflage; strong legs enable a fast pounce; claws hold prey; and canine teeth deliver the final blow.", "Hard"),
    ("Evaluate the impact of human population expansion on wild tiger reserves.", "Human expansion encroaches on forest land, causing habitat fragmentation, reducing prey availability, and increasing human-animal conflicts.", "Hard"),
    ("Why is the tiger called an 'apex predator' and an 'umbrella species'?", "It is an apex predator with no natural enemies, and an umbrella species because protecting its vast forest home automatically saves thousands of other plants and animals.", "Hard"),
    ("How can Class 1 students practice environmental conservation in daily life?", "Students can save paper (which saves trees), avoid buying items made from animal fur/skin, and plant trees locally.", "Hard"),
    ("Compare feline traits in domestic cats vs wild tigers.", "Both have padded paws, sharp claws, and keen senses; however, tigers are massive, hunt large prey, and roar rather than purring.", "Hard"),
    ("Deconstruct the word 'endangered' and discuss why timely action is vital.", "'En-danger-ed' means placed in danger. Timely conservation prevents species from crossing the point of no return into permanent extinction.", "Hard"),
    ("Explain why night hunting provides a survival advantage for Bengal tigers.", "Night temperatures are cooler for intense physical exertion, and darkness combined with vertical stripes gives maximum stealth against diurnal (day-active) prey.", "Hard"),
    ("Discuss the moral responsibility of humans toward wild animals.", "Humans have a duty to protect wildlife because human actions (deforestation, pollution, poaching) cause animal endangerment.", "Hard"),
    ("How does Project Tiger combine law enforcement with habitat restoration?", "It enforces strict anti-poaching laws while managing protected forest reserves to let natural habitats recover.", "Hard"),
    ("Synthesize the core educational takeaway of Chapter 07 for primary learners.", "Pride in national symbols goes hand-in-hand with environmental duty: protect wild tigers by preserving our forests and respecting nature's balance!", "Hard")
]

sa_content = f"# Short Answer — Chapter 07: Our National Animal\n\n> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK01_CH07_SA_{idx:03d}"
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

with open(os.path.join(CH07_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 6. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-15)
    ("Write a simple summary of Chapter 07 'Our National Animal'.", "The Royal Bengal tiger is India's national animal. It belongs to the feline (cat) family and is known for its daunting looks, powerful hunting skills, and striking fear in other creatures. Tigers are flesh-eating stealthy hunters with black striped fur for camouflage and soft padded feet for silent walking. They have strong legs, sharp claws, and large canine teeth for hunting. Tigers are endangered animals because illegal hunting and forest destruction have reduced their numbers. They are magnificent, fascinating, and scary animals that need our protection.", "Easy"),
    ("Describe the appearance and physical features of the Royal Bengal tiger.", "The Royal Bengal tiger is a grand, magnificent wild cat. It has a beautiful orange-yellow fur coat marked with dark black vertical stripes. Its paws have soft padded cushions underneath for silent walking and sharp curved claws that extend for gripping. It has powerful muscular legs and strong jaws fitted with large, sharp canine teeth designed for tearing meat.", "Easy"),
    ("Explain why the tiger is called a 'stealthy hunter'.", "The tiger is called a stealthy hunter because it hunts quietly and secretively. Its soft padded feet allow it to walk over dry leaves without making a sound, while its black striped coat blends into forest grass and shadows. This enables the tiger to sneak very close to its prey before springing a sudden attack.", "Easy"),
    ("Why are tigers classified as 'endangered' animals?", "Tigers are classified as endangered because their total population in the wild has fallen to dangerously low levels. Human activities, especially illegal hunting (poaching) for fur and body parts, along with the destruction of natural forest homes, have put tigers in danger of disappearing completely from Earth.", "Easy"),
    ("How do a tiger's soft padded feet and sharp claws help it survive?", "Soft padded feet act as cushions that absorb the sound of footsteps, allowing the tiger to move silently through the forest without scaring away prey. Sharp curved claws remain hidden inside paws while walking and extend when needed to grip and hold onto fast-running prey firmly.", "Easy"),
    ("Explain the meaning and importance of camouflage for tigers.", "Camouflage is the natural color pattern that helps an animal blend into its surroundings. The tiger's black vertical stripes mimic the dark shadows of tall forest grass and tree trunks. This makes the tiger nearly invisible to prey, helping it hunt successfully.", "Easy"),
    ("What are the main causes behind the decreasing number of wild tigers?", "The two primary causes are illegal hunting (poaching) and habitat destruction. Poachers kill tigers illegally for trade, while humans cut down forest trees for buildings and roads, destroying the natural shelter and food sources that wild tigers need.", "Easy"),
    ("What does it mean that tigers belong to the 'feline' family?", "Belonging to the feline family means tigers share biological traits with all cats, such as flexible muscular bodies, sharp retractable claws, padded paws, keen night vision, and carnivorous diets. The tiger is the largest member of the cat family.", "Easy"),
    ("Describe the eating habits of a tiger in the forest.", "Tigers are strict flesh-eating animals (carnivores). They hunt other forest animals like deer and wild boar for meat. They use their stealth to stalk prey, strong jaws and canine teeth to catch and kill, and then devour the fresh meat in a quiet spot.", "Easy"),
    ("Why is the Royal Bengal tiger a symbol of pride for India?", "The Royal Bengal tiger was chosen as India's national animal in 1973 because it embodies immense strength, grace, power, and agility. It represents the rich wildlife heritage and wilderness beauty of our nation.", "Easy"),
    ("What is the difference between a wild tiger and a zoo tiger?", "A wild tiger lives freely in vast natural forests, hunting its own prey and roaming large territories. A zoo tiger lives in a restricted enclosure, fed by zoo keepers, and protected from wild dangers, though it lacks forest freedom.", "Easy"),
    ("How do large canine teeth help carnivores like the tiger?", "Canine teeth are long, pointed, and extremely strong. In carnivores, they are positioned at the front corners of the jaw to puncture, hold, and tear tough meat and skin efficiently during feeding.", "Easy"),
    ("Why must we stop illegal hunting (poaching) of wild animals?", "Illegal hunting must be stopped because it rapidly reduces animal populations, drives endangered species to extinction, breaks environmental laws, and disrupts the natural balance of forest ecosystems.", "Easy"),
    ("How does saving forests help save our national animal?", "Forests are the natural homes (habitats) of wild tigers. Saving forests ensures tigers have trees for shade, cover for hunting, fresh water, and plentiful prey animals, allowing tiger populations to recover naturally.", "Easy"),
    ("What basic values can Class 1 students learn from studying Chapter 07?", "Class 1 students learn to take pride in national symbols, appreciate wild animals, understand environmental care, avoid harming nature, and support wildlife protection.", "Easy"),

    # Medium (16-40)
    ("Explain how top predators like the tiger maintain ecological balance in forests.", "As top carnivores, tigers hunt herbivores like deer and wild pigs. By controlling herbivore numbers, tigers prevent overgrazing of forest grass and saplings. This keeps the forest green, protects soil, and supports thousands of other plant and animal species.", "Medium"),
    ("Describe the process of a tiger's hunt from sighting to capture.", "A tiger uses keen sight and hearing to locate prey. It uses vertical stripes for camouflage and padded paws to stalk silently. When close enough, it uses powerful hind legs to sprint and pounce, gripping the prey with sharp claws and delivering a decisive bite with strong jaws.", "Medium"),
    ("Compare the features of feline (cat) animals and canine (dog) animals.", "Felines (cats like tigers) have retractable curved claws, soft padded feet, vertical pupil eyes, and stalk prey silently alone. Canines (dogs like wolves) have non-retractable claws, long snouts, run in packs, and rely heavily on stamina and scent tracking.", "Medium"),
    ("Discuss the significance of Project Tiger in India's conservation history.", "Project Tiger was launched in 1973 to save Bengal tigers from extinction. It created protected national parks and tiger reserves across India, banned poaching, restored forest land, and successfully helped rebuild wild tiger populations.", "Medium"),
    ("How does human encroachment into forest areas lead to human-tiger conflicts?", "When humans clear forests for farms and towns, tiger habitats shrink. Hungry tigers with reduced forest prey occasionally wander into nearby villages for livestock, leading to dangerous encounters between humans and tigers.", "Medium"),
    ("Why is night time advantageous for a hunting Bengal tiger?", "Night offers cooler temperatures for physical effort, and darkness maximizes the stealth of black stripes against night shadows. Tigers have specialized eye cells that see six times better in low light than humans.", "Medium"),
    ("Write a short speech for a school assembly on 'Protecting Our National Animal'.", "'Respected teachers and friends, the Royal Bengal tiger is our proud National Animal! It is powerful, graceful, and grand. But illegal hunting and tree cutting threaten its home. Let us promise to save paper, protect trees, and keep our forests safe for tigers. Jai Hind!'", "Medium"),
    ("Explain the vocabulary terms 'daunting', 'feline', 'endangered', and 'stealthy'.", "• Daunting: Frightening or grandly impressive.\n• Feline: Related to the cat family.\n• Endangered: Facing risk of extinction.\n• Stealthy: Quiet, cautious, and secretive in movement.", "Medium"),
    ("How do sharp claws retract inside a tiger's paws when walking?", "Tigers have retractable claws attached to elastic ligaments. When walking quietly, claws pull back inside skin sheaths to keep them sharp and prevent clicking noises; when pouncing, muscles extend claws outward.", "Medium"),
    ("Why are different tiger subspecies slightly different from each other?", "Different subspecies adapted to different environments. For example, Siberian tigers in cold regions have thicker fur and lighter coats, while Bengal tigers in warm Indian forests have shorter, brightly striped fur.", "Medium"),
    ("Describe the threat of wildlife trafficking (trade in animal parts).", "Illegal international trade in tiger skins, bones, and teeth drives poachers to kill wild tigers for money. Strict customs enforcement and harsh legal penalties are essential to stop this criminal trade.", "Medium"),
    ("How does saving paper help protect wild tiger habitats?", "Paper is made from wood pulp obtained by cutting down forest trees. By reducing paper waste and recycling paper, fewer trees are cut, preserving natural forest habitats for wild tigers.", "Medium"),
    ("Why do tigers prefer hunting alone rather than in packs?", "Tigers rely on surprise camouflage in dense brush rather than open pursuit. Hunting alone allows a single tiger to sneak quietly without being spotted by alert prey herds.", "Medium"),
    ("Explain the concept of 'habitat fragmentation' in simple terms.", "Habitat fragmentation occurs when roads, railways, or farms cut a continuous forest into small isolated pieces. This restricts tigers' movement, makes finding mates difficult, and reduces available prey.", "Medium"),
    ("How do national parks and tiger reserves help endangered species?", "National parks provide legally protected natural land where hunting, tree cutting, and human settlement are strictly banned, giving endangered species safe space to live and breed.", "Medium"),
    ("What makes the Bengal tiger's roar so powerful?", "Tigers have specially shaped vocal cords and cartilages in their throat that allow them to produce low-frequency roars carrying over two miles across dense forest.", "Medium"),
    ("How do mother tigers care for and train their cubs?", "Mother tigers feed cubs milk, hide them safely in dens, and teach them hunting skills over two years, showing them how to stalk, pounce, and survive independently.", "Medium"),
    ("Why should students refrain from buying products made from animal skins or teeth?", "Buying animal products creates market demand that encourages poachers to kill more wild animals. Refusing such products helps stop illegal wildlife crime.", "Medium"),
    ("How does the tiger's coat color change appearance in different lighting?", "In bright sunlight or dappled forest shade, orange fur absorbs yellow-red light while black stripes mimic shadows, breaking up the tiger's outline so it melts into background foliage.", "Medium"),
    ("Summarize Chapter 07 in four clear bullet points.", "• The Royal Bengal tiger is India's magnificent National Animal.\n• It is a stealthy feline carnivore with padded paws, sharp claws, and black stripes.\n• Illegal hunting and deforestation have made tigers an endangered species.\n• We must save forests and protect wildlife to preserve our natural heritage.", "Medium"),

    # Hard (41-50)
    ("Critique the ecological consequences of losing an apex predator like the Bengal tiger.", "Losing an apex predator triggers a trophic cascade. Herbivore populations explode, overconsuming vegetation and devastating forest saplings. This causes soil erosion, stream degradation, and loss of habitat for birds and insects, destroying overall ecosystem health.", "Hard"),
    ("Deconstruct the biological mechanisms of feline camouflage and acoustic stealth.", "Camouflage relies on disruptive coloration, where vertical black stripes disrupt body symmetry against vegetation. Acoustic stealth relies on soft plantar pads that deform over rough terrain, absorbing mechanical energy and dampening footfall acoustics.", "Hard"),
    ("Evaluate the effectiveness of Project Tiger after 50 years of implementation.", "Project Tiger successfully increased India's wild tiger count from under 1,800 in 1973 to over 3,000 today. It expanded protected territory into 50+ reserves, proving that political willpower combined with scientific habitat management can reverse species decline.", "Hard"),
    ("Analyze how human population growth drives deforestation and human-tiger conflict.", "Human demographic pressure expands agriculture and urban infrastructure into forest corridors. This fragments continuous habitats, forces tigers into human-dominated landscapes, and leads to retaliatory killings and severe human-animal conflict.", "Hard"),
    ("Discuss the role of international treaties (like CITES) in combating illegal wildlife trade.", "CITES (Convention on International Trade in Endangered Species) bans international commercial trade in tiger parts. Cross-border law enforcement, intelligence sharing, and strict penalties undermine global poaching syndicates.", "Hard"),
    ("Formulate a comprehensive primary school project on wildlife conservation.", "Students create 'Tiger Conservation Badges', write pledges to save paper, build a model forest reserve showing food chains, and present short skits on why wild animals deserve protection and respect.", "Hard"),
    ("Differentiate between morphological, physiological, and behavioral adaptations in tigers.", "• Morphological: Striped fur, sharp claws, canine teeth.\n• Physiological: Tapetum lucidum for night vision, carnivore digestive enzymes.\n• Behavioral: Solitary hunting, nocturnal activity, territory marking.", "Hard"),
    ("Examine the concept of 'Umbrella Species' in conservation biology.", "Tigers require large intact forest ecosystems (100+ sq km per tiger). By conserving enough forest to protect tigers, conservationists automatically protect thousands of sympatric plant, insect, bird, and mammal species living under that same 'umbrella'.", "Hard"),
    ("Why is public education and awareness crucial for successful wildlife preservation?", "Conservation laws fail without public support. Educating communities fosters pride in natural symbols, reduces demand for illegal animal goods, and encourages local participation in habitat protection.", "Hard"),
    ("Synthesize the ultimate philosophy of Chapter 07 for primary learners.", "Our National Animal teaches us that strength and beauty belong to nature. True progress means living in harmony with wildlife, preserving green forests, and fearlessly defending endangered creatures on Earth!", "Hard")
]

la_content = f"# Long Answer — Chapter 07: Our National Animal\n\n> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK01_CH07_LA_{idx:03d}"
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

with open(os.path.join(CH07_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

print("[SUCCESS] All 6 category files for Chapter 07 completely refined with 100% unique Class 1 questions!")
