import os
import random
import time
import sys
def render(text, args, header='', footer=''):
    if 'speak' in args:
        os.system('say ' + text)
    else:
        print header + text + footer
class English_language:
    def __init__(self):
        self.nouns = ['boy','girl','cat', 'dog', 'apple', 'jew', 'tomato', 'chamber', 'Hitler', 'computer', 'library', 'bookshelf', 'book', 'mouse', 'elephant', 'wall', 'floor', 'outlet', 'poster', 'glass', 'logo', 'officer', 'firetruck', 'humidifier', 'pen', 'pencil', 'fork', 'spoon', 'hospital', 'house', 'lightbulb', 'crab', 'robot', 'Donald Trump', 'Adrian', 'language', 'music', 'table', 'mirror', 'lunchbox', 'orange', 'bag', 'backpack', 'lunchbox', 'paper', 'printer', 'grapefruit', 'artwork', 'pencil', 'animal','earbuds', 'headphones', 'fire fighter', 'fire', 'bottle' 'mosque', 'temple', 'pool', 'beach', 'fiction', 'fantasy']
        self.verbs = ['get', 'consume', 'eat', 'swallow', 'devour', 'burn', 'gas', 'photograph', 'drink', 'type', 'read', 'destroy', 'explode', 'strike', 'smash', 'crush', 'mash', 'electrocute', 'shock', 'incinerate', 'break']
        self.indirect_verbs = ['sing', 'run', 'walk', 'jump', 'swim', 'look', 'drink', 'read', 'write']
        self.prepositions = ['over', 'through', 'about', 'under', 'in', 'around']
        self.adjectives = ['hungry', 'round', 'purple', 'blue', 'small', 'huge', 'red', 'green', 'orange', 'pink', 'dark', 'angry', 'depressed', 'laughing', 'crazy', 'dumb', 'awesome', 'cold', 'hot', 'warm', 'hurt', 'light']
        self.adverbs = ['quickly', 'suddenly', 'often', 'slowly', 'rapidly', 'spontaneously', 'voraciously', 'rarely', 'unexpectedly', 'unfortunately']
        self.articles = ['the', 'a']
        self.relative_pronouns = ['that', 'which']
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.system_commands = ['SYSTEM$ quit']
        self.obscenity = ['gorram']
    def ornate_noun(self):
        noun = random.choice(self.nouns)
        choice = random.randint(0,2)
        end_text = ''
        article = random.choice(self.articles) if not noun[0].capitalize() == noun[0] else ''

        #choice = random.randint(0,2)
        adjectives = ''
        if choice == 2:
            for_range = range(random.randint(1,3))
            for i in for_range:
                adjectives += ' ' + random.choice(self.adjectives)
                if i < len(for_range)-1:
                    adjectives += ','
        #print adjectives
        if choice == 2:
            end_text += ' ' + ('an' if (adjectives[1] in self.vowels) else 'a') if article == 'a' else article
            #print 'used adj'
        else:
            end_text += ' ' + ('an' if (noun[0] in self.vowels) else 'a') if article == 'a' else article
        end_text += adjectives
        end_text += ' ' + noun
        return end_text[1:] if end_text[0] == ' ' else end_text
    def ornate_verb(self):
        end_text = ''
        choice = random.randint(0,2)
        end_text = ''
        if choice == 2:
            end_text += ' ' + random.choice(self.adverbs)
        verb = random.choice(self.verbs + self.indirect_verbs)
        end_text += ' ' + verb + ('es' if verb.endswith('s') or verb.endswith('sh') else 's') + (' ' + random.choice(self.prepositions) if verb in self.indirect_verbs else '')
        return end_text[1:]
    def clause(self):
        end_text = ''
        end_text += ' ' + self.ornate_noun().capitalize()
        end_text += ' ' + self.ornate_verb()
        end_text += ' ' + self.ornate_noun()
        if random.randint(0,1) == 1:
            end_text += ' ' + random.choice(self.relative_pronouns)
            verb = random.choice(self.verbs)
            end_text += ' ' + verb + ('es' if verb.endswith('s') or verb.endswith('sh') else 's')
        if random.randint(0,1) == 1:
            clause = self.clause()
            #print clause
            end_text += '. ' + clause[0].title() + clause[1:]
        else:
            end_text += '.'
        return end_text[1:]
language = English_language()
if 'verbose' in sys.argv:
    render('\x1b[0;31;48mSuccessfully loaded English!\x1b[0m',sys.argv)
    render('\x1b[0;31;48mGenerating text...\x1b[0m', sys.argv)
sentence = language.clause()
if 'verbose' in sys.argv:
    render('Complete!', sys.argv, '\x1b[0;31;48m', '\x1b[0m')
if 'converse' in sys.argv:
    render('BEGIN CONVERSATION:', sys.argv, '\x1b[0;31;48m', '\x1b[0m')
    while True:
        try:
            question = raw_input('\x1b[0;34;48mYou: \x1b[0m ')
            if question in language.obscenity:
                sentence = ''
                for i in range(0, random.randint(0, 40)):
                    sentence += random.choice(language.obscenity) + ' '
            if question in language.system_commands:
                sys.exit()
        except:
            render('English: ', sys.argv, '\n\x1b[0;31;48m', '\x1b[0mGTG bye!')
            sys.exit()
    #for i in range(0,5):

        render('English: ', sys.argv, '\x1b[0;31;48m', '\x1b[0m' + sentence)
        sentence = language.clause()

render(sentence, sys.argv, '\x1b[0;39;48m' + '\x1b[0m')
#time.sleep(3)
#os.system('osascript -e 'tell app \'system events\' to keystroke \'/tts ' + sentence.replace('\'', ',') + '\''')
#os.system('say ' + sentence)
#verb = random.choice(language.verbs)
