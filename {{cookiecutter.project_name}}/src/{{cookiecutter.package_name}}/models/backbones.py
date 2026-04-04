from transformers import CLIPModel


def load_backbone(backbone_type: str, model_name: str):
    if backbone_type == "clip":
        model = CLIPModel.from_pretrained(model_name)
        feature_dim = model.config.projection_dim
        return model, feature_dim

    raise ValueError(f"Unsupported backbone_type: {backbone_type}")
