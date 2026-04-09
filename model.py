from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

model.eval()

def generate_sql(query):
    input_text = "translate English to SQL: " + query
    inputs = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_length=64,
        num_beams=4
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
