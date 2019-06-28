import random


characters = ("Snake", "Liquid", "Solid Snake", "Liquid Snake", "Solidus Snake", "Big Boss", "The Boss", "Raiden",
              "Otacon", "Meryl", "Naomi", "Ocelot", "Revolver Ocelot", "Gray Fox", "Psycho Mantis", "Sniper Wolf",
              "Vulcan Raven", "Decoy Octopus", "Kaz", "Paz", "Roy Campbell", "Mei Ling", "Vamp", "Volgin", "EVA",
              "Johnny", "Olga Gurlukovich", "Sergei Gurlukovich", "Rose", "Fortune", "Fatman", "Emma", "Zero", "Sokolov",
              "Para-Medic", "Sigint", "The Pain", "The Fear", "The End", "The Sorrow", "The Fury", "Raikov", "Sunny",
              "Drebin", "Amanda", "Chico", "Huey", "Coldman", "Zadornov", "Strangelove", "Cécile", "Doktor",
              "Jetstream Sam", "Sundowner", "Mistral", "Monsoon", "Bladewolf", "Armstrong", "Senator Armstrong",
              "Venom Snake", "Skull Face", "Quiet", "DD", "Code Talker", "Metal Gear Rex", "Metal Gear Ray",
              "Sahelanthropus", "Peace Walker", "Norman Reedus", "Outer Heaven", "FOXHOUND", "The Patriots",
              "Philanthropy", "FOX", "Militaires Sans Frontieres", "Cipher", "Diamond Dogs", "FOX", "XOF", "Deepthroat",
              "The La-li-lu-le-lo", "Pequod", "Boss", "Kojima", "Adamska", "Shalashaska", "Jack",
              "this funky freakign bot", )

verbs = ("sneak", "defect", "betray", "hug", "talk", "sleep", "crawl", "flop", "scream", "itch", "meme", "puke",
         "dance", "cry", "laugh", "CQC", "kill", "shoot", "stab", "sing", "lie", "clean", "fly", "play", "swim", "walk",
         "smile", "think", "wash", "punch", "kick", "build", "burn", "carry", "cook", "eat", "forget",
         "remember", "hop", "hate", "love", "jump", "kiss", "practice", "pretend", "ski", "drive", "ride", "stand",
         "sink", "swear", "steal", "suffer", "fight", "slither", "pounce", "claw", "bite", "roll", "run", "bounce",
         "flirt", "pull", "stomp", "push", "throw", "sniff", "fry", "break", "drink", "throw", "sit", "pay", "read",
         "hit", "hurt", "freeze", "boil", "hear", "see", "feel", "taste", "touch", "smell", "bend", "twist", "smoke",
         "Fulton", "deploy", "attach", "meow", "drown", "come", "go", "blink", "pet", "frisk", "pop", "snort", "blow",
         "suck", "chew", "lick", "huff", "chop", "punch", "kick", "slap")

objects = ("bandana", "banana", "orange", "SOCOM", "Hind D", "cardboard box", "egg", "eyepatch", "cigar", "cigarette",
           "Doritos", "Mountain Dew", "C4", "sneaking suit", "trash can", "barrel", "cyborg", "nanomachine", "Colonel",
           "keycard", "stinger missile", "pentazemin", "frying pan", "mech", "sunglasses", "husky", "decoy", "hat",
           "Fulton recovery balloon", "codec", "codec frequency", "cat", "dog", "diamond", "motorcycle", "flower",
           "snake", "frog", "dud", "demon", "fox", "man", "woman", "ocelot", "soldier", "government",
           "tool", "gene", "meme", "country", "fiddle", "AI", "alarm", "surveillance camera", "footprint", "binocular",
           "iDroid", "revolver", "silencer", "the mistake that is Metal Gear Survive", "scissors", "worm", "rock",
           "DNA", "CalorieMate", "grenade", "monkey", "tree", "fence", "border", "anime", "weeb", "boot", "rope", "sock",
           "cryptid", "syringe", "bird", "octopus", "mantis", "boy", "girl", "creature")

