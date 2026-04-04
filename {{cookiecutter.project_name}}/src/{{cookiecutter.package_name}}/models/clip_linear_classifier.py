class CLIPLinearClassifier:
    def __init__(
        self,
        backbone,
        feature_dim: int,
        num_classes: int,
        freeze_backbone: bool = True,
    ) -> None:
        self.backbone = backbone
        self.feature_dim = feature_dim
        self.num_classes = num_classes
        self.freeze_backbone = freeze_backbone

    def __repr__(self) -> str:
        return (
            f"CLIPLinearClassifier(feature_dim={self.feature_dim}, "
            f"num_classes={self.num_classes}, freeze_backbone={self.freeze_backbone})"
        )
