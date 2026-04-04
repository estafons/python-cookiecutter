class BaselineClassifier:
    def __init__(self, input_dim: int, hidden_dim: int, num_classes: int) -> None:
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.num_classes = num_classes

    def __repr__(self) -> str:
        return (
            f"BaselineClassifier(input_dim={self.input_dim}, "
            f"hidden_dim={self.hidden_dim}, num_classes={self.num_classes})"
        )