adjectives = ("purple", "orange", "red", "yellow", "green", "pink", "white", "black", "gray", "rainbow", "violet",
              "shiny", "dull", "slimy", "wet", "dry", "cute", "ugly", "loud", "noisy", "quiet", "shy", "dangerous",
              "questionable", "delicious", "disgusting", "fluffy", "soft", "cuddly", "sharp", "filthy", "solid",
              "crusty", "warm", "muffled", "chubby", "fat", "huge", "tall", "scrawny", "thin", "tiny", "short",
              "depressed", "nervous", "happy", "excited", "clever", "wild", "bloody", "attractive", "confident",
              "stupid", "smart", "obtuse", "obsolete", "bizarre", "crazy", "slippery", "dismissive", "rude", "old",
              "raw", "fresh", "spicy", "mellow", "bland", "clumsy", "lovely", "sloppy", "adorable", "revolting",
              "awkward", "boring", "dead", "juicy", "freaky", "famous", "lame", "stuffed", "hungry", "flap-jaw",
              "robotic", "pretty", "good", "fancy", "psycho", "little", "big", "old", "offensive", "sad", "livid")


def convert_past_tense(verb):
    if verb == "shoot":
        return "shot"
    elif verb == "sing":
        return "sung"
    elif verb == "swim":
        return "swam"
    elif verb == "think":
        return "thought"
    elif verb == "build":
        return "built"
    elif verb == "burn":
        return "burnt"
    elif verb == "eat":
        return "ate"
    elif verb == "forget":
        return "forgot"
    elif verb == "drive":
        return "drove"
    elif verb == "ride":
        return "rode"
    elif verb == "stand":
        return "stood"
    elif verb == "sink":
        return "sunk"
    elif verb == "swear":
        return "swore"
    elif verb == "steal":
        return "stole"
    elif verb == "fight":
        return "fought"
    elif verb == "run":
        return "ran"
    elif verb == "throw":
        return "threw"
    elif verb == "break":
        return "broke"
    elif verb == "drink":
        return "drank"
    elif verb == "throw":
        return "threw"
    elif verb == "sit":
        return "sat"
    elif verb == "pay":
        return "paid"
    elif verb == "freeze":
        return "froze"
    elif verb == "hear":
        return "heard"
    elif verb == "see":
        return "saw"
    elif verb == "feel":
        return "felt"
    elif verb == "deploy":
        return "deployed"
    elif verb == "come":
        verb == "came"
    elif verb == "go":
        verb == "went"
    elif verb == "hug" or verb == "flop" or verb == "stab" or verb == "hop" or verb == "pet" or verb == "pop"\
            or verb == "chop" or verb == "slap":
        return verb + verb[len(verb) - 1] + "ed"
    elif verb == "read" or verb == "hit" or verb == "hurt":
        return verb
    elif verb.endswith("y"):
        return verb.rstrip("y") + "ied"
    elif verb.endswith("e"):
        return verb + "d"
    else:
        return verb + "ed"


def convert_present_tense(verb):
    if verb == "lie":
        return "lying"
    elif verb == "sing":
        return "singing"
    elif verb == "hug" or verb == "flop" or verb == "stab" or verb == "hop" or verb == "run" or verb == "sit" or \
            verb == "hit":
        return verb + verb[len(verb) - 1] + "ing"
    elif verb.endswith("e"):
        return verb.rstrip("e") + "ing"
    else:
        return verb + "ing"


def convert_plural(item):
    if item == "cardboard box" or item == "eyepatch" or item == "fox":
        return item + "es"
    elif item == "husky":
        return "huskies"
    elif item == "man":
        return "men"
    elif item == "woman":
        return "women"
    elif item == "sunglasses" or item == "pentazemin":
        return item
    else:
        return item + "s"


quote_history = []
object_history = []
character_history = []
verb_history = []
adj_history = []

newObj = ""
newVerb = ""
newAdj = ""
newCharacter = ""


def get_new_obj():
    if len(object_history) > 9:
        object_history.pop(0)
    new_obj = random.choice(objects)
    while object_history.count(new_obj) != 0:
        new_obj = random.choice(objects)
    object_history.append(new_obj)
    return new_obj


def get_new_verb():
    if len(verb_history) > 9:
        verb_history.pop(0)
    new_verb = random.choice(verbs)
    while verb_history.count(new_verb) != 0:
        new_verb = random.choice(verbs)
    verb_history.append(new_verb)
    return new_verb


def get_new_adj():
    if len(adj_history) > 9:
        adj_history.pop(0)
    new_adj = random.choice(adjectives)
    while adj_history.count(new_adj) != 0:
        new_adj = random.choice(adjectives)
    adj_history.append(new_adj)
    return new_adj


def get_new_character():
    if len(character_history) > 9:
        character_history.pop(0)
    new_character = random.choice(characters)
    while character_history.count(new_character) != 0:
        new_character = random.choice(characters)
    character_history.append(new_character)
    return new_character

