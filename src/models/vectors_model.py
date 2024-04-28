from gensim.models import KeyedVectors


class VectorsModelException(Exception):
    pass


class VectorsModelNotInitializedException(VectorsModelException):
    pass


class VectorsModel:

    def __init__(self):
        self._initialized: bool = False
        self._model: KeyedVectors | None = None

    def init_model(self, path: str) -> None:
        self._model = KeyedVectors.load_word2vec_format(path)
        self._initialized = True

    def is_initialized(self) -> bool:
        return self._initialized

    def calculate_distance(self, phrase1: str, phrase2: str) -> float:
        if not self._initialized or self._model is None:
            raise VectorsModelNotInitializedException
        pairs = []
        for word1 in phrase1.split():
            for word2 in phrase2.split():
                pairs.append((word1, word2))
        distances = []
        for pair in pairs:
            try:
                distances.append(self._model.distance(*pair))
            except KeyError:
                continue
        return sum(distances) / len(distances)


vector_model = VectorsModel()
