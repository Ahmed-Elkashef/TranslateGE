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
                primary_def="When you Kauft something, you pay money in order to own it. You might buy your wife a bouquet of flowers for your anniversary.",
                primary_def_example="Ich werde heute ein neues Auto kaufen.",
                syn1="einkaufen",syn2="ankaufen",ant1="verkaufen",ant2="boykottieren",
                word_family_1st="abkaufen", word_family_1st_pron="ab-kaufen",
                word_family_box1_primary_def="To buy something from someone. The addition of 'ab' here gives the meaning 'from'", word_family_box1_primary_def_example="Ich kann dir keinen Whiskey abkaufen.",
                word_family_2nd="aufkaufen", word_family_2nd_pron="auf-kaufen",
                word_family_box2_primary_def="To buy up, take over ownership of corporations and shares of a company or a piece of land.", word_family_box2_primary_def_example="Er kaufte alle Aktien der Firma auf.",
                word_family_3rd="einkaufen", word_family_3rd_pron="ein-kaufen",
                word_family_box3_primary_def="To buy something in the context of shopping / doing the groceries, purchasing for the daily needs.", word_family_box3_primary_def_example="Wir gehen einmal pro Woche einkaufen.",
                word_family_4th=u"Zurückkaufen", word_family_4th_pron=u"Zurück-kaufen",
                word_family_box4_primary_def="To buy back what has been sold / lost / given away.", word_family_box4_primary_def_example=u"ich will den Schmuck zurückkaufen, den ich dir verkaufte.",
                other_meaning1="to bribe", other_meaning1_def="to pay money illegally in order to get something that isn't yours.", other_meaning1_def_example="der Sieg war gekauft.",
                other_meaning1_syn1="bestechen", other_meaning1_ant1=u"entschädigen")
session.add(Kaufen)
session.commit()

Klausurergebnisse = Word(
                    vocabulary_word='Klausurergebnis',
                    translated_word='Exam Results',
                    wordtype="v", vocabulary_word_pron="Klausur-ergebnis",
                    primary_def="Klausor: a test or an exam, Ergebnis: Result. Klausur is what you go for in the final study period to be examined of all the material you have learned throughout the semester. Ergibnes is the result of that Klausur.",
                    primary_def_example="Wann sind die Klausurergebnisse fertig?",
                    syn1=u"Prüfungsergebnisse",
                    word_family_1st="ergebnis", word_family_1st_pron="ergebnis",
                    word_family_box1_primary_def="", word_family_box1_primary_def_example="",
                    word_family_2nd="Klausur", word_family_2nd_pron="Klausur",
                    word_family_box2_primary_def="", word_family_box2_primary_def_example="",
                    other_meaning1="", other_meaning1_def="", other_meaning1_def_example="",
                    other_meaning2="", other_meaning2_def="", other_meaning2_def_example="",
                    other_meaning3="", other_meaning3_def="", other_meaning3_def_example="",
                    other_meaning4="", other_meaning4_def="", other_meaning4_def_example="",)
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
