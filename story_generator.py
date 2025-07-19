import random
from transformers import pipeline

story_generator = pipeline("text-generation", model="gpt2")

def generate_story(prompt, max_length=200, num_return_sequences=1):
    stories = story_generator(
        prompt,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True
    )
    return [story['generated_text'] for story in stories]

def create_story():
    prompts = [
        "Once upon a time in a faraway land,",
        "In a bustling city, a mysterious stranger arrived.",
        "Deep in the enchanted forest, a secret lay hidden.",
        "On a stormy night, a letter arrived that changed everything.",
        "In a world where dreams and reality intertwine, a hero emerges."
    ]
    selected_prompt = random.choice(prompts)
    story = generate_story(selected_prompt)
    return selected_prompt, story[0]

def main():
    print("Welcome to the Story Generator!")
    while True:
        input("Press Enter to generate a story...")
        prompt, story = create_story()
        print(f"\nPrompt: {prompt}\n")
        print("Story:\n", story)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
