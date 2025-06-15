from datasets import load_dataset

def load_bengali_dataset(task="summarization"):
    if task == "summarization":
        dataset = load_dataset("csebuetnlp/xlsum", "bn")
    elif task == "classification":
        dataset = load_dataset("ai4bharat/indic-classification", "bn")
    else:
        raise ValueError("Unknown task")
    return dataset
