from openvino.runtime import Core

class TextEmbeddingOpenVINO:
    def __init__(self, model_path="model.xml"):
        ie = Core()
        self.model = ie.read_model(model_path)
        self.compiled_model = ie.compile_model(self.model, "CPU")
        self.input_layer = self.compiled_model.input(0)
        self.output_layer = self.compiled_model.output(0)

    def infer(self, input_ids, attention_mask):
        result = self.compiled_model(
            {
                self.input_layer.any_name: input_ids,
                "attention_mask": attention_mask
            }
        )
        return result[self.output_layer]