from datasets import load_dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments

# Load dataset
dataset = load_dataset("json", data_files="data.json")

# Load model
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

def preprocess(example):
    inputs = tokenizer(
        example["input"],
        truncation=True,
        padding="max_length",
        max_length=64
    )

    outputs = tokenizer(
        example["output"],
        truncation=True,
        padding="max_length",
        max_length=64
    )

    labels = outputs["input_ids"]

    # Ignore padding tokens in loss
    labels = [
        token if token != tokenizer.pad_token_id else -100
        for token in labels
    ]

    inputs["labels"] = labels
    return inputs

tokenized = dataset.map(preprocess)

training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=20,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"]
)

trainer.train()

# Save model
model.save_pretrained("./nl2sql-model")
tokenizer.save_pretrained("./nl2sql-model")