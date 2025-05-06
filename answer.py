class Answer:
    """
    Answer

    @param text: The answer text.
    @param score: The answer score.
    """

    def __init__(self, text: str, score: int) -> None:
        self.text: str = text
        self.score: int = score
