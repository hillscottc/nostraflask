import logging
import random
from datetime import date, timedelta

from utils import choose_from, choose_uniq, sentence_case, ing_to_ed, an
from word_lists.default_library import default_library, Mood

log = logging.getLogger(__name__)


def get_words(name, library=default_library):
    """
    Get a named word list from library module.
    """
    return library[name]


def generate():
    """
    Generate a three to four sentence horoscope.
    """
    # Pick a mood (usually positive)
    mood = Mood.GOOD if random.random() <= 0.8 else Mood.BAD

    discussion_s = choose_from([relationship, encounter])
    sentences = [feeling_statement_s, warning_s, discussion_s]

    # Select 2 or 3 sentences
    k = random.randint(2, 3)
    sentences = random.sample(sentences, k)
    final_text = " ".join([sentence(mood) for sentence in sentences])

    # Optionally add a date prediction
    # if random.random() <= 0.5 and k == 2:
    #     final_text += " " + date_prediction_s(mood, dirty)
    # Always add a date prediction
    final_text += " " + date_prediction_s()

    log.info(final_text)

    return final_text


def relationship(mood):
    """
    Generate a sentence about a relationship.
    """
    if mood == Mood.GOOD:
        verb = "strengthened"
        talk = "discussion"
    else:
        verb = "strained"
        talk = "argument"

    # Wordlists
    # familiar_people = wordlist("familiar_people", alt_words)
    # conversation_topics = wordlist("conversation_topics", alt_words)

    familiar_people = get_words("familiar_people")
    conversation_topics = get_words("conversation_topics")

    person = choose_from(familiar_people)
    topic = choose_from(conversation_topics)
    s = "Your relationship with %s may be %s " % (person, verb)
    s += "as the result of %s about %s" % (an(talk), topic)

    return sentence_case(s)


def encounter(mood=Mood.NEUTRAL):
    """
    Generate a few sentences about a meeting with another person.
    """

    # if mood not in ['good', 'bad', '']:
    #     raise ValueError("Invalid mood option.")

    # Sentence 1: The meeting
    familiar_people = get_words("familiar_people")
    strange_people = get_words("strange_people")
    locations = get_words("locations")

    person = choose_from(familiar_people, strange_people)
    location = choose_from(locations)
    preposition = location[0]
    location = location[1]
    s1 = "You may meet %s %s %s." % (person, preposition, location)

    # Sentence 2: The discussion
    discussions = get_words("neutral_discussions")
    discussions += get_words(mood + "_discussions")
    feeling_nouns = get_words(mood + "_feeling_nouns")
    emotive_nouns = get_words(mood + "_emotive_nouns")
    conversation_topics = get_words("conversation_topics")

    discussion = choose_from(discussions)
    if random.random() <= 0.5:
        feeling = choose_from(feeling_nouns)
        feeling = "feelings of %s" % feeling
    else:
        feeling = choose_from(emotive_nouns)
    topic = choose_from(conversation_topics)

    s2 = "%s about %s may lead to %s." % (an(discussion), topic, feeling)
    s2 = sentence_case(s2)
    return "%s %s" % (s1, s2)


def date_prediction_s():
    """
    Generate a random prediction sentence containing a date.
    """
    days_in_future = random.randint(2, 8)
    significant_day = date.today() + timedelta(days=days_in_future)
    month = significant_day.strftime("%B")
    day = significant_day.strftime("%d").lstrip('0')

    r = random.random()

    if r <= 0.5:
        s = "%s %s will be an important day for you" % (month, day)
    elif r <= 0.8:
        s = "Interesting things await you on %s %s" % (month, day)
    else:
        s = "The events of %s %s have the potential to change your life." % (month, day)

    return sentence_case(s)


def feeling_statement_s(mood):
    """
    Generate a sentence that asserts a mood-based feeling.
    """
    adjectives = get_words(mood + "_feeling_adjs")
    degrees = get_words("neutral_degrees") + get_words(mood + "_degrees")

    adj = choose_from(adjectives)
    adj = ing_to_ed(adj)
    degree = choose_from(degrees)
    ending = positive_intensifier if mood == Mood.GOOD else consolation
    exciting = (mood == Mood.GOOD and random.random() <= 0.5)
    are = random.choice([" are", "'re"])
    s = "You%s feeling %s %s" % (are, degree, adj)
    s += ending()
    return sentence_case(s, exciting)


def positive_intensifier():
    """
    Extend a statement of positive feelings.
    """
    r = random.random()

    if r <= 0.5:
        verb = random.choice(["say", "do"])
        return ", and there's nothing anyone can %s to stop you" % verb
    elif r <= 0.95:
        return ", and you don't care who knows it"
    else:
        return ", and you don't give a damn"


def consolation():
    """
    Provide a consolation for feeling bad.
    """
    r = random.random()

    if r <= 0.6:
        when = random.choice(["shortly", "soon", "in due time"])
        return ", but don't worry, everything will improve %s" % when
    elif r <= 0.9:
        return ", perhaps you need a change in your life?"
    else:
        return "..."


def warning_s(*args):
    r = random.random()
    avoid_list = get_words("avoid_list")
    bad_thing = random.choice(avoid_list)

    if r <= 0.27:
        s = "You would be well advised to avoid %s" % bad_thing
    elif r <= 0.54:
        s = "Avoid %s at all costs" % bad_thing
    elif r <= 0.81:
        s = "Steer clear of %s for a stress-free week"  % bad_thing
    else:
        also_bad = choose_uniq({bad_thing}, avoid_list)
        s = "For a peaceful week, avoid %s and %s" % (bad_thing, also_bad)

    return sentence_case(s)


def emotive_event(mood):
    """
    Generate a sentence about a prolonged emotion.
    """
    feeling_adjs = get_words(mood + "_feeling_adjs")
    emotive_adjs = get_words(mood + "_emotive_adjs")
    feeling_nouns = get_words(mood + "_feeling_nouns")
    emotive_nouns = get_words(mood + "_emotive_nouns")
    time_periods = get_words("time_periods")
    time_period = random.choice(time_periods)

    if random.random() <= 0.5:
        adj = choose_from(feeling_adjs, emotive_adjs)
        return "%s %s" % (adj, time_period)
    else:
        noun = choose_from(feeling_nouns, emotive_nouns)
        return "%s of %s" % (time_period, noun)


