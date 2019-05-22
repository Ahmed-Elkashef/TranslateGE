# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Word, Base

engine = create_engine('sqlite:///words.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# German Words

Kaufen = Word(
                vocabulary_word='kaufen',
                translated_word='to buy',
                wordtype="v", vocabulary_word_pron="kaufen",
                primary_def="When you Kauft something, you pay money in order to own it. "
                +"You might buy your wife a bouquet of flowers for your anniversary.",
                primary_def_example="Ich werde heute ein neues Auto kaufen.",
                word_family_1st="abkaufen", word_family_2nd="aufkaufen", word_family_3rd="einkaufen",
                word_family_4th=u"Zurückkaufen", word_family_5th="Nachkaufen")
session.add(Kaufen)
session.commit()

Klausurergebnisse = Word(
                    vocabulary_word='Klausurergebnisse',
                    translated_word='Exam Results',
                    wordtype="v", vocabulary_word_pron="Klausur-ergebnisse",
                    primary_def="Klausur is what you go for in the final study period to be examined of all the material you have learned throughout the semester. Ergibnes is the result of that Klausur.",
                    primary_def_example="Wann sind die Klausurergebnisse fertig?")
session.add(Klausurergebnisse)
session.commit()

"""
Katze = Word(vocabulary_word='katze', short_description="What's another name for the four-legged feline that"
+" lies around on your keyboard all day and purrs? You might call it 'Fluffy,' but it's also known"
+" as a cat.", long_description="If you're in the market for a pet cat, just make sure it meows, "
+"and doesn't roar like the lion, tiger, or jaguar, all of which are in the same family as the"
+" housecat. Domesticated as long ago as ancient Egyptian times, the cat is a fixture not only in"
+" many homes, but also in a host of English expressions - like, 'when the cat's away, the mice"
+" will play,' 'it's raining cats and dogs,' and 'the cat's pajamas.'")
session.add(Katze)
session.commit()

Katalog = Word(vocabulary_word='katalog', short_description="A catalog is a book that lists many things: the"
+" most common type of catalog is for a store.", long_description="A catalog is an organized list that"
+" appears in book or pamphlet form. The Sears catalog tells you all the things you can buy at Sears,"
+" along with pictures of the items and what they cost. But you can also use catalog to mean any kind"
+" of listing. In an argument, you might say, 'Why don't you just make a catalog of all my faults!' "
+"When you're making a catalog of any kind, you're cataloging.")
session.add(Katalog)
session.commit()

Konkret = Word(vocabulary_word='konkret', short_description="Concrete is that pourable mix of cement,"
+" water, sand, and gravel that hardens into a super-strong building material. Sidewalks, foundations,"
+" and highways are all made of concrete.", long_description="Though people use the words cement and"
+" concrete as if they were the same, they're not. Concrete has cement in it, but also includes other"
+" materials; cement is what binds concrete together. Construction workers hate when kids write their"
+" names in concrete before it hardens: once concrete hardens, it's going to be solid for a long time."
+" When used as an adjective, concrete also means solid. If you've got concrete plans for Saturday,"
+" then you have a definite plan.")
session.add(Konkret)
session.commit()
"""

print("added words!")
