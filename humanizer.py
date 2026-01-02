import random
import re

class HumanizerEngine:
    """Transforms AI-generated text to appear human-written by injecting natural variation."""
    
    def __init__(self):
        # AI-typical phrases to replace
        self.ai_phrases = {
            "it is important to note": ["notably", "worth mentioning", "interestingly"],
            "furthermore": ["also", "plus", "and", "besides"],
            "moreover": ["also", "plus", "what's more", "and"],
            "consequently": ["so", "thus", "as a result", "therefore"],
            "in conclusion": ["to wrap up", "in summary", "overall", "finally"],
            "it can be argued": ["some say", "arguably", "one might say"],
            "research suggests": ["studies show", "evidence indicates", "data reveals"],
            "comprehensive": ["thorough", "complete", "detailed", "full"],
            "utilize": ["use", "employ", "apply"],
            "leverage": ["use", "exploit", "harness"],
            "paradigm": ["model", "framework", "approach"],
            "delve": ["explore", "examine", "look into"],
            "nuanced": ["subtle", "complex", "intricate"],
        }
        
        # Contractions to inject
        self.contractions = {
            "it is": "it's", "that is": "that's", "there is": "there's",
            "do not": "don't", "does not": "doesn't", "did not": "didn't",
            "cannot": "can't", "could not": "couldn't", "would not": "wouldn't",
            "should not": "shouldn't", "will not": "won't", "are not": "aren't",
            "is not": "isn't", "was not": "wasn't", "were not": "weren't",
            "have not": "haven't", "has not": "hasn't", "had not": "hadn't"
        }
    
    def inject_burstiness(self, sentences):
        """Vary sentence lengths dramatically to create human-like burstiness."""
        result = []
        i = 0
        while i < len(sentences):
            action = random.choice(['keep', 'merge', 'split'])
            
            if action == 'merge' and i < len(sentences) - 1 and len(sentences[i].split()) < 15:
                # Merge two short sentences
                merged = sentences[i].rstrip('.!?') + ', and ' + sentences[i+1][0].lower() + sentences[i+1][1:]
                result.append(merged)
                i += 2
            elif action == 'split' and len(sentences[i].split()) > 20:
                # Split long sentence
                words = sentences[i].split()
                mid = len(words) // 2
                part1 = ' '.join(words[:mid]) + '.'
                part2 = ' '.join(words[mid:])
                result.extend([part1, part2])
                i += 1
            else:
                result.append(sentences[i])
                i += 1
        
        return result
    
    def replace_ai_phrases(self, text):
        """Replace AI-typical phrases with natural alternatives."""
        for ai_phrase, alternatives in self.ai_phrases.items():
            if ai_phrase in text.lower():
                replacement = random.choice(alternatives)
                # Case-sensitive replacement
                text = re.sub(re.escape(ai_phrase), replacement, text, flags=re.IGNORECASE)
        return text
    
    def add_contractions(self, text):
        """Inject natural contractions."""
        for full, contracted in self.contractions.items():
            if random.random() > 0.5:  # 50% chance to contract
                text = re.sub(r'\b' + re.escape(full) + r'\b', contracted, text, flags=re.IGNORECASE)
        return text
    
    def add_natural_variation(self, text):
        """Add occasional fragments, questions, and informal touches."""
        sentences = re.split(r'(?<=[.!?])\s+', text)
        result = []
        
        for i, sent in enumerate(sentences):
            # Occasionally add a question
            if random.random() > 0.9 and len(sent.split()) > 8:
                sent = sent.rstrip('.') + '?'
            
            # Occasionally add emphasis
            if random.random() > 0.95:
                sent = sent.rstrip('.!?') + '!'
            
            result.append(sent)
        
        return ' '.join(result)
    
    def humanize(self, text):
        """Main humanization pipeline."""
        if not text or len(text.strip()) < 50:
            return text
        
        # Step 1: Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        # Step 2: Inject burstiness
        sentences = self.inject_burstiness(sentences)
        
        # Step 3: Rejoin
        text = ' '.join(sentences)
        
        # Step 4: Replace AI phrases
        text = self.replace_ai_phrases(text)
        
        # Step 5: Add contractions
        text = self.add_contractions(text)
        
        # Step 6: Add natural variation
        text = self.add_natural_variation(text)
        
        return text
