import re

wiki_text = "Python is an interpreted high-level general-purpose programming language. " \
              "Its design philosophy emphasizes code readability with its use of significant indentation. " \
              "Its language constructs as well as its object-oriented approach aim to help programmers write clear, " \
              "logical code for small and large-scale projects.[31] \n" \
              "python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, " \
              "including structured (particularly, procedural), object-oriented and functional programming. " \
              "It is often described as a batteries included " \
              " language due to its comprehensive standard library.[32][33] \n" \
              "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, " \
              "and first released it in 1991 as python 0.9.0.[34] Python 2.0 was released in 2000 and introduced new features, " \
              "such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). " \
              "Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. " \
              "Python 2 was discontinued with version 2.7.18 in 2020.[35]" \
              "Python consistently ranks as one of the most popular programming languages."

if __name__ == "__main__":
    a = """
    Hello \n
    from
    Python!
    """

    b = " ".join(re.split("\s+", a.strip()))
    print(b)
    print(len(b))

    l = list(b)
    l[0] = "R"
    print(l)
    print("".join(l))

    # print python word positions in wikipedia_string
    text_to_lower = wiki_text.lower()
    serch_str = "Python"
    print(f"Python occurances: {text_to_lower.count(serch_str.lower())}")
    pos = 0
    while pos >= 0:
        pos = text_to_lower.find(serch_str.lower(), pos)
        if pos >= 0:
            print(f"Python occurance: {wiki_text[pos: pos + len(serch_str)]} [{pos} - {pos + len(serch_str)}]")
            print("Python occurance: {text} [{start} - {end}]"
                  .format(text = wiki_text[pos: pos + len(serch_str)], start = pos, end = pos + len(serch_str)))
            pos += len(serch_str)
    
