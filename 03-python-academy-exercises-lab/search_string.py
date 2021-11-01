wiki_text = """
Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[31]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[32]

Guido van Rossum began working on python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting. Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.[34]

Python consistently ranks as one of the most popular programming languages.
"""

if __name__ == '__main__':
    text = wiki_text.replace("\n", "")
    text_lower = text.lower()
    print(text)
    serch_str = "Python".lower()
    pos = 0
    stop = False
    while pos >= 0:
        pos = text_lower.find(serch_str, pos)
        if pos >= 0 :
            print(pos, "->", text[pos:pos + len(serch_str)])
            pos += 1