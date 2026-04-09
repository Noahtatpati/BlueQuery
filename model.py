from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load trained model
model = T5ForConditionalGeneration.from_pretrained("./nl2sql-model")
tokenizer = T5Tokenizer.from_pretrained("./nl2sql-model")

model.eval()

def generate_sql(query):
    input_text = "translate English to SQL: " + query
    inputs = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_length=64,
        num_beams=4,
        do_sample=False
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)