from abc import ABC, abstractmethod

class Publication(ABC):
    def __init__(self, id: int = None, title: str = None, author: str = None, year: int = None, summary=None, keywords: tuple[str]=(),):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__year = year
        self.__summary = summary
        self.__keywords = keywords

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def summary(self):
        return self.__summary
    @summary.setter
    def summary(self, summary):
        self.__summary = summary

    @property
    def keywords(self):
        return self.__keywords
    @keywords.setter
    def keywords(self, keywords):
        self.__keywords = keywords

    def __str__(self):
        return f'{self.id}: {self.__title} ({self.__year}) - {self.__author} - {self.__summary} {self.__keywords}'

    @abstractmethod
    def __repr__(self):
        pass

class Book(Publication):
    def __init__(self, id: int = None, title: str=None, author: str=None, year:int = None, summary: str=None, keywords: tuple[str]=(),
                 isbn: str = None, publisher: str=None):
        super().__init__(id, title, author, year, summary, keywords)
        self.__isbn = isbn
        self.__publisher = publisher

    @property
    def isbn(self):
        return self.__isbn
    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def publisher(self):
        return self.__publisher
    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

    def __str__(self):
        return super().__str__() + f'{self.__isbn} - {self.__publisher}'
    def __repr__(self):
        return f'Book({self.id}, {self.title}, {self.author}, {self.summary}, {self.keywords}, {self.isbn}, {self.__publisher})'

class Paper(Publication):
    def __init__(self, id: int = None, title: str=None, author: str=None, year:int = None, summary: str=None, keywords: tuple[str]=(),
                 proc: str = None, pages: str=None):
        super().__init__(id, title, author, year, summary, keywords)
        self.__proc = proc
        self.__pages = pages

    @property
    def proc(self):
        return self.__proc
    @proc.setter
    def proc(self, proc):
        self.__proc = proc

    @property
    def pages(self):
        return self.__pages
    @pages.setter
    def pages(self, pages):
        self.__pages = pages

    def __str__(self):
        return super().__str__() + f'{self.__proc} - pp.{self.__pages}'
    def __repr__(self):
        return f'Paper({self.id}, {self.title}, {self.author}, {self.summary}, {self.keywords}, {self.__proc}, {self.__pages})'

if __name__ == '__main__':
    b1 = Book(1, 'Fluent Python', 'Luciano Ramalho', 2015,
                     'Python’s simplicity lets you become productive quickly, but this often means you aren’t using everything it has to offer. With this hands-on guide, you’ll learn how to write effective, idiomatic Python code by leveraging its best—and possibly most neglected—features. Author Luciano Ramalho takes you through Python’s core language features and libraries, and shows you how to make your code shorter, faster, and more readable at the same time.',
                     ('python', 'programming'), 1491946253, "O'Reilly Media, Inc.")
    p1 = Paper(2, 'WavTokenizer: an Efficient Acoustic Discrete Codec Tokenizer for Audio Language Modeling',
               'Shengpeng Ji, Ziyue Jiang, Xize Cheng, Yifu Chen, Minghui Fang, Jialong Zuo, Qian Yang, RuiQi Li, Ziang Zhang, Xiaoda Yang, Rongjie Huang, Yidi Jiang, Qian Chen, Siqi Zheng, Wen Wang, Zhou Zhao',
               2024, 'Language models have been effectively applied to modeling natural signals, such as images, video, speech, and audio. A crucial component of these models is the codec tokenizer, which compresses high-dimensional natural signals into lower-dimensional discrete tokens. In this paper, we introduce WavTokenizer, which offers several advantages over previous SOTA acoustic codec models in the audio domain: 1)extreme compression. By compressing the layers of quantizers and the temporal dimension of the discrete codec, one-second audio of 24kHz sampling rate requires only a single quantizer with 40 or 75 tokens. 2)improved subjective quality. Despite the reduced number of tokens, WavTokenizer achieves state-of-the-art reconstruction quality with outstanding UTMOS scores and inherently contains richer semantic information. Specifically, we achieve these results by designing a broader VQ space, extended contextual windows, and improved attention networks, as well as introducing a powerful multi-scale discriminator and an inverse Fourier transform structure. We conducted extensive reconstruction experiments in the domains of speech, audio, and music. WavTokenizer exhibited strong performance across various objective and subjective metrics compared to state-of-the-art models. We also tested semantic information, VQ utilization, and adaptability to generative models. Comprehensive ablation studies confirm the necessity of each module in WavTokenizer. The related code, demos, and pre-trained models are available at https://github.com/jishengpeng/WavTokenizer.',
               ('audio', 'language', 'modeling', 'tokenizer', 'PyTorch') )
    p2 = Paper(3, 'Explainable Person Re-Identification with Attribute-guided Metric Distillation',
               'Xiaodong Chen, Xinchen Liu, Wu Liu, Xiao-Ping Zhang, Yongdong Zhang, Tao Mei',
               2021, 'Despite the great progress of person re-identification (ReID) with the adoption of Convolutional Neural Networks, current ReID models are opaque and only outputs a scalar distance between two persons. There are few methods providing users semantically understandable explanations for why two persons are the same one or not. In this paper, we propose a post-hoc method, named Attribute-guided Metric Distillation (AMD), to explain existing ReID models. This is the first method to explore attributes to answer: 1) what and where the attributes make two persons different, and 2) how much each attribute contributes to the difference. In AMD, we design a pluggable interpreter network for target models to generate quantitative contributions of attributes and visualize accurate attention maps of the most discriminative attributes. To achieve this goal, we propose a metric distillation loss by which the interpreter learns to decompose the distance of two persons into components of attributes with knowledge distilled from the target model. Moreover, we propose an attribute prior loss to make the interpreter generate attribute-guided attention maps and to eliminate biases caused by the imbalanced distribution of attributes. This loss can guide the interpreter to focus on the exclusive and discriminative attributes rather than the large-area but common attributes of two persons. Comprehensive experiments show that the interpreter can generate effective and intuitive explanations for varied models and generalize well under cross-domain settings. As a by-product, the accuracy of target models can be further improved with our interpreter.',
               ('identification', 'cnn', 'explainable', 'metric'), 'ICCV 2021', '11813-11822' )
    publications = [b1, p1, p2]
    for publication in publications:
        print(repr(publication))
